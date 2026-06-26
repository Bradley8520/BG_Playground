# Skill: Workspace Review & Hygiene

## When to Use
Activate when the user says `review my workspace`, `workspace cleanup`, `folder review`, `am I organized`, or at the user's request ("review my files").
Can also be run weekly — suggested trigger: first session of each week.

---

## Review Checklist

Run through each section and report findings with a pass/flag/action-needed status.

### Section 1 — Handoffs
- [ ] Is there a handoff from the last session? (`handoffs/` — check for recent dated files)
- [ ] Are handoffs named correctly (`YYYY-MM-DD.md`)?
- [ ] Are there any handoffs older than 90 days that can be archived?
- [ ] Does `handoffs/TEMPLATE.md` still reflect current workflow?

**Flag if:** Last handoff is more than 2 sessions ago — user is losing session memory.

---

### Section 2 — Commits & Git Health
- [ ] Run `git status` — are there uncommitted changes?
- [ ] Run `git log --oneline -10` — are commit messages meaningful?
- [ ] Are commits happening at least once per work session?
- [ ] Is the branch `main`, or is there an active feature branch that should be merged?

**Flag if:** Uncommitted changes exist, or last commit was more than 1 week ago.

---

### Section 3 — Project Folders
For each folder under `projects/`:
- [ ] Does it have a `README.md`?
- [ ] Does it have an `output/` folder that is gitignored?
- [ ] Are there script files without comments or documentation?
- [ ] Are there files that look like temporary work (e.g., `test.py`, `temp.csv`, `scratch.sql`)?
- [ ] Are taxonomy/CSV files versioned correctly (v1, v2, etc.)?

**Flag if:** Project folder missing README, or has unversioned/temp files.

---

### Section 4 — Skills Folder
- [ ] Are all skills referenced in `copilot-instructions.md`?
- [ ] Are there skills that haven't been used in 4+ weeks? (Consider archiving)
- [ ] Are there repeated patterns in recent sessions that should become a new skill?
- [ ] Do all SKILL.md files have a "When to Use" section and trigger phrase?

**Flag if:** A skill exists but has no trigger phrase (Copilot won't load it automatically).

---

### Section 5 — `.github/copilot-instructions.md`
- [ ] Are all table names still current?
- [ ] Are all trigger phrases working and mapped to existing skills?
- [ ] Are there new gotchas from recent sessions that should be added to "Known Gotchas"?
- [ ] Is the Terminology Reference up to date?

**Flag if:** A skill was created but not added to copilot-instructions.md.

---

### Section 6 — Stale or Orphaned Files
Look for:
- `.py` scripts in `scripts/` with no corresponding output or docs reference
- `.csv` files in `taxonomy/` that are superseded by newer versions
- `.md` files in `docs/` that reference old taxonomy versions
- Any `~$*.docx` or `.tmp` files (Word lock files — should be gitignored)

---

## Output Format

```
## Workspace Review — [DATE]

### Overall Health: 🟢 Good / 🟡 Needs Attention / 🔴 Action Required

| Section | Status | Notes |
|---------|--------|-------|
| Handoffs | 🟢/🟡/🔴 | [finding] |
| Git / Commits | 🟢/🟡/🔴 | [finding] |
| Project Folders | 🟢/🟡/🔴 | [finding] |
| Skills Folder | 🟢/🟡/🔴 | [finding] |
| copilot-instructions.md | 🟢/🟡/🔴 | [finding] |
| Stale Files | 🟢/🟡/🔴 | [finding] |

### Action Items (prioritized)
1. [Most important — do this now]
2. [Can do this week]
3. [Nice to have — when time allows]

### Wins 🎉
[What the user is doing well organizationally]
```

---

## Tips to Share (rotate, don't repeat)
- "A good rule of thumb: if you haven't opened a file in 60 days, it should be archived or deleted."
- "Your `output/` folders are gitignored — but are they also cleaned up locally so they don't grow indefinitely?"
- "Every skill file should have a trigger phrase. Without one, Copilot has to guess when to load it."
- "The best handoff is one you could hand to a colleague cold — they'd know exactly where you left off."
- "Consider adding a `CHANGELOG.md` to taxonomy files so version history is human-readable, not just in git."
