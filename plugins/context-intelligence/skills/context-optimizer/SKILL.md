---
name: context-optimizer
description: Optimize context loading for maximum token efficiency and relevance. Use when preparing to load project context with pnpm ctx command, switching between project areas, or when context feels bloated.
---

# Context Optimizer

Intelligent context optimization for Claude Code's ctx system, ensuring you load only what's relevant while maintaining maximum quality.

## When to Use This Skill

- Before running `pnpm ctx [preset]`
- When context feels bloated or unfocused
- After adding new documentation or rules
- When switching between project areas (UI → backend)
- When experiencing slow response times
- When Claude provides generic or conflicting advice

## Core Concepts

### 1. The Context Ladder (Best → Worst)

```
Level 1: ULTRA-FOCUSED ⭐⭐⭐⭐⭐
├─ pnpm ctx ui              # Only UI patterns
├─ pnpm ctx backend         # Only backend patterns
└─ Token usage: 3,000-5,000 tokens

Level 2: FEATURE-FOCUSED ⭐⭐⭐⭐
├─ pnpm ctx auth-feature    # Auth-specific
├─ pnpm ctx payments        # Payment-specific
└─ Token usage: 5,000-8,000 tokens

Level 3: LAYER-FOCUSED ⭐⭐⭐
├─ pnpm ctx frontend        # All frontend
├─ pnpm ctx backend         # All backend
└─ Token usage: 8,000-12,000 tokens

Level 4: BROAD ⭐ (AVOID)
└─ pnpm ctx app             # Everything (diluted)
    Token usage: 15,000-25,000 tokens
```

**Rule: Use the narrowest context that serves your current task.**

### 2. Relevance Scoring

Rate each context rule for your current task:

```
Score 5: Critical (will use immediately)
Score 4: Highly relevant (likely to use)
Score 3: Moderately relevant (might use)
Score 2: Tangentially relevant (edge case)
Score 1: Not relevant (different area)
```

**Strategy: Load Score 5 rules, consider Score 4, skip Score 1-3.**

### 3. Token Budgeting

```
Available context window: ~200,000 tokens
Reserve for conversation: ~150,000 tokens
Budget for context: ~50,000 tokens maximum

Ideal distribution:
├─ CLAUDE.md base: 2,000 tokens (always)
├─ Skill metadata: 2,000 tokens (always)
├─ Active Skills: 5,000-10,000 tokens (as needed)
├─ Context rules: 10,000-20,000 tokens (focused)
└─ Working space: 15,000-30,000 tokens (responses)

Total active: 34,000-64,000 tokens
```

**Rule: Never exceed 50k tokens for context alone.**

## Optimization Strategies

### Strategy 1: Task-Driven Loading

**Step 1: Identify your task type**
```
Building UI component → pnpm ctx ui
Building API endpoint → pnpm ctx backend
Writing tests → pnpm ctx testing (if exists)
Documenting → pnpm ctx docs (if exists)
```

**Step 2: Load only that context**
```bash
# Working on payment modal (UI component)
pnpm ctx ui

# NOT: pnpm ctx app (includes irrelevant backend rules)
```

**Step 3: Switch when switching layers**
```bash
# Finished UI, now building API
pnpm ctx backend

# Context refreshes with backend-specific rules
```

### Strategy 2: Incremental Loading

**Start narrow, expand if needed:**

```bash
# Start with narrowest context
pnpm ctx ui

# If you need backend context too
pnpm ctx full-stack  # (if preset exists)

# Or reload manually
# 1. Finish UI work
# 2. pnpm ctx backend
# 3. Start backend work
```

### Strategy 3: Context Rotation

**For long sessions, rotate context:**

```bash
# Morning: UI work
pnpm ctx ui

# Afternoon: API work
pnpm ctx backend

# Evening: Testing
pnpm ctx testing
```

**Benefit: Fresh, focused context every rotation.**

### Strategy 4: Exclusion Lists

**Identify what NOT to load:**

```
Working on UI?
Exclude:
- Backend API patterns
- Database migration rules
- Infrastructure config
- Backend testing patterns

Working on Backend?
Exclude:
- UI component patterns
- CSS/styling rules
- Frontend state management
- UI testing patterns
```

## Common Pitfalls

### Pitfall 1: Always Using 'app' Preset

**Problem:**
```bash
# Every task uses app preset
pnpm ctx app
# → Loads everything (20k+ tokens)
# → Diluted, generic advice
# → Slow responses
```

**Solution:**
```bash
# Use focused presets
pnpm ctx ui       # UI work
pnpm ctx backend  # Backend work
# → Fast, specific advice
```

### Pitfall 2: Never Switching Context

**Problem:**
```bash
# Morning: Load backend context
pnpm ctx backend

# Afternoon: Switch to UI work (but keep backend context)
# → UI advice mixed with backend patterns
# → Confusion
```

**Solution:**
```bash
# Afternoon: Reload for UI
pnpm ctx ui
# → Clean, UI-focused context
```

### Pitfall 3: Loading Before Planning

**Problem:**
```bash
# Load context immediately
pnpm ctx backend

# Then plan (but unsure what you need)
/dotai:how feature-x
```

**Solution:**
```bash
# Plan first
/dotai:how feature-x

# Identify requirements
# → Needs backend + API

# Then load appropriate context
pnpm ctx backend
```

### Pitfall 4: Ignoring Token Bloat

**Problem:**
```bash
# Context feels slow
# Responses take long
# Advice is generic

# But keep using same context
```

**Solution:**
```bash
# Check context size (estimated)
# If > 20k tokens:
#   1. Use narrower preset
#   2. Reload with focus
#   3. Clear and restart
```

## Best Practices Checklist

**Before Loading Context:**
- [ ] Identify current task type (UI/backend/testing/docs)
- [ ] Choose narrowest relevant preset
- [ ] Verify preset exists (`pnpm ctx --help`)

**During Work:**
- [ ] Switch context when switching layers
- [ ] Monitor response quality (specific or generic?)
- [ ] Reload if advice becomes unfocused

**After Major Changes:**
- [ ] Update context rules (`/dotai:update-*`)
- [ ] Regenerate presets (if needed)
- [ ] Test with fresh load

## Integration with Other Skills

**Works With:**
- `semantic-search` - Find relevant rules before loading
- `token-efficiency` - Calculate token budgets
- `session-continuity` - Restore optimal context on session start

**Enhances Commands:**
- `pnpm ctx [preset]` - Primary enhancement target
- `/dotai:how` - Better advice with focused context
- `/fb:session-start` - Restores optimal context state

## Quick Reference

**Context Selection Decision Tree:**
```
What are you building?
├─ UI Component
│  └─ pnpm ctx ui
│
├─ API Endpoint
│  └─ pnpm ctx backend
│
├─ Full-stack Feature
│  ├─ Step 1: pnpm ctx backend (build API)
│  └─ Step 2: pnpm ctx ui (build UI)
│
└─ Documentation
   └─ pnpm ctx docs (if exists) or ui/backend
```

**Token Budget Guide:**
```
Narrow (ui/backend):    3k-8k tokens   ✅ Best
Medium (full-stack):    8k-15k tokens  ⚠️  OK
Broad (app):           15k-25k tokens  ❌ Avoid
```

**When to Reload:**
```
✅ Switching layers (UI → backend)
✅ Starting new feature
✅ After major doc updates
✅ When advice becomes generic

❌ Every few minutes (too frequent)
❌ In middle of implementing (disruptive)
```

---

**This Skill is always active when `pnpm ctx` is used. No manual activation needed.**

