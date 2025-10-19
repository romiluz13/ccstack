# MCP Servers Setup Guide (Optional)

**⚠️ IMPORTANT: This is an OPTIONAL advanced feature!**

**The Production Skills Framework works perfectly WITHOUT MCP servers.**

This guide is only for users who want to extend Claude with external tool integrations.

---

## What are MCP Servers?

MCP servers are **optional** external tools that enhance Claude's capabilities:
- **Filesystem MCP** - Read/write project files
- **GitHub MCP** - Manage issues, PRs, repositories  
- **Task Master MCP** - Workflow orchestration

**You do NOT need these for:**
- ✅ Skills activation (auto-loaded)
- ✅ Hooks automation (runs automatically)
- ✅ dotai commands (all work without MCP)
- ✅ All core functionality

**Only set up MCP if you specifically need these external integrations.**

---

## 🎯 Quick Setup (Choose Your Tool)

### Option 1: Cursor (Recommended for Development)

Cursor has two configuration options:

#### A. Global Configuration (All Projects)
```bash
# Edit global config
nano ~/.cursor/mcp.json
```

#### B. Project-Specific (This Project Only)
```bash
# Create project config
mkdir -p .cursor
nano .cursor/mcp.json
```

**Add this configuration:**
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "."],
      "description": "File system access for Claude"
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "description": "GitHub integration",
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "YOUR_GITHUB_TOKEN_HERE"
      }
    },
    "task-master": {
      "command": "npx",
      "args": ["-y", "@eyaltoledano/task-master", "mcp"],
      "description": "Task management"
    }
  }
}
```

---

### Option 2: Claude Desktop (For General Use)

#### macOS
```bash
# Edit Claude Desktop config
nano ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

#### Windows
```powershell
# Edit Claude Desktop config
notepad %APPDATA%\Claude\claude_desktop_config.json
```

#### Linux
```bash
# Edit Claude Desktop config
nano ~/.config/Claude/claude_desktop_config.json
```

**Add this configuration:**
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/your/project"],
      "description": "File system access"
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "description": "GitHub integration",
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "YOUR_TOKEN"
      }
    }
  }
}
```

**⚠️ Important:** Replace `/path/to/your/project` with your actual project path!

---

## 🔑 Setting Up GitHub Token (Optional)

The GitHub MCP server requires a personal access token:

### 1. Create Token on GitHub

1. Go to https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Name it: `Claude MCP Access`
4. Select scopes:
   - ✅ `repo` (Full control of private repositories)
   - ✅ `read:org` (Read org data)
   - ✅ `workflow` (Update GitHub Action workflows)
5. Click "Generate token"
6. **Copy the token immediately** (you won't see it again!)

### 2. Add Token to Configuration

#### Option A: Environment Variable (Recommended)

```bash
# Add to ~/.bashrc or ~/.zshrc
export GITHUB_TOKEN="ghp_your_token_here"

