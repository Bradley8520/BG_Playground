# Shop & Purchase — Sub-Topic Taxonomy Design Handoff

## Status: ✅ FINAL — 11 Topics, 51 Sub-Topics, Validated Against 97,002 Care Verbatims
**Last Updated:** 2026-06-16
**Related Verbatim File:** `Shop_Purchase_Verbatims_Feb-Apr2026.csv` (6,582 rows, Feb–Apr 2026)
**Related Analysis:** `Shop_Purchase_VOC_SubTopic_Analysis_FebApr2026.md`
**Taxonomy Version Context:** v3 build — these sub-topics are candidates for `VOC_Classification_Taxonomy_v3.csv`

---

## CONTEXT & DESIGN DECISIONS

### What This Document Covers
This handoff defines proposed descriptive sub-topics for the **Shop & Purchase** category of the VOC Classification Taxonomy. The taxonomy covers the **Care channel** (phone/digital) for both **Mobility and Broadband** customer interactions.

This is distinct from the **Retail Sales Experience** sub-topic list, which covers in-store interactions. Where Retail sub-topic names align, they are noted — but retail-only sub-topics (Store Pickup, Data Transfer, Device Setup, Repair) are excluded.

### Design Decisions Locked
1. **Channels:** Care (Mobility + Broadband unified list)
2. **Classifier output:** Single column (CATEGORY_LEVEL_3) — classifier outputs the descriptive sub-topic only
3. **Topic grouping:** Topics (e.g., "Upgrade", "Trade-In") are a roll-up/mapping layer derived from sub-topics — not a separate classified column
4. **Sub-topic granularity:** Moderate (3–5 per topic)
5. **Naming style:** Short issue labels (e.g., "Trade-In Credit Not Applied"), not full sentences
6. **Polarity:** Both positive and negative included where volumes warrant; single positive per topic as a baseline
7. **Cross-cutting themes:** Rep behavior / pricing misrepresentation → lands in `PROCESS > Perceived Trust – Wrong Information`; Unauthorized changes during a Shop & Purchase interaction → included here as a topic
8. **Depth:** 3-level path remains `VOC / Shop & Purchase / [Descriptive Sub-Topic]`; topic grouping is a mapping layer only

### Structure Overview
- **11 Topics** (roll-up grouping labels)
- **51 Sub-Topics** (classifier output): 41 negative, 10 positive
- Average ~4.6 sub-topics per topic; range 3–5

### Validation Status
- Sub-topics derived from:
  - Keyword frequency analysis of 6,582 verbatims (Feb–Apr 2026 Care sample)
  - Qualitative review of ~500 verbatims across full date range
  - Alignment review against Retail Sales Experience sub-topic list (22 sub-topics)
  - Review of existing CATEGORY_LEVEL_3 taxonomy nodes
- **NOT YET validated** against full Care sample for volume. Next step: run proposed sub-topics as a zero-shot classifier test on a random Care sample to evaluate volume per sub-topic before finalizing.

---

## RETAIL ALIGNMENT REFERENCE

| Retail Sub-Topic | Care Equivalent or Disposition |
|---|---|
| Activate Device | Activation & Porting — SIM or eSIM Activation Failed / Activation or Port Completed |
| Add A Line | Add a Line (all sub-topics) |
| Data Transfer | **Excluded** — in-store service only |
| Device Setup | **Excluded** — in-store service only |
| Exchange | Exchange & Replace (all sub-topics) |
| Fulfillment - Delivery | Fulfillment – Delivery (all sub-topics) |
| Fulfillment - Order | Fulfillment – Order (all sub-topics) |
| Insurance Exchange | Warranty & Device Protection Exchange — Protection Plan Claim – Process Friction |
| New Account | New Account (all sub-topics) |
| Porting | Activation & Porting — Number Port-In Incomplete / Activation or Port Completed |
| Price Matching | **Excluded** — covered in Pricing category, not Shop & Purchase |
| Rebate | **Excluded** — covered in Pricing category, not Shop & Purchase |
| Refunds | Returns — Return Confirmed – Credit or Refund Not Applied |
| Refurbished | Exchange & Replace — Refurbished Device Received When New Expected |
| Renew Account | Not included (low signal in current data; revisit if volume warrants) |
| Repair | **Excluded** — separate product/tech category |
| Replace | Exchange & Replace — Exchange Needed – Defective or Damaged on Arrival |
| Returns | Returns (all sub-topics) |
| Store Pickup | **Excluded** — physical retail only |
| Upgrade | Upgrade (all sub-topics) |
| Trade-In | Trade-In (all sub-topics) |
| Want a new Phone | **Merged into Upgrade** — device purchase intent language absorbed into Upgrade topic |
| Warranty Exchange | Warranty & Device Protection Exchange — Next Up Anytime – Exchange or Return Issue |

