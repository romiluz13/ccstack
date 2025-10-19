# Quick Start Guide

Get started with the Production Skills Framework in 5 minutes.

---

## 🚀 Your First Session

### 1. Start Claude Code

```bash
# Navigate to your project
cd your-project

# Start Claude Code (if not running)
claude
```

### 2. Let Skills Auto-Activate

Simply describe what you want to do:

**Example 1: API Development**
```
I need to build a REST API for user authentication
```

**Auto-Activated Skills:**
- 🎯 `rest-design-principles`
- 🎯 `auth-patterns`
- 🎯 `api-security-patterns`
- 🎯 `input-validation`

**Example 2: Code Review**
```
Please review my pull request
```

**Auto-Activated Skills:**
- 🎯 `code-review-checklist`
- 🎯 `architecture-patterns`
- 🎯 `security-audit`
- 🎯 `test-coverage-strategy`

---

## 🎯 Using dotai Commands (Optional)

If you have `pnpm` installed, use dotai orchestration:

### Planning a Feature

```
/dotai:how user-authentication-system
```

Claude will:
1. Create a detailed plan
2. Break down into tasks
3. Auto-load relevant Skills
4. Wait for your approval

### Optimizing Context

```
/ctx auth
```

Loads only files related to "auth" - uses `context-optimizer` Skill.

### Restoring Session

```
/fb:session-start
```

Restores previous session memory - uses `session-continuity` Skill.

---

## 🔄 Complete Workflow Example

### Building a New Feature

**Step 1: Plan**
```
/dotai:how checkout-payment-flow
```

**Step 2: Implement**
```
Approved. Let's start with the API endpoints.
```

Skills auto-activate:
- `rest-design-principles`
- `api-security-patterns`
- `test-coverage-strategy`

**Step 3: Test**
```
Now write tests for the payment endpoints
```

Skills auto-activate:
- `tdd-workflow`
- `e2e-testing-patterns`

**Step 4: Review**
```
/dotai:review
```

Hooks trigger:
- 🪝 `post-edit-security.sh` (scans for issues)
- 🪝 `pre-commit-validate.sh` (checks standards)

**Step 5: Document**
```
Generate API documentation for these endpoints
```

Skills auto-activate:
- `api-documentation`
- `architecture-docs`

---

## 🪝 Understanding Hooks

Hooks run automatically - you don't trigger them manually.

### When You Edit a File

**PostToolUse Hook activates:**
```bash
⚠️  Security Scan: api/auth.ts
   • Potential hardcoded secret detected
   
💡 Tip: Review security-hardening Skills
```

### When You Commit

**PreCommit Hook activates:**
```bash
🔍 Pre-Commit Validation

⚠️  2 file(s) contain TODO/FIXME comments
⚠️  1 file(s) exceed 500 lines (consider splitting)

💡 Tip: Run /dotai:review before committing
```

---

## 🌐 MCP Servers

MCP servers enhance Claude's capabilities.

### Filesystem MCP (Always Active)

Allows Claude to:
- Read project files
- Write code
- Navigate directories

### GitHub MCP (Optional)

Set your token:
```bash
export GITHUB_TOKEN="ghp_your_token_here"
```

Then use:
```
Create a GitHub issue for the authentication bug
```

```
Review open PRs in this repository
```

### Task Master MCP (Optional)

```
Create a task list for the checkout flow
```

```
Show my current tasks
```

---

## 💡 Pro Tips

### 1. Let Skills Guide You

Don't memorize commands. Just describe your task:

❌ Bad:
```
/skill load rest-design-principles
```

✅ Good:
```
I need to design a REST API
```

### 2. Use Context Optimization

Before starting work:
```
/ctx payment-system
```

This loads only relevant files, reducing token usage by 80%+.

### 3. Combine Skills + Commands

```
/dotai:how api-refactoring
```

Claude will use both:
- `dotai:how` command (orchestration)
- `refactoring-strategies` Skill (guidance)

### 4. Trust the Hooks

Hooks protect you automatically:
- Security scanning on every edit
- Validation before commits
- Session restoration on startup

---

## 🎨 Real-World Examples

### Example 1: Fixing a Bug

**You:**
```
There's a bug in the checkout flow - users can't complete payment
```

**System:**
```
🪝 SessionStart Hook
✅ Previous session context restored
🎯 Auto-activated: code-review-checklist, refactoring-strategies
```

Claude helps you:
1. Find the bug
2. Suggest a fix
3. Write tests
4. Security scan the changes

### Example 2: Building a Feature

**You:**
```
/fb:session-start
/ctx graphql
/dotai:how user-profile-api
```

**System:**
```
🪝 SessionStart Hook
✅ Memory restored

/ctx graphql
✅ Context optimized (203 files → 18 files)
🎯 Auto-activated: token-efficiency, context-optimizer

/dotai:how user-profile-api
🎯 Auto-activated: graphql-schema-design, api-security-patterns
```

### Example 3: Code Review

**You:**
```
Review the changes in src/api/ before I commit
```

**System:**
```
🎯 Auto-activated: 
   • code-review-checklist
   • security-audit
   • test-coverage-strategy
   
[Claude performs thorough review]

🪝 PreCommit Hook will run when you commit
```

---

## 📚 Next Steps

1. **Explore Skills** - Check `plugins/*/skills/*/SKILL.md`
2. **Read Architecture** - See [STRUCTURE.md](./STRUCTURE.md)
3. **Customize** - Edit `CLAUDE.md` for your workflow
4. **Contribute** - See [CONTRIBUTING.md](../../CONTRIBUTING.md)

---

## ❓ Common Questions

**Q: Do I need to learn all Skills?**  
A: No! Skills activate automatically based on context.

**Q: Can I disable certain Skills?**  
A: Yes, edit `.claude-plugin/marketplace.json` and set `"enabled": false`.

**Q: Do hooks slow things down?**  
A: No, hooks are lightweight and run asynchronously.

**Q: Can I use this with existing dotai?**  
A: Yes! This system enhances dotai, doesn't replace it.

---

**Ready to build?** Just start describing your task! 🚀

