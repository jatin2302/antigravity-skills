---
name: python-scripting
description: Best practices, snippets, and tools for writing and executing Python scripts inside the agentic environment. Use when scripting data processing, file handling, or automation logic.
version: 1.0.0
tags: [python, scripting, automation, development]
---

# Python Scripting

Provides guidelines and standard procedures for writing Python scripts.

## Workflow
1. Identify the inputs and outputs needed for the script.
2. Standardize execution using Python 3 native modules (like `os`, `sys`, `re`, `json`) to avoid external dependencies where possible.
3. If external dependencies are required, generate a `requirements.txt` file simultaneously.
4. Always wrap execution blocks in `if __name__ == "__main__":` to allow modular importing.
5. Print clean, parseable output to stdout so the agent can easily read the script's results via terminal tools.

## Instructions
- Prefer `pathlib` or `os.path` for path handling to ensure cross-platform compatibility (although macOS is the primary target here).
- Use `argparse` if parameter passing is necessary for complex scripts.
- Log errors to `stderr` and expected text to `stdout`.

## Resources
- N/A
