---
name: architecture-docs
description: Architecture documentation including system design, ADRs, and diagrams. Use when documenting system architecture or making architectural decisions.
---

# Architecture Documentation

Comprehensive architecture documentation including ADRs and system design.

## When to Use

- Documenting architecture
- Architecture Decision Records (ADRs)
- System design documentation
- Onboarding documentation

## ADR Template

```markdown
# ADR-001: Use PostgreSQL for Database

## Status
Accepted

## Context
Need to choose a database for user data storage. Requirements: ACID, relations, scalability.

## Decision
We will use PostgreSQL as our primary database.

## Consequences
Positive:
- ACID compliance
- Mature ecosystem
- Good performance
- Strong community support

Negative:
- Requires more setup than NoSQL
- Scaling requires partitioning strategy

## Alternatives Considered
- MongoDB: Flexible but no ACID guarantees
- MySQL: Similar but PostgreSQL has better JSON support
```

## Documentation Elements

- System overview diagram
- Component interactions
- Data flow diagrams
- Deployment architecture
- Technology decisions (ADRs)
- Scaling strategy

---

**Auto-loads with architecture documentation tasks.**

