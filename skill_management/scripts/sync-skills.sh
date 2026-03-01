#!/bin/bash
# Sync skills inventory and generate notebook files

# Define paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)"
INVENTORY_SCRIPT="$SCRIPT_DIR/reorganize_inventory.py"
NOTEBOOK_SCRIPT="$SCRIPT_DIR/generate_notebook_files.py"

echo "========================================"
echo "Starting Skill Synchronization..."
echo "========================================"

# Step 1: Reorganize inventory and add missing skills
if [ -f "$INVENTORY_SCRIPT" ]; then
    echo "Running reorganize_inventory.py..."
    python3 "$INVENTORY_SCRIPT"
else
    echo "Error: $INVENTORY_SCRIPT not found."
    exit 1
fi

# Step 2: Generate notebook markdown files
if [ -f "$NOTEBOOK_SCRIPT" ]; then
    echo "Running generate_notebook_files.py..."
    python3 "$NOTEBOOK_SCRIPT"
else
    echo "Error: $NOTEBOOK_SCRIPT not found."
    exit 1
fi

# Step 3: Generate skill tree markdown
TREE_SCRIPT="$SCRIPT_DIR/generate_skill_tree.py"
if [ -f "$TREE_SCRIPT" ]; then
    echo "Running generate_skill_tree.py..."
    python3 "$TREE_SCRIPT"
else
    echo "Warning: $TREE_SCRIPT not found."
fi

echo "========================================"
echo "Sync complete! Notebook files are in ./notebooks and structure is in SKILLS_TREE.md"
echo "========================================"
