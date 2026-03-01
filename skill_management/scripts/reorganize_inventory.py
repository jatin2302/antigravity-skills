import re
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
INVENTORY_PATH = os.path.join(script_dir, "..", "SKILL_INVENTORY.md")

# Defined Headers and their categorization logic (if needed) or fixed order
ORDERED_CATEGORIES = [
    "Development & IT",
    "Automation & Integration",
    "CRM & Sales",
    "Marketing & SEO",
    "Communication",
    "Project Management",
    "File Management",
    "Data & Analytics",
    "Content & Media",
    "Finance & Accounting",
    "HR & Admin",
    "Customer Support",
    "E-commerce",
    "Utilities",
    "Productivity", # Fallback for the rest
    "Other Tools & Utilities",
]

MISSING_SKILLS = [
    {"name": "Antigravity Skill Creator", "folder": "antigravity-skill-creator", "description": "Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.", "category": "Development & IT"},
    {"name": "Competitor Analysis", "folder": "competitor-analysis", "description": "Deep dive analysis for B2B SaaS competitors. Extract pricing, features, GTM strategy, and positioning holes.", "category": "Marketing & SEO"},
    {"name": "cPanel Deployer", "folder": "cpanel-deployer", "description": "Automate the deployment of PHP/MySQL applications to cPanel environments, including database creation and file uploads.", "category": "Development & IT"},
    {"name": "n8n Workflow Manager", "folder": "n8n-workflow-manager", "description": "Manage n8n workflows, nodes, and credentials. Export, import, and version control your automations.", "category": "Automation & Integration"},
    {"name": "SaaS Idea Validator", "folder": "saas-idea-validator", "description": "Evaluate \"boring\" B2B SaaS ideas against sustainability, market demand, and complexity criteria.", "category": "Product & Strategy"}
]

# Productivity & Collaboration Split Logic
# Keywords map to new Categories
SPLIT_MAP = {
    "Automation & Integration": ["workflow", "zapier", "make", "integromat", "n8n", "composio", "trigger", "hook", "connect", "integration", "sync", "bot", "script"],
    "Communication": ["slack", "discord", "email", "chat", "message", "notification", "whatsapp", "telegram", "sms", "voice", "call", "meeting", "zoom", "teams", "inbox", "reply", "sender", "newsletter", "customer support", "support", "ticket"],
    "Project Management": ["project", "asana", "trello", "jira", "clickup", "monday", "linear", "basecamp", "wrike", "scrum", "agile", "kanban", "roadmap", "issue", "sprint"],
    "HR & Admin": ["recruit", "hiring", "job", "candidate", "employee", "hr", "admin", "schedule", "calendar", "booking", "interview"],
    "E-commerce": ["shopify", "store", "product", "order", "sales", "customer", "payment", "invoice", "billing"],
    "Development & IT": ["git", "code", "dev", "deploy", "server", "cloud", "database", "api", "sdk", "test", "debug", "monitor", "log", "security", "auth"], 
    "File Management": ["file", "folder", "document", "pdf", "drive", "dropbox", "upload", "download", "storage", "box", "doc"],
    "Utilities": ["convert", "calculator", "time", "weather", "map", "search", "location", "ip", "qr", "image", "video", "ocr", "parse", "scrape"],
    "Productivity": [] # Fallback for the rest
}

def parse_inventory(path):
    with open(path, "r") as f:
        content = f.read()

    # Split by lines
    lines = content.split('\n')
    
    skills = []
    current_category = None
    
    # Regex for table row: | **Name** | `folder` | Description |
    row_regex = re.compile(r'\|\s*\*\*(.*?)\*\*\s*\|\s*`([^`]+)`\s*\|\s*(.*?)\s*\|')
    
    header_lines = [] # To keep top matter
    
    for line in lines:
        match = row_regex.match(line)
        if match:
            # It's a skill row
            name, folder, desc = match.groups()
            skills.append({
                "name": name.strip(),
                "folder": folder.strip(),
                "description": desc.strip(),
                "category": current_category
            })
        elif line.startswith("### "):
            current_category = line.replace("### ", "").split("(")[0].strip()
        elif line.startswith("# ") or line.startswith("Total Skills"):
            pass # We will regenerate these
        elif "| Name | Folder | Description |" in line or "| :--- |" in line:
            pass # Table headers, regenerate
        elif line.strip() == "":
            pass
        else:
            # Unknown line, keep it? usually just empty space or text
            pass
            
    return skills

