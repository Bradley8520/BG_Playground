---
mode: agent
description: Generate a completed end-of-session handoff document. Captures what was done, decisions made, learnings, and exactly what to do next session.
---

# Session Handoff Generator

Generate a completed handoff document using the structure in `handoffs/TEMPLATE.md`.

## Session Date

${input:Today's date (YYYY-MM-DD)}

## Instructions

Review this entire conversation and all file changes made, then populate every section of the handoff template:

### 1. Session Summary
- Summarize the primary goal and overall outcome (completed / partial / blocked)
- Note the current git branch

### 2. What Was Accomplished
- List each completed task as a concrete, specific bullet point
- Do NOT use vague entries like "worked on queries" — be specific about what changed

### 3. Files Changed
- List every file that was created, modified, or deleted
- Include a one-line description of what changed and why

### 4. Decisions Made
- Document every non-obvious choice and the reasoning behind it
- Include alternatives that were considered and rejected

### 5. Learnings & Gotchas
- Note anything new discovered about the codebase, data, or environment
- Flag any corrections to previous assumptions

### 6. In Progress / Blocked
- List any tasks that were started but not finished
- For each: explain why it's incomplete and what the concrete next step is

### 7. Next Session — Pick Up Here
- Write specific, ordered action items for next session
- NOT "continue work on X" — write "open file Y, go to line Z, fix [specific thing]"

### 8. Environment State
- Current branch, last commit, last deployment details

## Output

Show me the completed handoff document. Then ask: **"Should I save this to `handoffs/[date].md`?"**  
Wait for my confirmation before saving.
