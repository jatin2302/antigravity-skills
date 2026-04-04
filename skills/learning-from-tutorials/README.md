# Antigravity: learning-from-tutorials

Antigravity learning-from-tutorials skill: Uses NotebookLM to curate and learn from multiple YouTube tutorials. Finds the best source among candidates and extracts deterministic Antigravity skills.

## Install

### Symlink (recommended)

Clone to a fixed location and symlink into your agent's skills directory:

```bash
git clone https://github.com/jatin2302/learning-from-tutorials.git ~/learning-from-tutorials
```

Then link based on your tool:

| Tool | Command |
|---|---|
| **Antigravity** | `ln -s ~/learning-from-tutorials ~/.gemini/antigravity/skills/learning-from-tutorials` |
| **Claude Code** | `ln -s ~/learning-from-tutorials ~/.claude/skills/learning-from-tutorials` |
| **Gemini CLI** | `ln -s ~/learning-from-tutorials ~/.gemini/skills/learning-from-tutorials` |
| **Codex** | `ln -s ~/learning-from-tutorials ~/.codex/skills/learning-from-tutorials` |
| **Cursor** | `ln -s ~/learning-from-tutorials ~/.cursor/skills/learning-from-tutorials` |

### Manual Copy

Copy the `SKILL.md` file into your agent's `skills/learning-from-tutorials/` directory.

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
@learning-from-tutorials
```

## License

[MIT](LICENSE)
