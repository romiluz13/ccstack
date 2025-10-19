---
name: security-audit
description: Security audit checklist based on OWASP guidelines covering common vulnerabilities and security best practices. Use when conducting security reviews or hardening applications.
---

# Security Audit

Comprehensive security audit based on OWASP Top 10 and industry standards.

## When to Use

- Security reviews
- Pre-deployment audits
- Compliance checks
- Vulnerability assessment

## OWASP Top 10 Checklist

### 1. Injection
- [ ] Parameterized queries used
- [ ] Input validation in place
- [ ] No eval() or exec() with user input
- [ ] ORM/query builder used correctly

### 2. Broken Authentication
- [ ] Strong password requirements
- [ ] Account lockout after failures
- [ ] Session timeout configured
- [ ] Secure password storage (bcrypt)

### 3. Sensitive Data Exposure
- [ ] HTTPS enforced
- [ ] Sensitive data encrypted at rest
- [ ] No secrets in code/logs
- [ ] PII properly handled

### 4. XML External Entities (XXE)
- [ ] XML parser configured securely
- [ ] External entity processing disabled

### 5. Broken Access Control
- [ ] Authorization checks on all endpoints
- [ ] User can only access own data
- [ ] Admin functions protected

### 6. Security Misconfiguration
- [ ] Default passwords changed
- [ ] Unnecessary features disabled
- [ ] Error messages don't leak info
- [ ] Security headers configured

### 7. Cross-Site Scripting (XSS)
- [ ] Output escaped/sanitized
- [ ] Content-Security-Policy header
- [ ] No innerHTML with user input

### 8. Insecure Deserialization
- [ ] Deserialization from trusted sources only
- [ ] Input validation before deserialization

### 9. Using Components with Known Vulnerabilities
- [ ] Dependencies up to date
- [ ] npm audit/similar run regularly
- [ ] Security patches applied

### 10. Insufficient Logging & Monitoring
- [ ] Security events logged
- [ ] Failed login attempts tracked
- [ ] Anomalies monitored
- [ ] Logs protected from tampering

## Quick Audit

- [ ] Authentication secure
- [ ] Authorization enforced
- [ ] Input validated
- [ ] Output sanitized
- [ ] HTTPS enforced
- [ ] Secrets managed properly
- [ ] Dependencies updated
- [ ] Security headers set
- [ ] Rate limiting enabled
- [ ] Logging configured

---

**Auto-loads with security review tasks.**

