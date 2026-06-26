# Skill: Verbatim Analysis

## When to Use
Activate when the user asks to analyze, review, sample, classify, or summarize customer verbatims, survey responses, or raw text feedback.

---

## Context
- Verbatim files are stored in `projects/voc-taxonomy/verbatims/` — **gitignored, local only**
- Classification prompts are in `projects/voc-taxonomy/prompts/`
- Output files go to `projects/voc-taxonomy/output/` — also gitignored
- The active taxonomy for classification is `VOC_Classification_Taxonomy_v4.csv`

---

## Standard Analysis Workflow

### Step 1 — Clarify scope
Before analyzing, confirm:
1. What channel? (Care, Retail, All)
2. What date range?
3. Sample size or full file?
4. Goal: classify? summarize themes? identify gaps? validate taxonomy?

### Step 2 — Load the right taxonomy
Always reference the current master taxonomy before classifying:
- `projects/voc-taxonomy/taxonomy/VOC_Classification_Taxonomy_v4.csv` (master)
- `projects/voc-taxonomy/taxonomy/VOC_Classification_Taxonomy_Care.csv` (Care channel)

### Step 3 — Run classification
Use the prompt from `projects/voc-taxonomy/prompts/care_classification_prompt_v1.txt` as the base.
Save output to `projects/voc-taxonomy/output/` with a dated filename.

### Step 4 — Summarize findings
After classification, always produce:
- Volume by Category and Topic
- Top 5 subtopics by count
- Any verbatims that did not classify cleanly (edge cases)

---

## Known Gotchas
- Verbatim text often contains apostrophes — never use `'` as a delimiter
- Some verbatims are very short (< 5 words) — classify as "Insufficient Context" rather than forcing a topic
- Watch for Spanish-language verbatims — flag separately, do not force-classify into English taxonomy
- Survey artifacts (e.g., "N/A", "999", "test") should be excluded — see `taxonomy/SKILL.md` for full list

---

## [STUB — Expand this skill as patterns emerge]
Add specific classification rules, edge cases, and prompt refinements here as you discover them.
