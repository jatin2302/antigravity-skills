
import os
import shutil
import json
import subprocess
import sys

# Configuration
SOURCE_REPO_SKILLS = "/Users/jatinbhutani/Documents/GitHub/antigravity-skills/skills"
INTERNAL_AGENT_SKILLS = os.path.expanduser("~/.gemini/antigravity/skills")
NOTEBOOK_ID = "0eb2e536-0b2e-4f94-86ed-961c140ef348"  # Awesome Claude Skills Inventory

def sync_folders(src, dest):
    print(f"Syncing from {src} to {dest}...")
    if not os.path.exists(dest):
        os.makedirs(dest)
    
    # Simple recursive copy (could use rsync for efficiency if needed)
    # Using shutil.copytree with dirs_exist_ok=True for Python 3.8+
    try:
        shutil.copytree(src, dest, dirs_exist_ok=True)
        print(f"Successfully synced to {dest}")
    except Exception as e:
        print(f"Error syncing folders: {e}")

def upload_to_notebooklm(skill_folder_path, skill_name):
    # This function assumes it's being run by an agent that reads the output
    # and calls the actual MCP tool. Or we can print instructions.
    # Since I cannot call MCP tools directly from this python script running in shell,
    # I will output a JSON manifestation that the agent can read and act upon,
    # OR I will simply print a list of skills that need uploading.
    
    # Ideally, we check if it's already in NotebookLM (which is hard without querying).
    # For now, let's just identify new skills.
    
    skill_file = os.path.join(skill_folder_path, "SKILL.md")
    if os.path.exists(skill_file):
        with open(skill_file, 'r') as f:
            content = f.read()
        
        # We perform a "dry run" output here for the agent to parse
        print(f"NEED_UPLOAD: {skill_name} | {skill_file}")

def main():
    print("--- Starting Triad Sync ---")
    
    # 1. Sync GitHub -> Internal
    sync_folders(SOURCE_REPO_SKILLS, INTERNAL_AGENT_SKILLS)
    
    # 2. Identify skills for NotebookLM
    # We scan the SOURCE for SKILL.md files
    skills = [d for d in os.listdir(SOURCE_REPO_SKILLS) if os.path.isdir(os.path.join(SOURCE_REPO_SKILLS, d))]
    
    print(f"--- Scanning {len(skills)} skills for NotebookLM ---")
    # For this simplified version, we just list them. 
    # In a full recurring system, we'd track modification times.
    
    # Just printing the last 5 modify/created ones as potential candidates for now
    # or purely new ones.
    
    for skill in skills:
        path = os.path.join(SOURCE_REPO_SKILLS, skill)
        # Check logic could go here
        # upload_to_notebooklm(path, skill)

if __name__ == "__main__":
    main()
