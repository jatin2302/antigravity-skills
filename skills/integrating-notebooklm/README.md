# Antigravity: integrating-notebooklm

Antigravity integrating-notebooklm skill: Uses NotebookLM to research, analyze, and create content while AntiGravity takes action and builds. Use when the user asks to integrate NotebookLM, build automated courses, synthesize research, or create content engines.

## Install

### Symlink (recommended)

Clone to a fixed location and symlink into your agent's skills directory:

```bash
git clone https://github.com/jatin2302/integrating-notebooklm.git ~/integrating-notebooklm
```

Then link based on your tool:

| Tool | Command |
|---|---|
| **Antigravity** | `ln -s ~/integrating-notebooklm ~/.gemini/antigravity/skills/integrating-notebooklm` |
| **Claude Code** | `ln -s ~/integrating-notebooklm ~/.claude/skills/integrating-notebooklm` |
| **Gemini CLI** | `ln -s ~/integrating-notebooklm ~/.gemini/skills/integrating-notebooklm` |
| **Codex** | `ln -s ~/integrating-notebooklm ~/.codex/skills/integrating-notebooklm` |
| **Cursor** | `ln -s ~/integrating-notebooklm ~/.cursor/skills/integrating-notebooklm` |

### Manual Copy

Copy the `SKILL.md` file into your agent's `skills/integrating-notebooklm/` directory.

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
@integrating-notebooklm
```

## License

[MIT](LICENSE)
