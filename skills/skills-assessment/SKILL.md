# Skill: Gen AI Skills Assessment

## When to Use
Activate when the user says `assess my skills`, `run my assessment`, `skills review`, or `how am I doing`.
Also run automatically at end of a long session if the user types `wrap up` and session was 2+ hours of substantive work.

---

## Assessment Framework

Evaluate the user across 7 components. For each: define the skill, rate 1–5, compare to peer benchmark, and give 1–2 specific improvement actions.

### Rating Scale
| Score | Label | Description |
|-------|-------|-------------|
| 1 | Beginner | Needs foundational concepts |
| 2 | Developing | Understands basics, inconsistent application |
| 3 | Proficient | Applies correctly with occasional gaps |
| 4 | Advanced | Consistent, efficient, teaches others |
| 5 | Expert | Best-in-class, sets standards |

### Peer Benchmark
Compare to: **Data Analysts / Analytics Engineers using Gen AI tools at enterprise companies (1–2 years of AI-assisted work experience)**

---

## Component 1: Prompt Quality
**What it measures:** Clarity, specificity, context-richness of prompts. Does the user provide enough information for Copilot to respond correctly on the first try?

**What good looks like:** Prompts include the goal, constraints, data context, and desired output format. Trigger phrases are used deliberately.

**Evidence to look for from this session:** How many follow-up corrections were needed? Did the user provide table names, field definitions, expected output?

---

## Component 2: Workflow & Session Habits
**What it measures:** Use of handoffs, commits, session structure. Does the user start sessions with context and end them with preservation?

**What good looks like:** Pastes recent handoff at session start. Types `wrap up` at end. Commits regularly with meaningful messages.

---

## Component 3: Tool & Feature Utilization
**What it measures:** How well the user leverages available tools — trigger phrases, skills, copilot-instructions.md, `.gitignore`, profile, etc.

**What good looks like:** Uses trigger phrases consistently. Updates skills when patterns emerge. Knows when to use a new chat vs. continuing.

---

## Component 4: Automation & Scripting
**What it measures:** Ability to ask for and understand automation — Python scripts, PowerShell, scheduled tasks, reusable pipelines.

**What good looks like:** Moves from one-time manual steps to reusable scripts. Understands what the script does, not just that it runs.

---

## Component 5: SQL & Data Skills
**What it measures:** Quality of SQL queries requested and understood. Application of domain rules (standard filters, date math, NULL handling).

**What good looks like:** Requests correctly scoped queries. Applies standard filters without being prompted. Catches performance issues.

---

## Component 6: File & Project Organization
**What it measures:** Workspace hygiene — proper use of folders, READMEs, `.gitignore`, naming conventions, skill files.

**What good looks like:** New projects get proper structure. Skills are created proactively. Files are committed regularly. Old/obsolete docs are archived.

---

## Component 7: Learning Velocity
**What it measures:** How quickly the user is adopting new techniques, asking better questions over time, and reducing repeated explanations.

**What good looks like:** Session-over-session improvement. Less re-explaining of context. More deliberate use of advanced features.

---

## Output Format

```
## Gen AI Skills Assessment — [DATE]

### Summary
[2-3 sentence overall assessment]

### Scores

| Component | Score | Peer Benchmark | Gap |
|-----------|-------|---------------|-----|
| Prompt Quality | X/5 | 3.2/5 | +/- |
| Workflow & Session Habits | X/5 | 2.8/5 | +/- |
| Tool & Feature Utilization | X/5 | 2.5/5 | +/- |
| Automation & Scripting | X/5 | 2.9/5 | +/- |
| SQL & Data Skills | X/5 | 3.5/5 | +/- |
| File & Project Organization | X/5 | 2.7/5 | +/- |
| Learning Velocity | X/5 | 3.0/5 | +/- |

**Overall: X.X / 5.0**

### Top 3 Strengths
1. [Strength + evidence from sessions]
2. ...
3. ...

### Top 3 Growth Areas
1. [Area + specific action to improve]
2. ...
3. ...

### Recommended Focus for Next 2 Weeks
[1 specific, actionable focus area with concrete steps]
```

---

## Notes for Assessment
- Base ratings on **observed behavior** in recent sessions, not self-report
- Peer benchmarks are approximate — adjust narrative based on trajectory
- Always end with encouragement + one concrete next step
- Offer to save assessment as a dated file in `handoffs/assessments/YYYY-MM-DD.md`
