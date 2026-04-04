# 🌐 Antigravity Skills & Protocols (Monorepo)

Central repository for all Antigravity agent skills, operating protocols, and base configurations. This monorepo serves as the single source of truth for the Antigravity ecosystem.

## 🏗 Directory Structure

```text
.
├── base/                   # Core configurations and operating rules
│   └── AG_setup/           # Global rules (V7) and environment logic
│
├── skills/                 # Modular agent skills (meta-skills)
│   ├── ag-operating-protocols      # Session lifecycle & pre-flight gates
│   ├── agentic-planning-execution  # TDD specs & 3-strike execution
│   ├── api-orchestrator           # External service orchestration
│   ├── continuous-improvement     # Retro → KI extraction logic
│   ├── integrating-notebooklm     # Brain-Builder synchronization
│   ├── learning-from-tutorials    # YouTube curation via NotebookLM
│   ├── prompt-refinement          # Critique & recursive expansion
│   └── token-hygiene-and-skills   # Context optimization & surgical edits
│
└── skills_index.json       # Central registry for skill discovery
```

## 🚀 Installation & Sync

To use a skill in a local project:

1. Clone this monorepo:
   ```bash
   git clone https://github.com/jatin2302/antigravity-skills.git ~/GitHub/antigravity-skills
   ```

2. Link specific skills to your agent's local directory:
   ```bash
   ln -s ~/GitHub/antigravity-skills/skills/agentic-planning-execution ~/.gemini/antigravity/skills/
   ```

## 🔄 Updating Protocols

1. Edits to `base/AG_setup/GLOBAL_RULES.md` propagate to all new project instances via the `/new-project-setup` workflow.
2. New skills should be added to the `skills/` directory and registered in `skills_index.json`.

## 🛡 License
[MIT](LICENSE)
