# Antigravity Skills Architecture & Design Principles

This document outlines the architectural principles, directory structure, and design patterns for the Antigravity Skills repository. It builds upon modern LLM plugin architectural best practices while adapting them for the Antigravity (AG) scale and ecosystem.

## Core Philosophy

### Single Responsibility & Progressive Disclosure
- **One Skill, One Job**: Each folder in the `skills` directory handles exactly one workflow, external integration, or specific structural capability. 
- **Context Efficiency**: Instead of massive monolithic prompts, skills are designed to load only the required context when activated, ensuring optimal LLM token usage and maintaining high precision.
- **Deep Context via Sub-files**: Complex skills use additional sub-files (e.g., `scripts/`, `examples/`) that are only accessed dynamically when deep work is necessary.

### Automated Maintenance & Scalability
- **Script-Driven Organization**: The repository maintains 1,000+ skills dynamically. It relies on automated scripts (e.g., `reorganize_inventory.py`, `generate_notebook_files.py`) rather than fully manual grouping.
- **NotebookLM Integration**: Skills are automatically chunked into `notebooks/` by domain, allowing them to be ingested into Google NotebookLM for retrieval-augmented generation (RAG) at run-time without polluting context windows.

## Repository Structure (Proposed/Hybrid)

```text
antigravity-skills/
├── .ag-registry/                # Automated outputs (optional JSON state)
├── skills/                      # Master Directory of Skills
│   ├── development/             # Example categorized architecture (Optional future state)
│   │   ├── react-best-practices/
│   │   └── mcp-builder/
│   ├── automation/              # Over 600+ Composio MCP stubs
│   │   ├── github-automation/
│   │   └── slack-automation/
│   └── [1000+ Flat Folders]     # Current State: Flat folder of skills
├── workflows/                   # Multi-skill orchestrators / Slash commands
│   ├── client-onboarding.md
│   └── new-project-setup.md
├── scripts/                     # Automation for maintaining the repository
│   ├── reorganize_inventory.py
│   ├── generate_notebook_files.py
│   ├── audit_skills.py
│   └── sync-skills.sh
├── notebooks/                   # Auto-generated categorized markdown for NotebookLM
│   ├── development_&_it.md
│   ├── automation_&_integration.md
│   └── (others...).md
├── docs/                        # Internal documentation
│   └── architecture.md          # This file
└── SKILL_INVENTORY.md           # Master readable list categorized by domains
```

## Structure vs. Good Practices analyzed from Reference Architecture
Comparing our setup against strict hierarchical plugin architectures (like `claude-agents`), here is what we do well and where we can improve:

### What We Do Well (The Good)
1. **Composio Automation Scale**: Our repository scales horizontally exceptionally well with 1,000+ skills (over half being precise tool connectors like `notion-automation`).
2. **NotebookLM Grounding**: By explicitly generating grouped markdown files (`notebooks/`), we feed a semantic search system directly, maintaining lower context latency than the reference architecture's strategy.
3. **Task-Specific Tooling**: By avoiding bundled monoliths, when the agent invokes `mcp-builder`, it gets purely MCP-related guidance.

### Architectural Improvements & Roadmap
1. **Hierarchical Refactoring of `skills/`**: Currently, `skills/` operates as a massive flat array of 1000+ folders. 
   - *Improvement*: Group the nested folders into domain-driven structures (e.g. `skills/development/`, `skills/marketing/`, `skills/automation/`) matching our `SKILL_INVENTORY.md`. This makes manual navigation drastically faster and logically isolates domains.
2. **Standardized Entrypoints**: Every skill must have a uniform `SKILL.md` file format utilizing explicit YAML frontmatter (`name:`, `description:`, `triggers:`).
3. **Workflow Native Layer**: Differentiate between "Abilities" (Skills) and "Orchestrators" (Workflows/Commands). Our `workflows/` directory clearly separates how to *execute* processes (like `/client-onboarding`) from the raw ingredients (Skills).
4. **Agent + Skill Composition**: Instead of just having a skill file, complex tasks should include a `task.md` or a `template` inside the skill to act as a structured framework when invoked.

## Skill Anatomy

A standard skill package in `skills/` must include a primary `.md` entry point:

```text
skills/[skill-name]/
├── SKILL.md              # The primary instruction file with YAML frontmatter
├── scripts/              # Optional auxiliary scripts or automation tools
└── examples/             # Optional context to feed the logic
```

### Writing a Good `SKILL.md`
- **Frontmatter**: Include name, description, and strict conditions for invocation.
- **Rules/Principles**: Define what NOT to do.
- **Workflow Steps**: Define the sequence of actions if the skill implies a process.
- **Related Tools**: Recommend core files or tools to load.

## Automated Updating Routine
Whenever new folders (skills) are added or removed, `skills/scripts/sync-skills.sh` should be executed. This:
1. Re-indexes `SKILL_INVENTORY.md` 
2. Organizes them into logical category tables
3. Regenerates the `notebooks/` directory for fresh NotebookLM uploads.
