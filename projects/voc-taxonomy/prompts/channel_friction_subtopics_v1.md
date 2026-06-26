================================================================================
CHANNEL FRICTION SUB-TOPIC DEFINITIONS — CLASSIFICATION PROMPT REFERENCE
================================================================================
Source Data   : Retail_Store_Verbatims_Feb-Apr2026.csv
Survey Channel: Care (call center VOC, SMS-delivered)
Date Range    : February 2026 – April 2026
Total N       : 4,244 verbatims
Analysis Date : 2026-06-15
Category      : Process
Topic         : Channel Friction (Care ↔ Store)
Topic Def     : Failures that occur when customers are routed between the Care
                channel and the Retail Store channel — including unjustified
                referrals, deflection, circular handoffs, and inconsistent
                information across channels — resulting in unresolved issues
                and repeated customer effort.
================================================================================

CLASSIFICATION INSTRUCTIONS FOR THESE THEMES:
- These themes apply to the CARE channel survey only.
- Because this is a Care survey, the customer is always calling/calling in.
  References to "the store" describe a prior or parallel in-person interaction.
- Apply Process-category channel friction themes to ANY multi-interaction
  feedback — they are NOT restricted to the most recent rep (unlike People
  themes).
- A verbatim may match MORE than one channel friction theme if multiple friction
  types are independently evidenced.
- Do NOT apply these themes to positive store mentions unless friction language
  is also present.

================================================================================
SUB-TOPICS (5)          — Volume Summary
================================================================================

 Rank  Sub-Topic                                          Count    % of Total
 ----  -------------------------------------------------  -------  ----------
  1    Care-to-Store Referral: Tech / Device Issue          342       8.1%
  2    Care-to-Store Referral: Billing, Account & Policy    226       5.3%
  3    Store-to-Care Deflection                             220       5.2%
  4    Circular Runaround: Neither Channel Resolves         213       5.0%
  5    Conflicting Information: Store vs. Care              192       4.5%
       ─────────────────────────────────────────────────  -------  ----------
       Combined channel friction volume                   ~1,193    ~28.1%

Note: Counts are keyword-pattern estimates from regex search across verbatim
text. Verbatims may match more than one sub-topic. Use for volume benchmarking;
exact counts will vary with full AI classification.

================================================================================
SUB-TOPIC DEFINITIONS (Prompt Format)
================================================================================

────────────────────────────────────────────────────────────────────────────────
SUB-TOPIC 1: Care-to-Store Referral: Tech / Device Issue
────────────────────────────────────────────────────────────────────────────────
Category   : Process
Topic      : Channel Friction (Care ↔ Store)
Polarity   : Negative
Channel    : Care
Est. Count : 342 (8.1%)
Owner      : Care Channel Operations / Repair Routing

DEFINITION:
A Care rep referred or directed the customer to visit a retail store specifically
because the rep could not resolve a technical or device-related issue over the
phone. The customer expresses frustration at being asked to make a physical trip
for what they perceive as a phone-serviceable problem, OR the customer went to
the store and it still was not resolved.

INCLUDE when the verbatim contains explicit evidence of ALL of the following:
  (a) A Care rep redirected the customer to a store (or the customer went to a
      store after Care failed), AND
  (b) The reason is device- or tech-related: SIM card swap, eSIM activation,
      phone setup/transfer, device activation, signal/service issue, phone in
      SOS mode, voicemail setup, software/technical troubleshooting, device
      repair or replacement, router/equipment exchange.

INCLUDE language patterns such as:
  "told to go to the store" + tech/device context
  "directed me to the store" + SIM / eSIM / activation / signal / fix
  "had to go into the store" + phone / device / technical
  "rep couldn't fix it so I went to the store"
  "store to get my phone out of SOS mode"
  "go to the store to fix my phone"
  "went to the store and they fixed it in two minutes" (implies Care failed first)
  "needed to go in person" + device issue
  "store said to call / store couldn't help either" + device issue
      (this is ALSO a candidate for Sub-Topic 4 if circular)

EXCLUDE:
  - Referrals to the store for billing, payments, account changes, or policy
    reasons (→ Sub-Topic 2)
  - General store visit complaints without a Care referral context
  - Positive-only resolutions at the store with no expressed friction

