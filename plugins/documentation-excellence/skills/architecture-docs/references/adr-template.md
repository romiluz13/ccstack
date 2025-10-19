# ADR-[NUMBER]: [Title]

**Date:** YYYY-MM-DD  
**Status:** [Proposed | Accepted | Deprecated | Superseded by ADR-XXX]  
**Deciders:** [List everyone involved in the decision]  
**Technical Story:** [Link to issue/ticket if applicable]

---

## Context and Problem Statement

[Describe the context and problem statement, e.g., in free form using two to three sentences. You may want to articulate the problem in form of a question.]

**Key Questions:**
- [What decision needs to be made?]
- [What problem are we trying to solve?]
- [What constraints do we have?]

## Decision Drivers

* [driver 1, e.g., a force, facing concern, ...]
* [driver 2, e.g., a force, facing concern, ...]
* [driver 3, e.g., a force, facing concern, ...]

## Considered Options

### Option 1: [Title]

**Description:**
[Detailed description of this option]

**Pros:**
* ✅ [Good aspect 1]
* ✅ [Good aspect 2]

**Cons:**
* ❌ [Bad aspect 1]
* ❌ [Bad aspect 2]

**Trade-offs:**
* [Trade-off 1]
* [Trade-off 2]

---

###Option 2: [Title]

**Description:**
[Detailed description of this option]

**Pros:**
* ✅ [Good aspect 1]
* ✅ [Good aspect 2]

**Cons:**
* ❌ [Bad aspect 1]
* ❌ [Bad aspect 2]

**Trade-offs:**
* [Trade-off 1]
* [Trade-off 2]

---

### Option 3: [Title]

**Description:**
[Detailed description of this option]

**Pros:**
* ✅ [Good aspect 1]
* ✅ [Good aspect 2]

**Cons:**
* ❌ [Bad aspect 1]
* ❌ [Bad aspect 2]

**Trade-offs:**
* [Trade-off 1]
* [Trade-off 2]

---

## Decision Outcome

**Chosen option:** "[Option X]", because [justification. e.g., only option that satisfies key criteria, best trade-off between X and Y, etc.]

### Consequences

**Positive:**
* ✅ [Positive consequence 1]
* ✅ [Positive consequence 2]

**Negative:**
* ❌ [Negative consequence 1, e.g., compromises X, makes Y more difficult]
* ❌ [Negative consequence 2]

**Neutral:**
* ⚪ [Neutral consequence 1]

### Implementation Plan

1. [Step 1]
2. [Step 2]
3. [Step 3]

**Timeline:** [Expected completion date or duration]  
**Dependencies:** [List any blockers or prerequisites]

---

## Validation

**Success Metrics:**
- [ ] [Metric 1: e.g., Response time < 200ms]
- [ ] [Metric 2: e.g., Code coverage > 80%]
- [ ] [Metric 3: e.g., Zero production incidents in first month]

**Review Date:** [Date to review if decision still holds]

---

## Links and References

* [Link type] [Link to ADR, code, documentation]
* [RFC XXXX] [Link if applicable]
* [Design Doc] [Link if exists]
* [Implementation PR] [Link when available]

---

## Example ADRs

### Example 1: Database Choice

```markdown
# ADR-001: Choose PostgreSQL for Primary Database

**Date:** 2024-01-15
**Status:** Accepted
**Deciders:** Engineering Team, CTO
**Technical Story:** PROJ-123

## Context and Problem Statement

We need to select a primary database for our new microservices architecture. The system will handle complex relational data with strong consistency requirements and potentially high read/write throughput.

**Key Questions:**
- Which database best supports our data model (complex relations)?
- What provides best performance for our read/write patterns?
- What offers best operational simplicity for our team size?

## Decision Drivers

* Need ACID transactions for financial data
* Complex relational queries (joins, aggregations)
* Team expertise (most comfortable with SQL)
* Open-source preference
* Strong community and ecosystem

## Considered Options

### Option 1: PostgreSQL

**Pros:**
* ✅ Full ACID compliance
* ✅ Excellent JSON support (JSONB)
* ✅ Rich extension ecosystem
* ✅ Strong team familiarity
* ✅ Free and open-source

**Cons:**
* ❌ Vertical scaling limitations
* ❌ Replication complexity

### Option 2: MongoDB

**Pros:**
* ✅ Horizontal scalability
* ✅ Flexible schema
* ✅ Good for rapid prototyping

**Cons:**
* ❌ No ACID transactions across documents (at time of decision)
* ❌ Team less familiar
* ❌ Joins are complex

### Option 3: MySQL

**Pros:**
* ✅ ACID compliance
* ✅ Good performance
* ✅ Wide adoption

**Cons:**
* ❌ Less feature-rich than PostgreSQL
* ❌ Licensing concerns (Oracle ownership)

## Decision Outcome

**Chosen option:** "PostgreSQL", because it provides the best combination of ACID compliance, relational data support, team familiarity, and modern features (JSONB, full-text search, etc.).

### Consequences

**Positive:**
* ✅ Strong consistency guarantees for financial transactions
* ✅ Team can be productive immediately
* ✅ Flexible enough for future needs (JSONB for semi-structured data)

**Negative:**
* ❌ Will need to plan for sharding if we exceed vertical scaling limits
* ❌ Replication setup requires careful planning

### Implementation Plan

1. Set up PostgreSQL 15 on AWS RDS
2. Configure read replicas for reporting queries
3. Implement connection pooling (PgBouncer)
4. Set up automated backups and point-in-time recovery

**Timeline:** 2 weeks  
**Dependencies:** AWS account setup, network configuration

## Validation

**Success Metrics:**
- [x] Query response time < 100ms for 95th percentile
- [x] Support 10,000 concurrent connections
- [x] Zero data loss in failure scenarios
- [ ] Team trained on PostgreSQL best practices (in progress)

**Review Date:** 2024-07-15 (6 months)

## Links

* [PostgreSQL Documentation](https://www.postgresql.org/docs/)
* [Team Training Plan](link)
* [Schema Design Doc](link)
```

---

## Tips for Writing ADRs

### DO:
* ✅ Write ADRs for significant architectural decisions
* ✅ Include the context and problem statement clearly
* ✅ Document all options considered, not just the chosen one
* ✅ Be honest about trade-offs and negative consequences
* ✅ Update status when superseded
* ✅ Keep ADRs immutable (don't change past decisions, create new ones)

### DON'T:
* ❌ Write ADRs for trivial decisions
* ❌ Hide negative consequences
* ❌ Delete old ADRs (mark as superseded instead)
* ❌ Make ADRs too long (aim for 1-2 pages)
* ❌ Skip the "why" - always explain reasoning

### When to Write an ADR

Write an ADR when:
- The decision has significant impact
- Multiple options exist
- The decision is hard to reverse
- Future developers will wonder "why did they do it this way?"
- There's disagreement in the team

Don't write an ADR for:
- Following established patterns
- Trivial configuration changes
- Obvious decisions with no alternatives

