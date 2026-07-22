# SDD — Specification-Driven Development

This project follows **Specification-Driven Development (SDD)**.

## Non-Negotiable Directives

### 1. Specifications First
Code serves specifications, not the other way around. Before implementing any change, ensure `spec.md` and `plan.md` exist and are up to date.

### 2. Constitution Injection
`specs/constitution.md` is the supreme governance document. It MUST be loaded and injected into the agent's system prompt before any implementation begins. All code MUST align with its MUST principles.

### 3. Task Spec Compliance
When a task in `tasks.md` has a corresponding spec at `tasks/*/task-TNNN.md`, its directives are mandatory. Follow the Before / During / After phases strictly.

### 4. Operational Tags
Tasks tagged with `[DATABASE]`, `[SECURITY-CRITICAL]`, `[MIGRATION]` have additional mandatory gates:
- `[DATABASE]` / `[MIGRATION]`: ⛔ No production migrations without validated rollback plan
- `[SECURITY-CRITICAL]`: All security checks must pass before marking complete

### 5. MVP-First Slicing
User Story 1 (P1) is always the independently testable MVP. Every subsequent story builds incrementally on P1.

### 6. No Silent Failures
All error modes must be explicitly handled. Log meaningful context at boundary interfaces.

## SDD Commands Available

| Command | Purpose |
|---------|---------|
| `/sdd-baseline` | Reverse-engineer existing codebase into SDD artifacts |
| `/sdd-specify` | Create feature specification |
| `/sdd-clarify` | Resolve ambiguities in spec |
| `/sdd-plan` | Create technical architecture and design |
| `/sdd-tasks` | Break down plan into prioritized tasks |
| `/sdd-implement` | Execute tasks with constitution injection |
| `/sdd-converge` | Detect drift between code and spec |
| `/sdd-analyze` | Cross-artifact consistency check |
