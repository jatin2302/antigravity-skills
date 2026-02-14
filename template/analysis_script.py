
import os
import re

SKILL_INVENTORY_FILE = "/Users/jatinbhutani/.gemini/antigravity/playground/ultraviolet-parsec/SKILL_INVENTORY.md"

def analyze_categories():
    if not os.path.exists(SKILL_INVENTORY_FILE):
        print(f"Skipping analysis - file {SKILL_INVENTORY_FILE} not found.")
        return

    try:
        with open(SKILL_INVENTORY_FILE, 'r') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading {SKILL_INVENTORY_FILE}: {e}")
        return

    app_automation_skills = []
    in_app_automation = False
    
    for line in lines:
        if "### App Automation (Full List)" in line:
            in_app_automation = True
            continue
        if in_app_automation and line.startswith("###"):
            in_app_automation = False
            continue
            
        if in_app_automation and line.strip().startswith("|") and "Status" not in line and ":---" not in line:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 5:
                # Name is column 2 (index 2), Desc is column 4 (index 4)
                # But splits might have empty string at start/end
                name_idx = 2
                desc_idx = 4
                if len(parts) > desc_idx:
                    name = parts[name_idx].replace("**", "")
                    desc = parts[desc_idx]
                    app_automation_skills.append((name, desc))

    print(f"Found {len(app_automation_skills)} skills in 'App Automation' section.")
    
    # Simple keyword based categorization
    keywords = {
        "CRM & Sales": ["CRM", "sales", "leads", "contact", "pipeline", "HubSpot", "Salesforce", "Pipedrive", "Zoho", "outreach"],
        "Marketing & SEO": ["marketing", "SEO", "email", "campaign", "newsletter", "Mailchimp", "ads", "social media", "Instagram", "Twitter", "LinkedIn", "Facebook", "TikTok", "YouTube"],
        "Development & IT": ["git", "code", "API", "database", "server", "cloud", "deploy", "GitHub", "GitLab", "Docker", "AWS", "Azure", "Sentry", "PostHog", "New Relic", "Datadog", "Vercel", "Firebase", "Supabase", "MongoDB", "MySQL", "Postgres"],
        "Productivity & Collaboration": ["project", "task", "calendar", "meeting", "note", "Notion", "Trello", "Asana", "Jira", "Slack", "Teams", "Discord", "Zoom", "Google Meet", "Outlook", "Google Drive", "OneDrive"],
        "Data & Analytics": ["data", "analytics", "dashboard", "report", "Google Analytics", "mixpanel", "metrics", "scraping", "crawl", "airtable", "google sheets", "excel", "csv", "json"],
        "Content & Media": ["image", "video", "content", "design", "PDF", "YouTube", "blog", "cms", "wordpress", "webflow", "Canva", "Figma", "Adobe"],
        "Finance & Accounting": ["finance", "invoice", "payment", "Stripe", "accounting", "QuickBooks", "Xero", "Zoho Books", "FreshBooks", "Paypal", "Wise", "billing"],
        "Customer Support": ["support", "ticket", "helpdesk", "Zendesk", "Intercom", "customer service", "chat"],
        "HR & Admin": ["HR", "recruiting", "hiring", "employee", "payroll", "Workday", "BambooHR", "Gusto", "Deel", "Remote"],
        "Legal & Compliance": ["legal", "contract", "sign", "DocuSign", "HelloSign", "PandaDoc", "compliance", "GDPR"],
        "E-commerce": ["Shopify", "WooCommerce", "e-commerce", "store", "product", "inventory", "shipping"]
    }
    
    categorized_counts = {k: 0 for k in keywords}
    uncategorized_count = 0
    total_analyzed = 0
    
    for name, desc in app_automation_skills:
        found_cat = False
        desc_lower = desc.lower()
        name_lower = name.lower()
        
        # Check against each category's keywords
        for cat, keys in keywords.items():
            if any(k.lower() in desc_lower or k.lower() in name_lower for k in keys):
                categorized_counts[cat] += 1
                found_cat = True
                # Don't break immediately to allow multi-categorization if needed, 
                # but for simple counts let's just count primarily once or prioritize order.
                # Here we break for simplicity to sum to total.
                break
        
        if not found_cat:
            uncategorized_count += 1
        total_analyzed += 1

    print("\nPROPOSED CATEGORIZATION BREAKDOWN:")
    for cat, count in categorized_counts.items():
        print(f"  - {cat}: {count} skills")
    print(f"  - Uncategorized/Generic: {uncategorized_count} skills")

if __name__ == "__main__":
    analyze_categories()
