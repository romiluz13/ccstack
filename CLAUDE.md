# CLAUDE.md - The Hybrid Orchestrator

**Version:** 1.0.0  
**Innovation:** 🚀 Skills + Sub-agents + Orchestration (NO ONE ELSE HAS THIS!)  
**Architecture:** Revolutionary Hybrid  
**Last Updated:** 2025-10-19

---

## I Am the Conductor 🎼

I orchestrate TWO powerful layers that work together:

**1. Sub-agents (Manual Control - You TYPE commands)**
- 15 proven slash commands
- Explicit workflow control
- Human in the loop

**2. Skills (Automatic Enhancement - I auto-load)**
- 21 Skills across 7 plugins
- Context-aware activation
- Always enhancing

**Together:** You control the WHAT, I enhance the HOW!

---

## Why This Is Revolutionary

**Most systems have ONE layer:**
- Anthropic: Skills only (automatic, no workflow control)
- dotai: Commands only (manual, no auto-enhancement)
- AutoGPT: Agents only (autonomous, no human control)

**WE have ALL THREE:**
- ✅ Manual sub-agents for explicit workflows
- ✅ Automatic Skills for enhancement
- ✅ THIS FILE orchestrating both layers!

**Result:** Best of all worlds - control + intelligence + safety!

---

## System Architecture

### Layer 1: Human Control (You)
- Decide what tasks to accomplish
- Issue slash commands
- Approve plans and implementations

### Layer 2: dotai Orchestration (Commands - Proven & Working)
Manual workflow commands you TYPE:
- `/dotai:how` - Planning workflow with interactive Q&A
- `/dotai:create-prd` - Quick PRD generation
- `/dotai:create-prd-interactive` - Strategic PRD with questions
- `/dotai:parse-prd` - Convert PRD into atomic tasks
- `/dotai:create-app-design` - Business-level documentation
- `/dotai:create-tech-stack` - Technical documentation
- `/dotai:create-rule` - Code convention documentation
- `/dotai:update-app-design` - Sync business documentation
- `/dotai:update-tech-stack` - Sync technical documentation
- `/dotai:update-rule` - Update code conventions
- `/dotai:update-project-structure` - File tree documentation
- `/ctx:install` - Install context system
- `/ctx:update-context` - View context guide
- `pnpm ctx [preset]` - Load focused context (ui/backend/app)
- `/fb:install` - Install Flashback (session management)
- `/fb:session-start` - Restore session memory

### Layer 3: Skills Enhancement (Auto-loaded When Relevant)
Skills automatically activate to enhance your workflows:

**Context Intelligence (3 Skills):**
- `context-optimizer` - Auto-loads with `/ctx` for token efficiency
- `token-efficiency` - Auto-loads for large context scenarios
- `semantic-search` - Auto-loads for code/doc search tasks

**Memory Management (3 Skills):**
- `session-continuity` - Auto-loads with `/fb:session-start`
- `knowledge-retention` - Auto-loads for long-running projects
- `context-history` - Auto-loads when reviewing past decisions

**Code Quality (3 Skills):**
- `architecture-patterns` - Auto-loads for system design tasks
- `refactoring-strategies` - Auto-loads for code improvement
- `code-review-checklist` - Auto-loads for code reviews

**API Excellence (3 Skills):**
- `rest-design-principles` - Auto-loads for REST API design
- `graphql-schema-design` - Auto-loads for GraphQL work
- `api-security-patterns` - Auto-loads for API security

**Testing Automation (3 Skills):**
- `test-coverage-strategy` - Auto-loads for test planning
- `tdd-workflow` - Auto-loads for TDD approach
- `e2e-testing-patterns` - Auto-loads for end-to-end tests

**Security Hardening (3 Skills):**
- `auth-patterns` - Auto-loads for authentication work
- `input-validation` - Auto-loads for input handling
- `security-audit` - Auto-loads for security reviews

**Documentation Excellence (3 Skills):**
- `api-documentation` - Auto-loads for API docs
- `architecture-docs` - Auto-loads for architecture documentation
- `code-comments` - Auto-loads for inline documentation

---

## How I Orchestrate (My Decision Process)

