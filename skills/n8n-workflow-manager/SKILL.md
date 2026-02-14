---
name: n8n-workflow-manager
description: Manage n8n workflows, nodes, and credentials. Export, import, and version control your automations.
---

# n8n Workflow Manager

A set of utilities to help you manage your n8n instances, ensuring your automations are versioned, backed up, and easily deployable.

## When to Use This Skill
- Backing up all workflows from an n8n instance to local JSON files.
- version controlling your n8n workflows in Git.
- Validating workflow JSON structure.
- Migrating workflows between dev and prod instances.
- searching for specific nodes or credentials usage across all workflows.

## Features
1. **Bulk Export**: Download all workflows from your n8n instance API.
2. **Git Sync**: Commit workflow changes to a repository.
3. **Usage Analysis**: Find which workflows use specific nodes (e.g., "Where am I using the Google Sheets node?").
4. **Credential Audit**: List workflows that have missing or invalid credentials.

## Setup
(Instructions on how to authenticate with your n8n instance would go here, e.g., using `N8N_API_KEY` and `N8N_URL` environment variables)

## Usage
- "Export all my n8n workflows to the `workflows/` directory."
- "Find all workflows using the `Postgres` node."
- "Check if any workflows are active but haven't run in 30 days."

## Resources
- [n8n API Documentation](https://docs.n8n.io/api/)
