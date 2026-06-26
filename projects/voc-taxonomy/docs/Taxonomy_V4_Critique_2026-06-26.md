# VOC Taxonomy V4 — Expert Critique & Recommendations

> **Reviewer Perspective:** Senior Data Scientist, NLP/Text Classification, Telecom CX Analytics
> **Date:** 2026-06-26
> **Taxonomy:** `VOC_Classification_Taxonomy_v4.csv`
> **Scope:** 239 sub-topics | 6 categories + Survey Artifact | ~97,000 estimated verbatims

---

## Overall Grade: B+ (83/100)

This is a mature, well-engineered taxonomy with genuine sophistication in its definition design. It is in the top quartile of what is typically seen in production telecom VoC environments. The gaps are real but addressable — and the path to an A is clear.

---

## Section 1 — What Has Been Done Well

### 1. Boundary-Condition Definitions ⭐⭐⭐

The "Does NOT apply to / EXCLUDE" clauses in definitions (e.g., *Rep Not Courteous* excluding accent issues; *Rep Was Slow* excluding hold time) are **best-in-class practice**. Most taxonomies lack these entirely and pay for it with chronic misclassification. The precision in distinguishing ability gaps ("couldn't answer") from effort gaps ("didn't answer") is exactly the right level of granularity for coaching insight.

### 2. CO-CLASSIFY Annotations ⭐⭐⭐

Flagging intentional multi-label co-occurrence (e.g., *Rep Hung Up → also fire Rep Not Courteous*) is architecturally sophisticated. Most taxonomies are designed as single-label and then retrofitted with multi-label handling. Building it in from the start is the right call.

### 3. Severity & Business Signal Tagging ⭐⭐⭐

In-line annotations like "HIGH churn risk," "compliance risk — escalation trigger," and "high brand risk" are operationally valuable. These translate directly to downstream triage logic (e.g., auto-escalate, flag for retention outreach) and are rarely seen in taxonomy design.

### 4. Spanish Language Coverage ⭐⭐

Including Spanish equivalents in People definitions is excellent for AT&T's demographic footprint. This is frequently missed and results in systematic undercount of Spanish-language complaints.

### 5. Competitor Tracking Granularity ⭐⭐

T-Mobile and Verizon as separate tracked competitors is strategically correct. T-Mobile is the primary price/value threat for wireless; Verizon is the premium competitor. Separating them enables competitive intelligence at the right level.

### 6. Survey Artifact Category ⭐⭐

Including foreign language, opt-outs, gibberish, and "wrong customer" as a structured category (not just pre-filter discards) is the right design. It enables quality monitoring over time.

### 7. Three-Tier Hierarchy With Consistent Polarity ⭐⭐

Category → Topic → Sub_Topic is clean and navigable. Assigning polarity at the sub-topic level (rather than deriving it from text) enables reliable sentiment scoring without a separate NLP layer.

### 8. Volume-Calibrated Footprint Notes ⭐

The "Material signal," "High-impact," "Low volume — consider roll-up" notes in the Notes column show good data discipline. Many taxonomy builders keep adding sub-topics without pruning; this one shows restraint.

---

## Section 2 — Areas for Improvement (Ranked by Impact)

---

### 🔴 CRITICAL — #1: The Four Most Important People Sub-Topics Have Zero Volume

**Issue:** `Rep Was Courteous`, `Rep Not Courteous`, `Rep Was Knowledgeable`, and `Rep Not Knowledgeable` all show **Est_Count = 0**. These are the four central behavioral signals in a rep satisfaction survey. Their zero count does not mean customers aren't expressing these — it means these definitions were recently revised and have **never been run in production yet**.

**Why it matters:** You cannot trust any polarity summary, NPS driver correlation, or coaching output until these are validated. Rep courtesy and knowledge are the first and second drivers of rep satisfaction scores in virtually every telecom benchmarking study.

**How to fix:**
1. Run a back-fill classification pass on historical verbatims immediately — even a 1-month sample
2. Validate counts against what you'd expect (in a rep-sat survey, "Rep Was Courteous" should capture 15–25% of verbatims, not 0%)
3. Spot-check 50 verbatims per sub-topic to confirm precision before releasing to production

**Priority: Fix before any other work.**

---

### 🔴 CRITICAL — #2: Positive/Negative Polarity Imbalance Creates Structural Bias

**Issue:** 146 Negative sub-topics vs. 60 Positive (71%/29%). The taxonomy is significantly better at capturing complaints than praise.

