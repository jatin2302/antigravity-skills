# Antigravity Skills Synchronization Documentation

This document explains the architecture and tools used to manage and synchronize Claude Skills across three key locations: GitHub, Internal Agent Storage, and NotebookLM.

## 1. The Triad Architecture

To ensure skills are always available and up-to-date, we maintain them in three places:

1.  **Git Repository (Source of Truth)**
    -   **Location:** `/Users/jatinbhutani/Documents/GitHub/antigravity-skills/skills`
    -   **Purpose:** Permanent storage, version control (Git), and human-readable browsing. All new skills should be added here first.

2.  **Internal Agent Folder (Operational)**
    -   **Location:** `~/.gemini/antigravity/skills`
    -   **Purpose:** This is where the AI agent looks for skills to execute. If a skill isn't here, the agent might not "know" it exists during execution.

3.  **NotebookLM (Knowledge Base)**
    -   **Notebook:** "Awesome Claude Skills Inventory"
    -   **Purpose:** Smart search and "chatting with your skills." Allows you to ask questions like "Find me a tool for SEO" and get a cited answer from the inventory.

## 2. Categorization Strategy

We have moved away from a single massive list to **Categorized Inventories**. The script `categorize_and_sync.py` analyzes the description of every skill and sorts it into buckets:

-   **Productivity & Collaboration:** Task managers, calendars, Notion, Jira, etc.
-   **Development & IT:** Git, Cloud, Docker, APIs.
-   **Marketing & SEO:** Email marketing, Social media automation, SEO tools.
-   **CRM & Sales:** HubSpot, Salesforce, lead generation.
-   **Data & Analytics:** Scraping, visualization, reporting.
-   **Content & Media:** Video/Image editing, CMS.
-   **Finance & Accounting:** Invoicing, payments.
-   **HR & Admin:** Recruitment, payroll.
-   **Other Tools & Utilities:** Everything else.

These categories exist as separate Markdown files in `Categorized_Inventories/` and are uploaded as distinct sources to NotebookLM.

## 3. How to Sync Skills

We have created several utility scripts to manage this process. They are located in this folder (`template/`).

### `sync_skills_triad.py`
**The Master Sync Script.**
Run this to synchronize everything.
```bash
python3 sync_skills_triad.py
```
**What it does:**
1.  Copies all skills from **Git** -> **Internal Agent Folder**.
2.  (Placeholder) Identifies new skills to be uploaded to NotebookLM.

### `categorize_and_sync.py`
**The Organizer.**
Run this if you have added many new skills and want to regenerate the inventory files.
```bash
python3 categorize_and_sync.py
```
**What it does:**
1.  Scans all 1000+ skills in the Git folder.
2.  Reads their `SKILL.md` metadata (name, description).
3.  Categorizes them based on keywords.
4.  Generates the Markdown inventory files in `Categorized_Inventories/`.
5.  Syncs the Master Inventory to the main `SKILL_INVENTORY.md` in the skills folder.
6.  Also performs a sync to the Internal Agent Folder.

### `import_skills.py`
**The Importer.**
Used to bulk-import skills from the `awesome-claude-skills` repository.
```bash
python3 import_skills.py
```

## 4. Workflows

### Adding a New Skill
1.  Create the skill folder in `/Users/jatinbhutani/Documents/GitHub/antigravity-skills/skills/my-new-skill`.
2.  Add a `SKILL.md` file with the standard frontmatter.
3.  Run `python3 sync_skills_triad.py` to make it available to the agent.
4.  (Optional) Run `python3 categorize_and_sync.py` to update the markdown inventories.

### Updating NotebookLM
Currently, `categorize_and_sync.py` generates the files, but uploading to NotebookLM is handled via the AI agent (using the `mcp_notebooklm` tool).
To update NotebookLM:
1.  Ask the agent: *"Sync my categorized inventories to NotebookLM."*
2.  The agent will read the files from `Categorized_Inventories/` and push them to the notebook.

## 5. Directory Structure

```
antigravity-skills/
├── skills/                     # The Source of Truth (1000+ folders)
│   ├── SKILL_INVENTORY.md      # Master list
│   └── ... (skill folders)
├── template/
│   ├── Categorized_Inventories/ # Generated markdown files for NotebookLM
│   ├── sync_skills_triad.py     # Main sync script
│   ├── categorize_and_sync.py   # Inventory generator
│   └── SKILL_SYNC_DOCUMENTATION.md # This file
└── ...
```