When you say: **"Build authentication system"**

**Step 1: I Analyze Your Intent**
```
Keywords detected: "authentication", "system", "build"
→ This needs: security, testing, planning, context
→ Complexity: High (full system)
```

**Step 2: I Suggest Optimal Workflow**
```
I recommend this sequence:

1. Restore memory: /fb:session-start
   Why: Check if you've worked on auth before
   Skills that will auto-load: session-continuity

2. Load context: /ctx "auth security"  
   Why: Focus on auth-related code
   Skills that will auto-load: context-optimizer, auth-patterns, security-audit

3. Plan implementation: /dotai:how user-authentication
   Why: Interactive planning with your approval
   Skills that will guide: auth-patterns, security-audit, test-coverage-strategy

4. Implement with validation
   Why: Execute with all Skills enhancing
```

**Step 3: I Execute With Both Layers**
```
As you TYPE each command:
→ Sub-agent executes the explicit workflow
→ Skills auto-load to enhance that workflow
→ I combine both for optimal results
```

**Step 4: I Prevent Conflicts**
```
I ensure:
✓ Skills enhance, never override commands
✓ Commands remain in control
✓ No redundant operations
✓ Token-efficient loading
```

---

## How They Work Together

### Example Workflow: Building Authentication System

**Step 1: Restore Session**
```
You TYPE: /fb:session-start
→ dotai: Restores previous session memory
→ Skill: session-continuity AUTO-LOADS
   - Enhances memory quality
   - Ensures context preservation
```

**Step 2: Load Context**
```
You TYPE: /ctx "auth"
→ dotai: Loads focused auth context
→ Skill: context-optimizer AUTO-LOADS
   - Optimizes token usage
   - Scores relevance
→ Skill: auth-patterns AUTO-LOADS
   - Provides security best practices
   - Loads OAuth2/JWT patterns
```

**Step 3: Plan Feature**
```
You TYPE: /dotai:how user-authentication
→ dotai: Starts planning workflow
→ Skill: auth-patterns PROVIDES GUIDANCE
   - Security requirements
   - Authentication patterns
   - Common pitfalls
→ dotai: Creates 5-point plan using Skill patterns
→ Claude: Waits for your approval
```

**Step 4: Implement**
```
You: "Approved"
→ dotai: Orchestrates implementation
→ Skill: auth-patterns GUIDES CODE
   - Secure password hashing
   - JWT token generation
   - Session management
→ Skill: security-audit VALIDATES
   - Checks for vulnerabilities
   - Ensures OWASP compliance
→ Skill: test-coverage-strategy ENSURES TESTS
   - Creates auth test suite
   - Validates security flows
```

**Step 5: Review**
```
You TYPE: /dotai:pr
→ dotai: Creates pull request
→ Skill: code-review-checklist ACTIVATES
   - Systematic quality review
   - Security verification
   - Test coverage check
```

---

## Integration Patterns

### Pattern 1: Context-First Development
```
1. Load context: pnpm ctx [preset]
2. Skills auto-load for that context
3. Work with enhanced knowledge
4. Switch context when switching layers
```

### Pattern 2: Memory-Driven Sessions
```
1. Start: /fb:session-start
2. session-continuity Skill enhances restoration
3. Work with full project memory
4. End: /fb:save-session (if needed)
```

### Pattern 3: Feature Development Workflow
```
1. Plan: /dotai:create-prd-interactive [feature]
2. Tasks: /dotai:parse-prd [feature]
3. Context: pnpm ctx [relevant-preset]
4. Skills: Auto-load for implementation
5. Review: /dotai:pr
```

### Pattern 4: Quality-First Development
```
1. Design with architecture-patterns Skill
2. Implement with TDD using tdd-workflow Skill
3. Review with code-review-checklist Skill
4. Security audit with security-audit Skill
5. Document with appropriate doc Skills
```

---

## Command Quick Reference

