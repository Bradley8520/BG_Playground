# Taxonomy & Text Classification — Master Skill Reference (DRAFT FOR REVIEW)

> **Purpose:** Review this document and select elements to incorporate into the official `skills/taxonomy/SKILL.md`.
> This is a comprehensive reference covering: plain-English explanations, standard best practices, advanced techniques,
> non-traditional high-impact methods, your documented personal preferences, and a full testing/validation guide.

---

## PART 1 — WHAT THIS IS AND HOW IT WORKS (Plain English)

### What Is a VOC Taxonomy?

A **taxonomy** is an organized list of labeled buckets that describes every meaningful thing a customer might say in a survey. Think of it like a filing system: when a customer writes "the rep was rude and hung up on me," the taxonomy tells the AI model exactly which drawers to file that in — `Rep Not Courteous` AND `Rep Hung Up / Ended Call Prematurely`.

This taxonomy has three levels:
- **Category** — The broadest grouping (e.g., `People`, `Process`, `Pricing`)
- **Topic** — A cluster of related issues within a category (e.g., `Rep Courtesy` inside `People`)
- **Sub_Topic** — The specific, actionable label the model fires (e.g., `Rep Not Courteous`)

### What Does a Definition Actually Do?

The definition is the instruction you give the AI model. It tells the model:
1. What kind of verbatim **qualifies** for this label (with example phrases in customer language)
2. What kinds of verbatims look similar but should **not** get this label (EXCLUDE clauses)
3. Whether it should also fire a **second, related label** at the same time (CO-CLASSIFY)

**The definition is the most powerful lever you have.** A vague definition creates noise. A precise definition creates accurate, trustworthy data.

### How the AI Reads a Label (Zero-Shot NLI)

The model being used (BART-large-mnli or RoBERTa-large-mnli) is a **Natural Language Inference (NLI)** model. It doesn't just match keywords — it asks a logic question:

> *"Does this customer's statement entail (support, imply, or confirm) that [Sub_Topic label] applies?"*

This means:
- The **label name itself matters** — the model reads it as part of the hypothesis
- The **definition** (when passed as context) provides supporting evidence for what the label means
- Vague or overlapping labels create ambiguity because the model can't distinguish between near-synonyms

---

## PART 2 — DEFINITION WRITING STANDARDS (Current v4 Format)

### The Structure (Annotated)

```
[Core concept statement]
(including but not limited to: "phrase one," "phrase two," "phrase three," or similar [theme] language).
Does NOT apply to: (1) [specific exclusion — route to Sub_Topic X instead].
[CO-CLASSIFY instruction.]
[TRAILING ANNOTATION — polarity, channel, or special handling note.]
```

**Every component explained:**

| Component | Purpose | What happens if missing |
|---|---|---|
| Core concept statement | Defines the essential signal the model must detect | Model fires on surface-level keywords, misses the intent |
| Phrase list `(including but not limited to: ...)` | Provides customer-voice examples to anchor the semantic space | Model interprets the label too narrowly or too broadly |
| EXCLUDE clause | Routes near-miss verbatims to the more specific label | Catch-alls absorb too much volume; specific labels under-fire |
| CO-CLASSIFY instruction | Fires a second label simultaneously without a separate model pass | Rollup metrics are incomplete or require post-processing |
| Trailing annotation | Signals polarity, channel scope, or special edge case handling | Downstream aggregation errors; incorrect sentiment scoring |

### Phrase List Rules

- Use **double quotes** around every example phrase: `"the rep was rude"` not `the rep was rude`
- Separate phrases with commas; use `or` before the last phrase
- Open with `(including but not limited to:` and close with `)`
- Write in **customer voice** — how a real customer would write it in a survey, not how an analyst would describe it
  - ✅ `"rep was rude"`, `"she was so nasty"`, `"very unprofessional attitude"`
  - ❌ `"negative demeanor expressed by customer service representative"`
- Keep lists to **5–8 representative examples** — not an exhaustive dictionary
- Cover the range: mild → severe, formal → casual, direct → indirect

### Length Guidelines

| Length | Status | Action |
|---|---|---|
| ≤700 characters | Target | Good |
| 701–900 characters | Acceptable | Flag for future trim |
| >900 characters | Too long | Trim now — start with redundant phrase examples |

**Trim priority order:**
1. Remove redundant/overlapping phrase examples (the model generalizes from a few good examples)
2. Collapse verbose annotation text
3. Shorten EXCLUDE clause prose (keep the routing pointer; cut the explanation)
4. Never remove EXCLUDE clauses or CO-CLASSIFY annotations — they carry structural logic

