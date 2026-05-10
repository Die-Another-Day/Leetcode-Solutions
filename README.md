<div align="center">

<img src="https://leetcode.com/static/images/LeetCode_logo_rvs.png" width="90" alt="LeetCode"/>

# LeetCode Daily

**One problem. Every day. No excuses.**  
*Solutions auto-tracked via GitHub Actions — zero manual edits.*

---

[![Auto Update](https://img.shields.io/github/actions/workflow/status/YOUR_USERNAME/YOUR_REPO/update_readme.yml?branch=main&style=for-the-badge&logo=githubactions&logoColor=white&label=Auto%20Update&color=22c55e)](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/update_readme.yml)
[![Language](https://img.shields.io/badge/Primary-Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)](https://www.java.com)
[![Last Commit](https://img.shields.io/github/last-commit/YOUR_USERNAME/YOUR_REPO?style=for-the-badge&label=Last%20Solved&color=6366f1)](https://github.com/YOUR_USERNAME/YOUR_REPO/commits/main)
[![License](https://img.shields.io/badge/License-MIT-94a3b8?style=for-the-badge)](LICENSE)

</div>

---

## Table of Contents

- [About](#-about)
- [How Auto-Tracking Works](#-how-auto-tracking-works)
- [Progress Dashboard](#-progress-dashboard)
- [Solution Log](#-solution-log)
- [Repository Structure](#-repository-structure)
- [Problem Format](#-problem-format)
- [Setup Instructions](#-setup-instructions)

---

## 🎯 About

This repository is a **daily commitment** to algorithmic problem solving.  
Every solution is written with clarity and optimal complexity in mind.

| | |
|:--|:--|
| ✅ Clean, well-commented code | ✅ Time & space complexity noted |
| ✅ Approach explanation in each folder | ✅ Auto-indexed the moment you push |

> *"Consistency over intensity — small daily progress compounds into mastery."*

---

## ⚙️ How Auto-Tracking Works

```
You push a new solution
        │
        ▼
GitHub Actions triggers (push to main → problems/**)
        │
        ▼
scripts/update_readme.py scans /problems
        │
        ├── Reads folder name  →  problem number + slug
        ├── Reads inner README →  title, difficulty, topics
        └── Reads file mtime   →  date solved
        │
        ▼
Injects updated dashboard + log between marker comments
        │
        ▼
Auto-commits "📊 chore: auto-update solution log"
```

No manual editing required — ever.

---

## 📊 Progress Dashboard

<!-- DASHBOARD:START -->
| Metric | Count |
|:-------|------:|
| 🟢 Easy   | **0** |
| 🟡 Medium | **0** |
| 🔴 Hard   | **0** |
| ⭐ **Total Solved** | **0** |

**Difficulty distribution:** `────────────────────────────────────────`
> 🟢 Easy · 🟡 Medium · 🔴 Hard
<!-- DASHBOARD:END -->

---

## 📚 Solution Log

<!-- LOG:START -->
| # | Problem | Difficulty | Language | Solution | Date |
|--:|:--------|:----------:|:--------:|:--------:|-----:|
| — | *No solutions yet* | | | | |
<!-- LOG:END -->

---

## 📂 Repository Structure

```
daily-leetcode/
│
├── problems/                        # One folder per problem
│   └── 0001-two-sum/
│       ├── Solution.java            # Optimised solution
│       └── README.md                # Approach & complexity
│
├── scripts/
│   └── update_readme.py             # Auto-tracker script
│
├── .github/
│   └── workflows/
│       └── update_readme.yml        # GitHub Actions pipeline
│
└── README.md                        # This file — auto-updated
```

---

## 📝 Problem Format

Each problem lives in its own folder under `/problems/` using this naming convention:

```
NNNN-problem-slug/
├── Solution.java    ← or .py / .cpp / .ts
└── README.md
```

The inner `README.md` should follow this template so the script can parse it:

````markdown
# Two Sum

**Difficulty:** Easy  
**Topics:** Array, Hash Table  
**LeetCode:** https://leetcode.com/problems/two-sum/

## Approach

Explain your approach here.

## Complexity

| | |
|:--|:--|
| Time  | O(n) |
| Space | O(n) |
````

---

## 🚀 Setup Instructions

### 1 — Fork / clone this repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

### 2 — Update the badge URLs in this README

Replace every `YOUR_USERNAME/YOUR_REPO` with your actual GitHub username and repo name.

### 3 — Ensure Actions has write permission

`Settings → Actions → General → Workflow permissions → Read and write permissions ✅`

### 4 — Add your first solution

```bash
mkdir -p problems/0001-two-sum
# drop in Solution.java + README.md
git add problems/0001-two-sum
git commit -m "✅ 0001 · Two Sum"
git push
```

The workflow fires automatically. The README updates itself within ~30 seconds.

### 5 — (Optional) Run the script locally

```bash
python scripts/update_readme.py
```

---

<div align="center">

Made with consistency &nbsp;·&nbsp; MIT License

</div>
