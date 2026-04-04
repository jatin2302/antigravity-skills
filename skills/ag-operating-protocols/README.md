# Antigravity: ag-operating-protocols

Antigravity ag-operating-protocols skill: Master protocol for session lifecycle management. Enforces reading memory at start, running safety/pre-flight gates before major actions, and structuring handoffs at session end.

## Install

### Symlink (recommended)

Clone to a fixed location and symlink into your agent's skills directory:

```bash
git clone https://github.com/jatin2302/ag-operating-protocols.git ~/ag-operating-protocols\n```

Then link based on your tool:

| Tool | Command |
|---|---|
| **Antigravity** | `ln -s ~/ag-operating-protocols ~/.gemini/antigravity/skills/ag-operating-protocols` |
| **Claude Code** | `ln -s ~/ag-operating-protocols ~/.claude/skills/ag-operating-protocols` |
| **Gemini CLI** | `ln -s ~/ag-operating-protocols ~/.gemini/skills/ag-operating-protocols` |
| **Codex** | `ln -s ~/ag-operating-protocols ~/.codex/skills/ag-operating-protocols` |
| **Cursor** | `ln -s ~/ag-operating-protocols ~/.cursor/skills/ag-operating-protocols` |

### Manual Copy

Copy the `SKILL.md` file into your agent's `skills/ag-operating-protocols/` directory.

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
@ag-operating-protocols
```

## License

[MIT](LICENSE)