---

## PART 3 — TAXONOMY ARCHITECTURE PRINCIPLES

### Standard Best Practices

**1. Hierarchy should flow from abstract → specific**
Each level should be narrower than the one above it. A Sub_Topic that could belong to two different Topics is a design problem — it means the Topic definitions aren't tight enough.

**2. Mutual Exclusivity vs. Exhaustiveness (ME/CE)**
- **Mutually exclusive (ME):** No two sub-topics should fire on the same signal for the same reason
- **Collectively exhaustive (CE):** Every meaningful customer statement should have at least one sub-topic to land in
- In practice for VOC: you want **CE** (catch-alls handle edge cases) but ME is enforced through EXCLUDE clauses for the most common overlap zones
- Full mutual exclusivity is often impossible and unnecessary — the EXCLUDE clause is your disambiguation tool

**3. Granularity decisions**
- Too broad: one sub-topic absorbs 40%+ of volume → you can't act on it, you can't trend it
- Too narrow: sub-topics each have <0.1% volume → noise, not signal
- Rule of thumb: if you can't describe a specific action AT&T should take based on this label firing, it's probably too broad

**4. Catch-all sub-topics are necessary but dangerous**
Every topic needs a catch-all (`Rep Overall Positive`, `General Customer Service - Negative`) to handle verbatims that are real but don't fit a specific label. But catch-alls without EXCLUDE clauses will absorb volume that should go to specific labels. Always:
- Write EXCLUDE clauses in the specific sub-topics routing back to the catch-all (not the other way)
- Add minimum-signal language to catch-all definitions: *"only apply if no more specific sub-topic in this topic applies and the verbatim contains explicit [positive/negative] language about [X]"*

**5. Label names are part of the model's input — name them carefully**
For zero-shot NLI, the label name is read as a hypothesis. Short, clear, customer-facing language works best:
- ✅ `Rep Was Rude / Not Courteous`
- ❌ `Negative Demeanor Event`
- ✅ `Bill Went Up Unexpectedly`
- ❌ `Price Increase Customer Notification Failure`

**6. Polarity belongs at the sub-topic level, not just the topic level**
Some topics have both positive and negative sub-topics (`Rep Was Courteous` / `Rep Not Courteous`). Don't try to handle both with a single neutral label — you lose the sentiment signal.

---

### Advanced Practices

**7. CO-CLASSIFY — Multi-Label Without a Second Model Pass**

The standard approach to multi-label classification is running multiple classification passes or training a multi-head model. CO-CLASSIFY is a simpler, taxonomy-driven alternative:

When a specific sub-topic fires, instruct it (in the definition) to also fire an umbrella sub-topic. Example:

> *Rep Not Courteous definition:* `"...CO-CLASSIFY: also apply 'Rep Overall Negative (General Dissatisfaction)' whenever this sub-topic fires."`

**What this gives you:**
- A detailed signal (`Rep Not Courteous`) for root cause analysis
- A rollup signal (`Rep Overall Negative`) for executive dashboards
- Both from a single classification pass, with no post-processing join

**Design rule:** The umbrella sub-topic's own definition should then say "do NOT apply directly — this label is populated via CO-CLASSIFY from specific sub-topics." This prevents the model from also firing it independently on weak signals.

**8. EXCLUDE Clauses as Routing Logic, Not Just Rejection**

Most practitioners write EXCLUDE clauses as *"don't apply this label if..."* — a passive rejection. A more powerful framing is routing: *"if the verbatim is about X specifically, apply [more specific sub-topic] instead."*

This turns your taxonomy into a decision tree embedded in the definitions:

```
Bill Is Too High / Too Expensive:
  Does NOT apply to: (1) verbatims where the customer names a specific unexpected charge or fee
  → apply "Hidden Fees / Unexpected Charges on Bill" instead.
  (2) verbatims where the bill increased from last month
  → apply "Bill Increased / Price Went Up Unexpectedly" instead.
```

The model reads this as a routing instruction, not just a boundary condition.

**9. EXCLUDE Chains — Cascading Specificity**

You can chain EXCLUDE clauses across multiple sub-topics to create a specificity cascade:

- `General Bill` → if more specific → `Bill Inquiry`
- `Bill Inquiry` → if about an error → `Billing Error / Incorrect Charge`
- `Billing Error` → if specifically fraud → `Fraud / Scam Allegation`

