# dotai + Skills Integration

Complete guide to how dotai commands integrate with Skills for maximum effectiveness.

## Integration Matrix

| dotai Command | Enhanced By | Benefit |
|---------------|------------|---------|
| `/fb:session-start` | session-continuity, knowledge-retention | Smart memory restoration |
| `pnpm ctx [preset]` | context-optimizer, token-efficiency | Optimized context loading |
| `/dotai:how [feature]` | All domain Skills | Enhanced planning with patterns |
| `/dotai:create-prd` | architecture-patterns, domain Skills | Strategic PRD with best practices |
| `/dotai:parse-prd` | test-coverage-strategy | Tasks include comprehensive tests |
| `/dotai:update-*` | documentation-excellence | High-quality documentation |
| `/dotai:pr` | code-review-checklist | Systematic quality review |

---

## Command-by-Command Integration

### 1. Session Management

**Command:** `/fb:session-start`

**Skills Enhancement:**
```
session-continuity AUTO-LOADS
├─ Filters outdated context
├─ Prioritizes critical info
├─ Focuses on actionable items
└─ Result: Fast, relevant restoration

knowledge-retention PROVIDES
├─ Historical patterns
├─ Past decisions
└─ Lessons learned
```

**Example:**
```bash
/fb:session-start

# Skills enhance by:
# 1. Skipping old context (> 1 week)
# 2. Highlighting blockers
# 3. Surfacing key decisions
# 4. Loading last working plan
```

---

### 2. Context Management

**Command:** `pnpm ctx backend`

**Skills Enhancement:**
```
context-optimizer AUTO-LOADS
├─ Recommends narrow preset (backend vs app)
├─ Scores rule relevance
├─ Manages token budget
└─ Result: 5k tokens vs 20k tokens

token-efficiency MONITORS
├─ Current token usage
├─ Compression opportunities
└─ Performance impact
```

**Example:**
```bash
pnpm ctx backend

# Skills enhance by:
# 1. Loading only backend rules (not UI)
# 2. Optimizing for 5k tokens
# 3. Ensuring fast responses
# 4. Maintaining quality
```

---

### 3. Feature Planning

**Command:** `/dotai:how user-authentication`

**Skills Enhancement:**
```
auth-patterns AUTO-LOADS
├─ OAuth2 vs JWT guidance
├─ Session management patterns
├─ Security best practices
└─ Common pitfalls

api-security-patterns AUTO-LOADS
├─ OWASP checklist
├─ Input validation requirements
└─ Rate limiting strategies

test-coverage-strategy AUTO-LOADS
├─ Critical path testing (90%+)
└─ Security test requirements
```

**Example:**
```bash
/dotai:how user-authentication

# Plan enhanced with:
# 1. JWT implementation pattern
# 2. Security checklist (OWASP)
# 3. Test coverage strategy
# 4. Common auth pitfalls to avoid
```

---

### 4. PRD Creation

**Command:** `/dotai:create-prd-interactive payment-api`

**Skills Enhancement:**
```
rest-design-principles AUTO-LOADS
├─ Resource naming conventions
├─ HTTP method selection
├─ Status code guidance
└─ Versioning strategy

api-security-patterns AUTO-LOADS
├─ Payment security (PCI)
├─ Authentication requirements
└─ Validation strategies

test-coverage-strategy AUTO-LOADS
└─ Payment flow testing requirements
```

**Example:**
```bash
/dotai:create-prd-interactive payment-api

# PRD enhanced with:
# 1. REST endpoint design (/payments, POST)
# 2. PCI compliance requirements
# 3. Security validation checklist
# 4. Test strategy for critical paths
```

---

### 5. Task Generation

**Command:** `/dotai:parse-prd payment-api`

**Skills Enhancement:**
```
test-coverage-strategy AUTO-LOADS
├─ Ensures test tasks included
├─ Sets coverage goals (90% for payments)
├─ Defines test types (unit, integration, E2E)
└─ Result: Complete test coverage

architecture-patterns PROVIDES
└─ Structural organization guidance
```

**Example:**
```bash
/dotai:parse-prd payment-api

# Tasks enhanced with:
# Phase 1: Backend
#   ├─ Stripe integration
#   ├─ Payment model
#   └─ Unit tests (90% coverage) ← Skill added
# Phase 2: API
#   ├─ POST /payments endpoint
#   ├─ Input validation
#   └─ Integration tests ← Skill added
# Phase 3: E2E
#   └─ Payment flow E2E test ← Skill added
```

