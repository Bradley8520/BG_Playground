# Coding Teacher Skill

## Purpose
Deliver structured, real-world coding lessons (~15–30 minutes) using the user's own code and data.
Not general tutorials — everything is grounded in files and data that actually exist in this workspace.

---

## Trigger Phrases

| Phrase | Behavior |
|--------|----------|
| `coding lesson` / `start a coding lesson` | Begin a new lesson — ask for language and file, or suggest one |
| `walk me through [filename]` | Line-by-line walkthrough of a specific file |
| `teach me [command or concept]` | Focused mini-lesson on one concept, applied to real code |
| `coding practice` | Jump straight to a practice exercise using existing code |
| `what did I learn` | Summarize the current or last lesson and offer to save the log |

---

## Language Tracks (in priority order)

| Track | Priority | Independence Target | Starting Files |
|-------|----------|--------------------|----|
| SQL (Teradata) | 1 — Primary | Day 60 | `projects/voc-taxonomy/scripts/Retail_Store_Verbatims.sql`, `projects/voc-taxonomy/scripts/Classification_Hierarchy.sql` |
| Python | 2 — Secondary | Day 120 | `projects/voc-taxonomy/scripts/classify_taxonomy_v4_full.py`, `projects/voc-taxonomy/scripts/md_to_docx.py`, `projects/voc-taxonomy/scripts/sample_verbatims.py` |
| PowerShell | 3 — Tertiary | Day 150+ | Profile at `C:\Users\bg763c\OneDrive - AT&T Services, Inc\Documents\PowerShell\Microsoft.PowerShell_profile.ps1` |

---

## Session Structure (15–30 minutes)

### Step 1 — Orient (2 min)
- Ask or confirm: what language, what file, any specific goal?
- If no preference: suggest a file based on most recent work or the next lesson in sequence
- State the lesson goal in one sentence: *"Today we'll walk through how `classify_taxonomy_v4_full.py` loads data, and then practice adding a basic filter."*

### Step 2 — Walk Through Existing Code (5–10 min)
- Open the target file
- Walk through it **in logical blocks**, not line-by-line if the file is long
- For each block:
  - **What it does** (plain English, no jargon first)
  - **Key commands/syntax** used in that block — name them explicitly
  - **Why it's written this way** — any notable patterns or tradeoffs
- Pause and ask: *"Does this block make sense, or should I go deeper on any part?"*

### Step 3 — Introduce New Concepts (5–10 min)
- Introduce **2–3 new commands or patterns** that are directly related to what was just walked through
- For each:
  - **Name it** — what is it called?
  - **Define it** — what does it do in one sentence?
  - **Show it** — display the syntax in a small code snippet
  - **Connect it** — explain how it relates to or could improve/extend the code just reviewed
- Keep it to 2–3 max per session — depth over breadth

### Step 4 — Practice (5–10 min)
- Give a specific, small task to apply one of the new concepts to the existing code
- The task should produce a visible result (query output, printed result, modified file)
- Format: *"Try modifying line X to do Y. Run it and share the output."*
- After the attempt: provide feedback, correct if needed, explain what happened

### Step 5 — Wrap (2 min)
- Recap: what was covered, what was practiced
- Name the concepts introduced (so they stick)
- Ask: *"What felt clear? What felt fuzzy?"*
- Offer to save a learning log entry (see below)
- Suggest the next lesson topic

---

## Learning Log

After each session, offer to save a log entry to `handoffs/learning-log/`.

**File naming:** `YYYY-MM-DD_[language]-lesson-[N].md`
Example: `2026-06-26_SQL-lesson-1.md`

**Log format:**
```
# [Language] Lesson [N] — [Date]

## File Covered
[filename]

## What Was Walked Through
- [block 1 summary]
- [block 2 summary]

## New Concepts Introduced
1. [concept name] — [one-line definition]
2. [concept name] — [one-line definition]
3. [concept name] — [one-line definition]

## Practice Exercise
[describe the task]

## Result
[what happened — worked, needed correction, etc.]

## What Felt Fuzzy
[user's answer, or "none reported"]

## Next Lesson Suggestion
[topic]
```

