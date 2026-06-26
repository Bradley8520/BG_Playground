Taxonomy Revision Changes - VOC_Classification_Taxonomy_v4.csv
Date: 2026-06-17
Source Request: Taxonomy Revision Handoff Document - Current Model Gaps.txt

Summary
- Base file: VOC_Classification_Taxonomy_v3.csv (copied earlier to v4)
- Updated file: VOC_Classification_Taxonomy_v4.csv
- Row count changed from 201 to 240 (+39 net)
- Scope implemented: All 15 themes
- Confirmed implementation preferences used:
  - Shop & Purchase placed under Category=Process, Topic=Shop & Purchase
  - Shop & Purchase Polarity set to Mixed
  - Perceived Trust move removes People rows and re-adds in Process
  - Password/Passcode implemented as one combined sub-topic
  - Bill Inquiry and General Bill retained as catch-alls
  - Switching to competitor kept as Xfinity + Spectrum + Other ISP

Detailed Changes by Theme

1) Password/Passcode
- Updated existing row:
  - Category: Platform
  - Topic: Account Access & Login
  - Sub_Topic renamed from "Password Reset / Verification Too Difficult" to "Password/Passcode Reset"
  - Sub_Topic_Definition expanded to include password reset, passcode verification, and MFA recovery context

2) Privacy
- Added new row:
  - Category: Policy
  - Topic: Data Privacy & Security
  - Sub_Topic: Data Privacy/Security
  - Polarity: Negative
  - Survey_Channel: All

3) AT&T Phone (Home Phone)
- Added new row:
  - Category: Product
  - Topic: Home Phone Service
  - Sub_Topic: Home Phone
  - Definition includes landline (POTS), VoIP, and AT&T Phone - Advanced
  - Polarity: Mixed
  - Survey_Channel: All

4) Bill Inquiry and General Bill
- Added two catch-all rows:
  - Category: Pricing
  - Topic: Bill Inquiry & General Bill
  - Sub_Topics: Bill Inquiry, General Bill
  - Polarity: Neutral
  - Survey_Channel: All

5) Discounts (Promotions & Discounts)
- Added five rows under existing topic Promotions & Discounts:
  - Signature Savings Program
  - Appreciation Savings Program
  - Access by AT&T (Low-Cost Internet)
  - Wireless + Fiber Bundle Discount
  - 55+ Wireless + Internet Bundle Discount
- Polarity for all added rows: Mixed
- Survey_Channel: All

6) Call Audio Issues
- Added new topic and two rows:
  - Category: Process
  - Topic: Call Center Environment & Atmosphere
  - Sub_Topics:
    - Difficulty Hearing Rep (Headset/Audio)
    - Loud Background Noise in Call Center
  - Polarity: Negative
  - Survey_Channel: Care

7) Perceived Trust - Wrong Information
- Removed two rows from People > Rep Knowledge & Accuracy:
  - Rep Was Dishonest / Misleading / Deceptive
  - Inconsistent Information Across Reps
- Added three rows under Process:
  - Topic: Perceived Trust - Wrong Information
  - Sub_Topics:
    - Perceived Trust
    - Inconsistent Information
    - Wrong Information
  - Polarity: Negative
  - Survey_Channel: All

8) System Outage / In-Store Technology & Systems
- Renamed topic:
  - From: In-Store Technology & Systems
  - To: Technology & Systems Reliability
- Updated existing sub-topics for channel-neutral usage:
  - Store Systems Were Slow / Caused Delays -> System Slow/Outage Caused Delays
  - Transaction Was Smooth / System Worked Well retained but made channel-neutral
- Updated Survey_Channel for both existing rows to All
- Added retail-specific rows:
  - Store WiFi Issue
  - Pay Kiosk Issue
  - Survey_Channel: Retail | National Retail

9) Wait, Holds, & Speed of Service
- Replaced existing Wait Time & Speed of Service sub-topic set with 4 rows:
  - Long Wait for Rep
  - Long/Multiple Holds
  - Service Was Fast/Quick/Efficient
  - Overall Interaction Took Too Long
- Channels set per intent (Care for wait/hold specific, All for overall speed)

10) Rep Communication
- Renamed topic:
  - From: Rep Communication Clarity
  - To: Rep Communication
- Updated sub-topics to requested 5-sub-topic structure:
  - Language Barrier or Comprehension Issue
  - Request for Different Communication Support
  - Rep Communicated Clearly & Effectively
  - Unclear, Incomplete, or Confusing Communication
  - Poor Listening or Interruptive Behavior (added)

11) Cancellation & Switching Intent
- Removed old combined row:
  - Switching to Competitor - Xfinity / Spectrum / Other ISP
- Added three rows:
  - Switching to Competitor - Xfinity
  - Switching to Competitor - Spectrum
  - Switching to Competitor - Other ISP

12) Device & Equipment
- Added four rows under Product > Device & Equipment:
  - Modem-Router
  - Residential Gateway
  - WiFi Extender
  - Setup/Activate Equipment
- Polarity: Mixed
- Survey_Channel: All

13) General Customer Service
- Added new topic and two rows:
  - Category: Process
  - Topic: General Customer Service
  - Sub_Topics:
    - Positive General Customer Service
    - Negative General Customer Service

14) Retail Store (Cross-Channel Friction)
- Added new topic and five rows:
  - Category: Process
  - Topic: Cross-Channel Friction
  - Sub_Topics:
    - Care-to-Store Referral: Tech / Device Issue
    - Care-to-Store Referral: Billing, Account & Policy
    - Store-to-Care Deflection
    - Circular Runaround: Neither Channel Resolves
    - Conflicting Information: Store vs. Care
  - Survey_Channel: Care | Retail | National Retail

15) Shop & Purchase
- Added topic under Process with 11 sub-topics from workspace-approved structure:
  - New Account
  - Activation & Porting
  - Add a Line
  - Upgrade
  - Trade-In
  - Fulfillment - Order
  - Fulfillment - Delivery
  - Returns
  - Exchange & Replace
  - Warranty & Device Protection Exchange
  - Unauthorized Account Changes
- Category: Process
- Topic: Shop & Purchase
- Polarity: Mixed
- Survey_Channel: Care

Post-Update Validation Checks Performed
- Verified all requested new topics/sub-topics exist in v4
- Verified removal/replacement actions completed:
  - People dishonest/inconsistent rows removed
  - Old In-Store Technology & Systems topic removed (renamed replacement exists)
  - Old combined Xfinity/Spectrum/Other row removed

Notes
- Definitions were written to match VOC_Classification_Taxonomy CSV style and column format.
- Est_Count, Est_Pct, and some Actionable_Owner values are set to TBD for net-new rows pending model validation and volume calibration.
