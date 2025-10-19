---
name: api-documentation
description: API documentation best practices including OpenAPI/Swagger, endpoint documentation, and examples. Use when documenting APIs or creating API specifications.
---

# API Documentation

Comprehensive API documentation using OpenAPI/Swagger and best practices.

## When to Use

- Documenting APIs
- Creating API specifications
- Generating API docs
- API onboarding

## OpenAPI/Swagger Structure

```yaml
openapi: 3.0.0
info:
  title: User API
  version: 1.0.0

paths:
  /users:
    get:
      summary: List all users
      parameters:
        - name: limit
          in: query
          schema:
            type: integer
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/User'

components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: string
        email:
          type: string
        name:
          type: string
```

## Documentation Checklist

- [ ] All endpoints documented
- [ ] Request/response examples
- [ ] Error responses documented
- [ ] Authentication explained
- [ ] Rate limits specified
- [ ] Versioning strategy clear
- [ ] Status codes documented

---

**Auto-loads with API documentation tasks.**

