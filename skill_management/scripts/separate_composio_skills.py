import os
import re
import shutil

script_dir = os.path.dirname(os.path.abspath(__file__))
INVENTORY_PATH = os.path.join(script_dir, "..", "SKILL_INVENTORY.md")
COMPOSIO_DIR = os.path.join(script_dir, "..", "..", "composio_skills")
COMPOSIO_INVENTORY_PATH = os.path.join(COMPOSIO_DIR, "COMPOSIO_SKILL_INVENTORY.md")
COMPOSIO_TREE_PATH = os.path.join(COMPOSIO_DIR, "COMPOSIO_SKILL_TREE.md")
SKILLS_DIR = os.path.join(script_dir, "..", "..", "skills")

def separate_composio_skills():
    if not os.path.exists(COMPOSIO_DIR):
        os.makedirs(COMPOSIO_DIR)
        
    with open(INVENTORY_PATH, "r") as f:
        lines = f.readlines()

    header_metadata = []
    sections = [] 
    composio_rows = []
    composio_keywords = ["Composio", "Rube MCP"]

    current_heading = None
    current_rows = []
    in_header = True

    # First pass to identify heading structure and extract ALL skills
    for line in lines:
        if line.startswith("### "):
            if "Composio Automations" in line:
                in_header = False
                continue
                
            if current_heading:
                sections.append((current_heading, current_rows))
            
            current_heading = line.strip()
            current_rows = []
            in_header = False
            continue
        
        if in_header:
            header_metadata.append(line)
            continue

        if line.startswith("|"):
            if line.startswith("| Name |") or line.startswith("| :---"):
                current_rows.append(line)
                continue
            
            # Skill row - check for duplicates and Composio keywords
            if any(kw in line for kw in composio_keywords):
                if line not in composio_rows:
                    composio_rows.append(line)
            else:
                if current_rows and line not in current_rows:
                     current_rows.append(line)
                elif not current_rows:
                     current_rows.append(line)
        elif line.strip() == "" and current_heading:
            current_rows.append(line)
        elif not current_heading:
            header_metadata.append(line)

    if current_heading:
        sections.append((current_heading, current_rows))

    # Rebuild main inventory WITHOUT Composio section
    new_content = []
    new_content.extend(header_metadata)

    for heading, rows in sections:
        # Only count unique actual skill rows, skipping any Composio headers entirely
        if "Composio Automations" in heading:
            continue
            
        seen_rows = set()
        unique_skill_rows = []
        for r in rows:
            if r.startswith("|") and not (r.startswith("| Name |") or r.startswith("| :---")):
                if r not in seen_rows:
                    seen_rows.add(r)
                    unique_skill_rows.append(r)
        
        count = len(unique_skill_rows)
        if count == 0:
             # Skip empty headers entirely 
             pass
        else:
            new_heading = re.sub(r'\(\d+\)', f'({count})', heading)
            if "(" not in new_heading:
                 new_heading = f"{new_heading} ({count})"
            new_content.append(new_heading + "\n")
            
            has_table_header = any(r.startswith("| Name |") for r in rows)
            if not has_table_header and unique_skill_rows:
                new_content.append("\n| Name | Folder | Description |\n| :--- | :--- | :--- |\n")
            
            for r in rows:
                if r.startswith("| Name |") or r.startswith("| :---"):
                    new_content.append(r)
                elif r.startswith("|"):
                    if r in unique_skill_rows:
                        new_content.append(r)
                        unique_skill_rows.remove(r)
                else:
                    new_content.append(r)

    # Save main inventory
    final_text = "".join(new_content)
    with open(INVENTORY_PATH, 'w') as f:
        f.write(final_text)

    # Prepare Composio Inventory
    unique_composio = []
    seen_comp = set()
    for r in composio_rows:
        if r not in seen_comp:
            seen_comp.add(r)
            unique_composio.append(r)
            
    # Sort Composio skills A-Z by folder name
    # Regex to extract folder name for sorting
    def get_folder(row):
        cols = [c.strip() for c in row.split('|') if c.strip()]
        if len(cols) >= 2:
           return cols[1].strip('`').lower()
        return ""
        
    unique_composio.sort(key=get_folder)

    # Move the folders
    moved_count = 0
    for row in unique_composio:
        folder_name = get_folder(row)
        if folder_name:
            src_path = os.path.join(SKILLS_DIR, folder_name)
            dst_path = os.path.join(COMPOSIO_DIR, folder_name)
            if os.path.exists(src_path):
                try:
                    shutil.move(src_path, dst_path)
                    moved_count += 1
                except Exception as e:
                    print(f"Error moving {folder_name}: {e}")

    comp_inv_content = []
    comp_inv_content.append("# Composio & Rube MCP Skills Inventory\n\n")
    comp_inv_content.append(f"Auto-generated inventory of {len(unique_composio)} Composio and Rube MCP integrations.\n\n")
    comp_inv_content.append(f"### Composio Automations ({len(unique_composio)})\n\n")
    comp_inv_content.append("| Name | Folder | Description |\n")
    comp_inv_content.append("| :--- | :--- | :--- |\n")
    comp_inv_content.extend(unique_composio)

    with open(COMPOSIO_INVENTORY_PATH, "w") as f:
        f.writelines(comp_inv_content)

    # Prepare Composio Tree
    comp_tree_content = []
    comp_tree_content.append("# Composio Skills Hierarchy\n\n")
    comp_tree_content.append("- Composio Automations\n")
    
    for r in unique_composio:
        # Extract name from: | **name** | `folder` | desc |
        match = re.search(r'\|\s*\*\*(.*?)\*\*\s*\|', r)
        if match:
            s_name = match.group(1).strip()
            comp_tree_content.append(f"  - {s_name}\n")
            
    with open(COMPOSIO_TREE_PATH, "w") as f:
        f.writelines(comp_tree_content)

    print(f"Composio separation complete. physically moved {moved_count} of {len(unique_composio)} skills to {COMPOSIO_DIR}")

if __name__ == "__main__":
    separate_composio_skills()
