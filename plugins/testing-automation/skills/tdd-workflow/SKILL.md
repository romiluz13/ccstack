---
name: tdd-workflow
description: Test-Driven Development workflow with Red-Green-Refactor cycle and best practices. Use when following TDD approach or implementing test-first development.
---

# TDD Workflow

Test-Driven Development (TDD) Red-Green-Refactor cycle for quality code.

## When to Use

- TDD development approach
- Critical feature implementation
- Bug fixing with tests
- Refactoring with safety

## Red-Green-Refactor Cycle

### 1. RED: Write Failing Test
```typescript
describe('calculateTotal', () => {
  it('should calculate order total with tax', () => {
    const result = calculateTotal(100, 0.1);
    expect(result).toBe(110);
  });
});

// Run test → FAILS (function doesn't exist)
```

### 2. GREEN: Make It Pass
```typescript
function calculateTotal(amount: number, taxRate: number): number {
  return amount + (amount * taxRate);
}

// Run test → PASSES
```

### 3. REFACTOR: Improve Code
```typescript
function calculateTotal(amount: number, taxRate: number): number {
  const tax = amount * taxRate;
  return amount + tax;
}

// Run test → Still PASSES
```

## TDD Best Practices

- Write smallest test possible
- One test at a time
- Make test pass quickly
- Refactor only when green
- Commit after each cycle

---

**Auto-loads with TDD tasks.**

