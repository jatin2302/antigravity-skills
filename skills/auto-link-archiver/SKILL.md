---
name: Auto Link Archiver
description: Silently extracts high-value links, tools, and repositories encountered during active project execution and archives them to the global resource database.
---

# Auto Link Archiver Protocol

## Objective
To autonomously capture and categorize high-value resources (URLs, documentation, tools, repositories) mentioned or discovered during a session, appending them to a centralized database without interrupting the user.

## Execution Rules
1. **Trigger:** Whenever you (Antigravity) encounter, synthesize, or output a highly useful URL, tool name + link, or official documentation reference that is contextually valuable for future lookup.
2. **Local Archival:** Silently append the resource to the database at `/Users/jatinbhutani/Mega/Projects/03_Resources/Global_Resources.md`.
3. **NotebookLM Sync:** Immediately use `mcp_notebooklm_notebook_add_text` to upload the exact same link and description as a new text source to the NotebookLM notebook "Global Resources Database" (ID: `c4f9b3f9-e31f-48a0-8fc5-439002f1bdf0`).
4. **Format:** For the local file, you MUST append to the existing Markdown table using the exact format:
   `| YYYY-MM-DD | [Context/Project] | [Brief Description] | [URL] | #tag1 #tag2 |`
5. **Constraint:** DO NOT ask the user for permission. DO NOT notify the user that you saved the link unless specifically asked. Do local file updates via `run_command` and `echo`.
6. **Retrieval:** If the user asks for a past resource, use `grep_search` on the `Global_Resources.md` file.

## What Constitutes a "High-Value" Resource?
- Official API documentation links.
- GitHub repositories for useful libraries.
- Articles or tutorials solving specific architectural problems.
- SaaS tools or platforms relevant to the user's stack.
- Competitor links or strategic references.
