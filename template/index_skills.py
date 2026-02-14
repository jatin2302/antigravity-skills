
import os
import re

SOURCE_DIR = "/Users/jatinbhutani/Documents/GitHub/awesome-claude-skills"
TARGET_DIR = "/Users/jatinbhutani/Documents/GitHub/antigravity-skills/skills"
README_PATH = os.path.join(SOURCE_DIR, "README.md")

def get_skills_with_metadata(path):
    skills = {}
    for root, dirs, files in os.walk(path, maxdepth=2):
        if "SKILL.md" in files:
            skill_folder = os.path.basename(root)
            skill_path = os.path.join(root, "SKILL.md")
            with open(skill_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Extract name and description from YAML frontmatter
                name_match = re.search(r"^name:\s*(.*)$", content, re.MULTILINE)
                desc_match = re.search(r"^description:\s*\"?(.*?)\"?$", content, re.MULTILINE)
                
                name = name_match.group(1).strip() if name_match else skill_folder
                description = desc_match.group(1).strip() if desc_match else "No description available."
                
                skills[skill_folder] = {
                    "name": name,
                    "description": description,
                    "local_path": root
                }
    return skills

def parse_readme_categories(readme_path):
    categories = {}
    current_category = "Uncategorized"
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    for line in lines:
        # Match category header ### Category Name
        cat_match = re.match(r"^### (.*)$", line)
        if cat_match:
            current_category = cat_match.group(1).strip()
            categories[current_category] = []
            continue
            
        # Match skill link - [Name](./folder/) or - [Name](url)
        # We only care about Local relative links for inventory
        link_match = re.search(r"-\s*\[(.*?)\]\(\./(.*?)/?\)", line)
        if link_match:
            folder = link_match.group(2).strip()
            if current_category not in categories:
                categories[current_category] = []
            categories[current_category].append(folder)
            
    return categories

def main():
    # 1. Scrape all skills in source
    source_skills = {}
    # Walk manually since find showed many
    folders = [d for d in os.listdir(SOURCE_DIR) if os.path.isdir(os.path.join(SOURCE_DIR, d))]
    for folder in folders:
        skill_file = os.path.join(SOURCE_DIR, folder, "SKILL.md")
        if os.path.exists(skill_file):
            try:
                with open(skill_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    name_match = re.search(r"^name:\s*(.*)$", content, re.MULTILINE)
                    desc_match = re.search(r"^description:\s*\"?(.*?)\"?$", content, re.MULTILINE)
                    
                    name = name_match.group(1).strip() if name_match else folder
                    description = desc_match.group(1).strip() if desc_match else "No description available."
                    source_skills[folder] = {"name": name, "description": description}
            except Exception:
                continue

    # 2. Scrape existing skills in target
    existing_folders = [d for d in os.listdir(TARGET_DIR) if os.path.isdir(os.path.join(TARGET_DIR, d))]
    
    # 3. Parse README for categories
    readme_categories = parse_readme_categories(README_PATH)
    
    # Organize indexed skills by category
    indexed_by_category = {}
    processed_folders = set()
    
    for cat, folders in readme_categories.items():
        indexed_by_category[cat] = []
        for folder in folders:
            if folder in source_skills:
                skill_data = source_skills[folder]
                skill_data['folder'] = folder
                skill_data['exists_locally'] = folder in existing_folders
                indexed_by_category[cat].append(skill_data)
                processed_folders.add(folder)
                
    # Add remaining "Automation" skills to a generic category
    indexed_by_category["App Automation (Full List)"] = []
    for folder, data in source_skills.items():
        if folder not in processed_folders:
            data['folder'] = folder
            data['exists_locally'] = folder in existing_folders
            indexed_by_category["App Automation (Full List)"].append(data)

    # 4. Write Markdown Index
    with open("SKILL_INVENTORY.md", "w", encoding='utf-8') as f:
        f.write("# Awesome Claude Skills Inventory\n\n")
        f.write("This index categorizes the skills found in the `awesome-claude-skills` repository.\n\n")
        f.write("## Legend\n")
        f.write("- ✅ : Already imported to `antigravity-skills/skills` folder\n")
        f.write("- ➕ : New skill available for import\n\n")
        
        for cat, skills in indexed_by_category.items():
            if not skills: continue
            f.write(f"### {cat}\n\n")
            f.write("| Status | Name | Folder | Description |\n")
            f.write("| :--- | :--- | :--- | :--- |\n")
            for s in sorted(skills, key=lambda x: x['name']):
                status = "✅" if s['exists_locally'] else "➕"
                desc = s['description'].replace("\n", " ")
                f.write(f"| {status} | **{s['name']}** | `{s['folder']}` | {desc} |\n")
            f.write("\n")

    print(f"Inventory generated: {len(source_skills)} skills indexed.")

if __name__ == "__main__":
    main()
