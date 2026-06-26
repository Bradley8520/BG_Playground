# VOC Taxonomy Project

Voice of Customer (VOC) classification taxonomy for AT&T care and retail channels.

## Folder Layout

| Folder | Contents |
|--------|----------|
| `taxonomy/` | Taxonomy definition CSVs — all versions (v1–v5), step files |
| `scripts/` | Python classification scripts, SQL queries |
| `docs/` | Analysis write-ups, reference guides, enhancement notes |
| `prompts/` | AI prompt templates used in classification runs |
| `verbatims/` | Raw customer verbatim files (**gitignored** — local only) |
| `output/` | Script output files (**gitignored** — generated artifacts) |

## Taxonomy Versions

| File | Description |
|------|-------------|
| `VOC_Classification_Taxonomy.csv` | Original 24-topic taxonomy |
| `VOC_Classification_Taxonomy_v2.csv` | v2 revisions |
| `VOC_Classification_Taxonomy_v3.csv` | v3 — step-by-step build |
| `VOC_Classification_Taxonomy_v4.csv` | v4 — current production version |
| `Care_Taxonomy_V5_Mapping_Table.csv` | v5 Care mapping |
| `VOC_Taxonomy_v3_Step*.csv` | Step-by-step v3 category files |

## Key Scripts

| Script | Purpose |
|--------|---------|
| `classify_taxonomy_v4_full.py` | Full v4 taxonomy classification run |
| `classify_shop_purchase_topics.py` | Shop/Purchase topic classification |
| `classify_shop_purchase_subtopics.py` | Shop/Purchase subtopic classification |
| `analyze_trust_subtopics.py` | Trust subtopic analysis |
| `build_care_v5_mapping.py` | Care v5 taxonomy mapping builder |
| `sample_verbatims.py` | Verbatim sampling utility |
| `md_to_docx.py` | Markdown → DOCX converter |