EXAMPLE VERBATIMS:
  "The problem couldn't be solved without me going into an ATT store, but that
   wasn't his fault. He was very helpful."
  "She could not resolve the issue but directed me to the ATT store."
  "I need to go to AT&T store so they can hopefully get my phone out of SOS mode."
  "Miguel is amazing but I need to go to AT&T store [to fix device issue]."
  "The call rep told me if I go to my local ATT store they would not be able to
   correct the issue. I went to the ATT store after work and they resolved it."

────────────────────────────────────────────────────────────────────────────────
SUB-TOPIC 2: Care-to-Store Referral: Billing, Account & Policy Action
────────────────────────────────────────────────────────────────────────────────
Category   : Process
Topic      : Channel Friction (Care ↔ Store)
Polarity   : Negative
Channel    : Care
Est. Count : 226 (5.3%)
Owner      : Care Channel Operations / Policy Governance

DEFINITION:
A Care rep referred or directed the customer to visit a retail store because the
rep lacked the authority, system access, or policy clearance to complete a
non-technical account or billing action over the phone. Covers billing disputes,
credits/refunds, payment method updates, account name changes, line
cancellations, identity/authentication requirements (including deceased account
holder), trade-in processing, or plan changes that the rep claimed required
in-person handling.

INCLUDE when the verbatim contains explicit evidence of ALL of the following:
  (a) A Care rep redirected the customer to a store (or the customer expresses
      they were required to visit in person), AND
  (b) The reason is a billing, account, or policy matter: billing adjustment,
      credit, refund, charge dispute, autopay/payment card update, account name
      change, line cancellation or suspension, number transfer, account merge or
      unlink, identity verification, proof of ownership, deceased account,
      fraud claim, trade-in submission, return, or promotional credit dispute.

INCLUDE language patterns such as:
  "told to go to the store" + bill / credit / refund / charge / payment
  "had to go to the store" + cancel / account / name / plan
  "directed me to the store to process my trade-in"
  "told me to go to the store to get my refund"
  "go to the store to provide proof [of death / identity]"
  "system wouldn't let her add my bank info so we'll go to the store"
  "she told me to take my watch to the store to cancel / refund"
  "had to go to the store to update my payment method"
  "the rep couldn't do it over the phone, I had to go in person"
  "the agent was not able to verify my information due to an error, I will
   have to go to a store"

EXCLUDE:
  - Device or technical referrals to the store (→ Sub-Topic 1)
  - General complaints about billing errors not accompanied by a store referral
  - Trade-in disputes at the store without a Care-to-store referral

EXAMPLE VERBATIMS:
  "I'm frustrated over the fact that I have to go to an ATT store to provide
   proof that my wife is dead."
  "He told me I should go to the store to request my refund on the WiFi since
   I never used it."
  "System would not let her add my bank info. We will go to our local AT&T store."
  "She told me to take my watch to the Burlington store — store can't find a
   receipt or anything."
  "I needed to change my billing name. Drove 20 miles to an AT&T store at the
   recommendation of an AT&T person on the phone only to be told by the store
   they did not have a button to change this."

────────────────────────────────────────────────────────────────────────────────
SUB-TOPIC 3: Store-to-Care Deflection
────────────────────────────────────────────────────────────────────────────────
Category   : Process
Topic      : Channel Friction (Care ↔ Store)
Polarity   : Negative
Channel    : Care
Est. Count : 220 (5.2%)
Owner      : Retail Operations / Store Workforce Management

DEFINITION:
A retail store employee told or directed the customer to call Care / 611 /
customer service instead of resolving the issue in the store, OR the store
explicitly claimed it lacked the capability, system access, or authority to
handle the customer's request — creating a channel handoff from store to phone.
The customer is now calling Care as a direct result of store deflection. 

INCLUDE when the verbatim contains explicit evidence of:
  - The store told the customer to call, or refused to help, or said it could
    not process / access / handle the customer's issue, OR
  - The store directed the customer to another channel (phone, online, app)
    when the customer expected the store to resolve it.

