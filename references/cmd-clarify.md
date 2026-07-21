# Reference: /sdd-clarify — Detailed Behavior

## Ambiguity Taxonomy (9 Categories)

Scan the spec for `Partial` or `Missing` status in each category:

| Category | What to check |
|---|---|
| **Functional Scope & Behavior** | Core user goals, out-of-scope declarations, user roles/personas |
| **Domain & Data Model** | Entities, attributes, relationships, lifecycle/state transitions, data volume |
| **Interaction & UX Flow** | Critical user journeys, error/empty/loading states, accessibility |
| **Non-Functional Quality** | Performance (latency, throughput), scalability, reliability/uptime, security, compliance |
| **Integration & External Dependencies** | External services/APIs and failure modes, data formats, protocol assumptions |
| **Edge Cases & Failure Handling** | Negative scenarios, rate limiting, conflict resolution |
| **Constraints & Tradeoffs** | Technical constraints, rejected alternatives |
| **Terminology & Consistency** | Canonical glossary terms, avoided synonyms |
| **Completion Signals** | Acceptance criteria testability, measurable Definition of Done |

For each category with Partial/Missing status, generate a candidate question unless clarification would not materially change implementation.

---

## Question Limit & Prioritization

- **Maximum 5 questions** across the whole session
- If more than 5 categories remain unresolved, select top 5 by `(Impact × Uncertainty)` heuristic
- Priority order: scope > security/privacy > user experience > technical details
- Exclude: questions already answered, trivial stylistic preferences, plan-level execution details

---

## Sequential Questioning Protocol

Present **EXACTLY ONE question at a time**. Never reveal future questions.

### For multiple-choice questions:
1. Analyze all options and determine the **most suitable** based on best practices and risk reduction
2. Present recommendation prominently at the top:
   ```
   **Recommended:** Option [X] — [1-2 sentences of reasoning]
   ```
3. Render all options as a Markdown table:

   | Option | Description |
   |--------|-------------|
   | A | [Option A] |
   | B | [Option B] |
   | Short | Provide a different short answer (≤5 words) |

4. Add: `You can reply with the option letter (e.g., "A"), accept the recommendation by saying "yes" or "recommended", or provide your own short answer.`

### For short-answer questions:
```
**Suggested:** [your proposed answer] — [brief reasoning]
Format: Short answer (≤5 words). Accept with "yes" or provide your own.
```

### Handling answers:
- "yes", "recommended", "suggested" → use the stated recommendation/suggestion
- Otherwise, validate it maps to an option or fits ≤5 words
- If ambiguous, ask for disambiguation (doesn't count as new question)

---

## Encoding Answers Into the Spec

After each accepted answer:

1. Ensure a `## Clarifications` section exists (add it after the overview/context section)
2. Create `### Session YYYY-MM-DD` subheading (if not present for today)
3. Append bullet: `- Q: <question> → A: <final answer>`
4. Apply clarification to the most appropriate section:
   - Functional ambiguity → update Functional Requirements
   - Data shape/entities → update Data Model
   - Non-functional constraint → add measurable criteria in Success Criteria
   - Edge case/negative flow → add bullet under Edge Cases
   - Terminology conflict → normalize term across spec
5. **Save the spec file AFTER each integration** (atomic overwrite)
6. Replace obsolete contradictory text (don't duplicate)

---

## Re-validating the Spec Quality Checklist

After completing all questions, if `specs/[###-feature]/checklists/requirements.md` exists:
1. Re-evaluate each checkbox item against the updated spec
2. Toggle `[ ]` → `[x]` for items now passing
3. Toggle `[x]` → `[ ]` for items now failing (regressions)
4. Report before/after pass counts: e.g., `"12/16 → 15/16 items passing"`

---

## Completion Report

Report:
- Number of questions asked & answered
- Path to updated spec
- Sections touched (list names)
- Spec quality checklist status (before/after counts, newly checked, regressions)
- **Coverage Summary Table**:

  | Category | Status |
  |---|---|
  | Functional Scope | Resolved / Deferred / Clear / Outstanding |
  | Domain & Data Model | ... |
  | ... | ... |

- If Outstanding/Deferred remain, recommend whether to proceed to `/sdd-plan` or re-run `/sdd-clarify` later
