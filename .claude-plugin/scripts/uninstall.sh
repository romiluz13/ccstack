#!/bin/bash

# Uninstallation Script for Production Skills Framework
# Safely removes the system and cleans up

set -euo pipefail

echo ""
echo "🗑️  Production Skills Framework - Uninstallation"
echo "==============================================="
echo ""

# Confirm uninstallation
read -p "Are you sure you want to uninstall? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Uninstallation cancelled"
    exit 0
fi

echo "Removing system..."

# Remove symlinks
if [ -L "AGENTS.md" ]; then
    rm AGENTS.md
    echo "✅ Removed AGENTS.md symlink"
fi

# Note: We don't delete the actual plugin files,
# as the user may want to keep custom Skills/scripts
echo ""
echo "⚠️  Note: Plugin files kept in place"
echo "   To completely remove, manually delete the production/ directory"
echo ""

echo "✅ Uninstallation complete"
echo ""

