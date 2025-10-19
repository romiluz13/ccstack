---
name: rest-design-principles
description: REST API design best practices including resource naming, HTTP methods, status codes, and versioning. Use when designing REST APIs with /dotai:how or implementing endpoints.
---

# REST Design Principles

Industry best practices for designing clean, consistent REST APIs.

## When to Use

- Planning API with `/dotai:how`
- Designing endpoints
- API reviews
- Documentation

## Core Principles

### 1. Resource Naming
```
✅ GOOD:
GET    /users           # List users
GET    /users/123       # Get user
POST   /users           # Create user
PUT    /users/123       # Update user
DELETE /users/123       # Delete user

❌ BAD:
GET /getUsers
POST /createUser
GET /user/delete/123
```

### 2. HTTP Methods
- **GET**: Read (safe, idempotent)
- **POST**: Create (not idempotent)
- **PUT**: Update (idempotent)
- **PATCH**: Partial update
- **DELETE**: Remove (idempotent)

### 3. Status Codes
- **200**: Success
- **201**: Created
- **204**: No content (delete success)
- **400**: Bad request (client error)
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not found
- **500**: Server error

### 4. Versioning
```
/v1/users
/v2/users
```

### 5. Pagination
```
GET /users?page=1&limit=20
```

### 6. Filtering
```
GET /users?status=active&role=admin
```

## Quick Checklist

- [ ] Resource names are nouns (not verbs)
- [ ] Plural resource names (/users not /user)
- [ ] Proper HTTP methods
- [ ] Correct status codes
- [ ] Consistent error format
- [ ] Versioned if public API
- [ ] Pagination for lists
- [ ] Documented with examples

---

**Auto-loads with REST API design tasks.**

