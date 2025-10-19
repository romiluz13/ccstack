# How MCP Setup Works - For End Users (Optional)

**⚠️ IMPORTANT: MCP is OPTIONAL - read this only if you want external tool integrations.**

**The Production Skills Framework works perfectly WITHOUT MCP!**

This guide explains MCP setup for advanced users who want additional tool integrations.

---

## 🤔 What is MCP?

MCP (Model Context Protocol) is an **optional** way to give Claude external tools:

**WITHOUT MCP (Default - Works Great!):**
- ✅ Skills activate automatically
- ✅ Hooks protect your code
- ✅ dotai commands work perfectly
- ✅ All core features functional

**WITH MCP (Optional Advanced):**
- ✅ External file operations
- ✅ GitHub API integration
- ✅ Task management tools

**Think of it like:** Your system is a complete workshop. MCP adds power tools (optional).

---

## 🎯 What This System Provides

Our system uses **3 MCP servers**:

1. **Filesystem MCP** (Required)
   - Lets Claude read your project files
   - Lets Claude create/edit files
   - Essential for development work

2. **GitHub MCP** (Optional)
   - Lets Claude create issues
   - Lets Claude create/manage PRs
   - Lets Claude review code on GitHub

3. **Task Master MCP** (Optional)
   - Lets Claude manage task lists
   - Lets Claude track progress
   - Workflow orchestration

---

## 📦 What's Already Done For You

**Good news:** We've already configured everything in `plugin.json`!

```json
{
  "mcpServers": {
    "filesystem": { "command": "npx", "args": [...] },
    "github": { "command": "npx", "args": [...] },
    "task-master": { "command": "npx", "args": [...] }
  }
}
```

**But...** Your editor/app needs to know about these servers!

---

## 🔧 What End Users Must Do

### The Problem

Claude Desktop and Cursor need a **configuration file** that tells them:
- "Hey, there are MCP servers available"
- "Here's how to run them"
- "Here's where to find them"

### The Solution

Create **one simple JSON file** in the right location.

---

## 📝 Step-by-Step Setup

### For Cursor Users (Recommended)

**Step 1: Create the config file**
```bash
mkdir -p .cursor
```

**Step 2: Add configuration**

Create `.cursor/mcp.json` with:
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "."]
    }
  }
}
```

**Step 3: Restart Cursor**

**That's it!** 30 seconds total.

---

### For Claude Desktop Users

**Step 1: Find your config file**

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Step 2: Edit the file**

Add the same JSON as above.

**Step 3: Restart Claude Desktop**

Done!

---

## 🧪 How to Test It Works

After setup, try this in Claude:

```
List all files in the current directory
```

**If it works:**
- ✅ Claude will list your actual files
- ✅ You'll see file names, sizes, etc.

**If it doesn't work:**
- ❌ Claude will say "I can't access files"
- ❌ Need to check config and restart

---

## 🚀 What Happens Behind the Scenes

When you ask Claude to read a file:

1. **Claude** receives your request
2. **Checks** available MCP servers (from config)
3. **Runs** `npx @modelcontextprotocol/server-filesystem .`
4. **Server** reads the file
5. **Returns** content to Claude
6. **Claude** processes and responds

**All automatic!** You just set up the config once.

---

## 🔑 Optional: GitHub Token (For GitHub MCP)

If you want GitHub integration:

### Why Needed?

GitHub requires authentication to:
- Create issues
- Create PRs
- Access private repos

### How to Get Token

1. Go to https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Select scopes: `repo`, `read:org`, `workflow`
4. Copy token

### How to Use Token

**Method 1: Environment Variable (Recommended)**
```bash
export GITHUB_TOKEN="ghp_your_token_here"
```

Add to `~/.bashrc` or `~/.zshrc` to make permanent.

**Method 2: In Config (Less Secure)**
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

**⚠️ Never commit tokens to git!**

---

## 💡 Why This Approach?

### Why Not Auto-Install?

**Problem:** Different editors/apps store configs in different places.

**Our Solution:**
1. We provide the MCP configuration in `plugin.json`
2. You copy it to your editor's config location
3. One-time setup, works forever

### Benefits

- ✅ **Flexible** - Works with Cursor, Claude Desktop, VS Code, etc.
- ✅ **Secure** - You control where tokens go
- ✅ **Portable** - Project-specific configs can be shared
- ✅ **Standard** - Uses official MCP format

---

## 🎨 Configuration Options

### Minimal (Just Filesystem)

**Best for:** Getting started quickly

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "."]
    }
  }
}
```

**Size:** 6 lines  
**Setup time:** 30 seconds  
**What you get:** File read/write access

---

### Standard (Filesystem + GitHub)

**Best for:** Most developers

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "."]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

**Size:** 13 lines  
**Setup time:** 2 minutes (+ token)  
**What you get:** Files + GitHub integration

---

### Complete (All 3 Servers)

**Best for:** Power users

See [MCP_SETUP.md](.claude-plugin/docs/MCP_SETUP.md) for full configuration.

**Size:** 20 lines  
**Setup time:** 5 minutes  
**What you get:** Everything!

---

## 🐛 Common Issues

### "Claude can't read files"

**Cause:** MCP not configured or not restarted

**Fix:**
1. Check config file exists
2. Check JSON is valid: `cat ~/.cursor/mcp.json | jq empty`
3. Restart editor completely

---

### "GitHub operations don't work"

**Cause:** Token not set or invalid

**Fix:**
1. Check token: `echo $GITHUB_TOKEN`
2. Test token: `curl -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/user`
3. Regenerate if needed

---

### "MCP servers slow"

**Cause:** Accessing too many files

**Fix:**
1. Limit scope: `"args": ["-y", "@modelcontextprotocol/server-filesystem", "./src"]`
2. Use `.gitignore` to exclude `node_modules/`

---

## 📚 Additional Resources

- **Complete Setup Guide:** [MCP_SETUP.md](.claude-plugin/docs/MCP_SETUP.md)
- **Installation Guide:** [INSTALLATION.md](.claude-plugin/docs/INSTALLATION.md)
- **Quick Start:** [README.md](README.md)

---

## 🎯 Summary

**What you need to do:**
1. Create **one JSON file** (`.cursor/mcp.json` or similar)
2. Add **4-20 lines** of configuration
3. **Restart** your editor
4. **Test** with a simple command

**Time required:** 30 seconds to 5 minutes

**What you get:**
- ✅ Claude can read/write files
- ✅ Skills work automatically
- ✅ Hooks protect your code
- ✅ Complete AI development system

**It's that simple!** 🚀

---

**Questions?** See [MCP_SETUP.md](.claude-plugin/docs/MCP_SETUP.md) or open an issue!

