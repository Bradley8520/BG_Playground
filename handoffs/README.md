# Session Handoffs

This folder stores end-of-session continuity documents so you can resume work exactly where you left off in a new chat session.

---

## How to Generate a Handoff

At the end of any session, type one of these trigger phrases in Copilot Chat:

- **`wrap up`**
- **`end session`**

Copilot will fill in `TEMPLATE.md` based on your session and save it as `handoffs/YYYY-MM-DD.md`.

---

## How to Resume from a Handoff

At the start of a new session, paste this into Copilot Chat:

```
Read the most recent file in handoffs/ and resume where we left off.
```

Copilot will:
1. Read the latest handoff document
2. Summarize what was accomplished
3. List the "Next Session — Pick Up Here" steps
4. Ask if you want to start on the first item

---

## File Naming Convention

`YYYY-MM-DD.md` — one file per work session  
If you have multiple sessions on the same day: `YYYY-MM-DD-2.md`, `YYYY-MM-DD-3.md`, etc.

---

## Retention

Keep the last **10** handoff files active in this folder.  
Archive older files to `handoffs/archive/` — do not delete them.
