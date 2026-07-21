---
name: sdd-skill
description: Specification-Driven Development (SDD) skill for AI coding assistants (Claude, Antigravity, OpenCode, Cursor, Codex, Gemini). Inverts the power dynamic so code serves executable specifications. Provides complete workflows for constitution, specify, clarify, plan, tasks, implement, checklist, analyze, converge, and taskstoissues.
---

# Specification-Driven Development (SDD) Skill

This skill equips AI coding agents with **Specification-Driven Development (SDD)** capabilities. Under SDD, specifications and technical plans are the primary, executable source of truth. Code is a continuously generated expression of the specification.

> **How to use the references**: Each command below has a corresponding deep-dive file in `references/cmd-<name>.md`. Read the reference file for the full behavioral rules, output formats, and WRONG/CORRECT examples before executing the command.

---

## SDD Core Philosophy

1. **Power Inversion**: Specifications do not serve code — code serves specifications. Updating a feature means evolving the spec and plan first.
2. **Intent-Driven Development**: Developers specify intent, acceptance criteria, and constraints in natural language; AI agents generate architecture, tasks, and code.
3. **Executable Specifications**: Specifications are precise, complete, and testable. Ambiguities are explicitly marked with `[NEEDS CLARIFICATION: ...]`.
4. **MVP-First Story Slicing**: User journeys are prioritized (P1, P2, P3). User Story 1 (P1) is an independently testable Minimum Viable Product (MVP).

---

## Quick Command Reference

| Command | Action | Primary Output | Reference |
|---|---|---|---|
| `/sdd-constitution` | Establish or update non-negotiable project governance | `specs/constitution.md` | — |
| `/sdd-specify [description]` | Create feature specification from natural language description | `specs/[###-feature]/spec.md` + `checklists/requirements.md` | `references/cmd-specify.md` |
| `/sdd-clarify` | Interactively resolve ambiguities (1 question at a time, max 5) | Updated `spec.md` | `references/cmd-clarify.md` |
| `/sdd-plan [tech stack]` | Create technical architecture, research & design contracts | `plan.md`, `research.md`, `contracts/`, `quickstart.md` | `references/cmd-plan.md` |
| `/sdd-tasks` | Breakdown plan into actionable, prioritized task list | `tasks.md` | `references/cmd-tasks.md` |
| `/sdd-analyze` | Read-only cross-artifact consistency & quality analysis (6 categories, CRITICAL→LOW severity) | Consistency Report | `references/cmd-analyze.md` |
| `/sdd-checklist [type]` | Generate domain quality checklists ("Unit Tests for English") | `checklists/[type].md` | `references/cmd-checklist.md` |
| `/sdd-implement` | Execute tasks sequentially; auto-creates ignore files; gates on checklists | Working Code + Updated `tasks.md` | `references/cmd-implement.md` |
| `/sdd-converge` | Assess codebase against spec/plan/tasks and APPEND missing work to `tasks.md` | `tasks.md` (appended only) | `references/cmd-converge.md` |
| `/sdd-taskstoissues` | Convert `tasks.md` tasks into GitHub Issues (requires GitHub MCP) | GitHub Issues | `references/cmd-taskstoissues.md` |

---

## Detailed Command Instructions

### 1. `/sdd-constitution`
- **When to run**: At project start or when adding project-wide constraints.
- **Agent Instructions**:
  1. Check if `specs/constitution.md` or `.specify/constitution.md` exists.
  2. If missing, load `templates/constitution-template.md` from this skill.
  3. Prompt user for project-specific principles (e.g. TDD enforcement, CLI-first, zero secrets, performance budgets).
  4. Write the project constitution to `specs/constitution.md`.

---

### 2. `/sdd-specify [description]`
- **When to run**: Starting a new feature.
- **Reference**: `references/cmd-specify.md` — feature naming algorithm, auto-checklist generation, NEEDS CLARIFICATION rules, Success Criteria guidelines.
- **Agent Instructions**:
  1. Generate a **2-4 word action-noun short name** from the description (e.g., `user-auth`, `analytics-dashboard`).
  2. Determine the next sequential number by scanning `specs/` — create directory `specs/[NNN-short-name]/`.
  3. Persist the resolved path to `.specify/feature.json`.
  4. Fill out the spec using `templates/spec-template.md` as structure:
     - **User Stories**: Prioritized P1 (MVP), P2, P3. Each story MUST be independently testable using `Given / When / Then` acceptance criteria.
     - **Functional Requirements**: `FR-001`, `FR-002`...
     - **Success Criteria**: `SC-001`, `SC-002`... (technology-agnostic, measurable metrics — no frameworks/APIs).
     - **Ambiguities**: Use `[NEEDS CLARIFICATION: specific question]` — **maximum 3 markers total**.
  5. Auto-generate `specs/[###-feature]/checklists/requirements.md` and validate spec against it (up to 3 iterations).
  6. If `[NEEDS CLARIFICATION]` markers remain, present them as inline questions (max 3, one table per question) and wait for user answers before saving.

