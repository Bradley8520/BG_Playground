# Skill: SQL Query Writing

## When to Use This Skill
Activate when the user says `write a query for [X]` or asks to generate, write, or build any SQL query.

---

## Steps to Follow

### Step 1 — Clarify Requirements
Before writing any SQL, confirm:
1. Which table(s) are involved? (refer to Source Tables in `.github/copilot-instructions.md`)
2. What is the grain of the output? (one row per account? per event? per month?)
3. What date range? (default: last 13 months unless specified)
4. What filters apply beyond the standard ones?
5. Is this for a one-time ad-hoc run, or will it be saved/scheduled?

### Step 2 — Draft the Query
- Use fully qualified table names from the Source Tables reference
- Apply all Standard Filters from `.github/copilot-instructions.md` unless user explicitly says to omit them
- Add `-- Purpose: [description]` comment at the top
- Use UPPERCASE SQL keywords, lowercase aliases, 4-space indentation
- Add inline comments on non-obvious logic

### Step 3 — Review & Explain
After drafting:
1. Show the query
2. Call out any assumptions made
3. Flag any performance risks (e.g., large table joins, missing partition filters)
4. Ask: "Does this match what you need, or should I adjust anything?"

### Step 4 — Validation Checklist
Before finalizing, verify:
- [ ] All table names are fully qualified
- [ ] Standard filters are applied (or user explicitly waived them)
- [ ] No unbounded scans on partitioned tables
- [ ] NULL handling addressed for known nullable columns
- [ ] Date arithmetic uses `ADD_MONTHS()` not subtraction
- [ ] No `SELECT *` — all columns are named explicitly
- [ ] String literals are UPPERCASE

---

## Pitfalls to Avoid

| Anti-Pattern | Correct Approach |
|---|---|
| `SELECT *` | List explicit columns |
| `WHERE BILL_DT >= CURRENT_DATE - 365` | `WHERE BILL_DT >= ADD_MONTHS(CURRENT_DATE, -13)` |
| `WHERE status_cd = 'active'` | `WHERE STATUS_CD = 'A'` (uppercase, use code) |
| CTE for large intermediate datasets | `CREATE VOLATILE TABLE` or `#temp` |
| Missing filter on `USAGE_EVENTS` | Always filter by `EVENT_DT` partition key |
| `SELECT DISTINCT` on large tables | `GROUP BY` — optimizer handles it better |

---

## Example Output Format

```sql
-- Purpose: Count active residential accounts by billing cycle
-- Author: [user]
-- Date: [date]

SELECT
    billing_cycle,
    COUNT(DISTINCT acct_id) AS acct_count
FROM PROD_DB.SCHEMA_NAME.ACCOUNT_MASTER
WHERE STATUS_CD = 'A'
  AND ACCT_TYPE = 'R'
  AND ACCT_ID NOT LIKE 'TEST%'
  AND ACCT_ID NOT LIKE '9999%'
  AND BILL_DT >= ADD_MONTHS(CURRENT_DATE, -13)
GROUP BY billing_cycle
ORDER BY billing_cycle;
```

---

## Field Reference Quick Card

| Field | Valid Values | Notes |
|---|---|---|
| `STATUS_CD` | A, S, T, P | Default filter: `A` only |
| `ACCT_TYPE` | R, B, G, W | Residential, Business, Govt, Wholesale |
| `CHARGE_TYPE_CD` | MRC, BASE, FEAT (recurring); OTC, INST, DISC (one-time) | See MRC vs OTC rules |
| `PROD_CD` prefix | WL, BB, TV, LN | Wireless, Broadband, Video, Landline |
