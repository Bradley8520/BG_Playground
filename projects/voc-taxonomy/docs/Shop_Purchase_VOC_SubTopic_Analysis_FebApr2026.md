# Shop & Purchase MOB — VOC Sub-Topic Analysis
**Survey Period:** February – April 2026  
**Total Verbatim Records:** 6,582  
**Category Filter:** CATEGORY_LEVEL_2 = `Shop & Purchase_MOB`  
**Analysis Method:** Keyword frequency counts (Select-String regex) + qualitative verbatim review  
**Date Produced:** 2025-07

---

## 1. Executive Summary

Customers surveyed after a Shop & Purchase interaction express frustration dominated by **process failure and broken promises** — not product dissatisfaction. The five most prevalent complaint themes are:

| Rank | Theme | Verbatim Signal Count* |
|------|-------|------------------------|
| 1 | Return/exchange process friction | 1,934 rows mention return/exchange |
| 2 | Upgrade process friction | 1,838 rows mention upgrade |
| 3 | Delivery / fulfillment failure | 891 rows mention delivery/shipping |
| 4 | Order cancellation (unexpected) | 415 rows |
| 5 | Trade-in credit issues | 436 rows |

> \* Signal counts reflect keyword presence in the full verbatim text; a single row may contribute to multiple themes.

**Churn signal is high:** 218 rows explicitly name a competitor (T-Mobile, Verizon, Xfinity) or state intent to switch. 154 additional rows reference cancelling account/service. Combined, ~372 rows (~5.7% of total) carry an active churn indicator.

**Trust is the core issue:** 196 rows include words like *lied*, *misled*, *deceived*, or *false information* — the single sharpest trust-damage signal in the dataset.

---

## 2. Category-Level Distribution (CATEGORY_LEVEL_3)

| CATEGORY_LEVEL_3 | Approx. Row Count | % of Total |
|---|---|---|
| Upgrade_MOB | ~371 | 6% |
| Exchange-Return-Replace_MOB | ~370 | 6% |
| Fulfillment - Order_MOB | ~264 | 4% |
| Add a Line_MOB | ~127 | 2% |
| Fulfillment - Delivery_MOB | ~120 | 2% |
| Want new phone_MOB | ~108 | 2% |
| New Account_MOB | ~57 | <1% |
| IMEI-SIM SHOP_MOB | ~21 | <1% |

> Note: The file contains 6,582 total verbatim records. Many rows carry multi-dimensional complaints that span multiple CATEGORY_LEVEL_3 paths; the above reflects the primary taxonomy assignment, not total volume per theme.

---

## 3. Deep Sub-Topic Analysis

Sub-topics are organized by primary CATEGORY_LEVEL_3 grouping, with cross-references where themes overlap.

---

### 3.1 UPGRADE_MOB — Sub-Topics

**Taxonomy path:** `VOC / Shop & Purchase_MOB / Upgrade_MOB`  
**Keyword signal: 1,838 rows mention "upgrade"**

#### 3.1.1 Upgrade/Activation Fee Surprise — 113 rows
Customers are not informed of the $35 upgrade fee until checkout or billing. Common expressions:
- *"I was not told there would be a $35 upgrade fee"*
- *"Why am I being charged an activation fee for upgrading my own phone?"*
- *"The rep didn't mention any fee. It just showed up on my bill."*

**Root cause:** Point-of-sale disclosure gap. Fee is not surfaced proactively during the upgrade conversation — in store, over the phone, or online.

---

#### 3.1.2 Next Up Anytime Confusion — 38 rows
Issues split between two failure modes:
- **Not offered:** Customers eligible for Next Up Anytime say they were never told the option existed
- **Misunderstood:** Customers enrolled in Next Up Anytime were surprised at the additional monthly cost or unclear on the return/credit terms
- *"No one told me about Next Up Anytime when I bought my phone. Now I'm stuck paying full price."*

---

#### 3.1.3 Upgrade Eligibility Blocked — 15 rows (keyword-matched) + pattern appears more broadly
Customers unable to upgrade due to:
- Outstanding balance on current installment plan
- Plan type restriction (most commonly **55+ plans** — 23 rows explicitly mention 55+ plan and upgrade/eligibility)
- Contract terms or promotional lock-in periods not clearly communicated at time of sale

> **55+ Plan as a structural barrier is a distinct sub-topic:** 23 rows specifically reference the 55+ plan blocking upgrade eligibility or limiting offers available to them. These customers are often long-tenured and express frustration at being penalized for their plan type.

