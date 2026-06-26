from pathlib import Path

import pandas as pd


BASE = Path(r"c:\Users\bg763c\OneDrive - AT&T Services, Inc\Documents\VS Code\Git Test")
INPUT_FILE = BASE / "VOC_Classification_Taxonomy_v4.csv"
OUT_CSV = BASE / "Care_Taxonomy_V5_Mapping_Table.csv"
OUT_MD = BASE / "Care_Taxonomy_V5_Mapping_Table.md"


PROTECTED_SUBTOPICS = {
    "Request for Different Communication Support",
    "Request to Stop Outsourcing / Use Local Staff",
    "Rep Did Not Follow Through / Broken Promise",
    "Call Was Dropped / Disconnected",
    "Data Privacy/Security",
}


def is_care_scope(s: str) -> bool:
    txt = str(s or "")
    parts = [p.strip() for p in txt.split("|")]
    return "Care" in parts or "All" in parts


def to_int(x) -> int:
    try:
        return int(float(str(x).strip()))
    except Exception:
        return 0


def map_row(row: pd.Series) -> dict:
    category = str(row["Category"])
    topic = str(row["Topic"])
    subtopic = str(row["Sub_Topic"])
    survey_channel = str(row["Survey_Channel"])
    count = to_int(row["Est_Count"])

    v5_topic = topic
    v5_subtopic = subtopic
    change_type = "Keep as-is"
    probation_days = 0
    strategic_protection = "No"

    # Targeted reporting rollups from recommendations.
    if topic == "General Customer Service":
        v5_subtopic = "General Customer Service (Unspecified)"
        change_type = "Reporting rollup"
        probation_days = 60

    if topic == "Bill Inquiry & General Bill" and subtopic in {"Bill Inquiry", "General Bill"}:
        v5_subtopic = "General Billing Inquiry"
        change_type = "Reporting rollup"
        probation_days = 60

    if topic == "Rep Recognition & Retention" and subtopic in {
        "Rep Named Specifically (Positive Mention)",
        "Rep Named Specifically (Negative Mention)",
    }:
        v5_subtopic = "Rep Named Specifically"
        change_type = "Probation rollup candidate"
        probation_days = 90

    if topic == "Shop & Purchase":
        keep_core = {"Add a Line", "Fulfillment — Order"}
        if subtopic not in keep_core:
            v5_subtopic = "Shop & Purchase — Other Transaction Friction"
            change_type = "Probation rollup candidate"
            probation_days = 60

    if (
        topic == "Door-to-Door Sales Experience"
        and subtopic == "D2D Rep Was Dishonest About Offers / Pricing"
    ):
        v5_topic = "Sales Transparency & Offer Accuracy"
        v5_subtopic = "Offer Was Misrepresented / Not What Was Promised"
        change_type = "Dual-map during probation"
        probation_days = 60

    # Strategic protection overrides.
    if subtopic in PROTECTED_SUBTOPICS:
        strategic_protection = "Yes"
        if probation_days == 0:
            probation_days = 0

    # Scorecard tiering tuned for stability-first requirement.
    if strategic_protection == "Yes":
        tier = "Protected (show in analyst + governance views)"
    elif count >= 100:
        tier = "Executive scorecard"
    elif 30 <= count <= 99:
        tier = "Analyst monitor tier"
        probation_days = max(probation_days, 60)
    else:
        tier = "Probation parking lot"
        probation_days = max(probation_days, 60)

    if change_type == "Keep as-is" and tier != "Executive scorecard":
        change_type = "No structure change; visibility tier change"

    rationale = []
    if strategic_protection == "Yes":
        rationale.append("Strategic-risk or accessibility signal; keep distinct regardless of volume.")
    if change_type.startswith("Reporting rollup"):
        rationale.append("High semantic overlap and same operational action path.")
    if change_type.startswith("Probation rollup"):
        rationale.append("Low-volume node; monitor before any default rollup decision.")
    if change_type.startswith("Dual-map"):
        rationale.append("Potentially better fit in sales-transparency family; preserve trend continuity.")
    if not rationale:
        rationale.append("Retain diagnostic granularity while aligning scorecard visibility to volume.")

    return {
        "Current_Category": category,
        "Current_Topic": topic,
        "Current_Sub_Topic": subtopic,
        "Survey_Channel": survey_channel,
        "Est_Count": count,
        "Est_Pct": row["Est_Pct"],
        "V5_Reporting_Category": category,
        "V5_Reporting_Topic": v5_topic,
        "V5_Reporting_Sub_Topic": v5_subtopic,
        "Scorecard_Tier": tier,
        "Probation_Days": probation_days,
        "Strategic_Protection": strategic_protection,
        "Change_Type": change_type,
        "Rationale": " ".join(rationale),
    }