---

### 3. `/sdd-clarify`
- **When to run**: Before technical planning, to resolve ambiguities in `spec.md`.
- **Reference**: `references/cmd-clarify.md` — 9-category taxonomy, sequential questioning protocol, encoding format, coverage summary table.
- **Agent Instructions**:
  1. Read active `specs/[###-feature]/spec.md`.
  2. Scan using the **9-category ambiguity taxonomy**: Functional Scope, Domain & Data Model, Interaction & UX, Non-Functional Quality, Integration & Dependencies, Edge Cases, Constraints & Tradeoffs, Terminology, Completion Signals.
  3. Generate a prioritized queue of up to **5 targeted questions**. Present **ONE at a time** with a prominent recommendation.
  4. After each accepted answer, encode it into spec under `## Clarifications > ### Session YYYY-MM-DD` AND update the relevant spec section.
  5. Re-validate `checklists/requirements.md` (if it exists) after all answers are integrated.
  6. Output a Coverage Summary Table showing Resolved/Deferred/Clear/Outstanding status per category.

---

### 4. `/sdd-plan [tech stack]`
- **When to run**: When `spec.md` is complete and clear.
- **Reference**: `references/cmd-plan.md` — Phase 0 research, quickstart.md scope rules, contracts optionality, constitution gates.
- **Agent Instructions**:
  1. Read `specs/constitution.md` (if present) and verify Constitution Gates — ERROR if violations are unjustified.
  2. **Phase 0 — Research**: For each unknown or NEEDS CLARIFICATION, produce research tasks and consolidate findings into `research.md` (Decision / Rationale / Alternatives format).
  3. **Phase 1 — Design**: Produce supporting design artifacts in `specs/[###-feature]/`:
     - `plan.md`: Technical context, architecture, project layout.
     - `research.md`: Tech decisions, library benchmarks, rationale.
     - `data-model.md`: Schema definitions, entities, relationships.
     - `contracts/`: API specifications, schemas, event types (**only if project has external interfaces**).
     - `quickstart.md`: Runnable validation scenarios — **NOT implementation code or full test suites**.

---

### 5. `/sdd-tasks`
- **When to run**: After `plan.md` and design artifacts exist.
- **Reference**: `references/cmd-tasks.md` — exact task format, WRONG/CORRECT examples, [USx] label rules, tests-optional rule.
- **Agent Instructions**:
  1. Read `spec.md`, `plan.md`, `data-model.md`, `contracts/` (if present).
  2. **Tests are OPTIONAL** — only include test tasks if the spec or user explicitly requests them.
  3. Generate tasks in strict checklist format: `- [ ] T001 [P?] [USx] Description with exact file path`
     - `[USx]` label is **REQUIRED** in User Story phases, **NOT included** in Setup/Foundational/Polish phases.
  4. Group tasks into phases:
     - **Phase 1: Setup** — No `[USx]` label. Directory layout, tooling.
     - **Phase 2: Foundational** — No `[USx]` label. Core schemas, middleware, DB connections. Blocks all user stories.
     - **Phase 3+: User Story N (Px)** — `[USx]` label REQUIRED. One phase per story, in priority order.
     - **Final Phase: Polish** — No `[USx]` label. Documentation, optimization, cleanup.
  5. Output a completion report: total tasks, per-story count, parallel opportunities, MVP scope.

---

