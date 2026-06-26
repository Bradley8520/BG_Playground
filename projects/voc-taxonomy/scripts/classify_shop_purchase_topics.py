"""
Shop & Purchase Sub-Topic Classification - 11 Topics
Runs keyword-based multi-label classification for 11 Shop & Purchase
topic areas against the full Care verbatim sample (97k rows).

Each row can match multiple topics (multi-label).
For each topic: Total | Negative | Positive | % of 97k total.
Polarity detected via sentiment overlay on top of topic match.

Output: console summary + CSV.
"""

import pandas as pd
import time

INPUT_FILE   = r"C:\Users\bg763c\OneDrive - AT&T Services, Inc\Documents\VS Code\Git Test\Care_Verbatims_Apr2026_classification_testing.csv"
OUTPUT_FILE  = r"C:\Users\bg763c\OneDrive - AT&T Services, Inc\Documents\VS Code\Git Test\Shop_Purchase_Topic_Volume_Results_v3.csv"
VERBATIM_COL = "VERBATIM_RESPONSE"

# ── Sentiment signal patterns (applied on top of topic match) ─────────────────
# Positive: customer clearly expressing satisfaction / success
POS_PATTERN = (
    r"\b(easy|easily|quick|quickly|fast|smooth|seamless|great|excellent|wonderful|"
    r"perfect|fantastic|outstanding|amazing|awesome|helpful|very helpful|extremely helpful|"
    r"love|loved|happy|satisfied|pleased|impressed|appreciate|appreciated|thank|thanks|"
    r"no problem|no issue|no hassle|no complaints|resolved quickly|handled well|"
    r"best|top notch|five star|10 out of 10|10/10|above and beyond|went above|"
    r"couldn.t ask for better|couldn.t be happier|made it easy|so easy|very easy|"
    r"very fast|very quick|right away|immediately|on time|as expected|worked perfectly)\b"
)

# Negative: customer expressing frustration, failure, or unresolved issue
NEG_PATTERN = (
    r"\b(problem|problems|issue|issues|error|errors|failed|failure|wrong|incorrect|"
    r"missing|never|didn.t|don.t|can.t|cannot|couldn.t|won.t|wouldn.t|hasn.t|haven.t|"
    r"not received|not applied|not working|not fixed|not resolved|not done|"
    r"still waiting|still not|still being|still owe|still charged|still have|"
    r"frustrated|frustrating|upset|angry|disappointed|terrible|horrible|awful|"
    r"nightmare|ridiculous|unacceptable|disgusting|pathetic|waste|wasted|"
    r"lie|lied|lying|mislead|misled|deceived|false|misinformation|wrong information|"
    r"no one|nobody|no help|no resolution|no answer|no response|no callback|"
    r"cancel|cancelling|canceling|leaving|switching|quit|done with|fed up|"
    r"hours|multiple times|third time|fourth time|fifth time|again and again|"
    r"charged incorrectly|overcharged|unauthorized|without my permission|without asking)\b"
)

# ── Topic definitions: (Topic_Name, pattern) ──────────────────────────────────
# Patterns are intentionally broad to capture the topic concept across all phrasings.
# Multi-label: a row contributes to every topic it matches.

