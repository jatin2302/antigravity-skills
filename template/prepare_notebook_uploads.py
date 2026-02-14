#!/usr/bin/env python3
"""
Upload skills to NotebookLM category notebooks.
This script reads SKILL.md files and outputs JSON instructions for the agent.
"""
import os
import re
import json

SKILLS_DIR = "/Users/jatinbhutani/Documents/GitHub/antigravity-skills/skills"

# Notebook IDs by category
NOTEBOOKS = {
    "marketing_seo": "2c5714a8-bc9a-4ce8-b816-ec2a3221cd8c",
    "crm_sales": "4acfbfaa-5db1-4274-b9a8-539f535979fd",
    "dev_it": "4e432d1a-1f91-41ac-a759-c3a5e408b5fd",
    "data_analytics": "7a37d928-0ce0-4b0f-8b6f-88684983de1b",
    "content_design": "a5c763d6-b25a-428d-958a-955dc38638bd",
    "finance_hr": "e0124706-20b6-4721-8d3c-1af2ba22a942",
    "ai_strategy": "9c3487f2-b65c-46e9-a57a-0acbf0e30369",
    "productivity": "b2845185-8192-4a75-83b9-5d72d5c125b8",
}

# Category keyword matching
CATEGORY_KEYWORDS = {
    "marketing_seo": ["marketing", "seo", "email campaign", "newsletter", "mailchimp", "ads", "social media", "instagram", "twitter", "linkedin", "facebook", "tiktok", "brevo", "sendgrid", "mailerlite", "omnisend", "semrush", "ahrefs", "moz", "seo-strategist", "content-page-builder", "reddit-outreach", "reddit", "competitive-ads", "SEO", "ai content"],
    "crm_sales": ["crm", "sales", "leads", "contact", "pipeline", "hubspot", "salesforce", "pipedrive", "zoho crm", "apollo", "attio", "close", "kommo", "capsule", "lead-research", "fastestrank", "gong", "outreach"],
    "dev_it": ["git", "code", "api", "database", "server", "cloud", "deploy", "github", "gitlab", "docker", "sentry", "posthog", "new relic", "datadog", "vercel", "supabase", "neon", "render", "circleci", "buildkite", "bitbucket", "snowflake", "mcp-builder", "webapp-testing", "cpanel"],
    "data_analytics": ["data", "analytics", "dashboard", "report", "google analytics", "mixpanel", "amplitude", "scraping", "crawl", "airtable", "google sheets", "excel", "firecrawl", "apify", "bigquery", "segment"],
    "content_design": ["image", "video", "design", "pdf", "canva", "figma", "adobe", "cms", "webflow", "cloudinary", "pptx", "docx", "canvas-design", "heygen", "shotstack", "elevenlabs"],
    "finance_hr": ["finance", "invoice", "payment", "stripe", "accounting", "quickbooks", "xero", "freshbooks", "payroll", "recruiting", "hiring", "employee", "workday", "bamboohr", "deel", "harvest", "wave", "zoho books", "zoho invoice", "ramp"],
    "ai_strategy": ["saas-idea", "competitor-analysis", "evaluation", "context-", "memory-systems", "multi-agent", "tool-design", "project-development", "bdi-mental", "advanced-evaluation", "agency-builder", "brainstorming", "planning-with-files", "hosted-agents"],
    "productivity": ["slack", "notion", "gmail", "calendar", "jira", "asana", "trello", "teams", "discord", "zoom", "outlook", "google drive", "onedrive", "todoist", "clickup", "linear", "monday", "telegram", "whatsapp", "clients", "internal-comms", "qa-sop", "n8n"],
}

def get_skill_content(folder_path):
    skill_file = os.path.join(folder_path, "SKILL.md")
    if not os.path.exists(skill_file):
        return None, None
    try:
        with open(skill_file, 'r', encoding='utf-8') as f:
            content = f.read()
        name_match = re.search(r"^name:\s*(.*)$", content, re.MULTILINE)
        name = name_match.group(1).strip() if name_match else os.path.basename(folder_path)
        return name, content
    except:
        return None, None

def categorize_skill(folder_name, name, content):
    text = f"{folder_name} {name} {content}".lower()
    for cat, keywords in CATEGORY_KEYWORDS.items():
        if any(k.lower() in text for k in keywords):
            return cat
    return None  # Skip uncategorized

def main():
    uploads = {cat: [] for cat in NOTEBOOKS}
    skipped = 0

    folders = sorted([d for d in os.listdir(SKILLS_DIR) if os.path.isdir(os.path.join(SKILLS_DIR, d))])
    
    for folder in folders:
        path = os.path.join(SKILLS_DIR, folder)
        name, content = get_skill_content(path)
        if not name or not content:
            continue
        
        cat = categorize_skill(folder, name, content)
        if cat and len(uploads[cat]) < 50:  # Respect 50-source limit
            uploads[cat].append({
                "folder": folder,
                "name": name,
                "title": f"{name}",
            })
        else:
            skipped += 1

    # Print summary
    total = 0
    for cat, skills in uploads.items():
        print(f"\n{cat} ({len(skills)} skills) -> Notebook: {NOTEBOOKS[cat]}")
        for s in skills:
            print(f"  - {s['name']} ({s['folder']})")
        total += len(skills)
    
    print(f"\nTotal to upload: {total}")
    print(f"Skipped (uncategorized or over limit): {skipped}")
    
    # Save manifest
    manifest = {
        "notebooks": NOTEBOOKS,
        "uploads": {cat: [s['folder'] for s in skills] for cat, skills in uploads.items()},
        "total": total,
        "skipped": skipped,
    }
    with open("notebook_manifest.json", "w") as f:
        json.dump(manifest, f, indent=2)
    print("\nManifest saved to notebook_manifest.json")

if __name__ == "__main__":
    main()