def categorize_skill(skill):
    # Categories to ALWAYS re-evaluate (because we are tweaking logical splits)
    DYNAMIC_CATEGORIES = [
        "Productivity & Collaboration",
        "Productivity",
        "Project Management",
        "Communication",
        "Automation & Integration",
        "File Management",
        "Utilities"
    ]

    current_cat = skill.get("category")
    
    # If it's a stable category, keep it.
    if current_cat and current_cat not in DYNAMIC_CATEGORIES and current_cat in ORDERED_CATEGORIES:
        return current_cat
        
    # Otherwise, re-evaluate based on text
    desc = skill["description"].lower() if skill["description"] else ""
    name = skill["name"].lower() if skill["name"] else ""
    folder = skill["folder"].lower() if skill["folder"] else ""
    text = f"{name} {folder} {desc}"
        
    # Check Project Management
    for keyword in SPLIT_MAP["Project Management"]:
        if keyword in text:
            return "Project Management"
            
    # Check Communication
    for keyword in SPLIT_MAP["Communication"]:
        if keyword in text:
            return "Communication"
            
    # Check Development & IT
    for keyword in SPLIT_MAP["Development & IT"]:
        if keyword in text:
            return "Development & IT"

    # Check E-commerce
    for keyword in SPLIT_MAP["E-commerce"]:
        if keyword in text:
            return "E-commerce"

    # Check HR & Admin
    for keyword in SPLIT_MAP["HR & Admin"]:
        if keyword in text:
            return "HR & Admin"

    # Check Automation
    for keyword in SPLIT_MAP["Automation & Integration"]:
        if keyword in text:
            return "Automation & Integration"

    # Check File Management
    for keyword in SPLIT_MAP["File Management"]:
        if keyword in text:
            return "File Management"

    # Check Utilities
    for keyword in SPLIT_MAP["Utilities"]:
        if keyword in text:
            return "Utilities"
            
    return "Productivity" # Fallback
        
    return skill["category"]

def main():
    skills = parse_inventory(INVENTORY_PATH)
    
    # Add missing skills
    existing_folders = {s["folder"] for s in skills}
    for m in MISSING_SKILLS:
        if m["folder"] not in existing_folders:
            skills.append(m)
    
    # Re-categorize
    categorized_skills = {}
    for s in skills:
        cat = categorize_skill(s)
        # Handle "Product & Strategy" special case not in ORDERED (add to Dev & IT or create new?)
        if cat == "Product & Strategy":
            cat = "Development & IT" 
            
        if cat not in categorized_skills:
            categorized_skills[cat] = []
        categorized_skills[cat].append(s)
        
    # Generate Output
    output_lines = []
    output_lines.append("# Awesome Claude Skills - Master Inventory")
    output_lines.append("")
    total_skills = sum(len(v) for v in categorized_skills.values())
    output_lines.append(f"Total Skills: {total_skills}")
    output_lines.append("")
    
    # Sort categories based on ORDERED_CATEGORIES, putting others at end
    sorted_cats = [c for c in ORDERED_CATEGORIES if c in categorized_skills]
    remaining_cats = [c for c in categorized_skills.keys() if c not in sorted_cats]
    
    for cat in sorted_cats + remaining_cats:
        s_list = categorized_skills[cat]
        if not s_list:
            continue
            
        # Sort skills by Folder name A-Z
        s_list.sort(key=lambda x: x["folder"].lower())
        
        output_lines.append(f"### {cat} ({len(s_list)})")
        output_lines.append("")
        output_lines.append("| Name | Folder | Description |")
        output_lines.append("| :--- | :--- | :--- |")
        for s in s_list:
            output_lines.append(f"| **{s['name']}** | `{s['folder']}` | {s['description']} |")
        output_lines.append("")
        
    # Write backup
    # os.system(f"cp {INVENTORY_PATH} {INVENTORY_PATH}.bak") 
    
    # Write new content
    with open(INVENTORY_PATH, "w") as f:
        f.write("\n".join(output_lines))
        
    print(f"Successfully updated inventory with {total_skills} skills.")

if __name__ == "__main__":
    main()
