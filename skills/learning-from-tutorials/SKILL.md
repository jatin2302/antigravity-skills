---
name: learning-from-tutorials
description: Uses NotebookLM to curate and learn from multiple YouTube tutorials. Finds the best source among candidates and extracts deterministic Antigravity skills.
version: 1.2.0
tags: [youtube, learning, notebooklm, curation, automation]
---
metadata:
  author: jatinbhutani
  version: "1.0"
license: MIT
---

# Learning From Tutorials (NotebookLM Curation)

This skill leverages NotebookLM as a curation and synthesis engine. Instead of picking one video blindly, it ingests multiple candidates and uses AI to identify the "Best-in-Class" walkthrough.

## When to use this skill
- Triggered by "learn [task] from youtube".
- Use when you want to find the most optimal way to perform a workflow by comparing multiple tutorial sources.

## 🛠 Workflow (The Curation System)

### 1. Discovery (YouTube)
- Use `YOUTUBE_SEARCH_YOU_TUBE` to find the top 3-5 tutorials for the requested task.
- Target videos with high engagement or titles that suggest a "Masterclass" or "Complete Guide".

### 2. Curation (NotebookLM Ingestion)
- Create a new research notebook or use an existing learning notebook.
- **Add all candidate URLs** to the notebook via `mcp_notebooklm_source_add`.
- Wait for indexing to complete.

### 3. Selection & Extraction (NotebookLM Query)
- Use `mcp_notebooklm_notebook_query` to identify the best source:
  - *"Compare the provided YouTube tutorials for [TASK]. Identify which one provides the most clear, step-by-step, and technically accurate instructions for an AI agent to follow."*
- Extract the deterministic skill logic from the selected source:
  - *"Using the best source identified, generate a step-by-step technical workflow for [TASK]. Include all necessary commands, logic gates, and required tools."*

### 4. Skill Production
- Translate the extracted workflow into the standard `ag-skill-creator` template.
- Save to `skills/[gerund-name]/SKILL.md` and sync to `~/GitHub/antigravity-skills/`.

## 📋 Pre-Flight Checklist
- [ ] At least 3 candidate tutorials searched?
- [ ] All candidates added to NotebookLM?
- [ ] NotebookLM used to rank and select the best source?
- [ ] Final skill follows Antigravity Gerund naming conventions?

## Resources
- [integrating-notebooklm skill](file:///Users/jatinbhutani/MEGA/Projects/03_Resources/AG%20improvements/_agent/skills/integrating-notebooklm/SKILL.md)