---

#### 3.1.4 Upgrade Process Described as Burdensome — 67 rows
Customers use negative sentiment words (nightmare, horrible, terrible, mess, difficult, hassle, frustrating, disaster, awful) directly adjacent to "upgrade":
- Extended call times (multiple rows reference 2–4 hours) to complete what should be a simple upgrade
- Website/system failures during checkout
- Conflicting quotes from different reps/channels requiring multiple contacts
- *"The upgrade process was an absolute nightmare. Three calls, four reps, still not resolved."*

---

### 3.2 EXCHANGE-RETURN-REPLACE_MOB — Sub-Topics

**Taxonomy path:** `VOC / Shop & Purchase_MOB / Exchange-Return-Replace_MOB`  
**Keyword signal: 1,934 rows mention return or exchange**

#### 3.2.1 No Return Label / Wrong Return Instructions — 54 rows
- Label was not included in original shipment box
- Label was supposed to be emailed but was not received
- Customer was given incorrect drop-off instructions (sent to wrong UPS/FedEx location)
- *"I've been waiting 3 weeks for a return label. I've called 3 times. No one can tell me when it's coming."*

---

#### 3.2.2 30-Day Return Window Not Disclosed — 51 rows
- Customers missed the 30-day window because they were never told about it at time of purchase
- Some customers received incorrect information about the window length (told 45 days, actually 30)
- *"No one told me there was only a 30-day window. By the time I realized the phone wasn't what I wanted it was day 35."*

---

#### 3.2.3 Returned Device — Still Charged / No Credit — 6 rows (explicit pattern) + broader pattern in trade-in section
- Customer has carrier confirmation (UPS/FedEx tracking) that device was returned; AT&T account not updated
- 9 additional rows match "return confirmed by carrier + AT&T not crediting" pattern
- *"I have the UPS tracking number showing AT&T received my phone. They're still charging me."*

---

#### 3.2.4 Equipment Return Fee / Threatened Charge — ~10 rows
- Customers who returned equipment (broadband modems, phones) are threatened with or charged a $150–$200 equipment non-return fee even after confirmed return
- Smaller signal count but high financial impact and customer anger level in verbatims

---

### 3.3 FULFILLMENT - ORDER_MOB — Sub-Topics

**Taxonomy path:** `VOC / Shop & Purchase_MOB / Fulfillment - Order_MOB`  
**Keyword signal: 415 rows — order cancellation; 207 rows — wrong item shipped**

