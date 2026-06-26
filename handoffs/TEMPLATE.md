# Session Handoff — [DATE]

> Trigger: Type **"wrap up"** or **"end session"** and Copilot will fill this template automatically.
> Save completed handoffs as `handoffs/YYYY-MM-DD.md`.

---

## Session Summary

| Field | Value |
|---|---|
| **Date** | [YYYY-MM-DD] |
| **Duration** | [approx hours] |
| **Branch** | [git branch name] |
| **Primary Goal** | [one sentence: what you were trying to accomplish] |
| **Status** | Completed / Partial / Blocked |

---

## What Was Accomplished

- [ ] [Completed task 1 — be specific]
- [ ] [Completed task 2 — be specific]
- [ ] [Completed task 3 — be specific]

---

## Files Changed

| File | Change Type | Summary |
|---|---|---|
| `[path/to/file]` | Created / Modified / Deleted | [brief description of what changed and why] |

---

## Decisions Made

Document any non-obvious choices made this session and the reasoning:

1. **[Decision title]:** [What was decided and why. Include alternatives considered.]
2. **[Decision title]:** [What was decided and why.]

---

## Learnings & Gotchas Discovered

Document anything new learned about the codebase, data, or environment:

- [Something discovered about a table, column, or behavior]
- [Anti-pattern found and avoided]
- [Correction to a previous assumption — what was wrong and what's correct]

---

## In Progress / Blocked

Tasks that were started but not completed:

- [ ] **[Task name]** — [Why it's incomplete. What's blocking it. What the next concrete step is.]
- [ ] **[Task name]** — [Why it's incomplete.]

---

## Next Session — Pick Up Here

Ordered list of exactly what to do first in the next session. Be concrete and specific — not "continue work on X" but "open file Y and fix Z":

1. [Exact first action — file to open, command to run, question to answer]
2. [Second action]
3. [Third action]

---

## Environment State

```bash
# Current branch
git branch --show-current   # → [branch name]

# Last commit
git log --oneline -1        # → [hash] [message]

# Last deployment
# Environment: [dev / staging / prod]
# Deployed at: [timestamp]
# Deploy command used: [command]

# Pending / uncommitted changes
# [list any stashed or in-progress work]
```

---

## References Used This Session

- [File path or URL that was key to this session's work]
- [Documentation consulted]
- [Query or script that was useful — or path to where it was saved]
