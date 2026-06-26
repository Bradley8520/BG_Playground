# VOC Classification Taxonomy v4 — Revised Prompts Integration Handoff

## Status: 🔄 IN PROGRESS — 12 of 24 Revised Prompts Applied
**Last Updated:** 2026-06-20
**Active File:** `VOC_Classification_Taxonomy_v4.csv`
**Total Sub-Topics (current):** 249
**Source of Revised Prompts:** `VOC Verbatim Taxonomy (original 24).csv`

---

## CONTEXT

The v4 taxonomy is an in-place refinement of v3. The work involves:
1. **Applying revised prompt definitions** from the "original 24" CSV — replacing or updating `Sub_Topic_Definition` values with more precisely engineered LLM classification prompts
2. **Structural changes** — topic/sub-topic moves, renames, additions, and deletions driven by classification accuracy needs
3. **Gap analysis** for each revised prompt — compare existing definition vs. revised prompt, identify added patterns and exclusion rules, apply with modifications

---

## CURRENT TAXONOMY STATS

| Category | Sub-Topics |
|---|---|
| People | 77 |
| Process | 66 |
| Pricing | 30 |
| Product | 30 |
| Policy | 22 |
| Platform | 17 |
| Survey Artifact | 7 |
| **Total** | **249** |

---

## WHAT WAS ACCOMPLISHED (This Work Stream)

### Structural Changes Applied

| Change | Type | Detail |
|---|---|---|
| Rep Was Thorough / Detailed | **Moved** | Topic changed from Rep Courtesy → Rep Helpfulness |
| Rep Made an Account or Setup Error | **Added** | New sub-topic under Rep Knowledge & Accuracy (Negative, All channels) — 3 dispute patterns: billing errors, unauthorized charges, phantom service charges |
| No Comment / Nothing Entered | **Removed** | Eliminated from Survey Artifact |
| Single Word Non-Actionable | **Removed** | Eliminated from Survey Artifact |
| Perfect Score Affirmation / No Issue | **Removed** | Eliminated from Survey Artifact |
| Score Explanation / Meant Different Rating | **Removed** | Eliminated from Survey Artifact |
| No Feedback (sub-topic) | **Added** | New comprehensive definition under No Feedback topic — 4 patterns: non-semantic text, explicit opt-outs, single word sentiment, conversational filler |
| Score Error Correction | **Added (topic + sub-topic)** | New topic AND sub-topic (same name) replacing the two removed sub-topics above |
| Survey Experience Complaint (topic) | **Renamed** | → Survey Feedback |
| Survey Too Long / Poorly Designed (sub-topic) | **Renamed** | → Survey Feedback; definition expanded to include frequency complaints; CO-CLASSIFY rule added for mixed verbatims |
| Stop Sending Surveys / Too Many Surveys (sub-topic) | **Renamed** | → Stop Survey / Opt-Out Request (pure opt-outs only; frequency/design → Survey Feedback) |
| No Feedback / Blank Response (topic) | **Renamed** | → No Feedback (matches sub-topic name; consistent with Score Error Correction and Stop Survey / Opt-Out Request pattern) |

### Survey Artifact — Final Structure

| Topic | Sub-Topic |
|---|---|
| Foreign Language Response | Non-English Response / Requires Translation |
| No Feedback | No Feedback |
| Score Error Correction | Score Error Correction |
| Stop Survey / Opt-Out Request | Stop Survey / Opt-Out Request |
| Survey Feedback | Survey Feedback |
| Unintelligible / Gibberish | Random Characters / Keyboard Input |
| Wrong Customer / Wrong Interaction | Wrong Person / Did Not Call |

---

## REVISED PROMPTS STATUS

### Completed (12 of 24)

