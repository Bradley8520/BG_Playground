import re
from pathlib import Path

import numpy as np
import pandas as pd
from collections import Counter, defaultdict


BASE = Path(r"c:\Users\bg763c\OneDrive - AT&T Services, Inc\Documents\VS Code\Git Test")
TAXONOMY_FILE = BASE / "VOC_Classification_Taxonomy_v4.csv"
VERBATIMS_FILE = BASE / "Care_Verbatims_Apr2026_classification_testing.csv"
VERBATIM_COL = "VERBATIM_RESPONSE"

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "been", "being", "but", "by",
    "for", "from", "had", "has", "have", "he", "her", "hers", "him", "his",
    "i", "if", "in", "into", "is", "it", "its", "me", "my", "of", "on", "or",
    "our", "ours", "she", "so", "that", "the", "their", "them", "they", "this",
    "to", "too", "us", "was", "we", "were", "what", "when", "where", "which",
    "who", "with", "you", "your", "yours", "att", "atandt", "service", "customer",
}


def clean_text(s: str) -> str:
    s = "" if s is None else str(s)
    s = s.replace("\n", " ").replace("\r", " ")
    return re.sub(r"\s+", " ", s).strip()


def build_label_text(row: pd.Series) -> str:
    parts = [
        clean_text(row.get("Category", "")),
        clean_text(row.get("Category_Definition", "")),
        clean_text(row.get("Topic", "")),
        clean_text(row.get("Topic_Definition", "")),
        clean_text(row.get("Sub_Topic", "")),
        clean_text(row.get("Sub_Topic_Definition", "")),
        f"polarity {clean_text(row.get('Polarity', ''))}",
        f"channel {clean_text(row.get('Survey_Channel', ''))}",
    ]
    return " ".join(p for p in parts if p)


def tokenize(s: str) -> list[str]:
    s = clean_text(s).lower().replace("at&t", "att")
    toks = re.findall(r"[a-z0-9']+", s)
    out = []
    for t in toks:
        if len(t) < 3:
            continue
        if t in STOPWORDS:
            continue
        out.append(t)
    return out


def same_topic_neighbor(subtopic_idx: int, sim_matrix: np.ndarray, topic_ids: np.ndarray) -> tuple[int, float]:
    same_topic = np.where(topic_ids == topic_ids[subtopic_idx])[0]
    same_topic = same_topic[same_topic != subtopic_idx]
    if len(same_topic) == 0:
        return -1, 0.0
    sims = sim_matrix[subtopic_idx, same_topic]
    best_pos = int(np.argmax(sims))
    return int(same_topic[best_pos]), float(sims[best_pos])


def note_for_row(
    row: pd.Series,
    count: int,
    pct: float,
    avg_score: float,
    avg_margin: float,
    sibling_name: str,
    sibling_sim: float,
) -> str:
    status = ""
    action = ""

    if count == 0:
        status = "No matched verbatims in Apr-2026 sample."
        action = "Candidate to park or aggregate into topic-level bucket until measurable volume appears."
    elif count < 15:
        status = "Very low volume signal."
        action = "Consider aggregating with nearest sibling unless a distinct operational owner requires separate tracking."
    elif count < 50:
        status = "Low volume but present."
        action = "Retain for monitoring; consider roll-up if this remains low across multiple months."
    elif pct >= 1.0:
        status = "High-impact sub-topic with strong share of verbatims."
        action = "Keep as a standalone sub-topic."
    else:
        status = "Material signal with usable volume."
        action = "Keep as standalone and tune examples as needed."

    overlap = ""
    if sibling_sim >= 0.78:
        overlap = (
            f" High contextual overlap with '{sibling_name}' (definition similarity {sibling_sim:.2f}); "
            "consider combining or tightening boundaries."
        )

    confidence = ""
    if count > 0 and avg_margin < 0.03:
        confidence = " Boundary appears fuzzy in this sample; refine examples/keywords to improve separability."
    elif count > 0 and avg_score < 0.12:
        confidence = " Match confidence is light; consider clearer discriminators in definition text."

    category_move = ""
    name_text = f"{row.get('Topic', '')} {row.get('Sub_Topic', '')}".lower()
    category = str(row.get("Category", ""))
    if category == "People" and re.search(r"\b(bill|billing|price|pricing|promo|credit|fee|cost)\b", name_text):
        category_move = " Context may align more with Pricing; review category placement."
    elif category == "Pricing" and re.search(r"\b(rude|friendly|helpful|empathy|attitude|professional)\b", name_text):
        category_move = " Context may align more with People; review category placement."

    return f"{status} {action}{overlap}{confidence}{category_move}".strip()


