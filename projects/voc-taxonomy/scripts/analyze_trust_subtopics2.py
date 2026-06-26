import csv, re, sys
from collections import defaultdict
from datetime import datetime

# Force UTF-8 output
sys.stdout.reconfigure(encoding="utf-8")

# Sub-topic rules – ordered; first match wins
SUBTOPICS = [
    ("Unauthorized Charges / Services Added Without Consent", (
        r"without (my |me |our )?(knowing|consent|permission|telling me|authoriz)"
        r"|didn'?t (authorize|request|ask for)"
        r"|added.{0,30}(plan|service|line|feature|add.?on).{0,30}without"
        r"|(plan|service|line|add.?on|feature).{0,40}without (me|my|our|us) (knowing|asking|consent|permis)"
        r"|put (me|us).{0,25}on.{0,50}without (my|me|our)? ?(knowing|asking|consent|permiss)"
        r"|services? (i|they) did not (request|ask|use|authorize)"
        r"|charged for.{0,30}(something|service|it).{0,50}(didn'?t|did not).{0,20}(use|request|ask|authorize)"
        r"|unsolicited"
    )),
    ("Scam / External Fraud Concern", (
        r"\bscam(med|ming|s|ner)?\b"
        r"|\bfraud\b|\bfraudulent\b"
        r"|fake att|impersonat|phishing"
        r"|someone.{0,40}claiming to be (att|at&t)"
        r"|people.{0,30}who said (they were|he was|she was).{0,30}(att|at&t)"
    )),
    ("Rep Perceived as Lying / Dishonesty", (
        r"\blied\b|\bliar\b|\bliars\b"
        r"|\blie after lie\b"
        r"|(you|they|att|he|she|rep|agent|company).{0,5}lied"
        r"|accused.{0,30}(liar|lying|making.{0,10}up)"
        r"|(being|been|was|get).{0,10}lied (to|about)"
        r"|company.{0,40}(lie|lied|lies)"
        r"|\blies\b.{0,50}(money|promot|about|to get|when|to (us|me|you))"
        r"|\blie\b.{0,25}(about|to (us|me|you)|when|just to)"
        r"|stop lying|nothing but lies|bunch of.{0,15}liar"
        r"|dishonest|decepti"
        r"|(lie|lying) about (how much|price|cost|plan|promot|offer|what)"
    )),
    ("Promotion / Advertised Offer Not Honored", (
        r"promot.{0,70}(not honor|didn'?t honor|never got|never receiv|not applied|refuse|won'?t honor|lied about)"
        r"|bait.{0,10}switch"
        r"|advertis.{0,50}(not honor|false|misled|lied)"
        r"|offer.{0,60}(not honor|not given|refused|lied about|misrepresent)"
        r"|(free phone|free upgrade|free device|told.{0,30}(phone|device).{0,20}(would be|was).{0,5}free).{0,100}(not free|now charged|now owe|owe|paying for|wasn'?t|costs?|instalments?|charged)"
        r"|promo.{0,60}(not honor|refused|never got|never applied|didn'?t get|lied)"
        r"|reward.{0,60}(never receiv|never got|didn'?t receiv|not given|wait|weeks?|month)"
        r"|gift card.{0,50}(never|didn'?t|not receiv|not given)"
        r"|(honor|honored).{0,25}(promo|offer|deal|advertis|reward|screen replacement|lifetime|warranty)"
        r"|(don'?t|didn'?t|refused? to|would not|won'?t).{0,20}honor.{0,50}(promo|offer|deal|advertis|commitment|promise|agreement|discount)"
        r"|qualify.{0,50}promot.{0,40}(didn'?t|don'?t|no longer|not|refused|won'?t)"
    )),
    ("Billing / Pricing Higher Than Quoted", (
        r"(bill|charge|cost|price|rate|amount).{0,70}(more than|higher than|different from|not what|not match).{0,50}(told|quoted|promised|expected|said)"
        r"|quoted.{0,70}(now paying|being charged|owe|bill|instead)"
        r"|(told|promised|said|quoted).{0,40}\$[\d,]+.{0,100}(owe|paying|charged|bill|cost|now)"
        r"|(told|said|promised|quoted).{0,80}(would be|going to be|is going to be|will be).{0,50}\$[\d,]+"
        r"|bill.{0,60}(jumped?|increased?|went up|higher|more|spike).{0,50}(no warn|unexpect|surpris|without)"
        r"|over.?charg"
        r"|hidden fee"
        r"|(more|higher).{0,20}than.{0,30}(told|quoted|promised|expected|said)"
        r"|pay.{0,15}more.{0,40}(than|what).{0,40}(told|promised|quoted|expected|was supposed)"
        r"|wrong (amount|price|charge|bill)"
        r"|(monthly fees?|monthly bill|monthly cost).{0,80}(promised|told|quoted|said).{0,50}(att|at.t|store|costco|walmart|representative|rep|them|they)"
        r"|(free|free of charge).{0,100}(now owe|now.{0,15}charged|charged me|paying|bill|instalments?)"
        r"|\bcheated.{0,20}(me|us).{0,15}(for|out of).{0,5}\$"
        r"|not what (i was|we were).{0,10}told.{0,40}(pay|cost|bill|charge)"
        r"|(supposed to|going to).{0,10}(pay|cost|be).{0,30}\$[\d,]+.{0,50}(but|now|instead|however)"
    )),
    ("Promise / Commitment Not Followed Through", (
        r"promis.{0,100}(never|didn'?t|not (there|happen|done|fulfilled?|receiv|given|followed)|no one|nothing|still (haven'?t|waiting)|fail|never happened|never came|never called|never sent|not receiv|hasn'?t|haven'?t|don'?t exist)"
        r"|as promised.{0,60}(never|didn'?t|not|no one|still|haven'?t|hasn'?t|yet|did not|have yet)"
        r"|(did not|didn'?t|never|have not|haven'?t|yet to).{0,40}(receiv|get|hear|see).{0,50}(promised|said.{0,15}would|told.{0,15}would)"
        r"|(never|didn'?t).{0,15}(called back|followed up|got back|came through|emailed|reached out|follow.{0,10}up|honored.{0,15}(promise|commit))"
        r"|said.{0,60}would.{0,80}(call|follow|send|email|resolve|fix|credit|contact|reach).{0,80}(never|didn'?t|not|nothing|still|hasn'?t|haven'?t)"
        r"|told.{0,60}would.{0,80}(resolve|fix|call|follow|contact|reach|get back|send).{0,80}(never|didn'?t|not|nothing|still|hasn'?t|haven'?t)"
        r"|not follow.{0,10}through"
        r"|(callback|call.?back|follow.{0,5}up).{0,50}(never|didn'?t|not|still)"
        r"|waiting.{0,80}(nothing|no one|no.{0,5}call|still|no response|hear from|never)"
        r"|fell through"
        r"|promised.{0,15}(document|email|case.{0,10}number|call|credit|refund|discount|number|resolution).{0,60}(never|didn'?t|not|still|haven'?t|have yet|no one|nothing)"
        r"|(didn'?t|don'?t|won'?t).{0,15}get.{0,25}(what|what was).{0,25}promised"
        r"|(what|things?).{0,15}(was|were) promised.{0,40}(not|never|doesn'?t|don'?t|didn'?t|don'?t exist)"
        r"|told.{0,60}(resolved|fixed|handled|taken care).{0,60}(clearly|but|however).{0,60}(not|it hadn'?t|it wasn'?t|hadn'?t)"
        r"|have yet to (hear|receive|get|see).{0,50}(promis|said|told|expected)"
    )),
    ("Wrong / Misleading Information from Rep", (
        r"wrong (info|information|detail|answer|thing|plan|price|data)"
        r"|incorrect (info|information|detail|answer|amount|price|plan)"
        r"|\bmislead|\bmisinform|\bmisled"
        r"|every (person|representative|rep|agent|store).{0,40}had a different"
        r"|(told|said|given).{0,15}(something |one thing |different|another thing).{0,60}(but|however|instead|and then|turns out|not true|not right|which was (wrong|incorrect|false))"
        r"|found out.{0,40}(that was not|it was not|it wasn'?t|that isn'?t|was wrong|was incorrect|was different|not the case)"
        r"|my (understanding|assumption).{0,30}was.{0,40}(not the case|wrong|incorrect|different)"
        r"|thought.{0,40}(included|covered|part of).{0,50}(but|however|turns out|found out).{0,40}(not|wasn'?t|doesn'?t|didn'?t)"
        r"|rep.{0,40}(wrong|incorrect|mislead|misinform|didn'?t know|no clue)"
        r"|information.{0,25}(wrong|incorrect|false|misleading|inaccurate)"
        r"|contradictory|contradiction"
        r"|gave (me|us).{0,10}(the |all the )?wrong"
        r"|didn'?t even (check|look up|pull up|verify|research|bother)"
        r"|totally different from what (it was|we were|i was)"
        r"|(was not|wasn'?t) (told|informed|warned).{0,40}(about|that|of).{0,25}(fee|charge|cost|price|increase)"
        r"|(told|given|said).{0,15}(different|conflicting|various|multiple) (things?|answers?|information|stories)"
    )),
    ("General Trust / Credibility Concern", (
        r"can'?t trust|don'?t trust|no trust|lost.{0,15}trust|trust.{0,25}(you|att|at&t|broken|gone|issue)"
        r"|honoring.{0,15}(their )?word|honor.{0,15}their word"
        r"|\bcheated\b"
        r"|\bripped?.{0,5}off\b|ripoff"
        r"|\bshady\b|\bsketchy\b"
        r"|unfair (practice|treatment|billing)"
        r"|(terrible|horrible|awful).{0,15}company"
        r"|unethical"
        r"|very disappointed (in|with).{0,15}(att|at&t|you|your|this company|the company)"
        r"|(rip|ripping).{0,10}(off|us|me)"
        r"|not transparent|lack of transparency"
    )),
]