Each level excludes up to the next more specific one. This keeps catch-alls from absorbing volume and ensures the most specific applicable label always wins.

**10. Channel Scoping as a First-Pass Filter**

Rather than running the full taxonomy against every verbatim from every channel, create channel-specific taxonomy files (as you've done with the Care file). This:
- Reduces the label space the model must discriminate across → improves accuracy
- Prevents IHE-only sub-topics from firing on Care verbatims (where they're meaningless)
- Allows channel-specific phrase lists (store language vs. phone language vs. field tech language)

**11. Polarity Embedded in Paired Sub-Topics**

Instead of running a separate sentiment model, embed polarity directly in sub-topic pairs:
- `Rep Was Courteous` (Positive) / `Rep Not Courteous` (Negative)
- `Issue Resolved` (Positive) / `Issue Not Resolved` (Negative)

This lets you aggregate sentiment by any dimension (topic, category, channel) without a separate pass. The `Polarity` column in the CSV drives downstream aggregation.

---

### Non-Traditional but High-Impact Practices

**12. The `Taxonomy` Column as a Self-Contained Prompt Input**

Standard practice passes the label list and definitions separately to the model. A more powerful approach: concatenate them as `Sub_Topic->Sub_Topic_Definition` (which is what your `Taxonomy` column contains) and pass this single string as the label. The model now has both the label name AND its full context embedded in a single field.

This is particularly useful for:
- Batch classification APIs where prompt structure is constrained
- Ensemble approaches where you test multiple label formats
- Future fine-tuning datasets where you want rich label descriptions

**13. Identity Collision Avoidance**

Zero-shot NLI models are susceptible to **identity collision**: when a sub-topic has the same name (or near-same name) as its parent topic, the model conflates them. The model's hypothesis for `Perceived Trust` (sub-topic) is functionally identical to `Perceived Trust - Wrong Information` (topic), so it can't distinguish which level to fire.

**Prevention rule:** Every sub-topic name must be meaningfully distinct from its parent topic name. When naming, ask: *"If I saw only the sub-topic name with no context, would I know it was different from the topic?"*

Known instance in this taxonomy: `Perceived Trust` sub-topic inside `Perceived Trust - Wrong Information` topic → recommended rename: `Rep Was Deceptive / Customer Felt Misled`.

**14. Minimum-Signal Thresholds for Catch-Alls**

Standard definition: *"General negative sentiment about the representative."* This catches everything. Instead, add a minimum-signal requirement:

*"Only apply if the verbatim contains an explicit evaluative statement about the overall interaction or representative performance AND no more specific sub-topic in the Rep Helpfulness, Rep Courtesy, Rep Knowledge, or Rep Communication topics applies."*

This dramatically reduces catch-all absorption rates and improves signal quality in specific sub-topics.

**15. Writing Definitions as If-Then Logic**

Instead of writing definitions as descriptive prose ("this sub-topic covers..."), write them as executable logic the model can follow:

**Prose style (weak):**
> *"This sub-topic applies when a customer mentions that their bill went up."*

**If-then style (strong):**
> *"Apply when: customer explicitly states their bill amount increased, went up, or is higher than before (including but not limited to: "my bill went up," "price increase," "bill is higher"). Does NOT apply to: (1) customer says they received an unexpected or surprise charge → apply Hidden Fees instead. (2) customer's promotional rate expired → apply Promotion Expired instead."*

The if-then style gives the model the conditions, the phrase evidence, and the routing logic all in one pass.

**16. Phrase List as Semantic Anchor, Not Keyword List**

Practitioners often write phrase lists as keyword dictionaries expecting keyword matching. NLI doesn't work that way — it does semantic inference. Your phrase list should be designed to **anchor the semantic space** (define the center and edges of the concept), not enumerate every possible wording.

This means:
- Include phrases from opposite ends of formality: `"rep was rude"` AND `"the representative displayed very unprofessional behavior"`
- Include mild and severe instances: `"a little impatient"` AND `"screamed at me"`
- Include direct and indirect expressions: `"she hung up on me"` AND `"the call just ended and she never called back"`
- You do NOT need to list every possible synonym — the model generalizes from the examples

---

## PART 4 — YOUR DOCUMENTED PREFERENCES (From Sessions)

These are preferences you've demonstrated, requested, or explicitly confirmed over the taxonomy build sessions.

### Definition Style
- **Always use double quotes** around phrase examples in phrase lists — never single quotes or bare text
- **Contractions must be correct** — `"didn't"`, `"can't"`, `"wouldn't"` written fully; never broken artifacts from delimiter collisions
- **Customer voice in examples** — phrases should sound like something a customer would actually type in a survey
- **No analyst jargon** in phrase lists — the model reads these as evidence, not documentation
- **Length target: ≤700 characters** — aggressively trim if over 900; never sacrifice EXCLUDE or CO-CLASSIFY to hit the limit

### File Management
- **Always sort**: Category → Topic → Sub_Topic, A-Z
- **UTF-8 no BOM** encoding on every save — use `WriteAllLines` with `UTF8Encoding $false`
- **Preserve original definitions** in a separate column (`Original Definition`) when doing bulk rewrites — creates a rollback reference
- **Taxonomy column format**: `Sub_Topic->Sub_Topic_Definition` — the combined field for prompt use
- **Channel values** use pipe delimiter: `Care | IHE`, `Care | Retail | National Retail`

### PowerShell / Script Preferences
- **Run inline in terminal** — never save scripts as `.ps1` files when definitions contain Unicode characters (`—`, `→`, smart quotes)
- **Single-quoted strings** for definitions containing double-quoted phrase examples
- **Double apostrophes** inside single-quoted strings for contractions: `'didn''t'`
- **Hashtable pattern** for bulk edits — `$fixes = @{ 'Sub_Topic' = 'definition' }` loop
- **Always verify row count** after any save operation

### Taxonomy Design
- **CO-CLASSIFY** for umbrella + specific sub-topic pairing — prefer this over post-processing joins
- **EXCLUDE clauses mandatory** for any sub-topic that shares semantic space with another
- **Channel-specific files** for operational use — don't classify Care verbatims against IHE-only sub-topics
- **Paired polarity sub-topics** preferred over neutral combined labels
- **Catch-alls need guards** — minimum-signal threshold language to prevent over-absorption

### Structural Rules You've Confirmed
- Sub-topic names must be distinct from parent topic names (identity collision rule)
- `Rep Was Pushy` placement: currently in Rep Courtesy — deferred decision on whether to move to Sales Transparency
- `Perceived Trust` sub-topic rename: deferred but agreed it's a problem
- `Bill Inquiry` vs. `General Bill`: different intents — definitions should sharpen the boundary

---

## PART 5 — KNOWN GOTCHAS & ANTI-PATTERNS

### 1. Apostrophe Collision in Bulk Conversions ⚠️ CRITICAL
**What it is:** Using the apostrophe character `'` as a phrase delimiter in a conversion script. The same character appears in contractions (`didn't`, `can't`, etc.), causing phrases to split at the apostrophe and produce corrupted output.

**What the artifacts look like:**
- `"didn",` — truncated contraction in a phrase list
- `t know'.` — dangling text outside the closing parenthesis
- `"s",` — severed possessive (`Sam's` → `"s"`)

**Rule:** Never use `'`, `"`, `,`, or `.` as delimiters when processing definition text. Use `|`, tab (`\t`), or `;;`.

**Detection scan (run after any bulk conversion):**
```powershell
$rows = Import-Csv $path
$rows | Where-Object {
    $_.Sub_Topic_Definition -match '"didn",|"can",|"wasn",|"couldn",|"wouldn",|"shouldn",|"don",|"won",'
} | Select-Object Sub_Topic
```
Zero results = clean. Any results = repair immediately before using for classification.

### 2. PowerShell .ps1 File Encoding ⚠️ HIGH RISK
**What it is:** When a script file is created by VS Code tools, it saves as UTF-8. But PowerShell on Windows reads `.ps1` files as Latin-1 (CP1252). Em dash `—` (U+2014) becomes `â€"`. Right arrow `→` (U+2192) also corrupts.

**Rule:** Never save taxonomy edit scripts as `.ps1` files when definitions contain `—` or `→`. Run all commands inline in the PowerShell terminal directly.

**Safe substitutes in scripts only:** `--` for `—`, `->` for `→`. The CSV itself can keep the original Unicode.

### 3. Dollar Signs in PowerShell Strings
In double-quoted PowerShell strings, `$` triggers variable expansion. If a definition contains `$10` or `$X`, it will be interpreted as a variable and produce empty output.

**Fix:** Use backtick escape `` `$10 `` in double-quoted strings, or use single-quoted strings `'...'` where `$` is literal.

### 4. Identity Collision (Sub-Topic Name = Topic Name)
If a sub-topic has the same name as its parent topic, the NLI model cannot distinguish between them and conflates the two labels.

**Rule:** Every sub-topic name must be meaningfully distinct from its parent topic name.

### 5. Catch-All Over-Absorption
A poorly guarded catch-all sub-topic can absorb 30–40% of verbatims, masking the signal from specific sub-topics. The symptom: one label has disproportionately high volume, specific sub-topics in the same topic have suspiciously low volume.

**Fix:** Add minimum-signal threshold language to catch-all definitions and ensure specific sub-topics have EXCLUDE clauses routing edge cases back to the catch-all.

### 6. Phrase List as Keyword Dictionary (Wrong Mental Model)
Writing phrase lists expecting the model to do keyword matching. NLI models do semantic inference — they read the phrase list as examples that define the semantic space, not as a lookup table.

**Symptom:** You add 30 phrases to a definition hoping to catch every variant, and recall still doesn't improve.

**Fix:** Choose 5–8 phrases that cover the range of the concept (mild/severe, formal/casual, direct/indirect) and trust the model to generalize.

---

## PART 6 — FILE & SCRIPT MANAGEMENT REFERENCE

### Safe File Save Pattern (Always Use)
```powershell
$path = "...\VOC_Classification_Taxonomy_Care.csv"
$rows = Import-Csv $path

# --- make your changes here ---

$csv = $rows | ConvertTo-Csv -NoTypeInformation
[System.IO.File]::WriteAllLines($path, $csv, (New-Object System.Text.UTF8Encoding $false))
Write-Host "Saved. Rows: $($rows.Count)"
```
- `ConvertTo-Csv -NoTypeInformation` — removes the PowerShell type header row
- `UTF8Encoding $false` — UTF-8 without BOM
- Never use `Export-Csv` (may add BOM) or `Out-File` (encoding unreliable)

### Bulk Definition Edit Pattern
```powershell
$fixes = @{
    'Sub_Topic_Name_1' = 'corrected definition text here'
    'Sub_Topic_Name_2' = 'another corrected definition'
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
- Keys in the hashtable must match `Sub_Topic` exactly (case-sensitive)
- Use single-quoted strings for values containing double-quoted phrase examples
- Internal apostrophes in single-quoted strings: double them → `'didn''t'`

### Column Schema Reference
| Column | Purpose |
|---|---|
| `Category` | Broadest grouping (People, Process, Pricing, Platform, Product, Policy, Survey Artifact) |
| `Category_Definition` | Definition of the category for model context |
| `Topic` | Mid-level grouping within a category |
| `Topic_Definition` | Definition of the topic for model context |
| `Sub_Topic` | The specific label the model fires |
| `Sub_Topic_Definition` | Full instruction to the model — the most important field |
| `Polarity` | Positive / Negative / Neutral / Mixed — drives sentiment aggregation |
| `Survey_Channel` | All / Care / IHE / Retail / National Retail (pipe-delimited for multi-channel) |
| `Est_Count` | Estimated volume from 87K verbatim sample (refresh after classifier runs) |
| `Est_Pct` | Estimated percentage from same sample |
| `Notes` | Internal notes; not passed to model |
| `Original Definition` | Pre-v4 definition string — reference only, not used in classification |
| `Taxonomy` | Combined `Sub_Topic->Sub_Topic_Definition` — used as single-field LLM input |

---

## PART 7 — TESTING, VALIDATION & SKILL DOCUMENT POWER

### Level 1: Testing the Taxonomy (Does Classification Work?)

**A. Sample Run — First Check**
Run the classifier against a small, labeled sample (50–100 verbatims where you know what the correct label should be). Calculate:
- **Precision** for each sub-topic: of all verbatims the model labeled X, what % actually are X?
- **Recall** for each sub-topic: of all verbatims that are actually X, what % did the model catch?

**B. Distribution Check — Sanity Check**
After a full run, look at the label distribution:
- Any single sub-topic absorbing >15% of total volume → likely a catch-all problem
- Any sub-topic with <0.1% volume → definition may be too narrow, or the concept may not appear in the data
- Paired polarity sub-topics should have reasonable ratios (e.g., `Rep Was Courteous` should dominate in high-satisfaction surveys)

**C. Catch-All Absorption Rate**
Specifically calculate: what % of verbatims fire ONLY a catch-all sub-topic with no specific sub-topic? This is your "unresolved signal" rate. Target: <10%.

**D. CO-CLASSIFY Verification**
Confirm that every verbatim that fires a specific CO-CLASSIFY sub-topic also fires the umbrella sub-topic. If not, the CO-CLASSIFY instruction isn't being followed — the definition may be too long and the instruction is being truncated.

**E. EXCLUDE Clause Effectiveness**
Find verbatims that fire both a specific sub-topic and its catch-all. These are cases where the EXCLUDE clause isn't routing correctly. Investigate the definition — the routing pointer may be ambiguous.

**F. Co-occurrence Analysis**
Look at which sub-topics frequently fire together. Expected co-occurrences (e.g., `Rep Not Courteous` + `Rep Overall Negative`) confirm CO-CLASSIFY is working. Unexpected co-occurrences (e.g., `Bill Is Too High` + `Bill Inquiry`) may indicate overlap between definitions.

### Level 2: Testing the SKILL Document (Does Copilot Follow It?)

**What makes a skill document powerful for an LLM:**

1. **Explicit triggers** — the document should specify exactly what phrase causes Copilot to load it. Vague triggers mean the skill never fires.

2. **Actionable rules, not descriptive prose** — "always use double quotes around phrase examples" is actionable. "Definitions should be well-formatted" is not.

3. **Concrete examples** — show both correct and incorrect versions. The LLM learns the pattern from contrast.

4. **Decision rules for ambiguous cases** — the skill should answer "what do I do when..." questions so Copilot doesn't have to guess.

5. **Copy-paste ready code patterns** — for recurring operations (file save, bulk edit), the exact PowerShell pattern should be in the skill so Copilot can use it without re-deriving it.

**How to test if the skill is being applied:**

- Type `taxonomy: [task]` and observe whether Copilot reads the skill file before responding
- Ask Copilot to write a definition and check: does it follow the v4 format? Does it use double quotes? Is it under 700 chars?
- Ask Copilot to write a PowerShell update script and check: does it use `WriteAllLines`? Does it use single-quoted strings?
- Ask Copilot a gotcha scenario (e.g., "update these definitions with a script") and see if it proactively warns about `.ps1` encoding or apostrophe collisions

**Signs the skill document isn't working:**

- Copilot writes definitions in prose style without phrase lists
- Copilot uses `Export-Csv` instead of `WriteAllLines`
- Copilot creates `.ps1` files with Unicode characters in them
- Copilot writes catch-all definitions without EXCLUDE clauses
- Copilot names a sub-topic the same as its parent topic

**What to do when the skill isn't being followed:**
- Make the rule more explicit — add "ALWAYS" or "NEVER" capitalization for non-negotiables
- Move the rule higher in the document — LLMs read top-to-bottom and weight earlier content more
- Add an example of the wrong approach alongside the right approach
- Add it to `copilot-instructions.md` Known Gotchas so it's always in context even when the skill isn't loaded

### Level 3: Measuring the Full Power of the Skill

The skill document's full power is realized when:

1. **Zero re-explanation needed** — you can say `taxonomy: fix the catch-all definitions` and Copilot knows what that means, what the format rules are, and what tools to use — without you specifying any of it

2. **Gotchas are self-avoiding** — Copilot proactively warns you about apostrophe collisions, `.ps1` encoding, and identity collision before you encounter them, not after

3. **New sub-topics are written correctly on first draft** — you can say "add a new sub-topic for X under Topic Y" and the definition comes back in v4 format, under 700 chars, with EXCLUDE clauses, at the right polarity, without revision

4. **Session continuity is maintained** — the skill, combined with the handoff documents, means each new session picks up exactly where the last left off with no re-context-setting

---

## PART 8 — ELEMENTS TO SELECT FOR THE OFFICIAL SKILL

Review this document and mark which sections to include. Suggested evaluation criteria:

| Element | Include if... |
|---|---|
| Plain-English explanations (Part 1) | You want the skill to help onboard a new collaborator, not just remind you |
| Full definition format (Part 2) | Always — this is the core operating standard |
| Standard best practices (Part 3, items 1–6) | Include as concise rules, not full explanations |
| Advanced practices (Part 3, items 7–11) | Include CO-CLASSIFY and EXCLUDE routing in full; summarize others |
| Non-traditional practices (Part 3, items 12–16) | Include items 13, 14, 15 — highest practical impact; item 12 optional |
| Your documented preferences (Part 4) | Include all — these are the rules Copilot needs to follow for your work |
| Gotchas (Part 5) | Include all — these prevent real, recurring mistakes |
| File & script patterns (Part 6) | Include all code patterns verbatim — Copilot uses these directly |
| Testing guide (Part 7) | Include as a reference section; can be summarized for the skill |

---

*Draft created: 2026-06-23 | For review — not yet incorporated into skills/taxonomy/SKILL.md*