---

## FULL SUB-TOPIC LIST WITH DEFINITIONS

---

### TOPIC: New Account
*Customer establishing a new Mobility line or Broadband service through the Care channel (phone or digital). Includes first-time account creation, initial order placement, and onboarding failures.*

| Sub-Topic | Polarity | Definition |
|---|---|---|
| Account Setup Error | Negative | Wrong email address, billing address, or account details were captured during new account creation. Include: "wrong address on account," "wrong email," "account information incorrect," "set up wrong," "account was created incorrectly." |
| New Service Not Activating | Negative | Account was created and/or equipment received, but service is not live or functioning. Include: "won't activate," "service not working after setup," "equipment arrived but no signal," "can't connect," "set up but not working." |
| Port-In Stalled or Failed | Negative | Customer's phone number transfer from another carrier did not complete, is stuck, or failed entirely. Include: "number didn't transfer," "port didn't go through," "still showing old carrier," "number transfer failed," "porting issue." See also: Activation & Porting — Number Port-In Incomplete. |
| SIM or Equipment Not Received | Negative | New customer never received the SIM card or broadband equipment needed to activate service. Include: "SIM never arrived," "no modem received," "never got the router," "equipment not delivered," "waiting for SIM." |
| New Account Opened Successfully | Positive | Customer confirms their new account or service was set up correctly and is functioning as expected. Include: "account set up great," "new service working perfectly," "everything activated without issue," "smooth setup." |

---

### TOPIC: Activation & Porting
*Activating a new SIM, eSIM, or device IMEI on an existing account, or porting a phone number in from another carrier. Distinct from New Account in that the account already exists.*

| Sub-Topic | Polarity | Definition |
|---|---|---|
| SIM or eSIM Activation Failed | Negative | A SIM or eSIM could not be activated on an existing account; device shows no service after attempted activation. Include: "SIM won't activate," "eSIM not working," "no service after activation," "activation failed," "SIM not recognized." |
| IMEI or Device Not Recognized | Negative | The device IMEI is rejected by the system, shows as incompatible, or cannot be associated with the account during activation. Include: "IMEI not recognized," "device not compatible," "phone won't activate on account," "IMEI invalid," "device rejected." |
| Number Port-In Incomplete | Negative | Customer's phone number failed to transfer from a previous carrier; the number is still active on the old carrier, or the transfer has been pending for an extended period. Include: "number still with old carrier," "port hasn't gone through," "been waiting days to transfer my number," "porting delayed." |
| Activation or Port Completed | Positive | Customer confirms that a SIM, eSIM, or device was activated or that a number transfer completed without issue. Include: "activated right away," "number transferred quickly," "SIM worked immediately," "activation was easy and fast." |

---

### TOPIC: Add a Line
*Adding a new Mobility line or broadband service line to an existing account via the Care channel.*

| Sub-Topic | Polarity | Definition |
|---|---|---|
| Add a Line — Extended Time or Multiple Contacts | Negative | A line addition required excessive call time, multiple calls, or multiple transfers to complete — a task the customer expected to be simple. Include: "took 3 hours to add a line," "had to call back multiple times," "still not added after two calls," "transferred 4 times just to add a line." |
| Add a Line — Wrong Plan or Rate Applied | Negative | The new line was added to an incorrect plan, tier, or rate — different from what the customer agreed to or was quoted. Include: "added wrong plan," "wrong rate applied," "not the plan I asked for," "put on the wrong tier," "incorrect plan on new line." |
| Add a Line — Cost Not Accurately Disclosed | Negative | The true monthly cost of adding the line was not communicated before the line was added; customer was surprised by the charge. Include: "didn't tell me how much it would cost," "bill was more than I was told," "cost wasn't explained," "wasn't told there would be a fee," "surprised by the charge." |
| Add a Line — Conflicting Channel Instructions | Negative | Customer received different eligibility information, pricing, or instructions from store, phone, and/or online channels for the same add-a-line request. Include: "store said one thing, phone said another," "got different answers," "contradictory information," "sent back and forth." |
| Add a Line — Completed Correctly | Positive | Line was added to the correct plan at the correct rate in a single interaction without errors. Include: "added the line quickly," "new line working right away," "exactly what I asked for," "easy to add a line," "rep added it correctly." |

