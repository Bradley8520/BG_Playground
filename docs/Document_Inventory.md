# Document Inventory

> **Living document** — update whenever files are added, archived, or retired.
> Last updated: 2026-06-26 (deleted superseded Workspace_Guide snapshots)
> Trigger phrase: `review my workspace` will prompt a full refresh of this file.

---

## How Copilot Accesses Files

| Mode | What Copilot Sees |
|------|-------------------|
| **Automatic** | `.github/copilot-instructions.md` only — injected into every chat |
| **Trigger phrase** | `taxonomy: [X]` → loads `skills/taxonomy/SKILL.md` automatically |
| **You must attach** | All project files: CSVs, scripts, docs, verbatims — drag into chat or type `#file:path/filename` |

---

## Starter Attachment Set — Taxonomy Work

When starting a taxonomy session, attach these:

```
Minimum for Care taxonomy:
  handoffs/VOC_TAXONOMY_CARE_FILE_BUILD_HANDOFF.md   ← most recent context
  projects/voc-taxonomy/taxonomy/VOC_Classification_Taxonomy_v4.csv  ← current master
  projects/voc-taxonomy/docs/Care_Taxonomy_V5_Mapping_Table.md       ← V5 doc

Add for V5 build work:
  projects/voc-taxonomy/taxonomy/Care_Taxonomy_V5_Mapping_Table.csv
  projects/voc-taxonomy/docs/Taxonomy_V4_Enhancement_Recommendations.md

Add for prompt work:
  projects/voc-taxonomy/prompts/care_classification_prompt_v1.md
  projects/voc-taxonomy/docs/VOC_Prompt_Authoring_Guide.md
```

---

## Taxonomy — Master Data (`projects/voc-taxonomy/taxonomy/`)

| File | Summary | Last Updated | Status |
|------|---------|--------------|--------|
| `VOC_Classification_Taxonomy_v4.csv` | **Current master taxonomy — Care channel** | 2026-06-22 | ✅ Active |
| `VOC_Classification_Taxonomy_Care.csv` | Care-channel version, parallel to v4 | 2026-06-22 | ✅ Active |
| `Care_Taxonomy_V5_Mapping_Table.csv` | V5 mapping in progress — enhanced definitions | 2026-06-20 | ✅ Active |
| `Shop_Purchase_Topic_Volume_Results_v2.csv` | Shop/Purchase topic volume — v2 run | 2026-06-16 | ✅ Active |
| `Shop_Purchase_SubTopic_Volume_Results.csv` | Shop/Purchase subtopic volume results | 2026-06-16 | ✅ Active |

---

## Taxonomy — SQL (`projects/voc-taxonomy/scripts/`)

| File | Summary | Last Updated | Status |
|------|---------|--------------|--------|
| `Retail_Store_Verbatims.sql` | Pulls retail store verbatims from Teradata | 2026-06-15 | ✅ Active |
| `Classification_Hierarchy.sql` | Taxonomy hierarchy query | 2026-06-26 | ✅ Active |

---

## Taxonomy — Scripts (`projects/voc-taxonomy/scripts/`)

| File | Summary | Last Updated | Status |
|------|---------|--------------|--------|
| `classify_taxonomy_v4_full.py` | Full V4 classification run on verbatims | 2026-06-19 | ✅ Active |
| `build_care_v5_mapping.py` | Builds the V5 mapping table CSV | 2026-06-19 | ✅ Active |
| `classify_shop_purchase_topics.py` | Classifies Shop/Purchase verbatims by topic | 2026-06-16 | ✅ Active |
| `classify_shop_purchase_subtopics.py` | Classifies Shop/Purchase verbatims by subtopic | 2026-06-16 | ✅ Active |
| `analyze_trust_subtopics2.py` | Analyzes perceived trust subtopics (v2) | 2026-06-25 | ✅ Active |
| `sample_verbatims.py` | Samples verbatims for testing/review | 2026-06-16 | ✅ Active |
| `md_to_docx.py` | Converts markdown output to Word (.docx) | 2026-06-23 | ✅ Active |
| `archive/analyze_trust_subtopics.py` | V1 trust analysis — superseded by v2 | 2026-06-25 | 📦 Archived |

---

## Taxonomy — Prompts (`projects/voc-taxonomy/prompts/`)

| File | Summary | Last Updated | Status |
|------|---------|--------------|--------|
| `care_classification_prompt_v1.md` | LLM prompt for Care channel classification | 2026-06-02 | ✅ Active |
| `channel_friction_subtopics_v1.md` | LLM prompt for channel friction subtopic classification | 2026-06-16 | ✅ Active |

---

## Taxonomy — Project Docs (`projects/voc-taxonomy/docs/`)

