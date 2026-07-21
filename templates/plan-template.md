# Implementation Plan: [FEATURE]

**Branch**: `[###-feature-name]` | **Date**: [DATE] | **Spec**: [link to spec.md]
**Input**: Feature specification from `specs/[###-feature-name]/spec.md`

## Summary

[Extract from feature spec: primary requirement + technical approach from research]

## Technical Context

**Language/Version**: [e.g., Python 3.11, TypeScript 5.0, Rust 1.75 or NEEDS CLARIFICATION]
**Primary Dependencies**: [e.g., FastAPI, React, Tokio or NEEDS CLARIFICATION]
**Storage**: [if applicable, e.g., PostgreSQL, Redis, SQLite or N/A]
**Testing**: [e.g., pytest, Vitest, cargo test or NEEDS CLARIFICATION]
**Target Platform**: [e.g., Linux server, iOS 15+, Browser or NEEDS CLARIFICATION]
**Project Type**: [e.g., library/cli/web-service/mobile-app/desktop-app or NEEDS CLARIFICATION]
**Performance Goals**: [domain-specific, e.g., <200ms p95, 1000 req/s or NEEDS CLARIFICATION]
**Constraints**: [domain-specific, e.g., <100MB memory, offline-capable or NEEDS CLARIFICATION]

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

[Verify alignment with project constitution in specs/constitution.md or .specify/constitution.md]

## Project Structure

### Feature Documentation

```text
specs/[###-feature]/
├── plan.md              # This file
├── research.md          # Technical research & decisions (Phase 0)
├── data-model.md        # Data entities and schemas (Phase 1)
├── quickstart.md        # Validation & test scenarios (Phase 1)
├── contracts/           # API and interface specs (Phase 1)
└── tasks.md             # Actionable task list (Phase 2)
```

### Source Code Layout

```text
src/
├── models/
├── services/
├── api/
└── lib/

tests/
├── unit/
├── integration/
└── contract/
```

**Structure Decision**: [Document selected layout and rationale]

## Complexity Tracking

| Violation / Deviation | Why Needed | Simpler Alternative Rejected Because |
|-----------------------|------------|--------------------------------------|
| [e.g., Extra layer]   | [Reason]   | [Why standard pattern insufficient]  |
