# Reference: /sdd-specify — Detailed Behavior

## Feature Directory Naming

1. Generate a **2-4 word short name** from the feature description:
   - Use action-noun format: `user-auth`, `analytics-dashboard`, `fix-payment-timeout`
   - Preserve technical terms: OAuth2, JWT, API
   - Examples: "I want to add user authentication" → `user-auth`

2. Determine prefix from `.specify/init-options.json` → `feature_numbering`:
   - `"sequential"` (default): next 3-digit number scanning `specs/` directory → `003-user-auth`
   - `"timestamp"`: current timestamp → `20260319-143022-user-auth`

3. Create directory: `specs/<prefix>-<short-name>/spec.md`

4. Persist to `.specify/feature.json`:
   ```json
   { "feature_directory": "specs/003-user-auth" }
   ```

---

## [NEEDS CLARIFICATION] Rules

- **MAXIMUM 3 markers total** across the entire spec
- Only use them when:
  - The choice significantly impacts feature scope or user experience
  - Multiple reasonable interpretations exist with different implications
  - No reasonable default exists
- **Do NOT ask about** (use reasonable defaults):
  - Data retention → industry-standard practices
  - Performance targets → standard web/mobile expectations
  - Authentication method → standard session-based or OAuth2 for web apps
  - Error handling → user-friendly messages with fallbacks

---

## Clarification Resolution (Inline)

When `[NEEDS CLARIFICATION]` markers remain after writing, present options in this format (max 3 questions):

```markdown
## Question [N]: [Topic]

**Context**: [Quote relevant spec section]
**What we need to know**: [Specific question]

**Suggested Answers**:

| Option | Answer | Implications |
|--------|--------|--------------|
| A      | [First answer] | [What this means] |
| B      | [Second answer] | [What this means] |
| Custom | Provide your own answer | |

**Your choice**: _[Wait for user response]_
```

Wait for all answers, then update spec replacing each marker.

---

## Spec Quality Checklist (Auto-generated)

After writing the spec, auto-generate `specs/[###-feature]/checklists/requirements.md`:

```markdown
# Specification Quality Checklist: [FEATURE NAME]

**Purpose**: Validate specification completeness and quality before proceeding to planning
**Created**: [DATE]
**Feature**: [Link to spec.md]

## Content Quality
- [ ] No implementation details (languages, frameworks, APIs)
- [ ] Focused on user value and business needs
- [ ] Written for non-technical stakeholders
- [ ] All mandatory sections completed

## Requirement Completeness
- [ ] No [NEEDS CLARIFICATION] markers remain
- [ ] Requirements are testable and unambiguous
- [ ] Success criteria are measurable
- [ ] Success criteria are technology-agnostic
- [ ] All acceptance scenarios are defined
- [ ] Edge cases are identified
- [ ] Scope is clearly bounded
- [ ] Dependencies and assumptions identified

## Feature Readiness
- [ ] All functional requirements have clear acceptance criteria
- [ ] User scenarios cover primary flows
- [ ] Feature meets measurable outcomes defined in Success Criteria
- [ ] No implementation details leak into specification
```

Run validation against each item. If items fail, update the spec and re-run (max 3 iterations).

---

## Success Criteria Guidelines

Success criteria MUST be:
- **Measurable**: include specific metrics (time, percentage, count, rate)
- **Technology-agnostic**: no frameworks, languages, databases, or tools
- **User-focused**: outcomes from user/business perspective, not system internals
- **Verifiable**: can be tested without knowing implementation details

**Good examples:**
- "Users can complete checkout in under 3 minutes"
- "System supports 10,000 concurrent users"
- "95% of searches return results in under 1 second"

**Bad examples (implementation-focused):**
- "API response time is under 200ms" → use "Users see results instantly"
- "Database can handle 1000 TPS" → use a user-facing metric
- "React components render efficiently" → framework-specific

---

## Completion Report

After finishing, report:
- Feature directory path
- Spec file path
- Checklist results summary
- Readiness for next phase (`/sdd-clarify` or `/sdd-plan`)