| File | Summary | Last Updated | Status |
|------|---------|--------------|--------|
| `Care_Taxonomy_V5_Mapping_Table.md` | Full V5 mapping doc with definitions and rationale | 2026-06-19 | ✅ Active |
| `Taxonomy_V4_Enhancement_Recommendations.md` | Recommended improvements to V4 | 2026-06-19 | ✅ Active |
| `Taxonomy_Revision_Changes_v4.md` | Log of changes made in V4 revision | 2026-06-19 | ✅ Active |
| `Taxonomy_Revision_Handoff_Current_Model_Gaps.md` | Gap analysis for current model | 2026-06-17 | ✅ Active |
| `VOC_Prompt_Authoring_Guide.md` | Guide for writing classification prompts | 2026-06-19 | ✅ Active |
| `Shop_Purchase_VOC_SubTopic_Analysis_FebApr2026.md` | Subtopic analysis results for Shop/Purchase | 2026-06-16 | ✅ Active |
| `Taxonomy_V4_Critique_2026-06-26.md` | Expert NLP/DS critique of V4 taxonomy — grade, findings, recommendations, prompting guidance | 2026-06-26 | ✅ Active |
| `Taxonomy_Skill_Master_Reference_DRAFT.md` | Draft master reference for taxonomy skill | 2026-06-23 | 🔄 Draft — incorporate into `skills/taxonomy/SKILL.md` when finalized |

---

## Taxonomy — Verbatims (`projects/voc-taxonomy/verbatims/`) — gitignored, local only

| File | Summary | Last Updated | Status |
|------|---------|--------------|--------|
| `Retail_Store_Verbatims_Feb-Apr2026.csv` | Retail store verbatims Feb–Apr 2026 | 2026-06-15 | ✅ Active |
| `Shop_Purchase_Verbatims_Feb-Apr2026.csv` | Shop/Purchase verbatims Feb–Apr 2026 | 2026-06-16 | ✅ Active |
| `Care_Verbatims_Apr2026_classification_testing.csv` | Care verbatims for classification testing | 2026-06-16 | ✅ Active |
| `Perceived Trust Verbatims.csv` | Perceived trust verbatims (has spaces — rename when convenient) | 2026-06-25 | ✅ Active |

---

## Taxonomy — Output Files (`projects/voc-taxonomy/output/`) — gitignored, local only

| File | Summary | Last Updated | Status |
|------|---------|--------------|--------|
| `topic_classify_output_v2.txt` | Most recent topic classification output | 2026-06-16 | ✅ Active output |
| `topic_classify_output.txt` | Earlier topic classification run | 2026-06-16 | ⏸️ Review before deleting |
| `classify_output.txt` | General classification output | 2026-06-16 | ⏸️ Review before deleting |
| `sample_verbatims_output.txt` | Sample verbatim test run output | 2026-06-16 | ⏸️ Review before deleting |

---

## Taxonomy — Archived Data (`projects/voc-taxonomy/taxonomy/archive/`)

Preserved for historical reference. Do not attach to chats — these are superseded.

| File | Reason Archived | Archived Date |
|------|----------------|---------------|
| `VOC_Classification_Taxonomy.csv` | V1 — superseded by v4 | 2026-06-26 |
| `VOC_Classification_Taxonomy_v2.csv` | V2 — superseded by v4 | 2026-06-26 |
| `VOC_Classification_Taxonomy_v3.csv` | V3 — superseded by v4 | 2026-06-26 |
| `VOC Verbatim Taxonomy (original 24).csv` | Pre-rebuild original 24 topics | 2026-06-26 |
| `VOC Verbatim Gen AI Classification - Taxonomy (original 24).csv` | Gen AI classification on original 24 | 2026-06-26 |
| `Shop_Purchase_Topic_Volume_Results.csv` | V1 results — superseded by v2 | 2026-06-26 |
| `VOC_Taxonomy_v3_Step1_People_Core.csv` through `Step11_ShopPurchase.csv` (11 files) | V3 build step artifacts — V3 complete | 2026-06-26 |

---

## Handoffs (`handoffs/`)