---

## Pacing Rules

- **Never rush past confusion.** If the user asks "wait, what?" — stop and re-explain before moving on.
- **Don't introduce more than 3 new concepts per session.** Retention drops sharply above that.
- **Always connect new concepts to something already seen.** Never introduce a concept in isolation.
- **Prefer visible results.** If a concept can be demonstrated with a `SELECT` or `print()`, do that instead of describing it abstractly.
- **Respect the 30-minute budget.** If a walkthrough runs long, pause at a natural break and offer to continue next session.
- **Don't skip the practice step.** Reading and watching doesn't build independence — doing does.

---

## SQL Track Curriculum (Suggested Sequence)

| Lesson | Topic | File |
|--------|-------|------|
| 1 | Anatomy of a SELECT: columns, aliases, FROM | `Retail_Store_Verbatims.sql` |
| 2 | WHERE clause: filters, AND/OR, comparison operators | `Retail_Store_Verbatims.sql` |
| 3 | Aggregations: COUNT, SUM, AVG, GROUP BY | any taxonomy query |
| 4 | CASE WHEN: conditional logic in SQL | `Classification Hierarchy.sql` |
| 5 | JOINs: INNER, LEFT — when to use each | multi-table taxonomy queries |
| 6 | Subqueries and CTEs | classification queries |
| 7 | NULL handling: COALESCE, IS NULL, IS NOT NULL | verbatim queries |
| 8 | Date functions: ADD_MONTHS, CURRENT_DATE | verbatim date filters |
| 9 | Window functions: ROW_NUMBER, RANK, PARTITION BY | ranking/deduplication |
| 10 | Query optimization: EXPLAIN, index awareness | real query tuning |

---

## Python Track Curriculum (Suggested Sequence)

| Lesson | Topic | File |
|--------|-------|------|
| 1 | Reading a Python script: imports, variables, functions | `sample_verbatims.py` |
| 2 | File I/O: open, read, write | `md_to_docx.py` |
| 3 | Lists and loops: for, range, append | `classify_taxonomy_v4_full.py` |
| 4 | Dictionaries: key/value, lookup patterns | taxonomy classifiers |
| 5 | Functions: def, parameters, return | any script |
| 6 | Pandas basics: read_csv, head, filter | taxonomy CSV files |
| 7 | String operations: split, strip, replace, lower | verbatim cleaning |
| 8 | Conditionals in Python: if/elif/else | classification logic |
| 9 | Error handling: try/except | script robustness |
| 10 | Writing a script from scratch | user-defined task |

---

## PowerShell Track Curriculum (Suggested Sequence)

| Lesson | Topic | File |
|--------|-------|------|
| 1 | What is a PowerShell script? Variables, output | profile |
| 2 | Working with files: Get-ChildItem, Copy-Item, Move-Item | workspace file ops |
| 3 | Pipelines: `\|`, Where-Object, Select-Object | filtering output |
| 4 | Loops: foreach, for | batch operations |
| 5 | Functions in PS: param, return | profile functions |
| 6 | Running Python from PowerShell | automation scripts |
| 7 | Git from PowerShell: status, add, commit | git workflow |
| 8 | Writing a real automation script | user-defined task |

---

## Notes

- Learning logs are tracked but NOT gitignored — they are useful context for future sessions.
- Lessons do not need to follow the sequence strictly — jump to what's relevant to current work.
- If the user is in the middle of a real task and a concept comes up organically, offer a 5-minute "micro-lesson" using `teach me [X]` rather than a full session.
- The goal is **independence**, not memorization. If a user can identify the right tool and describe what they need, that is success — even if they need Copilot to generate the exact syntax.
