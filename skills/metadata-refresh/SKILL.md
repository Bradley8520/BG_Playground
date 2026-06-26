# Skill: Metadata Refresh

## When to Use This Skill
Activate when the user says `refresh metadata`, `update schema`, `what columns does [table] have`, or asks about table structures, column types, or row counts.

---

## What This Skill Does

Discovers and caches current table schemas, column types, nullable flags, and row counts into `memories/repo/` files. This prevents re-querying the same schema information every session and keeps a verified reference that Copilot uses in query generation.

---

## Steps to Follow

### Step 1 — Identify Tables to Refresh

Ask: **"Which tables do you want to refresh? (all / specific table aliases)"**

Reference the Source Tables table in `.github/copilot-instructions.md` for the full list of aliases.

### Step 2 — Discover Schema

For each table, retrieve:
- Column names and data types
- Nullable columns
- Primary key and/or partition key
- Approximate row count (if available via stats)
- Last updated timestamp or last stats refresh date

Suggested discovery query (adapt for your platform):
```sql
-- Teradata
SELECT
    columnname,
    columntype,
    nullable,
    columnformat
FROM dbc.columnsv
WHERE databasename = '[SCHEMA]'
  AND tablename    = '[TABLE]'
ORDER BY columnid;

-- SQL Server / T-SQL
SELECT
    COLUMN_NAME,
    DATA_TYPE,
    IS_NULLABLE,
    CHARACTER_MAXIMUM_LENGTH
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = '[SCHEMA]'
  AND TABLE_NAME   = '[TABLE]'
ORDER BY ORDINAL_POSITION;
```

### Step 3 — Format and Cache

Save discovered schema to `memories/repo/schema-[alias].md` using this format:

```markdown
## Table: PROD_DB.SCHEMA_NAME.TABLE_NAME
**Alias:** [alias]
**Last Verified:** [YYYY-MM-DD]
**Row Count (approx):** [count]
**Source Environment:** [prod / staging / dev]

| Column Name      | Type         | Nullable | Notes                              |
|------------------|--------------|----------|------------------------------------|
| ACCT_ID          | VARCHAR(20)  | NO       | Primary key                        |
| STATUS_CD        | CHAR(1)      | NO       | See valid values in copilot-instructions.md |
| BILL_DT          | DATE         | YES      | Partition key — always filter this |
| ACCT_TYPE        | CHAR(1)      | NO       | R/B/G/W                            |
```

### Step 4 — Flag Discrepancies

Compare discovered columns against what's documented in `.github/copilot-instructions.md`. If any column listed in Key Field Definitions is missing or has a different type, alert the user:

> "Column `STATUS_CD` is documented as CHAR(1) but the table shows VARCHAR(2). Should I update the instructions?"

### Step 5 — Confirm Cache

Tell the user:
> "Schema cached in `memories/repo/schema-[alias].md`. I'll use this in future sessions without re-querying."

---

## Pitfalls to Avoid

- Do NOT cache schema sourced from a DEV environment as authoritative for prod queries — always note the source environment in the cache file
- Do NOT overwrite a cached schema without noting the previous version — append a "Changed" note
- Flag any column that exists in the table but is undocumented in the instructions — it may be important

---

## Cached Schema Files

Once created, the following files in `memories/repo/` serve as the schema reference:

<!-- This list updates as schemas are verified -->
| Alias    | Cache File                                   | Last Verified |
|----------|----------------------------------------------|---------------|
| orders   | `memories/repo/schema-orders.md`             | [not yet]     |
| accounts | `memories/repo/schema-accounts.md`           | [not yet]     |
| billing  | `memories/repo/schema-billing.md`            | [not yet]     |
| events   | `memories/repo/schema-events.md`             | [not yet]     |
