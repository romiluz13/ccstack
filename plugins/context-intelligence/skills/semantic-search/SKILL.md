---
name: semantic-search
description: Find relevant code, documentation, and patterns using semantic search strategies. Use when searching for implementations, finding examples, or discovering related code across the codebase.
---

# Semantic Search

Advanced strategies for finding relevant code and documentation using meaning-based search rather than exact text matching.

## When to Use This Skill

- Finding specific function implementations
- Discovering similar patterns in codebase
- Locating relevant documentation
- Understanding code relationships
- Finding usage examples
- Identifying duplicate logic
- Exploring unfamiliar codebases
- Researching how features work

## Core Concepts

### 1. Semantic vs. Exact Search

**Exact Search (grep, text search):**
```bash
# Find literal string "calculateTotal"
grep "calculateTotal" **/*.ts

# Misses:
- calculateTotalAmount
- computeTotal
- getTotalCalculation
```

**Semantic Search (codebase_search):**
```bash
# Find by meaning: "calculate total"
codebase_search: "How do we calculate order totals?"

# Finds:
- calculateTotal() ✅
- calculateTotalAmount() ✅
- computeTotal() ✅
- getTotalCalculation() ✅
- Any function computing sums ✅
```

**Rule: Use semantic search for exploration, exact search for known targets.**

### 2. Query Formulation

**Bad Queries (Too vague):**
```
"authentication" → Too broad, 1000+ results
"config" → Generic, many unrelated matches
"user" → Everywhere, not helpful
```

**Good Queries (Specific intent):**
```
"How do we authenticate users with JWT?" → Precise
"Where is API configuration loaded?" → Clear purpose
"How do we validate user input in forms?" → Specific context
```

**Rule: Ask complete questions, not keywords.**

### 3. Search Refinement

**Progressive narrowing:**

```
Round 1: Broad exploration
"How does authentication work?"
→ Finds 50 results across system

Round 2: Narrow to area
"How does JWT authentication work in API?"
→ Finds 10 results in backend

Round 3: Specific file
"How is JWT validated in auth middleware?"
→ Finds exact implementation
```

**Rule: Start broad, narrow progressively.**

## Search Strategies

### Strategy 1: Question-Based Search

**Instead of keywords, ask questions:**

```bash
❌ BAD: "payment processing"
✅ GOOD: "How do we process credit card payments?"

❌ BAD: "database connection"
✅ GOOD: "Where is the database connection established?"

❌ BAD: "error handling"
✅ GOOD: "How do we handle API errors?"
```

**Why: Questions capture intent, keywords don't.**

### Strategy 2: Context Layers

**Search in layers from high to low:**

```
Layer 1: Architecture
"What is the overall authentication architecture?"
→ Understand system design

Layer 2: Implementation
"How is authentication implemented in the backend?"
→ Find specific code

Layer 3: Details
"Where are JWT tokens validated?"
→ Exact function/line
```

### Strategy 3: Relationship Discovery

**Find connections between components:**

```bash
# Find what calls a function
"What calls the calculateTotal function?"

# Find what a function calls
"What does the processPayment function call?"

# Find similar implementations
"Are there other functions that calculate totals?"

# Find usages
"Where is the User model used?"
```

### Strategy 4: Pattern Mining

**Discover patterns across codebase:**

```bash
# Find authentication patterns
"Show me all authentication implementations"

# Find error handling patterns
"How do we handle errors in API endpoints?"

# Find testing patterns
"How do we test database operations?"

# Find configuration patterns
"How are environment variables used?"
```

## Search Techniques

### Technique 1: Synonym Expansion

**Think of alternative terms:**

```
Looking for: Authentication logic

Search variations:
1. "How do we authenticate users?"
2. "Where is login implemented?"
3. "How do we verify user identity?"
4. "Where is auth token validated?"

Each may find different relevant code
```

### Technique 2: Scope Restriction

**Narrow search to relevant areas:**

```bash
# Full codebase search (slow, noisy)
codebase_search: "payment processing"

# Restricted to backend (faster, focused)
codebase_search in backend/: "payment processing"

# Restricted to specific module (fastest, precise)
codebase_search in backend/payments/: "payment processing"
```

**Rule: Use smallest scope that might contain answer.**

### Technique 3: Multi-Query Strategy

**Run multiple related queries:**

```bash
Query 1: "How is user authentication implemented?"
→ Finds auth service

Query 2: "Where are user credentials validated?"
→ Finds validation logic

Query 3: "How are auth tokens generated?"
→ Finds token generation

Combined: Complete understanding of auth system
```

### Technique 4: Negative Search

**Exclude irrelevant areas:**

```bash
# Find payment code, but not tests
"payment processing" -test -spec -mock

# Find auth code, but not external libraries
"authentication" in src/ (not node_modules/)

# Find config, but not examples
"configuration loading" -example -sample
```

## Search Patterns for Common Tasks

### Finding Implementation

