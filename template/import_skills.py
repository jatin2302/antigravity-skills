
import os
import shutil

SOURCE_DIR = "/Users/jatinbhutani/Documents/GitHub/awesome-claude-skills"
TARGET_DIR = "/Users/jatinbhutani/Documents/GitHub/antigravity-skills/skills"

def main():
    if not os.path.exists(TARGET_DIR):
        print(f"Target directory {TARGET_DIR} does not exist. Creating it.")
        os.makedirs(TARGET_DIR)

    # 1. Get all folders in source that have a SKILL.md
    source_folders = [d for d in os.listdir(SOURCE_DIR) if os.path.isdir(os.path.join(SOURCE_DIR, d))]
    
    imported = 0
    skipped = 0
    
    for folder in source_folders:
        source_path = os.path.join(SOURCE_DIR, folder)
        target_path = os.path.join(TARGET_DIR, folder)
        skill_file = os.path.join(source_path, "SKILL.md")
        
        if os.path.exists(skill_file):
            if not os.path.exists(target_path):
                try:
                    # Use shutil.copytree to copy the entire folder
                    shutil.copytree(source_path, target_path)
                    imported += 1
                except Exception as e:
                    print(f"Error importing {folder}: {e}")
            else:
                skipped += 1
                
    print(f"Import complete: {imported} new skills imported, {skipped} already existed.")

if __name__ == "__main__":
    main()