#### 3.3.1 Order Cancelled Unexpectedly — 415 rows  *(second-highest single pattern in dataset)*
This is the **most quantifiable specific complaint** in the file. Root causes cluster into:
- System or identity verification failure at checkout (driver's license scan failure, credit check trigger)
- Payment processing failure (card declined, funds held/pending, duplicate charge)
- Representative-initiated cancellation with no explanation
- *"My order just disappeared. No email, no notification. When I called, no one knew why it was cancelled."*
- *"The online system kept failing during checkout. After 3 attempts it locked me out and cancelled my order."*

---

#### 3.3.2 Wrong Item Shipped — 207 rows
- Wrong phone model, wrong color, wrong storage capacity
- Wrong broadband modem/router shipped (common in broadband + mobile combined orders)
- Wrong SIM type
- *"They sent me the Samsung Galaxy when I ordered the iPhone 16. How does this happen?"*
- *"Got a refurbished modem when I was promised a new one."*

---

#### 3.3.3 Multi-Hour Call Time to Complete Order — 103 rows
- Customers reference spending 2–5 hours on a single call just to place or correct an order
- Often involves multiple transfers and repeated account verification steps
- *"I spent 4 hours on the phone to add a line. By hour 3 I was crying."*

---

#### 3.3.4 System / Payment Failure — 14 rows (explicit) + broader context in order cancellation theme
- Card charged but order not placed
- Duplicate pending charges on bank account (customers report $400–$1,200 funds being held)
- Website checkout freezes mid-flow

---

### 3.4 FULFILLMENT - DELIVERY_MOB — Sub-Topics

**Taxonomy path:** `VOC / Shop & Purchase_MOB / Fulfillment - Delivery_MOB`  
**Keyword signal: 891 rows mention delivery/shipping**

#### 3.4.1 Late / Missing / Lost Delivery — 36 rows (explicit pattern)
- Package marked as "lost in transit" with no resolution path offered
- Delivery significantly later than promised date
- *"My phone has been 'in transit' for 11 days. FedEx says to contact AT&T. AT&T says contact FedEx."*

---

#### 3.4.2 Next-Day / Overnight Shipping Not Honored — 40 rows
- Customer paid for next-day or overnight delivery; actual delivery took 3–7 days
- Rep promised same-day or next-day; shipping confirmation showed standard delivery
- *"I was told it would arrive the next day. It's been 5 days."*

---

#### 3.4.3 Signature Required / Missed Delivery — 20 rows
- Device requires adult signature; customer was not home; no re-delivery option offered
- FedEx held package at facility 30+ miles away with short pickup window
- No alternative (neighbor signature, locker pickup) offered
- *"They require a signature but don't let you change the delivery time. I had to take off work."*

---

### 3.5 WANT NEW PHONE_MOB / ADD A LINE_MOB — Sub-Topics

**Taxonomy path:** `VOC / Shop & Purchase_MOB / Want new phone_MOB` and `Add a Line_MOB`

#### 3.5.1 Loyalty / Value Gap for Long-Term Customers — 210 rows
This is one of the **most emotionally intense** themes in the dataset. Signal: 210 rows explicitly reference customer tenure (e.g., "10-year customer," "20 years with AT&T," "loyal customer").

- New customer promotions, deals, and device credits are perceived as significantly better than what long-term customers are offered
- 55+ plan holders and legacy plan holders especially feel the gap
- 218 rows name a specific competitor (T-Mobile, Verizon, Xfinity) as offering a better deal
- 154 rows threaten to cancel account/service
- *"I've been with AT&T for 22 years. T-Mobile offered me a free phone just for switching. AT&T offered me nothing."*
- *"New customers get a free iPhone. I have to pay full price as a 15-year customer. That's insulting."*

> **Churn overlap:** The loyalty gap theme and churn intent are strongly correlated. ~372 combined rows carry a churn signal.

---

#### 3.5.2 Add a Line — Process Complexity and Errors — 127 rows in Add a Line category
- Multiple calls and hours required to add a line (should be a simple transaction)
- Incorrect information given about cost of adding a line
- Line added to wrong account, wrong plan, or wrong device
- Store and phone channel give conflicting instructions
- *"It took 3 calls and 6 hours to add one line for my kid. This is ridiculous."*

---

### 3.6 NEW ACCOUNT / ONBOARDING — Sub-Topics

**Taxonomy path:** `VOC / Shop & Purchase_MOB / New Account_MOB`

#### 3.6.1 SIM / IMEI Activation Failures — overlaps with IMEI-SIM SHOP_MOB (21 rows)
- SIM card not received after signup
- Port-in from another carrier stalled or never completed
- Account activated with wrong device identifier (IMEI)
- *"I switched from Verizon 2 weeks ago. My old number still doesn't work on my new SIM."*

---

#### 3.6.2 Channel Onboarding Inconsistency
- Different information received online, in-store, and on the phone
- Account setup errors (wrong email address, wrong billing address captured)
- No continuity of notes between channels — customer must re-explain from scratch each contact

---

## 4. Cross-Cutting Themes (Appear Across All CATEGORY_LEVEL_3 Groups)

These themes are not tied to one taxonomy node — they surface across the entire dataset.

---

### 4.1 Pricing / Promotional Misrepresentation — 196+ rows

| Sub-Pattern | Count |
|---|---|
| Rep described as lying, misleading, or giving false information | 196 |
| Bill higher than what rep quoted | 13 |
| Told phone was free, now being charged | 21 |
| Promotion or credit not applied to account | 6 |
| Trade-in value misrepresented at point of sale | 19 |

**Total misrepresentation-related rows: ~255** (with overlap)

This is the most trust-damaging theme in the dataset. Customers use strong language: *lied*, *deceived*, *fraud*, *bait and switch*, *false advertising*.

> Representative verbatim: *"The rep told me my bill would be $85/month. My first bill was $147. When I called back, nobody would honor what I was told."*

---

### 4.2 Call Handling Failure — 267–449 rows

| Sub-Pattern | Count |
|---|---|
| Call dropped, hung up, or no callback provided | 267 |
| Multiple calls or transfers needed to resolve | 182 |
| Language barrier / couldn't understand rep | 85 |
| Unwanted upsell pushed during issue call | 60 |

**Combined: ~450+ rows** (with overlap)

Call handling quality is a widespread amplifier of frustration — a customer who already had a fulfillment failure is significantly more likely to escalate or churn if their service call is also mishandled.

> Representative verbatim: *"I was transferred 4 times and on hold for 2 hours. The last rep hung up on me. I'm done."*

---

### 4.3 Unauthorized / Fraudulent Additions — 43 rows

- Lines added without customer consent
- Insurance/ProTech plans added without permission (recurring theme)
- Charges appearing on bill that customer did not authorize
- *"I called about my upgrade and suddenly there was a new line on my account I never asked for."*
- *"They added a $17/month protection plan without asking me. When I called to remove it, I was told it couldn't be removed until the next billing cycle."*

---

### 4.4 Channel Inconsistency — Broad Signal
*(Pattern match returned 0 for narrow regex; qualitatively observed in hundreds of verbatims)*

A pervasive structural issue: customers receive different information from in-store, phone (611/1-800), and online channels. No channel has visibility into what the customer was promised in another channel.

Common patterns:
- *"The store told me to call. The call center told me to go back to the store."*
- *"I accepted an offer online. The rep on the phone said that offer doesn't exist."*
- *"I've explained my situation to 5 different reps. No one has any notes from the last call."*

---

## 5. Key Findings and Priority Actions

### Finding 1: Order Cancellation is the #1 Specific Failure Point
415 rows describe an unexpected order cancellation. This directly drives calls to 611, frustration, and churn. Root cause is likely a combination of system-side identity/payment verification failures and rep-initiated cancellations without notification. **Recommend:** Identify the top 3 system error codes triggering auto-cancellation and audit the customer notification workflow.

### Finding 2: Trade-In is a Broken Promise at Scale
436 verbatims mention trade-in. Of these, 73 say the credit was not applied or is missing, 19 describe misrepresentation of the trade-in value, and 9 say their phone was lost. Trade-in promises are frequently the primary reason a customer agrees to upgrade — when the credit doesn't appear, it directly drives distrust and churn. **Recommend:** Audit trade-in credit application SLA; mandate upfront disclosure of trade-in value estimate at point of sale before customer commits.

### Finding 3: Trust Damage is Quantifiable — 196+ "lied/misled" Rows
The single most diagnostic signal of a systemic issue: 196 rows use trust-breaking language. When combined with pricing misrepresentation sub-patterns (~255 total rows), this is the highest-severity theme in the dataset. **Recommend:** Mystery shop / call auditing targeted at the "price and credit promise" moment in upgrade and new device transactions.

### Finding 4: Churn Risk is Concentrated and Trackable
~372 rows carry an explicit churn indicator (competitor name or account cancellation language). Many of these customers identify themselves as long-tenured (210 rows explicitly reference years of loyalty). **Recommend:** Integrate churn-signal verbatim flagging into the post-interaction workflow so these customers can be triaged to a retention queue within 24 hours.

### Finding 5: Call Handling Failure Amplifies Every Other Issue
267 rows describe a call drop, hang-up, or no callback. 182 describe needing multiple calls. When a customer already has a delivery failure or a billing discrepancy, a mishandled service call converts a recoverable complaint into a defection. **Recommend:** Prioritize callback-completion rate as a standalone KPI, separate from FCR.

### Finding 6: 55+ Plan Customers Are a Disproportionately Vocal Segment
23 rows explicitly name the 55+ plan as a barrier to upgrade eligibility or competitive offers. This segment likely punches above its row count in terms of tenure length and lifetime value. The loyalty gap theme is particularly acute for this group.

---

## 6. Methodology Notes

- **Keyword matching** using PowerShell `Select-String` with case-insensitive regex against all 6,582 rows of the raw CSV
- A single row may be counted in multiple themes if it contains keywords for more than one pattern
- Counts represent **rows containing at least one keyword match**, not total keyword occurrences
- Narrow patterns (e.g., "30-day return window") undercount relative to actual theme volume; qualitative review of verbatims confirms each theme is more prevalent than keyword counts alone suggest
- The `equipment return fee` pattern (regex escaped `$150`/`$200`) had an error in one run; a simplified alternative pattern returned ~10 rows
- Channel Inconsistency pattern returned 0 on the specific regex tested (too narrow); qualitative reading of ~500 verbatims confirms this is a high-volume theme not yet fully captured by keyword search

---

*Analysis produced from: `Shop_Purchase_Verbatims_Feb-Apr2026.csv`*  
*Keyword quantification method: PowerShell `Select-String` / case-insensitive regex*  
*Qualitative review: ~500 verbatim records read directly across full date range (Feb–Apr 2026)*
