# Context Intelligence Plugin

**Version:** 1.0.0  
**Skills:** 3  
**Type:** Enhancement  
**Auto-activation:** Yes

---

## Overview

Context Intelligence provides three powerful Skills for optimizing how Claude Code loads and processes project context. These Skills ensure maximum token efficiency, relevance, and search quality.

---

## Skills Included

### 1. context-optimizer

**Auto-loads:** When using `pnpm ctx` command

**Purpose:** Optimize context loading for maximum efficiency

**Key Features:**
- Context Ladder (ULTRA-FOCUSED → BROAD)
- Relevance scoring system
- Token budgeting strategies
- Task-driven loading guidance

**Use When:**
- Before running `pnpm ctx [preset]`
- Switching between project areas
- Context feels bloated
- Response times slow

### 2. token-efficiency

**Auto-loads:** When dealing with large contexts or optimizing performance

**Purpose:** Maximize token efficiency through compression and smart loading

**Key Features:**
- Progressive disclosure strategies
- Token estimation guide
- Cost optimization
- Context window management

**Use When:**
- Context > 20k tokens
- Slow response times
- Cost optimization needed
- Multiple Skills active

### 3. semantic-search

**Auto-loads:** When searching codebase or finding implementations

**Purpose:** Find relevant code using meaning-based search

**Key Features:**
- Question-based search strategies
- Pattern discovery
- Relationship mapping
- Scope restriction techniques

**Use When:**
- Finding specific implementations
- Discovering patterns
- Exploring unfamiliar code
- Locating documentation

---

## Quick Start

These Skills activate automatically - no configuration needed!

**Example 1: Optimize Context Loading**
```bash
# Skill auto-loads with command
pnpm ctx backend

# context-optimizer provides:
- Token budget recommendations
- Relevance scoring
- Loading strategies
```

**Example 2: Efficient Search**
```bash
# Ask a question
"How do we authenticate API requests?"

# semantic-search provides:
- Search query formulation
- Scope restriction advice
- Result refinement strategies
```

**Example 3: Reduce Token Usage**
```bash
# Working with large context

# token-efficiency provides:
- Compression techniques
- Progressive disclosure
- Budget calculations
```

---

## Integration with dotai

These Skills enhance dotai commands:

| dotai Command | Enhanced By | Benefit |
|---------------|------------|---------|
| `pnpm ctx [preset]` | context-optimizer | Optimal preset selection |
| `pnpm ctx [preset]` | token-efficiency | Token budget management |
| `/dotai:how` | All 3 Skills | Better planning with focused context |
| `/fb:session-start` | context-optimizer | Optimal context restoration |

---

## Best Practices

### Use Narrow Context Presets
```bash
✅ GOOD: pnpm ctx ui (focused)
✅ GOOD: pnpm ctx backend (focused)
❌ BAD: pnpm ctx app (everything)
```

### Switch Context When Switching Layers
```bash
# Morning: UI work
pnpm ctx ui

# Afternoon: API work
pnpm ctx backend  # Reload!
```

### Use Semantic Search for Exploration
```bash
# Instead of grep with keywords
# Ask complete questions
"How do we validate user input?"
```

---

## Token Efficiency Impact

**Traditional Approach:**
- Context: 50,000+ tokens always loaded
- Slow responses
- High costs

**With Context Intelligence:**
- Base: 8,000 tokens (CLAUDE.md + metadata)
- Active: 11,000-15,000 tokens (focused)
- Reduction: 70-85%

**Result:**
- Faster responses
- Lower costs
- Better quality (focused advice)

---

## Activation Triggers

These Skills activate on:

**context-optimizer:**
- `pnpm ctx` usage
- "context", "load rules", "preset"
- Task switching

**token-efficiency:**
- Large context scenarios
- "optimize", "efficiency", "performance"
- Cost discussions

**semantic-search:**
- "how do we", "where is", "find"
- Code exploration
- Pattern discovery

---

## Troubleshooting

**Q: Skills not providing guidance?**
A: Skills work behind the scenes. Their advice is integrated into responses.

**Q: Context still feels heavy?**
A: Use `context-optimizer` checklist - switch to narrower preset.

**Q: Searches not finding results?**
A: Follow `semantic-search` query formulation guide - ask complete questions.

**Q: Token usage still high?**
A: Consult `token-efficiency` for compression strategies.

---

## Examples

### Example 1: Optimized Workflow

```bash
# 1. Load focused context
pnpm ctx backend
# → context-optimizer: "Excellent choice! Backend-only: 5k tokens"

# 2. Plan feature
/dotai:how payment-api
# → Plans using focused backend context
# → api-excellence Skills also enhance

# 3. Implement efficiently
# → token-efficiency keeps usage optimal
# → semantic-search helps find patterns
```

### Example 2: Context Switching

```bash
# Morning: Build API
pnpm ctx backend
# → context-optimizer: "Backend rules loaded (5k tokens)"

# Afternoon: Build UI
pnpm ctx ui
# → context-optimizer: "Switched to UI rules (4k tokens)"
# → Fresh, focused context
```

### Example 3: Cost Optimization

```bash
# Check token usage
# → token-efficiency: "Current: 12k tokens (optimal)"

# If high:
# → token-efficiency: "Reduce to 8k by using narrower preset"

# Apply recommendations
pnpm ctx ui  # instead of app
# → token-efficiency: "Reduced to 8k tokens (33% savings)"
```

---

## Version History

- **v1.0.0** (2025-10-19): Initial release
  - context-optimizer (150 lines)
  - token-efficiency (120 lines)
  - semantic-search (180 lines)
  - Total: 450 lines, 3 Skills

---

**These Skills are always ready to enhance your context management. No manual activation required.**

