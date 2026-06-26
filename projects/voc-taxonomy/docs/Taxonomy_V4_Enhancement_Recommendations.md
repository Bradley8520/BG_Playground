# Taxonomy V4 Enhancement Recommendations (Care Scope)

## Objective
Refine the taxonomy so it remains diagnostic for root-cause analysis while preserving enough volume per node for stable metrics.

Scope for this review:
- Only rows where `Survey_Channel` includes `Care` or `All`
- No hard deletions/removals from taxonomy
- Probation-first governance before any reporting-layer consolidation

## Current-State Diagnostic (from April 2026 classification run)
- Full taxonomy sub-topics: 240
- Care/All scoped sub-topics: 203
- Total classified verbatims (full run): 97,002
- Care/All scoped sub-topics with count < 15: 24
- Care/All scoped sub-topics with count < 30: 39
- Care/All scoped sub-topics with count < 50: 57

Low-signal concentration is clustered in specific areas rather than spread evenly, which means targeted restructuring is preferable to broad taxonomy reduction.

Lowest-volume Care/All topics by total count currently include:
- Process > General Customer Service
- Survey Artifact > Unintelligible / Gibberish
- People > Rep Professionalism
- Policy > Outsourcing & Staffing Practices
- Survey Artifact > Survey Experience Complaint

## AI Council Feedback Synthesis
I incorporated an additional AI-council review process (independent agent critique) in addition to the cross-functional council lens (CX Operations, QA/Coaching, Product/Digital, Pricing/Retention, Analytics Governance).

### CX Operations Lens
- Preserve operationally actionable topics with owner accountability (wait time, transfers, issue resolution, billing errors).
- Reduce duplicate labels that describe similar intent but split volume.

### QA/Coaching Lens
- Keep behavior-specific rep topics that inform coaching.
- Collapse generic/ambiguous “catch-all” labels that do not map to a clear intervention.

### Product/Digital Lens
- Keep platform and self-service failure themes separate from human-agent behavior.
- Ensure outages/performance/system friction topics remain distinguishable from policy/pricing complaints.

### Pricing/Retention Lens
- Maintain explicit switching intent and competitor intelligence nodes.
- Consolidate billing-intent labels that do not materially change action path.

### Analytics Governance Lens
- Introduce thresholds and lifecycle rules for low-volume labels.
- Use a two-level reporting model: detailed taxonomy for NLP tagging, roll-up taxonomy for scorecards.

## Priority Recommendations

Guiding rule for all recommendations below:
- Keep full label set in classification taxonomy.
- Apply consolidation in reporting layer only.
- Use probation windows before promoting any roll-up to default scorecards.

## 1) Consolidate ultra-low-value generic labels
### Recommendation (reporting layer)
Roll up Process > General Customer Service:
- Negative General Customer Service
- Positive General Customer Service

into one neutral intent label:
- General Customer Service (Unspecified)

Classification-layer instruction:
- Keep both original labels in taxonomy and tagging output.

### Why
- Current counts are near-zero and not analytically stable.
- Sentiment is already represented by the Polarity field.
- These labels add ambiguity and reduce model precision.

## 2) Rationalize Shop & Purchase granularity with a probation-first two-tier approach
### Recommendation
Keep as standalone in scorecard:
- Add a Line
- Fulfillment — Order

Move remaining low-volume Shop & Purchase nodes into an analyst-level detail tier (not executive scorecard) for 60-day monitoring:
- Activation & Porting
- New Account
- Trade-In
- Upgrade
- Returns
- Exchange & Replace
- Fulfillment — Delivery
- Warranty & Device Protection Exchange
- Unauthorized Account Changes

If combined volume for the detail tier remains low for 2 to 3 months, aggregate in reporting to:
- Shop & Purchase — Other Transaction Friction

Classification-layer instruction:
- Keep all 11 Shop & Purchase sub-topics intact regardless of reporting roll-ups.

### Why
- Current topic has 11 sub-topics, but volume is concentrated in only 2.
- Preserves drill-down capability without polluting primary KPI views.

## 3) Merge overlapping billing-intent nodes
### Recommendation (reporting layer)
In Pricing > Bill Inquiry & General Bill, merge:
- Bill Inquiry
- General Bill

to:
- General Billing Inquiry

### Why
- High semantic overlap and similar action path.
- Reduces classifier confusion and duplicate reporting.

## 4) Named-rep recognition: probation before merge (Care-first exception)
### Recommendation
Do not merge immediately for Care scorecards.

