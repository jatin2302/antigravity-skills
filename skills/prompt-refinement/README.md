# Antigravity: prompt-refinement

Antigravity prompt-refinement skill: Critiques and expands the user's initial prompt into a highly detailed, professional prompt, forcing the creation of an in-depth research and execution plan before any active tool use.

## Install

### Symlink (recommended)

Clone to a fixed location and symlink into your agent's skills directory:

```bash
git clone https://github.com/jatin2302/prompt-refinement.git ~/prompt-refinement
```

Then link based on your tool:

| Tool | Command |
|---|---|
| **Antigravity** | `ln -s ~/prompt-refinement ~/.gemini/antigravity/skills/prompt-refinement` |
| **Claude Code** | `ln -s ~/prompt-refinement ~/.claude/skills/prompt-refinement` |
| **Gemini CLI** | `ln -s ~/prompt-refinement ~/.gemini/skills/prompt-refinement` |
| **Codex** | `ln -s ~/prompt-refinement ~/.codex/skills/prompt-refinement` |
| **Cursor** | `ln -s ~/prompt-refinement ~/.cursor/skills/prompt-refinement` |

### Manual Copy

Copy the `SKILL.md` file into your agent's `skills/prompt-refinement/` directory.

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
@prompt-refinement
```

## License

[MIT](LICENSE)