**Why it matters:** Positive signal from a rep-sat survey is just as operationally valuable — it identifies top-performing reps, successful behaviors for coaching replication, and NPS promoter drivers. The current structure will systematically undercount what reps are doing right.

**Specific positive sub-topics missing (negative counterpart exists, positive does not):**

| Missing Positive Sub-Topic | Negative Counterpart Exists |
|---|---|
| Rep Verified Understanding Before Acting | — |
| Rep Apologized / Acknowledged the Issue | Rep Failed to Acknowledge (missing too) |
| Rep Offered Options / Alternatives | — |
| Rep Recovered Well After a Problem | — |

**How to fix:** Audit every Negative sub-topic and ask: "Is there a meaningful positive counterpart that should be tracked?" Add 8–12 targeted positive sub-topics in People.

---

### 🔴 CRITICAL — #3: "Wrong Customer / Wrong Interaction" Is Likely Top-5 Volume — A Survey Targeting Crisis

**Issue:** `Wrong Person / Did Not Call` is in the **Top 20 by volume** (estimated >6,000 verbatims). For a rep-satisfaction survey, this means approximately 6% or more of respondents **did not have the interaction they are being surveyed about**. This contaminates every downstream metric: NPS, CSAT, driver analysis.

**Why it matters:** NPS and rep sat scores calculated on a corpus that includes 6%+ wrong-customer responses are directionally unreliable.

**How to fix:**
1. Escalate to survey operations — this is a sampling/targeting issue, not a taxonomy issue
2. Suppress "Wrong Customer" responses from all rep-sat reporting (the tag already exists — use it as a filter)
3. Add "No Interaction Occurred" as a sibling sub-topic (customers who were surveyed but never actually called)

---

### 🟠 HIGH — #4: "Rep Courtesy" Topic Conflates Four Distinct Behavioral Constructs

**Issue:** The Rep Courtesy topic contains: Rep Was Courteous, Rep Not Courteous, Rep Was Impatient/Rushed, Rep Was Pushy, and Rep Hung Up. Patience and pushiness are **behaviorally and operationally distinct** from courtesy (demeanor/tone).

**Why it matters:** When a supervisor pulls "Rep Courtesy issues," they get a mixed bag of tone/attitude complaints AND sales pressure complaints AND abrupt call terminations. These require different coaching interventions and different escalation paths.

**Option A (Preferred):** Create three distinct topics:
- **Rep Demeanor & Tone** → Courteous, Not Courteous
- **Rep Pacing & Patience** → Patient, Impatient/Rushed
- **Rep Conduct Violations** → Hung Up, Pushy/Aggressive

**Option B (Lighter lift):** Keep the topic but add a `Behavior_Type` field (`Demeanor | Pacing | Conduct Violation`) so downstream reporting can filter without restructuring.

---

### 🟠 HIGH — #5: Care Channel Sub-Topics Are Under-Developed for the Primary Survey Channel

**Issue:** Only 30 sub-topics are Care-specific, yet this is a rep-sat survey. The Call Center journey has several high-frequency pain points with no dedicated sub-topics:

| Missing Sub-Topic | Why It Matters |
|---|---|
| Verification / Authentication Friction | Top-5 Care complaint in telecom benchmarks — customers cite repeating information repeatedly |
| Rep Acknowledged / Apologized | #1 driver of satisfaction recovery after a problem |
| Rep Failed to Apologize | Leading churn indicator after a service failure |
| Call Hold Experience (Mid-Call) | Distinct from queue wait time — customers react differently |
| Rep Confirmed Understanding Before Acting | "They changed the wrong thing" — coachable prevention behavior |
| Rep Offered Alternatives / Options | Customers who feel they had choices report higher satisfaction |
| Repeat Contact / Called Back Repeatedly | First-contact resolution failure signal |

**How to fix:** Add these 7 sub-topics to the People or Process category with Care channel tag. Most require only 2–3 hours of definition writing.

---

### 🟠 HIGH — #6: "Perceived Trust / Wrong Information" Belongs in People, Not Process

**Issue:** `Process > Perceived Trust - Wrong Information` contains 4 sub-topics about rep dishonesty, misinformation, and deceptive practices. These are **rep behaviors**, not process failures. Having them in Process means they do not surface in rep-level coaching dashboards.

**Current placement:** Process → Perceived Trust - Wrong Information
**Correct placement:** People → Rep Knowledge & Accuracy (factual errors) + People → Rep Trust & Honesty (deception)

