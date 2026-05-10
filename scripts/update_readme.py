#!/usr/bin/env python3
"""
update_readme.py
────────────────────────────────────────────────────────────────────
Scans the /problems directory, parses solution metadata, then
injects a live dashboard and solution log into the root README.md.

Markers used in README.md (must be present, never deleted):
  <!-- DASHBOARD:START -->  …  <!-- DASHBOARD:END -->
  <!-- LOG:START -->         …  <!-- LOG:END -->
────────────────────────────────────────────────────────────────────
"""

import os
import re
from datetime import datetime
from pathlib import Path

# ── Paths ────────────────────────────────────────────────────────────
REPO_ROOT    = Path(__file__).resolve().parent.parent
PROBLEMS_DIR = REPO_ROOT / "problems"
README_PATH  = REPO_ROOT / "README.md"

# ── Difficulty display ───────────────────────────────────────────────
DIFFICULTY_LABEL = {
    "easy":   "🟢 Easy",
    "medium": "🟡 Medium",
    "hard":   "🔴 Hard",
}

# ── Solution file extensions (priority order) ────────────────────────
SOLUTION_FILES = ["Solution.java", "solution.java",
                  "Solution.py",   "solution.py",
                  "Solution.cpp",  "solution.cpp",
                  "Solution.ts",   "Solution.js"]


# ────────────────────────────────────────────────────────────────────
# Metadata parser
# ────────────────────────────────────────────────────────────────────
def parse_metadata(folder: Path) -> dict | None:
    """Return a metadata dict for one problem folder, or None if invalid."""
    match = re.match(r"^(\d+)-(.+)$", folder.name)
    if not match:
        return None

    number = int(match.group(1))
    slug   = match.group(2)
    title  = slug.replace("-", " ").title()
    difficulty = "medium"          # default
    language   = "Java"
    sol_file   = None

    # ── Find a solution file ─────────────────────────────────────────
    for name in SOLUTION_FILES:
        candidate = folder / name
        if candidate.exists():
            sol_file = candidate
            ext = candidate.suffix.lower()
            language = {"java": "Java", "py": "Python",
                        "cpp":  "C++",  "ts": "TypeScript",
                        "js":   "JavaScript"}.get(ext.lstrip("."), "Java")
            break

    # ── Date from file mtime, fallback to today ──────────────────────
    if sol_file:
        mtime = os.path.getmtime(sol_file)
        date  = datetime.fromtimestamp(mtime).strftime("%d %b %Y")
        sol_rel = f"./problems/{folder.name}/{sol_file.name}"
    else:
        date    = datetime.now().strftime("%d %b %Y")
        sol_rel = None

    # ── Parse the problem's own README for richer metadata ───────────
    inner_readme = folder / "README.md"
    if inner_readme.exists():
        text = inner_readme.read_text(encoding="utf-8", errors="ignore")

        # Title
        m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
        if m:
            title = m.group(1).strip()

        # Difficulty
        m = re.search(r"\*\*Difficulty:\*\*\s*(Easy|Medium|Hard)", text, re.IGNORECASE)
        if m:
            difficulty = m.group(1).lower()

        # Topics (optional)
        m = re.search(r"\*\*Topics?:\*\*\s*(.+)$", text, re.MULTILINE | re.IGNORECASE)
        topics = m.group(1).strip() if m else ""
    else:
        topics = ""

    return {
        "number":     number,
        "slug":       slug,
        "title":      title,
        "difficulty": difficulty,
        "language":   language,
        "date":       date,
        "sol_rel":    sol_rel,
        "topics":     topics,
    }


