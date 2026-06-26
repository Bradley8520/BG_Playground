# VOC Taxonomy v4 — Analytical Label Framework Handoff

## Status: 📋 DESIGN COMPLETE — Pending Application to Sub-Topics
**Created:** 2026-06-21
**Active File:** `VOC_Classification_Taxonomy_v4.csv`
**Labels Currently Applied:** `HIGH SEVERITY` (Technician No-Show only — proof of concept)
**Labels Designed, Not Yet Applied:** All others below

---

## CONTEXT

Analytical labels are short tags embedded at the end of `Sub_Topic_Definition` text in the taxonomy CSV. They travel with the sub-topic everywhere — into LLM classifier prompts, downstream analyst views, and scoring pipelines.

**How they work technically:**
- The `Sub_Topic_Definition` field is passed directly to the LLM as the classification hypothesis
- Tags embedded in that text are read by the LLM as metadata about the sub-topic
- For classification firing: tags have minimal impact — the LLM fires based on semantic match to the verbatim, not the tags
- For scoring (CES, severity): tags serve as explicit anchors the LLM can reference when calculating scores
- For human analysts: tags in the definition text appear in any data dictionary or export, giving instant context about the nature of each sub-topic without needing a separate lookup

**Format convention (match existing HIGH SEVERITY pattern):**
Tags are appended at the end of the definition, separated by a period. Use ALL CAPS. Multiple tags separated by ` | `.

*Example:*
> `...Does NOT apply to X. PROCESS FAILURE | HIGH FRICTION | CHURN RISK.`

---

## FULL LABEL FRAMEWORK

### Label 1: `HIGH SEVERITY`
| Field | Detail |
|---|---|
| **What it does** | Flags sub-topics with outsized churn or escalation risk |
| **Primary consumer** | Ops leadership |
| **Feeds into** | Escalation queue, churn alerts, priority dashboards |
| **LLM use** | Informs severity scoring; signals to reasoning models this sub-topic warrants elevated output priority |
| **Analysis use** | Filter classified output to HIGH SEVERITY sub-topics → route to case management. Volume trending is a leading churn indicator |
| **Status** | ✅ Already applied to Technician No-Show / Did Not Show Up |

---

### Label 2: `HIGH FRICTION` | `LOW EFFORT` | `MULTI-TOUCH`
| Field | Detail |
|---|---|
| **What it does** | Anchors Customer Effort Score (CES) calculation |
| **Primary consumer** | CX analytics |
| **Feeds into** | CES scoring pipeline, effort reduction roadmap |
| **LLM use** | When LLM is asked to calculate CES alongside classification, fired sub-topics with HIGH FRICTION tags pull the score toward 6–7 (high effort); LOW EFFORT tags pull toward 1–2 |
| **Analysis use** | CES by sub-topic, channel, product line. Identify which processes drive the most customer effort. Friction reduction roadmap prioritization |
| **Key distinction** | HIGH FRICTION = general excessive effort; MULTI-TOUCH = specifically required multiple contacts or reps |
| **Status** | ⬜ Not yet applied |

---

### Label 3: `RESOLUTION FAILURE`
| Field | Detail |
|---|---|
| **What it does** | Marks sub-topics where the issue was not resolved during the interaction |
| **Primary consumer** | Ops / FCR team |
| **Feeds into** | First Call Resolution (FCR) metric, repeat contact analysis |
| **LLM use** | Signals unresolved outcome; can be used to distinguish resolved vs. unresolved in structured LLM output |
| **Analysis use** | Track RESOLUTION FAILURE rate by rep, team, channel, and issue type. Verbatims with RESOLUTION FAILURE that reappear from the same customer are strong churn signals |
| **Status** | ⬜ Not yet applied |

---

