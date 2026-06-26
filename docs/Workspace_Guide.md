# BG_Playground Workspace Guide

> **Living document** — updated automatically whenever the workspace structure changes.
> Last updated: 2026-06-26
> For session-specific context, see `handoffs/` dated files.

---

## Your Workspace — What Everything Is and Does

---

### GitHub Repository (`BG_Playground`)

This is the **version-controlled backup and history** of your entire workspace. Think of it as a cloud save plus a complete audit trail. Every file you commit is tracked — you can always roll back to any previous state.

**Rule of thumb:** Anything you'd be upset to lose should be committed.

---

### Commits

A **commit is a labeled snapshot** of your files at a point in time. Good commits are small, focused, and have a meaningful message like `"feat: add Shop_Purchase subtopics v2"` rather than `"updates"`. Commit after completing a logical unit of work.

Your repo uses a **commit message template** (`.gitmessage`) — run `git commit` (no `-m`) and it will open with a pre-filled format in your editor. Types: `feat | fix | docs | chore | refactor`.

---

### Folder Map (Current State)

```
BG_Playground/
│
├── .github/
│   ├── copilot-instructions.md         ← Most important file. Auto-injected into every chat.
│   └── prompts/                        ← VS Code reusable prompt files (.prompt.md)
│       ├── deploy-checklist.prompt.md
│       ├── session-handoff.prompt.md
│       └── write-query.prompt.md
│
├── .vscode/
│   └── settings.json                   ← Workspace editor settings (font, rulers, tab sizes)
│
├── docs/                               ← Living reference documents (never dated, always current)
│   ├── Workspace_Guide.md              ← This file
│   └── Trigger_Phrases_Reference.md    ← All trigger phrases with full definitions
│
├── handoffs/                           ← Dated session memory (one file per session)
│   ├── assessments/                    ← Skills assessment snapshots (.md, dated — track progress)
│   │   └── 2026-06-26.md
│   ├── learning-log/                   ← [created on first coding lesson] lesson logs by date/language
│   ├── TEMPLATE.md                     ← Master form for wrap-up handoffs
│   ├── README.md                       ← Explains handoffs purpose and naming convention
│   └── [dated session handoffs .md]    ← Session_Handoff, VOC taxonomy, taxonomy V3/V4, etc.
│
├── projects/
│   └── voc-taxonomy/                   ← VOC taxonomy work (self-contained project)
│       ├── README.md
│       ├── docs/                       ← Project docs (.md)
│       │   └── *.md                    ← Care mapping, shop/purchase analysis, prompt guide, taxonomy revision notes
│       ├── output/                     ← gitignored: classification outputs (.txt)
│       ├── prompts/                    ← LLM prompt templates (.md)
│       ├── scripts/                    ← Python scripts (.py) + SQL queries (.sql)
│       │   ├── *.py                    ← classify_*, analyze_trust_subtopics2, build_*, sample_*, md_to_docx
│       │   ├── *.sql                   ← Retail_Store_Verbatims.sql, Classification_Hierarchy.sql
│       │   └── archive/                ← Superseded scripts (analyze_trust_subtopics.py v1)
│       ├── taxonomy/                   ← Master taxonomy files (.csv only)
│       │   └── *.csv                   ← VOC_Classification_Taxonomy v1–v4, V3 step files, results
│       └── verbatims/                  ← gitignored: raw verbatim data (.csv)
│
├── skills/                             ← Copilot workflow instruction files (.md)
│   ├── ad-hoc-query/SKILL.md
│   ├── advanced-prompting/SKILL.md
│   ├── coding-teacher/SKILL.md
│   ├── deploy/SKILL.md
│   ├── doc-export/SKILL.md
│   ├── learning-coach/SKILL.md
│   ├── metadata-refresh/SKILL.md
│   ├── python-scripts/SKILL.md
│   ├── session-start/SKILL.md
│   ├── skills-assessment/SKILL.md
│   ├── sql-writing/SKILL.md
│   ├── taxonomy/SKILL.md
│   ├── verbatim-analysis/SKILL.md
│   └── workspace-review/SKILL.md
│
├── .gitignore                          ← Excludes: *.docx, *.xlsx, verbatims/, output/, .venv/
├── .gitmessage                         ← Git commit message template (feat/fix/docs/chore/refactor)
├── .venv/                              ← gitignored: Python virtual environment (local only)
└── README.md                           ← Root repo overview
```

