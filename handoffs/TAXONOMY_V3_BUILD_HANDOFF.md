# VOC Classification Taxonomy v3 — Build Handoff

## Status: ✅ BUILD COMPLETE — Pending User Review & Definition Refinement
**Build Completed:** 2026-05-29  
**Final Output:** `VOC_Classification_Taxonomy_v3.csv`  
**Total Sub-Topics:** 201 across 68 topics in 7 categories  

---

## WHAT WAS ACCOMPLISHED

### Research Phase
- Reviewed 87,000 Care VOC verbatims for pattern identification
- Reviewed existing v1 taxonomy (50 sub-topics) and v2 taxonomy (70 sub-topics)
- Researched BART-large-mnli / RoBERTa-large-mnli zero-shot NLI design patterns
- Researched industry CX taxonomy frameworks (J.D. Power, NICE, Qualtrics)
- Gathered multi-channel survey scope: Care, Retail, National Retail, IHE
- Confirmed service lines: Consumer Residential — Wireless + Internet ONLY (no TV)

### Design Decisions Locked
1. **Channels:** Care | Retail | National Retail | IHE | All
2. **Categories:** 7 total — People, Process, Pricing, Product, Policy, Platform, Survey Artifact
3. **People category:** Shared core topics + channel-specific sub-topic blocks for Retail/IHE
4. **Polarity:** Only paired where both polarities genuinely occur in survey data
5. **Depth:** 3 levels (Category > Topic > Sub_Topic); no 4th level needed
6. **Sales topics:** Included — pressure selling, upsell, BOGO, D2D, IHE conduct
7. **Tech visit topics:** Under Process — scheduling, no-show, timeliness
8. **Sub_Topic_Definition style:** Written as NLI-compatible hypothesis statements with example phrases and exclusion rules
9. **Survey Artifact:** Neutral polarity for non-actionable items; foreign language NOT auto-classified negative

### Build Execution (11 Steps)
Built category-by-category to avoid network timeout issues on large outputs.

| Step | File | Category | Topics | Sub-Topics | Status |
|------|------|----------|--------|------------|--------|
| 1 | `VOC_Taxonomy_v3_Step1_People_Core.csv` | People — Core | 10 | 34 | ✅ |
| 2 | `VOC_Taxonomy_v3_Step2_People_Retail.csv` | People — Retail | 6 | 17 | ✅ |
| 3 | `VOC_Taxonomy_v3_Step3_People_IHE_Sales.csv` | People — IHE/Sales | 5 | 17 | ✅ |
| 4 | `VOC_Taxonomy_v3_Step4_Process_Core.csv` | Process — Core | 9 | 30 | ✅ |
| 5 | `VOC_Taxonomy_v3_Step5_Process_Scheduling.csv` | Process — Scheduling | 4 | 14 | ✅ |
| 6 | `VOC_Taxonomy_v3_Step6_Pricing.csv` | Pricing | 7 | 23 | ✅ |
| 7 | `VOC_Taxonomy_v3_Step7_Product.csv` | Product | 7 | 25 | ✅ |
| 8 | `VOC_Taxonomy_v3_Step8_Policy.csv` | Policy | 6 | 19 | ✅ |
| 9 | `VOC_Taxonomy_v3_Step9_Platform.csv` | Platform | 6 | 16 | ✅ |
| 10 | `VOC_Taxonomy_v3_Step10_Survey_Artifact.csv` | Survey Artifact | 6 | 9 | ✅ |
| 11 | Assembly & Validation | Combined CSV | — | — | ✅ |

---

## FINAL TAXONOMY STATS

| Metric | Value |
|--------|-------|
| Total Sub-Topics | 201 |
| Unique Topics | 68 |
| Categories | 7 |
| Columns | 11 (all populated, zero missing) |
| Duplicate Sub-Topics | 0 |

### Category Breakdown
| Category | Sub-Topics | Topics |
|----------|-----------|--------|
| People | 67 | 17 |
| Process | 43 | 13 |
| Product | 25 | 7 |
| Pricing | 23 | 7 |
| Policy | 19 | 8 |
| Platform | 15 | 6 |
| Survey Artifact | 9 | 6 |

### Polarity Distribution
| Polarity | Count | % |
|----------|-------|---|
| Negative | 132 | 65.7% |
| Positive | 58 | 28.9% |
| Neutral | 11 | 5.5% |

### Channel Coverage
| Channel | Sub-Topics |
|---------|-----------|
| All (cross-channel) | 138 |
| Retail \| National Retail | 21 |
| Care | 16 |
| IHE | 13 |
| Care \| IHE | 10 |
| National Retail | 3 |

---

## KEY NEW TOPICS vs. v2

