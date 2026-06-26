# VOC Verbatim Classification — Prompt Authoring Guide

**Purpose:** Personal reference for writing and revising classification prompts fed to an LLM (GPT-4 / Claude) for multi-label verbatim tagging.
**Scope:** Applies to all themes across the 24-theme Care taxonomy and the expanded VOC_Classification_Taxonomy_v4 set.

---

## What We Learned from the 24-Theme Revision

The initial prompts were written as general intent descriptions. When tested against real verbatims, they produced consistent failure patterns:

| Failure Type | Root Cause | Example |
|---|---|---|
| Generic words triggering the wrong theme | No explicit exclusion of vague signal words | "great" triggering Rep Was Courteous instead of Rep Was Helpful |
| Adjacent theme bleed | No cross-theme routing rules | "problem not resolved" auto-tagging Rep Not Helpful when system policy caused the failure |
| Scope creep | No attribution anchor | "lied" (about AT&T generally) triggering Rep Not Courteous |
| Low recall | Narrow keyword list missed natural language variation | "Era 5" and "Q1=5" missed by Error Correction |
| Catch-all abuse | No Feedback used as fallback when no theme matched | Substantive unclassifiable comments silently labeled No Feedback |
| Semantic conflation | Ability gap vs effort gap not distinguished | "couldn't help" (knowledge) confused with "didn't help" (effort) |
| Language gap | Spanish verbatims not covered | Spanish demeanor words missed entirely |

Every revision in the file addressed one or more of these failure types. The patterns below codify what worked.

---

## Prompt Structure — Standard Template

Use this template for every prompt. All sections in `[brackets]` are required unless marked optional.

```
[THEME NAME] -> [CORE TRIGGER CONDITION]. [SCOPE ANCHOR if needed]. 
(including but not limited to: [word1], [word2], [word3], or similar [category descriptor]). 
[GENERIC EXCLUSION if applicable: GENERIC [X] ALONE (e.g., "[example1]," "[example2]") does NOT qualify unless accompanied by [required context].]
[CONDITIONAL RULE if applicable: IF [condition A] → classify as [Theme X]. [Condition B] ONLY when [discriminating factor].]
[EXCLUDE: [false positive source 1]. [false positive source 2 if applicable].]
[DEFAULT ROUTING if applicable: "[Ambiguous phrase]" defaults to [Theme A]; use [Theme B] ONLY when [distinguishing signal].]
Spanish equivalents (including but not limited to: [Spanish word1], [Spanish word2], or similar Spanish [category] words) also qualify.
```

### Annotated Example

```
Rep Was Courteous -> Customer uses SPECIFIC DEMEANOR WORDS describing the 
representative's manner, tone, or interpersonal behavior              ← CORE TRIGGER
(including but not limited to: polite, friendly, nice, kind, respectful, 
professional, patient, pleasant, or similar demeanor descriptors).    ← QUALIFYING WORD LIST
GENERIC PRAISE ALONE (e.g., "great," "fantastic," "excellent") does NOT qualify 
unless accompanied by a demeanor descriptor.                          ← GENERIC EXCLUSION
This theme measures HOW the rep interacted, not WHAT they accomplished.  ← SCOPE ANCHOR
Spanish equivalents (including but not limited to: amable, cortés, educado, 
or similar Spanish demeanor words) also qualify.                      ← LANGUAGE COVERAGE
```

---

## Formatting Rules

### 1. Opening line format
Always use:
```
[Theme Name] -> [Trigger condition starting with "Customer..."]
```
- Use `->` as separator (not `—`, `–`, `:`, or `—>`).
- Start the definition with `Customer` to anchor the prompt in the customer's perspective.
- The trigger condition should state the **minimum required signal**, not just intent.

### 2. Capitalization convention
Use ALL CAPS for:
- Key constraint terms: `SPECIFIC`, `GENERIC`, `EXCLUDE`, `ONLY`, `DO NOT`, `MUST`
- Required elements: `CURRENT REP`, `BEFORE`, `AFTER`, `UNEXPECTED`
- Logical operators embedded in prose: `IF PROBLEM WAS RESOLVED →`, `DO NOT auto-classify`