| # | Original 24 Theme | Maps To (Sub-Topic) | Topic | Category | Status |
|---|---|---|---|---|---|
| 1 | Rep Was Courteous | Rep Was Courteous / Friendly / Professional | Rep Courtesy | People | ✅ Applied |
| 2 | Rep Not Courteous | Rep Was Rude / Dismissive / Unprofessional | Rep Courtesy | People | ✅ Applied |
| 3 | Rep Was Helpful | Rep Was Helpful / Resolved My Issue | Rep Helpfulness | People | ✅ Applied |
| 4 | Rep Not Helpful | Rep Was Unhelpful / Did Not Resolve My Issue | Rep Helpfulness | People | ✅ Applied |
| 5 | Rep Was Knowledgeable | Rep Was Knowledgeable / Gave Correct Info | Rep Knowledge & Accuracy | People | ✅ Applied |
| 6 | Rep Not Knowledgeable | Rep Was Unknowledgeable / Gave Wrong Info | Rep Knowledge & Accuracy | People | ✅ Applied |
| 7 | Bill Increase | Bill Increased / Price Went Up Unexpectedly | Billing Errors & Disputes | Pricing | ✅ Applied + EXCLUDEs added |
| 8 | Bill Too High | Bill Is Too High / Too Expensive | Billing Errors & Disputes | Pricing | ✅ Applied + routing distinction |
| 9 | Bill Dispute | Billing Error / Incorrect Charge / Overcharge | Billing Errors & Disputes | Pricing | ✅ Applied + 3-pattern structure |
| 10 | No Feedback | No Feedback | No Feedback | Survey Artifact | ✅ Applied (new sub-topic) |
| 11 | Error Correction | Score Error Correction | Score Error Correction | Survey Artifact | ✅ Applied (new topic + sub-topic) |
| 12 | Stop | Stop Survey / Opt-Out Request | Stop Survey / Opt-Out Request | Survey Artifact | ✅ Applied + renamed |

### Remaining (12 of 24)

| # | Original 24 Theme | Maps To (Sub-Topic) | Topic | Category | Notes |
|---|---|---|---|---|---|
| 13 | Wrong Customer | Wrong Person / Did Not Call | Wrong Customer / Wrong Interaction | Survey Artifact | Straightforward replacement |
| 14 | Call Disconnects | Rep Hung Up / Ended Call Prematurely | Rep Courtesy | People | Straightforward replacement |
| 15 | Callbacks Never Received | Rep Did Not Follow Through / Broken Promise | Rep Accountability & Follow-Through | People | Straightforward replacement |
| 16 | Transfers / Multiple Reps | *(multiple sub-topics)* | Transfers & Routing | Process | May span multiple sub-topics |
| 17 | Long Wait for Rep | Long Wait for Rep | Wait Time & Speed of Service | Process | Consolidation decision likely — see note below |
| 18 | Long Hold Time | Long / Multiple Holds | Wait Time & Speed of Service | Process | Consolidation decision likely |
| 19 | Multiple Holds | Long / Multiple Holds | Wait Time & Speed of Service | Process | Consolidation decision likely |
| 20 | Wait / Hold Time | *(overall topic)* | Wait Time & Speed of Service | Process | Consolidation decision likely |
| 21 | Missed Field Tech Appointment | *(technician no-show)* | Technician Visit Timeliness | Process | Straightforward replacement |
| 22 | Seeking Credits | Refund / Credit Request | Billing Errors & Disputes | Pricing | Straightforward replacement |
| 23 | Need to Lower Bill | Request to Lower Bill / Reduce Cost | Billing Errors & Disputes | Pricing | Straightforward replacement |
| 24 | Wireless Coverage | *(coverage sub-topics)* | Coverage & Signal | Product | May span multiple sub-topics |

> **Wait/Hold Time Note:** Themes 17–20 all map into the same topic (Wait Time & Speed of Service). These should be pulled and compared together — a consolidation decision is likely needed (similar to how Rep Courtesy handled multiple themes into one topic). Pull all 4 revised prompts simultaneously and compare against current sub-topics: Long Wait for Rep, Long/Multiple Holds, Overall Interaction Took Too Long, Service Was Fast/Quick/Efficient.

---

## KEY DESIGN DECISIONS (This Work Stream)

1. **Revised prompt format:** Original 24 CSV has `Initial Prompt` and `Revised Prompt` columns. Both start with "ThemeName -> definition" — strip prefix with `-replace '^ThemeName\s*->\s*',''`. Arrow artifacts ("?") must be fixed with `-replace '\?','→'`.

2. **Bill Increase EXCLUDEs:** Added two routing rules to prevent overlap:
   - EXCLUDE: affordability complaints without an unexpected change → routes to Bill Too High
   - EXCLUDE: promo expiration mentions → routes to Promotion Expired

