# VOC Taxonomy — Care File Build & Definition Repair Handoff

## Status: ✅ SESSION COMPLETE — Care taxonomy file ready for use
**Session Date:** 2026-06-22
**Primary Files:** `VOC_Classification_Taxonomy_v4.csv`, `VOC_Classification_Taxonomy_Care.csv`

---

## 1. WHAT WAS ACCOMPLISHED THIS SESSION

### A. Full Definition Audit & Repair (v4)
- Ran automated scan across all 239 rows of `VOC_Classification_Taxonomy_v4.csv` detecting broken definitions from the v3→v4 bulk conversion
- Identified **57 broken definitions total** (53 automated + 4 manual catch)
- Root cause: the v3→v4 conversion used the apostrophe `'` as a phrase delimiter — the same character used in contractions — causing phrases like `"didn't"` to split into `"didn"` fragment + dangling `t know'.` text outside the parenthetical
- Three artifact types repaired:
  - **(A) Truncated contractions** — `"didn"`, `"can"`, `"wasn"`, `"couldn"`, `"wouldn"`, `"shouldn"`, `"don"`, `"won"` etc. appearing in phrase lists
  - **(B) Dangling text** — text outside closing `)` followed by `'.` and annotation
  - **(C) Severed fragments** — `"s"` (from `Sam's`), `"t"` (from `didn't`)
- Repairs executed in 4 PowerShell chunks (People, Process, Platform/Policy/Pricing/Product)
- All 57 definitions fully restored with correct v4 format

### B. Long Definition Trimming (v4)
- Identified **15 definitions exceeding 700 characters**
- Trimmed all 15 in 2 batch operations (avg ~20% reduction)
- Target: ≤700 chars; achieved on all 15
- See trim results table in prior session handoff or conversation summary for char counts

### C. Full Verification Pass (v4)
- Ran pattern scan for all known broken artifact signatures
- Result: **zero broken patterns detected** across all 239 rows

### D. Sort (v4)
- Sorted `VOC_Classification_Taxonomy_v4.csv` A-Z by Category → Topic → Sub_Topic
- 239 rows confirmed after sort

### E. Care-Channel Taxonomy File Created
- Copied v4 → `VOC_Classification_Taxonomy_Care.csv`
- Filtered to **Care-relevant rows only**: kept `Survey_Channel` = `All`, `Care`, `Care | IHE`, `Care | Retail | National Retail`
- Removed 37 rows scoped to IHE-only, National Retail-only, or Retail-only channels
- **Final row count: 202**

### F. Column Cleanup on Care File
- Renamed legacy `Taxonomy` column → `Original Definition` (preserves original pre-repair definition strings for reference)
- Added new `Taxonomy` column populated with current v4 format: `Sub_Topic->Sub_Topic_Definition`
- Final column order: `Category`, `Category_Definition`, `Topic`, `Topic_Definition`, `Sub_Topic`, `Sub_Topic_Definition`, `Polarity`, `Survey_Channel`, `Est_Count`, `Est_Pct`, `Notes`, `Original Definition`, `Taxonomy`

---

## 2. TAXONOMY ARCHITECTURE — INSIGHTS & BEST PRACTICES

### Definition Format Standard (v4)
All Sub_Topic_Definitions follow this structure:
```
[Core concept statement] (including but not limited to: "phrase one," "phrase two," or similar [theme] language). Does NOT apply to: (1) [exclude → routing pointer]. [CO-CLASSIFY annotation.] [TRAILING ANNOTATION.]
```

**Key format rules:**
- Use double quotes `"..."` around all example phrases in the phrase list
- Separate phrases with commas; use `or` before the last phrase
- Parenthetical phrase list opened with `(including but not limited to:` and closed with `)`.
- EXCLUDE clauses use `Does NOT apply to:` with numbered list pointing to the more-specific sub-topic
- CO-CLASSIFY annotations direct the LLM to also fire an umbrella sub-topic alongside the specific one
- TRAILING ANNOTATIONS appear at the very end (e.g., `[NEGATIVE]`, `[POSITIVE]`, polarity cues)

