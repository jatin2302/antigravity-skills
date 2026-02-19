---
name: mcp-google-sheets
description: Official-style community MCP server for Google Sheets integration. Allows reading, writing, and managing spreadsheets via Service Account.
---

# Google Sheets MCP

This skill uses the `mcp-google-sheets` MCP server to interact with Google Sheets.
It is configured in `claude_desktop_config.json` and runs via `npx`.

## Prerequisite
- The server authentication is handled via `GOOGLE_APPLICATION_CREDENTIALS` pointing to a Service Account JSON key.
- The Service Account must be an **Editor** on the specific Google Sheets you want to access.
- You **MUST** share any target spreadsheet with the Service Account email address found in the JSON key file.

## Capabilities
The server provides tools to:
1. **Read Data**: Read rows or cells from a sheet.
2. **Write Data**: Append rows or update cells.
3. **Manage Sheets**: Create new spreadsheets or tabs.
4. **Formatting**: Apply cell formatting (if supported).

## Usage
When using this skill, simply ask Claude to perform actions on your Google Sheets.
Example prompts:
- "Read the first 10 rows of spreadsheet [ID]"
- "Append a new row to the 'Leads' tab with values [A, B, C]"
- "Create a new spreadsheet looking for leads"

## Troubleshooting
- If tools fail with "Permission Denied", check if the Service Account email is added as an Editor to the Sheet.
- If tools fail with "Credentials missing", verify `claude_desktop_config.json` path.