Do not ALL CAPS entire sentences — use it surgically for the decision-critical word or phrase.

### 3. Qualifying word lists
Always use the formula:
```
(including but not limited to: word1, word2, word3, or similar [category] descriptors)
```
- **"including but not limited to"** signals the LLM the list is illustrative, not exhaustive.
- End with **"or similar [category] words/descriptors"** so the model generalizes correctly.
- Aim for 5–10 representative words. Too few = low recall. Too many = noise.
- Words should span formal, informal, and colloquial registers where possible.

### 4. Exclusion blocks
Use `EXCLUDE:` as a labeled prefix for explicit false-positive sources:
```
EXCLUDE: Background noise/technical issues (not rep demeanor).
EXCLUDE: Language Barrier/accent issues (communication issue, not knowledge).
```
- One EXCLUDE per false-positive source, not combined into a single run-on.
- If the exclusion redirects to another theme, name it: `EXCLUDE: Customer-initiated hang-ups (use Rep Hung Up theme).`

### 5. Generic word exclusions
When a theme is vulnerable to generic positive or negative words, add an explicit block:
```
GENERIC PRAISE ALONE (e.g., "great," "excellent," "amazing") does NOT qualify unless accompanied by [specific required signal].
GENERIC NEGATIVE WORDS ALONE (e.g., "terrible," "awful," "horrible") do NOT qualify unless accompanied by [demeanor/action/knowledge indicator].
```
This pattern proved critical — generic signals were the #1 source of false positives across the 24-theme test.

### 6. Default routing rules
When two themes share similar surface language, add an explicit default routing rule:
```
"[Ambiguous phrase]" defaults to [Theme A]; use [Theme B] ONLY when [discriminating signal].
```
Examples from the revision:
- `"Answered my questions"` defaults to Rep Was Helpful; use Rep Was Knowledgeable ONLY when expertise is emphasized.
- `"Explained things"` defaults to Rep Communication; use Rep Was Knowledgeable ONLY when explanation shows expertise.

This prevents classifier drift when the LLM is uncertain.

### 7. Conditional classification rules
For themes with outcome-dependent logic, use IF/THEN blocks in this format:
```
IF [condition] → classify as [Theme]. 
IF NOT [condition] → DO NOT auto-classify as [Theme].
```
Example:
```
IF PROBLEM WAS RESOLVED → classify as Rep Was Helpful.
IF PROBLEM NOT RESOLVED → DO NOT auto-classify as Rep Not Helpful.
```
The positive and negative versions of a rule should always be stated together.

### 8. Semantic precision pairs
When two themes hinge on a single-word distinction, state the rule explicitly as an equation:
```
"Didn't answer my questions" = Rep Not Helpful (effort gap).
"Couldn't answer my questions" = Rep Not Knowledgeable (ability gap).
```
```
"Overcharged" = Bill Dispute (error claim).
"Overpriced" = Bill Too High (affordability).
```
These pairs dramatically reduce overlap between adjacent themes.

### 9. Scope anchors
When a theme applies only to a specific entity or timeframe, state it explicitly:
```
Perceived Trust (lied, misled) ONLY qualifies if explicitly attributed to the CURRENT rep, 
not previous reps or the company generally.
```
Scope anchors prevent attribution bleed from historical or company-level mentions to the current interaction.

### 10. Spanish equivalents
End every prompt with a Spanish equivalents clause:
```
Spanish equivalents (including but not limited to: [word1], [word2], or similar Spanish [category] words) also qualify.
```
- Provide 3–5 representative Spanish terms.
- Mirror the same word categories used in the English list (demeanor, action, affordability, etc.).
- Keep the same `including but not limited to` structure.

---

## Principles for Improving Existing Prompts

Use this checklist when revising a prompt that has known accuracy problems.

