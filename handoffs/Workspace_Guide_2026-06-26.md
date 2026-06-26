# BG_Playground Workspace Guide
**Date:** June 26, 2026

---

## Your Workspace — What Everything Is and Does

---

### GitHub Repository (`BG_Playground`)

This is the **version-controlled backup and history** of your entire workspace. Think of it as a cloud save plus a complete audit trail. Every file you commit is tracked — you can always roll back to any previous state. It also lets Copilot read your repo context (branch, owner, diffs) to give smarter answers.

**Rule of thumb:** Anything you'd be upset to lose should be committed.

---

### Commits

A **commit is a labeled snapshot** of your files at a point in time. Good commits are small, focused, and have a meaningful message like `"Add Shop_Purchase subtopics v2"` rather than `"updates"`. You should commit after completing a logical unit of work — finishing a script, updating a taxonomy version, building a new skill. You never need to commit everything at once.

---

### Handoff Docs (`handoffs/`)

These are **session memory for your future self** (and Copilot). Because each chat session starts with no memory of prior work, handoffs bridge the gap.

| Action | When |
|--------|------|
| **Create** | Type `wrap up` at the end of any session where meaningful work was done |
| **Update** | Never — each handoff is a dated snapshot, not a living doc |
| **Archive/Obsolete** | Leave old ones in place; they are a log. Only delete if they contain sensitive data |
| **Reference** | Paste the most recent handoff into a new chat to restore full context instantly |

Your `TEMPLATE.md` is the master form. Completed handoffs should be named `YYYY-MM-DD.md` (e.g., `2026-06-26.md`).

---

### Project Folders (`projects/`)

Each subfolder under `projects/` is a **self-contained unit of work** — its own scripts, data, outputs, prompts, and docs. Your current structure (`projects/voc-taxonomy/`) is correct. Add new top-level folders here when you start genuinely new work (e.g., `projects/billing-analytics/`, `projects/churn-model/`).

---

### README.md Files (Three Levels)

| Location | Purpose | Read First? |
|----------|---------|-------------|
| **Root** `README.md` | Describes the whole repo — structure, conventions, what's here | Yes — Copilot reads this to orient itself |
| **`projects/voc-taxonomy/README.md`** | Explains that specific project — goals, file map, current status | Yes — paste into chat when starting project work |
| **`handoffs/README.md`** | Instructions for using the handoff system | Reference only |

Think of `README.md` files as **the briefing you'd give a new team member** before they touched that folder. Copilot uses them too — a well-written README means better, more accurate suggestions.

---

### Skills (`skills/`)

Skills are **instruction files that tell Copilot exactly how to perform a specific type of task** in your domain. They are not code — they are procedural knowledge written in plain English markdown.

**Your current skills:**

| Skill | What It Does |
|-------|-------------|
| `taxonomy/SKILL.md` | Rules for building, editing, and converting VOC taxonomy files |
| `sql-writing/SKILL.md` | Step-by-step protocol for writing queries against your tables |
| `ad-hoc-query/SKILL.md` | Rapid data exploration workflow |
| `deploy/SKILL.md` | Deployment checklist |
| `metadata-refresh/SKILL.md` | Schema discovery process |

**When to create a new skill:** When you find yourself re-explaining the same context repeatedly in new chats, or when a task has specific rules, gotchas, or a defined process. Good candidates: `reporting/`, `verbatim-analysis/`, `python-scripts/`.

**Copilot will suggest codifying a skill** when it notices patterns — that is a good signal to act on.

---

### Prompts

| Type | Location | Purpose |
|------|----------|---------|
| **Copilot chat prompts** (`.prompt.md`) | `.github/prompts/` | Reusable chat commands you can invoke with `/` in VS Code Copilot |
| **LLM classification prompts** (`.txt`) | `projects/voc-taxonomy/prompts/` | The actual prompt text sent to GPT/Claude to classify verbatims |

Keep classification prompts inside the project folder (they are project-specific). Keep Copilot slash-command prompts in `.github/prompts/` (they are workspace-wide tools).

---

### `.github/copilot-instructions.md`

This is **the most important file in your repo**. It is automatically injected into every Copilot chat session. It contains your table names, field definitions, standard filters, business rules, and trigger phrases. Keep it current — it is your "standing briefing" to Copilot every single session.

---

## Starting a New Project — Step by Step

**Step 1 — Decide scope**

Is this a new topic? New data domain? New deliverable type? If yes, create a new project folder. If it is related to voc-taxonomy, add to that project.

**Step 2 — Create the folder structure**

```
projects/
  your-project-name/
    README.md        <- Write this first. Describe goal, data sources, outputs
    scripts/
    docs/
    output/          <- Add to .gitignore if outputs are large/sensitive
```

You can ask Copilot: *"scaffold a new project folder for [your project name]"* and it will create the structure for you.

**Step 3 — Update root README.md**

Add the new project to the Projects section so the repo stays accurate.

**Step 4 — Start a new chat**

Paste in:
- Your most recent handoff doc (context from last session)
- The new project README.md

You do NOT need to start a new chat just because it is a new project — but fresh chats equal clean context, which is often better for new work.

**Step 5 — Skills**

Ask yourself: *"Does this project have unique rules Copilot keeps getting wrong?"*
If yes, create `skills/your-project/SKILL.md` and add a trigger phrase to `.github/copilot-instructions.md` so it loads automatically.

**Step 6 — Prompts**

- Store LLM prompts (for classification scripts) in `projects/your-project/prompts/`
- Store reusable Copilot slash-commands in `.github/prompts/`

**Step 7 — End of session**

Type `wrap up` → save handoff as `handoffs/YYYY-MM-DD.md` → commit everything.

---

## Quick Reference Card

| File or Folder | One-Liner |
|----------------|-----------|
| `.github/copilot-instructions.md` | Auto-injected briefing — most important file |
| `skills/` | How-to procedures for Copilot (domain knowledge) |
| `handoffs/` | Session memory — bridge between chats |
| `projects/` | Self-contained work units |
| `README.md` | Human and AI orientation doc for that folder |
| `.github/prompts/` | Reusable slash commands for Copilot chat |
| `projects/*/prompts/` | LLM prompt files used in scripts |
| Commits | Dated snapshots — small, frequent, meaningful messages |

---

## The Single Most Impactful Habit

End every session with `wrap up`, save the handoff, and commit. That one habit compounds into a powerful, reliable working memory system across all future sessions.