| File | Summary | Last Updated | Status |
|------|---------|--------------|--------|
| `VOC_TAXONOMY_CARE_FILE_BUILD_HANDOFF.md` | Most recent Care taxonomy build session | 2026-06-22 | ✅ Active — attach at start of Care sessions |
| `VOC_TAXONOMY_V4_REVISED_PROMPTS_HANDOFF.md` | V4 prompt revision session context | 2026-06-21 | ✅ Active |
| `VOC_TAXONOMY_ANALYTICAL_LABELS_HANDOFF.md` | Analytical labels design session | 2026-06-21 | ✅ Active |
| `Rep_Courtesy_Definition_Gap_Analysis.md` | Gap analysis for rep courtesy definitions | 2026-06-19 | ✅ Active |
| `SHOP_PURCHASE_SUBTOPIC_DESIGN_HANDOFF.md` | Shop/Purchase subtopic design session | 2026-06-16 | ✅ Active |
| `TAXONOMY_V3_BUILD_HANDOFF.md` | V3 build session context | 2026-05-29 | 📦 Archive — V3 complete, no need to attach |
| `Session_Handoff_2026-06-26.md` | Session handoff 2026-06-26 | 2026-06-26 | ✅ Active |
| `assessments/2026-06-26.md` | Day 0 Gen AI skills baseline assessment | 2026-06-26 | ✅ Active |
| `README.md` | Handoffs folder usage guide | 2026-05-28 | ✅ Active |
| `TEMPLATE.md` | Session handoff template | 2026-05-28 | ✅ Active |

---

## Skills (`skills/`)

| File | Trigger Phrase | Last Updated | Status |
|------|----------------|--------------|--------|
| `taxonomy/SKILL.md` | `taxonomy: [X]` | 2026-06-23 | ✅ Active |
| `coding-teacher/SKILL.md` | `coding lesson` / `walk me through [file]` / `teach me [X]` / `coding practice` | 2026-06-26 | ✅ Active |
| `advanced-prompting/SKILL.md` | `prompt coaching` / `prompt tip` / `advanced prompting` | — | ✅ Active |
| `learning-coach/SKILL.md` | `explain that` / `teach me` / `why did you do it that way` | — | ✅ Active |
| `skills-assessment/SKILL.md` | `assess my skills` / `run my assessment` / `skills review` | — | ✅ Active |
| `workspace-review/SKILL.md` | `review my workspace` / `workspace cleanup` / `folder review` | — | ✅ Active |
| `session-start/SKILL.md` | `start session` / `new session` / `where did we leave off` | — | ✅ Active |
| `doc-export/SKILL.md` | `export as Word` / `save as Word doc` / `convert to Word` | — | ✅ Active |
| `verbatim-analysis/SKILL.md` | `verbatim: [X]` / `analyze verbatims` | — | ✅ Active |
| `python-scripts/SKILL.md` | (referenced in coding work) | — | ✅ Active |
| `sql-writing/SKILL.md` | `write a query for [X]` | 2026-05-28 | ✅ Active |
| `ad-hoc-query/SKILL.md` | `ad hoc: [question]` | 2026-05-28 | ✅ Active |
| `deploy/SKILL.md` | `deploy [env]` | 2026-05-28 | ✅ Active |
| `metadata-refresh/SKILL.md` | `refresh metadata` | 2026-05-28 | ✅ Active |

---

## Workspace Config & Docs

| File | Summary | Last Updated | Status |
|------|---------|--------------|--------|
| `.github/copilot-instructions.md` | Auto-injected master config — trigger phrases, conventions, skills refs | 2026-06-26 | ✅ Active |
| `.github/prompts/deploy-checklist.prompt.md` | Reusable deploy checklist prompt | 2026-05-28 | ✅ Active |
| `.github/prompts/session-handoff.prompt.md` | Reusable session handoff prompt | 2026-05-28 | ✅ Active |
| `.github/prompts/write-query.prompt.md` | Reusable query-writing prompt | 2026-05-28 | ✅ Active |
| `docs/Workspace_Guide.md` | Living workspace map — folder structure, tools, extensions | 2026-06-26 | ✅ Active |
| `docs/Trigger_Phrases_Reference.md` | Full reference for all trigger phrases and workflows | 2026-06-26 | ✅ Active |
| `docs/Document_Inventory.md` | **This file** — living inventory of all workspace documents | 2026-06-26 | ✅ Active |
| `.gitignore` | Excludes verbatims/, output/, .venv/, .docx files | 2026-06-26 | ✅ Active |
| `.gitmessage` | Git commit message template | 2026-06-26 | ✅ Active |
| `.vscode/settings.json` | Workspace VS Code settings | 2026-06-26 | ✅ Active |
| `README.md` | Repo overview | — | ✅ Active |
| `projects/voc-taxonomy/README.md` | VOC taxonomy project overview | 2026-06-26 | ✅ Active |

---

## Status Key

| Symbol | Meaning |
|--------|---------|
| ✅ Active | In use, safe to attach |
| 📦 Archived | Preserved for history, do not attach |
| 🔄 Draft | In progress, treat as provisional |
| ⏸️ Review before deleting | Likely obsolete — review contents before removing |