---

### `docs/` — Living Reference Documents

The `docs/` folder holds **reference material that stays current** — not session snapshots. Files here are updated automatically when the workspace changes.

| File | Updated When |
|------|-------------|
| `Workspace_Guide.md` | New folders, skills, tools, or structural changes |
| `Trigger_Phrases_Reference.md` | New trigger phrases or skill files are added |

**Rule:** If it's a one-time session record → `handoffs/`. If it should always be accurate → `docs/`.

---

### `handoffs/` — Session Memory

These are **dated snapshots** for your future self (and Copilot). Because each chat session starts with no memory of prior work, handoffs bridge the gap.

| Action | When |
|--------|------|
| **Create** | Type `wrap up` at the end of any session |
| **Use** | Paste the most recent handoff at the start of a new session (`start session`) |
| **Accumulate** | Leave old ones — they are a log, not a living doc |

Your `TEMPLATE.md` is the master form. Name completed handoffs `Session_Handoff_YYYY-MM-DD.md`.

---

### `projects/` — Work Units

Each subfolder is a **self-contained unit of work** with its own scripts, data, outputs, and docs.

**To add a new project:**
1. Create `projects/your-project-name/` with subfolders: `scripts/`, `docs/`, `output/`, `prompts/`, `taxonomy/` (as needed)
2. Write `projects/your-project-name/README.md` first — describe the goal, data sources, and outputs
3. Add `projects/your-project-name/output/` and `projects/your-project-name/verbatims/` to `.gitignore` if they contain large or sensitive files
4. Update this `Workspace_Guide.md` to add the new project to the Folder Map

---

### `skills/` — Copilot Instruction Files

Skills are **procedure files that tell Copilot exactly how to perform a task** in your domain. Not code — structured plain-English workflows.

| Skill | What It Does | Trigger Phrase |
|-------|-------------|---------------|
| `advanced-prompting/SKILL.md` | 13-technique prompting library, weekly practice protocol | `prompt coaching` / `prompt tip` |
| `ad-hoc-query/SKILL.md` | Rapid exploratory query workflow | `ad hoc: [question]` |
| `coding-teacher/SKILL.md` | Structured 15–30 min coding lessons using real workspace files (SQL → Python → PowerShell) | `coding lesson` / `walk me through [file]` / `teach me [X]` |
| `deploy/SKILL.md` | Deployment checklist with confirmation gate | `deploy [env]` |
| `doc-export/SKILL.md` | Convert markdown output to Word (.docx) | `export as Word` |
| `learning-coach/SKILL.md` | Standing coaching behaviors — active every session | `explain that` / `teach me` |
| `metadata-refresh/SKILL.md` | Schema discovery for tables | `refresh metadata` |
| `python-scripts/SKILL.md` | Python environment facts and conventions | *(auto-loaded by Copilot)* |
| `session-start/SKILL.md` | Session startup checklist to restore context | `start session` |
| `skills-assessment/SKILL.md` | 7-component Gen AI skills evaluation | `assess my skills` |
| `sql-writing/SKILL.md` | Multi-step SQL generation protocol | `write a query for [X]` |
| `taxonomy/SKILL.md` | VOC taxonomy build, edit, conversion rules | `taxonomy: [X]` |
| `verbatim-analysis/SKILL.md` | Customer verbatim classification workflow | `verbatim: [X]` |
| `workspace-review/SKILL.md` | Folder/file hygiene checklist | `review my workspace` |

**When to create a new skill:** When you find yourself re-explaining the same context in multiple chats, or when a task has specific rules and gotchas. Copilot will suggest this when it notices patterns.

