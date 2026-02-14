
import os
import re
import shutil
import json

SOURCE_SKILLS_DIR = "/Users/jatinbhutani/Documents/GitHub/antigravity-skills/skills"
INTERNAL_AG_SKILLS = os.path.expanduser("~/.gemini/antigravity/skills")
OUTPUT_DIR = "/Users/jatinbhutani/.gemini/antigravity/playground/ultraviolet-parsec/Categorized_Inventories"

CATEGORIES = {
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

def clean_desc(desc):
    return desc.strip().replace("\n", " ")

def get_skill_metadata(skill_path):
    skill_file = os.path.join(skill_path, "SKILL.md")
    if not os.path.exists(skill_file):
        return None
        
    try:
        with open(skill_file, 'r', encoding='utf-8') as f:
            content = f.read()
            name_match = re.search(r"^name:\s*(.*)$", content, re.MULTILINE)
            desc_match = re.search(r"^description:\s*\"?(.*?)\"?$", content, re.MULTILINE)
            
            folder_name = os.path.basename(skill_path)
            name = name_match.group(1).strip() if name_match else folder_name
            description = desc_match.group(1).strip() if desc_match else "No description available."
            
            return {
                "name": name,
                "folder": folder_name,
                "description": description,
                "path": skill_path
            }
    except Exception as e:
        print(f"Error reading {skill_file}: {e}")
        return None

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    if not os.path.exists(INTERNAL_AG_SKILLS):
        os.makedirs(INTERNAL_AG_SKILLS)

    print("Scanning skills...")
    all_skills = []
    folders = [d for d in os.listdir(SOURCE_SKILLS_DIR) if os.path.isdir(os.path.join(SOURCE_SKILLS_DIR, d))]
    
    for folder in folders:
        skill_data = get_skill_metadata(os.path.join(SOURCE_SKILLS_DIR, folder))
        if skill_data:
            all_skills.append(skill_data)

    print(f"Found {len(all_skills)} valid skills.")

    # Group skills
    categorized_skills = {cat: [] for cat in CATEGORIES}
    uncategorized = []
    
    for skill in all_skills:
        found_cat = False
        desc_lower = skill['description'].lower()
        name_lower = skill['name'].lower()
        
        for cat, keywords in CATEGORIES.items():
            if any(k.lower() in desc_lower or k.lower() in name_lower for k in keywords):
                categorized_skills[cat].append(skill)
                found_cat = True
                break # Assign to first matching category
        
        if not found_cat:
            uncategorized.append(skill)

    # Add uncategorized to a specific bucket
    categorized_skills["Other Tools & Utilities"] = uncategorized

    # Generate Inventory Files
    main_inventory_path = os.path.join(OUTPUT_DIR, "MASTER_SKILL_INVENTORY.md")
    with open(main_inventory_path, "w", encoding='utf-8') as main_f:
        main_f.write("# Awesome Claude Skills - Master Inventory\n\n")
        main_f.write(f"Total Skills: {len(all_skills)}\n\n")
        
        for cat, skills in categorized_skills.items():
            if not skills: continue
            
            # Create Category File
            cat_filename = f"Skills - {cat.replace('&', 'and').replace(' ', '_')}.md"
            cat_path = os.path.join(OUTPUT_DIR, cat_filename)
            
            with open(cat_path, "w", encoding='utf-8') as cat_f:
                cat_f.write(f"# {cat} Skills\n\n")
                cat_f.write(f"This collection contains {len(skills)} skills related to {cat}.\n\n")
                
                cat_f.write("| Name | Folder | Description |\n")
                cat_f.write("| :--- | :--- | :--- |\n")
                
                # Write to Main Inventory too
                main_f.write(f"### {cat} ({len(skills)})\n\n")
                main_f.write("| Name | Folder | Description |\n")
                main_f.write("| :--- | :--- | :--- |\n")
                
                for s in sorted(skills, key=lambda x: x['name']):
                    row = f"| **{s['name']}** | `{s['folder']}` | {clean_desc(s['description'])} |\n"
                    cat_f.write(row)
                    main_f.write(row)
                
                main_f.write("\n")
            
            print(f"Generated {cat_filename}")

    print(f"Generated MASTER_SKILL_INVENTORY.md")

    # Sync to Internal Folder
    print("\nSyncing skills to Internal AG Folder...")
    synced_count = 0
    for folder in folders:
        src = os.path.join(SOURCE_SKILLS_DIR, folder)
        dest = os.path.join(INTERNAL_AG_SKILLS, folder)
        
        if not os.path.exists(dest):
            try:
                shutil.copytree(src, dest)
                synced_count += 1
            except Exception as e:
                print(f"Error copying {folder}: {e}")
    
    print(f"Sync complete. {synced_count} new skills copied to {INTERNAL_AG_SKILLS}.")

if __name__ == "__main__":
    main()
