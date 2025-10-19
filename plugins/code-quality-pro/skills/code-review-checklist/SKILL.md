---
name: code-review-checklist
description: Systematic code review checklist covering functionality, design, testing, naming, and security. Use when reviewing code, creating PRs, or self-reviewing before commit.
---

# Code Review Checklist

Systematic review process ensuring quality, security, and maintainability.

## When to Use

- Before creating PR (`/dotai:pr`)
- Reviewing teammate's code
- Self-review before commit
- Quality audits

## Review Checklist

### Functionality
- [ ] Code does what it's supposed to
- [ ] Edge cases handled
- [ ] Error cases handled
- [ ] No obvious bugs

### Design
- [ ] Follows project patterns
- [ ] DRY (no duplication)
- [ ] Single Responsibility
- [ ] Appropriate abstraction level

### Testing
- [ ] Tests exist
- [ ] Tests cover happy path
- [ ] Tests cover error cases
- [ ] Tests are readable

### Naming
- [ ] Variables have clear names
- [ ] Functions reveal intent
- [ ] No abbreviations (except common)
- [ ] Consistent with codebase

### Security
- [ ] Input validation
- [ ] No SQL injection risk
- [ ] No XSS vulnerabilities
- [ ] Secrets not hardcoded
- [ ] Auth/authz checks present

### Performance
- [ ] No obvious performance issues
- [ ] Appropriate data structures
- [ ] No N+1 queries
- [ ] Caching where appropriate

### Documentation
- [ ] Complex logic commented
- [ ] API changes documented
- [ ] README updated if needed

---

**Auto-loads with PR creation and code reviews.**

