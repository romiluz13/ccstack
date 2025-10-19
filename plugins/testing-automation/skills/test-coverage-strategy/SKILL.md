---
name: test-coverage-strategy
description: Strategic test coverage planning including what to test, coverage goals, and testing priorities. Use when planning tests, generating test suites, or evaluating coverage.
---

# Test Coverage Strategy

Strategic approach to test coverage ensuring quality without over-testing.

## When to Use

- Planning tests with `/dotai:parse-prd`
- Test generation
- Coverage evaluation
- Quality audits

## Coverage Goals by Area

### Critical (90-100% coverage)
- Authentication & authorization
- Payment processing
- Data mutations
- Security-sensitive code
- Business logic calculations

### Important (80-90% coverage)
- API endpoints
- Database operations
- User workflows
- Error handling

### Standard (70-80% coverage)
- Utility functions
- Helpers
- Formatters

### Optional (< 70% coverage)
- UI components (focus on logic)
- Configuration
- Constants
- Types/interfaces

## What to Test

### ✅ ALWAYS Test
- Business logic
- Data transformations
- Edge cases
- Error scenarios
- Security checks
- API contracts

### ❌ DON'T Test
- Third-party libraries
- Framework internals
- Trivial getters/setters
- UI styling (unless critical)
- Configuration constants

## Test Pyramid

```
      E2E Tests (10%)
    ──────────────
   Integration Tests (30%)
  ────────────────────────
 Unit Tests (60%)
──────────────────────────
```

---

**Auto-loads with testing planning tasks.**

