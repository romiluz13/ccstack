---
name: api-security-patterns
description: API security best practices including authentication, authorization, rate limiting, and OWASP guidelines. Use when building secure APIs or conducting security reviews.
---

# API Security Patterns

Essential security patterns for protecting APIs from common threats.

## When to Use

- API security design
- Security reviews
- Implementing auth
- Threat mitigation

## Core Security Patterns

### 1. Authentication
```typescript
// JWT tokens
Authorization: Bearer <token>

// API keys
X-API-Key: <key>

// OAuth2
Authorization: Bearer <access_token>
```

### 2. Authorization
```typescript
// Role-based (RBAC)
if (!user.roles.includes('admin')) {
  throw new ForbiddenError();
}

// Resource-based
if (post.authorId !== user.id) {
  throw new ForbiddenError();
}
```

### 3. Input Validation
```typescript
// Always validate & sanitize
const schema = z.object({
  email: z.string().email(),
  age: z.number().min(0).max(120)
});

const validated = schema.parse(input);
```

### 4. Rate Limiting
```typescript
// Prevent abuse
// 100 requests per 15 minutes per IP
app.use(rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 100
}));
```

### 5. CORS
```typescript
// Whitelist origins
app.use(cors({
  origin: ['https://trusted-domain.com']
}));
```

## OWASP Top 10 for APIs

1. Broken Object Level Authorization
2. Broken Authentication
3. Excessive Data Exposure
4. Lack of Resources & Rate Limiting
5. Broken Function Level Authorization
6. Mass Assignment
7. Security Misconfiguration
8. Injection
9. Improper Assets Management
10. Insufficient Logging & Monitoring

## Security Checklist

- [ ] Authentication required
- [ ] Authorization checked
- [ ] Input validated
- [ ] SQL injection prevented (parameterized queries)
- [ ] XSS prevented (sanitized output)
- [ ] CSRF protection (tokens)
- [ ] Rate limiting enabled
- [ ] HTTPS enforced
- [ ] Secrets in env vars
- [ ] Error messages don't leak info

---

**Auto-loads with API security tasks.**