**When you create a new skill:** Also add a trigger phrase to `.github/copilot-instructions.md` AND update `docs/Trigger_Phrases_Reference.md` AND this file's skills table.

---

### `.github/copilot-instructions.md`

**The most important file in the repo.** Auto-injected into every Copilot chat. Contains:
- Domain context and data platform
- Source table names (fully qualified)
- Key field definitions and valid values
- Standard SQL filters
- Business classification logic
- Known gotchas and anti-patterns
- All trigger phrases → skill file mappings
- Skills reference
- Coaching behavior rules
- Maintenance rules (what to update and when)

Keep it current. This is your "standing briefing" to Copilot every session.

---

### `.vscode/settings.json`

Workspace-scoped editor settings. Currently configured:
- **Font:** Cascadia Code with ligatures (monospace, optimized for SQL/code)
- **Rulers:** Vertical guides at 72 chars (commit body wrap) and 100 chars (code line limit)
- **SQL:** 4-space indentation
- **Python:** 4-space indentation
- **Whitespace:** Trim trailing whitespace on save

---

### `.gitmessage` — Commit Template

Pre-fills commit messages when you run `git commit` (without `-m`). Format:

```
<type>: <summary>

Types: feat | fix | docs | chore | refactor
```

---

### Installed Tools

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.14 | Scripts, classification, doc export |
| PowerShell | 7.6.3 (pwsh) | Terminal with PSReadLine + posh-git |
| Pandoc | 3.10 | Markdown → Word conversion (better formatting than python-docx) |
| python-docx | latest | Word doc generation from Python |

**Python path:** `C:/Users/bg763c/AppData/Local/Programs/Python/Python314/python.exe`
(Always use full path in PowerShell — `python` alone may not resolve correctly)

---

### VS Code Extensions (Installed)

| Extension | What It Does |
|-----------|-------------|
| GitHub Copilot | AI coding assistant |
| Rainbow CSV | Color-codes CSV columns — essential for taxonomy files |
| GitLens | Rich git history, blame, and diff explorer |
| Excel Viewer (GrapeCity) | View .xlsx files in VS Code |
| Error Lens | Inline error/warning display |
| Markdown Preview Enhanced | Better markdown rendering |
| SQLTools | SQL syntax and formatting |
| indent-rainbow | Color-codes Python indentation levels |
| Todo Tree | Collects TODO/FIXME comments into one panel |

---

## Starting a New Project

1. Create `projects/your-project-name/` with appropriate subfolders
2. Write `README.md` first — describe the goal, inputs, and outputs
3. Add sensitive/large output folders to `.gitignore`
4. If the project has unique rules → create `skills/your-project/SKILL.md`
5. If the skill has trigger phrases → update `.github/copilot-instructions.md` AND `docs/Trigger_Phrases_Reference.md` AND this file
6. Update the Folder Map in this file to show the new project
7. End every session with `wrap up` → commit → push

---

## Quick Reference Card

| File or Folder | One-Liner |
|----------------|-----------|
| `.github/copilot-instructions.md` | Auto-injected briefing — most important file |
| `docs/` | Living reference docs — always current |
| `docs/Workspace_Guide.md` | This file — updated when workspace changes |
| `docs/Trigger_Phrases_Reference.md` | All trigger phrases with full definitions |
| `skills/` | Copilot workflow instruction files (13 active) |
| `handoffs/` | Dated session snapshots — session memory |
| `projects/` | Self-contained work units |
| `README.md` files | Human + AI orientation for that folder |
| `.vscode/settings.json` | Editor font, rulers, tab settings |
| `.gitmessage` | Git commit template |
| Commits | Small, frequent, meaningful — use the template |

---

## The Single Most Impactful Habits

1. **End every session with `wrap up`** → save handoff → commit → push. Compounds into a reliable working memory system across all future sessions.
2. **Apply one new prompting technique per week** from `skills/advanced-prompting/SKILL.md`. Say `prompt coaching` to activate coaching mode.
