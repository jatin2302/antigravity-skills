---
name: agentic-planning-execution
description: Comprehensive framework for Manus-style file-based planning, writing TDD-based implementation specs, and batch-executing complex tasks across sessions.
license: MIT
metadata:
  author: jatinbhutani
  version: "1.0"
---

# Agentic Planning & Execution Framework

A meta-skill that unifies how AI coding agents plan, track, and execute multi-step tasks extending beyond a single context window or requiring 5+ tool calls.

## Core Principle — Working Memory on Disk

```
Context Window = RAM  (volatile, limited)
Filesystem     = Disk (persistent, unlimited)
```

Never start a complex task without creating the planning files. Everything important gets written to disk.

## 1. The Planning Phase

### Planning Files

| File | Purpose |
|---|---|
| `task_plan.md` | TDD-driven implementation spec with bite-sized tasks |
| `findings.md` | Discoveries, blockers, and research notes |
| `progress.md` | Session handoff state and next actions |

### Writing the Implementation Spec (`task_plan.md`)

Write plans assuming the executing agent has **zero context** for the codebase. Give them the whole plan as bite-sized, TDD-driven tasks (2-5 mins each).

**Format for a Task Step:**

```markdown
### Task N: [Component Name]
**Files:**
- Create: `exact/path/to/file.py`

**Step 1: Write failing test**
[Code block for test]

**Step 2: Run test to verify it fails**
Run: `pytest tests/path/test.py` -> Expected: FAIL

**Step 3: Write minimal implementation**
[Code block for feature]

**Step 4: Verify it passes & Commit**
```

## 2. The Execution Phase

When executing a written plan, operate in batches to allow for human (or self) review.

**Protocol:**
1. Read `task_plan.md` critically. Identify gaps.
2. Execute tasks in batches (default: 3 tasks at a time).
3. Mark each task as `[x]` (completed) or `[/]` (in progress) in the plan.
4. Stop executing immediately when hitting a blocker, missing dependency, or failing test. Output the specific error and ask for guidance.

### The 3-Strike Error Protocol (During Execution)

1. **ATTEMPT 1:** Diagnose & Fix the exact error.
2. **ATTEMPT 2:** Try a different method/tool. NEVER repeat the exact same failing action.
3. **ATTEMPT 3:** Broader rethink. Update the plan.
4. **AFTER 3 FAILURES:** Escalate to User.

## Anti-Patterns

- **Don't** start executing code on complex features without making `task_plan.md` first.
- **Don't** repeat failed actions silently. Use the 3-Strike Protocol.
- **Don't** stuff discoveries into context RAM forever. Save to `findings.md`.
- **Don't** keep running code if the TDD spec fails. Stop and fix/ask.