**Task: "How is X implemented?"**
```bash
1. Search: "How is [X] implemented?"
2. If too broad: "Where in [area] is [X] implemented?"
3. If too narrow: "What are examples of [X] implementation?"
```

### Finding Usage

**Task: "Where is X used?"**
```bash
1. Search: "Where is [X] used?"
2. Alternative: "What calls [X]?"
3. Alternative: "Show examples of [X] usage"
```

### Finding Similar Code

**Task: "Are there other X?"**
```bash
1. Search: "Are there other implementations of [X]?"
2. Alternative: "Find all [X] patterns"
3. Alternative: "Show me similar code to [X]"
```

### Understanding Flow

**Task: "How does X work?"**
```bash
1. Search: "How does [X] work?" (architecture)
2. Search: "What is the flow of [X]?" (sequence)
3. Search: "What happens when [X]?" (process)
```

## Common Pitfalls

### Pitfall 1: Over-Specific Queries

**Problem:**
```bash
# Too specific, might miss variations
"getUserById function in user service"

# May miss:
- getUserByID (capitalization)
- fetchUserById (synonym)
- userService.getById (different structure)
```

**Solution:**
```bash
# More flexible query
"How do we get a user by ID?"

# Finds all variations
```

### Pitfall 2: Keyword-Only Search

**Problem:**
```bash
# Keywords without context
"authentication JWT token"

# Unclear: Looking for validation? Generation? Storage?
```

**Solution:**
```bash
# Complete question
"How do we validate JWT tokens for authentication?"

# Clear intent
```

### Pitfall 3: Ignoring File Context

**Problem:**
```bash
# Searching without file/directory hints
"payment calculation"

# May search entire codebase including tests, docs, etc.
```

**Solution:**
```bash
# Provide file context
"payment calculation in backend services"
"payment calculation in src/ directory"
```

### Pitfall 4: Not Refining Results

**Problem:**
```bash
# Initial query returns 100 results
# Give up or read all 100
```

**Solution:**
```bash
# Refine query based on results
Initial: "How does authentication work?" (100 results)
Refined: "How does JWT authentication work in API?" (10 results)
Final: "Where is JWT token validated?" (exact match)
```

## Integration with codebase_search Tool

**Use codebase_search for semantic queries:**

```typescript
// Example semantic searches:
codebase_search({
  query: "How do we authenticate API requests?",
  target_directories: ["backend/"]
})

codebase_search({
  query: "Where is user input validated?",
  target_directories: ["src/api/"]
})

codebase_search({
  query: "How do we handle database errors?",
  target_directories: ["backend/services/"]
})
```

**Benefits over grep:**
- Understands meaning, not just text
- Finds synonyms and variations
- Returns ranked results by relevance
- Better for exploration

## Best Practices Checklist

**Before Searching:**
- [ ] Formulate as a complete question
- [ ] Consider alternative phrasings
- [ ] Identify relevant scope/directory
- [ ] Decide if semantic or exact search

**During Search:**
- [ ] Start broad, narrow progressively
- [ ] Review top 5-10 results first
- [ ] Refine query if too many/few results
- [ ] Try synonyms if no matches

**After Finding:**
- [ ] Verify result relevance
- [ ] Check surrounding context
- [ ] Look for related implementations
- [ ] Note patterns for future searches

## Quick Reference

**Query Templates:**
```
Implementation: "How is [feature] implemented?"
Usage: "Where is [component] used?"
Pattern: "What is the pattern for [task]?"
Flow: "How does [process] work?"
Location: "Where is [thing] defined?"
Relationship: "What uses [component]?"
Similar: "Are there other [things] like this?"
```

**Scope Strategies:**
```
Unknown: Search full codebase first
Backend: Restrict to backend/, src/server/
Frontend: Restrict to frontend/, src/client/, components/
Tests: Restrict to __tests__/, *.test.*, *.spec.*
Docs: Restrict to docs/, README files
```

**Refinement Patterns:**
```
Too many results:
├─ Add more context
├─ Narrow scope
└─ Be more specific

Too few results:
├─ Broaden query
├─ Try synonyms
└─ Widen scope

Wrong results:
├─ Rephrase question
├─ Add domain context
└─ Specify area
```

**Decision Matrix:**
```
Know exact symbol?
└─ Yes → Use grep/exact search

Exploring unfamiliar code?
└─ Yes → Use semantic search

Looking for pattern?
└─ Yes → Use semantic search

Finding usage?
└─ Yes → Use semantic search (or both)

Know file and line?
└─ Yes → Direct file read
```

## Integration with Other Skills

**Works With:**
- `context-optimizer` - Find rules before loading context
- `token-efficiency` - Targeted search reduces token usage
- `architecture-patterns` - Discover architectural patterns

**Enhances:**
- Exploration tasks
- Code reviews (find related code)
- Refactoring (find all usages)
- Documentation (find examples)

---

**This Skill provides semantic search strategies for code exploration. Active when searching codebases or finding implementations.**

