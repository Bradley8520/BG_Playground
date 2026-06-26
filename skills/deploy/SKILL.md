# Skill: Deployment

## When to Use This Skill
Activate when the user says `deploy [env]`, `push to [env]`, `go live`, or any deployment-related request.

---

## Pre-Deployment Checklist

Run through every item before executing any deploy command. Do not skip steps.

### 1. Show Pending Changes
```bash
git status
git diff --staged
```
Present the full diff to the user. Do not proceed until they confirm: **"changes look good"**.

### 2. Test Confirmation
Ask explicitly: **"Have all tests passed? (yes / no)"**
- If no → Stop. Do not deploy.
- If yes → Proceed to step 3.

### 3. Secrets & Credentials Check
Scan staged files for:
- Hardcoded passwords, API keys, tokens
- Connection strings with embedded credentials
- Files ending in `.env`, `.key`, `.pem` that should not be committed

If any found → Stop and alert the user.

### 4. Confirm Target Environment
Ask: **"Deploying to dev, staging, or prod?"**

| Environment | Required Confirmation |
|---|---|
| dev | None — proceed after test confirmation |
| staging | User must type "confirmed" |
| prod | User must type "confirmed for production" |

### 5. Execute Deploy
Run the environment-specific command (see Terminology Reference in `.github/copilot-instructions.md` for actual commands).

### 6. Verify Success
Check deploy output for errors. Confirm the deployment endpoint/service is responding.

---

## Post-Deployment Steps

1. Note what was deployed, to which environment, and at what time
2. Offer to update the session handoff (`handoffs/YYYY-MM-DD.md`) with deploy details
3. If issues arise, offer to create a rollback checklist

---

## Rollback Protocol

If a deployment causes issues:
1. Do NOT attempt a hotfix deploy without running the full pre-deployment checklist
2. Revert to last known-good state:
   ```bash
   git revert HEAD
   ```
   or use environment-specific rollback command
3. Document the issue in the session handoff under "Known Issues"

---

## Pitfalls to Avoid

- **Never** use `git push --force` without explicit user permission
- **Never** use `--no-verify` to bypass git hooks without telling the user
- **Never** assume dev and staging share the same database schema
- **Never** default to prod — always confirm the target environment
- **Never** deploy with uncommitted local changes that haven't been reviewed

---

## Environment Reference

<!-- REPLACE: Fill in your actual deploy commands and environment details -->

| Environment | Deploy Command | URL / Endpoint |
|---|---|---|
| dev | `[REPLACE: dev deploy command]` | `[REPLACE: dev URL]` |
| staging | `[REPLACE: staging deploy command]` | `[REPLACE: staging URL]` |
| prod | `[REPLACE: prod deploy command]` | `[REPLACE: prod URL]` |
