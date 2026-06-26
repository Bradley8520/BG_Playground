import csv, re
from collections import defaultdict
from datetime import datetime

# ── Sub-topic keyword rules (ordered – first match wins) ──────────────────────
SUBTOPICS = [
    (
        "Unauthorized Charges / Services Added Without Consent",
        (
            r"without (my |me )?(knowing|consent|permission|telling me|authoriz)"
            r"|didn'?t (authorize|request|ask for)"
            r"|add.{0,25}without (my |me )?(knowing|consent|permission|asking)"
            r"|put (me |add.{0,10}) on.{0,30}without"
            r"|unsolicited"
            r"|services? (i|they) did not (request|ask|use|authorize)"
            r"|charged for (something|service|it).{0,30}(didn'?t|did not) (use|request|ask|authorize)"
            r"|added.{0,20}(plan|service|line|feature).{0,20}(without|didn'?t|not)"
        ),
    ),
    (
        "Scam / External Fraud Concern",
        (
            r"\bscam(med|ming|s)?\b"
            r"|\bfraud\b|\bfraudulent\b"
            r"|fake att|impersonat|phishing"
            r"|someone.{0,30}claiming to be (att|at&t)"
            r"|almost got scammed"
            r"|people.{0,20}who said (they were|he was|she was).{0,20}(att|at&t)"
        ),
    ),
    (
        "Rep Perceived as Lying / Dishonesty",
        (
            r"\blied\b|\bliar\b|\bliars\b"
            r"|\blie after lie\b"
            r"|\byou lied\b|\bthey lied\b|\batt lied\b"
            r"|accused.{0,20}(liar|lying|making up)"
            r"|being lied|has lied|have lied"
            r"|company.{0,20}(lie|lied|lies)"
            r"|\blies\b.{0,30}(money|promot|about|to get|when)"
            r"|\blie\b.{0,15}(about|to|when|just)"
            r"|dishonest|decepti|making (assumption|me feel like i was making)"
            r"|stop lying|nothing but lies|bunch of.{0,15}liar"
        ),
    ),
    (
        "Promotion / Advertised Offer Not Honored",
        (
            r"promot.{0,50}(not honor|didn'?t honor|never got|never receiv|not applied|refuse|won'?t honor|lied about)"
            r"|bait.{0,10}switch"
            r"|advertis.{0,30}(not honor|false|misled|lied)"
            r"|offer.{0,40}(not honor|not given|refused|lied about|misrepresent)"
            r"|(free|free upgrade).{0,40}(not free|now charged|owe|paying for|wasn'?t|costs?)"
            r"|promo.{0,40}(not honor|refused|never got|never applied|didn'?t get|lied)"
            r"|reward.{0,40}(never|didn'?t|not receiv|not given|wait|weeks|month)"
            r"|gift card.{0,30}(never|didn'?t|not receiv|not given)"
            r"|(honor|honored).{0,15}(promo|offer|deal|advertis|reward|screen|lifetime|warranty|commitment|agreement)"
            r"|(don'?t|didn'?t|refused to).{0,10}honor.{0,30}(promo|offer|deal|advertis|commitment|promise|agreement)"
            r"|qualify.{0,30}promot.{0,30}(didn'?t|don'?t|no longer|not)"
        ),
    ),
    (
        "Billing / Pricing Higher Than Quoted",
        (
            r"(bill|monthly bill|charge|cost|price|rate|amount).{0,50}(more than|higher than|different from|not what|not match|higher|more).{0,30}(told|quoted|promised|expected|said)"
            r"|quoted.{0,40}(now paying|being charged|owe|but.{0,20}bill|instead)"
            r"|(told|promised|said).{0,30}\$[\d,]+.{0,40}(but|and now|instead|however).{0,30}(bill|charge|owe|paying|cost)"
            r"|(told|said|promised).{0,30}(bill|cost|it would be|would be).{0,30}\$[\d,]+"
            r"|bill.{0,30}(jumped|increased|went up|higher|more|spike).{0,30}(no warn|unexpect|surpris|without)"
            r"|overcharg"
            r"|hidden fee"
            r"|(was not|wasn'?t).{0,10}(told|informed).{0,30}(charge|fee|cost|price|bill)"
            r"|(more|higher).{0,10}than.{0,20}(told|quoted|promised|expected|said)"
            r"|pay more.{0,20}(than|what).{0,20}(told|promised|quoted|expected)"
            r"|wrong (amount|price|charge|bill)"
            r"|(monthly fee|monthly bill).{0,40}(promised|told|quoted|said).{0,20}(att|at.t|store|costco|walmart|representative|rep)"
            r"|(free|free of charge).{0,50}(now owe|now charged|charged me|now.{0,10}paying|bill)"
        ),
    ),
    (
        "Promise / Commitment Not Followed Through",
        (
            r"promis.{0,60}(never|didn'?t|not|no one|nothing|still|fail|never happen|never came|never called|never sent|not receiv|hasn'?t|haven'?t|don'?t exist|not followed)"
            r"|as promised.{0,30}(never|didn'?t|not|no one|still|haven'?t|hasn'?t)"
            r"|(never|didn'?t).{0,10}(called|followed up|got back|came through|sent|emailed|received|honor)"
            r"|said.{0,30}would.{0,30}(call|follow|send|email|resolve|fix|credit|contact|reach out).{0,50}(never|didn'?t|not|nothing|still|hasn'?t|haven'?t)"
            r"|told.{0,30}(72 hours|24 hours|hours|days|weeks).{0,30}(nothing|no one|still|never|haven'?t|hasn'?t)"
            r"|commitment.{0,30}(not honor|not kept|not fulfil|didn'?t)"
            r"|not follow.{0,10}through"
            r"|(callback|call back|follow.{0,5}up).{0,30}(never|didn'?t|not)"
            r"|waiting.{0,40}(nothing|no one|no.{0,5}call|still|no response|hear from)"
            r"|fell through"
            r"|promised.{0,10}(document|email|call|credit|refund|discount|number).{0,30}(never|didn'?t|not|still|haven'?t)"
            r"|(didn'?t|don'?t|won'?t).{0,10}get.{0,20}(what|what was).{0,20}promised"
            r"|what.{0,5}(was|were).{0,5}promised.{0,30}(not|never|doesn'?t|don'?t)"
            r"|told.{0,30}(resolved|fixed|handled|taken care).{0,30}(clearly|but).{0,30}(not|it hadn'?t|it wasn'?t)"
        ),
    ),
    (
        "Wrong / Misleading Information from Rep",
        (
            r"wrong (info|information|detail|answer|thing|plan|price|data)"
            r"|incorrect (info|information|detail|answer|amount|price|plan)"
            r"|\bmislead|\bmisinform|\bmisled"
            r"|different (answer|info|story|thing|told|explanation).{0,30}(every|different|each|another|multiple|various)"
            r"|every (person|representative|rep|agent|store).{0,20}had a different"
            r"|told (me |us )?(something |one thing |different|another thing ).{0,30}(but|however|instead|and then|turns out)"
            r"|found out.{0,20}(that was not|it was not|it wasn'?t|that isn'?t|was wrong|was incorrect|was different)"
            r"|my understanding was.{0,30}(not the case|wrong|incorrect|different)"
            r"|thought.{0,20}(included|covered|part of).{0,30}(but|however|turns out|found out)"
            r"|rep.{0,30}(wrong|incorrect|mislead|misinform|didn'?t know|no clue|clueless)"
            r"|information.{0,20}(wrong|incorrect|false|misleading|inaccurate|different)"
            r"|contradictory|contradiction"
            r"|told.{0,30}(plan|feature|service).{0,30}(included|covered|free|no charge).{0,30}(but|turns out|found out|however).{0,30}(not|wasn'?t|doesn'?t|didn'?t)"
            r"|was (not|never) told.{0,30}(about|that|of).{0,20}(fee|charge|cost|price|increase)"
        ),
    ),
    (
        "General Trust / Credibility Concern",
        (
            r"can'?t trust|don'?t trust|no trust|lost.{0,10}trust|trust.{0,20}(you|att|at&t|broken|gone|issue)"
            r"|honoring.{0,10}(their )?word|honor.{0,10}their word"
            r"|feel.{0,15}(cheated|robbed|ripped off|taken advantage)"
            r"|\brip.?off\b|ripoff"
            r"|shady|sketchy|borderline shady"
            r"|unfair (practice|treatment|charge|billing)"
            r"|terrible (company|service|practice)"
            r"|unethical"
            r"|owe me|you owe|they owe"
            r"|very disappointed (in|with).{0,5}(att|at&t|you|your)"
            r"|paying at least.{0,20}too much"
            r"|credibility"
            r"|not transparent|lack of transparency"
        ),
    ),
]