### Label 4: `CHURN RISK`
| Field | Detail |
|---|---|
| **What it does** | Tags sub-topics empirically correlated with voluntary disconnect or competitive loss |
| **Primary consumer** | Retention / Sales |
| **Feeds into** | Churn propensity model, save offers, retention targeting |
| **LLM use** | Strong signal for models calculating churn probability scores alongside classification |
| **Analysis use** | Overlay CHURN RISK sub-topic volume against actual churn cohorts to validate. Build churn propensity score using CHURN RISK sub-topic count per customer. Alert retention teams when CHURN RISK sub-topics spike |
| **Note** | Should be validated against actual churn data before relying on for propensity modeling — start with candidates below and refine based on correlation |
| **Status** | ⬜ Not yet applied |

---

### Label 5: `ACTIONABLE` | `NON-ACTIONABLE`
| Field | Detail |
|---|---|
| **What it does** | Distinguishes sub-topics where AT&T can take corrective action vs. informational/external issues |
| **Primary consumer** | All — ops, exec, frontline |
| **Feeds into** | Dashboard filtering, exec reporting, process improvement workstreams |
| **LLM use** | Can be used to filter LLM output — "return only ACTIONABLE sub-topics for this verbatim" |
| **Analysis use** | ACTIONABLE → ops dashboards, coaching queues; NON-ACTIONABLE → market intelligence, product strategy. Calculate "actionable issue rate" by channel/team as a standalone KPI |
| **Examples — NON-ACTIONABLE** | Survey Artifact sub-topics, Wrong Customer, competitive price comparisons, general market grievances |
| **Status** | ⬜ Not yet applied |

---

### Label 6: `COACHING TARGET`
| Field | Detail |
|---|---|
| **What it does** | Tags sub-topics mapping to a specific, coachable rep behavior |
| **Primary consumer** | Supervisors / QA / Workforce Management |
| **Feeds into** | Rep scorecards, coaching queues, QA sampling prioritization |
| **LLM use** | When rep handle ID is associated with COACHING TARGET sub-topics above threshold → auto-trigger coaching flag |
| **Analysis use** | Track COACHING TARGET sub-topic rate by rep, team, supervisor. Becomes a performance metric. Pair with PROCESS FAILURE to distinguish individual behavior failures from systemic failures — critical for fair rep evaluation |
| **Important distinction** | COACHING TARGET = individual rep behavior. PROCESS FAILURE = systemic/structural. Never use COACHING TARGET sub-topic volume to penalize reps for PROCESS FAILURE issues |
| **Status** | ⬜ Not yet applied |

---

### Label 7: `PROCESS FAILURE`
| Field | Detail |
|---|---|
| **What it does** | Tags sub-topics representing systemic or structural failures — not attributable to individual rep behavior |
| **Primary consumer** | Ops engineering / Process improvement |
| **Feeds into** | Process improvement backlog, staffing models, systems/technology roadmap |
| **LLM use** | Separates what needs ops/engineering attention from what needs coaching |
| **Analysis use** | PROCESS FAILURE volume by sub-topic → improvement roadmap. High PROCESS FAILURE volume in a call center is a staffing/systems signal, not a people signal. Exclude PROCESS FAILURE sub-topics from individual rep performance metrics |
| **Status** | ⬜ Not yet applied |

---

### Label 8: `REVENUE IMPACT`
| Field | Detail |
|---|---|
| **What it does** | Tags sub-topics directly tied to billing, pricing, or revenue retention risk |
| **Primary consumer** | Finance / Retention |
| **Feeds into** | Revenue-at-risk model, P&L reporting, retention offer prioritization |
| **LLM use** | Strong signal for revenue-at-risk scoring models run alongside classification |
| **Analysis use** | Correlate REVENUE IMPACT sub-topic volume with actual revenue churn in same period. Build revenue-at-risk estimate: REVENUE IMPACT verbatim count × average MRC = estimated revenue exposure. Pairs with CHURN RISK for highest-priority retention targeting |
| **Status** | ⬜ Not yet applied |

---

