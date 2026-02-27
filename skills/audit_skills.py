import os
import shutil

SKILLS_DIR = "/Users/jatinbhutani/.gemini/antigravity/skills"
ARCHIVE_DIR = os.path.join(SKILLS_DIR, "_archive_cold")

# List of skills to explicitly KEEP in the root (based on the AG Brain notebook)
ACTIVE_SKILLS = {
    "planning-with-files",
    "executing-plans",
    "brainstorming",
    "writing-plans",
    "verification-before-completion",
    "systematic-debugging",
    "test-driven-development",
    "seo-strategist",
    "content-page-builder",
    "content-research-writer",
    "competitor-analysis",
    "competitive-ads-extractor",
    "qa-sop-enforcer",
    "reddit-outreach",
    "reddit-marketing-system",
    "reddit-worker-management",
    "twitter-algorithm-optimizer",
    "agency-builder",
    "fastestrank-intake",
    "client-onboarding",
    "saas-idea-validator",
    "frontend-design",
    "webapp-testing",
    "cpanel-deployer",
    "remotion-best-practices",
    "gmail-automation",
    "google-calendar-automation",
    "google-drive-automation",
    "googlesheets-automation",
    "slack-automation",
    "notion-automation",
    "hubspot-automation",
    "jira-automation",
    "shopify-automation",
    "stripe-automation",
    "n8n-workflow-manager",
    "pdf",
    "docx",
    "pptx",
    "xlsx",
    "canvas-design",
    "mcp-builder",
    "composio",
    "notebooklm",
    "integrating-notebooklm",
    "skill-creator",
    "blast-protocol",
    "last30days",
    "defuddle",
    "doc-coauthoring",
    # Additional explicitly created custom skills:
    "using-git-worktrees",
    "finishing-a-development-branch",
    "using-superpowers",
    "superpowers",
    "theme-factory",
    "web-artifacts-builder",
    "artifacts-builder",
    "brand-guidelines",
    "brain-notebook",
    "active-projects",
    "file-organizer",
    "brand-identity"
}

def is_composio_stub(folder_name):
    # Most composio stubs end with "-automation" 
    if not folder_name.endswith("-automation"):
        return False
    # If it's one of our explicitly active automation skills, keep it
    if folder_name in ACTIVE_SKILLS:
        return False
    return True

def main(dry_run=True):
    print(f"Starting audit (Dry run: {dry_run})")
    
    if not os.path.exists(ARCHIVE_DIR):
        if not dry_run:
            os.makedirs(ARCHIVE_DIR)
        print(f"Would create archive dir: {ARCHIVE_DIR}")

    folders = [d for d in os.listdir(SKILLS_DIR) if os.path.isdir(os.path.join(SKILLS_DIR, d))]
    
    to_move = []
    
    for folder in folders:
        if folder == "_archive_cold" or folder.startswith("."):
            continue
            
        if is_composio_stub(folder):
            to_move.append(folder)
            
    print(f"Found {len(to_move)} unused Composio stubs out of {len(folders)} total folders.")
    
    for folder in to_move:
        src = os.path.join(SKILLS_DIR, folder)
        dst = os.path.join(ARCHIVE_DIR, folder)
        
        if dry_run:
            print(f"[DRY RUN] Would move: {folder} -> _archive_cold/")
        else:
            try:
                shutil.move(src, dst)
            except Exception as e:
                print(f"Failed to move {folder}: {e}")

    if not dry_run:
        print(f"\nSuccessfully moved {len(to_move)} folders to {ARCHIVE_DIR}")

if __name__ == "__main__":
    import sys
    dry_run = "--execute" not in sys.argv
    main(dry_run)
