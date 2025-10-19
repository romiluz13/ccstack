---
name: refactoring-strategies
description: Safe refactoring strategies with incremental improvements, test-driven approach, and risk mitigation. Use when improving code quality, eliminating technical debt, or restructuring code.
---

# Refactoring Strategies

Safe, systematic approaches to improving code without changing behavior.

## When to Use

- Code smell detection
- Technical debt reduction
- Performance optimization
- Improving maintainability

## Core Strategies

### 1. Test First
Always have tests before refactoring. No tests = no safety net.

### 2. Small Steps
Make one change at a time. Verify tests pass after each change.

### 3. Common Refactorings

**Extract Method**: Break large functions
```typescript
// Before: 50-line function
// After: 5-line orchestrator + helper functions
```

**Extract Variable**: Clarify complex expressions
```typescript
const isEligible = user.age >= 18 && user.verified && !user.blocked;
```

**Rename**: Improve clarity
```typescript
// calc() → calculateOrderTotal()
```

**Move Method**: Better cohesion
```typescript
// UserValidator.validateOrder() → OrderValidator.validate()
```

## Safety Checklist

- [ ] Tests exist and pass
- [ ] One refactoring at a time
- [ ] Tests still pass after change
- [ ] Commit after each successful refactoring
- [ ] No behavior changes

---

**Auto-loads with refactoring tasks.**