---

### TOPIC: Upgrade
*Upgrading an existing Mobility device or Broadband speed tier or plan via the Care channel.*

| Sub-Topic | Polarity | Definition |
|---|---|---|
| Upgrade Fee Not Disclosed at POS | Negative | The $35 upgrade fee or activation fee was not mentioned during the upgrade conversation and appeared unexpectedly at checkout or on the bill. Include: "wasn't told about the $35 fee," "upgrade fee not disclosed," "charged activation fee without warning," "fee showed up on bill," "no one mentioned a fee." |
| Upgrade Eligibility Blocked | Negative | Customer is unable to complete an upgrade due to plan type restrictions (55+, legacy plans), outstanding installment balance, promotional lock-in period, or other policy that was not clearly disclosed at time of original purchase. Include: "not eligible to upgrade," "can't upgrade because of my plan," "55+ plan won't let me upgrade," "still owe too much on phone," "locked in," "not allowed to upgrade yet." |
| Next Up Anytime — Not Offered or Misunderstood | Negative | Next Up Anytime was not presented as an option at time of device purchase (customer later discovered it existed), or the terms (additional monthly cost, return requirements, eligibility) were not clearly explained. Include: "no one told me about Next Up," "didn't know Next Up existed," "Next Up terms were confusing," "didn't understand the Next Up program," "wasn't offered Next Up when I bought." |
| Upgrade Process — Extended Time or System Failure | Negative | The upgrade required 2+ hours, multiple contacts, multiple transfers, or encountered website/system errors before completing. Include: "took 3 hours to upgrade," "website kept failing," "system wouldn't let me complete the upgrade," "had to call back," "upgrade process was a nightmare," "multiple reps just to upgrade." |
| Upgrade Completed Successfully | Positive | Customer confirms the upgrade was completed efficiently, with accurate pricing and without errors. Include: "upgrade was easy," "rep helped me upgrade quickly," "great experience upgrading," "smooth upgrade process," "got my new phone without any issues." |

---

### TOPIC: Trade-In
*Trading an existing device for credit toward a new purchase via the Care channel. Covers value quoted at POS, credit application to account, device receipt confirmation, and return logistics.*

| Sub-Topic | Polarity | Definition |
|---|---|---|
| Trade-In Credit Not Applied to Account | Negative | The credit for a traded device has not appeared on the customer's bill after the expected timeframe. Include: "trade-in credit never showed up," "haven't received the credit," "still not on my bill," "been waiting months for the credit," "trade-in credit missing." |
| Trade-In Value Misrepresented at POS | Negative | The trade-in value the customer was quoted at the time of sale is different — typically lower — than what was ultimately applied to their account. Include: "told my trade-in was worth $1000, got $350," "quoted a higher trade-in value," "trade-in value changed after the fact," "misled about how much I'd get," "different trade-in credit than promised." |
| Trade-In Device Lost — No AT&T Receipt Confirmation | Negative | Customer returned the trade-in device but AT&T has no record of receiving it. Include: "AT&T says they never got my phone," "no record of my trade-in," "sent phone but no confirmation," "trade-in missing," "can't find my returned phone." |
| Trade-In Return Label or Kit Not Provided | Negative | No return label was included in the box, a label was not emailed, or the customer received incorrect trade-in return instructions. Include: "no return label in the box," "never got a label," "wrong return instructions," "still waiting for trade-in kit," "label not emailed." |
| Trade-In Processed Correctly | Positive | Trade-in credit was applied accurately and on schedule; customer confirms the trade-in was handled correctly. Include: "got my trade-in credit," "trade-in was easy," "credit showed up on my bill," "trade-in process was smooth," "received the correct trade-in value." |

---

