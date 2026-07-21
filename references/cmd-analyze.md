# Reference: /sdd-analyze — Detailed Behavior

## Operating Constraints

**STRICTLY READ-ONLY**: Do NOT modify any files. Output a structured analysis report only.
- Offer an optional remediation plan, but user must explicitly approve before any editing.
- If a constitution principle needs changing, that must happen in a separate `/sdd-constitution` run.

---

## Artifacts to Load

| Artifact | Sections to Load |
|---|---|
| `spec.md` | Overview, Functional Requirements, Success Criteria, User Stories, Edge Cases |
| `plan.md` | Architecture/stack, Data Model references, Phases, Technical constraints |
| `tasks.md` | Task IDs, Descriptions, Phase grouping, Parallel markers [P], Referenced file paths |
| `constitution.md` | All MUST/SHOULD normative statements |

**About Success Criteria**: Only include SC items that require **buildable work** (e.g., load-testing infrastructure, security audit tooling). Exclude post-launch outcome metrics and business KPIs (e.g., "Reduce support tickets by 50%").

---

## 6 Detection Categories

| Category | What to flag |
|---|---|
| **A. Duplication** | Near-duplicate requirements; mark lower-quality phrasing for consolidation |
| **B. Ambiguity** | Vague adjectives (fast, scalable, secure, intuitive) lacking measurable criteria; unresolved placeholders (TODO, ???, `<placeholder>`) |
| **C. Underspecification** | Requirements with verbs but missing object or measurable outcome; user stories missing acceptance criteria alignment; tasks referencing files not defined in spec/plan |
| **D. Constitution Alignment** | Any requirement or plan element conflicting with a MUST principle; missing mandated sections or quality gates |
| **E. Coverage Gaps** | Requirements with zero associated tasks; tasks with no mapped requirement/story; SC requiring buildable work not reflected in tasks |
| **F. Inconsistency** | Terminology drift (same concept named differently); data entities in plan but absent in spec (or vice versa); task ordering contradictions; conflicting requirements |

**Limit to 50 findings total.** Aggregate remainder in an overflow summary.

---

## Severity Assignment

| Severity | When to use |
|---|---|
| **CRITICAL** | Violates constitution MUST; missing core spec artifact; requirement with zero coverage that blocks baseline functionality |
| **HIGH** | Duplicate or conflicting requirement; ambiguous security/performance attribute; untestable acceptance criterion |
| **MEDIUM** | Terminology drift; missing non-functional task coverage; underspecified edge case |
| **LOW** | Style/wording improvements; minor redundancy not affecting execution order |

---

## Output Format

### Analysis Report (in-session output, no file writes)

```markdown
## Specification Analysis Report

| ID | Category | Severity | Location(s) | Summary | Recommendation |
|----|----------|----------|-------------|---------|----------------|
| A1 | Duplication | HIGH | spec.md:L120-134 | Two similar requirements... | Merge; keep clearer version |
| C1 | Underspecification | MEDIUM | tasks.md:T015 | References undefined file path | Define path in plan.md |
```

### Coverage Summary Table

```markdown
| Requirement Key | Has Task? | Task IDs | Notes |
|-----------------|-----------|----------|-------|
| FR-001          | ✅ Yes     | T012, T013 | |
| FR-007          | ❌ No      | —        | No tasks found |
```

### Metrics

- Total Requirements
- Total Tasks
- Coverage % (requirements with ≥1 task)
- Ambiguity Count
- Duplication Count
- Critical Issues Count

---

## Next Actions Block

- If CRITICAL issues: recommend resolving before `/sdd-implement`
- If only LOW/MEDIUM: user may proceed with improvement suggestions
- Provide explicit command suggestions: e.g., "Run `/sdd-tasks` to add coverage for FR-007"

---

## Remediation Offer

End with: "Would you like me to suggest concrete remediation edits for the top N issues?"
(Do NOT apply them automatically.)
