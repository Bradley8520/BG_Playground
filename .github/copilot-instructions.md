# Copilot Instructions

> Auto-injected into every GitHub Copilot Chat session in this workspace.
> Fill in the REPLACE sections with your domain-specific details.
> Reference skill files for deep procedural knowledge: `skills/<capability>/SKILL.md`

---

## Domain Context

<!-- REPLACE: Describe your business domain in 2-3 sentences -->
This workspace supports [DOMAIN — e.g., "telecom billing analytics for consumer accounts"].
Primary data platform: [PLATFORM — e.g., "Teradata / Databricks / SQL Server"].
Primary language for data work: SQL (ANSI / Teradata SQL / T-SQL).

---

## Source Tables (Fully Qualified)

<!-- REPLACE: Add your actual fully qualified table names -->
| Alias    | Fully Qualified Name                      | Description                    |
|----------|-------------------------------------------|--------------------------------|
| orders   | `PROD_DB.SCHEMA_NAME.ORDERS`              | Customer order records         |
| accounts | `PROD_DB.SCHEMA_NAME.ACCOUNT_MASTER`      | Master account registry        |
| billing  | `PROD_DB.SCHEMA_NAME.BILLING_SUMMARY`     | Monthly billing aggregates     |
| events   | `PROD_DB.SCHEMA_NAME.USAGE_EVENTS`        | Raw usage/event log            |

**Rule:** Always use fully qualified names in generated SQL. Never use aliases as table names in production queries.

---

## Key Field Definitions & Valid Values

<!-- REPLACE: Define your important fields and their allowed values -->

### `STATUS_CD`
- `A` = Active
- `S` = Suspended
- `T` = Terminated
- `P` = Pending

### `ACCT_TYPE`
- `R` = Residential
- `B` = Business
- `G` = Government
- `W` = Wholesale

### `BILLING_CYCLE`
- Integer 1–31 representing day-of-month billing closes

### `PROD_CD` (Product Code)
- Prefix `WL` = Wireless
- Prefix `BB` = Broadband
- Prefix `TV` = Video/TV
- Prefix `LN` = Landline

---

## Standard Filters (Always Apply)

<!-- REPLACE: Define filters that should appear in every query unless explicitly overridden -->

```sql
-- Active records only (unless query explicitly asks for all statuses)
WHERE STATUS_CD = 'A'
-- Exclude test accounts
  AND ACCT_ID NOT LIKE 'TEST%'
  AND ACCT_ID NOT LIKE '9999%'
-- Standard date range (last 13 months unless specified)
  AND BILL_DT >= ADD_MONTHS(CURRENT_DATE, -13)
```

**Anti-pattern:** Never run unbounded queries on `USAGE_EVENTS` without a date filter — the table is partitioned by `EVENT_DT` and full scans cause cluster contention.

---

## Business Classification Logic

<!-- REPLACE: Document your key business rules for classifying data -->

### Customer Tier Classification
```
monthly_revenue >= 500  → Tier 1 (Enterprise)
monthly_revenue >= 100  → Tier 2 (SMB)
monthly_revenue >= 20   → Tier 3 (Consumer)
ELSE                    → Tier 4 (Low-Value)
```

### Churn Definition
A customer is considered churned if:
- `STATUS_CD` changed from `A` → `T` within the measurement period
- AND no reactivation within 30 days

### MRC vs OTC
- MRC (Monthly Recurring Charge): `CHARGE_TYPE_CD IN ('MRC','BASE','FEAT')`
- OTC (One-Time Charge): `CHARGE_TYPE_CD IN ('OTC','INST','DISC')`

---

## Known Gotchas & Anti-Patterns

1. **NULL handling in joins** — `ACCT_ID` can be NULL in `USAGE_EVENTS` for pre-activation events. Always use `COALESCE(ACCT_ID, 'UNKNOWN')` or filter NULLs explicitly.
2. **Date arithmetic** — Use `ADD_MONTHS()` not date subtraction for month-based ranges; subtraction gives inaccurate results at month boundaries.
3. **DISTINCT vs GROUP BY** — Prefer `GROUP BY` over `SELECT DISTINCT` on large tables; optimizer handles it better.
4. **Case sensitivity** — All string values in this database are uppercase. Never compare with mixed-case literals.
5. **Temp tables** — Use `CREATE VOLATILE TABLE` (Teradata) or `#temp` (T-SQL) prefix for session-scoped temp tables. Do not use CTEs for large intermediate datasets.
6. **Taxonomy — apostrophe collision in bulk conversions** — Never use `'` as a delimiter when processing taxonomy definition text. Contractions (`didn't`, `can't`, etc.) contain apostrophes and will be split, corrupting 20–25% of definitions. Use pipe `|`, tab, or multi-char sequence `;;` instead. After any bulk conversion, run a scan for truncated contraction artifacts (`"didn",`, `"can",`, `"wasn",` in phrase lists). See `skills/taxonomy/SKILL.md` for full detection pattern.
7. **Taxonomy — PowerShell .ps1 encoding** — Never save taxonomy edit scripts as `.ps1` files when definitions contain `—` or `→`; Windows reads them as Latin-1 and corrupts Unicode. Run inline in terminal instead.

---

## Trigger Phrases → Workflows

When I type these phrases, follow the associated workflow:

