---
name: context-history
description: Track and review decision history, understand past context, and maintain decision rationale. Use when reviewing past decisions, understanding why code exists, or auditing architectural choices.
---

# Context History

Maintain clear decision history and context for understanding past choices and their rationale.

## When to Use This Skill

- Reviewing past decisions
- Understanding "why" behind code
- Auditing architectural choices
- Onboarding to legacy code
- Refactoring with context
- Avoiding repeating past mistakes

## Core Concepts

### 1. Decision Documentation

**What to document:**
- Decision made
- Options considered
- Rationale for choice
- Trade-offs accepted
- Expected outcomes

**Why document:**
- Future you won't remember
- Team needs context
- Refactoring needs rationale
- Mistakes can be learned from

### 2. Context Preservation

```
ADR (Architecture Decision Record):
- Problem statement
- Context & constraints
- Options evaluated
- Decision made
- Consequences & trade-offs

Store in:
- docs/adr/ directory
- Or in-line code comments
- Or architecture documentation
```

## Best Practices

### Document Decisions

```bash
# Major architectural decisions
/dotai:update-app-design
# → Documents in architecture docs

# Add ADR for significant choices
# Create docs/adr/001-choice-name.md
```

### Review History

```bash
# Before refactoring
"Why was this implemented this way?"

# Use semantic-search:
"What was the decision history for authentication?"
"Why did we choose PostgreSQL?"
```

### Learn from History

```bash
# Periodic reviews
# What worked? What didn't?
# Update patterns and conventions
# Avoid repeating mistakes
```

## Quick Reference

**When to Document:**
- [ ] Architectural decisions
- [ ] Non-obvious implementations
- [ ] Trade-off choices
- [ ] Pattern selections
- [ ] Technology choices

**Where to Document:**
- Architecture docs (/dotai:update-app-design)
- ADR files (docs/adr/)
- Code comments (complex logic)
- PRs (change rationale)

---

**This Skill provides decision history tracking for maintaining context over time.**