# Reload shell
source ~/.zshrc  # or source ~/.bashrc
```

#### Option B: Direct in Config (Less Secure)

Replace `"YOUR_GITHUB_TOKEN_HERE"` in the MCP configuration with your actual token.

**⚠️ Security Warning:** Never commit tokens to git!

---

## ✅ Verifying MCP Setup

### For Cursor

1. **Restart Cursor** completely
2. **Check Settings:**
   - Open Settings (Cmd+, or Ctrl+,)
   - Search for "MCP"
   - Verify servers are listed

3. **Test in Chat:**
   ```
   List files in the current directory
   ```
   
   If filesystem MCP works, Claude will list your files!

### For Claude Desktop

1. **Restart Claude Desktop** completely
2. **Test with a prompt:**
   ```
   Can you read the README.md file in my current project?
   ```

3. **Check for errors:**
   - Look for MCP-related errors in responses
   - Check console logs if available

---

## 🔧 Minimal Configuration (Just Filesystem)

If you only want file access (required):

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

This is the **minimum required** for the system to work!

---

## 📁 Configuration File Locations Reference

### Quick Reference Table

| Tool | OS | Config File Location |
|------|----|--------------------|
| **Cursor** | All | `~/.cursor/mcp.json` (global) |
| **Cursor** | All | `.cursor/mcp.json` (project) |
| **Claude Desktop** | macOS | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| **Claude Desktop** | Windows | `%APPDATA%\Claude\claude_desktop_config.json` |
| **Claude Desktop** | Linux | `~/.config/Claude/claude_desktop_config.json` |
| **Claude Code** | All | `~/.claude.json` |

---

## 🐛 Troubleshooting

### MCP Servers Not Loading

**Symptom:** Claude can't read files or access GitHub

**Solutions:**
1. **Check Node.js version:**
   ```bash
   node --version  # Should be 20+
   ```

2. **Verify config syntax:**
   ```bash
   # Test JSON validity
   cat ~/.cursor/mcp.json | jq empty
   # or
   cat ~/Library/Application\ Support/Claude/claude_desktop_config.json | jq empty
   ```

3. **Check server installation:**
   ```bash
   # Test filesystem server manually
   npx -y @modelcontextprotocol/server-filesystem .
   ```

4. **Restart your editor/app completely**

### GitHub MCP Not Working

**Symptom:** GitHub operations fail or are unavailable

**Check:**
1. **Token is set:**
   ```bash
   echo $GITHUB_TOKEN  # Should show your token
   ```

2. **Token has correct scopes:**
   - Go to https://github.com/settings/tokens
   - Verify `repo` scope is enabled

3. **Test token:**
   ```bash
   curl -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/user
   ```

### Filesystem MCP Can't Find Files

**Symptom:** "File not found" errors

**Solutions:**
1. **Check working directory:**
   - For Cursor project config: Uses project root
   - For global config: Specify absolute path

2. **Use absolute paths in config:**
   ```json
   {
     "mcpServers": {
       "filesystem": {
         "command": "npx",
         "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/you/projects/myproject"]
       }
     }
   }
   ```

### Performance Issues

**Symptom:** Slow responses when using MCP

**Solutions:**
1. **Limit filesystem scope:**
   ```json
   "args": ["-y", "@modelcontextprotocol/server-filesystem", "./src"]
   ```

2. **Exclude large directories:**
   - Edit `.gitignore` to exclude `node_modules/`, `dist/`, etc.
   - MCP respects `.gitignore`

---

## 🚀 Advanced Configuration

### Multiple Filesystem Servers

```json
{
  "mcpServers": {
    "filesystem-src": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "./src"]
    },
    "filesystem-docs": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "./docs"]
    }
  }
}
```

### Custom Environment Variables

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}",
        "GITHUB_API_URL": "https://api.github.com"
      }
    }
  }
}
```

### Project-Specific GitHub Org

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github",
        "--org",
        "yourorg"
      ]
    }
  }
}
```

---

## 📚 MCP Server Documentation

- **Filesystem**: https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem
- **GitHub**: https://github.com/modelcontextprotocol/servers/tree/main/src/github
- **Task Master**: https://github.com/eyaltoledano/task-master

---

## ✨ What You Get After Setup

Once MCP is configured, Claude can:

### With Filesystem MCP:
- ✅ Read any project file
- ✅ Write new files
- ✅ Edit existing files
- ✅ Navigate directories
- ✅ Search file contents

### With GitHub MCP:
- ✅ Create issues
- ✅ Create pull requests
- ✅ Comment on PRs
- ✅ List repositories
- ✅ Check PR status
- ✅ Review code

### With Task Master MCP:
- ✅ Create task lists
- ✅ Track progress
- ✅ Generate reports
- ✅ Manage workflows

---

## 🎯 Next Steps

After setting up MCP:

1. **Test the system:**
   ```bash
   ./.claude-plugin/scripts/verify.sh
   ```

2. **Try a command:**
   ```
   Read the CLAUDE.md file and explain the system
   ```

3. **Explore Skills:**
   - Skills will auto-activate based on context
   - MCP servers provide the tools
   - Skills provide the guidance

---

## 💡 Pro Tips

1. **Use project-specific config** (`.cursor/mcp.json`) for team sharing
2. **Add config to .gitignore** if it contains tokens
3. **Use environment variables** for sensitive data
4. **Restart your editor** after config changes
5. **Test one server at a time** when troubleshooting

---

**Questions?** Open an issue: https://github.com/yourusername/production-skills-framework/issues