### Phrase List Best Practices
- Contractions must be written as full words: `"didn't"`, not `"didn"` + dangling `t`
- Dollar signs in PowerShell scripts require backtick escape: `` `$X `` in double-quoted strings
- Em dash `—` and right arrow `→` are valid in the CSV itself but **must not appear in `.ps1` script files** created via file tools — they corrupt on Windows (Latin-1/CP1252 read issue); use `--` and `->` in scripts only, run inline in terminal
- Keep phrase lists to 5–8 representative examples; avoid exhaustive lists that bloat char count
- Phrase list examples should be customer-voice language, not agent/taxonomy language

### Definition Length Guidelines
- **Target: ≤700 characters** for LLM token efficiency and prompt stability
- **Hard warning: >900 characters** — trim aggressively
- Trim strategy: remove redundant phrase examples first, then collapse verbose annotations, then shorten EXCLUDE clauses
- Do NOT remove EXCLUDE clauses entirely — they are critical for routing accuracy
- Do NOT remove CO-CLASSIFY annotations — they drive multi-label behavior

### CO-CLASSIFY Architecture (Model A)
- Rep Courtesy umbrella uses CO-CLASSIFY Model A
- Specific sub-topics (Rep Was Courteous, Rep Not Courteous, Rep Was Impatient, Rep Was Pushy, Rep Hung Up) each instruct the LLM to also fire `Rep Overall Positive` or `Rep Overall Negative` as appropriate
- This creates a two-tier signal: specific + rollup, without requiring separate classification passes

### Polarity Column
- `Positive`, `Negative`, `Neutral`, or `Mixed`
- Used downstream for sentiment aggregation — always set accurately
- Sub-topics that can fire for either polarity (e.g., "Billing Error") should be `Negative`; confirm/resolution sub-topics should be `Positive`

### Survey_Channel Scoping
- Valid values: `All`, `Care`, `IHE`, `Retail`, `National Retail`, `Care | IHE`, `Care | Retail | National Retail`, `Retail | National Retail`
- `All` = fires across every channel
- Pipe-delimited values mean the sub-topic is relevant to multiple but not all channels
- When creating channel-specific taxonomy files, filter: keep rows where `Survey_Channel` equals `All` OR contains the target channel name

### LLM Classification Design Principles
- **Multi-label**: A single verbatim can and should fire multiple sub-topics
- **Exclusion routing**: EXCLUDE clauses prevent over-classification into catch-alls when a more specific sub-topic exists
- **Catch-all sub-topics** (`Rep Overall Positive/Negative`, `Positive/Negative General Customer Service`): should only fire when no specific sub-topic applies — definitions should include minimum-signal language to prevent over-absorption
- **Identity collision risk**: Avoid naming a sub-topic the same as its parent topic — the LLM will conflate them (see deferred item: "Perceived Trust" sub-topic inside "Perceived Trust - Wrong Information" topic)

### File Encoding
- Always save taxonomy CSVs as **UTF-8 no BOM** using `[System.IO.File]::WriteAllLines($path, $csv, (New-Object System.Text.UTF8Encoding $false))`
- Do NOT use `Export-Csv` — it may add BOM or alter quoting
- Do NOT use `Out-File` — encoding unreliable
- `ConvertTo-Csv -NoTypeInformation` → `WriteAllLines` is the safe pattern

### PowerShell Bulk Edit Pattern
```powershell
$path = "...\VOC_Classification_Taxonomy_Care.csv"
$rows = Import-Csv $path

$fixes = @{
    'Sub_Topic_Name_1' = 'corrected definition...'
    'Sub_Topic_Name_2' = 'corrected definition...'
}

$updated = 0
foreach ($row in $rows) {
    if ($fixes.ContainsKey($row.Sub_Topic)) {
        $row.Sub_Topic_Definition = $fixes[$row.Sub_Topic]
        $updated++
    }
}