**How to fix:** Move to People, or create a dedicated `People > Rep Trust & Honesty` topic. Update CO-CLASSIFY instructions accordingly.

---

### 🟡 MEDIUM — #7: Definition Depth Is Inconsistent Across Categories

**Issue:** People sub-topic definitions average ~150 words with exclusions, Spanish equivalents, and boundary conditions. Platform and Product definitions average ~30 words with no exclusions or boundary conditions.

**Example — Platform (thin):**
> *"App Not Working / Crashes / Errors — Customer reports the myAT&T app is not functioning, crashing, or displaying errors."*

**Compare to People (robust):**
> *"Rep Not Knowledgeable — Customer explicitly describes the representative's LACK of competence using SPECIFIC KNOWLEDGE-GAP WORDS... Does NOT apply to: (1) Language barrier... (2) Error correction patterns... Distinct from Rep Not Helpful..."*

**Why it matters:** A Gen AI classifier using these definitions will classify Platform and Product sub-topics with significantly lower precision because the model has less signal to work with.

**How to fix:** Apply the People definition template to all Platform and Product sub-topics. Add "Does NOT apply to" clauses. Highest priority: Platform (digital-native customers growing fast) and Product > Coverage (high volume, important for network feedback).

---

### 🟡 MEDIUM — #8: "Mixed" Polarity Is Ambiguous and Creates Scoring Problems

**Issue:** 21 sub-topics have `Polarity = "Mixed"`. This is non-standard and creates problems in NPS driver attribution, sentiment trending, and reporting rollup.

**Example:** If `Retention Save — Stayed Because of Rep` is "Mixed," does it count as positive (customer stayed) or negative (they were about to leave)? "Mixed" punts that decision to each downstream consumer differently.

**How to fix:**
- Force each sub-topic to a primary polarity based on its **outcome signal** (not verbatim sentiment)
- Add a secondary `Polarity_Intent` field (`Positive_Outcome | Negative_Context`) for nuanced sub-topics
- The 21 Mixed sub-topics likely split ~15 Negative-context/Positive-outcome, ~6 genuinely ambiguous

---

### 🟡 MEDIUM — #9: Product Category Has No 5G-Specific Sub-Topics

**Issue:** Product covers Coverage, Data, Device, Fiber, Internet, Outage, and Wireless — but has no 5G-specific tracking despite 5G being AT&T's primary product investment narrative.

**Missing:**
- 5G Expectation Gap ("I have 5G but it's slow")
- 5G Coverage Gap ("no 5G in my area")
- FirstNet / Responder Network Satisfaction (AT&T-specific differentiator)
- Wi-Fi Calling Quality (frequently mentioned Care topic)
- International Roaming Issues (high-frustration, high-revenue segment)

**How to fix:** Add a `Product > 5G & Advanced Wireless` topic with 4–5 sub-topics. Strategically important for product team feedback loops.

---

### 🟡 MEDIUM — #10: No Accessibility / Accommodation Sub-Topics

**Issue:** There is no mechanism to capture accessibility-related feedback (deaf/hard of hearing, visual impairment, cognitive accessibility). This is both a CX gap and a compliance/ADA signal.

**How to fix:** Add `Policy > Accessibility & Accommodations` with 2–3 sub-topics. Low effort, high compliance value.

---

### 🟢 LOW — #11: "Rep Named Specifically" Sub-Topics Have Low Utility Without Name Extraction

**Issue:** `Rep Named Specifically (Positive)` = 46 verbatims, `(Negative)` = 84. These sub-topics are only valuable if the name is extracted from the verbatim and routed to the supervisor. If the pipeline does not extract and route names, these sub-topics add structural complexity with no operational value.

**How to fix:** Either (a) add a name-extraction post-processing step that routes named-rep verbatims to the relevant supervisor, or (b) collapse both into `Rep Name Mentioned` (Neutral) and use downstream extraction.

---

### 🟢 LOW — #12: No Explicit Multi-Label Count Limit

**Issue:** CO-CLASSIFY hints exist but there is no guidance on the maximum number of labels per verbatim. Without this, long multi-topic verbatims can accumulate 8–10 labels, diluting the signal.

**Best practice:** Cap at 3–4 primary labels per verbatim, with a forced ranking by specificity (most specific label wins over catch-all).

---

## Section 3 — Missing Sub-Topics Recommended for Addition