# ────────────────────────────────────────────────────────────────────
# Table builders
# ────────────────────────────────────────────────────────────────────
def build_dashboard(problems: list[dict]) -> str:
    easy   = sum(1 for p in problems if p["difficulty"] == "easy")
    medium = sum(1 for p in problems if p["difficulty"] == "medium")
    hard   = sum(1 for p in problems if p["difficulty"] == "hard")
    total  = len(problems)

    # Progress bar (max width = 40 chars)
    bar_width = 40
    if total:
        e_w = round(easy   / total * bar_width)
        m_w = round(medium / total * bar_width)
        h_w = bar_width - e_w - m_w
    else:
        e_w = m_w = h_w = 0

    bar = f"`{'█' * e_w}{'▓' * m_w}{'░' * h_w}`"

    lines = [
        "| Metric | Count |",
        "|:-------|------:|",
        f"| 🟢 Easy   | **{easy}** |",
        f"| 🟡 Medium | **{medium}** |",
        f"| 🔴 Hard   | **{hard}** |",
        f"| ⭐ **Total Solved** | **{total}** |",
        "",
        f"**Difficulty distribution:** {bar}",
        f"> 🟢 Easy &nbsp;·&nbsp; 🟡 Medium &nbsp;·&nbsp; 🔴 Hard",
    ]
    return "\n".join(lines)


def build_solution_log(problems: list[dict]) -> str:
    header = (
        "| # | Problem | Difficulty | Language | Solution | Date |\n"
        "|--:|:--------|:----------:|:--------:|:--------:|-----:|"
    )

    if not problems:
        return header + "\n| — | *No solutions yet* | | | | |"

    rows = [header]
    for idx, p in enumerate(problems, 1):
        lc_url  = f"https://leetcode.com/problems/{p['slug']}/"
        sol_col = f"[View]({p['sol_rel']})" if p["sol_rel"] else "—"
        diff    = DIFFICULTY_LABEL.get(p["difficulty"], p["difficulty"].title())
        rows.append(
            f"| {idx} "
            f"| [{p['title']}]({lc_url}) "
            f"| {diff} "
            f"| {p['language']} "
            f"| {sol_col} "
            f"| {p['date']} |"
        )

    return "\n".join(rows)


# ────────────────────────────────────────────────────────────────────
# README injector
# ────────────────────────────────────────────────────────────────────
def inject_section(content: str, start_marker: str, end_marker: str, new_body: str) -> str:
    """Replace everything between start_marker and end_marker with new_body."""
    pattern = re.compile(
        rf"({re.escape(start_marker)})\n.*?(\n{re.escape(end_marker)})",
        re.DOTALL,
    )
    replacement = rf"\1\n{new_body}\2"
    updated, count = pattern.subn(replacement, content)
    if count == 0:
        raise ValueError(
            f"Marker not found in README: {start_marker!r}\n"
            "Please add both <!-- DASHBOARD:START --> / <!-- DASHBOARD:END --> "
            "and <!-- LOG:START --> / <!-- LOG:END --> to your README.md."
        )
    return updated


# ────────────────────────────────────────────────────────────────────
# Entry point
# ────────────────────────────────────────────────────────────────────
def main() -> None:
    if not PROBLEMS_DIR.exists():
        print(f"[WARN] Problems directory not found: {PROBLEMS_DIR}")
        return

    # ── Collect & sort problems ──────────────────────────────────────
    problems: list[dict] = []
    for folder in sorted(PROBLEMS_DIR.iterdir()):
        if folder.is_dir():
            meta = parse_metadata(folder)
            if meta:
                problems.append(meta)

    problems.sort(key=lambda p: p["number"])
    print(f"[INFO] Found {len(problems)} problem(s).")

    # ── Build content blocks ─────────────────────────────────────────
    dashboard    = build_dashboard(problems)
    solution_log = build_solution_log(problems)

    # ── Read README ──────────────────────────────────────────────────
    if not README_PATH.exists():
        print(f"[ERROR] README not found: {README_PATH}")
        return

    readme = README_PATH.read_text(encoding="utf-8")

    # ── Inject sections ──────────────────────────────────────────────
    try:
        readme = inject_section(readme, "<!-- DASHBOARD:START -->", "<!-- DASHBOARD:END -->", dashboard)
        readme = inject_section(readme, "<!-- LOG:START -->",       "<!-- LOG:END -->",       solution_log)
    except ValueError as exc:
        print(f"[ERROR] {exc}")
        return

    # ── Write back ───────────────────────────────────────────────────
    README_PATH.write_text(readme, encoding="utf-8")
    print("[INFO] README.md updated successfully.")


if __name__ == "__main__":
    main()
