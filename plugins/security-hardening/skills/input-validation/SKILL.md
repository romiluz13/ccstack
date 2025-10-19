---
name: input-validation
description: Input validation and sanitization patterns to prevent SQL injection, XSS, and other injection attacks. Use when handling user input or validating data.
---

# Input Validation

Comprehensive input validation strategies preventing injection attacks.

## When to Use

- Handling user input
- API endpoint implementation
- Form processing
- Data validation

## Core Principles

### 1. Validate Everything
```typescript
// Use validation library (Zod, Joi, etc.)
import { z } from 'zod';

const userSchema = z.object({
  email: z.string().email(),
  age: z.number().min(0).max(120),
  username: z.string().min(3).max(20).regex(/^[a-zA-Z0-9_]+$/)
});

// Validate
const validatedUser = userSchema.parse(input);
```

### 2. Sanitize Output
```typescript
// Prevent XSS
import DOMPurify from 'dompurify';

const clean = DOMPurify.sanitize(userInput);
```

### 3. Parameterized Queries
```typescript
// ✅ GOOD: Parameterized (prevents SQL injection)
const user = await db.query(
  'SELECT * FROM users WHERE email = $1',
  [email]
);

// ❌ BAD: String concatenation (SQL injection risk)
const user = await db.query(
  `SELECT * FROM users WHERE email = '${email}'`
);
```

### 4. Whitelist Approach
```typescript
// Only allow known-good values
const allowedRoles = ['user', 'admin', 'moderator'];

if (!allowedRoles.includes(role)) {
  throw new ValidationError('Invalid role');
}
```

## Validation Checklist

- [ ] Server-side validation (never trust client)
- [ ] Type validation
- [ ] Range/length validation
- [ ] Format validation (email, URL, etc.)
- [ ] Whitelist known-good values
- [ ] Sanitize output
- [ ] Use parameterized queries
- [ ] Escape special characters
- [ ] Reject unexpected fields

---

**Auto-loads with input handling tasks.**

