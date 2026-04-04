---
name: continuous-improvement-protocol
description: After each project or major epic, logs what worked, extracts reusable domain knowledge into KIs, and updates invariant rules to prevent repeated mistakes.
version: 1.1.0
---

# Continuous Improvement Protocol

This skill ensures that every project contributes to the long-term intelligence of the AI agent. It transforms temporary project successes into permanent system improvements.

## 🛠 Workflow

### 1. The Retrospective (After every major task/epic)
- Create or update `_agent/findings.md`.
- **What worked?** (Specific tools, prompts, or architectures that were highly effective).
- **What failed?** (Blockers, bugs, or inefficient approaches).
- **The "Why"?** (Root cause analysis of successes and failures).

### 2. Knowledge Extraction (Creating KIs)
- If a new pattern or deep domain knowledge was discovered, create a new Knowledge Item (KI) in `~/.gemini/antigravity/knowledge/[topic]/`.
- A KI must include:
    - `metadata.json`: Summary, tags, and references.
    - `artifacts/`: The actual code snippets, diagrams, or documentation.

### 3. Rule Invariance (Updating GLOBAL_RULES)
- If a specific error was repeated 3+ times, or a new "Must-Follow" rule is identified, update `~/GitHub/antigravity-skills/base/AG_setup/GLOBAL_RULES.md`.
- Rules must be concise, punchy, and execution-oriented.

## 📋 Retro Checklist
- [ ] Findings logged to `_agent/findings.md`?
- [ ] Any unique logic extracted to a new KI?
- [ ] Global rules updated if a systemic failure occurred?
- [ ] Task as a whole marked as COMPLETED in `projects_overview.md`?