| Task | Command | Auto-loaded Skills |
|------|---------|-------------------|
| Restore session | `/fb:session-start` | session-continuity |
| Load UI context | `pnpm ctx ui` | context-optimizer |
| Load backend context | `pnpm ctx backend` | context-optimizer |
| Plan complex feature | `/dotai:create-prd-interactive [name]` | architecture-patterns |
| Plan simple feature | `/dotai:create-prd [name]` | - |
| Generate tasks | `/dotai:parse-prd [name]` | - |
| Update docs | `/dotai:update-app-design` | documentation-excellence |
| Create PR | `/dotai:pr` | code-review-checklist |

---

## Skills Activation Guide

Skills activate automatically based on context:

**When you mention:**
- "authentication", "login", "auth" → `auth-patterns` loads
- "API", "REST", "endpoint" → `rest-design-principles` loads
- "test", "testing", "coverage" → `test-coverage-strategy` loads
- "refactor", "improve code" → `refactoring-strategies` loads
- "security", "vulnerability" → `security-audit` loads
- "context", "load rules" → `context-optimizer` loads

**You don't need to activate Skills manually - they work behind the scenes!**

---

## Key Principles

1. **Commands orchestrate workflows** (dotai proven system)
2. **Skills enhance with knowledge** (auto-loaded patterns)
3. **No duplication** (Skills enhance, don't replace)
4. **Progressive disclosure** (Skills load only what's needed)
5. **Context efficiency** (Smaller = faster, better)

---

## Getting Started

### First Time Setup
1. Navigate to production directory
2. Install dotai: Follow `/dotai:install` instructions
3. Install context system: `/ctx:install`
4. (Optional) Install Flashback: `/fb:install`

### Daily Usage
1. Start session: `/fb:session-start` (if using Flashback)
2. Load context: `pnpm ctx [preset]` for focused work
3. Plan features: `/dotai:how [feature]` or `/dotai:create-prd [feature]`
4. Work with Skills enhancing automatically
5. Create PRs: `/dotai:pr`

---

## Troubleshooting

**Skills not activating?**
- Ensure you're in production/ directory
- Skills activate on keywords (auth, API, test, etc.)
- Check plugin installation in `.claude-plugin/`

**Commands not found?**
- Verify dotai plugin is in `plugins/dotai-enhanced/`
- Check marketplace.json configuration
- Restart Claude Code if needed

**Context feels heavy?**
- Use narrower presets: `pnpm ctx ui` instead of `pnpm ctx app`
- Skills use progressive disclosure (load only when needed)
- Focused context = better quality

---

## Version History

- **v1.0.0** (2025-10-19): Initial production release
  - 7 plugin categories
  - 21 Skills total
  - 15 dotai commands
  - Hybrid orchestration architecture

---

## State of the Art - Competitive Advantage

### What Makes This Revolutionary 🚀

**NO OTHER SYSTEM HAS:**

1. **Dual Control Model**
   - Manual commands (you decide workflows)
   - Automatic Skills (I enhance automatically)
   - Both working together seamlessly

2. **Intelligent Orchestration**
   - THIS FILE is the brain
   - Suggests optimal workflows
   - Prevents conflicts
   - Coordinates both layers

3. **Progressive Intelligence**
   - Start simple (just type commands)
   - Get advanced (Skills enhance automatically)
   - Master patterns (understand orchestration)
   - All without changing behavior!

4. **Safety + Power**
   - You control the workflow (sub-agents)
   - I enhance the quality (Skills)
   - Human approval required (safe)
   - Best practices automatic (powerful)

### Comparison Table

| Feature | Anthropic Skills | dotai Plugins | Our System |
|---------|-----------------|---------------|------------|
| Automatic enhancement | ✅ | ❌ | ✅ |
| Manual workflow control | ❌ | ✅ | ✅ |
| Orchestration intelligence | ❌ | ❌ | ✅ |
| Human in the loop | ❌ | ✅ | ✅ |
| Context awareness | ✅ | ❌ | ✅ |
| Proven workflows | ❌ | ✅ | ✅ |
| **TOTAL** | 2/6 | 3/6 | **6/6** |

**Our system is the ONLY one with all six capabilities!**

---

**This system combines proven dotai orchestration with cutting-edge Skills architecture based on research from 20+ top plugins (18k+ stars), creating a revolutionary hybrid architecture that NO ONE ELSE HAS.**

