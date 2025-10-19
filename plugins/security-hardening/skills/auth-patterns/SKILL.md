---
name: auth-patterns
description: Secure authentication patterns including OAuth2, JWT, session management, and password security. Use when implementing authentication, login systems, or user identity verification.
---

# Auth Patterns

Secure authentication patterns based on industry best practices.

## When to Use

- Implementing authentication
- Designing login systems
- Security reviews
- User identity verification

## Core Patterns

### 1. Password Security
```typescript
// Hash passwords with bcrypt
import bcrypt from 'bcrypt';

const saltRounds = 12;
const hashedPassword = await bcrypt.hash(password, saltRounds);

// Verify
const isValid = await bcrypt.compare(password, hashedPassword);
```

### 2. JWT Tokens
```typescript
// Generate
const token = jwt.sign(
  { userId: user.id, email: user.email },
  process.env.JWT_SECRET,
  { expiresIn: '1h' }
);

// Verify
const decoded = jwt.verify(token, process.env.JWT_SECRET);
```

### 3. Session Management
```typescript
// HTTP-only cookies (secure)
res.cookie('sessionId', session.id, {
  httpOnly: true,
  secure: true, // HTTPS only
  sameSite: 'strict',
  maxAge: 24 * 60 * 60 * 1000 // 24 hours
});
```

### 4. OAuth2 Flow
```
1. Redirect to OAuth provider
2. User authorizes
3. Receive authorization code
4. Exchange for access token
5. Use token for API calls
```

## Security Checklist

- [ ] Passwords hashed (bcrypt/argon2)
- [ ] JWTs have expiration
- [ ] Secrets in environment variables
- [ ] HTTPS enforced
- [ ] Sessions use HTTP-only cookies
- [ ] Rate limiting on login
- [ ] Account lockout after failures
- [ ] Password reset with tokens
- [ ] 2FA for sensitive accounts

---

**Auto-loads with authentication tasks.**

