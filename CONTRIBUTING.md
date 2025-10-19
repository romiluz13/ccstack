# Contributing to Production Skills Framework

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing.

---

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on the code, not the person
- Help others learn and grow

---

## How to Contribute

### 1. Report Bugs

**Before submitting:**
- Check existing issues
- Verify it's reproducible
- Gather relevant information

**Create an issue with:**
- Clear, descriptive title
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, Node version, Claude Code version)
- Error messages/logs

### 2. Suggest Features

**Feature requests should include:**
- Clear use case
- Why it's valuable
- How it fits the architecture
- Potential implementation approach

### 3. Submit Pull Requests

**PR Guidelines:**
- One feature/fix per PR
- Follow existing code style
- Add tests if applicable
- Update documentation
- Keep changes focused

---

## Development Setup

### Prerequisites

```bash
# Required
- Node.js 20+
- Git
- Your favorite editor

# Optional but recommended
- Python 3.x (for scripts)
- pnpm (for dotai commands)
```

### Setup Steps

```bash
# 1. Fork the repository
# Click "Fork" on GitHub

# 2. Clone your fork
git clone https://github.com/romiluz13/ccstack.git
cd ccstack

# 3. Add upstream remote
git remote add upstream https://github.com/romiluz13/ccstack.git

# 4. Create a branch
git checkout -b feature/your-feature-name

# 5. Make changes
# ... code, code, code ...

# 6. Test your changes
./.claude-plugin/scripts/verify.sh

# 7. Commit
git add .
git commit -m "feat: add amazing feature"

# 8. Push
git push origin feature/your-feature-name

# 9. Create Pull Request
# Go to GitHub and click "New Pull Request"
```

---

## Project Structure

```
ccstack/
├── .claude-plugin/          # Plugin configuration
│   ├── plugin.json          # Plugin metadata
│   ├── marketplace.json     # Marketplace config
│   ├── hooks/               # Hook configurations
│   ├── scripts/             # Installation/verification scripts
│   └── docs/                # Documentation
├── plugins/                 # Plugin collection
│   ├── [plugin-name]/
│   │   ├── README.md        # Plugin documentation
│   │   └── skills/
│   │       └── [skill-name]/
│   │           ├── SKILL.md # Skill definition
│   │           ├── scripts/ # Executable scripts
│   │           ├── references/ # Reference docs
│   │           └── assets/  # Templates, configs
├── examples/                # Usage examples
├── CLAUDE.md                # Master orchestrator
├── HYBRID_ARCHITECTURE.md   # Architecture docs
└── README.md                # Main documentation
```

---

## Adding a New Skill

### 1. Choose the Right Plugin

Skills are organized by purpose:
- `context-intelligence` - Context/token optimization
- `memory-management` - Session/knowledge management
- `code-quality-pro` - Architecture/refactoring
- `api-excellence` - API design/security
- `testing-automation` - Testing strategies
- `security-hardening` - Security best practices
- `documentation-excellence` - Documentation

### 2. Create Skill Structure

```bash
# Navigate to plugin
cd plugins/YOUR_PLUGIN/skills

# Create skill directory
mkdir your-skill-name
cd your-skill-name

# Create SKILL.md
touch SKILL.md
```

### 3. Write SKILL.md

```markdown
---
name: your-skill-name
description: Brief description for auto-activation
triggers:
  - keyword1
  - keyword2
---

# Your Skill Name

## When to Use This Skill
[Describe when this skill should activate]

## Core Concepts
[Main skill content]

## Quick Start
[Practical examples]
```

### 4. Add Optional Components

```bash
# For executable scripts
mkdir scripts
touch scripts/your-script.py

# For reference materials
mkdir references
touch references/deep-dive.md

# For templates/configs
mkdir assets
touch assets/template.yaml
```

### 5. Test the Skill

```bash
# Verify format
cat SKILL.md

# Run verification
cd ../../../../
./.claude-plugin/scripts/verify.sh
```

### 6. Document in Plugin README

Update `plugins/YOUR_PLUGIN/README.md`:
```markdown
### your-skill-name

**Purpose**: [What it does]
**Activates**: [When it activates]
**Contains**: [Scripts/references/assets]
```

---

## Adding a New Hook

### 1. Create Hook Script

```bash
cd .claude-plugin/scripts
touch your-hook.sh
chmod +x your-hook.sh
```

### 2. Write Hook Logic

```bash
#!/bin/bash
set -euo pipefail

# Your hook logic here
echo "Hook triggered!"

# Always exit 0 to not block workflow
exit 0
```

### 3. Configure in hooks.json

```json
{
  "hooks": {
    "YourEvent": [{
      "hooks": [{
        "type": "command",
        "command": "/bin/bash .claude-plugin/scripts/your-hook.sh"
      }]
    }]
  }
}
```

### 4. Test Hook

```bash
# Test manually
./.claude-plugin/scripts/your-hook.sh

# Verify configuration
cat .claude-plugin/hooks/hooks.json
```

---

## Code Style

### General Guidelines
- Use clear, descriptive names
- Add comments for complex logic
- Keep functions small and focused
- Follow existing patterns

### Shell Scripts
- Use `#!/bin/bash`
- Add `set -euo pipefail`
- Quote variables: `"$VAR"`
- Check file existence before operations

### Python Scripts
- Use Python 3 syntax
- Add type hints
- Include docstrings
- Handle errors gracefully

### Markdown
- Use headers (H1-H4)
- Add code blocks with language
- Keep lines under 100 characters
- Use bullet points for lists

---

## Testing

### Manual Testing

```bash
# 1. Install locally
./.claude-plugin/scripts/install.sh

# 2. Verify installation
./.claude-plugin/scripts/verify.sh

# 3. Test Skills activation
# Start Claude and describe a task

# 4. Test Hooks
# Edit a file, trigger hooks manually

# 5. Test MCP servers
npx -y @modelcontextprotocol/server-filesystem .
```

### Automated Testing (Future)

We're working on automated tests. For now, manual testing is required.

---

## Documentation

### Update These Files When:

**Adding a Skill:**
- Plugin README.md
- .claude-plugin/marketplace.json

**Adding a Hook:**
- .claude-plugin/hooks/hooks.json
- .claude-plugin/docs/STRUCTURE.md

**Changing Architecture:**
- HYBRID_ARCHITECTURE.md
- .claude-plugin/docs/STRUCTURE.md

**Adding Features:**
- README.md
- .claude-plugin/docs/QUICKSTART.md

---

## Commit Message Format

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `style`: Code style (formatting)
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance

**Examples:**
```
feat(skills): add graphql-schema-design skill

Add new skill for GraphQL schema design best practices.
Includes schema validation patterns and resolver optimization.

Closes #123
```

```
fix(hooks): prevent security scan false positives

Update regex in post-edit-security.sh to reduce false positives
for password variable names vs actual hardcoded passwords.
```

---

## Pull Request Checklist

Before submitting your PR:

- [ ] Code follows project style
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] Verification script passes
- [ ] Commit messages follow convention
- [ ] PR description explains changes
- [ ] Related issues linked

---

## Questions?

- **Issues**: https://github.com/romiluz13/ccstack/issues
- **Discussions**: https://github.com/romiluz13/ccstack/discussions

---

Thank you for contributing! 🎉