INCLUDE language patterns such as:
  "store told me to call" / "store said to call 611"
  "store said call customer service" / "store sent me back to the phone"
  "store couldn't help me" / "store said they can't do that"
  "store doesn't have a button for that"
  "the store told me to go online"
  "store couldn't cancel my line / process the return / apply the credit"
  "the rep at the store said they didn't have access to [action]"
  "store said that's a Care issue"
  "store directed me to call the 800 number"
  "walked into store and they had no answers — told me to call"
  "in-store reps are unhelpful; I should not have to go to a store and be
   told to call customer service"

NOTE — polarity nuance: Classify even when the customer gives the Care rep a
positive rating ("Care rep was great"), if the verbatim separately describes
store deflection as the reason for the call.

EXCLUDE:
  - Cases where the store attempted to help but could not, and the Care rep
    ultimately resolved it (positive resolution — no friction signal)
  - Cases where the store appropriately routed a complex issue (e.g., a clearly
    Care-only billing dispute) with no customer frustration expressed

EXAMPLE VERBATIMS:
  "The in-store representatives are unhelpful. I should not have to go to a
   store and be told to call customer service."
  "She went to AT&T store. They told her to call 611."
  "Store told me they couldn't cancel my line — he lied about having to go to
   the store to cancel services."
  "I went to AT&T store and paid the bill. I asked can they merge the billing.
   The person said call 611."
  "I was told I couldn't inquire about getting Direct TV in an AT&T store."
  "Wasn't able to help — just passed my issue off to a store that could still
   not help." [ALSO tag Sub-Topic 4]

────────────────────────────────────────────────────────────────────────────────
SUB-TOPIC 4: Circular Runaround: Neither Channel Resolves
────────────────────────────────────────────────────────────────────────────────
Category   : Process
Topic      : Channel Friction (Care ↔ Store)
Polarity   : Negative
Channel    : Care
Est. Count : 213 (5.0%)
Owner      : Care Channel Operations / Retail Operations (Joint)

DEFINITION:
The customer was bounced between Care and the retail store (in any direction,
any number of times) and the issue remained unresolved by BOTH channels. The
customer explicitly states, implies, or demonstrates through narrative that
neither the phone rep(s) nor the store rep(s) resolved the issue — creating a
closed loop of channel deflection with no ownership. This is the highest-severity
channel friction pattern and a strong churn risk indicator.

INCLUDE when the verbatim contains explicit evidence of:
  - The customer contacted both Care AND a store (or multiple of either), AND
  - The issue was NOT resolved by either channel, OR
  - Language of circular handoff: each channel pointed to the other, or the
    customer was sent back and forth.

INCLUDE language patterns such as:
  "each pointed to the other"
  "store said call Care; Care said go to the store"
  "back and forth" / "runaround" / "going in circles"
  "neither could help" / "both failed" / "no one could resolve it"
  "went to the store and they still couldn't help" (after Care referral)
  "called multiple times AND went to store — still not resolved"
  "prior agent told me go to a store; the store told me go to another store;
   that second store directed me to this call in"
  "the store can't help and Care can't help — I'm stuck"
  "I have been to the store X times and called Y times — no resolution"

SEVERITY NOTE: When this theme is present alongside a satisfaction score of 1
or 2, flag as elevated churn risk.

CO-TAGGING: This theme may co-exist with Sub-Topic 1, 2, or 3 when the initial
referral direction is also clearly identified. Apply all that apply.

EXCLUDE:
  - Single-channel failures only (only store visited, or only phone called)
  - Cases where the issue WAS ultimately resolved after multiple contacts
    (apply Repeat Contact / Multiple Calls to Resolve instead)
  - Frustration with multiple phone calls alone (no store interaction)

EXAMPLE VERBATIMS:
  "Customer service and in-store are horrible. Each pointed to the other to
   attempt to resolve my issue and neither were able to do so."
  "I was told by a prior agent to go to a store. The store told me to go to
   another store. That second store directed me to this call in."
  "Retail and support should be in sync. I've spent hours trying to get a
   mischarge taken care of. I've been to the store 3 times and 3-4 hours on
   the phone. The retail store asked me to come back again today."
  "I have had to make numerous calls to customer service and trips to the
   AT&T store in an attempt to get this issue resolved."
  "She told me I had to go to an ATT store. I am here at the store and they
   can't find a receipt or anything." [after Care referral — both fail]

