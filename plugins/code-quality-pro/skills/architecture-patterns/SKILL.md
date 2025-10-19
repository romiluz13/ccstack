---
name: architecture-patterns
description: Apply proven architecture patterns including SOLID principles, DDD, microservices, and system design. Use when designing systems, reviewing architecture, or making structural decisions.
---

# Architecture Patterns

Proven patterns for building maintainable, scalable systems based on industry best practices.

## When to Use

- System design with `/dotai:create-prd-interactive`
- Architecture reviews
- Refactoring decisions
- Technology selection
- Scalability planning

## Core Patterns

### SOLID Principles
- Single Responsibility: One class, one reason to change
- Open/Closed: Open for extension, closed for modification  
- Liskov Substitution: Subtypes must be substitutable
- Interface Segregation: Many specific interfaces > one general
- Dependency Inversion: Depend on abstractions, not concretions

### Layered Architecture
```
Presentation Layer → Business Logic → Data Access → Database
```
**Use when**: Clear separation of concerns needed

### Microservices
- Independent services
- Domain-driven boundaries
- API-first communication

**Use when**: Scale, team autonomy needed

### Monolith First
- Start simple
- Split when needed

**Use when**: Early stage, unclear boundaries

## Quick Reference

**Choosing Pattern:**
- Small app → Layered monolith
- Clear domains → DDD + microservices
- Rapid iteration → Monolith first
- High scale → Event-driven + microservices

---

**Auto-loads with system design tasks.**

