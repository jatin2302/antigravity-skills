---
name: token-hygiene-and-skills
description: Surgical editing protocols to minimize token usage and prevent context bloat. Enforces use of local skills and specific tool selection logic.
version: 1.0.5
---

# Token Hygiene & Skill Management

A protocol for maintaining a lean, high-ROI context window by strictly controlling file edits and skill installations.

## 1. Surgical Edits (The Replacement Rule)
- **NEVER** use `write_to_file` to overwrite an entire existing file with 100+ lines.
- **ALWAYS** use `replace_file_content` or `multi_replace_file_content` for surgical, precise changes.
- If you must create a new version of a file, use the `/tmp/` directory for staging before finalizing.

## 2. Skill Management
- **Local Skills Only:** Antigravity must primarily use skills from the local `_agent/skills/` directory.
- **Zero Global Install:** Never install new skills directly to the global `~/.gemini/antigravity/skills/` directory during a project session.
- **Syncing:** New project-specific skills are created in the local `_agent/skills/` and then synced to the `antigravity-skills` monorepo at session end.

## 3. Tool Selection Logic
Before using any tool, AG must ask:
- *Is there an MCP tool that can do this faster?*
- *Is this tool call actually necessary for the NEXT step in `task_plan.md`?*
- *Can I combine multiple operations into a single tool call (e.g. `multi_replace`)?*

## 4. Context Cleaning
- Periodically summarize long conversation histories into a single "State Memo" and ask the user to start a new thread if token count exceeds 30k.
- Use `ls` sparingly on large directories; prefer targeted `grep` searches.