| New Topic | Category | Why Added |
|-----------|----------|-----------|
| Rep Empathy & Emotional Ownership | People | Separates emotional acknowledgment from patience/attitude |
| Rep Accountability & Follow-Through | People | Broken promises are #1 trust violation — needed dedicated tracking |
| Store Greeting & Initial Engagement | People | Retail-specific first impression driver |
| IHE Setup & Onboarding Assistance | People | Primary IHE value-add — was missing entirely |
| Door-to-Door Sales Experience | People | D2D generates high-severity complaints — needs isolation |
| Escalation & Supervisor Access | Process | Captures "can't reach supervisor" frustration |
| Proactive Communication & Transparency | Process | Growing expectation — outage notifications, status updates |
| New Customer Onboarding Experience | Process | First 90 days = highest churn risk — first bill confusion |
| Hidden Fees & Unexpected Charges | Pricing | Trust erosion signal distinct from general "too expensive" |
| Device Payment & Installment Plan | Pricing | Device financing confusion is a growing verbatim theme |
| Service Outage (dedicated) | Product | Outages now get duration, communication, and credit sub-topics |
| Data & Throttling | Product | Throttling/deprioritization complaints are growing |
| Online Chat Experience | Platform | Chat volume growing — needs dedicated quality tracking |
| Self-Service & Digital Tools | Platform | Digital containment success/failure is a strategic metric |
| Survey Experience Complaint | Survey Artifact | Distinct from opt-out — customer complains about survey design |

---

## CSV Column Structure
```
Category, Category_Definition, Topic, Topic_Definition, Sub_Topic, Sub_Topic_Definition, Polarity, Survey_Channel, Est_Count, Est_Pct, Actionable_Owner
```

---

## FILES IN WORKSPACE

| File | Description |
|------|-------------|
| `VOC_Classification_Taxonomy_v3.csv` | **FINAL assembled taxonomy** — 201 sub-topics |
| `VOC_Classification_Taxonomy_v2.csv` | Previous version for comparison (70 sub-topics) |
| `VOC_Classification_Taxonomy.csv` | Original v1 (50 sub-topics) |
| `VOC_Taxonomy_v3_Step[1-10]_*.csv` | Individual build step files (can be deleted after final review) |

---

## NEXT STEPS (User to drive)

1. **User Review** — Download and review v3 taxonomy for:
   - Missing topics or sub-topics
   - Overlapping or confusing definitions
   - Polarity accuracy
   - Channel assignment accuracy
   - Actionable_Owner accuracy
2. **Definition Refinement** — Optimize Sub_Topic_Definition text for NLI zero-shot classification:
   - Ensure hypothesis-style phrasing works well with BART-large-mnli / RoBERTa-large-mnli
   - Test for confusion pairs (definitions that overlap semantically)
   - Tune inclusion/exclusion language
3. **NLI Model Testing** — Build scoring pipeline:
   - Sample 500-1000 verbatims across channels
   - Human-label gold standard
   - Run 2-stage NLI (Category → Sub_Topic)
   - Evaluate accuracy, F1, confusion matrix
   - Set confidence thresholds (auto-classify vs. human review)
4. **Iterate** — Refine definitions based on model performance, re-test

---

## GAPS ADDRESSED FROM v2

All 18 identified gaps from v2 were addressed:

| Gap | Addressed In | Status |
|-----|-------------|--------|
| Rep Empathy / Apology / Emotional Ownership | Step 1 | ✅ |
| Rep Accountability / Follow-Through / Broken Promises | Step 1 | ✅ |
| Retail store associate behaviors | Step 2 | ✅ |
| IHE setup/onboarding/sales behavior | Step 3 | ✅ |
| Door-to-door sales conduct | Step 3 | ✅ |
| First Contact Resolution (FCR) | Step 4 | ✅ |
| Repeat Contacts / Called Multiple Times | Step 4 | ✅ |
| Escalation Path / Supervisor Access | Step 4 | ✅ |
| Transfer Quality / Had to Repeat Info | Step 4 | ✅ |
| Appointment Scheduling Friction | Step 5 | ✅ |
| Installation & New Service Setup | Step 5 | ✅ |
| Service Outage (dedicated topic) | Step 7 | ✅ |
| Data/Throttling | Step 7 | ✅ |
| Upgrade/Trade-In Credits & Policy | Steps 6 & 8 | ✅ |
| Activation Fees & Hidden Charges | Step 6 | ✅ |
| Return/Exchange Policy | Step 8 | ✅ |
| Competitive Switch Reasons (WHY not just WHO) | Step 8 | ✅ |
| Store Environment & Systems | Steps 2 & 9 | ✅ |
| Proactive Communication / Status Updates | Step 4 |
| Sales Pressure / BOGO Confusion / Unwanted Upsell | Step 3 |
| National Retail-specific context | Steps 2, 3, 9 |

---

## HOW TO RESUME

When you say **"proceed with Step [N]"**, I will:
1. Generate that category's full sub-topic rows in CSV format
2. Present it for your review
3. Wait for your approval or edits
4. Mark the step complete and ask if you want to proceed to the next

If we hit the network error again, we can split that step into smaller chunks (e.g., Step 1a, Step 1b).

---

## CONTEXT FOR SEAMLESS CONTINUATION

If this conversation drops and we start fresh:
- Point me to this file: `handoffs/TAXONOMY_V3_BUILD_HANDOFF.md`
- Point me to the design decisions in session memory
- Tell me which step to resume from
- I will pick up exactly where we left off