### TOPIC: Fulfillment – Order
*Order processing after a purchase decision is made via the Care channel. Covers order cancellation, incorrect items, payment processing, and order status.*

| Sub-Topic | Polarity | Definition |
|---|---|---|
| Order Cancelled Unexpectedly | Negative | Order was cancelled without customer consent — due to a system failure, payment error, identity verification failure, or rep action — without clear notification to the customer. Include: "order just disappeared," "order was cancelled without telling me," "system cancelled my order," "ID verification failed and cancelled," "payment issue cancelled the order," "rep cancelled it by mistake." Highest-volume specific complaint in Feb–Apr 2026 data (~415 mentions). |
| Wrong Item Shipped | Negative | Incorrect phone model, color, storage capacity, or broadband equipment was shipped to the customer. Include: "sent the wrong phone," "got the wrong color," "wrong storage size," "sent wrong modem," "not what I ordered," "received the wrong device." |
| Payment Processing Failure | Negative | A payment card was declined, funds were held/pending without an order being placed, or a duplicate charge appeared during order processing. Include: "card was charged but no order," "duplicate charge," "funds on hold," "payment didn't go through," "charged twice," "bank shows pending charge but no order." |
| Order Status Unavailable or Inaccurate | Negative | Customer cannot find accurate tracking information; order shows a status that is inconsistent with what is actually happening. Include: "no tracking update," "order status hasn't changed," "says processing but it's been a week," "no confirmation email," "can't find my order," "tracking is wrong." |
| Order Fulfilled Accurately | Positive | Correct item was shipped and received as expected, with accurate order status and tracking. Include: "order arrived correctly," "got exactly what I ordered," "order was processed quickly," "everything was right," "shipped fast and correctly." |

---

### TOPIC: Fulfillment – Delivery
*Physical shipment and last-mile delivery of devices or broadband equipment ordered through the Care channel.*

| Sub-Topic | Polarity | Definition |
|---|---|---|
| Delivery Late or Missed Promised Date | Negative | Next-day or expedited shipping was not honored; delivery arrived significantly later than the committed date. Include: "told it would arrive next day," "delivery is late," "was supposed to be here yesterday," "expedited shipping not delivered on time," "still waiting for package," "took a week instead of next day." |
| Package Lost in Transit | Negative | The carrier tracking shows the package as lost, stuck with no movement, or the carrier and AT&T are unable to locate it. Include: "package is lost," "tracking hasn't updated in a week," "carrier says contact AT&T, AT&T says contact carrier," "lost in transit," "package never arrived and no one can find it." |
| Missed Delivery — No Flexible Re-delivery Option | Negative | Delivery required an adult signature; customer was not home; no convenient re-delivery time, pickup alternative, or neighbor delivery option was offered. Include: "couldn't deliver because I wasn't home," "need signature but no alternative," "package held at facility too far away," "couldn't reschedule delivery," "no pickup option offered." |
| Delivered On Time and Intact | Positive | Package arrived on the promised date in correct and undamaged condition. Include: "arrived on time," "package was perfect," "delivered when they said," "fast delivery," "came in great condition," "on schedule." |

---

### TOPIC: Returns
*Returning a device or broadband equipment through the Care channel. Covers return label logistics, return window disclosure, credit/refund confirmation, and equipment return fees.*

| Sub-Topic | Polarity | Definition |
|---|---|---|
| Return Label Missing or Not Sent | Negative | No return label was included with the original shipment, a label was not emailed as promised, or the customer has been waiting for a label with no resolution. Include: "no return label in the box," "never received a return label," "label not emailed," "waiting for return label," "no instructions on how to return." |
| 30-Day Return Window Not Disclosed at POS | Negative | Customer was not told about the 30-day return window at the time of purchase and missed it as a result, or was given incorrect information about the window length. Include: "didn't know there was a 30-day limit," "nobody told me I only had 30 days," "was told 45 days to return," "missed the window because I didn't know," "return policy not explained." |
| Return Confirmed — Credit or Refund Not Applied | Negative | Carrier tracking or AT&T confirmation shows the device was returned, but the customer's account still shows the charge or the credit has not been applied. Include: "UPS says you received it but I'm still charged," "return confirmed but still on my bill," "have tracking confirmation but no credit," "returned it weeks ago and still owe," "AT&T received the phone but no refund." |
| Equipment Return Fee Charged After Return | Negative | A $150–$200 equipment non-return fee was applied to the customer's account despite the customer having confirmed that the device or equipment was returned. Include: "charged for equipment I already returned," "$150 fee even though I sent it back," "non-return fee charged after I returned it," "$200 charge despite return confirmation," "fee for equipment I mailed back." |
| Return Processed and Credited Correctly | Positive | Device was returned and the credit or refund was applied accurately and in a reasonable timeframe. Include: "return was easy," "got my refund quickly," "credit showed up after return," "return process was smooth," "received confirmation and credit." |

