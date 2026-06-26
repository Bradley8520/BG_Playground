# Advanced Prompting — Skill File

> **Goal:** Make leading-edge prompting technique a *daily work habit*, not just theory.
> Each section includes the technique, when to use it, and a concrete example from your actual work.
> Trigger: `prompt coaching` / `prompt tip` / `advanced prompting`

---

## My Prompting Goal

> *"I want to reach 'Leading Edge' on the advanced-prompting benchmark within 90 days by applying one new technique per week to real work tasks."*

Milestones:
- **Day 0 (baseline):** Run `assess my skills` to establish starting score
- **Day 30:** Reach "Advanced" tier — RCTF + CoT + Few-Shot are default habits
- **Day 60:** Using prompt chaining and verification loops consistently in real work
- **Day 90:** Reach "Leading Edge" — building reusable templates, using meta-prompting, adversarial review

---

## Coaching Protocol (Active Every Session)

When this skill is loaded, Copilot will:
1. Name the technique being used whenever it applies one
2. Suggest a *better prompt* if your prompt could be improved — shown as a "Prompt upgrade:" callout
3. Introduce one new technique per session if the conversation is substantive
4. Challenge you to rewrite a prompt using a specific technique on request (`quiz me` + this skill)

---

## Technique Library

### Tier 1 — Foundation (Master These First)

---

#### 1. Role + Context + Task + Format (RCTF)
**What it is:** The four-part structure that underpins almost every high-quality prompt.
- **Role** — Who should Copilot act as?
- **Context** — What background does it need?
- **Task** — What specific action should it take?
- **Format** — How should the output be structured?

**Example (weak):** `Write a query for churned accounts`

**Example (RCTF):**
```
Role: You are a senior Teradata SQL analyst.
Context: STATUS_CD = 'T' means terminated. Churn = STATUS_CD flipped from A → T
         with no reactivation within 30 days. Table: PROD_DB.SCHEMA.ACCOUNT_MASTER.
Task: Write a query that counts churned accounts by ACCT_TYPE for the last 13 months.
Format: UPPERCASE keywords, snake_case aliases, -- Purpose: comment at top, 4-space indent.
```

**When to use:** Any time you need accurate, production-quality output. This is your default prompt structure.

---

#### 2. Chain-of-Thought (CoT)
**What it is:** Ask the model to reason step by step before giving a final answer. Dramatically improves accuracy on complex problems.

**How to trigger it:** Add one of these to your prompt:
- `"Think through this step by step before answering."`
- `"Walk me through your reasoning before giving the final answer."`
- `"First, identify what we know. Then reason through it. Then give the answer."`

**Example:**
```
I have a taxonomy node called "Billing > Payment > Failed Payment". A customer verbatim says
"I keep getting charged twice but the second charge disappears after a few days."
Think through this step by step: what topic(s) apply, and why? Then give your classification.
```

**When to use:** Classification decisions, SQL logic with multiple joins, debugging, any problem where "right on first try" matters.

---

#### 3. Few-Shot Prompting
**What it is:** Provide 2–4 examples of input → output before asking for the real thing. The model learns your pattern and style from the examples.

**Example (verbatim classification):**
```
Classify each verbatim as the best-fitting taxonomy topic.

Example 1:
Verbatim: "The agent was rude and didn't listen to me."
Classification: People > Agent Behavior > Attitude/Tone

Example 2:
Verbatim: "I was on hold for 45 minutes."
Classification: People > Agent Behavior > Hold Time

Now classify:
Verbatim: "She talked over me the whole time and never let me finish."
Classification:
```

**When to use:** Any classification task. Any output where style/format consistency matters. Taxonomy work, verbatim analysis.

---

#### 4. Constraint Prompting (Negative Prompting)
**What it is:** Explicitly tell the model what NOT to do. Prevents the most common failure modes before they happen.

