#!/bin/bash

# Installation Script for Production Skills Framework
# Sets up the system and verifies all components

set -euo pipefail

echo ""
echo "🚀 Production Skills Framework - Installation"
echo "=============================================="
echo ""

# Check Node.js version
if ! command -v node &> /dev/null; then
    echo "❌ Error: Node.js is not installed"
    echo "   Please install Node.js 20.x or later"
    exit 1
fi

NODE_VERSION=$(node --version | cut -d'v' -f2 | cut -d'.' -f1)
if [ "$NODE_VERSION" -lt 20 ]; then
    echo "⚠️  Warning: Node.js $NODE_VERSION detected. Version 20+ recommended"
fi

# Check for git
if ! command -v git &> /dev/null; then
    echo "⚠️  Warning: Git not installed. Some features may not work"
fi

echo "✅ Prerequisites check passed"
echo ""

# Make scripts executable
chmod +x .claude-plugin/scripts/*.sh
echo "✅ Scripts made executable"
echo ""

# Check for optional MCP servers
echo "📦 Checking optional dependencies..."
if command -v gh &> /dev/null; then
    echo "   ✅ GitHub CLI installed (MCP GitHub server ready)"
else
    echo "   ℹ️  GitHub CLI not installed (MCP GitHub server optional)"
fi

if command -v pnpm &> /dev/null; then
    echo "   ✅ pnpm installed (dotai commands available)"
else
    echo "   ℹ️  pnpm not installed (dotai commands optional)"
    echo "      Install: npm install -g pnpm"
fi

echo ""
echo "📊 System Inventory:"
PLUGIN_COUNT=$(find plugins -name "README.md" 2>/dev/null | wc -l | tr -d ' ')
SKILL_COUNT=$(find plugins -name "SKILL.md" 2>/dev/null | wc -l | tr -d ' ')
SCRIPT_COUNT=$(find plugins -name "*.py" 2>/dev/null | wc -l | tr -d ' ')
HOOK_COUNT=$(ls -1 .claude-plugin/scripts/*.sh 2>/dev/null | wc -l | tr -d ' ')

echo "   • Plugins: $PLUGIN_COUNT"
echo "   • Skills: $SKILL_COUNT"
echo "   • Scripts: $SCRIPT_COUNT"
echo "   • Hooks: $HOOK_COUNT"
echo ""

# Create symlinks if needed
if [ ! -f "AGENTS.md" ] && [ -f "CLAUDE.md" ]; then
    ln -s CLAUDE.md AGENTS.md
    echo "✅ Created AGENTS.md symlink"
fi

echo ""
echo "✨ Installation Complete!"
echo ""
echo "Next steps:"
echo "  1. Review CLAUDE.md for system overview"
echo "  2. Check HYBRID_ARCHITECTURE.md for integration patterns"
echo "  3. Run: /plugin verify production-skills-framework"
echo ""
echo "Quick start:"
echo "  • Type your task to begin (Skills auto-activate)"
echo "  • Use /dotai:how for planning workflows"
echo "  • Use /ctx for context optimization"
echo ""

