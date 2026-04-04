---
name: prompt-refinement
description: Critiques and expands the user's initial prompt into a highly detailed, professional prompt, forcing the creation of an in-depth research and execution plan before any active tool use.
license: MIT
---
metadata:
  author: jatinbhutani
  version: "1.0"
license: MIT
---

# Prompt Refinement & Deep Research Planning

**AG Global Meta-Skill**

This skill serves as a forced pause to ensure maximum leverage on complex requests. Before writing any code or modifying any files, AG must rigorously refine the user's raw prompt and construct a massive, failure-proof research and execution plan.

## 1. The Trigger
Invoke this skill when:
- The user asks for a "workflow or skill for prompt refinement".
- The user provides a vague or massive prompt (e.g., "Build a full stack SaaS app").
- The user explicitly requests "deep research" or "superior prompt refinement".

## 2. Phase 1: Prompt Critique & Refinement
Do NOT start working on the task yet. First, output a **Prompt Refinement Block** for the user to review. 

**Format:**
```markdown
# 🔍 Prompt Refinement & Critique

## Your Original Request
[Summarize user's raw prompt]

## AG's Critique (The Weak Points)
- [Identify vague requirements]
- [Identify missing technical constraints]
- [Identify potential failure points]

## The Superior Refined Prompt
[A highly detailed, production-ready, bulleted prompt that AG will ACTUALLY use to execute the task. This should be 3-5x longer and more specific than the original prompt.]

## Clarifying Questions (Optional)
- [Any final questions before execution begins]
```

## 3. Phase 2: In-Depth Research Plan
Once the prompt is refined, build an **In-Depth Research & Execution Plan**. AG must investigate existing code, system limits, and KIs (Knowledge Items) before executing.

**Create or update `task_plan.md`:**
1. **Phase 1: Deep Research** (List specific files, directories, and dependencies to read/search).
2. **Phase 2: Draft Architecture / Strategy** (How we will solve the problem based on research).
3. **Phase 3: Execution Steps** (Granular, step-by-step TDD tasks).
4. **Phase 4: Verification** (How we prove it works).

## 4. Anti-Patterns
- **Don't** immediately start writing code after a vague user prompt. Stop and refine.
- **Don't** rush the research phase. Take the time to read the existing codebase architecture.
- **Don't** assume standard best practices apply; check `gemini.md` and `/knowledge` KIs first.