3. **Bill Too High routing distinction:** Overcharged (wrongness assertion — "they charged me wrong") routes to Billing Error; Overpriced (value judgment — "too expensive for what I get") stays in Bill Too High. Spanish equivalents included ("cobran demasiado", "muy caro").

4. **Billing Error 3-pattern structure:** (a) billing errors — statement discrepancies, (b) unauthorized charges — services not requested, (c) phantom service charges — charges for services customer denies receiving. All require a wrongness assertion gate.

5. **Survey Artifact naming consistency:** Topic name = Sub-topic name pattern was adopted for: Score Error Correction, Stop Survey / Opt-Out Request, No Feedback. This mirrors how single-sub-topic topics should be named.

6. **Multi-label vs. mutual exclusivity:** Sub-topics WITHIN the same topic should be mutually exclusive. Cross-topic co-classification is expected and desired. Survey Feedback + Stop Survey / Opt-Out Request can both fire on "Stop, I receive too many surveys" because they are different topics.

7. **Rep Was Thorough / Detailed placement:** Moved from Rep Courtesy to Rep Helpfulness because thoroughness is an outcome of effort/helpfulness, not tone/demeanor (which is what Rep Courtesy measures).

---

## TECHNICAL NOTES

- **PowerShell encoding:** All CSV writes use `[System.IO.File]::WriteAllLines` with `New-Object System.Text.UTF8Encoding $false` (UTF-8 no BOM)
- **Dollar sign escaping:** Definition strings containing `$X` must use backtick escape (`` `$X ``) in double-quoted PowerShell strings to prevent variable expansion
- **Sort order:** After every change, rows are sorted Category → Topic → Sub-Topic A-Z
- **Verification pattern:** After each change, confirm total row count (should be 249) and spot-check the affected sub-topic with `Format-List`

---

## NEXT SESSION — PICK UP HERE

**Recommended order:**

1. **Wrong Customer (Theme 13)** — Pull revised prompt from original 24 CSV:
   ```powershell
   $orig = Import-Csv "c:\Users\bg763c\OneDrive - AT&T Services, Inc\Documents\VS Code\Git Test\VOC Verbatim Taxonomy (original 24).csv"
   $orig | Where-Object { $_.'Initial Prompt' -like '*Wrong Customer*' } | Select-Object 'Initial Prompt','Revised Prompt' | Format-List
   ```
   Compare against current definition for `Wrong Person / Did Not Call` under `Wrong Customer / Wrong Interaction` in v4. Apply revised prompt.

2. **Call Disconnects (Theme 14)** — Same pattern. Maps to `Rep Hung Up / Ended Call Prematurely` under `Rep Courtesy`.

3. **Callbacks Never Received (Theme 15)** — Maps to `Rep Did Not Follow Through / Broken Promise` under `Rep Accountability & Follow-Through`.

4. **Wait/Hold Time (Themes 17–20) — Pull all 4 together:**
   ```powershell
   $orig | Where-Object { $_.'Initial Prompt' -match 'Wait|Hold' } | Select-Object 'Initial Prompt','Revised Prompt' | Format-List
   ```
   Also pull current Wait Time & Speed of Service sub-topics from v4 for side-by-side comparison. Make consolidation decision before applying.

5. **Transfers / Multiple Reps (Theme 16)** — Pull revised prompt, compare against Transfers & Routing sub-topics in v4.

6. **Missed Field Tech Appointment (Theme 21)** — Maps to Technician Visit Timeliness sub-topics.

7. **Seeking Credits (Theme 22)** + **Need to Lower Bill (Theme 23)** — Both Pricing; pull together.

8. **Wireless Coverage (Theme 24)** — Pull revised prompt, compare against Coverage & Signal sub-topics in v4.

---

## FILES REFERENCE

| File | Purpose |
|---|---|
| `VOC_Classification_Taxonomy_v4.csv` | **Active taxonomy — all changes applied here** |
| `VOC Verbatim Taxonomy (original 24).csv` | Source of revised prompt definitions — read-only reference |
| `Care_Verbatims_Apr2026_classification_testing.csv` | 97,002 real verbatims for testing/validation |