### Label 9: `COMPETITIVE SIGNAL`
| Field | Detail |
|---|---|
| **What it does** | Tags sub-topics where a competitor is mentioned or implied |
| **Primary consumer** | Strategy / Marketing |
| **Feeds into** | Market intelligence reports, competitive response planning |
| **LLM use** | Can prompt extraction of competitor names from COMPETITIVE SIGNAL verbatims as a secondary output |
| **Analysis use** | Track COMPETITIVE SIGNAL volume over time — spikes indicate competitive pressure events (competitor promotion, price drop, network event). Feed into market intelligence reports alongside sales data |
| **Status** | ⬜ Not yet applied |

---

### Label 10: `COMPLIANCE RISK`
| Field | Detail |
|---|---|
| **What it does** | Tags sub-topics containing potential regulatory exposure — unauthorized charges, deceptive practices, consumer protection issues |
| **Primary consumer** | Legal / Compliance |
| **Feeds into** | Regulatory review queue, compliance audit trail |
| **LLM use** | Compliance-flagged verbatims can be routed to a separate review pipeline automatically |
| **Analysis use** | COMPLIANCE RISK sub-topics trigger a separate review queue — not just ops reporting. Volume trending can signal a systemic issue before it reaches regulatory complaint stage (FCC, BBB, CFPB). Pairs with REVENUE IMPACT for unauthorized charge sub-topics |
| **Status** | ⬜ Not yet applied |

---

## CANDIDATE SUB-TOPIC LABEL ASSIGNMENTS

> These are recommended starting assignments. Validate CHURN RISK labels against actual churn cohort data before using in propensity models.

### People Category

| Sub-Topic | Recommended Labels |
|---|---|
| Rep Was Rude / Dismissive / Unprofessional | `COACHING TARGET` `CHURN RISK` `ACTIONABLE` |
| Rep Was Unhelpful / Did Not Resolve My Issue | `COACHING TARGET` `RESOLUTION FAILURE` `CHURN RISK` `ACTIONABLE` |
| Rep Was Knowledgeable / Gave Correct Info | `LOW EFFORT` `ACTIONABLE` |
| Rep Was Unknowledgeable / Gave Wrong Info | `COACHING TARGET` `ACTIONABLE` |
| Rep Made an Account or Setup Error | `COACHING TARGET` `COMPLIANCE RISK` `HIGH SEVERITY` `ACTIONABLE` |
| Rep Hung Up / Ended Call Prematurely | `COACHING TARGET` `CHURN RISK` `HIGH SEVERITY` `ACTIONABLE` |
| Rep Did Not Follow Through / Broken Promise | `COACHING TARGET` `RESOLUTION FAILURE` `CHURN RISK` `ACTIONABLE` |
| Rep Was Courteous / Friendly / Professional | `LOW EFFORT` `ACTIONABLE` |
| Rep Was Helpful / Resolved My Issue | `LOW EFFORT` `ACTIONABLE` |
| Rep Was Thorough / Detailed | `LOW EFFORT` `ACTIONABLE` |

### Process Category

| Sub-Topic | Recommended Labels |
|---|---|
| Long Wait for Rep | `PROCESS FAILURE` `HIGH FRICTION` `ACTIONABLE` |
| Long/Multiple Holds | `PROCESS FAILURE` `HIGH FRICTION` `ACTIONABLE` |
| Overall Interaction Took Too Long | `HIGH FRICTION` `ACTIONABLE` |
| Service Was Fast/Quick/Efficient | `LOW EFFORT` `ACTIONABLE` |
| Too Many Transfers / Bounced Around | `PROCESS FAILURE` `HIGH FRICTION` `MULTI-TOUCH` `CHURN RISK` `ACTIONABLE` |
| Had to Repeat Information After Transfer | `PROCESS FAILURE` `HIGH FRICTION` `ACTIONABLE` |
| Transferred to Right Person / Smooth Handoff | `LOW EFFORT` `ACTIONABLE` |
| Transfers / Multiple Reps | `MULTI-TOUCH` `ACTIONABLE` |
| Promised Callback Never Received | `PROCESS FAILURE` `HIGH FRICTION` `RESOLUTION FAILURE` `ACTIONABLE` |
| Call Was Dropped / Disconnected | `PROCESS FAILURE` `HIGH FRICTION` `ACTIONABLE` |
| Technician No-Show / Did Not Show Up | `PROCESS FAILURE` `HIGH FRICTION` `HIGH SEVERITY` *(already tagged)* `ACTIONABLE` |