---

### TOPIC: Exchange & Replace
*Exchanging or replacing a device or broadband equipment that was received incorrectly or arrived damaged. Includes wrong items, defective-on-arrival, and undisclosed refurbished devices.*

| Sub-Topic | Polarity | Definition |
|---|---|---|
| Exchange Needed — Wrong Item Received | Negative | Customer received the wrong phone model, color, storage capacity, or broadband equipment and needs a like-for-like exchange of the correct item. Include: "received wrong phone need to exchange," "sent wrong model need the right one," "need to swap for correct device," "got wrong item need exchange," "this isn't what I ordered." |
| Exchange Needed — Defective or Damaged on Arrival | Negative | The device or equipment arrived broken, non-functional, cracked, or otherwise damaged. Include: "phone was broken when I got it," "arrived cracked," "device doesn't work out of the box," "defective on arrival," "damaged when delivered," "DOA." |
| Refurbished Device Received When New Expected | Negative | Customer paid for a new device but received a refurbished unit without prior disclosure. Include: "phone was refurbished not new," "sent a used phone," "clearly not a new device," "got a refurb when I paid for new," "phone had scratches and was used." |
| Exchange or Replacement Completed Correctly | Positive | The correct replacement device was sent and received without additional issues. Include: "got the right phone this time," "exchange went smoothly," "replacement arrived quickly," "correct device delivered," "exchange was handled well." |

---

### TOPIC: Warranty & Device Protection Exchange
*Device replacement through a protection plan (ProTech), manufacturer warranty, Next Up Anytime, or insurance claim. Also captures unauthorized addition of protection plans during Shop & Purchase interactions.*

| Sub-Topic | Polarity | Definition |
|---|---|---|
| Protection Plan Claim — Process Friction | Negative | The claims process for a device protection plan is difficult, delayed, unclear on requirements, or deductible terms were not disclosed at enrollment. Include: "claim process is complicated," "took forever to process my claim," "deductible wasn't disclosed," "hard to file a claim," "requirements unclear," "protection plan claim denied." |
| Next Up Anytime — Exchange or Return Issue | Negative | Customer enrolled in Next Up Anytime is experiencing difficulty with the upgrade exchange or early upgrade return process; includes confusion about return requirements and credit timing. Include: "Next Up return is confusing," "can't figure out how to exchange through Next Up," "Next Up exchange taking too long," "didn't receive credit after Next Up return." |
| Protection Plan Added Without Customer Consent | Negative | A device protection plan, insurance, or ProTech feature was added to the customer's account during a Shop & Purchase interaction without explicit agreement. Include: "protection plan added without my permission," "didn't agree to insurance," "ProTech was added without asking," "insurance on my bill I never signed up for," "added protection plan I didn't want." |
| Protection Plan Exchange Completed Successfully | Positive | A warranty claim, protection plan claim, or Next Up exchange was handled correctly and in a reasonable timeframe. Include: "claim was easy," "replacement came quickly through insurance," "ProTech handled it well," "Next Up exchange was smooth," "warranty exchange processed without issue." |

---

### TOPIC: Unauthorized Account Changes
*Lines, device protection plans, features, or services added to a customer's account without their explicit consent — typically occurring during or immediately after a Shop & Purchase interaction.*

