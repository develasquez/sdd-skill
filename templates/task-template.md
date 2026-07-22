# Task Specification: TNNN — [Task Description]

**Source**: `tasks.md` — [Feature Name]
**Classification**: `[TAG]`
**Created**: [DATE]

## Operational Classification

| Tag | Applies |
|-----|---------|
| `[DATABASE]` | Yes / No |
| `[SECURITY-CRITICAL]` | Yes / No |
| `[API]` | Yes / No |
| `[MIGRATION]` | Yes / No |
| `[UI]` | Yes / No |
| `[INFRASTRUCTURE]` | Yes / No |

## Prerequisites Before Starting

- [ ] Load `constitution.md` and verify this task aligns with all MUST principles
- [ ] Consult decision history in memory store for prior architectural decisions
- [ ] Search codebase for reference patterns relevant to this task
- [ ] Review related task specs (if any exist)

## Dependencies

- **Blocked by**: [Txxx, Txxx]
- **Blocks**: [Txxx, Txxx]

---

## Execution Directives

### Before

1. Read `specs/constitution.md` and confirm no principle violation
2. Retrieve relevant past decisions from `.specify/decisions/` or memory store
3. Scan existing codebase for analogous patterns to replicate
4. Verify that all prerequisite tasks have been completed

### During

1. Implement code in isolation — modify ONLY the files listed in this spec
2. Follow modular patterns identified in `plan.md`
3. Respect existing code conventions (linting, naming, error handling)
4. Do NOT over-engineer; implement the minimum required to satisfy the task

### After

1. Run unit tests for the affected modules
2. Run security analysis tools if `[SECURITY-CRITICAL]` is set
3. Run database migration validation if `[DATABASE]` or `[MIGRATION]` is set
4. Register any new architectural decisions in `.specify/decisions/` or equivalent
5. Commit using a structured message:
   ```
   TNNN: [Short description]

   - What: [what was implemented]
   - Why: [rationale]
   - Tags: [tags]
   ```

---

## Database & Migration Policy

⛔ **ABSOLUTELY PROHIBITED** — Run migrations directly on production without:
- A validated rollback plan (tested in isolation first)
- Documented backup strategy
- Defined seed data initialization

✅ **REQUIRED** before marking task complete:
- [ ] Rollback plan written and validated
- [ ] Backup strategy documented
- [ ] Seed data initialization defined
- [ ] Migration tested in isolated environment

---

## Security Requirements

If `[SECURITY-CRITICAL]` is set, ALL of the following MUST pass:

- [ ] Security linter executed with zero critical findings
- [ ] No secrets, tokens, or credentials in code
- [ ] All user inputs validated and sanitized at boundaries
- [ ] Authentication and authorization enforced on every protected endpoint
- [ ] Dependencies scanned for known vulnerabilities

---

## Definition of Done

- [ ] Code implements the task description
- [ ] All existing tests pass
- [ ] New code follows existing conventions (lint, format, types)
- [ ] Required security checks pass
- [ ] Migration policy satisfied (if applicable)
- [ ] Architectural decisions logged
- [ ] Task marked as completed in `tasks.md`
