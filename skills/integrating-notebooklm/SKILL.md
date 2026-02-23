---
name: integrating-notebooklm
description: Uses NotebookLM to research, analyze, and create content while AntiGravity takes action and builds. Use when the user asks to integrate NotebookLM, build automated courses, synthesize research, or create content engines.
version: 1.0.0
tags: [notebooklm, integration, automation, research, content-creation]
---

# The AntiGravity and NotebookLM Integration Master Guide

The Brain + The Builder. NotebookLM researches, analyzes, and creates. AntiGravity takes action, builds, and automates. Together? Unstoppable.

## Workflow

When asked to leverage NotebookLM for building or automating, follow the relevant playbook below to orchestrate NotebookLM tasks (via the NotebookLM MCP tools) and AntiGravity actions.

### 1. Connect Antigravity to NotebookLM (Setup)
If the user hasn't set up the MCP server, ensure you do so using the `mcp_notebooklm_*` tools. You may need to run `notebooklm-mcp-auth` in Bash.

### 2. Learning & Education workflows
#### The 30-Minute Course Creator
1. `research_start` (deep) to fetch 40+ sources on the topic.
2. `source_get_content` to extract key modules as markdown.
3. `video_overview_create` to produce intro videos for each module.
4. `audio_overview_create` for podcast-style audio lessons.
5. `quiz_create` + `flashcards_create` for student assessments.
6. Use AntiGravity bash/code tools to build the course platform + payment interface.

### 3. Business & Agency Workflows
#### Client Onboarding on Autopilot
1. Feed deep research on their industry + competitors to NotebookLM.
2. Generate Video Overview ("Your Industry Landscape"), Infographic (Market opportunity map), Data Table (Competitor comparison), and a Slide Deck (Strategy presentation).
3. Use AntiGravity tools to build a custom client portal containing this data.

#### Weekly Competitor Intelligence
1. Scrape competitor websites and pull YouTube videos/blogs.
2. Feed them into NotebookLM.
3. Generate a trend report and an opportunity heat map infographic.
4. Notify the user via Slack (using Slack MCP).

#### Proposal Generator
1. Research client's industry challenges via NotebookLM tools.
2. Generate case study comparisons and infographics showing the solution.
3. Build a slide deck for the presentation using `slide_deck_create`.
4. Assemble into a branded PDF.

### 4. Content Creation
#### The Content Repurposing Engine
Take one piece of deep research and repurpose it via NotebookLM tools:
- Blog Post (`report_create`)
- YouTube Script (`video_overview_create`)
- Podcast Episode (`audio_overview_create`)
- Infographic (`infographic_create`)
- Slide Deck (`slide_deck_create`)
- Mind Map (`mind_map_create`)

### 5. Research & Analysis
#### Market Research Package
1. Research industry trends, competitors, and pain points into a Notebook.
2. Ask NotebookLM to generate:
   - Market size infographic
   - Competitor comparison table
   - Trend analysis report
   - SWOT mind map
3. Use AntiGravity to build an interactive market dashboard UI.

## Output Formats Reference

### Audio Overview Styles
- `deep_dive`: Comprehensive exploration
- `brief`: Quick summary
- `critique`: Critical analysis
- `debate`: Multiple perspectives

### Video Overview Styles
- `classic`: Professional
- `whiteboard`: Educational
- `kawaii`: Fun/Playful
- `anime`: Engaging
- `watercolor`: Artistic
- `retro_print`: Vintage
- `heritage`: Traditional
- `paper_craft`: Crafty

### Report Formats
- Briefing Doc — Executive summary
- Study Guide — Learning-focused
- Blog Post — Publication-ready
- Create Your Own — Custom format

## Pro Tips
- **Token Savings**: Use `source_get_content` to extract only what you need before querying. 12,000 tokens vs 150,000+ tokens = 10x faster, 10x cheaper.
- **Sync Drive Sources**: Use `source_sync_drive` to keep notebooks updated when source docs change.
- **Match Visual Style to Audience**: kawaii for Gen Z, classic for executives, whiteboard for education.
- **Stack Outputs**: Combine infographic + audio + data table for complete content packages.