def classify(text):
    t = text.lower() if text else ""
    for label, pattern in SUBTOPICS:
        if re.search(pattern, t, re.IGNORECASE):
            return label
    return "Other / Unclassifiable"


# Read CSV
FILE = "Perceived Trust Verbatims.csv"
may_counts = defaultdict(int)
jun_counts = defaultdict(int)
total_rows = 0
samples    = defaultdict(list)

with open(FILE, newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total_rows += 1
        verbatim = row.get("VERBATIM_RESPONSE", "")
        date_str = row.get("SRVY_CMPL_DT", "").strip()
        try:
            dt = datetime.strptime(date_str, "%m/%d/%Y")
        except ValueError:
            continue
        subtopic = classify(verbatim)
        if len(samples[subtopic]) < 3:
            samples[subtopic].append(f"  [{date_str}] {verbatim[:120]}")
        if dt.month == 5 and dt.year == 2026:
            may_counts[subtopic] += 1
        elif dt.month == 6 and dt.year == 2026:
            jun_counts[subtopic] += 1

# Aggregate
all_topics = sorted(set(list(may_counts.keys()) + list(jun_counts.keys())))
total_may  = sum(may_counts.values())
total_jun  = sum(jun_counts.values())

print(f"Total rows: {total_rows}  |  May: {total_may}  |  June: {total_jun}")
print()

HDR = f"{'Sub-Topic':<52} {'May':>5} {'May%':>6}  {'Jun':>5} {'Jun%':>6}  {'Chg':>6} {'%Chg':>8}"
print(HDR)
print("=" * 100)

rows_out = []
for topic in all_topics:
    m = may_counts[topic]; j = jun_counts[topic]
    m_pct = (m / total_may * 100) if total_may else 0
    j_pct = (j / total_jun * 100) if total_jun else 0
    chg   = j - m
    pct_chg = ((j - m) / m * 100) if m else float("inf")
    rows_out.append((topic, m, m_pct, j, j_pct, chg, pct_chg))

rows_out.sort(key=lambda x: x[3], reverse=True)

for topic, m, m_pct, j, j_pct, chg, pct_chg in rows_out:
    p = f"{pct_chg:+.1f}%" if pct_chg != float("inf") else "   NEW"
    print(f"{topic:<52} {m:>5} {m_pct:>5.1f}%  {j:>5} {j_pct:>5.1f}%  {chg:>+6} {p:>8}")

print("-" * 100)
print(f"{'TOTAL':<52} {total_may:>5}          {total_jun:>5}")

print()
print("-- SAMPLE VERBATIMS PER SUB-TOPIC (up to 3 each) --")
for topic, m, m_pct, j, j_pct, chg, pct_chg in rows_out:
    print(f"\n[{topic}]")
    for s in samples.get(topic, []):
        print(s)