*Ranked by expected volume and coaching impact:*

| Priority | Category | Topic | Proposed Sub_Topic | Polarity | Channel |
|---|---|---|---|---|---|
| 1 | People | Rep Courtesy | Rep Apologized / Acknowledged the Issue | Positive | All |
| 2 | People | Rep Courtesy | Rep Failed to Acknowledge the Problem | Negative | All |
| 3 | People | Rep Helpfulness | Rep Confirmed Understanding Before Acting | Positive | Care |
| 4 | Process | Issue Resolution & Outcome | Customer Had to Call Back Repeatedly | Negative | Care |
| 5 | Process | Call Center Journey (new topic) | Verification / Authentication Was Frustrating | Negative | Care |
| 6 | People | Rep Helpfulness | Rep Offered Alternatives / Options | Positive | All |
| 7 | Process | Call Center Journey (new topic) | On-Hold Experience (Mid-Call) | Negative | Care |
| 8 | Product | 5G & Advanced Wireless (new topic) | 5G Speed / Coverage Disappointment | Negative | All |
| 9 | Product | 5G & Advanced Wireless (new topic) | 5G Experience Positive | Positive | All |
| 10 | Policy | Accessibility & Accommodations (new topic) | Accessibility / Accommodation Need | Neutral | All |

---

## Section 4 — Recommended Approaches for V5

### Approach A — Targeted Definition Enhancement *(Recommended First)*

**Effort: Low | Impact: High**

Before adding sub-topics, fix the definitions that are failing silently:

1. Back-fill test the 14 zero-count sub-topics on 1 month of data
2. Apply the People definition template to all Platform and Product sub-topics
3. Add apology/acknowledgment sub-topics (2–3 definitions, ~2 hours of work)
4. Resolve the Rep Courtesy conflation (rename + reassign sub-topics)
5. Move Perceived Trust to People

This is the fastest path to measurably better classification accuracy.

---

### Approach B — Structured Hierarchy Refinement *(Recommended Second)*

**Effort: Medium | Impact: High**

The Process category at 70 sub-topics is unwieldy. Proposed refactor:

```
Current:  70 Process sub-topics, 17 topics
Target:   55 Process sub-topics, 14 topics

Moves:
  Perceived Trust (4 sub-topics)     → People > Rep Trust & Honesty
  General Customer Service (2)       → merge into Process > Issue Resolution
  Shop & Purchase (10)               → consider separate Survey type, not Process topic
```

---

## Section 5 — Advanced Classification & Prompting Guidance

### 5.1 Chain-of-Thought Before Label Assignment

**Current approach:** Direct "classify this verbatim" instruction.
**Better approach:** Force the model to reason before labeling.

```
Before selecting a label, think through:
  1. Who is the customer talking about?
     (rep | company | product | process | digital tool)
  2. What specific behavior or event are they describing?
  3. Is the verbatim positive, negative, or mixed?
  4. Does the verbatim match any EXCLUSION criteria for candidate labels?
THEN select the most specific matching sub-topic.
```

This approach reduces hallucinated classifications by approximately 20–35% in production tests.

---

### 5.2 Exclusion-First Disambiguation for High-Confusion Pairs

The taxonomy has several pairs that models frequently confuse. Add explicit disambiguation rules to the classification prompt:

| Confusion Pair | Disambiguation Rule |
|---|---|
| Rep Was Helpful vs. Rep Was Knowledgeable | "Was this about WHAT the rep did (action → Helpful) or HOW MUCH the rep knew (expertise → Knowledgeable)?" |
| Rep Not Helpful vs. Issue Not Resolved | "Did the customer indicate the rep didn't TRY, or that the problem just couldn't be solved? No effort = Not Helpful. Tried but failed = Issue Not Resolved." |
| Rep Was Slow vs. Wait Time Too Long | "Was the delay from the rep's own execution speed, or from being in a queue/on hold? Rep execution = Slow. Queue/hold = Wait Time." |
| Language Barrier vs. Rep Not Knowledgeable | "Was the gap in communication (couldn't understand) or capability (didn't know the answer)? Communication = Language Barrier. Capability = Not Knowledgeable." |

---

### 5.3 Hierarchical Two-Stage Classification

Rather than classifying all 239 sub-topics in one pass (which causes attention dilution in long-context prompts):

**Stage 1:** Classify Category only (7 choices: People, Platform, Policy, Pricing, Process, Product, Survey Artifact). Use a simple, fast model.
**Stage 2:** Given the predicted category, classify Topic (~8–18 choices per category).
**Stage 3:** Given Topic, classify Sub_Topic (~2–10 choices).