**Example:**
```
Write a Teradata SQL query for active wireless accounts.
Do NOT use SELECT DISTINCT — use GROUP BY instead.
Do NOT use date subtraction for month ranges — use ADD_MONTHS().
Do NOT include test accounts (ACCT_ID LIKE 'TEST%' or '9999%').
```

**When to use:** Anytime you know the common failure modes. Pair with RCTF for maximum precision.

---

### Tier 2 — Intermediate (Develop Over Next 30 Days)

---

#### 5. Prompt Chaining
**What it is:** Break a complex task into sequential prompts where each output feeds the next. More reliable than one massive prompt.

**Pattern:**
```
Step 1: "List all the taxonomy categories that could apply to this verbatim."
Step 2: "Of those categories, which best fits based on the primary complaint?"
Step 3: "Write a confidence score and brief rationale for that classification."
```

**When to use:** Multi-step analysis (taxonomy build, verbatim analysis pipeline), anywhere a single prompt produces messy output.

---

#### 6. Self-Consistency Prompting
**What it is:** Ask for multiple independent answers to the same question, then take the most consistent one. Especially useful for classifications where you're not certain.

**How to do it:**
```
Give me 3 independent classifications for this verbatim, reasoned separately,
then tell me which classification appeared most often and why.

Verbatim: "The website kept timing out when I tried to pay my bill."
```

**When to use:** High-stakes classification decisions. Verifying edge cases in taxonomy design.

---

#### 7. Iterative Refinement ("That's close, but...")
**What it is:** A prompting *habit*, not a technique. Instead of accepting a near-miss output, explicitly describe the gap and ask for targeted revision.

**Pattern:**
```
"That's close, but [specific thing that's wrong]. Keep [what's right]. Change [specific fix]."
```

**Example:**
```
That's close, but the WHERE clause is missing the test account filter.
Keep the GROUP BY and the date range logic. Add:
AND ACCT_ID NOT LIKE 'TEST%'
AND ACCT_ID NOT LIKE '9999%'
```

**When to use:** After any first-draft output. This is the habit that separates fast users from precise users.

---

#### 8. Verification / Critic Loop
**What it is:** After getting an answer, ask the model to critique its own output.

**How to trigger it:**
- `"Now review your answer. What assumptions did you make? What could be wrong?"`
- `"Act as a critic. What are the 3 most likely flaws in what you just produced?"`
- `"Check your SQL for the gotchas in the copilot-instructions.md. What did you miss?"`

**When to use:** Before using any generated SQL in production. After complex taxonomy decisions. Whenever stakes are high.

---

### Tier 3 — Advanced (Leading Edge)

---

#### 9. Meta-Prompting
**What it is:** Ask the model to *write a better prompt* than the one you have. Use Copilot to improve your prompting.

**Example:**
```
Here's my prompt: "Write a query for churn."
Rewrite this as a production-quality RCTF prompt using the conventions in copilot-instructions.md.
Then explain what you changed and why.
```

**When to use:** When you're not sure how to frame a complex request. Use the output as a template for future similar tasks. Builds your prompting vocabulary fast.

---

#### 10. Persona + Adversarial Prompting
**What it is:** Ask the model to take an opposing or expert-skeptic role to stress-test your work.

**Examples:**
```
"Act as a skeptical data analyst reviewing this SQL. Find every assumption that could be wrong."
"Act as a taxonomy SME who thinks this classification is wrong. Argue against it."
"Act as a stakeholder who will reject this output. What objections will they raise?"
```

**When to use:** Before presenting taxonomy designs to stakeholders. Reviewing SQL before it goes to production. Any output that will be challenged.

---

#### 11. Structured Output Prompting
**What it is:** Instruct the model to return output in a specific machine-readable or presentation-ready format.

**Examples:**
```
Return your answer as a markdown table with columns: Verbatim | Topic | Subtopic | Confidence | Rationale

Return the classification as JSON:
{
  "topic": "",
  "subtopic": "",
  "confidence": 0.0,
  "rationale": ""
}
```

