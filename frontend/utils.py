from typing import Any

def render_jha_md(jha: dict[str, Any]) -> str:
    jd = jha["job_data"]
    lines = [
        f"# Job Hazard Analysis: {jd['job_name']}\n",
        f"**Date:** {jd['job_date']}\n",
        f"**Location:** {jd['job_location']}\n",
        f"**Site Conditions:** {jd['site_conditions']}",
        "",
        "---",
        "## Weather",
        *[f"- {w}" for w in jha.get("weather", [])],
        "---",
        "## Site Hazards",
        *[f"- {h}" for h in jha.get("site_hazards", [])],
        "",
        "## Site Control Measures",
        *[f"- {m}" for m in jha.get("site_control_measures", [])],
        "",
        "## PPE",
        *[f"- {p}" for p in jha.get("site_ppe", [])],
        "---",
        "## Tasks",
    ]
    for t in jha.get("jha_tasks", []):
        lines += [
            f"### {t['task_name']}",
            f"{t['task_description']}",
            "",
            "**Hazards**",
            *[f"- {h}" for h in t.get("task_hazards", [])],
            "",
            "**Control Measures**",
            *[f"- {c}" for c in t.get("task_control_measures", [])],
            "",
            "**PPE**",
            *[f"- {p}" for p in t.get("task_ppe", [])],  # typo fixed below
            "",
        ]
    return "\n".join(lines)
