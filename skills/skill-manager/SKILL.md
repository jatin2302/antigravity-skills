---
name: skill-manager
description: Decide whether to install, bookmark, or skip a discovered skill. Prevents token bloat from unnecessary installs.
---

# skill-manager

When a new skill or tool is discovered, run this decision tree **before** installing anything.

## Step 1 — Classify Tier

Ask the user: **"Will I use this weekly?"**

| Answer | Tier | Action |
|---|---|---|
| **Yes, weekly+** | Tier 1 — Install | Install to (1) AG skill folder → (2) GitHub skills repo → (3) NotebookLM |
| **Sometimes** | Tier 2 — On-Demand | Save SKILL.md URL to `Global_Resources.md` with tag `on-demand`. Read URL fresh at runtime when needed |
| **Maybe someday** | Tier 3 — Reference | Save catalog/repo URL to `Global_Resources.md` only. Pull individual skills from it later |

## Step 2 — On-Demand Retrieval (Tier 2)

When user says "use [skill] from Global Resources":

1. Use `grep_search` on `Global_Resources.md` for the skill name
2. Use `read_url_content` or `view_file` on the SKILL.md URL/Path from the matched row
3. Follow the SKILL.md instructions for that session only

## Step 3 — Quarterly Audit

Count installed skills:
Run `ls ~/.gemini/antigravity/skills/ | wc -l` using `run_command`

Flag any installed skill unused in 3+ months → demote to Tier 2 (archive URL, delete local SKILL.md after user confirmation).