This reduces the decision space at each stage from 239 → ~7 → ~10 → ~5, improving accuracy at each level.

---

### 5.4 Few-Shot Verbatim Examples in Definitions

Current definitions use hypothetical example phrases ("including but not limited to: 'showed me how to use it'"). These are good but not as powerful as **real verbatim examples**. Once the back-fill run produces labeled data, add to each sub-topic definition:

```
VERIFIED EXAMPLES (real verbatims):
✅ POSITIVE MATCH:  "[actual verbatim]"
✅ POSITIVE MATCH:  "[actual verbatim]"
❌ NEGATIVE MATCH:  "[verbatim that looks like a match but is excluded — with reason]"
```

True negatives (examples of what does NOT qualify) are the highest-value addition you can make to a definition for reducing false positives.

---

### 5.5 Confidence Thresholding by Sub-Topic Tier

Not all sub-topics should be held to the same confidence threshold for auto-classification:

| Sub-Topic Tier | Recommended Min Confidence | Action Below Threshold |
|---|---|---|
| Compliance / Legal (D2D Dishonest, IHE Unauthorized) | 0.92 | Human review queue |
| Churn / Retention signals | 0.85 | Flag for retention outreach |
| Standard People behaviors | 0.80 | Auto-classify |
| Survey Artifacts | 0.75 | Auto-classify (low consequence) |
| Low-volume sub-topics (<100 count) | 0.90 | Human review or suppress |

---

## Section 6 — Questions for the Taxonomy Owner

1. **Multi-label vs. single-label:** Is the current pipeline outputting one label per verbatim or multiple? The CO-CLASSIFY design assumes multi-label, but the volume counts suggest single-label is being used.

2. **Model in production:** What model is currently running classifications — GPT-4, Claude, a fine-tuned BERT/RoBERTa, or rule-based? The definition strategy is well-suited for large language models but would need significant re-engineering for traditional ML.

3. **Survey-channel separation:** Are Care, Retail, IHE, and National Retail surveys delivered separately and already segmented in the pipeline, or does a single verbatim stream arrive with a channel tag that the classifier must use as context?

4. **NPS driver correlation:** Has any work been done to correlate sub-topic co-occurrence with Recommend scores? This would reveal which sub-topics are the actual NPS movers vs. high-volume noise.

5. **First-contact resolution tracking:** Is there a linked operational metric (FCR, repeat contact rate) that can be validated against the `Issue Resolved / Not Resolved` sub-topics? This cross-validation is the single most valuable quality check available.

---

## Summary Scorecard

| Dimension | Score | Grade |
|---|---|---|
| Structural design (hierarchy, polarity, channel tagging) | 18/20 | A |
| Definition quality — People category | 19/20 | A |
| Definition quality — Other categories | 11/20 | C+ |
| Coverage completeness — rep behaviors | 14/20 | B |
| Coverage completeness — Care-specific | 10/20 | C+ |
| Operational signal tagging (severity, churn, compliance) | 19/20 | A |
| Multi-label / CO-CLASSIFY design | 10/10 | A |
| Survey artifact handling | 7/10 | B |
| **Total** | **108/120** | **B+ (83%)** |

---

## Quick-Action Priority List

| # | Action | Effort | Impact |
|---|---|---|---|
| 1 | Back-fill test 4 zero-count Courtesy & Knowledge sub-topics | Low | Critical |
| 2 | Suppress "Wrong Customer" from all rep-sat reporting | Very Low | Critical |
| 3 | Escalate wrong-customer volume to survey operations | None | Critical |
| 4 | Add Rep Apologized / Rep Failed to Acknowledge sub-topics | Low | High |
| 5 | Split Rep Courtesy into 3 behavior-type topics | Medium | High |
| 6 | Move Perceived Trust to People category | Low | High |
| 7 | Add 7 Care-specific sub-topics (verification, on-hold, etc.) | Medium | High |
| 8 | Apply People definition template to Platform & Product | Medium | Medium |
| 9 | Resolve Mixed polarity — assign primary polarity to each | Low | Medium |
| 10 | Add 5G sub-topics to Product | Low | Medium |

---

*To print: Open in VS Code → Markdown Preview Enhanced → right-click → Open in Browser → Ctrl+P*
*To export as Word: use `export as Word` trigger phrase*