TOPICS = [

    ("New Account",
     r"\b(new account|open.{0,10}account|opening.{0,10}account|new customer|new service|"
     r"just (signed up|joined|switched|started|got service)|brand new (customer|account|service)|"
     r"first (bill|month|time customer)|sign.?up|signed.?up|"
     r"new to AT.?T|recently (joined|switched|signed|started)|joining AT.?T)\b"),

    ("Activation & Porting",
     r"\b(SIM card|eSIM|e.SIM|IMEI|activat|re.activat|"
     r"port.in|port in|porting|number (transfer|port|porting|transferred|switch)|"
     r"transfer.{0,20}(number|my number)|switch.{0,20}(number|my number)|"
     r"number.{0,20}(transfer|port|switch))\b"),

    ("Add a Line",
     r"\b(add.{0,10}(a )?line|adding.{0,10}(a )?line|added.{0,10}(a )?line|"
     r"add.{0,10}(a )?number|additional line|extra line|second line|third line|"
     r"another line|new line (for|to|on)|add.{0,10}phone (to|for)|"
     r"adding (a )?phone (to|for)|added (a )?phone (to|for))\b"),

    ("Upgrade",
     r"\b(upgrad|upgrading|upgraded|upgrade.{0,5}(my|the|a)|"
     r"next up anytime|next up program|installment (plan|upgrade)|"
     r"AT.?T (next|upgrade)|upgrade fee|activation fee|"
     r"\$35|35.dollar.{0,15}fee|upgrade.{0,20}(phone|device|watch|tablet)|"
     r"want.{0,15}(new|a new) (phone|device|iphone|samsung|android|tablet|watch)|"
     r"(looking|hoping|trying|want).{0,20}(get|buy|purchase).{0,20}(new|a new) (phone|device)|"
     r"new phone (deal|offer|option|price|cost)|"
     r"(get|buy|purchase).{0,20}(iphone|samsung|pixel|motorola|galaxy|oneplus|android phone))\b"),

    ("Trade-In",
     r"\b(trade.in|trade in|trading in|traded in|trade.?ins|"
     r"trade.{0,5}(my|the|a).{0,20}(phone|device|old phone|iphone|samsung)|"
     r"(send|sent|sending|return|returned|returning).{0,30}(trade.in|old (phone|device)))\b"),

    ("Fulfillment - Order",
     r"\b(order.{0,5}(cancel|cancelled|cancellation|cancelled without|was cancelled|got cancelled)|"
     r"cancel.{0,20}(order|my order)|"
     r"(placed|place|placing).{0,20}order|order.{0,20}(placed|processing|processed|confirmed|confirmation)|"
     r"wrong (phone|device|item|product|model|color|modem|router|equipment|size|storage) (sent|shipped|received|delivered|arrived)|"
     r"(sent|shipped|received|delivered).{0,20}wrong (phone|device|item|model|color|modem|router|equipment)|"
     r"payment.{0,30}(fail|failed|declined|error|didn.t go through|processing|charged|issue)|"
     r"duplicate (charge|payment|billing)|charged (twice|double|two times)|"
     r"order.{0,30}(status|tracking|confirmation|number|not.{0,10}received|missing)|"
     r"not.{0,10}what.{0,10}(I ordered|was ordered|was promised))\b"),

    ("Fulfillment - Delivery",
     r"\b(deliver|delivered|delivery|deliveries|"
     r"(ship|ships|shipped|shipping|shipment)|"
     r"(package|parcel|box).{0,30}(sent|arrived|delivered|missing|lost|received|didn.t arrive)|"
     r"(UPS|FedEx|USPS|carrier).{0,50}(deliver|package|tracking|shipment)|"
     r"tracking (number|info|status|update)|"
     r"(next.day|overnight|same.day|2.day|two.day).{0,20}(shipping|delivery)|"
     r"(lost|missing).{0,20}(in transit|package|shipment|delivery)|"
     r"signature (required|needed|on delivery))\b"),

    ("Returns",
     r"\b(return|returning|returned|returns|"
     r"return (label|kit|instructions|policy|window|period|process)|"
     r"(30|thirty).day (return|window|period|policy)|"
     r"return (my|the|a).{0,20}(phone|device|modem|router|equipment|item)|"
     r"(send|sent|sending|mail|mailed|mailing|ship|shipped|shipping).{0,20}(it back|back|return)|"
     r"refund|money back|credit (for|on).{0,20}(return|returned))\b"),

    ("Exchange & Replace",
     r"\b(exchang|replacing|replacement|replace|swap|swapping|"
     r"(wrong|incorrect|defective|damaged|broken|faulty|DOA|dead on arrival).{0,30}(phone|device|item|modem|router|equipment)|"
     r"(phone|device|modem|router|equipment).{0,30}(wrong|incorrect|defective|damaged|broken|faulty|cracked|not working|doesn.t work)|"
     r"arrived.{0,30}(broken|damaged|defective|cracked|wrong|not working)|"
     r"refurbished|refurb|used (phone|device).{0,20}(instead of new|not new|paid for new))\b"),

    ("Warranty & Device Protection",
     r"\b(warranty|manufacturer warranty|manufacturer.s warranty|"
     r"(protection plan|device protection|mobile protect|ProTech|NEXT UP|insurance).{0,30}(claim|add|added|charge|charged|enrolled|enroll|signed up|coverage|cancel|issue|problem)|"
     r"insurance (claim|coverage|deductible)|"
     r"(file|filed|filing).{0,20}(claim|insurance claim)|"
     r"deductible|"
     r"protection plan.{0,50}(without|permission|consent|didn.t|never|unauthorized))\b"),

    ("Unauthorized Account Changes",
     r"\b(without (my )?(permission|consent|authorization|knowledge|asking)|"
     r"(added|charged|changed|switched|activated|enrolled).{0,30}(without|unauthorized)|"
     r"unauthorized (charge|line|account|change|addition|service|feature|plan)|"
     r"didn.t (authorize|agree to|consent to|ask for|request|want|approve).{0,40}(line|charge|plan|service|feature|protection|insurance|ProTech)|"
     r"never (agreed to|authorized|asked for|requested|approved).{0,40}(line|charge|plan|service|feature|protection|insurance)|"
     r"(line|service|feature|plan|insurance|ProTech|protection).{0,50}added without)\b"),

]

# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    t0 = time.time()
    print("Loading file...")
    df = pd.read_csv(INPUT_FILE, low_memory=False, encoding="utf-8", on_bad_lines="skip")
    total = len(df)
    print(f"  Loaded {total:,} rows in {time.time()-t0:.1f}s\n")

    v = df[VERBATIM_COL].fillna("").astype(str)

    # Pre-compute sentiment masks once (reused for every topic)
    print("Computing sentiment masks...")
    pos_mask = v.str.contains(POS_PATTERN, case=False, regex=True, na=False)
    neg_mask = v.str.contains(NEG_PATTERN, case=False, regex=True, na=False)
    print(f"  Positive signal rows: {pos_mask.sum():,}  ({pos_mask.sum()/total*100:.1f}%)")
    print(f"  Negative signal rows: {neg_mask.sum():,}  ({neg_mask.sum()/total*100:.1f}%)")

    print()

    results = []
    print(f"Running {len(TOPICS)} topic patterns...")
    print(f"{'#':<3} {'Topic':<35} {'Total':>8} {'%Tot':>6}  {'Neg':>8} {'%Neg':>6}  {'Pos':>8} {'%Pos':>6}")
    print("-" * 90)

    for i, (topic, pattern) in enumerate(TOPICS, 1):
        topic_mask = v.str.contains(pattern, case=False, regex=True, na=False)
        total_count = int(topic_mask.sum())
        neg_count   = int((topic_mask & neg_mask).sum())
        pos_count   = int((topic_mask & pos_mask).sum())
        pct_total   = total_count / total * 100
        pct_neg     = neg_count   / total * 100
        pct_pos     = pos_count   / total * 100

        results.append({
            "Topic":          topic,
            "Total_Count":    total_count,
            "Pct_of_Total":   round(pct_total, 3),
            "Negative_Count": neg_count,
            "Pct_Neg":        round(pct_neg, 3),
            "Positive_Count": pos_count,
            "Pct_Pos":        round(pct_pos, 3),
        })

        print(f"{i:<3} {topic:<35} {total_count:>8,} {pct_total:>5.2f}%  "
              f"{neg_count:>8,} {pct_neg:>5.2f}%  {pos_count:>8,} {pct_pos:>5.2f}%")

    out = pd.DataFrame(results)
    out.to_csv(OUTPUT_FILE, index=False)

    print(f"\nTotal rows in file: {total:,}")
    print(f"Results saved to:   {OUTPUT_FILE}")
    print(f"Completed in {time.time()-t0:.1f}s")

if __name__ == "__main__":
    main()
