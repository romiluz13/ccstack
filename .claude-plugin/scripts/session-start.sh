#!/bin/bash

# Session Start Hook for Production System
# Restores context, loads Skills, and prepares environment

set -euo pipefail

echo "🚀 Production System - Session Start"
echo ""

# 1. Load CLAUDE.md context
if [ -f "CLAUDE.md" ]; then
    echo "✅ CLAUDE.md orchestrator loaded"
else
    echo "⚠️  CLAUDE.md not found in current directory"
fi

# 2. Check for HYBRID_ARCHITECTURE.md
if [ -f "HYBRID_ARCHITECTURE.md" ]; then
    echo "✅ Hybrid architecture patterns loaded"
fi

# 3. Display available plugins
PLUGIN_COUNT=$(find plugins -name "README.md" 2>/dev/null | wc -l | tr -d ' ')
SKILL_COUNT=$(find plugins -name "SKILL.md" 2>/dev/null | wc -l | tr -d ' ')
SCRIPT_COUNT=$(find plugins -name "*.py" 2>/dev/null | wc -l | tr -d ' ')

echo ""
echo "📦 System Components:"
echo "   • Plugins: $PLUGIN_COUNT"
echo "   • Skills: $SKILL_COUNT"
echo "   • Scripts: $SCRIPT_COUNT"
echo ""

# 4. Check for dotai commands (if available)
if command -v pnpm &> /dev/null; then
    echo "✅ dotai commands available (pnpm installed)"
    echo "   Use: /dotai:how, /ctx, /fb:session-start"
else
    echo "ℹ️  dotai commands require pnpm installation"
fi

echo ""
echo "🎯 Ready! Skills will auto-activate based on context."
echo "   Type your task to begin."
echo ""

