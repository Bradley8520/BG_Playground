# Trigger Phrases Reference

> These phrases activate specific Copilot workflows or skill files automatically.
> Say them in any chat session and Copilot will load the associated behavior.
> Last updated: 2026-06-26

---

## How Trigger Phrases Work

Trigger phrases are shorthand commands you type in Copilot Chat. Instead of explaining what you need from scratch, you say a short phrase and Copilot automatically loads the right skill file and follows the defined workflow for that task. Think of them as keyboard shortcuts — but for AI behavior.

---

## Data & SQL

### `write a query for [X]`
**What it does:** Starts the full SQL generation protocol.
**Skill loaded:** `skills/sql-writing/SKILL.md`
**What to expect:** Copilot will ask clarifying questions about filters, joins, and output columns before writing anything. The query will follow all coding conventions (UPPERCASE keywords, snake_case aliases, `-- Purpose:` comment, standard filters applied).
**Example:** `write a query for active wireless accounts billed in the last 90 days`

---

### `ad hoc: [question]`
**What it does:** Rapid exploratory query with plain-English explanation.
**Skill loaded:** `skills/ad-hoc-query/SKILL.md`
**What to expect:** Copilot generates a quick query and explains it in plain English. Good for one-off lookups where you don't need a full protocol.
**Example:** `ad hoc: how many accounts have STATUS_CD = 'S' right now?`

---

### `refresh metadata`
**What it does:** Triggers schema and metadata discovery for a table or set of tables.
**Skill loaded:** `skills/metadata-refresh/SKILL.md`
**What to expect:** Copilot will walk through the schema discovery steps and cache the results for the session.
**Example:** `refresh metadata for USAGE_EVENTS`

---

## VOC Taxonomy

### `taxonomy: [X]`
**What it does:** Activates the full VOC taxonomy workflow — build, edit, conversion, and definition standards.
**Skill loaded:** `skills/taxonomy/SKILL.md`
**What to expect:** Covers everything from building new taxonomy nodes to converting definitions safely (with apostrophe-collision protection). Applies all known gotchas automatically.
**Example:** `taxonomy: add a new subtopic under Care > Billing > Payment Options`

---

### `verbatim: [X]` / `analyze verbatims`
**What it does:** Starts the customer verbatim analysis and classification workflow.
**Skill loaded:** `skills/verbatim-analysis/SKILL.md`
**What to expect:** Copilot will classify or analyze verbatim text using the current taxonomy, flag edge cases, and surface themes.
**Example:** `verbatim: classify these 50 comments from the April survey`
**Example:** `analyze verbatims`

---

## Output & Document Export

### `export as Word` / `save as Word doc` / `convert to Word`
**What it does:** Converts the current markdown output to a formatted, print-ready Word (.docx) file.
**Skill loaded:** `skills/doc-export/SKILL.md`
**What to expect:** Copilot will write a Python script using `python-docx`, run it with the full Python path, generate the `.docx` file locally, and confirm the file location. The `.docx` is gitignored (not committed to GitHub).
**Example:** `export as Word` (after any Copilot output)
**Example:** `save as Word doc`

---

## Session Management

### `start session` / `new session` / `where did we leave off`
**What it does:** Runs the session startup checklist to restore context and set a goal for the session.
**Skill loaded:** `skills/session-start/SKILL.md`
**What to expect:** Copilot will prompt you to paste the last handoff document, confirm the active project, load relevant skills, check git status, and set a session goal.
**Example:** `start session`

---

### `wrap up` / `end session`
**What it does:** Generates a session handoff document and optionally triggers a skills assessment summary.
**Template used:** `handoffs/TEMPLATE.md`
**What to expect:** Copilot summarizes everything done this session — files changed, decisions made, problems solved, and what's pending. Output can be saved as a handoff `.md` file.
**Example:** `wrap up`

---

### `what did we do today`
**What it does:** Quick summary of all changes, decisions, and learnings from the current session.
**What to expect:** A concise bullet-point recap — no skill file needed. Good for a mid-session check-in or before wrapping up.
**Example:** `what did we do today`

---

### `that fixed it`
**What it does:** Signals that a problem was solved — offers to capture the fix as a session learning and update the handoff document.
**What to expect:** Copilot will offer to document the root cause, the fix, and any pattern worth remembering. Good for capturing "aha moments" before you forget them.
**Example:** `that fixed it` (after resolving a bug or error)

---

## Checklists & Reviews

### `show me the checklist`
**What it does:** Displays the relevant checklist for whatever task is currently in progress.
**What to expect:** If you're writing SQL, you get the SQL checklist. If you're deploying, you get the deploy checklist. Context-aware.
**Example:** `show me the checklist`

---

### `deploy [env]`
**What it does:** Starts the deployment workflow with a confirmation gate before any action is taken.
**Skill loaded:** `skills/deploy/SKILL.md`
**What to expect:** Copilot runs through the deploy checklist, confirms the target environment, asks "Have tests passed?", and requires explicit typed confirmation before proceeding.
**Valid values for `[env]`:** `dev`, `staging`, `stage`, `prod`, `production`
**Example:** `deploy staging`

---

## Learning & Self-Improvement

### `explain that` / `teach me` / `why did you do it that way` / `is there a better way` / `quiz me`
**What it does:** Activates coaching and learning mode for the current topic.
**Skill loaded:** `skills/learning-coach/SKILL.md`
**What to expect:** Copilot will explain the technique used, name the pattern, offer an alternative if one exists, and may ask you a reflection question to reinforce the concept.
**Example:** `explain that` (after Copilot writes a SQL query)
**Example:** `is there a better way?`
**Example:** `quiz me on window functions`

