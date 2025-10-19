---
name: session-continuity
description: Ensure seamless session continuity through intelligent memory restoration and context preservation. Use when starting new sessions with /fb:session-start or resuming previous work.
---

# Session Continuity

Intelligent strategies for maintaining project continuity across sessions using Flashback integration.

## When to Use This Skill

- Starting new Claude Code session
- Using `/fb:session-start` command
- Resuming work after breaks
- Switching between multiple projects
- Recovering from interrupted sessions
- Onboarding to existing project work

## Core Concepts

### 1. Session Memory Hierarchy

```
Tier 1: Critical Context (Always restore)
├─ Current task/feature
├─ Active decisions
├─ Blocking issues
└─ Next immediate steps

Tier 2: Project State (Restore if relevant)
├─ Recent changes (last 24hrs)
├─ Active PRs/branches
├─ Tech stack updates
└─ Team communications

Tier 3: Historical Context (On demand)
├─ Past decisions & rationale
├─ Completed features
├─ Archived discussions
└─ Legacy patterns
```

### 2. Continuity Preservation

**What to preserve between sessions:**
- Working plan & progress
- Decision rationale
- Code patterns discovered
- Blockers & workarounds
- Team context & communications

**What not to preserve:**
- Outdated context (> 1 week)
- Completed task details
- Irrelevant discussions
- Temporary workarounds (if resolved)

### 3. Context Restoration Strategy

```
Session Start Flow:
1. Restore Tier 1 (critical - always)
2. Check Tier 2 (project state - if relevant)
3. Skip Tier 3 (historical - unless requested)

Result: Fast restoration with essential context
```

## Best Practices

### Starting Sessions

```bash
# ALWAYS start with session restoration
/fb:session-start

# Flashback restores:
- Working plan
- Last known state
- Active context
- Decision history

# session-continuity enhances:
- Prioritizes critical info
- Filters outdated context
- Focuses on actionable items
```

### Ending Sessions

```bash
# Save session state before ending
/fb:save-session

# Captures:
- Current progress
- Next steps
- Active decisions
- Context for next session

# session-continuity ensures:
- Only essential info saved
- Clear next-session guidance
- No bloat
```

### Mid-Session Saving

```bash
# After major milestones
# After important decisions
# Before switching contexts

/fb:save-session

# Creates checkpoint for recovery
```

## Integration with Flashback

**Flashback provides:** Memory infrastructure
**This Skill provides:** Intelligent restoration strategies

**Together:**
- Flashback stores session data
- session-continuity optimizes what/how to restore
- Result: Fast, relevant session starts

## Quick Reference

**Session Start Checklist:**
- [ ] Run /fb:session-start
- [ ] Review restored working plan
- [ ] Check for blockers/updates
- [ ] Verify context relevance
- [ ] Proceed with work

**Session End Checklist:**
- [ ] Document progress
- [ ] Note next steps
- [ ] Save important decisions
- [ ] Run /fb:save-session (if significant progress)

---

**This Skill auto-loads with /fb:session-start to enhance memory restoration.**

