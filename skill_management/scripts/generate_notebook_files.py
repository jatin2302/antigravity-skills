import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
INVENTORY_PATH = os.path.join(script_dir, "..", "SKILL_INVENTORY.md")
OUTPUT_DIR = os.path.join(script_dir, "..", "notebooks")

def parse_inventory(path):
    with open(path, "r") as f:
        content = f.read()

    lines = content.split('\n')
    
    categories = {}
    current_category = None
    
    row_regex = re.compile(r'\|\s*\*\*(.*?)\*\*\s*\|\s*`([^`]+)`\s*\|\s*(.*?)\s*\|')
    
    for line in lines:
        match = row_regex.match(line)
        if match:
            # It's a skill row
            name, folder, desc = match.groups()
            if current_category:
                categories[current_category].append({
                    "name": name.strip(),
                    "folder": folder.strip(),
                    "description": desc.strip()
                })
        elif line.startswith("### "):
            current_category = line.replace("### ", "").split("(")[0].strip()
            if current_category not in categories:
                categories[current_category] = []
            
    return categories

def generate_files(categories):
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    for cat, skills in categories.items():
        if not skills:
            continue
            
        safe_cat_name = cat.replace(" & ", "_").replace(" ", "_").lower()
        filename = os.path.join(OUTPUT_DIR, f"{safe_cat_name}.md")
        
        with open(filename, "w") as f:
            f.write(f"# Skills - {cat}\n\n")
            f.write(f"Total Skills: {len(skills)}\n\n")
            f.write("| Name | Folder | Description |\n")
            f.write("| :--- | :--- | :--- |\n")
            for s in skills:
                f.write(f"| **{s['name']}** | `{s['folder']}` | {s['description']} |\n")
                
        print(f"Generated {filename} with {len(skills)} skills.")

def main():
    categories = parse_inventory(INVENTORY_PATH)
    generate_files(categories)

if __name__ == "__main__":
    main()
