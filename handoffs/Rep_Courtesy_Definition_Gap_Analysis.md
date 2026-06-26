# Rep Courtesy — Definition Gap Analysis & Recommendations

**Date:** 2026-06-19
**Status:** Documented for future reference — no changes applied
**Context:** After consolidating Rep Attitude & Demeanor, Rep Empathy & Emotional Ownership, Rep Patience & Thoroughness, and Rep Professionalism into a single `Rep Courtesy` topic, two anchor sub-topics were added — `Rep Was Courteous` and `Rep Not Courteous` — with definitions sourced from the 24-prompt revised prompt set. This document records gaps identified between those anchor definitions and the signal coverage in the component sub-topics they are intended to represent.

**Note on approach:** The Rep Was Courteous and Rep Not Courteous definitions are intentionally written for LLM classification, not REGEX. The LLM is expected to use contextual understanding to recognize semantic equivalents (e.g., inferring that "took time to explain" signals patience; "pressured me" signals pushiness). The gaps below are documented in case explicit phrase expansion is ever needed — they are NOT recommended for immediate addition.

---

## Rep Was Courteous — Gaps

**Sub-topics considered part of Rep Was Courteous:**
- Rep Was Friendly / Kind / Warm
- Rep Was Patient
- Rep Was Professional

### From Rep Was Friendly / Kind / Warm

| Signal in sub-topic definition | Covered in Rep Was Courteous? | Gap |
|---|---|---|
| friendly, nice, kind, warm, sweet, polite, courteous, pleasant | ✅ Yes — explicit in word list | — |
| wonderful, lovely, delightful | ❌ No | These terms are in the Friendly sub-topic word list but absent from the Courteous anchor |
| "nice attitude," "pleasant voice," "great personality" | ❌ No | Phrase-level signals not represented |

### From Rep Was Patient

| Signal in sub-topic definition | Covered in Rep Was Courteous? | Gap |
|---|---|---|
| patient | ✅ Yes — explicit in word list | — |
| "took their time," "took time to explain" | ❌ No | Behavioral patience phrases not in anchor |
| "never rushed me," "gave me all the time I needed" | ❌ No | Absence-of-rush signals not in anchor |

### From Rep Was Professional

| Signal in sub-topic definition | Covered in Rep Was Courteous? | Gap |
|---|---|---|
| professional | ✅ Yes — explicit in word list | — |
| well spoken, composed, business-like, proper | ❌ No | Professionalism-specific descriptors absent |
| "carried themselves well" | ❌ No | Behavioral phrasing absent |
| Spanish: "muy profesional," "bien hablado" | ❌ No | Current Spanish list has `educado` but not `profesional` |

### Recommended Additions (if explicit expansion ever needed)

**Word list additions:**
> wonderful, lovely, delightful, well spoken, composed, business-like, proper

**Behavioral phrase examples:**
> "nice attitude," "great personality," "pleasant voice," "took their time," "took time to explain," "never rushed me," "gave me all the time I needed," "carried themselves well"

**Spanish additions:**
> profesional, muy profesional, bien hablado

---

## Rep Not Courteous — Gaps

**Sub-topics considered part of Rep Not Courteous:**
- Rep Was Dismissive / Did Not Listen
- Rep Was Impatient / Rushed
- Rep Was Pushy / Aggressive Sales Approach
- Rep Was Rude / Disrespectful
- Rep Was Unprofessional / Incompetent *(courtesy-related signals only — see note below)*

### From Rep Was Dismissive / Did Not Listen

| Signal in sub-topic definition | Covered in Rep Not Courteous? | Gap |
|---|---|---|
| dismissive | ✅ Yes — explicit in word list | — |
| robotic, impersonal | ❌ No | Emotional detachment descriptors absent |
| "did not listen," "talked over me," "ignored what I said" | ❌ No | Listening-failure phrases not in anchor |
| "didn't care about my problem" | ❌ No | Indifference phrase absent |

### From Rep Was Impatient / Rushed

| Signal in sub-topic definition | Covered in Rep Not Courteous? | Gap |
|---|---|---|
| impatient | ✅ Yes — explicit in word list | — |
| "rushed me," "cut me short," "didn't let me finish" | ❌ No | Rushing behavior phrases absent |
| "wanted to get me off the phone," "felt hurried" | ❌ No | Urgency-framing signals absent |

### From Rep Was Pushy / Aggressive Sales Approach

| Signal in sub-topic definition | Covered in Rep Not Courteous? | Gap |
|---|---|---|
| pushy | ✅ Yes — explicit in word list | — |
| "hard sell," "pressured me," "forced products on me" | ❌ No | Sales-pressure phrases absent |
| "wouldn't take no," "kept trying to sell me" | ❌ No | Persistence-framing signals absent |
| Distinction: applies to conduct/demeanor, not sales effectiveness | ❌ No | Not stated in anchor definition |

### From Rep Was Rude / Disrespectful

| Signal in sub-topic definition | Covered in Rep Not Courteous? | Gap |
|---|---|---|
| rude, disrespectful, condescending | ✅ Yes — explicit in word list | — |
| nasty, arrogant, mean, snappy | ❌ No | Additional rudeness descriptors absent |
| "talked down to me," "had an attitude," "nasty attitude" | ❌ No | Phrase-level signals absent |

### From Rep Was Unprofessional / Incompetent (courtesy signals only)

| Signal in sub-topic definition | Covered in Rep Not Courteous? | Gap / Note |
|---|---|---|
| unprofessional | ✅ Yes — explicit in word list | — |
| poor conduct, sloppy, careless | ❌ No | Conduct/behavior words absent from anchor |
| incompetent, "doesn't know what they're doing," "needs retraining," "clearly not trained" | ⚠️ Not excluded | **These signals belong to Rep Lacked Knowledge / Gave Wrong Information, not Rep Not Courteous.** A future EXCLUDE clause may be warranted if LLM misroutes these. |

### Recommended Additions (if explicit expansion ever needed)

**Word list additions:**
> nasty, arrogant, mean, snappy, robotic, impersonal

**Behavioral phrase examples:**
> "talked down to me," "had an attitude," "nasty attitude," "did not listen," "talked over me," "ignored what I said," "rushed me," "cut me short," "didn't let me finish," "wanted to get me off the phone," "hard sell," "pressured me," "forced products on me," "wouldn't take no," "poor conduct"

**Spanish additions:**
> agresivo, impaciente, indiferente

**EXCLUDE clause (if competence bleed is observed):**
> EXCLUDE: Competence-gap language ("incompetent," "doesn't know what they're doing," "needs retraining," "clearly not trained") — routes to Rep Lacked Knowledge / Gave Wrong Information, not Rep Not Courteous.

---

## When to Revisit This Document

Consider applying some or all of these recommendations if:
- Classification runs show Rep Was Courteous / Rep Not Courteous with unexpectedly low recall compared to the component sub-topics (e.g., Rep Was Friendly captures volume that Rep Was Courteous misses)
- Competence-gap language ("incompetent," "needs retraining") is being misrouted to Rep Not Courteous instead of Rep Lacked Knowledge
- Spanish verbatim coverage on professional or pushy signals is weak
- A REGEX fallback layer is added alongside the LLM classifier

---

*Document created: 2026-06-19*
*Source: Gap analysis comparing Rep Was Courteous / Rep Not Courteous anchor definitions against component sub-topic definitions in VOC_Classification_Taxonomy_v4.csv*
