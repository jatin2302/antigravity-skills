---
name: business-context
description: Enforces reading Business Brain.md before making product, copy, or logic decisions to ensure alignment.
---

# Business Context Skill

## When to use this skill
- When starting any task involving marketing copy, UI/UX design, or product architecture.
- When you are asked to generate text, emails, or pages that will be read by the user's customers.
- When you need to make decisions about the target audience, brand tone, or business strategy.
- When creating courses, automated funnels, client onboarding portals, or combining NotebookLM with AntiGravity workflows.
- During any planning phase where the project touches the user's "Machine" (the funnel/product) or represents the "Maker" (the founder/brand).

## Instructions

### 1. Locate the Blueprint
Before taking any action or generating plans, immediately locate and read `Business Brain.md` in the current project or workspace (or the NotebookLM space if provided).

### 2. Internalize the Identity
Read the file with the Operator Mindset. Extract and hold the following in your context memory for the duration of the task:
- **The Machine:** The specific target customer demographics, the top 3 pain points, the exact customer journey steps, and the metric focus.
- **The Maker:** The founder's credibility markers, the unique edge/angle of the brand, and the sophistication level (Beginner/Intermediate/Advanced) of the audience.

### 3. Execution Invariants
- **No Generic Output:** NEVER generate generic copy or standard SaaS boilerplate. Every piece of copy, design, or logic must uniquely map to the "Pain Points" and "Edge" defined in the Business Brain.
- **Tone & Sophistication:** Calibrate your output to the specific "Audience Awareness" level. Do not speak down to an Advanced audience, and do not use overly complex jargon for a Beginner audience.
- **No Hallucinations:** You must use the exact credibility markers and origin stories provided. Do not invent business details. If a crucial detail is missing from `Business Brain.md`, use `notify_user` to ask the operator.

### 4. Verification Setup
Before delivering any final code, artifact, or text, self-cross-reference your work:
- Does this solve one of the top 3 pain points?
- Does it fit logically into the defined Customer Journey?
- Does it project the defined Credibility and Edge?
If "No" to any of the above, revise it before presenting it to the user.