────────────────────────────────────────────────────────────────────────────────
SUB-TOPIC 5: Conflicting Information: Store vs. Care
────────────────────────────────────────────────────────────────────────────────
Category   : Process
Topic      : Channel Friction (Care ↔ Store)
Polarity   : Negative
Channel    : Care
Est. Count : 192 (4.5%)
Owner      : Training / Knowledge Management / Channel Governance

DEFINITION:
The customer received different, contradictory, or inconsistent information from
the retail store and the Care channel (in any order). The conflicting information
relates to pricing, promotional terms, plan features, eligibility, policy,
what actions are possible, or what was promised — resulting in customer confusion,
financial harm, or eroded trust. This is a systemic knowledge alignment failure
between channels.

INCLUDE when the verbatim contains explicit evidence of:
  - The customer received materially different information from a store
    employee AND a Care rep (or online channel), AND
  - The customer expresses frustration, confusion, or financial impact as a
    result of the contradiction.

INCLUDE language patterns such as:
  "store told me X, phone told me Y"
  "different information from the store vs. customer service"
  "conflicting information" / "inconsistent" / "not in sync"
  "retail and support have completely different information"
  "store said one thing, rep said another"
  "was promised [price/promotion] at the store but Care wouldn't honor it"
  "Care rep couldn't match what the store told me"
  "told something different in store vs. on the phone"
  "store said it would be [price/feature]; now I'm being charged differently"
  "store rep said no problem; Care said can't be done"
  "I spent 3 hours at a store talking to customer service which refused to
   honor the deal I was promised when I signed up"

NOTE — scope: Include cases where the store gave the wrong information AND the
customer is now calling Care to correct it, even if the Care rep cannot resolve
it. The friction is the channel misalignment, not just one side being wrong.

DISTINGUISH FROM:
  - "Rep Lacked Knowledge / Gave Wrong Information": applies when a single Care
    rep gave wrong info with no cross-channel conflict described.
  - "Rep Was Dishonest / Misleading / Deceptive": applies when a single rep
    intentionally misled the customer. Conflicting Information may CO-TAG with
    Dishonest if the store deception is also described.

EXAMPLE VERBATIMS:
  "The ATT retail store and your customer service team seem to have completely
   different information on in-store promotions."
  "Your retail and support should be in sync. I've spent hours trying to get a
   mischarge taken care of."
  "I was told over the phone I had to pay full price for Ultra 3. Went to my
   local ATT store and they got me the watch I wanted with payments."
  "AT&T is billing us for a different service plan than what we signed up for.
   Laura advised I need to go to an AT&T store to resolve because if she
   updated the plan I would lose promotional credits."
  "The solution the rep provided wasn't accurate. When I went to the store,
   they told me the rep had given me wrong information."

================================================================================
TAXONOMY CSV ROW FORMAT (for appending to VOC_Classification_Taxonomy_v3.csv)
================================================================================
The 5 rows below are formatted to match the existing taxonomy column structure:
Category, Category_Definition, Topic, Topic_Definition, Sub_Topic,
Sub_Topic_Definition, Polarity, Survey_Channel, Est_Count, Est_Pct,
Actionable_Owner

--- COPY ROWS BELOW INTO VOC_Classification_Taxonomy_v3.csv ---

