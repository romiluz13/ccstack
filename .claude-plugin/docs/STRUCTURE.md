# System Structure & Architecture

Complete technical reference for the Production Skills Framework.

---

## 📁 Directory Structure

```
ccstack/
├── .claude-plugin/              # Plugin configuration
│   ├── plugin.json              # Plugin metadata + MCP servers
│   ├── marketplace.json         # Marketplace metadata
│   ├── hooks/
│   │   └── hooks.json           # Hooks configuration
│   ├── scripts/
│   │   ├── install.sh           # Installation script
│   │   ├── uninstall.sh         # Uninstallation script
│   │   ├── verify.sh            # Verification script
│   │   ├── session-start.sh     # SessionStart hook
│   │   ├── post-edit-security.sh # PostToolUse hook
│   │   └── pre-commit-validate.sh # PreCommit hook
│   └── docs/
│       ├── INSTALLATION.md      # Installation guide
│       ├── QUICKSTART.md        # Quick start guide
│       └── STRUCTURE.md         # This file
├── plugins/                     # Plugin collection
│   ├── context-intelligence/    # Context & token optimization
│   │   ├── README.md
│   │   └── skills/
│   │       ├── context-optimizer/
│   │       │   ├── SKILL.md
│   │       │   ├── scripts/
│   │       │   │   └── analyze-context.py
│   │       │   └── references/
│   │       ├── token-efficiency/
│   │       │   ├── SKILL.md
│   │       │   └── scripts/
│   │       │       └── token-counter.py
│   │       └── semantic-search/
│   │           └── SKILL.md
│   ├── memory-management/       # Session & knowledge management
│   │   ├── README.md
│   │   └── skills/
│   │       ├── session-continuity/
│   │       │   └── SKILL.md
│   │       ├── knowledge-retention/
│   │       │   └── SKILL.md
│   │       └── context-history/
│   │           └── SKILL.md
│   ├── code-quality-pro/        # Architecture & refactoring
│   │   ├── README.md
│   │   └── skills/
│   │       ├── architecture-patterns/
│   │       │   ├── SKILL.md
│   │       │   └── references/
│   │       ├── refactoring-strategies/
│   │       │   └── SKILL.md
│   │       └── code-review-checklist/
│   │           └── SKILL.md
│   ├── api-excellence/          # API design & security
│   │   ├── README.md
│   │   └── skills/
│   │       ├── rest-design-principles/
│   │       │   ├── SKILL.md
│   │       │   └── assets/
│   │       │       └── rest-api-template.yaml
│   │       ├── graphql-schema-design/
│   │       │   └── SKILL.md
│   │       └── api-security-patterns/
│   │           └── SKILL.md
│   ├── testing-automation/      # Testing strategies
│   │   ├── README.md
│   │   └── skills/
│   │       ├── test-coverage-strategy/
│   │       │   └── SKILL.md
│   │       ├── tdd-workflow/
│   │       │   └── SKILL.md
│   │       └── e2e-testing-patterns/
│   │           └── SKILL.md
│   ├── security-hardening/      # Security best practices
│   │   ├── README.md
│   │   └── skills/
│   │       ├── auth-patterns/
│   │       │   ├── SKILL.md
│   │       │   └── references/
│   │       │       └── oauth2-jwt-patterns.md
│   │       ├── input-validation/
│   │       │   └── SKILL.md
│   │       └── security-audit/
│   │           ├── SKILL.md
│   │           └── scripts/
│   │               └── owasp-checker.py
│   └── documentation-excellence/ # Documentation
│       ├── README.md
│       └── skills/
│           ├── api-documentation/
│           │   └── SKILL.md
│           ├── architecture-docs/
│           │   ├── SKILL.md
│           │   └── references/
│           │       └── adr-template.md
│           └── code-comments/
│               └── SKILL.md
├── examples/                    # Usage examples
│   ├── hybrid-workflow-example.md
│   ├── skills-activation-demo.md
│   └── dotai-skills-integration.md
├── CLAUDE.md                    # Master orchestrator
├── HYBRID_ARCHITECTURE.md       # Architecture deep dive
├── README.md                    # Main documentation
├── LICENSE                      # MIT License
├── CONTRIBUTING.md              # Contribution guidelines
└── .gitignore                   # Git ignore patterns
```

