---
description: Add a new skill to the antigravity-skills repo and sync the project structure
---

# /sync-ag-skills

Use this workflow whenever the user wants to add a new skill to the AG ecosystem or restructure existing skills inside the `antigravity-skills` repository.

## Step 1: Add the Skill Files

1. Create a new folder for the skill inside `/Users/jatinbhutani/GitHub/antigravity-skills/skills/`.
   - Ensure the folder name is lowercase and uses hyphens (e.g., `my-new-skill`).
2. Inside that folder, create the `SKILL.md` file. It MUST include a YAML frontmatter block with `name` and `description` properties.

## Step 2: Sync the Inventory and Notebooks

Run the primary synchronization script to detect the new skill, generate the updated NotebookLM files, and refresh the visual skill tree.

// turbo-all
```bash
cd /Users/jatinbhutani/GitHub/antigravity-skills
bash skill_management/scripts/sync-skills.sh
```

## Step 3: Validate Outputs

Check the following to ensure the sync succeeded:
1. Review `/Users/jatinbhutani/GitHub/antigravity-skills/skill_management/SKILL_INVENTORY.md` to guarantee the new skill got categorized.
2. Review `/Users/jatinbhutani/GitHub/antigravity-skills/SKILLS_TREE.md` to see the new skill reflected in the tree structure.

## Step 4: Commit Changes

Finally, ask the user if they would like to commit these changes to the GitHub repository using git.