def main() -> None:
    taxonomy = pd.read_csv(TAXONOMY_FILE, encoding="utf-8", low_memory=False)
    verbatims = pd.read_csv(VERBATIMS_FILE, encoding="utf-8", low_memory=False, on_bad_lines="skip")

    if VERBATIM_COL not in verbatims.columns:
        raise ValueError(f"Missing expected verbatim column: {VERBATIM_COL}")

    taxonomy = taxonomy.copy().reset_index(drop=True)
    text_labels = taxonomy.apply(build_label_text, axis=1).tolist()
    text_verbatims = verbatims[VERBATIM_COL].fillna("").astype(str).apply(clean_text).tolist()

    # Build weighted token profiles for each sub-topic and inverted index.
    n_labels = len(taxonomy)
    label_tokens = []
    df_counter = Counter()
    for i, row in taxonomy.iterrows():
        base_tokens = tokenize(text_labels[i])
        name_tokens = tokenize(str(row.get("Sub_Topic", "")))
        topic_tokens = tokenize(str(row.get("Topic", "")))

        tok_weights = Counter(base_tokens)
        for t in name_tokens:
            tok_weights[t] += 3
        for t in topic_tokens:
            tok_weights[t] += 2

        label_tokens.append(tok_weights)
        for t in tok_weights.keys():
            df_counter[t] += 1

    idf = {t: np.log((n_labels + 1) / (df + 1)) + 1.0 for t, df in df_counter.items()}

    token_to_labels: dict[str, list[tuple[int, float]]] = defaultdict(list)
    for i, weights in enumerate(label_tokens):
        for t, w in weights.items():
            token_to_labels[t].append((i, w * idf.get(t, 1.0)))

    # Score each verbatim against candidate labels sharing at least one token.
    top1_idx = np.zeros(len(text_verbatims), dtype=int)
    top1_score = np.zeros(len(text_verbatims), dtype=float)
    top2_score = np.zeros(len(text_verbatims), dtype=float)

    for i, txt in enumerate(text_verbatims):
        toks = tokenize(txt)
        if not toks:
            # Fallback to a generic high-level intent bucket by deterministic index.
            top1_idx[i] = 0
            continue

        scores = defaultdict(float)
        tok_counts = Counter(toks)
        for t, tf in tok_counts.items():
            postings = token_to_labels.get(t)
            if not postings:
                continue
            for lbl_idx, lbl_w in postings:
                scores[lbl_idx] += tf * lbl_w

        if not scores:
            top1_idx[i] = 0
            continue

        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        top1_idx[i] = ranked[0][0]
        top1_score[i] = float(ranked[0][1])
        top2_score[i] = float(ranked[1][1]) if len(ranked) > 1 else 0.0

    margin = top1_score - top2_score

    total = len(text_verbatims)
    counts = np.bincount(top1_idx, minlength=len(taxonomy))

    avg_score_by_subtopic = np.zeros(len(taxonomy), dtype=float)
    avg_margin_by_subtopic = np.zeros(len(taxonomy), dtype=float)
    for i in range(len(taxonomy)):
        m = top1_idx == i
        if np.any(m):
            avg_score_by_subtopic[i] = float(np.mean(top1_score[m]))
            avg_margin_by_subtopic[i] = float(np.mean(margin[m]))

    # Build same-topic overlap map using weighted token cosine similarity.
    lab_sim = np.zeros((n_labels, n_labels), dtype=float)
    norms = np.zeros(n_labels, dtype=float)
    for i in range(n_labels):
        norms[i] = np.sqrt(sum((w * idf.get(t, 1.0)) ** 2 for t, w in label_tokens[i].items()))

    for i in range(n_labels):
        for j in range(i, n_labels):
            if i == j:
                lab_sim[i, j] = 1.0
                continue
            common = set(label_tokens[i].keys()) & set(label_tokens[j].keys())
            dot = 0.0
            for t in common:
                wi = label_tokens[i][t] * idf.get(t, 1.0)
                wj = label_tokens[j][t] * idf.get(t, 1.0)
                dot += wi * wj
            denom = norms[i] * norms[j]
            s = (dot / denom) if denom > 0 else 0.0
            lab_sim[i, j] = s
            lab_sim[j, i] = s
    topic_ids = taxonomy["Topic"].fillna("").astype(str).to_numpy()

    notes = []
    for i, row in taxonomy.iterrows():
        neighbor_idx, neighbor_sim = same_topic_neighbor(i, lab_sim, topic_ids)
        neighbor_name = taxonomy.loc[neighbor_idx, "Sub_Topic"] if neighbor_idx >= 0 else "n/a"

        c = int(counts[i])
        pct = round((c / total) * 100, 3) if total else 0.0
        note = note_for_row(
            row=row,
            count=c,
            pct=pct,
            avg_score=float(avg_score_by_subtopic[i]),
            avg_margin=float(avg_margin_by_subtopic[i]),
            sibling_name=str(neighbor_name),
            sibling_sim=float(neighbor_sim),
        )
        notes.append(note)

    taxonomy["Classified_Count"] = counts.astype(int)
    taxonomy["Classified_Pct"] = np.round((counts / total) * 100, 3)
    taxonomy["Notes"] = notes

    taxonomy.to_csv(TAXONOMY_FILE, index=False, encoding="utf-8")

    print(f"Updated taxonomy file: {TAXONOMY_FILE}")
    print(f"Total verbatims classified: {total:,}")
    print(f"Sub-topics with zero volume: {(taxonomy['Classified_Count'] == 0).sum()}")
    print("Top 15 sub-topics by count:")
    print(
        taxonomy[["Category", "Topic", "Sub_Topic", "Classified_Count", "Classified_Pct"]]
        .sort_values("Classified_Count", ascending=False)
        .head(15)
        .to_string(index=False)
    )


if __name__ == "__main__":
    main()
