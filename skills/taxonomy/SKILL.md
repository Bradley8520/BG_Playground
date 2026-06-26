# Skill: VOC Taxonomy — Build, Edit & Conversion Standards

## When to Use This Skill
Activate when the user says `taxonomy:` or asks to build, edit, convert, audit, or repair a VOC classification taxonomy file.

---

## Active Taxonomy Files

| File | Rows | Scope | Status |
|---|---|---|---|
| `VOC_Classification_Taxonomy_v4.csv` | 239 | All channels | Master — fully repaired, sorted |
| `VOC_Classification_Taxonomy_Care.csv` | 202 | Care + All channels | Active — derived from v4 |

**Column schema:** `Category`, `Category_Definition`, `Topic`, `Topic_Definition`, `Sub_Topic`, `Sub_Topic_Definition`, `Polarity`, `Survey_Channel`, `Est_Count`, `Est_Pct`, `Notes`, `Original Definition`, `Taxonomy`

---

## Definition Format Standard (v4)

All `Sub_Topic_Definition` values follow this structure:

```
[Core concept statement] (including but not limited to: "phrase one," "phrase two," or similar [theme] language). Does NOT apply to: (1) [exclude → routing pointer]. [CO-CLASSIFY annotation.] [TRAILING ANNOTATION.]
```

**Rules:**
- Double quotes `"..."` around every example phrase in the phrase list
- Separate phrases with commas; use `or` before the last phrase
- Phrase list opened with `(including but not limited to:` and closed with `)`
- EXCLUDE clauses use `Does NOT apply to:` with numbered list routing to the more-specific sub-topic
- CO-CLASSIFY annotations direct the LLM to also fire an umbrella sub-topic
- TRAILING ANNOTATIONS appear at the very end (e.g., polarity cues, channel notes)

**Length targets:**
- ≤700 characters — target for all definitions
- >900 characters — trim aggressively; remove redundant phrase examples first, then collapse verbose annotations, then shorten EXCLUDE clauses
- Never remove EXCLUDE clauses or CO-CLASSIFY annotations — they are critical for routing accuracy

---

## Known Gotchas & Anti-Patterns

### ⚠️ APOSTROPHE COLLISION — Bulk Conversion Risk
**What happened (v3 → v4):** A bulk conversion script used the apostrophe character `'` as a phrase delimiter. That same character appears in English contractions (`didn't`, `can't`, `wasn't`, etc.) inside phrase example lists. Result: 57 of 239 definitions were corrupted.

**Three artifact types produced:**
| Type | Broken output example |
|---|---|
| Truncated contraction | `"didn",` `"can",` `"wasn",` `"wouldn",` left in phrase list |
| Dangling text outside `)` | `...or similar language). t know'. Does NOT apply to:...` |
| Severed single character | `"s",` (from `Sam's`) or `"t",` (from `didn't`) |

**Prevention rule:** Any script that splits, parses, or restructures definition text must use a delimiter that **cannot appear in plain English text** — e.g., pipe `|`, tab `\t`, or a multi-character sequence like `;;`. Never use `'`, `"`, `,`, or `.` as delimiters.

**Detection scan (PowerShell):**
```powershell
$rows = Import-Csv $path
$rows | Where-Object {
    $_.Sub_Topic_Definition -match '"didn",|"can",|"wasn",|"couldn",|"wouldn",|"shouldn",|"don",|"won",'
} | Select-Object Sub_Topic
```
Run this after any bulk conversion to catch apostrophe-collision artifacts before they propagate.

---

### ⚠️ .ps1 FILE ENCODING — Unicode Corruption on Windows
**Problem:** Files created via VS Code file tools save as UTF-8, but PowerShell on this Windows system reads `.ps1` files as Latin-1/CP1252. Em dash `—` (U+2014) corrupts to `â€"`. Right arrow `→` (U+2192) also corrupts.

**Rule:** Never save taxonomy edit scripts as `.ps1` files when definitions contain `—` or `→`. Run all multi-definition update commands **inline in the terminal** directly.

**Safe substitutes in scripts only:** Use `--` instead of `—`, and `->` instead of `→`. The CSV file itself can retain the original Unicode characters.

---

### ⚠️ DOLLAR SIGNS IN POWERSHELL STRINGS
In double-quoted PowerShell strings, `$` triggers variable expansion. Definition text containing `$X` (e.g., dollar amounts) must use backtick escape: `` `$X `` or use single-quoted strings `'...'`.

**Internal apostrophes/contractions in single-quoted strings:** double them → `''` (e.g., `'didn''t know'`).

---

### ⚠️ IDENTITY COLLISION — Sub-Topic Named Same as Parent Topic
If a sub-topic has the same name as its parent topic, the LLM conflates them and over-fires the sub-topic.

**Known instance:** Sub-topic `Perceived Trust` inside topic `Perceived Trust - Wrong Information`. Recommended rename: `Rep Was Deceptive / Customer Felt Misled` (deferred as of 2026-06-22).

**Rule:** Sub-topic names must be meaningfully distinct from their parent topic name.

---

## File Save Pattern (Always Use)

```powershell
$path = "...\VOC_Classification_Taxonomy_Care.csv"
$rows = Import-Csv $path

# --- make changes to $rows here ---

$csv = $rows | ConvertTo-Csv -NoTypeInformation
[System.IO.File]::WriteAllLines($path, $csv, (New-Object System.Text.UTF8Encoding $false))
Write-Host "Saved. Rows: $($rows.Count)"
```

- **Always use `WriteAllLines` with `UTF8Encoding $false`** (no BOM)
- Never use `Export-Csv` (may add BOM or alter quoting)
- Never use `Out-File` (encoding unreliable)

---

## Bulk Definition Edit Pattern

```powershell
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
Write-Host "Updated: $updated rows"
```

- Use single-quoted strings for definitions containing double-quoted phrase examples
- Double internal apostrophes: `'didn''t'` → renders as `didn't`
- Run inline in terminal — not from `.ps1` files — when definitions contain Unicode

---

## Channel Scoping

| Survey_Channel value | Meaning |
|---|---|
| `All` | Fires across every channel |
| `Care` | Care (phone/chat) only |
| `IHE` | In-Home Expert only |
| `Retail` | Retail store only |
| `National Retail` | National retail partner only |
| `Care \| IHE` | Care and IHE |
| `Care \| Retail \| National Retail` | Care, Retail, National Retail |
| `Retail \| National Retail` | Retail and National Retail |

**To create a channel-specific file:** filter where `Survey_Channel -eq 'All' -or $_.Survey_Channel -match 'Care'` (substitute target channel name).

---

## LLM Classification Design Principles

- **Multi-label:** A single verbatim can and should fire multiple sub-topics
- **EXCLUDE clauses:** Prevent over-classification into catch-alls when a more specific sub-topic exists — never remove them
- **CO-CLASSIFY (Model A):** Rep Courtesy umbrella — specific courtesy sub-topics instruct the LLM to also fire `Rep Overall Positive` or `Rep Overall Negative`
- **Catch-all sub-topics** (`Rep Overall Positive/Negative`, `Positive/Negative General Customer Service`): should only fire when no specific sub-topic applies — definitions should include minimum-signal threshold language
- **Phrase list language:** Use customer-voice language in examples, not agent/taxonomy language
