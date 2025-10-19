# Installation Guide

## Prerequisites

### Required
- **Node.js 20.x or later** - [Download](https://nodejs.org/)
- **npm or pnpm** - Comes with Node.js

### Optional (Recommended)
- **Git** - For version control
- **GitHub CLI (`gh`)** - For GitHub MCP server
- **pnpm** - For dotai commands: `npm install -g pnpm`
- **Python 3.x** - For Python scripts in Skills

---

## Installation Methods

### Method 1: Clone from GitHub (Recommended)

```bash
# Clone the repository
git clone https://github.com/romiluz13/ccstack.git

# Navigate to directory
cd ccstack

# Run installation
./.claude-plugin/scripts/install.sh
```

### Method 2: Claude Code Plugin Command

```bash
# Add marketplace
/plugin marketplace add https://github.com/romiluz13/ccstack

# Install plugin
/plugin install ccstack
```

### Method 3: Claude Plugins CLI

```bash
# One-command installation
npx claude-plugins install ccstack
```

---

## Post-Installation

### 1. Verify Installation

```bash
./.claude-plugin/scripts/verify.sh
```

You should see:
- ✅ All core files present
- ✅ 7 plugins loaded
- ✅ 21 Skills activated
- ✅ Hooks configured

### 2. Test the System

Start a new Claude session and type:

```
Hello! I'd like to build a REST API with authentication
```

You should see Skills automatically activate:
- 🎯 `rest-design-principles` Skill loaded
- 🎯 `auth-patterns` Skill loaded
- 🎯 `api-security-patterns` Skill loaded

---

## Troubleshooting

### Hooks Not Working

```bash
# Make sure scripts are executable
chmod +x .claude-plugin/scripts/*.sh

# Check hooks.json
cat .claude-plugin/hooks/hooks.json
```

### Skills Not Activating

Check:
1. CLAUDE.md exists in project root
2. Plugins directory structure is correct
3. SKILL.md files have proper format

### Python Scripts Failing

```bash
# Check Python installation
python3 --version

# Install required packages
pip3 install tiktoken  # For token counting
```

---

## Uninstallation

```bash
./.claude-plugin/scripts/uninstall.sh
```

This will remove symlinks but keep plugin files for safety.

---

## Next Steps

After installation:
1. Read [QUICKSTART.md](./QUICKSTART.md) for usage examples
2. Review [STRUCTURE.md](./STRUCTURE.md) for architecture
3. Check the main [README.md](../../README.md) for features

---

## Advanced: Optional MCP Integration

**The system works perfectly without MCP servers.**

However, if you want to extend Claude's capabilities with external tools, you can optionally configure MCP servers:

**What MCP Provides:**
- File system access (read/write files)
- GitHub integration (issues, PRs)
- Task management tools

**Setup Guide:**
See [MCP_SETUP.md](./MCP_SETUP.md) for complete instructions.

**Note:** MCP is **NOT required** for:
- Skills activation
- Hooks automation
- dotai commands
- All core functionality

Only add MCP if you specifically need external tool integrations.

---

## Support

- **Issues**: https://github.com/romiluz13/ccstack/issues
- **Discussions**: https://github.com/romiluz13/ccstack/discussions
- **Documentation**: https://github.com/romiluz13/ccstack/wiki

