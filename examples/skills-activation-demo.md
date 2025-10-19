# Skills Activation Demo

This document demonstrates how Skills activate automatically based on your work context.

## How Skills Activate

Skills use keywords and context to determine when they're relevant. You don't need to manually activate them - they work behind the scenes.

---

## Activation Examples

### Example 1: Context Intelligence Skills

**Trigger:** Using `pnpm ctx` command

```bash
pnpm ctx backend
```

**Auto-activated Skills:**
- ✅ `context-optimizer` - Optimizes what rules to load
- ✅ `token-efficiency` - Manages token budget

**How you know it's working:**
- Context loads faster
- Only relevant rules included
- Advice is backend-specific (not generic)

---

### Example 2: API Development Skills

**Trigger:** Mentioning "API", "endpoint", "REST" in task

```bash
/dotai:how payment-api-endpoint
```

**Auto-activated Skills:**
- ✅ `rest-design-principles` - REST best practices
- ✅ `api-security-patterns` - Security guidance
- ✅ `api-documentation` - Documentation standards

**How you know it's working:**
- Plan includes REST conventions (GET, POST, proper status codes)
- Security checklist included (auth, validation)
- Documentation steps present

---

### Example 3: Authentication Skills

**Trigger:** Keywords "auth", "login", "authentication"

```bash
/dotai:create-prd-interactive user-authentication
```

**Auto-activated Skills:**
- ✅ `auth-patterns` - OAuth2, JWT, session management
- ✅ `security-audit` - OWASP checklist
- ✅ `input-validation` - Secure input handling

**How you know it's working:**
- PRD includes OAuth2 vs JWT decision
- Security requirements prominent
- Input validation strategy included

---

### Example 4: Testing Skills

**Trigger:** Keywords "test", "testing", "coverage"

```bash
/dotai:parse-prd payment-integration
```

**Auto-activated Skills:**
- ✅ `test-coverage-strategy` - Coverage goals
- ✅ `tdd-workflow` - TDD approach
- ✅ `e2e-testing-patterns` - E2E test strategies

**How you know it's working:**
- Generated tasks include test tasks
- Critical paths have 90%+ coverage goals
- E2E tests for user flows included

---

### Example 5: Code Quality Skills

**Trigger:** Keywords "refactor", "improve", "architecture"

```bash
"I need to refactor the user service"
```

**Auto-activated Skills:**
- ✅ `refactoring-strategies` - Safe refactoring
- ✅ `architecture-patterns` - Design patterns
- ✅ `code-review-checklist` - Quality verification

**How you know it's working:**
- Suggests test-first approach
- Recommends small, incremental changes
- Provides architectural guidance

---

### Example 6: Memory Skills

**Trigger:** Using Flashback commands

```bash
/fb:session-start
```

**Auto-activated Skills:**
- ✅ `session-continuity` - Smart restoration
- ✅ `knowledge-retention` - Long-term learning
- ✅ `context-history` - Decision tracking

**How you know it's working:**
- Restoration prioritizes critical context
- Outdated info filtered
- Key decisions highlighted

---

### Example 7: Documentation Skills

**Trigger:** Keywords "document", "docs", "documentation"

```bash
/dotai:update-app-design
```

**Auto-activated Skills:**
- ✅ `api-documentation` - API docs standards
- ✅ `architecture-docs` - ADR format
- ✅ `code-comments` - JSDoc best practices

**How you know it's working:**
- Documentation follows standard format
- ADRs include rationale
- Code comments explain why, not what

---

## Multiple Skills Active

**Scenario:** Complex feature with multiple concerns

```bash
/dotai:create-prd-interactive secure-payment-api
```

**Triggers multiple keywords:** "secure", "payment", "API"

**Auto-activated Skills (7+ Skills):**
- `api-excellence` (all 3 Skills)
- `security-hardening` (all 3 Skills)
- `testing-automation` (test-coverage-strategy)
- `code-quality-pro` (architecture-patterns)

**Result:**
- Comprehensive guidance
- No conflicts (Skills designed to compose)
- Holistic quality approach

---

## Verification

### How to verify Skills are working:

**1. Check advice specificity:**
- Generic advice = Skills not active
- Specific patterns/examples = Skills active

**2. Check completeness:**
- Missing security = security Skills not active
- Missing tests = testing Skills not active
- Incomplete = relevant Skills didn't activate

**3. Check keyword triggers:**
- If you mention "auth" but get no auth guidance → Issue
- If you mention "API" but get no REST patterns → Issue

**4. Check orchestration file:**
- Review `production/CLAUDE.md` for activation triggers
- Ensure your keywords match documented triggers

---

## Troubleshooting

**Skills not activating?**

1. **Check keywords:** Use activation keywords explicitly
   - "authentication" not just "login"
   - "API endpoint" not just "function"

2. **Check context:** Load appropriate context preset
   - `pnpm ctx backend` for backend work
   - `pnpm ctx ui` for UI work

3. **Check orchestrator:** Verify `CLAUDE.md` is in production/

4. **Check marketplace:** Verify plugins enabled in `marketplace.json`

---

## Best Practices

**1. Use descriptive feature names:**
```bash
✅ GOOD: /dotai:how user-authentication-jwt
❌ BAD: /dotai:how feature-x
```

**2. Mention key technologies:**
```bash
✅ GOOD: /dotai:create-prd rest-api-payments
❌ BAD: /dotai:create-prd backend-thing
```

**3. Load appropriate context:**
```bash
✅ GOOD: pnpm ctx backend (before API work)
❌ BAD: pnpm ctx app (loads everything)
```

**4. Trust the system:**
- Skills work behind the scenes
- No manual activation needed
- Just use natural language with keywords

---

**Skills are always ready. Just describe your work naturally, and they'll enhance it automatically.**