---

### `assess my skills` / `run my assessment` / `skills review` / `how am I doing`
**What it does:** Runs a structured Gen AI skills evaluation across 7 dimensions.
**Skill loaded:** `skills/skills-assessment/SKILL.md`
**What to expect:** Scores you on Prompt Quality, Workflow Habits, Tool Utilization, Automation, SQL/Data Skills, File Organization, and Learning Velocity. Compares against a peer benchmark and recommends focus areas.
**Example:** `assess my skills`
**Example:** `how am I doing`

---

### `review my workspace` / `workspace cleanup` / `folder review` / `am I organized`
**What it does:** Runs the workspace hygiene checklist and flags anything that needs attention.
**Skill loaded:** `skills/workspace-review/SKILL.md`
**What to expect:** Checks handoffs, git commits, project folders, skills folder, `copilot-instructions.md`, and stale files. Outputs a green/yellow/red status table.
**Example:** `review my workspace`
**Example:** `am I organized`

---

### `prompt coaching` / `prompt tip` / `advanced prompting`
**What it does:** Loads the advanced prompting technique library and activates coaching mode for prompt improvement.
**Skill loaded:** `skills/advanced-prompting/SKILL.md`
**What to expect:** Copilot will introduce a technique, show how it applies to your current work, name techniques as it uses them, and offer "Prompt upgrade:" callouts when your prompt could be stronger. Includes a 13-technique library, weekly practice protocol, and benchmarks for reaching "Leading Edge" proficiency.
**Example:** `prompt coaching` (to start a coaching session on prompting)
**Example:** `prompt tip` (for a quick technique of the day)
**Example:** `advanced prompting` (to load the full technique library)

---

### `coding lesson` / `start a coding lesson`
**What it does:** Begins a structured 15–30 minute coding lesson using your real workspace files and data.
**Skill loaded:** `skills/coding-teacher/SKILL.md`
**What to expect:** Copilot asks which language/file (or suggests one), walks through a logical block of existing code in plain English, introduces 2–3 new concepts directly tied to that code, and ends with a hands-on practice task using your actual data. A learning log entry is offered at the end.
**Example:** `coding lesson` (Copilot picks a good starting file)
**Example:** `start a coding lesson` (same behavior)

---

### `walk me through [filename]`
**What it does:** Line-by-line (or block-by-block) walkthrough of a specific file in your workspace.
**Skill loaded:** `skills/coding-teacher/SKILL.md`
**What to expect:** Copilot opens the file, explains each logical block in plain English, names the commands used, and explains why the code is written that way. Pauses for questions throughout.
**Example:** `walk me through classify_taxonomy_v4_full.py`
**Example:** `walk me through Retail Store Verbatims.sql`

---

### `teach me [command or concept]`
**What it does:** Focused mini-lesson on a single command or concept, applied to your existing code.
**Skill loaded:** `skills/coding-teacher/SKILL.md`
**What to expect:** Copilot defines the concept, shows the syntax, connects it to real code you already have, and gives a small practice task. Faster than a full lesson — ~5–10 minutes.
**Example:** `teach me CASE WHEN`
**Example:** `teach me GROUP BY`
**Example:** `teach me how pandas reads a CSV`

---

### `coding practice`
**What it does:** Jumps straight to a practice exercise without a full walkthrough preamble.
**Skill loaded:** `skills/coding-teacher/SKILL.md`
**What to expect:** Copilot gives you a specific, small task to complete using your existing code. After your attempt, provides feedback and explains what happened.
**Example:** `coding practice` (Copilot picks an appropriate exercise based on recent lessons)

---

## Quick Reference Card

> Last updated: 2026-06-26

| Say This | Gets You |
|----------|---------|
| `write a query for [X]` | Full SQL generation protocol |
| `ad hoc: [question]` | Quick query + plain-English explanation |
| `refresh metadata` | Schema discovery for a table |
| `taxonomy: [X]` | VOC taxonomy build/edit workflow |
| `verbatim: [X]` / `analyze verbatims` | Verbatim classification workflow |
| `export as Word` / `save as Word doc` / `convert to Word` | Convert output to .docx file |
| `start session` / `new session` / `where did we leave off` | Session startup checklist |
| `wrap up` / `end session` | Session handoff document |
| `what did we do today` | Quick session recap |
| `that fixed it` | Capture a fix as a session learning |
| `show me the checklist` | Context-aware task checklist |
| `deploy [env]` | Deployment workflow with confirmation gate |
| `explain that` / `teach me` / `why did you do it that way` / `is there a better way` / `quiz me` | Coaching and learning mode |
| `assess my skills` / `run my assessment` / `skills review` / `how am I doing` | Gen AI skills evaluation |
| `review my workspace` / `workspace cleanup` / `folder review` / `am I organized` | Workspace hygiene review |
| `prompt coaching` / `prompt tip` / `advanced prompting` | Advanced prompting technique + coaching |
| `coding lesson` / `start a coding lesson` | 15–30 min structured lesson using your real code |
| `walk me through [filename]` | Block-by-block walkthrough of a specific file |
| `teach me [command/concept]` | Focused 5–10 min mini-lesson on one concept |
| `coding practice` | Jump straight to a practice exercise |
