---
mode: agent
description: Run through the full deployment checklist before deploying to any environment. Enforces review, test confirmation, and environment-appropriate approval gates.
---

# Deployment Checklist

Read and follow the full protocol in `skills/deploy/SKILL.md`.

## Target

${input:Which environment are you deploying to? (dev / staging / prod) — and briefly describe what you're deploying.}

## Checklist to Run (in order)

1. **Show diff** — run `git status` and `git diff --staged`, display the full output
2. **Await review** — wait for me to say "changes look good" before proceeding
3. **Test confirmation** — ask: "Have all tests passed?"
4. **Secrets scan** — check staged files for hardcoded credentials or secrets
5. **Environment confirmation gate:**
   - dev → no additional gate
   - staging → require me to type "confirmed"
   - prod → require me to type "confirmed for production"
6. **Execute deploy** — run the environment-specific command
7. **Verify success** — confirm the service/endpoint is responding
8. **Update handoff** — offer to log the deployment in `handoffs/YYYY-MM-DD.md`

## Rules

- Do NOT skip any checklist step
- Do NOT default to prod — always confirm the environment
- Do NOT use `git push --force` or `--no-verify` without explicit permission
- If tests have NOT passed → stop immediately, do not deploy