def main() -> None:
    df = pd.read_csv(INPUT_FILE, encoding="utf-8", low_memory=False)
    care_df = df[df["Survey_Channel"].apply(is_care_scope)].copy()

    mapped_rows = [map_row(r) for _, r in care_df.iterrows()]
    out = pd.DataFrame(mapped_rows)
    out = out.sort_values(["Current_Category", "Current_Topic", "Current_Sub_Topic"]).reset_index(drop=True)
    out.to_csv(OUT_CSV, index=False, encoding="utf-8")

    # Compact markdown preview with top recommendations and sample table.
    total = len(out)
    scorecard_n = (out["Scorecard_Tier"] == "Executive scorecard").sum()
    monitor_n = (out["Scorecard_Tier"] == "Analyst monitor tier").sum()
    parking_n = (out["Scorecard_Tier"] == "Probation parking lot").sum()
    protected_n = (out["Strategic_Protection"] == "Yes").sum()

    top_changes = out[out["Change_Type"] != "Keep as-is"]
    top_changes = top_changes[
        [
            "Current_Category",
            "Current_Topic",
            "Current_Sub_Topic",
            "V5_Reporting_Topic",
            "V5_Reporting_Sub_Topic",
            "Change_Type",
            "Probation_Days",
        ]
    ]

    lines = []
    lines.append("# Care-Only v5 Mapping Table")
    lines.append("")
    lines.append("This table is scoped to rows where Survey_Channel includes Care or All.")
    lines.append("No taxonomy labels are deleted; changes are reporting-layer mappings and visibility tiers.")
    lines.append("")
    lines.append("## Summary")
    lines.append(f"- Care/All rows mapped: {total}")
    lines.append(f"- Executive scorecard rows: {scorecard_n}")
    lines.append(f"- Analyst monitor rows: {monitor_n}")
    lines.append(f"- Probation parking lot rows: {parking_n}")
    lines.append(f"- Strategic-protection rows: {protected_n}")
    lines.append("")
    lines.append("## Highest-Priority Structural Mappings")
    lines.append("")
    lines.append("| Current Topic | Current Sub-Topic | Proposed v5 Reporting Sub-Topic | Change Type | Probation Days |")
    lines.append("|---|---|---|---|---:|")

    hp = top_changes[
        top_changes["Current_Sub_Topic"].isin(
            {
                "Negative General Customer Service",
                "Positive General Customer Service",
                "Bill Inquiry",
                "General Bill",
                "Rep Named Specifically (Positive Mention)",
                "Rep Named Specifically (Negative Mention)",
                "D2D Rep Was Dishonest About Offers / Pricing",
            }
        )
    ]

    for _, r in hp.iterrows():
        lines.append(
            f"| {r['Current_Topic']} | {r['Current_Sub_Topic']} | {r['V5_Reporting_Sub_Topic']} | {r['Change_Type']} | {int(r['Probation_Days'])} |"
        )

    lines.append("")
    lines.append("## Full Mapping")
    lines.append(f"Full mapping is in {OUT_CSV.name}.")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")

    print(f"Created: {OUT_CSV}")
    print(f"Created: {OUT_MD}")
    print(f"Care/All rows mapped: {total}")


if __name__ == "__main__":
    main()