### 6. `/sdd-analyze`
- **When to run**: Pre-implementation check. Run AFTER `tasks.md` exists.
- **Reference**: `references/cmd-analyze.md` — 6 detection categories, CRITICAL/HIGH/MEDIUM/LOW severity, structured table format.
- **Agent Instructions**:
  1. **Read-only** — do NOT edit files.
  2. Load `spec.md`, `plan.md`, `tasks.md`, and `constitution.md`.
  3. Run **6 detection passes**: Duplication, Ambiguity, Underspecification, Constitution Alignment, Coverage Gaps, Inconsistency.
  4. Assign severity: **CRITICAL** (constitution violations, zero-coverage blockers) / **HIGH** / **MEDIUM** / **LOW**.
  5. Output a structured Markdown table (max 50 findings) + Coverage Summary Table + Metrics.
  6. Offer remediation suggestions, but do NOT apply them without explicit user approval.

---

### 7. `/sdd-checklist [type]`
- **When to run**: Adding specialized domain verification before or during implementation.
- **Reference**: `references/cmd-checklist.md` — "Unit Tests for English" concept, WRONG/CORRECT examples, CHK### IDs, append-only behavior.
- **Agent Instructions**:
  1. **Core concept**: Checklist items validate the **quality of requirements**, NOT whether the implementation works. Every item must ask "Is X clearly specified?" not "Does X work correctly?"
  2. Ask up to 3 clarifying questions to determine focus, depth, and audience.
  3. Generate items using the 9 standard category headings (Completeness, Clarity, Consistency, Acceptance Criteria Quality, Scenario Coverage, Edge Case Coverage, Non-Functional Requirements, Dependencies & Assumptions, Ambiguities & Conflicts).
  4. File behavior: **Append-only**. If `checklists/[type].md` exists, continue from the last CHK ID. If not, create and start at CHK001.
  5. Soft cap: 40 items. Merge near-duplicates.

---

### 8. `/sdd-implement`
- **When to run**: Executing feature development.
- **Reference**: `references/cmd-implement.md` — checklist gate table, ignore files auto-creation, task execution rules, error handling.
- **Agent Instructions**:
  1. Verify prerequisite files: `spec.md`, `plan.md`, `tasks.md`.
  2. **Checklist gate**: Scan all `checklists/*.md`, build a status table. If any are incomplete, ask user to confirm before proceeding. Halt if user says no.
  3. Auto-detect and create/verify ignore files (`.gitignore`, `.dockerignore`, etc.) based on tech stack in `plan.md`.
  4. Process tasks phase-by-phase:
     - Write tests FIRST only if test tasks are explicitly listed in `tasks.md`.
     - Implement code in target files (models → services → endpoints/UI).
     - Mark each completed task in `tasks.md`: `- [x] T001...`
     - Parallel tasks `[P]` can run together; sequential tasks must complete before the next starts.
     - Halt if a non-parallel task fails. For parallel task failures, continue others and report.
  5. Pause at User Story phase checkpoints to validate independence.

---

### 9. `/sdd-converge`
- **When to run**: After `/sdd-implement` has processed `tasks.md` and the codebase may have drifted from the spec.
- **Reference**: `references/cmd-converge.md` — APPEND-ONLY constraint, gap types, severity, convergence task format.
- **Agent Instructions**:
  1. **CRITICAL**: This command is **APPEND-ONLY to `tasks.md`**. It NEVER modifies `spec.md`, `plan.md`, or application code.
  2. Read `spec.md`, `plan.md`, and `tasks.md` as the sole source of intent.
  3. Assess the current codebase against each FR-###, SC-###, and user story acceptance criterion.
  4. Classify each gap as: `missing` / `partial` / `contradicts` / `unrequested`.
  5. Assign severity: **CRITICAL** (constitution MUST violation or P1-blocking) / **HIGH** / **MEDIUM** / **LOW**.
  6. Output a **Convergence Findings** table (in-session, no file writes yet).
  7. If there are actionable findings, append `## Phase N: Convergence` to `tasks.md` with new task IDs continuing from the existing maximum.
  8. If codebase already satisfies everything → report "✅ Converged" and leave `tasks.md` unchanged.

---

### 10. `/sdd-taskstoissues`
- **When to run**: After `tasks.md` is generated, to track work in GitHub Issues.
- **Reference**: `references/cmd-taskstoissues.md` — deduplication, GitHub MCP requirements, issue title format.
- **Requires**: GitHub MCP server (`github/github-mcp-server`). Skip if not available.
- **Agent Instructions**:
  1. Verify the repo remote is a GitHub URL. Do NOT proceed otherwise.
  2. Fetch existing issues and build a set of task IDs that already have issues (deduplication).
  3. For each uncovered task, create an issue with title format: `T001: <description>`.
  4. Report: issues created, issues skipped (already existed), any errors.
