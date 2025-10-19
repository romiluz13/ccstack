#!/bin/bash

# Verification Script for Production Skills Framework
# Tests all components and reports health

set -euo pipefail

echo ""
echo "🔍 Production Skills Framework - Verification"
echo "============================================="
echo ""

ERRORS=0
WARNINGS=0

# Check core files
echo "📁 Checking core files..."
for file in "CLAUDE.md" "HYBRID_ARCHITECTURE.md" "README.md" ".claude-plugin/plugin.json" ".claude-plugin/hooks/hooks.json"; do
    if [ -f "$file" ]; then
        echo "   ✅ $file"
    else
        echo "   ❌ Missing: $file"
        ERRORS=$((ERRORS + 1))
    fi
done
echo ""

# Check plugins
echo "🔌 Checking plugins..."
PLUGIN_DIRS=$(find plugins -maxdepth 1 -type d ! -path plugins 2>/dev/null | sort)
if [ -z "$PLUGIN_DIRS" ]; then
    echo "   ❌ No plugins found"
    ERRORS=$((ERRORS + 1))
else
    PLUGIN_COUNT=0
    for dir in $PLUGIN_DIRS; do
        PLUGIN_COUNT=$((PLUGIN_COUNT + 1))
        PLUGIN_NAME=$(basename "$dir")
        if [ -f "$dir/README.md" ]; then
            echo "   ✅ $PLUGIN_NAME"
        else
            echo "   ⚠️  $PLUGIN_NAME (missing README.md)"
            WARNINGS=$((WARNINGS + 1))
        fi
    done
    echo "   Total: $PLUGIN_COUNT plugins"
fi
echo ""

# Check Skills
echo "✨ Checking Skills..."
SKILL_FILES=$(find plugins -name "SKILL.md" 2>/dev/null)
if [ -z "$SKILL_FILES" ]; then
    echo "   ❌ No Skills found"
    ERRORS=$((ERRORS + 1))
else
    SKILL_COUNT=$(echo "$SKILL_FILES" | wc -l | tr -d ' ')
    echo "   ✅ Found $SKILL_COUNT Skills"
    
    # Validate SKILL.md format
    INVALID_SKILLS=0
    while IFS= read -r skill_file; do
        if ! grep -q "^# " "$skill_file" 2>/dev/null; then
            INVALID_SKILLS=$((INVALID_SKILLS + 1))
        fi
    done <<< "$SKILL_FILES"
    
    if [ $INVALID_SKILLS -gt 0 ]; then
        echo "   ⚠️  $INVALID_SKILLS Skill(s) may have formatting issues"
        WARNINGS=$((WARNINGS + 1))
    fi
fi
echo ""

# Check scripts
echo "🔧 Checking scripts..."
PYTHON_SCRIPTS=$(find plugins -name "*.py" 2>/dev/null | wc -l | tr -d ' ')
if [ "$PYTHON_SCRIPTS" -gt 0 ]; then
    echo "   ✅ Found $PYTHON_SCRIPTS Python script(s)"
    
    # Check if Python is available
    if ! command -v python3 &> /dev/null; then
        echo "   ⚠️  Python 3 not installed (scripts won't run)"
        WARNINGS=$((WARNINGS + 1))
    fi
else
    echo "   ℹ️  No Python scripts found"
fi
echo ""

# Check hooks
echo "🪝 Checking hooks..."
if [ -f ".claude-plugin/hooks/hooks.json" ]; then
    echo "   ✅ hooks.json configured"
    
    # Verify hook scripts exist
    for script in "session-start.sh" "post-edit-security.sh" "pre-commit-validate.sh"; do
        if [ -x ".claude-plugin/scripts/$script" ]; then
            echo "   ✅ $script (executable)"
        elif [ -f ".claude-plugin/scripts/$script" ]; then
            echo "   ⚠️  $script (not executable)"
            WARNINGS=$((WARNINGS + 1))
        else
            echo "   ❌ Missing: $script"
            ERRORS=$((ERRORS + 1))
        fi
    done
else
    echo "   ❌ hooks.json missing"
    ERRORS=$((ERRORS + 1))
fi
echo ""

# Check MCP configuration (optional)
echo "🌐 Checking MCP configuration..."
if grep -q "mcpServers" ".claude-plugin/plugin.json" 2>/dev/null; then
    MCP_COUNT=$(grep -o "\"command\":" ".claude-plugin/plugin.json" | wc -l | tr -d ' ')
    echo "   ✅ MCP servers configured (optional)"
    echo "   • Configured servers: $MCP_COUNT"
else
    echo "   ℹ️  No MCP servers (optional - not required)"
fi
echo ""

# Summary
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
    echo "✅ System Status: HEALTHY"
    echo ""
    echo "All components verified successfully!"
    exit 0
elif [ $ERRORS -eq 0 ]; then
    echo "⚠️  System Status: DEGRADED"
    echo ""
    echo "Warnings: $WARNINGS"
    echo "System is functional but has minor issues"
    exit 0
else
    echo "❌ System Status: BROKEN"
    echo ""
    echo "Errors: $ERRORS"
    echo "Warnings: $WARNINGS"
    echo ""
    echo "Please fix errors before using the system"
    exit 1
fi

