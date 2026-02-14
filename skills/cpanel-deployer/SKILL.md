---
name: cpanel-deployer
description: Automate the deployment of PHP/MySQL applications to cPanel environments, including database creation and file uploads.
---

# cPanel Deployer

Streamline the tedious process of deploying and updating applications on cPanel hosting.

## When to Use This Skill
- Initial setup of a new application on cPanel.
- Managing database migrations and SQL imports.
- Updating application code via FTP or Git hooks.
- Configuring environment variables and .htaccess files.

## Features
1. **Database Setup**: Create MySQL databases and users automatically.
2. **SQL Import**: Import schema and data from SQL dumps.
3. **File Sync**: Deployment of application files.
4. **Subdomain Management**: Configure subdomains for staging/prod environments.

## Usage
- "Deploy the current directory to my cPanel staging site."
- "Create a new database named `app_db` and import `schema.sql`."
- "Update the `.env` file on the production server."

## Prerequisites
- cPanel credentials (username, password, URL).
- SSH access enabled (preferred) or FTP access.
