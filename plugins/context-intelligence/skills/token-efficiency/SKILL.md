---
name: token-efficiency
description: Maximize token efficiency through smart compression, summarization, and progressive disclosure. Use when dealing with large contexts, experiencing slow responses, or optimizing for cost.
---

# Token Efficiency

Advanced strategies for minimizing token usage while maintaining context quality and response accuracy.

## When to Use This Skill

- Large context loads (> 20k tokens)
- Slow response times
- Cost optimization goals
- Working with extensive documentation
- Long conversation threads
- Multiple Skills active simultaneously
- Complex multi-file operations

## Core Principles

### 1. Progressive Disclosure

**Load in tiers, not all at once:**

```
Tier 1: Always Loaded (~4k tokens)
├─ CLAUDE.md (system orchestration)
├─ Skill metadata (all 21 Skills)
└─ Essential project context

Tier 2: When Needed (~8k tokens)
├─ Active Skill content
├─ Relevant context preset
└─ Current file context

Tier 3: On Demand (unlimited)
├─ Skill references
├─ Deep documentation
├─ Historical context
└─ External resources
```

**Rule: Don't load Tier 3 unless explicitly needed.**

### 2. Compression Techniques

**Technique 1: Summarization**
```
Full documentation: 5,000 tokens
↓ Summarize key points
Summary: 800 tokens
Efficiency: 84% reduction

Use full docs only when implementing
Use summary for planning/understanding
```

**Technique 2: Reference vs. Inline**
```
❌ BAD: Inline everything
SKILL.md contains:
- All patterns (3,000 tokens)
- All examples (2,000 tokens)
- All edge cases (1,500 tokens)
Total: 6,500 tokens always loaded

✅ GOOD: Reference externally
SKILL.md contains:
- Core concepts (1,500 tokens)
- "See references/ for patterns"
- "See examples/ for code samples"
Total: 1,500 tokens (4,000 saved)
```

**Technique 3: Deduplication**
```
Multiple rules mention "async/await best practices"
↓ Create single source
Create: shared/async-patterns.md
Reference from multiple rules
Savings: 60-80% on duplicated content
```

### 3. Context Window Management

**Monitor usage tiers:**

```
Tier 1: Minimal (< 10k tokens)
├─ Status: Excellent
├─ Response: Fast
└─ Quality: High

Tier 2: Moderate (10k-25k tokens)
├─ Status: Good
├─ Response: Normal
└─ Quality: High

Tier 3: Heavy (25k-50k tokens)
├─ Status: Acceptable
├─ Response: Slower
└─ Quality: Still good

Tier 4: Overloaded (> 50k tokens)
├─ Status: Poor
├─ Response: Very slow
└─ Quality: Degraded
```

**Target: Stay in Tier 1-2.**

## Token Reduction Strategies

### Strategy 1: Smart File Selection

**Problem: Loading entire file for one function**
```bash
# Loading 800-line file for one 20-line function
File: utils/helpers.ts (800 lines = ~12k tokens)
Need: calculateTotal() function (20 lines)
```

**Solution: Targeted reading**
```bash
# Use codebase_search or grep for specific function
# Load only relevant section
# Savings: 11.7k tokens (97% reduction)
```

### Strategy 2: Incremental Context

**Problem: Loading all context upfront**
```bash
# Day 1: Need backend context
pnpm ctx backend + all backend rules
= 15k tokens

# Day 2: Still need backend, but different area
Same 15k tokens loaded, only 3k relevant
```

**Solution: Feature-specific loading**
```bash
# Day 1: Auth work
pnpm ctx backend-auth
= 5k tokens (relevant)

# Day 2: Payment work  
pnpm ctx backend-payments
= 5k tokens (relevant)

Savings: 10k tokens per day
```

### Strategy 3: Conversation Pruning

**Problem: Long conversation history**
```bash
# 20 messages in thread
# Each with full context
# Repetitive information accumulates
```

**Solution: Start fresh conversations**
```bash
# When task changes significantly:
1. Summarize key decisions
2. Start new conversation
3. Reference summary if needed

# Or use /fb:session-start
# Restores only essential context
```

### Strategy 4: Skill Deactivation

**Problem: Multiple Skills loaded unnecessarily**
```bash
# Working on UI, but backend Skills still active
Active Skills:
- context-optimizer (needed)
- architecture-patterns (needed)
- api-security-patterns (NOT needed for UI)
- auth-patterns (NOT needed for UI)

Waste: 6k-8k tokens
```

**Solution: Restart with focused context**
```bash
# Reload for UI-only work
pnpm ctx ui

# Only UI-relevant Skills activate
Active Skills:
- context-optimizer
- architecture-patterns (UI architecture)

Savings: 6k-8k tokens
```