---

### 6. Documentation Updates

**Command:** `/dotai:update-app-design`

**Skills Enhancement:**
```
architecture-docs AUTO-LOADS
├─ ADR format guidance
├─ System diagram recommendations
└─ Documentation structure

api-documentation AUTO-LOADS (if API feature)
└─ OpenAPI/Swagger format
```

**Example:**
```bash
/dotai:update-app-design

# Documentation enhanced with:
# 1. ADR for major decisions
# 2. Architecture diagrams
# 3. Component relationships
# 4. API specifications (if applicable)
```

---

### 7. Pull Request Creation

**Command:** `/dotai:pr`

**Skills Enhancement:**
```
code-review-checklist AUTO-LOADS
├─ Functionality verification
├─ Design quality checks
├─ Testing verification
├─ Security audit
├─ Performance review
└─ Documentation completeness

security-audit PROVIDES (if security-sensitive)
└─ OWASP Top 10 verification
```

**Example:**
```bash
/dotai:pr

# PR enhanced with:
# Description: Feature summary
# Checklist: ← Skill provides
#   - [ ] Tests pass (100%)
#   - [ ] Security audit (OWASP)
#   - [ ] Input validation verified
#   - [ ] API documented
#   - [ ] Performance acceptable
#   - [ ] No lint errors
```

---

## Workflow Patterns

### Pattern 1: Full-Stack Feature

```bash
# 1. Start session
/fb:session-start
# → session-continuity enhances

# 2. Plan feature
/dotai:create-prd-interactive user-profile-api

# → Multiple Skills activate:
#    - architecture-patterns (system design)
#    - rest-design-principles (API design)
#    - api-security-patterns (security)

# 3. Generate tasks
/dotai:parse-prd user-profile-api
# → test-coverage-strategy ensures tests

# 4. Build backend
pnpm ctx backend
# → context-optimizer focuses context

# Implementation with Skills guiding

# 5. Build frontend
pnpm ctx ui
# → context-optimizer switches context

# Implementation with UI Skills

# 6. Create PR
/dotai:pr
# → code-review-checklist verifies quality
```

---

### Pattern 2: Security-First Feature

```bash
# 1. Plan with security focus
/dotai:create-prd-interactive secure-payment-processing

# → Security Skills dominate:
#    - auth-patterns (authentication)
#    - api-security-patterns (API security)
#    - input-validation (data validation)
#    - security-audit (OWASP)

# 2. Implementation guided by security Skills
# All code follows security best practices

# 3. Security audit built into PR
/dotai:pr
# → security-audit checklist verified
```

---

### Pattern 3: Test-Driven Feature

```bash
# 1. Plan with testing emphasis
/dotai:create-prd-interactive payment-processing

# → test-coverage-strategy active
#    Sets 90%+ coverage for critical paths

# 2. Tasks include comprehensive tests
/dotai:parse-prd payment-processing
# → Unit, integration, E2E tests all included

# 3. TDD workflow
# → tdd-workflow Skill guides Red-Green-Refactor

# 4. Verify coverage in PR
/dotai:pr
# → Checklist includes test verification
```

---

## Success Metrics

**How to know integration is working:**

1. **Plans are comprehensive** - Include security, tests, documentation
2. **Tasks are complete** - Test tasks automatically included
3. **Code is secure** - Security patterns followed automatically
4. **Documentation is high-quality** - ADRs, OpenAPI, JSDoc all present
5. **PRs are thorough** - Checklists cover all quality aspects

**If missing any of above → Check Skills activation**

---

## Troubleshooting Integration

**Problem:** Plans lack security guidance
**Solution:** Mention "secure" or "authentication" in feature name

**Problem:** Tasks don't include tests
**Solution:** Run `/dotai:parse-prd` (test-coverage-strategy should activate)

**Problem:** Context feels heavy
**Solution:** Use `context-optimizer` recommendations (narrow presets)

**Problem:** Generic advice
**Solution:** Use more specific keywords to trigger relevant Skills

---

**The integration is designed to be invisible. Commands orchestrate, Skills enhance, you stay productive.**