Place these two labels on 90-day probation with parallel tracking:
- Rep Named Specifically (Positive Mention)
- Rep Named Specifically (Negative Mention)

At end of probation, decide whether to roll up reporting to:
- Rep Named Specifically

Classification-layer instruction:
- Keep both labels and keep Polarity usage unchanged.

### Why
- Semantically close, but Care QA/coaching may still benefit from distinct positive vs negative accountability tracking.
- Probation-first avoids premature loss of coaching signal.

## 5) Re-home one pricing-rooted behavior signal
### Recommendation
Move:
- People > Door-to-Door Sales Experience > D2D Rep Was Dishonest About Offers / Pricing

to either:
- Pricing > Promotions & Discounts
or
- People > Sales Transparency & Offer Accuracy

Preferred placement: People > Sales Transparency & Offer Accuracy (keeps behavior + sales-representation context together).

Implementation note:
- Keep existing node during probation and dual-map this label to a reporting roll-up under Sales Transparency to avoid trend breaks.

### Why
- Current node is behaviorally framed but economically rooted.
- Alignment with sales transparency architecture improves root-cause ownership.

## 6) Keep but monitor low-volume structural topics
### Recommendation
Do not remove these; place on watchlist with explicit review cadence and strategic exceptions:
- People > Rep Professionalism
- People > Store Environment & Atmosphere
- Policy > Data Privacy & Security
- Policy > Outsourcing & Staffing Practices
- Product > Coverage & Signal

### Why
- Low current volume can still represent strategic risk areas.
- Policy/security themes are low-frequency but high-severity.

## Care-Specific Probation Candidates (AI-council additions)
- AI Automation & IVR Experience sub-topics: monitor 60 days before any roll-up (UX friction and human-preference signals should not be collapsed too early).
- Appointment Scheduling: consider Care vs IHE operational split before consolidation.
- Cross-Channel Friction: keep Care-to-Store technical referral friction visible during probation; evaluate lower-volume variants for roll-up.
- Request for Different Communication Support: treat as strategic accessibility signal (protect from aggregation despite volume profile).

## Reporting Architecture Change (Important)
Adopt two parallel taxonomies:
- Classification Taxonomy (fine-grain): used by NLP tagging pipeline
- Reporting Taxonomy (roll-up): used for KPI dashboards and confidence-sensitive metrics

This preserves analytical depth while avoiding sparse-scorecard noise.

Explicit policy:
- No hard deletions of Care/All sub-topics.
- Any aggregation is reporting-only and reversible.

## Governance Rules (recommended)
- Keep standalone for scorecard: count >= 100 and stable in 2 consecutive months
- Monitor tier: 30 to 99
- Park/aggregate candidate: < 30 for 2 consecutive months
- Exception rule: strategic-risk labels (privacy, legal, severe trust issues) can stay standalone despite low volume

Probation operations:
- Default probation window: 60 days
- Extended probation (QA/coaching-sensitive labels): 90 days
- Decision SLA after probation close: 5 business days

## Implementation Plan
1. Phase 1 (immediate): configure reporting-layer roll-ups only for General Customer Service and Bill Inquiry/General Bill.
2. Phase 2 (2-week validation): run back-test with roll-ups and compare precision/trend continuity for Care scorecards.
3. Phase 3 (60-day probation): apply Shop & Purchase two-tier reporting and track low-volume nodes.
4. Phase 4 (60-90 day probation): evaluate named-rep split, IVR subtypes, and cross-channel subtypes for Care.
5. Phase 5: monthly AI-council + business-council review with explicit approve/defer decisions.

## What to Keep Unchanged (for now)
- Core operational process topics with demonstrated volume (Issue Resolution, Cross-Channel Friction, Wait Time, Installation, Billing Errors)
- Competitor-specific switching labels under Cancellation & Switching Intent
- Major rep-behavior families that map directly to QA coaching

Care strategic-protection examples:
- Request for Different Communication Support
- Request to Stop Outsourcing / Use Local Staff
- Rep Did Not Follow Through / Broken Promise

## Clarifying Questions Before Final Revision Proposal
1. Do you want the next artifact to be a Care-only v5 mapping table (old label -> reporting roll-up label -> probation window -> owner)?
2. For probation governance, which cadence should I assume: monthly council checkpoint or bi-weekly checkpoint?
3. Should Survey Artifact labels remain visible on Care scorecards, or only in analyst-quality views?
4. For protected low-volume topics (policy/security/workforce), should I mark them as permanent strategic exceptions or review annually?
