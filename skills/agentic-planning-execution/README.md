# Agentic Planning & Execution

A framework for AI coding agents to plan, track, and execute complex multi-step tasks that extend beyond a single context window.

## What It Does

- **File-based planning** — treats the filesystem as persistent working memory (Manus-style).
- **TDD-driven task specs** — breaks work into bite-sized, testable implementation steps.
- **Batch execution** — processes tasks in reviewable batches with checkpoint tracking.
- **3-Strike Error Protocol** — structured escalation when things go wrong.

## Install

### Symlink (recommended)

Clone to a fixed location and symlink into your agent's skills directory:

```bash
git clone https://github.com/jatinbhutani/agentic-planning-execution.git ~/agentic-planning-execution
```

Then link based on your tool:

| Tool | Command |
|---|---|
| **Antigravity** | `ln -s ~/agentic-planning-execution ~/.gemini/antigravity/skills/agentic-planning-execution` |
| **Claude Code** | `ln -s ~/agentic-planning-execution ~/.claude/skills/agentic-planning-execution` |
| **Gemini CLI** | `ln -s ~/agentic-planning-execution ~/.gemini/skills/agentic-planning-execution` |
| **Codex** | `ln -s ~/agentic-planning-execution ~/.codex/skills/agentic-planning-execution` |
| **Cursor** | `ln -s ~/agentic-planning-execution ~/.cursor/skills/agentic-planning-execution` |

### Manual Copy

Copy the `SKILL.md` file into your agent's `skills/agentic-planning-execution/` directory.

## Compatibility

| Agent | Support |
|---|---|
| Antigravity | ✅ Full |
| Claude Code | ✅ Full |
| Gemini CLI | ✅ Full |
| Codex | ✅ Full |
| Cursor | ✅ Full |
| Windsurf | ✅ Full |
| OpenCode | ✅ Full |
| GitHub Copilot | ⚠️ Partial |

## Usage

Reference the skill in your prompt or invoke it by name:

```
@agentic-planning-execution Build a REST API with auth, rate limiting, and tests.
```

The agent will create `task_plan.md`, break the work into TDD tasks, and execute in batches.

## License

[MIT](LICENSE)
