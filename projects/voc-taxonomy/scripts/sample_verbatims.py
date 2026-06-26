import pandas as pd, random, textwrap, sys

INPUT_FILE = r"c:\Users\bg763c\OneDrive - AT&T Services, Inc\Documents\VS Code\Git Test\Care_Verbatims_Apr2026_classification_testing.csv"
df = pd.read_csv(INPUT_FILE, low_memory=False, encoding="utf-8", on_bad_lines="skip")

# Find verbatim column
vcol = None
for c in df.columns:
    if "verbatim" in c.lower() or "comment" in c.lower() or "text" in c.lower() or "response" in c.lower():
        vcol = c; break
if not vcol:
    vcol = df.columns[-1]

v = df[vcol].fillna("").astype(str)
random.seed(42)

TOPICS = {
    "Price, Promo & Credits": (
        r"\b(promo|promotion|promotional|"
        r"bill credit|account credit|monthly credit|"
        r"(discount|offer|deal|incentive).{0,40}(not applied|missing|not received|not honored|didn.t|haven.t|never|wasn.t)|"
        r"(credit|discount|promo|offer).{0,60}(not (applied|received|showing|on bill|appearing|there)|missing|still waiting|haven.t|hasn.t)|"
        r"(bill|billing|monthly bill|charge).{0,60}(higher|more than|not what|different from|doesn.t match|not match).{0,60}(told|quoted|promised|expected|said|agreed)|"
        r"(told|promised|quoted|said).{0,60}(free|no cost|no charge).{0,30}(phone|device|iphone|samsung)|"
        r"(free phone|free device|free iphone).{0,40}(being charged|now owe|installment|shows charge|still charging)|"
        r"rebate|price match|"
        r"(lied|misled|deceived|false).{0,60}(price|cost|bill|rate|charge|fee|credit|discount|promo))\b"
    ),
    "Unauthorized Account Changes": (
        r"\b(without (my )?(permission|consent|authorization|knowledge|asking)|"
        r"(added|charged|changed|switched|activated|enrolled).{0,30}(without|unauthorized)|"
        r"unauthorized (charge|line|account|change|addition|service|feature|plan)|"
        r"didn.t (authorize|agree to|consent to|ask for|request|want|approve).{0,40}(line|charge|plan|service|feature|protection|insurance|ProTech)|"
        r"never (agreed to|authorized|asked for|requested|approved).{0,40}(line|charge|plan|service|feature|protection|insurance)|"
        r"(line|service|feature|plan|insurance|ProTech|protection).{0,50}added without)\b"
    ),
    "Warranty & Device Protection": (
        r"\b(warranty|manufacturer warranty|manufacturer.s warranty|"
        r"(protection plan|device protection|mobile protect|ProTech|NEXT UP|insurance).{0,30}(claim|add|added|charge|charged|enrolled|enroll|signed up|coverage|cancel|issue|problem)|"
        r"insurance (claim|coverage|deductible)|"
        r"(file|filed|filing).{0,20}(claim|insurance claim)|"
        r"deductible|"
        r"protection plan.{0,50}(without|permission|consent|didn.t|never|unauthorized))\b"
    ),
}

CHURN_SIGNAL = (
    r"\b(cancel|cancelling|canceling|close my account|leaving AT.?T|"
    r"switching to|going to (leave|switch)|thinking about (leaving|switching)|"
    r"done with AT.?T|fed up|last straw|final straw|had enough)\b"
)
SAP_SIGNAL = (
    r"\b(order|trade.in|trade in|upgrade|deliver|shipping|shipment|"
    r"return|refund|exchange|replacement|swap|wrong (phone|device|item|modem|router|equipment)|"
    r"credit|promo|promotion|promotional credit|bill credit|free phone|free device|"
    r"didn.t receive|never received|not applied|overcharged|charged incorrectly|"
    r"unauthorized|without my permission|fulfillment|payment (fail|declined))\b"
)

SEP = "=" * 90

for topic, pattern in TOPICS.items():
    mask = v.str.contains(pattern, case=False, regex=True, na=False)
    hits = v[mask].tolist()
    n = min(10, len(hits))
    sample = random.sample(hits, n)
    print(f"\n{SEP}")
    print(f"TOPIC: {topic}  ({len(hits)} total hits)")
    print(SEP)
    for i, txt in enumerate(sample, 1):
        wrapped = textwrap.fill(txt[:500], width=85, initial_indent="  ", subsequent_indent="  ")
        print(f"[{i}] {wrapped}\n")

# Churn co-occurrence
churn_mask = v.str.contains(CHURN_SIGNAL, case=False, regex=True, na=False)
sap_mask   = v.str.contains(SAP_SIGNAL,   case=False, regex=True, na=False)
cooc_mask  = churn_mask & sap_mask
hits = v[cooc_mask].tolist()
n = min(10, len(hits))
sample = random.sample(hits, n)
print(f"\n{SEP}")
print(f"TOPIC: S&P - Cancel / Churn Intent  ({len(hits)} total hits)")
print(SEP)
for i, txt in enumerate(sample, 1):
    wrapped = textwrap.fill(txt[:500], width=85, initial_indent="  ", subsequent_indent="  ")
    print(f"[{i}] {wrapped}\n")