**When to use:** When output feeds another process (Python script, Excel paste, stakeholder table). Taxonomy batch classification. Any output that will be reformatted.

---

#### 12. Context Window Management
**What it is:** Deliberately loading the right context at the start of a session so every prompt in that session inherits it.

**Pattern:**
```
"Here is the session context. Reference this for all prompts this session:
- Active project: VOC Taxonomy V5
- Taxonomy file: VOC_Classification_Taxonomy_v4.csv
- Known issues: [paste relevant gotchas]
- My constraints: [paste standard filters]"
```

**When to use:** At the start of every complex work session. Pair with `start session` trigger phrase. Reduces repetitive context-setting across prompts.

---

#### 13. Prompt Templates (Parameterized Prompts)
**What it is:** Pre-written prompts with `[VARIABLE]` placeholders that you fill in. Turns your best prompts into repeatable tools.

**Example template (verbatim classification):**
```
You are a VOC taxonomy analyst for a telecom company.
Classify the following verbatim according to the [TAXONOMY_VERSION] taxonomy.
Topic candidates: [TOPIC_LIST]
Verbatim: "[VERBATIM_TEXT]"
Return: Topic | Subtopic | Confidence (H/M/L) | One-sentence rationale
Do NOT invent taxonomy nodes that don't exist in the list above.
```

**When to use:** Any task you run more than 3 times. Build a `prompts/` folder of your best templates. This is how you scale your prompting skill into a personal prompt library.

---

## Weekly Practice Protocol

Each week, pick one technique from this file and consciously apply it to a real work task:

| Week | Technique to Practice | Work Task to Apply It To |
|------|----------------------|--------------------------|
| 1 | RCTF structure | Rewrite your most-used SQL prompt |
| 2 | Chain-of-Thought | Verbatim classification pipeline |
| 3 | Few-Shot | Build a batch classification prompt |
| 4 | Verification Loop | Review generated SQL before using it |
| 5 | Meta-Prompting | Improve a prompt that gave weak output |
| 6 | Persona/Adversarial | Stress-test a taxonomy design decision |
| 7 | Prompt Templates | Write 3 reusable templates for your work |
| 8+ | Review and level up | Reassess with `assess my skills` |

---

## "Prompt Upgrade" Callout Format

When Copilot spots an improvable prompt, it will show:

> **Prompt upgrade:** Your prompt was `[original]`. A stronger version using `[technique]` would be:
> `[improved prompt]`
> This matters because: `[brief reason]`

---

## Benchmarks — What "Advanced" Looks Like

| Level | Description |
|-------|-------------|
| Beginner | One-line prompts, accepts first output, no iteration |
| Intermediate | Uses RCTF, iterates with feedback, knows when CoT helps |
| Advanced | Chains prompts, uses templates, applies verification loops, builds a prompt library |
| Leading Edge | Meta-prompts to improve own prompts, uses adversarial review, contributes reusable templates, systematically tests techniques on real work |

**Target:** Reach "Advanced" in 30 days, "Leading Edge" in 90 days through the weekly practice protocol above.

---

## Quick-Reference: Technique Cheat Sheet

| Technique | One-liner trigger |
|-----------|------------------|
| RCTF | Role, Context, Task, Format — always |
| Chain-of-Thought | "Think through this step by step" |
| Few-Shot | Provide 2–4 examples before asking |
| Constraint | "Do NOT..." |
| Prompt Chaining | Break into Step 1 → Step 2 → Step 3 |
| Self-Consistency | "Give me 3 independent answers" |
| Iterative Refinement | "That's close, but..." |
| Verification Loop | "Now critique your own answer" |
| Meta-Prompting | "Rewrite this as a better prompt" |
| Adversarial | "Act as a skeptic and challenge this" |
| Structured Output | "Return as a markdown table / JSON" |
| Context Loading | Load context at session start |
| Prompt Templates | `[VARIABLE]` placeholders in saved prompts |