## Token Estimation Guide

**Rough token counts (for planning):**

```
English text: ~0.75 tokens per word
Code: ~1.3 tokens per word
JSON: ~1.2 tokens per character pair
Markdown: ~0.8 tokens per word

Examples:
- 1000 words prose: ~750 tokens
- 1000 words code: ~1,300 tokens
- 100 lines code (avg 50 chars): ~3,000-4,000 tokens
- CLAUDE.md (200 lines): ~2,000 tokens
- Typical SKILL.md (180 lines): ~1,800 tokens
```

**Use for budgeting:**
```bash
# Budget: 10k tokens for context
# CLAUDE.md: 2k tokens
# Active preset: 5k tokens
# Remaining: 3k tokens for Skills

# Can activate 1-2 Skills comfortably
```

## Cost Optimization

**Token costs (approximate, check current pricing):**

```
Input tokens: $3 per 1M tokens
Output tokens: $15 per 1M tokens

Context optimization impact:
- Traditional: 50k tokens per session
- Optimized: 12k tokens per session
- Savings: 76% reduction

For 100 sessions/day:
- Traditional: 5M input tokens = $15/day
- Optimized: 1.2M input tokens = $3.60/day
- Savings: $11.40/day = $342/month
```

## Common Pitfalls

### Pitfall 1: Premature Optimization

**Problem:**
```bash
# Spending hours optimizing 2k tokens
# Time cost > Token cost
```

**Solution:**
```bash
# Optimize when:
- Context > 20k tokens
- Response times slow
- Cost is significant concern

# Don't optimize:
- Context < 10k tokens (already efficient)
- One-time tasks
- Time is more valuable than savings
```

### Pitfall 2: Over-Compression

**Problem:**
```bash
# Compress so much that quality suffers
# Missing critical context
# Requires multiple clarifications
```

**Solution:**
```bash
# Balance compression with quality
# Rule: Never compress critical information
# Better: Load less, but load completely
```

### Pitfall 3: Ignoring Caching

**Problem:**
```bash
# Reloading same context every session
# Not leveraging Claude's caching
```

**Solution:**
```bash
# Use consistent context structure
# Claude caches repeated content
# Benefit: Faster loads, lower costs
```

## Best Practices Checklist

**Before Starting Work:**
- [ ] Estimate token needs for task
- [ ] Load minimal required context
- [ ] Verify no unnecessary Skills active

**During Work:**
- [ ] Monitor context size (if slow, too large)
- [ ] Reload if context drifts (wrong focus)
- [ ] Use targeted file reads

**For Cost Optimization:**
- [ ] Use narrowest context presets
- [ ] Start fresh conversations for new tasks
- [ ] Leverage caching with consistent structure

## Integration with Other Skills

**Works With:**
- `context-optimizer` - Determines what to load
- `semantic-search` - Finds relevant content efficiently
- `session-continuity` - Restores minimal essential context

**Provides To:**
- All Skills - Token budget calculations
- All commands - Context size recommendations

## Measurement & Monitoring

**Signs of good token efficiency:**
- Fast responses (< 3 seconds)
- Specific, focused advice
- Minimal context clarification needed
- Cost within budget

**Signs of poor token efficiency:**
- Slow responses (> 5 seconds)
- Generic or unfocused advice
- Frequent "which file?" questions
- High cost alerts

**Action when inefficient:**
1. Check context size (estimate)
2. Reload with narrower preset
3. Deactivate unnecessary Skills
4. Start fresh conversation if bloated

## Quick Reference

**Token Budget Template:**
```
Base load: ~4k tokens
  ├─ CLAUDE.md: 2k
  └─ Skill metadata: 2k

Active context: ~8k tokens
  ├─ Context preset: 5k
  └─ Active Skills (1-2): 3k

Working space: ~8k tokens
  └─ File context: varies

Total: ~20k tokens (optimal)
Maximum: ~50k tokens (limit)
```

**Optimization Priority:**
```
High Impact:
1. Use narrow presets (ui/backend vs app)
2. Load fewer Skills
3. Start fresh conversations

Medium Impact:
4. Targeted file reads
5. Summarize long docs
6. Prune old messages

Low Impact:
7. Micro-optimizations
8. File renaming for token count
```

**Decision Matrix:**
```
Context > 50k?
└─ Yes → Critical: Reload immediately

Response > 5s?
└─ Yes → High: Investigate context size

Cost > Budget?
└─ Yes → High: Optimize strategy

All good?
└─ Yes → Maintain current approach
```

---

**This Skill provides token efficiency strategies for all contexts. Active when optimizing for performance or cost.**