### Diagnosis questions
Before writing, answer these:
1. What is the most common **false positive** source? (What is matching that shouldn't?)
2. What is the most common **false negative** source? (What is being missed?)
3. Which **adjacent themes** does this overlap with?
4. Does this theme require a **specific word/phrase**, or is general intent enough?
5. Does the theme apply to the **current rep/interaction only**, or also historical events?
6. Are there **generic positive or negative words** that currently over-trigger this theme?
7. Are there **semantic pairs** (couldn't vs didn't, overcharged vs overpriced) that need disambiguation?

### Improvement actions mapped to failure types

| Problem Observed | Fix to Apply |
|---|---|
| Generic praise/complaints triggering incorrectly | Add `GENERIC X ALONE does NOT qualify` block |
| Adjacent theme bleed (e.g., helpful vs knowledgeable) | Add DEFAULT ROUTING rule |
| Scope creep (general company vs current rep) | Add SCOPE ANCHOR for CURRENT rep / CURRENT interaction |
| Low recall on natural language variation | Expand qualifying word list; add Spanish equivalents |
| Outcome-dependent misclassification | Add IF/THEN conditional rule |
| Semantic near-duplicate words routing to wrong theme | Add explicit semantic precision pairs |
| Theme used as catch-all fallback | Add explicit `NOT a default/catch-all` statement |
| Narrow keyword list missing common phrasings | Add `including but not limited to` + broader vocabulary |
| Edge case with valid exception | Add `Exception:` block at end of EXCLUDE section |

---

## Prompt Length Guidelines

| Theme complexity | Expected prompt length | Notes |
|---|---|---|
| Simple binary (opt-out, identity mismatch) | 2–4 sentences | Stop, Wrong Customer, No Feedback |
| Behavioral (demeanor, helpfulness, knowledge) | 4–7 sentences | Rep themes — need exclusions + routing rules |
| Billing / financial | 4–6 sentences | Need comparison vs absolute language distinction |
| Operational process | 3–6 sentences | Need timing anchors (before/after connection) |
| Survey artifact | 2–4 sentences | Keep narrow; these are meta-themes not CX themes |

Prompts that are too short risk low recall and generic triggering.  
Prompts that are too long risk confusing the model with conflicting signals.

---

## What NOT to Do

- **Do not** use vague scope language like "applies when customer mentions X" — be specific about what signal is required.
- **Do not** rely on the theme name alone to distinguish it from adjacent themes — state the distinction explicitly.
- **Do not** use `No Feedback` (or any catch-all theme) as a fallback — unclassifiable substantive content should remain untagged to signal taxonomy gaps.
- **Do not** omit the `including but not limited to` construction — hard-coded lists produce brittle prompts.
- **Do not** combine multiple EXCLUDE conditions into one run-on sentence — one per line improves LLM parsing.
- **Do not** assume the LLM will infer semantic pairs — if `couldn't` and `didn't` route to different themes, say so explicitly.

---

## Phase 2 Theme Checklist

These themes were deferred and still need full revision using this guide:

| Theme | Known Gap | Priority Focus |
|---|---|---|
| Seeking Credits | No sub-theme verbatims reviewed; no exclusions defined | Distinguish from Bill Dispute (requesting vs disputing) |
| Need to Lower Bill | No exclusions; `forward-looking` intent not anchored | Distinguish from Bill Too High (future-looking vs current judgment) |
| Missed Field Tech Appointment | Basic definition only; no word list or exclusions | Add no-show/reschedule language; exclude callback no-shows |

---

## Quick Reference — Structural Checklist

Before finalizing any prompt, verify:

- [ ] Opens with `[Theme Name] -> Customer...`
- [ ] Core trigger condition states the minimum required signal
- [ ] Qualifying word list uses `including but not limited to` formula
- [ ] Generic praise/complaint exclusion added if theme is vulnerable to vague signals
- [ ] EXCLUDE blocks cover known false-positive sources
- [ ] Default routing rules added for any shared surface language with adjacent themes
- [ ] Conditional IF/THEN rules added for outcome-dependent logic
- [ ] Semantic precision pairs stated for near-duplicate signal words
- [ ] Scope anchor added if attribution must be limited to current rep/interaction
- [ ] Spanish equivalents clause included
- [ ] No unqualified catch-all language

---

*Last updated: 2026-06-19*