---

## 🏗️ Architecture Layers

### Layer 1: Human Control (You)
- **Role**: Decision maker
- **Actions**: Issue commands, describe tasks
- **Control**: Full control over what happens

### Layer 2: Sub-Agents (dotai Commands)
- **Role**: Workflow orchestration
- **Activation**: Manual (`/dotai:how`, `/ctx`, `/fb:session-start`)
- **Purpose**: Structured workflows, memory, context

### Layer 3: Skills (Auto-Enhancement)
- **Role**: Capability enhancement
- **Activation**: Automatic (based on context)
- **Purpose**: Best practices, patterns, guidance

### Layer 4: Hooks (Auto-Protection)
- **Role**: Safety & validation
- **Activation**: Automatic (on events)
- **Purpose**: Security, quality gates

### Layer 5: MCP Servers (Tool Access)
- **Role**: External integrations
- **Activation**: Automatic (when needed)
- **Purpose**: File access, GitHub, tasks

---

## 🔄 Data Flow

```
1. You type a request
   ↓
2. CLAUDE.md orchestrates
   ↓
3. Skills auto-activate (if relevant)
   ↓
4. Sub-agents execute (if you invoke them)
   ↓
5. MCP servers provide tools (if needed)
   ↓
6. Claude generates response
   ↓
7. Hooks validate (PostToolUse, PreCommit)
   ↓
8. Result returned to you
```

---

## 📜 File Formats

### SKILL.md Format

```markdown
---
name: skill-name
description: Brief description for auto-activation
triggers:
  - keyword1
  - keyword2
---

# Skill Name

## When to Use This Skill
[Activation criteria]

## Core Concepts
[Main content]

## Quick Start
[Examples]
```

### plugin.json Format

```json
{
  "name": "plugin-name",
  "version": "1.0.0",
  "description": "Plugin description",
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["package-name"],
      "description": "Server description",
      "optional": false
    }
  }
}
```

### hooks.json Format

```json
{
  "hooks": {
    "SessionStart": [{
      "hooks": [{
        "type": "command",
        "command": "/bin/bash script.sh"
      }]
    }],
    "PostToolUse": [{
      "matcher": "Write|Edit|MultiEdit",
      "hooks": [{
        "type": "command",
        "command": "validation-command"
      }]
    }]
  }
}
```

---

## 🔌 Plugin Types

### Type 1: Orchestration Plugins
- **Purpose**: Workflow management
- **Example**: `dotai-enhanced`
- **Contains**: Commands (slash commands)
- **Activation**: Manual

### Type 2: Enhancement Plugins
- **Purpose**: Capability augmentation
- **Example**: `context-intelligence`, `code-quality-pro`
- **Contains**: Skills (SKILL.md files)
- **Activation**: Automatic

### Type 3: Hybrid Plugins
- **Purpose**: Both orchestration + enhancement
- **Example**: Your custom plugin
- **Contains**: Commands + Skills
- **Activation**: Manual + Automatic

---

## 🧩 Skill Components

### 1. SKILL.md (Required)
- Core skill logic
- Activation criteria
- Best practices

### 2. scripts/ (Optional)
- Executable Python/Shell scripts
- Example: `analyze-context.py`
- Provides tools for Claude

### 3. references/ (Optional)
- Deep reference material
- Example: `oauth2-jwt-patterns.md`
- Progressive disclosure

### 4. assets/ (Optional)
- Templates, configs
- Example: `rest-api-template.yaml`
- Ready-to-use resources

---

## 🪝 Hook Types & Events

