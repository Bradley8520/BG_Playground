# Skill: Ad-Hoc Query

## When to Use This Skill
Activate when the user says `ad hoc: [question]`, asks a quick data question, or needs fast exploratory SQL without full production engineering.

---

## Philosophy

Ad-hoc queries are **exploratory, not production**. Prioritize:
1. Getting a working result quickly
2. Plain-English explanation of what the query returns
3. Offering easy next steps

Do NOT over-engineer. Skip the full Step 1 clarification loop when intent is clear — just draft and explain.

---

## Steps to Follow

### Step 1 — Parse the Question

Extract from the user's phrasing:
- **What**: metric, count, list, average, etc.
- **Who/What entity**: account, order, event, product, etc.
- **Implied filters**: time period, status, product type, region
- **Grain**: one row per what?

### Step 2 — Quick Draft

Write a concise query:
- Default date range: **last 30 days** unless user specifies otherwise
- Apply standard filters from `.github/copilot-instructions.md`
- Use CTEs if ≤3 steps; use temp/volatile tables if more complex
- Still use fully qualified table names
- Add a brief `-- Purpose:` comment at the top

### Step 3 — Plain-English Explanation

After the query, always include:

```
This query returns [WHAT] for [WHO/ENTITY], filtered to [CONDITIONS].
Expected output: approximately [N] rows, one per [GRAIN].
```

### Step 4 — Offer Next Steps

End with:
> "Do you want to:
> 1. Refine filters or date range?
> 2. Add a breakdown/grouping dimension?
> 3. Save this as a named skill in `skills/`?
> 4. Promote this to a scheduled/production query?"

---

## Example Interaction

**User:** `ad hoc: how many active wireless accounts do we have right now?`

**Response:**

```sql
-- Purpose: Count of active wireless accounts as of today

SELECT
    COUNT(DISTINCT acct_id) AS active_wireless_acct_count
FROM PROD_DB.SCHEMA_NAME.ACCOUNT_MASTER
WHERE STATUS_CD = 'A'
  AND PROD_CD LIKE 'WL%'
  AND ACCT_ID NOT LIKE 'TEST%'
  AND ACCT_ID NOT LIKE '9999%';
```

> This query counts distinct accounts that are currently active (`STATUS_CD = 'A'`) and have a wireless product (`PROD_CD` starting with `WL`), excluding test accounts.
> Expected output: 1 row with a single count.

---

## Pitfalls to Avoid

- Still apply partition/date filters on large tables like `USAGE_EVENTS` — even for ad-hoc queries
- Still use fully qualified table names — no shortcuts
- String values must be UPPERCASE (this database is case-sensitive)
- For `USAGE_EVENTS`: always filter `EVENT_DT` — full table scans cause cluster contention

---

## Quick Reference: Default Assumptions

| Parameter | Ad-Hoc Default |
|---|---|
| Date range | Last 30 days |
| Status filter | `STATUS_CD = 'A'` (active only) |
| Test exclusion | `ACCT_ID NOT LIKE 'TEST%' AND ACCT_ID NOT LIKE '9999%'` |
| Query style | CTE if simple, temp table if complex |
| Grain | Stated by user; if unclear, assume account-level |
