# Skill: Session Start

## When to Use
Activate at the beginning of any new chat session, or when the user says `start session`, `new session`, or `where did we leave off`.

---

## Session Start Checklist

Walk the user through this in order:

### Step 1 — Restore Context
Ask: "Do you have a recent handoff doc to paste in?"
- If yes: read it and summarize the current state in 3 bullet points
- If no: ask what project/task they're picking up and reconstruct from available files

### Step 2 — Confirm Active Project
Ask: "What are we working on today?"
Options to help them orient:
- [ ] Continuing a previous task (from handoff)
- [ ] Starting something new (→ scaffold new project folder)
- [ ] Exploring / learning / ad-hoc question

### Step 3 — Load Relevant Context
Based on the project, suggest which skills to activate:
- VOC taxonomy work → `skills/taxonomy/SKILL.md`
- SQL query work → `skills/sql-writing/SKILL.md`
- Verbatim analysis → `skills/verbatim-analysis/SKILL.md`
- Python scripting → `skills/python-scripts/SKILL.md`
- Document export → `skills/doc-export/SKILL.md`

### Step 4 — Check Git Status
Quick check: are there uncommitted changes from the last session?
```powershell
git status
git log --oneline -5
```
If uncommitted changes exist → offer to commit them before starting new work.

### Step 5 — Set Session Goal
Ask: "What's the one thing you want to have done by the end of this session?"
Write it down at the top of the session — refer back to it at wrap-up.

---

## Session End (tie to `wrap up` trigger)
At wrap up, confirm:
1. Was the session goal achieved?
2. Generate handoff using `handoffs/TEMPLATE.md`
3. Commit all changed files
4. Note any new skills that should be created or updated

---

## Pro Tips to Share at Session Start (rotate)
- "Starting with a handoff paste takes 30 seconds and saves 10 minutes of re-explanation."
- "Setting a session goal keeps you focused — it's easy to rabbit-hole without one."
- "Committing at the start clears your slate — you know exactly what changed this session."
