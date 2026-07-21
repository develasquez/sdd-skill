# Reference: /sdd-plan — Detailed Behavior

## Phase 0: Research

For each unknown or "NEEDS CLARIFICATION" item found while filling the Technical Context:

1. Identify research tasks:
   - Each NEEDS CLARIFICATION → one research task
   - Each dependency → best practices research task
   - Each integration → patterns research task

2. Consolidate findings in `research.md` using format:
   ```
   ## Decision: [what was chosen]
   - **Rationale**: [why chosen]
   - **Alternatives considered**: [what else was evaluated]
   ```

**Output**: `research.md` with all NEEDS CLARIFICATION resolved before proceeding to Phase 1.

---

## Phase 1: Design & Contracts

**Prerequisites**: `research.md` complete

### 1. Data Model (`data-model.md`)

Extract entities from the feature spec:
- Entity name, fields, relationships
- Validation rules from requirements
- State transitions (if applicable)

### 2. Interface Contracts (`contracts/`)

> [!NOTE]
> Only create `contracts/` if the project has **external interfaces**. Skip entirely if the project is purely internal (build scripts, one-off tools, etc.).

Types of contracts by project type:
- **Web services**: REST/GraphQL endpoint specifications
- **Libraries**: Public API specifications
- **CLI tools**: Command schemas and output formats
- **Applications**: UI contracts, event types

### 3. Quickstart Validation Guide (`quickstart.md`)

Document runnable validation scenarios that prove the feature works end-to-end.

**INCLUDE:**
- Prerequisites and setup commands
- Test/run commands with expected outcomes
- References/links to contracts and data model

**DO NOT INCLUDE:**
- Full implementation code
- Model/service/controller bodies
- Complete migrations
- Complete test suites
- Anything that belongs in `tasks.md`

This artifact is a **validation/run guide**, not an implementation guide.

---

## Constitution Gates

Before finalizing the plan, check `specs/constitution.md` (or `.specify/constitution.md`):

- Verify all architectural choices comply with MUST principles
- If a gate violation is found and cannot be justified → **ERROR**, do not proceed
- Document any tradeoffs in `research.md`

---

## Completion Report

Report:
- Feature directory path
- `plan.md` path
- Generated artifacts: `research.md`, `data-model.md`, `contracts/` (if created), `quickstart.md`
- Constitution check: PASS or violations found