### Pricing Category

| Sub-Topic | Recommended Labels |
|---|---|
| Bill Increased / Price Went Up Unexpectedly | `REVENUE IMPACT` `CHURN RISK` `ACTIONABLE` |
| Bill Is Too High / Too Expensive | `REVENUE IMPACT` `CHURN RISK` `ACTIONABLE` |
| Billing Error / Incorrect Charge / Overcharge | `REVENUE IMPACT` `COMPLIANCE RISK` `HIGH FRICTION` `ACTIONABLE` |
| Request to Lower Bill / Reduce Cost | `REVENUE IMPACT` `CHURN RISK` `ACTIONABLE` |
| Refund / Credit Request | `REVENUE IMPACT` `ACTIONABLE` |
| Promotion Expired / Rate Change | `REVENUE IMPACT` `CHURN RISK` `ACTIONABLE` |

### Survey Artifact Category

| Sub-Topic | Recommended Labels |
|---|---|
| All Survey Artifact sub-topics | `NON-ACTIONABLE` |

---

## IMPLEMENTATION PLAN

### Step 1 — Add a `Labels` column to the taxonomy CSV
Rather than embedding all labels only in `Sub_Topic_Definition` text, consider adding a dedicated `Labels` column. This enables:
- SQL/PowerShell filtering by label without text parsing
- Structured LLM prompt injection ("sub-topics with label CHURN RISK fired: ...")
- Clean reporting joins (label as a dimension in Power BI / Tableau)

**Proposed column:** `Labels` — pipe-delimited string, e.g. `HIGH FRICTION | CHURN RISK | ACTIONABLE`

### Step 2 — Embed shortened label reference in Sub_Topic_Definition (optional)
Keep the trailing tag in the definition text as a human-readable annotation AND populate the separate Labels column for machine use. Both serve different consumers.

### Step 3 — Apply labels by category in batches
Recommended order: People → Process → Pricing → Product → Policy → Platform → Survey Artifact

### Step 4 — Validate CHURN RISK labels
Pull 90-day churn cohort from production data. Cross-reference with Care verbatim classifications. Confirm which sub-topics have statistically significant churn correlation before using in propensity models.

### Step 5 — Update classifier prompt to use Labels column
When building the LLM classification prompt, inject label context:
```
For the sub-topics that fire, note any labels present (HIGH FRICTION, CHURN RISK, etc.)
and use them to inform your Customer Effort Score and Severity Score outputs.
```

---

## NEXT SESSION — PICK UP HERE

1. **Decide on Labels column:** Add dedicated `Labels` column to `VOC_Classification_Taxonomy_v4.csv` alongside embedding in definition text, OR embed in definition text only. Column approach is recommended for analytical flexibility.

2. **Apply labels — People category first** (highest coaching and churn value). Use the candidate assignments table above as starting point.

3. **Apply labels — Process category** (highest friction/effort value for CES).

4. **Apply labels — Pricing category** (highest revenue impact value).

5. **Apply Survey Artifact NON-ACTIONABLE** — straightforward batch update.

6. **Complete remaining 3 revised prompts** (Seeking Credits, Need to Lower Bill, Wireless Coverage) before or after label application — labels can be added at the same time as definition updates.

---

## FILES REFERENCE

| File | Purpose |
|---|---|
| `VOC_Classification_Taxonomy_v4.csv` | Active taxonomy — all changes applied here |
| `VOC Verbatim Taxonomy (original 24).csv` | Source of revised prompt definitions — read-only reference |
| `Care_Verbatims_Apr2026_classification_testing.csv` | 97,002 real verbatims for testing/validation |
| `handoffs/VOC_TAXONOMY_V4_REVISED_PROMPTS_HANDOFF.md` | Tracks revised prompt application progress (20 of 24 done) |
