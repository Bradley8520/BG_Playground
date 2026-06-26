"""
Shop & Purchase Sub-Topic Classification — 14 Broad Topics
Runs keyword-based classification for 14 Shop & Purchase topic areas
against the Care verbatim sample (97k rows).

For each topic:
  - Total matches (multi-label: a row can match multiple topics)
  - Negative matches (topic + negative sentiment signal)
  - Positive matches (topic + positive sentiment signal)
  - % of all 97,002 rows

Output: console summary + CSV.
"""

import pandas as pd
import re
import time

# ── Config ────────────────────────────────────────────────────────────────────
INPUT_FILE   = r"C:\Users\bg763c\OneDrive - AT&T Services, Inc\Documents\VS Code\Git Test\Care_Verbatims_Apr2026_classification_testing.csv"
OUTPUT_FILE  = r"C:\Users\bg763c\OneDrive - AT&T Services, Inc\Documents\VS Code\Git Test\Shop_Purchase_Topic_Volume_Results.csv"
VERBATIM_COL = "VERBATIM_RESPONSE"

# ── Sub-topic definitions ──────────────────────────────────────────────────────
# Format: (Topic, Sub-Topic, Polarity, regex_pattern)
SUBTOPICS = [

    # ── NEW ACCOUNT ────────────────────────────────────────────────────────────
    ("New Account", "Account Setup Error", "Negative",
        r"wrong.{0,25}(address|email|account)|account.{0,25}(incorrect|set.?up wrong|created incorrectly)|setup error|account information.{0,20}wrong"),

    ("New Account", "New Service Not Activating", "Negative",
        r"(service|account).{0,35}(not activating|won.t activate|can.t activate|not working after setup|not live)|"
        r"equipment.{0,30}(arrived|received).{0,40}(no service|can.t connect|not working)"),

    ("New Account", "Port-In Stalled or Failed", "Negative",
        r"port.{0,20}(failed|stalled|didn.t go through|incomplete|not completed|issue|problem|error)|"
        r"number.{0,35}(didn.t transfer|not transferred|still with old carrier|transfer failed)|"
        r"porting.{0,50}(failed|issue|problem|error|delay|not working|didn.t work|hasn.t)"),

    ("New Account", "SIM or Equipment Not Received", "Negative",
        r"(SIM|modem|router|equipment|gateway).{0,35}(never arrived|not received|never got|not delivered|still waiting|hasn.t arrived)"),

    ("New Account", "New Account Opened Successfully", "Positive",
        r"(new account|new service|set up|setup).{0,60}(easy|smooth|great|perfect|quick|worked|working|no problem|no issue)"),

    # ── ACTIVATION & PORTING ───────────────────────────────────────────────────
    ("Activation & Porting", "SIM or eSIM Activation Failed", "Negative",
        r"(SIM|eSIM).{0,35}(won.t activate|not activate|activation failed|not working|not recognized|no service after|can.t activate|failed to activate)"),

    ("Activation & Porting", "IMEI or Device Not Recognized", "Negative",
        r"IMEI.{0,35}(not recognized|invalid|rejected|not compatible|doesn.t work)|"
        r"device.{0,30}(not recognized|rejected|not compatible).{0,30}account"),

    ("Activation & Porting", "Number Port-In Incomplete", "Negative",
        r"(port.in|port in|porting|number transfer).{0,60}(incomplete|failed|not completed|still pending|delayed|hasn.t gone through|taking.{0,15}(days|weeks))"),

    ("Activation & Porting", "Activation or Port Completed", "Positive",
        r"(activated|activation|ported|port.in).{0,60}(right away|quickly|easy|smooth|without issue|immediately|fast|worked|no problem)"),

    # ── ADD A LINE ─────────────────────────────────────────────────────────────
    ("Add a Line", "Add a Line - Extended Time or Multiple Contacts", "Negative",
        r"(add.{0,10}line|adding.{0,10}line|added.{0,10}line).{0,100}(hours|multiple|called back|transferred|calls|long time|took too long|still not|couldn.t|weeks)"),

    ("Add a Line", "Add a Line - Wrong Plan or Rate Applied", "Negative",
        r"(add.{0,10}line|adding.{0,10}line|added.{0,10}line).{0,100}(wrong plan|incorrect plan|wrong rate|wrong tier|not the plan|different plan)"),

    ("Add a Line", "Add a Line - Cost Not Accurately Disclosed", "Negative",
        r"(add.{0,10}line|adding.{0,10}line).{0,100}(didn.t tell|not told|surprised|wasn.t informed|no one mentioned).{0,50}(cost|fee|charge|price|how much)"),

    ("Add a Line", "Add a Line - Conflicting Channel Instructions", "Negative",
        r"(add.{0,10}line|adding.{0,10}line).{0,100}(different|conflicting|store said|phone said|contradictory|sent back|told me.{0,30}then|told me.{0,30}but)"),

    ("Add a Line", "Add a Line - Completed Correctly", "Positive",
        r"(add.{0,10}line|adding.{0,10}line|added.{0,10}line).{0,80}(easy|quickly|smooth|great|correctly|without issue|right away|perfect|fast)"),

    # ── UPGRADE ────────────────────────────────────────────────────────────────
    ("Upgrade", "Upgrade Fee Not Disclosed at POS", "Negative",
        r"(upgrade|activation).{0,60}fee.{0,80}(not told|not informed|wasn.t told|didn.t know|surprised|never mentioned|showed up|not disclosed|without warning)|"
        r"\$35.{0,30}(upgrade|fee|surprised|not told|not informed|wasn.t)|"
        r"35.{0,10}(dollar|fee).{0,30}(upgrade|activation|surprised|not told)"),

    ("Upgrade", "Upgrade Eligibility Blocked", "Negative",
        r"not eligible.{0,40}upgrade|can.t upgrade|unable to upgrade|not allowed to upgrade|won.t let me upgrade|"
        r"(55.plus|55\+).{0,60}(upgrade|eligible|plan|restrict)|"
        r"legacy plan.{0,60}upgrade|"
        r"still owe.{0,50}(upgrade|eligible)|locked in.{0,40}upgrade"),

    ("Upgrade", "Next Up Anytime - Not Offered or Misunderstood", "Negative",
        r"next up.{0,80}(not offered|didn.t offer|no one told|wasn.t told|didn.t know|confus|didn.t understand|terms|misunderstood|issue|problem)"),

    ("Upgrade", "Upgrade Process - Extended Time or System Failure", "Negative",
        r"upgrade.{0,100}(nightmare|horrible|terrible|mess|difficult|hassle|frustrat|disaster|awful|"
        r"took.{0,10}(2|3|4|5|two|three|four|five).{0,10}hour|"
        r"multiple calls|system.{0,20}(fail|error|broken|won.t|glitch)|website.{0,20}(fail|error|broken))"),

    ("Upgrade", "Upgrade Completed Successfully", "Positive",
        r"upgrade.{0,80}(easy|smooth|great|quickly|fast|no problem|no issue|perfect|helpful|excellent|wonderful|without any issue|seamless)"),

    # ── WANT A NEW DEVICE ──────────────────────────────────────────────────────
    ("Want a New Device", "No Competitive Offer for Existing Customer", "Negative",
        r"(years?.{0,25}customer|loyal|long.time customer|longtime customer|been with AT.?T).{0,100}"
        r"(no offer|no deal|no discount|no incentive|better for new|new customer.{0,40}(get|gets|receive)|"
        r"nothing for me|won.t give|don.t get|can.t get.{0,30}deal)"),

    ("Want a New Device", "Plan Type Limiting Device Access or Pricing", "Negative",
        r"(55.plus|55\+|legacy plan|grandfathered plan).{0,80}"
        r"(won.t|can.t|not eligible|restrict|limit|no deal|no offer|no discount|doesn.t qualify|excludes|not allowed)"),

    ("Want a New Device", "Competitor Offer Driving Consideration", "Negative",
        r"T.Mobile|Verizon|Xfinity|Cox.{0,10}(communic|cable|internet)|"
        r"switching to.{0,30}(another|different|T.Mobile|Verizon|Xfinity)|"
        r"going to (switch|leave|cancel)|leaving AT.?T|left AT.?T"),

    ("Want a New Device", "Rep Helped Find Right Device or Deal", "Positive",
        r"(helped me find|helped me choose|helped me pick|helped me understand).{0,60}(phone|device|plan|deal|option)|"
        r"(great|excellent|wonderful).{0,40}(helping me.{0,30}(find|choose|pick|decide).{0,30}(phone|device))"),

    # ── TRADE-IN ───────────────────────────────────────────────────────────────
    ("Trade-In", "Trade-In Credit Not Applied to Account", "Negative",
        r"trade.in.{0,100}(credit.{0,40}(not|never|hasn.t|haven.t|missing|no credit)|"
        r"not applied|not received|not showing|not on.{0,20}bill|missing|no credit|still waiting|months)"),

    ("Trade-In", "Trade-In Value Misrepresented at POS", "Negative",
        r"trade.in.{0,80}(told|quoted|promised|said|worth).{0,80}(different|less|lower|not what|changed|wrong)|"
        r"(told|quoted|promised).{0,60}trade.in.{0,60}(different|less|lower|more|not what|changed)"),

    ("Trade-In", "Trade-In Device Lost - No AT&T Receipt Confirmation", "Negative",
        r"trade.in.{0,80}(lost|no record|can.t find|never received|never got|not received by|no confirmation).{0,60}(phone|device|AT.?T)?|"
        r"(sent|mailed|shipped).{0,40}trade.in.{0,60}(no confirmation|no record|lost|missing|never received)"),

    ("Trade-In", "Trade-In Return Label or Kit Not Provided", "Negative",
        r"trade.in.{0,80}(no label|no return label|label not|kit not|no instructions|no packaging)|"
        r"(return label|trade.in label|trade.in kit).{0,60}(not sent|not received|never got|not emailed|missing|no label)"),

    ("Trade-In", "Trade-In Processed Correctly", "Positive",
        r"trade.in.{0,80}(easy|smooth|great|correctly|on time|no problem|no issue|perfect|applied|credited|received)"),

    # ── FULFILLMENT - ORDER ────────────────────────────────────────────────────
    ("Fulfillment - Order", "Order Cancelled Unexpectedly", "Negative",
        r"order.{0,60}cancel|cancel.{0,60}order"),

    ("Fulfillment - Order", "Wrong Item Shipped", "Negative",
        r"(sent|shipped|received|got).{0,30}(wrong|incorrect).{0,30}(phone|device|model|modem|router|equipment|item|color|storage|SIM)|"
        r"wrong.{0,30}(phone|device|model|modem|router|equipment|item|color|storage|SIM).{0,30}(sent|shipped|received|delivered)|"
        r"not what I ordered"),

    ("Fulfillment - Order", "Payment Processing Failure", "Negative",
        r"(payment|card).{0,50}(fail|declined|error|didn.t go through|not processed|rejected)|"
        r"duplicate.{0,20}charge|double.{0,20}charged|"
        r"funds.{0,25}(hold|held|pending).{0,40}(no order|order not)|"
        r"charged.{0,30}(twice|but no order|but order|and no order)"),

    ("Fulfillment - Order", "Order Status Unavailable or Inaccurate", "Negative",
        r"(order|tracking).{0,50}(no update|not updated|wrong status|no status|can.t track|no confirmation email|can.t find|no tracking|hasn.t updated|shows wrong)"),

    ("Fulfillment - Order", "Order Fulfilled Accurately", "Positive",
        r"order.{0,60}(arrived correctly|was correct|fulfilled|processed quickly|shipped fast|right item|exactly what|as expected|no issues|went smoothly)"),

    # ── FULFILLMENT - DELIVERY ─────────────────────────────────────────────────
    ("Fulfillment - Delivery", "Delivery Late or Missed Promised Date", "Negative",
        r"(delivery|delivered|shipping|shipment|package).{0,80}"
        r"(late|delayed|not on time|missed.{0,10}date|never arrived|still waiting|didn.t arrive|took.{0,15}(days|week)|slow|hasn.t arrived)|"
        r"next.day.{0,25}(delivery|shipping).{0,60}(not|didn.t|never|late|wrong)|"
        r"overnight.{0,25}(delivery|shipping).{0,60}(not|didn.t|never|late)"),

    ("Fulfillment - Delivery", "Package Lost in Transit", "Negative",
        r"(package|shipment|device|phone|equipment).{0,50}(lost|missing).{0,30}(transit|shipping|delivery)?|"
        r"lost in transit|"
        r"(carrier.{0,40}contact AT.?T|AT.?T.{0,40}contact carrier|carrier.{0,30}blame|blame.{0,30}carrier)"),

    ("Fulfillment - Delivery", "Missed Delivery - No Flexible Re-delivery Option", "Negative",
        r"(signature required|adult signature).{0,80}(not home|wasn.t home|no alternative|no option|no re.delivery|can.t reschedule|no pickup)|"
        r"(wasn.t home|not home).{0,80}(signature|no re.delivery|no option|no alternative|can.t reschedule)|"
        r"missed delivery.{0,60}(no option|can.t|won.t|no alternative|no pickup)"),

    ("Fulfillment - Delivery", "Delivered On Time and Intact", "Positive",
        r"(delivery|delivered|package|shipment).{0,60}(on time|as promised|arrived quickly|fast delivery|great condition|perfect condition|no damage|right on schedule)"),

    # ── RETURNS ────────────────────────────────────────────────────────────────
    ("Returns", "Return Label Missing or Not Sent", "Negative",
        r"(no return label|return label.{0,50}(missing|not sent|not received|not emailed|not included|never got|never received|still waiting|waiting for))|"
        r"(label not.{0,25}(sent|emailed|included|provided|received))|"
        r"no label.{0,30}(return|included|in box|provided)"),

    ("Returns", "30-Day Return Window Not Disclosed at POS", "Negative",
        r"30.day.{0,60}(not told|not informed|didn.t know|wasn.t told|never told|no one told|not disclosed|missed|didn.t say)|"
        r"thirty.day.{0,60}(not told|not informed|didn.t know|wasn.t told)|"
        r"(return window|return period|return policy).{0,60}(not told|not informed|didn.t know|wasn.t told|never disclosed|not explained)"),

    ("Returns", "Return Confirmed - Credit or Refund Not Applied", "Negative",
        r"(return.{0,50}(confirmed|confirmation|tracking number|receipt)|"
        r"(UPS|FedEx|carrier).{0,40}(received|confirmed|shows delivered)).{0,100}"
        r"(still charged|still owe|no credit|credit not|refund not|still on my bill|still billing|haven.t received credit)"),

    ("Returns", "Equipment Return Fee Charged After Return", "Negative",
        r"(equipment|non.return).{0,35}(fee|charge).{0,50}(returned|sent back|mailed|already return)|"
        r"\$150.{0,40}(returned|sent back|already|after return)|\$200.{0,40}(returned|sent back|already|after return)|"
        r"(charged|charge).{0,30}(150|200).{0,40}(return|returned|sent back)"),

    ("Returns", "Return Processed and Credited Correctly", "Positive",
        r"(return|returned).{0,60}(easy|smooth|great|correctly|quickly|no problem|no issue|processed|credit.{0,20}applied|refund.{0,20}received|went well)"),

    # ── EXCHANGE & REPLACE ─────────────────────────────────────────────────────
    ("Exchange & Replace", "Exchange Needed - Wrong Item Received", "Negative",
        r"(exchange|swap|need to replace).{0,80}(wrong|incorrect|not what I ordered|different model|different color|wrong model)|"
        r"received.{0,40}wrong.{0,40}(need|want|exchange|swap|replace)"),

    ("Exchange & Replace", "Exchange Needed - Defective or Damaged on Arrival", "Negative",
        r"(broken|defective|damaged|cracked|DOA|doesn.t work|not working|non.functional).{0,50}(arrived|arrival|when.{0,10}got|out of the box|on arrival|when I received|when delivered)|"
        r"arrived.{0,40}(broken|defective|damaged|cracked|not working|doesn.t work)"),

    ("Exchange & Replace", "Refurbished Device Received When New Expected", "Negative",
        r"refurb(ished)?|"
        r"(sent|received|got).{0,30}(used|pre.owned|not new).{0,30}(phone|device)|"
        r"paid for new.{0,40}(got|received|sent).{0,30}(refurb|used|not new|pre.owned)|"
        r"(phone|device).{0,30}(had scratches|was used|wasn.t new|clearly used)"),

    ("Exchange & Replace", "Exchange or Replacement Completed Correctly", "Positive",
        r"(exchange|replacement|replace).{0,60}(easy|smooth|great|correctly|quickly|no problem|no issue|went well|handled well|correct device|right phone)"),

    # ── WARRANTY & DEVICE PROTECTION ──────────────────────────────────────────
    ("Warranty & Device Protection", "Protection Plan Claim - Process Friction", "Negative",
        r"(claim|insurance claim|protection plan|ProTech).{0,80}"
        r"(difficult|complicated|denied|delayed|hard|long time|won.t|refused|unclear|confus|deductible not|not disclosed|taking.{0,15}(weeks|months|long)|process is)"),

    ("Warranty & Device Protection", "Next Up Anytime - Exchange or Return Issue", "Negative",
        r"next up.{0,100}(exchange|return|issue|problem|confus|can.t|won.t|trouble|difficult|doesn.t work|not working|how to)"),

    ("Warranty & Device Protection", "Protection Plan Added Without Customer Consent", "Negative",
        r"(protection plan|insurance|ProTech|mobile protect|device protection).{0,80}"
        r"(without.{0,25}(my permission|my consent|asking|my knowledge|authorization)|"
        r"added without|added.{0,20}without|didn.t agree|didn.t authorize|unauthorized|never asked|didn.t ask me)|"
        r"(without my permission|without my consent|without asking).{0,60}(protection|insurance|ProTech)"),

    ("Warranty & Device Protection", "Protection Plan Exchange Completed Successfully", "Positive",
        r"(claim|insurance claim|ProTech|protection plan|warranty).{0,60}"
        r"(easy|smooth|great|quickly|handled well|processed quickly|no problem|worked|resolved|completed)"),

    # ── PRICE, PROMO & CREDITS ─────────────────────────────────────────────────
    ("Price, Promo & Credits", "Promotional Credit Not Applied", "Negative",
        r"(promo|promotion|promotional credit|discount|bill credit|account credit|offer).{0,100}"
        r"(not applied|not received|not on.{0,20}bill|haven.t received|never received|still waiting|missing|hasn.t shown|hasn.t appeared|not showing)"),

    ("Price, Promo & Credits", "Bill Higher Than Price Quoted at POS", "Negative",
        r"(bill|billing|monthly bill).{0,100}(higher|more than|not what|different from|not match|doesn.t match|over.what|above.what).{0,80}"
        r"(told|quoted|promised|expected|said|agreed|represented)"),

    ("Price, Promo & Credits", "Free Device Offer Not Honored", "Negative",
        r"(told|said|promised|offered).{0,80}(free.{0,25}(phone|device|iphone|samsung|pixel|motorola))|"
        r"(free phone|free device|free iphone).{0,60}(not honored|being charged|still charging|installment|now owe|shows charge)|"
        r"phone was (supposed to be|going to be|would be) free"),

    ("Price, Promo & Credits", "Price Match or Rebate Not Fulfilled", "Negative",
        r"rebate.{0,60}(not received|never came|didn.t get|missing|no rebate|still waiting)|"
        r"price match.{0,60}(denied|not honored|refused|won.t|can.t)"),

    ("Price, Promo & Credits", "Promotional Credit Applied Correctly", "Positive",
        r"(promo|promotion|discount|credit|offer).{0,60}(applied correctly|showed up|on my bill|received|came through|honored|reflected|was there)"),

    # ── UNAUTHORIZED ACCOUNT CHANGES ──────────────────────────────────────────
    ("Unauthorized Account Changes", "Line Added Without Customer Consent", "Negative",
        r"(line|new line).{0,50}(added|appeared|showed up|on my account).{0,80}"
        r"(without.{0,25}(my permission|my consent|asking|authorization)|didn.t authorize|unauthorized|never asked|didn.t ask)|"
        r"(without my permission|without my consent|without asking).{0,60}(line|new line)"),

    ("Unauthorized Account Changes", "Feature or Service Added Without Permission", "Negative",
        r"(protection plan|insurance|ProTech|hotspot|mobile protect|feature|service|add.on).{0,80}"
        r"(added.{0,40}(without|I didn.t|never|unauthorized)|without my (permission|consent|knowledge|asking)|"
        r"I didn.t (ask|request|want|authorize)|never agreed|didn.t agree|unauthorized)"),

    ("Unauthorized Account Changes", "Plan or Account Changed Without Authorization", "Negative",
        r"(plan|account|rate plan).{0,50}(changed|switched|modified|altered).{0,80}"
        r"(without.{0,25}(my permission|my consent|asking|authorization|telling me)|didn.t authorize|unauthorized|never agreed|without telling|I didn.t ask)|"
        r"(without my permission|without my consent).{0,60}(plan|account|changed|switched)"),
]

# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    start = time.time()
    print(f"Loading file...")
    df = pd.read_csv(INPUT_FILE, low_memory=False, encoding="utf-8", on_bad_lines="skip")
    total_rows = len(df)
    print(f"  Loaded {total_rows:,} rows in {time.time()-start:.1f}s")

    # Clean verbatim column
    df[VERBATIM_COL] = df[VERBATIM_COL].fillna("").astype(str)

    results = []
    print(f"\nRunning {len(SUBTOPICS)} sub-topic patterns...")

    for i, (topic, subtopic, polarity, pattern) in enumerate(SUBTOPICS, 1):
        t0 = time.time()
        count = df[VERBATIM_COL].str.contains(pattern, case=False, regex=True, na=False).sum()
        pct = (count / total_rows) * 100
        results.append({
            "Topic": topic,
            "Sub-Topic": subtopic,
            "Polarity": polarity,
            "Count": count,
            "Pct_of_Total": round(pct, 3),
        })
        print(f"  [{i:02d}/{len(SUBTOPICS)}] {subtopic[:55]:<55} -> {count:>6,}  ({pct:.2f}%)")

    # Build output dataframe
    out = pd.DataFrame(results)

    # Add topic-level totals (sum of negatives per topic for roll-up)
    topic_neg_totals = (
        out[out["Polarity"] == "Negative"]
        .groupby("Topic")["Count"]
        .sum()
        .reset_index()
        .rename(columns={"Count": "Topic_Neg_Total"})
    )
    out = out.merge(topic_neg_totals, on="Topic", how="left")

    # Save
    out.to_csv(OUTPUT_FILE, index=False)
    print(f"\nDone in {time.time()-start:.1f}s. Results saved to:\n  {OUTPUT_FILE}")

    # ── Print summary table ────────────────────────────────────────────────────
    print(f"\n{'='*90}")
    print(f"{'TOPIC':<35} {'SUB-TOPIC':<50} {'POL':>4} {'COUNT':>8} {'PCT':>6}")
    print(f"{'='*90}")
    current_topic = None
    for _, row in out.iterrows():
        if row["Topic"] != current_topic:
            current_topic = row["Topic"]
            neg_total = row["Topic_Neg_Total"]
            print(f"\n  ── {current_topic} (neg keyword total: {int(neg_total):,}) ──")
        pol_char = "(-)" if row["Polarity"] == "Negative" else "(+)"
        print(f"  {'':<33} {row['Sub-Topic']:<50} {pol_char:>4} {int(row['Count']):>8,}  {row['Pct_of_Total']:>5.2f}%")

    print(f"\nTotal rows in file: {total_rows:,}")

if __name__ == "__main__":
    main()