$csv = $rows | ConvertTo-Csv -NoTypeInformation
[System.IO.File]::WriteAllLines($path, $csv, (New-Object System.Text.UTF8Encoding $false))
Write-Host "Updated: $updated rows"
```
- Use single-quoted strings `'...'` for definitions containing double-quoted examples
- Internal apostrophes/contractions in single-quoted strings: double them → `''` (e.g., `'didn''t'`)
- Run **inline in terminal** — do NOT save as `.ps1` files when definitions contain Unicode characters

---

## 3. DEFERRED ITEMS — TO DO OR DECIDE LATER

### Structural / Architecture

| # | Item | Description | Priority |
|---|---|---|---|
| 1 | **Perceived Trust sub-topic rename** | Sub-topic `Perceived Trust` inside topic `Perceived Trust - Wrong Information` creates LLM identity collision. Recommended rename: `Rep Was Deceptive / Customer Felt Misled` | High |
| 2 | **Inconsistent Information routing** | Currently in `Perceived Trust - Wrong Information` topic, but is arguably a process consistency failure, not a trust/ethics issue. Decide: move to `Cross-Channel Friction` or `Proactive Communication & Transparency`? | Medium |
| 3 | **Catch-all over-absorption** | `Rep Overall Positive/Negative` and `Positive/Negative General Customer Service` may capture too much volume. Add minimum-signal threshold language: "only apply if no specific sub-topic applies and verbatim contains explicit overall sentiment language." | Medium |
| 4 | **Bill Inquiry vs. General Bill** | Two sub-topics in `Bill Inquiry & General Bill` topic: `Bill Inquiry` (asking about the bill) vs. `General Bill` (general mention). Different intents — clarify definitions to sharpen the boundary, or consider whether `General Bill` is a true catch-all vs. duplicate. | Medium |
| 5 | **Rep Was Pushy placement** | Currently in `Rep Courtesy` (People). Was discussed: should it move to `Sales Transparency & Offer Accuracy` (Process)? Deferred. Decide before v4 is finalized for production use. | Low |

### Maintenance / Hygiene

| # | Item | Description |
|---|---|---|
| 6 | **Care file: validate CO-CLASSIFY references** | CO-CLASSIFY annotations in Care file reference umbrella sub-topics — confirm all referenced sub-topics are still present in the 202-row Care file (none were removed in the filter step, but worth spot-checking) |
| 7 | **Return & Exchange Policy** | Two sub-topics exist (`Return / Exchange Was Easy`, `Return Denied / Window Closed`) — verify Survey_Channel is set correctly; these may be store-only and should have been filtered out of Care file |
| 8 | **Est_Count / Est_Pct columns** | Values are estimates from v3 build (87K verbatim sample). Will need refresh when Care VOC data for new periods is run through the classifier |
| 9 | **v4 master file sort** | `VOC_Classification_Taxonomy_v4.csv` was sorted A-Z this session — note that `VOC_Classification_Taxonomy_Care.csv` also reflects this sort order |

---

## 4. FILES CHANGED THIS SESSION

| File | Change | Notes |
|---|---|---|
| `VOC_Classification_Taxonomy_v4.csv` | Modified | All 57 broken definitions repaired; 15 long definitions trimmed; sorted A-Z by Category/Topic/Sub_Topic |
| `VOC_Classification_Taxonomy_Care.csv` | Created | Copy of v4 filtered to Care + All channels (202 rows); `Taxonomy` column renamed to `Original Definition`; new `Taxonomy` column added with `Sub_Topic->Sub_Topic_Definition` format |

---

## 5. NEXT SESSION — PICK UP HERE

1. **Validate CO-CLASSIFY references in Care file** — load Care file, extract all CO-CLASSIFY targets from `Sub_Topic_Definition`, confirm each target sub-topic exists in the file
2. **Decide on Perceived Trust sub-topic rename** — rename `Perceived Trust` → `Rep Was Deceptive / Customer Felt Misled` in both v4 and Care files if approved
3. **Tighten catch-all definitions** — open `Rep Overall Positive`, `Rep Overall Negative`, `Positive General Customer Service`, `Negative General Customer Service` and add minimum-signal threshold language
4. **Run Care file through classify script** — test against `Care_Verbatims_Apr2026_classification_testing.csv` to validate sub-topic distribution and catch any over-firing catch-alls
5. **Refresh Est_Count / Est_Pct** — recompute after first classifier run on Care verbatims