### SessionStart
- **When**: Claude session begins
- **Purpose**: Load context, restore memory
- **Example**: `session-start.sh`

### PostToolUse
- **When**: After Claude uses a tool (Write/Edit/Bash)
- **Purpose**: Validate, scan, format
- **Example**: `post-edit-security.sh`

### PreCommit
- **When**: Before git commit
- **Purpose**: Quality checks, standards
- **Example**: `pre-commit-validate.sh`

### Stop
- **When**: Claude session ends
- **Purpose**: Save state, generate reports
- **Example**: `session-end.sh` (optional)

---

## 🌐 MCP Server Integration

### Filesystem MCP
- **Package**: `@modelcontextprotocol/server-filesystem`
- **Purpose**: File operations
- **Required**: Yes

### GitHub MCP
- **Package**: `@modelcontextprotocol/server-github`
- **Purpose**: GitHub integration
- **Required**: No
- **Requires**: `GITHUB_TOKEN` env var

### Task Master MCP
- **Package**: `@eyaltoledano/task-master`
- **Purpose**: Task management
- **Required**: No

---

## 🔧 Customization Points

### 1. Modify CLAUDE.md
Change orchestration logic:
- Add custom decision trees
- Update integration patterns
- Define new workflows

### 2. Create Custom Skills
Add to any plugin:
```bash
mkdir plugins/your-plugin/skills/your-skill
echo "# Your Skill" > plugins/your-plugin/skills/your-skill/SKILL.md
```

### 3. Add Custom Hooks
Edit `.claude-plugin/hooks/hooks.json`:
```json
{
  "hooks": {
    "YourEvent": [{
      "hooks": [{
        "type": "command",
        "command": "your-script.sh"
      }]
    }]
  }
}
```

### 4. Configure MCP Servers
Edit `.claude-plugin/plugin.json`:
```json
{
  "mcpServers": {
    "your-server": {
      "command": "your-command",
      "args": ["arg1", "arg2"]
    }
  }
}
```

---

## 📊 Token Efficiency

### Without Skills
- Average session: 80K-120K tokens
- Context: Everything loaded

### With Skills (Progressive Disclosure)
- Average session: 8K-15K tokens (83% reduction)
- Context: Only relevant Skills

### How It Works
1. Only SKILL.md loaded initially (~200 lines)
2. references/ loaded on demand
3. scripts/ executed when needed
4. Full detail only if requested

---

## 🧪 Testing Structure

### Verify Installation
```bash
./.claude-plugin/scripts/verify.sh
```

### Test Specific Skill
```bash
# Read the SKILL.md
cat plugins/context-intelligence/skills/context-optimizer/SKILL.md

# Run associated script (if exists)
python3 plugins/context-intelligence/skills/context-optimizer/scripts/analyze-context.py
```

### Test Hook
```bash
# Manually trigger hook
echo '{"tool_input":{"file_path":"test.js"}}' | \
  ./.claude-plugin/scripts/post-edit-security.sh test.js
```

### Test MCP Server
```bash
# Test filesystem MCP
npx -y @modelcontextprotocol/server-filesystem .
```

---

## 🚀 Performance Characteristics

| Component | Load Time | Memory | Token Impact |
|-----------|-----------|--------|--------------|
| CLAUDE.md | ~50ms | 20KB | ~400 tokens |
| Single Skill | ~10ms | 5KB | ~200 tokens |
| Hook | ~100ms | 2MB | 0 tokens |
| MCP Server | ~500ms | 50MB | 0 tokens |

---

## 📚 Further Reading

- [INSTALLATION.md](./INSTALLATION.md) - Setup guide
- [QUICKSTART.md](./QUICKSTART.md) - Usage examples
- [HYBRID_ARCHITECTURE.md](../../HYBRID_ARCHITECTURE.md) - Deep dive
- [CONTRIBUTING.md](../../CONTRIBUTING.md) - Development guide

---

**Questions?** Open an issue: https://github.com/romiluz13/ccstack/issues

