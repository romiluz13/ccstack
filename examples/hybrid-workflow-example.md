# Hybrid Workflow Example

This example demonstrates how commands and Skills work together in a complete feature development workflow.

## Scenario: Building Payment Integration

### Step 1: Start Session

```bash
/fb:session-start
```

**What happens:**
- Flashback restores previous session state
- `session-continuity` Skill AUTO-LOADS
- Enhances memory restoration with smart filtering
- Focuses on actionable context

**Result:** You're immediately oriented with last session's context.

---

### Step 2: Load Context

```bash
pnpm ctx backend
```

**What happens:**
- dotai loads backend context rules
- `context-optimizer` Skill AUTO-LOADS
- Ensures only relevant backend rules loaded (5k tokens, not 20k)
- Scores relevance for current task

**Result:** Fast, focused context for backend work.

---

### Step 3: Plan Feature

```bash
/dotai:create-prd-interactive payment-integration
```

**What happens:**
- dotai starts PRD creation with Q&A
- `api-excellence` Skills AUTO-LOAD (rest-design-principles, api-security-patterns)
- Guides API design with best practices
- Security patterns inform payment handling

**Questions asked:**
1. What payment providers? (Stripe, PayPal)
2. What payment methods? (Credit card, ACH)
3. Subscription or one-time? (Both)
4. Security requirements? (PCI compliance)
5. Webhook handling? (Yes)

**Result:** Comprehensive PRD with security best practices built in.

---

### Step 4: Generate Tasks

```bash
/dotai:parse-prd payment-integration
```

**What happens:**
- dotai converts PRD to atomic tasks
- `test-coverage-strategy` Skill AUTO-LOADS
- Ensures test tasks included for critical payment logic

**Generated tasks include:**
- Backend: Stripe integration, webhook handler, payment model
- Security: Input validation, PCI compliance audit
- Testing: Payment flow tests, webhook tests
- Documentation: API endpoint docs

**Result:** Complete task checklist with testing built in.

---

### Step 5: Implement with Skills Guidance

```bash
# Working on Stripe integration
```

**Active Skills providing guidance:**
- `api-security-patterns` - Secure API design
- `auth-patterns` - Payment authentication
- `input-validation` - Validate payment data
- `test-coverage-strategy` - Test critical paths

**Code example influenced by Skills:**

```typescript
/**
 * Process payment with Stripe
 * Security: Validated by input-validation Skill
 * Auth: JWT token required (auth-patterns)
 */
export async function processPayment(
  req: AuthRequest,
  res: Response
) {
  // Input validation (input-validation Skill)
  const schema = z.object({
    amount: z.number().positive(),
    currency: z.string().length(3),
    paymentMethod: z.string()
  });
  
  const validated = schema.parse(req.body);
  
  // Authorization check (auth-patterns Skill)
  if (!req.user) {
    throw new UnauthorizedError();
  }
  
  // Process payment (api-security-patterns Skill)
  const payment = await stripe.paymentIntents.create({
    amount: validated.amount,
    currency: validated.currency,
    payment_method: validated.paymentMethod,
    customer: req.user.stripeCustomerId
  });
  
  // Test coverage ensured (test-coverage-strategy Skill)
  return res.json({ payment });
}
```

**Result:** Secure, tested, well-documented code.

---

### Step 6: Review & Create PR

```bash
/dotai:pr
```

**What happens:**
- dotai creates PR
- `code-review-checklist` Skill AUTO-LOADS
- Systematic quality review

**Checklist verified:**
- [ ] Functionality works (payment processing)
- [ ] Security audit passed (PCI compliance)
- [ ] Tests exist and pass (payment flow, webhooks)
- [ ] Input validation present
- [ ] Authorization checks included
- [ ] Documentation updated

**Result:** High-quality PR ready for review.

---

## Key Takeaways

**Commands provide structure:**
- `/fb:session-start` - Memory restoration
- `pnpm ctx backend` - Context loading
- `/dotai:create-prd-interactive` - Strategic planning
- `/dotai:parse-prd` - Task generation
- `/dotai:pr` - PR creation

**Skills provide knowledge:**
- `session-continuity` - Smart memory filtering
- `context-optimizer` - Token efficiency
- `api-excellence` - API design patterns
- `security-hardening` - Security best practices
- `testing-automation` - Test strategies
- `code-review-checklist` - Quality verification

**You stay in control:**
- You decide what to build
- You TYPE the commands
- Skills enhance automatically
- No manual activation needed

---

**This is the hybrid advantage: Proven workflows + Cutting-edge knowledge.**