def classify(text):
    t = text.lower() if text else ""
    for label, pattern in SUBTOPICS:
        if isinstance(pattern, tuple):
            combined = "|".join(f"(?:{p})" for p in pattern)
            if re.search(combined, t):
                return label
        else:
            if re.search(pattern, t):
                return label
    return "Other / Unclassifiable"

# ── Read CSV ──────────────────────────────────────────────────────────────────
file = "Perceived Trust Verbatims.csv"
may_counts  = defaultdict(int)
jun_counts  = defaultdict(int)
total_rows  = 0
skipped     = 0

# Also capture sample verbatims per subtopic for audit
samples = defaultdict(list)

with open(file, newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total_rows += 1
        verbatim    = row.get("VERBATIM_RESPONSE", "")
        date_str    = row.get("SRVY_CMPL_DT", "").strip()

        try:
            dt = datetime.strptime(date_str, "%m/%d/%Y")
        except ValueError:
            skipped += 1
            continue

        subtopic = classify(verbatim)

        if len(samples[subtopic]) < 3:
            samples[subtopic].append(f"  [{date_str}] {verbatim[:120]}")

        if dt.month == 5 and dt.year == 2026:
            may_counts[subtopic] += 1
        elif dt.month == 6 and dt.year == 2026:
            jun_counts[subtopic] += 1

# ── Aggregate ─────────────────────────────────────────────────────────────────
all_topics = sorted(set(list(may_counts.keys()) + list(jun_counts.keys())))

total_may = sum(may_counts.values())
total_jun = sum(jun_counts.values())

print(f"Total rows parsed : {total_rows}  |  Skipped (no valid date): {skipped}")
print(f"May records       : {total_may}   |  June records: {total_jun}")
print()

header = f"{'Sub-Topic':<52} {'May':>5} {'May%':>6}  {'Jun':>5} {'Jun%':>6}  {'Chg':>6} {'%Chg':>8}"
print(header)
print("=" * 100)

rows_out = []
for topic in all_topics:
    m = may_counts[topic]
    j = jun_counts[topic]
    m_pct = (m / total_may * 100) if total_may else 0
    j_pct = (j / total_jun * 100) if total_jun else 0
    chg   = j - m
    pct_chg = ((j - m) / m * 100) if m else float("inf")
    rows_out.append((topic, m, m_pct, j, j_pct, chg, pct_chg))

# Sort by June volume desc
rows_out.sort(key=lambda x: x[3], reverse=True)

for topic, m, m_pct, j, j_pct, chg, pct_chg in rows_out:
    pct_chg_str = f"{pct_chg:+.1f}%" if pct_chg != float("inf") else "   NEW"
    chg_str = f"{chg:+d}"
    print(f"{topic:<52} {m:>5} {m_pct:>5.1f}%  {j:>5} {j_pct:>5.1f}%  {chg_str:>6} {pct_chg_str:>8}")

print("-" * 100)
print(f"{'TOTAL':<52} {total_may:>5} {'':>6}  {total_jun:>5}")

print()
print("-- OTHER / UNCLASSIFIABLE SAMPLE (first 40) --")
other_samples = []
with open(file, newline="", encoding="utf-8-sig") as f2:
    reader2 = csv.DictReader(f2)
    for row in reader2:
        v = row.get("VERBATIM_RESPONSE","")
        d = row.get("SRVY_CMPL_DT","")
        if classify(v) == "Other / Unclassifiable" and len(other_samples) < 40:
            other_samples.append(f"  [{d}] {v[:140]}")
for s in other_samples:
    print(s)

print()
print("-- SAMPLE VERBATIMS PER SUB-TOPIC (up to 3 each) --")
for topic, m, m_pct, j, j_pct, chg, pct_chg in rows_out:
    print(f"\n[{topic}]")
    for s in samples.get(topic, []):
        print(s)