| Trigger Phrase             | Workflow to Follow                                                   |
|----------------------------|----------------------------------------------------------------------|
| `write a query for [X]`    | Load `skills/sql-writing/SKILL.md` — multi-step SQL generation protocol |
| `deploy [env]`             | Load `skills/deploy/SKILL.md` — deployment checklist and confirmation flow |
| `refresh metadata`         | Load `skills/metadata-refresh/SKILL.md` — schema discovery protocol |
| `ad hoc: [question]`       | Load `skills/ad-hoc-query/SKILL.md` — rapid query + explain workflow |
| `taxonomy: [X]`            | Load `skills/taxonomy/SKILL.md` — taxonomy build, edit, conversion & definition standards |
| `export as Word` / `save as Word doc` / `convert to Word` | Load `skills/doc-export/SKILL.md` — markdown-to-Word conversion process |
| `that fixed it`            | Offer to capture session learnings and update the handoff document   |
| `wrap up` / `end session`  | Generate a session handoff using `handoffs/TEMPLATE.md`; also trigger skills assessment summary if session was substantive |
| `what did we do today`     | Summarize all changes, decisions, and learnings from this session    |
| `show me the checklist`    | Display the relevant checklist for the current task context          |
| `start session` / `new session` / `where did we leave off` | Load `skills/session-start/SKILL.md` — session startup checklist |
| `assess my skills` / `run my assessment` / `skills review` / `how am I doing` | Load `skills/skills-assessment/SKILL.md` — Gen AI skills evaluation |
| `review my workspace` / `workspace cleanup` / `folder review` / `am I organized` | Load `skills/workspace-review/SKILL.md` — folder/file hygiene review |
| `explain that` / `teach me` / `why did you do it that way` / `is there a better way` / `quiz me` | Load `skills/learning-coach/SKILL.md` — coaching and learning mode |
| `verbatim: [X]` / `analyze verbatims` | Load `skills/verbatim-analysis/SKILL.md` — verbatim analysis workflow |
| `prompt coaching` / `prompt tip` / `advanced prompting` | Load `skills/advanced-prompting/SKILL.md` — advanced prompting technique coaching and practice |

---

## Skills Reference

Load these files when tasks match their domain:

- `skills/sql-writing/SKILL.md` — Writing optimized SQL queries
- `skills/deploy/SKILL.md` — Deployment procedures and checklists
- `skills/metadata-refresh/SKILL.md` — Schema/metadata discovery and caching
- `skills/ad-hoc-query/SKILL.md` — Rapid ad-hoc data exploration
- `skills/taxonomy/SKILL.md` — VOC taxonomy build, edit, conversion standards, and known gotchas
- `skills/doc-export/SKILL.md` — Convert any markdown output to a formatted, print-ready Word document
- `skills/advanced-prompting/SKILL.md` — Advanced prompting techniques, weekly practice protocol, and benchmarks
- `skills/learning-coach/SKILL.md` — Active learning coaching behaviors; loads on coaching trigger phrases
- `skills/skills-assessment/SKILL.md` — Gen AI skills evaluation framework; run weekly or on request
- `skills/workspace-review/SKILL.md` — Folder/file hygiene checklist; run weekly or on request
- `skills/verbatim-analysis/SKILL.md` — Customer verbatim analysis and classification workflow
- `skills/python-scripts/SKILL.md` — Python environment facts, conventions, and reusable patterns
- `skills/session-start/SKILL.md` — Session startup checklist to restore context and set goals

---

## Coaching Behavior (Always Active)

Copilot acts as a learning coach in all sessions. See `skills/learning-coach/SKILL.md` for full protocol. Summary:
- After non-trivial tasks: add a brief "Coach note" if a better approach exists
- Name techniques and patterns when using them
- Ask one reflection question after completing complex work
- Flag when a repeated pattern should be codified as a skill
- Never block task completion to coach — finish first, then teach

---

## Maintenance Rules (Always Apply)

**Trigger Phrase Reference Doc:** `docs/Trigger_Phrases_Reference.md`
- Whenever a new skill file is created, add it to both the **Skills Reference** section above AND `docs/Trigger_Phrases_Reference.md` (Skills Reference section at bottom).
- Whenever a new trigger phrase is added to the table above, add a full entry to `docs/Trigger_Phrases_Reference.md` with: what it does, skill loaded, what to expect, and an example.
- Keep the Quick Reference Card table at the bottom of `docs/Trigger_Phrases_Reference.md` in sync with the trigger phrase table above.
- Update the `Last updated:` date in `docs/Trigger_Phrases_Reference.md` whenever it is changed.

---

## Coding Conventions

- **SQL style:** UPPERCASE keywords, lowercase aliases, 4-space indentation
- **Column aliases:** Descriptive snake_case (`customer_id`, not `c` or `cust_id`)
- **Comments:** Add a `-- Purpose:` comment at the top of every generated query
- **Version control:** Never commit or push without showing a diff first
- **Testing:** Always confirm tests pass before any deploy action

---

## Terminology Reference

| My Term              | Meaning                                         |
|----------------------|-------------------------------------------------|
| "prod"               | Production environment                          |
| "staging" / "stage"  | Pre-production / UAT environment                |
| "dev"                | Local development environment                   |
| "the cluster"        | [REPLACE: your data platform cluster name/URL]  |
| "the pipeline"       | [REPLACE: your ETL/data pipeline name]          |