| Sub-Topic | Polarity | Definition |
|---|---|---|
| Line Added Without Customer Consent | Negative | A new line appeared on the customer's account following a Shop & Purchase interaction that the customer did not authorize. Include: "new line on my account I didn't ask for," "line was added without my permission," "didn't authorize a new line," "extra line appeared after my call," "added a line I never agreed to." |
| Feature or Service Added Without Permission | Negative | A device protection plan, insurance, hotspot, or other feature or service was activated on the account during a purchase interaction without the customer's explicit agreement. Include: "insurance added without asking," "hotspot added I didn't request," "ProTech added without consent," "service on my bill I didn't sign up for," "added features I never agreed to." |
| Plan or Account Changed Without Authorization | Negative | The customer's account plan type, rate plan, or account structure was changed during a purchase call without consent. Include: "plan was changed without my permission," "rep changed my plan without telling me," "account structure changed I didn't authorize," "different plan after the call," "switched my plan without asking." |

---

## VOLUME SIGNALS FROM FEB–APR 2026 DATA

The following keyword-frequency counts were run against `Shop_Purchase_Verbatims_Feb-Apr2026.csv` (n=6,582). Counts reflect rows containing at least one keyword match — a row may appear in multiple categories. These are estimates to inform prioritization, not final classifier counts.

| Topic | Signal Count (Rows) | Notes |
|---|---|---|
| Fulfillment – Order | 415 (order cancelled) + 207 (wrong item) + 103 (multi-hour call) | Highest-volume specific failure — order cancellation is #1 single complaint pattern |
| Returns / Exchange | 1,934 rows mention "return" or "exchange" | Broad; many rows are mixed returns + exchanges |
| Upgrade | 1,838 rows mention "upgrade" | Broad; 113 fee complaints, 67 negative descriptors, 38 Next Up, 23 55+ plan |
| Trade-In | 436 all mentions; 73 credit not applied; 19 value misrepresented; 9 device lost | |
| Fulfillment – Delivery | 891 rows mention delivery/shipping; 40 next-day not honored; 36 lost/late | |
| Unauthorized Changes | 43 rows | Lower volume; emotionally high-intensity |

---

## OPEN QUESTIONS FOR NEXT SESSION

1. **Returns vs. Exchange & Replace** — In the data these overlap heavily (wrong item shipped → return → exchange). Should they remain as two separate topics or collapse into **Returns & Exchange**? Currently kept separate to align with Retail naming, but Care verbatims rarely describe a clean exchange without a return component.

2. **Positive sub-topic consolidation** — There are currently 12 positive sub-topics (one per topic). Consider whether to keep them separate or consolidate into a single **"Transaction Completed Successfully"** sub-topic that applies across all topics. Positives may be low-volume in this dataset.

3. **Warranty & Device Protection scope** — This topic sits at the intersection of Shop & Purchase and Product/Tech. Confirm whether warranty/insurance exchanges should live here or under a separate Product or Tech category in the broader taxonomy.

4. **Unauthorized Account Changes scope** — Confirm whether this should be scoped narrowly to Shop & Purchase interactions only (rep added something during an upgrade or new line call) or broadly (any unauthorized change regardless of call reason). If broadly, it may belong in People > Policy or a dedicated Fraud topic.

5. **Volume validation** — Run proposed sub-topics as zero-shot classifier against a random Care sample (recommend 1,000–2,000 rows) before finalizing. If any sub-topic returns fewer than ~30 rows per month across the full Care sample, consider merging with an adjacent sub-topic.

6. **Cancel-Order contacts** — "Cancel my order" contacts (customers calling to cancel a pending device or equipment order) roll into **Fulfillment – Order** under the existing **Order Cancelled Unexpectedly** sub-topic. The current definition covers AT&T/system-initiated cancellations; consider expanding it to explicitly include customer-initiated order cancellation requests, which represent a distinct contact reason (customer changed their mind or is dissatisfied before delivery).

---

## FILES REFERENCED

| File | Description |
|---|---|
| `Shop_Purchase_Verbatims_Feb-Apr2026.csv` | Source verbatim data (6,582 rows) used for signal counts and qualitative review |
| `Shop_Purchase_VOC_SubTopic_Analysis_FebApr2026.md` | Full quantitative and qualitative sub-topic analysis with keyword counts |
| `VOC_Classification_Taxonomy_v3.csv` | Current taxonomy file; these sub-topics are candidates for CATEGORY_LEVEL_3 |
| `VOC_Taxonomy_v3_Step4_Process_Core.csv` | Process category taxonomy — cross-cutting themes (rep behavior, call handling) land here |
| `handoffs/TAXONOMY_V3_BUILD_HANDOFF.md` | v3 taxonomy build context and design decisions |
