import re
import os

def create_tree():
    # Paths relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    inventory_path = os.path.join(script_dir, '..', 'SKILL_INVENTORY.md')
    output_path = os.path.join(script_dir, '..', '..', 'SKILLS_TREE.md')
    
    with open(inventory_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    tree = ["# Antigravity Skills Category Tree\n"]
    tree.append("A hierarchical view of all skills organized by their respective categories.\n")
    tree.append("```text\nskills/\n")
    
    current_category = None
    
    for line in lines:
        line = line.strip()
        if line.startswith('### '):
            match = re.search(r'### (.+?)\s*\(\d+\)', line)
            if match:
                current_category = match.group(1).strip()
                safe_cat_name = current_category.replace(' & ', '_').lower().replace(' ', '_')
                tree.append(f"├── {safe_cat_name}/\n")
        elif line.startswith('| **'):
            cols = [c.strip() for c in line.split('|') if c.strip()]
            if len(cols) >= 3 and current_category:
                folder_name = cols[1].strip('` ')
                tree.append(f"│   ├── {folder_name}/\n")
                
    tree.append("```\n")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(tree)
        
    print(f"Tree structure saved to {output_path}")

if __name__ == "__main__":
    create_tree()
