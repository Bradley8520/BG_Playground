---
mode: agent
description: Write an optimized SQL query following project conventions. Triggers the full multi-step SQL writing protocol.
---

# Write SQL Query

Read and follow the full protocol in `skills/sql-writing/SKILL.md` before writing any code.

## My Request

${input:Describe what you want the query to return. Include: which table(s), the metric or data, any specific filters, and the grain (one row per what?)}

## Constraints (from .github/copilot-instructions.md)

- Use fully qualified table names from the Source Tables section
- Apply Standard Filters unless I explicitly say to skip them
- UPPERCASE SQL keywords, lowercase snake_case aliases
- Add `-- Purpose:` comment at the top
- Date arithmetic: use `ADD_MONTHS()` not subtraction
- No `SELECT *` — list explicit columns
- No unbounded scans on `USAGE_EVENTS` — always filter `EVENT_DT`

## Expected Copilot Behavior

1. If my request is ambiguous, ask clarifying questions (grain, date range, additional filters) before drafting
2. Draft the query with inline comments on non-obvious logic
3. After the query, explain any assumptions made
4. Flag any performance risks
5. Ask: "Does this match what you need, or should I adjust?"
