---
name: e2e-testing-patterns
description: End-to-end testing patterns with Playwright/Cypress including stable selectors and reliable tests. Use when writing E2E tests or implementing user flow testing.
---

# E2E Testing Patterns

Reliable end-to-end testing strategies for user workflows.

## When to Use

- User flow testing
- Integration testing
- Smoke tests
- Regression testing

## Core Patterns

### 1. Stable Selectors
```typescript
// ✅ GOOD: Data attributes
await page.click('[data-testid="login-button"]');

// ❌ BAD: CSS classes (change frequently)
await page.click('.btn-primary');
```

### 2. Page Object Model
```typescript
class LoginPage {
  async login(email: string, password: string) {
    await this.emailInput.fill(email);
    await this.passwordInput.fill(password);
    await this.submitButton.click();
  }
}
```

### 3. Wait for Conditions
```typescript
// Wait for element
await page.waitForSelector('[data-testid="dashboard"]');

// Wait for network
await page.waitForResponse(resp => resp.url().includes('/api/user'));
```

## Best Practices

- Use data-testid attributes
- Avoid hard-coded waits
- Test critical user flows
- Keep tests independent
- Clean up test data
- Run in CI/CD

---

**Auto-loads with E2E testing tasks.**

