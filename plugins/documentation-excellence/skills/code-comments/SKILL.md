---
name: code-comments
description: Code commenting best practices including JSDoc/TSDoc for inline documentation. Use when writing inline documentation or documenting complex code.
---

# Code Comments

Effective inline documentation using JSDoc/TSDoc and commenting best practices.

## When to Use

- Documenting functions/classes
- Explaining complex logic
- API documentation
- Type definitions

## JSDoc/TSDoc Format

```typescript
/**
 * Calculate the total price including tax
 *
 * @param amount - The base amount
 * @param taxRate - Tax rate as decimal (0.1 for 10%)
 * @returns The total amount including tax
 * @throws {ValidationError} If amount is negative
 *
 * @example
 * ```typescript
 * const total = calculateTotal(100, 0.1);
 * // returns 110
 * ```
 */
function calculateTotal(amount: number, taxRate: number): number {
  if (amount < 0) {
    throw new ValidationError('Amount cannot be negative');
  }
  return amount + (amount * taxRate);
}
```

## When to Comment

### ✅ DO Comment
- Complex algorithms
- Non-obvious decisions
- Workarounds for bugs
- Performance optimizations
- Security considerations
- Public APIs

### ❌ DON'T Comment
- Obvious code
- What the code does (should be clear from code)
- Redundant information
- Outdated comments (keep updated or remove)

## Comment Quality

```typescript
// ❌ BAD: Obvious
// Increment counter
counter++;

// ❌ BAD: What, not why
// Loop through users
users.forEach(user => ...);

// ✅ GOOD: Explains why
// Use batch processing to avoid N+1 query problem
const userIds = users.map(u => u.id);
const posts = await Post.findByUserIds(userIds);
```

---

**Auto-loads with inline documentation tasks.**

