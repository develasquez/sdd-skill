# Reference: /sdd-checklist — Detailed Behavior

## Core Concept: "Unit Tests for English"

**CRITICAL**: Checklists are **UNIT TESTS FOR REQUIREMENTS WRITING** — they validate the quality, clarity, and completeness of *requirements*, NOT the implementation.

### WRONG ❌ (testing implementation behavior)
```
- [ ] Verify the button clicks correctly
- [ ] Test error handling works
- [ ] Confirm the API returns 200
- [ ] Verify landing page displays 3 episode cards
```

### CORRECT ✅ (testing requirements quality)
```
- [ ] Are visual hierarchy requirements defined for all card types? [Completeness]
- [ ] Is 'prominent display' quantified with specific sizing/positioning? [Clarity]
- [ ] Are hover state requirements consistent across all interactive elements? [Consistency]
- [ ] Are accessibility requirements defined for keyboard navigation? [Coverage]
- [ ] Does the spec define what happens when logo image fails to load? [Edge Cases]
```

**Metaphor**: If your spec is code written in English, the checklist is its unit test suite. You're testing whether the requirements are well-written, complete, unambiguous, and ready for implementation.

---

## Required Item Patterns

| Pattern | Purpose |
|---|---|
| "Are [requirement type] defined/specified/documented for [scenario]?" | Completeness |
| "Is [vague term] quantified/clarified with specific criteria?" | Clarity |
| "Are requirements consistent between [section A] and [section B]?" | Consistency |
| "Can [requirement] be objectively measured/verified?" | Measurability |
| "Are [edge cases/scenarios] addressed in requirements?" | Coverage |
| "Does the spec define [missing aspect]?" | Completeness |

## Prohibited Patterns ❌

Any item starting with "Verify", "Test", "Confirm", "Check" + implementation behavior. References to code execution, user actions, or system behavior. "Displays correctly", "works properly", "functions as expected". "Click", "navigate", "render", "load", "execute".

---

## 9 Standard Category Headings

```
## Requirement Completeness
## Requirement Clarity
## Requirement Consistency
## Acceptance Criteria Quality
## Scenario Coverage
## Edge Case Coverage
## Non-Functional Requirements
## Dependencies & Assumptions
## Ambiguities & Conflicts
```

---

## Item Format & IDs

Every item follows: `- [ ] CHK### <requirement quality question> [Dimension, Spec §X.Y or Gap/Ambiguity/Conflict/Assumption]`

- IDs are globally incrementing: CHK001, CHK002...
- **Traceability**: ≥80% of items MUST include at least one reference: `[Spec §X.Y]`, `[Gap]`, `[Ambiguity]`, `[Conflict]`, or `[Assumption]`

Examples:
```
- [ ] CHK001 Are the number and layout of featured episodes explicitly specified? [Completeness, Spec §FR-001]
- [ ] CHK002 Is 'fast loading' quantified with specific timing thresholds? [Clarity, Spec §NFR-2]
- [ ] CHK003 Are error handling requirements defined for all API failure modes? [Gap]
- [ ] CHK004 Is the rollback behavior specified for migration failures? [Gap, Edge Case]
```

---

## File Handling (Append-Only)

- **Filename**: short descriptive name based on domain: `ux.md`, `api.md`, `security.md`, `performance.md`
- **If file does NOT exist**: create new file, start IDs at CHK001
- **If file exists**: APPEND new items continuing from last CHK ID (e.g., last is CHK015 → start new at CHK016)
- **NEVER delete or replace existing checklist content**

---

## Content Limits

- **Soft cap**: If raw candidate items > 40, prioritize by risk/impact
- Merge near-duplicates checking the same requirement aspect
- If > 5 low-impact edge cases: create one item: "Are edge cases X, Y, Z addressed in requirements? [Coverage]"

---

## Clarifying Questions Before Generation (Max 3)

Before generating, ask up to 3 questions derived from the spec signals:
- Scope refinement
- Risk prioritization (which areas get mandatory gating checks?)
- Depth calibration (lightweight pre-commit vs formal release gate?)
- Audience framing (author only vs PR reviewers?)

Generate questions ONLY if they materially change checklist content.

---

## Completion Report

Report:
- Full path to checklist file
- Item count
- Whether file was created new or appended
- Focus areas selected
- Any explicit user-specified must-have items incorporated
