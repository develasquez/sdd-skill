# SDD Workflow Guide

The SDD lifecycle consists of 10 distinct, structured commands that guide software from existing-code understanding to verified, production-ready code.

```text
               ┌───────────────────────┐
               │     sdd-baseline      │  (Reverse-engineer existing codebase)
               └───────────┬───────────┘
                           │
                           ▼
               ┌───────────────────────┐
               │   sdd-constitution    │  (Project-wide governance)
               └───────────┬───────────┘
                           │
                           ▼
               ┌───────────────────────┐
               │      sdd-specify      │  (Feature request → specs/###-name/spec.md)
               └───────────┬───────────┘
                           │
                           ▼
               ┌───────────────────────┐
               │      sdd-clarify      │  (Interactive ambiguity resolution)
               └───────────┬───────────┘
                           │
                           ▼
               ┌───────────────────────┐
               │       sdd-plan        │  (Technical plan & design contracts)
               └───────────┬───────────┘
                           │
                           ▼
               ┌───────────────────────┐
               │       sdd-tasks       │  (Task breakdown by User Story P1/P2/P3)
               └───────────┬───────────┘
                           │
            ┌──────────────┴──────────────┐
            ▼                             ▼
  ┌───────────────────┐         ┌───────────────────┐
  │    sdd-analyze    │         │   sdd-checklist   │
  │ (Read-only check) │         │ (Domain quality)  │
  └─────────┬─────────┘         └─────────┬─────────┘
            │                             │
            └──────────────┬──────────────┘
                           │
                           ▼
               ┌───────────────────────┐
               │     sdd-implement     │  (Sequential execution & TDD)
               └───────────┬───────────┘
                           │
                           ▼
               ┌───────────────────────┐
               │      sdd-converge     │  (Re-align spec & code if diverged)
               └───────────────────────┘
```

---

## 0. `/sdd-baseline`
- **Goal**: Reverse-engineer an existing codebase into complete SDD artifacts.
- **Output**: `specs/000-baseline/{spec.md, plan.md, research.md, data-model.md, contracts/, quickstart.md}`.
- **When to run**: At project start for brownfield/legacy projects, before any other SDD command.
- **Key Actions**:
  - Scans project root for config, dependencies, and structure.
  - Reads source code to extract User Stories, FRs, entities, endpoints, and architecture.
  - Generates all plan-time artifacts (research, data-model, contracts, quickstart) from existing code.
  - Tags every inference with `[INFERRED FROM: path]` for human validation.

## 1. `/sdd-constitution`
- **Goal**: Establish or update non-negotiable project principles, coding standards, and architectural constraints.
- **Output**: `specs/constitution.md` (or `.specify/constitution.md`).
- **When to run**: At project start or when introducing project-wide architectural changes.

## 2. `/sdd-specify [feature description]`
- **Goal**: Convert a natural language description into a structured specification document.
- **Output**: `specs/[###-feature-name]/spec.md`.
- **Key Actions**:
  - Auto-allocates next sequential feature number (e.g. `001`, `002`).
  - Identifies prioritized User Stories (P1 MVP, P2, P3).
  - Uses `Given / When / Then` format for acceptance criteria.
  - Marks ambiguous requirements explicitly with `[NEEDS CLARIFICATION: ...]`.

## 3. `/sdd-clarify`
- **Goal**: Interactively resolve `[NEEDS CLARIFICATION]` tags in the specification before planning.
- **Key Actions**:
  - Scans `spec.md` for open questions.
  - Asks up to 5 targeted questions.
  - Encodes user answers directly back into `spec.md`.

## 4. `/sdd-plan [tech stack details]`
- **Goal**: Create technical architecture, data model, and API contracts based on `spec.md`.
- **Output**: `plan.md`, `research.md`, `data-model.md`, `contracts/`, `quickstart.md`.
- **Key Actions**:
  - Performs Constitution Check against project governance.
  - Resolves technology choices, platforms, dependencies.

## 5. `/sdd-tasks`
- **Goal**: Generate an actionable, prioritized task list from `plan.md` and `spec.md`.
- **Output**: `tasks.md`.
- **Task Format**: `[Txxx] [P?] [USx] Description with exact file path`
  - Grouped by Phase 1 Setup, Phase 2 Foundational (blocking), Phase 3+ User Stories (P1 MVP first), Phase N Polish.

## 6. `/sdd-analyze`
- **Goal**: Read-only cross-artifact consistency check.
- **Key Actions**:
  - Verifies alignment across `spec.md`, `plan.md`, `tasks.md`, and `constitution.md`.
  - Flags missing paths, unmapped user stories, or constitution violations.

## 7. `/sdd-checklist [type]`
- **Goal**: Generate domain-specific verification checklists (e.g., UX, Security, Performance).
- **Output**: `specs/[###-feature-name]/checklists/[type].md`.

## 8. `/sdd-implement`
- **Goal**: Execute tasks in `tasks.md` sequentially.
- **Key Actions**:
  - Verifies prerequisite checklists.
  - Implements code following TDD (if requested).
  - Updates checkboxes in `tasks.md` upon completion.

## 9. `/sdd-converge`
- **Goal**: Re-align specifications and codebase when implementation details or requirements have evolved during development.
- **Key Actions**: Updates `spec.md` or `plan.md` to match current code reality.