Process,"Feedback about operational processes workflows and systemic failures that impact customer experience — including call handling issue resolution routing and channel coordination.",Channel Friction,"Failures that occur when customers are routed between Care and Retail Store — including unjustified referrals deflection circular handoffs and inconsistent information across channels resulting in unresolved issues and repeated customer effort.","Care-to-Store Referral: Tech / Device Issue","A Care rep referred or directed the customer to a retail store because the rep could not resolve a technical or device-related issue remotely. Include: 'told to go to the store' + SIM/eSIM/activation/device context; 'directed me to the store to fix my phone'; 'had to go in person' for signal/service/setup issues; 'problem couldn't be solved without going into a store'; 'she couldn't fix it so sent me to the store'. Classify even when the customer positively rates the rep if the referral created customer effort. Exclude referrals for billing/account/policy reasons (see Care-to-Store: Billing/Account/Policy).",Negative,Care,342,8.1%,Care Channel Operations
Process,"Feedback about operational processes workflows and systemic failures that impact customer experience — including call handling issue resolution routing and channel coordination.",Channel Friction,"Failures that occur when customers are routed between Care and Retail Store — including unjustified referrals deflection circular handoffs and inconsistent information across channels resulting in unresolved issues and repeated customer effort.","Care-to-Store Referral: Billing, Account & Policy Action","A Care rep referred or directed the customer to visit a retail store for a non-technical billing or account action the rep lacked authority or system access to complete. Include: 'told to go to the store' + bill/credit/refund/payment/account context; 'go to the store to update my payment method'; 'had to go in person to provide proof'; 'system wouldn't let her add my bank info — go to store'; 'store to provide proof of death'; 'rep told me to go in person to process trade-in/return'. Covers: billing disputes credits refunds autopay/card updates account name changes line cancellations number transfers identity/authentication requirements deceased account fraud claims trade-in and return processing. Exclude device/tech referrals (see Care-to-Store: Tech/Device).",Negative,Care,226,5.3%,Care Channel Operations
Process,"Feedback about operational processes workflows and systemic failures that impact customer experience — including call handling issue resolution routing and channel coordination.",Channel Friction,"Failures that occur when customers are routed between Care and Retail Store — including unjustified referrals deflection circular handoffs and inconsistent information across channels resulting in unresolved issues and repeated customer effort.",Store-to-Care Deflection,"A retail store employee directed or referred the customer to call Care/611/customer service instead of resolving the issue in store OR the store explicitly claimed it lacked capability system access or authority to handle the request. Include: 'store told me to call'; 'store said call 611'; 'store said they can't do that'; 'store doesn't have a button for that'; 'store said to go online'; 'store said that's a Care issue'; 'I should not have to go to a store and be told to call customer service'. Apply even when Care rep is rated positively if store deflection is described as the reason for the call. Exclude appropriate Care routing with no customer frustration expressed.",Negative,Care,220,5.2%,Retail Operations
Process,"Feedback about operational processes workflows and systemic failures that impact customer experience — including call handling issue resolution routing and channel coordination.",Channel Friction,"Failures that occur when customers are routed between Care and Retail Store — including unjustified referrals deflection circular handoffs and inconsistent information across channels resulting in unresolved issues and repeated customer effort.",Circular Runaround: Neither Channel Resolves,"The customer was bounced between Care and the retail store in any direction any number of times and the issue remained unresolved by BOTH channels. Each channel pointed to the other or the customer made multiple contacts across channels with no resolution. Include: 'each pointed to the other'; 'back and forth'; 'runaround'; 'neither could help'; 'both failed'; 'went to store X times and called Y times — still not resolved'; 'store told me go to another store — that store directed me to call in'. Highest-severity channel friction signal — strong churn risk. May co-tag with Sub-Topics 1 2 or 3 when initial direction is clear. Exclude: issue resolved after multiple contacts (apply Repeat Contact theme instead).",Negative,Care,213,5.0%,Care Channel Operations / Retail Operations
Process,"Feedback about operational processes workflows and systemic failures that impact customer experience — including call handling issue resolution routing and channel coordination.",Channel Friction,"Failures that occur when customers are routed between Care and Retail Store — including unjustified referrals deflection circular handoffs and inconsistent information across channels resulting in unresolved issues and repeated customer effort.",Conflicting Information: Store vs. Care,"Customer received materially different or contradictory information from the retail store and Care (in any order) regarding pricing promotions plan terms eligibility policy or what actions are possible — resulting in customer confusion financial harm or eroded trust. Include: 'store told me X phone told me Y'; 'conflicting information'; 'retail and support have completely different information'; 'was promised [promotion] at store but Care won't honor it'; 'told something different in store vs. on the phone'; 'store said no problem; Care said can't be done'. Distinct from Rep Lacked Knowledge (single-rep error) — requires explicit cross-channel contradiction. May co-tag with Rep Was Dishonest if store deception is separately described.",Negative,Care,192,4.5%,Training / Knowledge Management

================================================================================
END OF FILE
================================================================================
