---
name: knowledge-retention
description: Retain and leverage project knowledge across long-running projects and team collaborations. Use for long-term projects, knowledge transfer, and learning from past implementations.
---

# Knowledge Retention

Strategies for capturing, organizing, and leveraging project knowledge over time.

## When to Use This Skill

- Long-running projects (> 1 month)
- Onboarding to existing projects
- Knowledge transfer between team members
- Learning from past implementations
- Building on previous work
- Avoiding repeated mistakes

## Core Concepts

### 1. Knowledge Categories

```
Architectural Knowledge:
- Design decisions & rationale
- Pattern choices
- Technology selections
- System constraints

Implementation Knowledge:
- Coding patterns discovered
- Gotchas & workarounds
- Performance optimizations
- Testing strategies

Process Knowledge:
- Workflow improvements
- Team conventions
- Review patterns
- Deployment processes
```

### 2. Retention Strategies

**Document Immediately:**
- Don't rely on memory
- Document decisions when made
- Capture rationale, not just result

**Organize by Impact:**
- Critical decisions → Architecture docs
- Patterns → Code conventions
- Processes → Team guidelines

**Review Periodically:**
- Weekly: Recent learnings
- Monthly: Pattern validation
- Quarterly: Knowledge audit

## Best Practices

### Capture Knowledge

```bash
# After architectural decisions
/dotai:update-app-design

# After discovering patterns
/dotai:create-rule [pattern-name]

# After tech changes
/dotai:update-tech-stack
```

### Leverage Knowledge

```bash
# Before starting similar work
# Review past implementations

# Use semantic-search:
"How did we implement authentication?"
"What patterns did we use for API design?"

# Build on learnings, don't repeat research
```

### Share Knowledge

```bash
# Document for team and future self

# In PRs: Link to related past work
# In docs: Reference decision history
# In code: Comment on non-obvious patterns
```

## Quick Reference

**Knowledge Capture:**
- Decisions → /dotai:update-app-design
- Patterns → /dotai:create-rule
- Tech → /dotai:update-tech-stack
- Context → /fb:save-session

**Knowledge Retrieval:**
- Search → semantic-search Skill
- Review → Architecture docs
- Restore → /fb:session-start

---

**This Skill provides knowledge retention strategies for long-term projects.**

