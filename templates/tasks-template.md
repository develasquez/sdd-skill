# Tasks: [FEATURE NAME]

**Input**: Design documents from `specs/[###-feature-name]/`
**Prerequisites**: `plan.md` (required), `spec.md` (required), `research.md`, `data-model.md`, `contracts/`

## Task Format: `[Txxx] [P?] [USx] [TAG?] Description`

- **[P]**: Can run in parallel (independent files, no blocking dependencies)
- **[USx]**: Maps task to User Story x (e.g., US1, US2, US3)
- **[TAG]**: Optional classification for critical tasks: `[DATABASE]`, `[SECURITY-CRITICAL]`, `[API]`, `[MIGRATION]`, `[UI]`, `[INFRASTRUCTURE]`
- Always include exact file paths in task descriptions.

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Initial structure & configuration

- [ ] T001 Create feature directory structure per plan
- [ ] T002 Initialize core dependencies and imports
- [ ] T003 [P] Configure linting, formatting, and build tools

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure required before user stories can begin

- [ ] T004 [DATABASE] Define core data schemas and database models
- [ ] T005 [P] Setup base middleware / error handling structures
- [ ] T006 [P] Configure environment variables and config loader

**Checkpoint**: Foundation complete - User Stories can now start independently

---

## Phase 3: User Story 1 - [Title] (Priority: P1) 🎯 MVP

**Goal**: [What this story delivers to the end user]
**Independent Test**: [How to verify this story works stand-alone]

### Tests for User Story 1 (Optional / If requested)
- [ ] T010 [P] [US1] Unit / Contract test for [endpoint/feature] in `tests/unit/test_[feature].py`

### Implementation for User Story 1
- [ ] T011 [P] [US1] Create data model in `src/models/[model].py`
- [ ] T012 [US1] Implement business service in `src/services/[service].py` (depends on T011)
- [ ] T013 [US1] Implement endpoint / entry point in `src/api/[route].py`
- [ ] T014 [US1] Add validation and error handling

**Checkpoint**: User Story 1 is fully functional and testable independently

---

## Phase 4: User Story 2 - [Title] (Priority: P2)

**Goal**: [What this story delivers to the end user]
**Independent Test**: [How to verify this story works stand-alone]

### Implementation for User Story 2
- [ ] T020 [P] [US2] Implement sub-component in `src/services/[feature2].py`
- [ ] T021 [US2] Integrate with User Story 1 components in `src/api/[route2].py`

**Checkpoint**: User Stories 1 and 2 work independently and together

---

## Phase N: Polish & Cross-Cutting Concerns

- [ ] T030 [P] Update user and API documentation
- [ ] T031 Refactor and clean up code
- [ ] T032 Run performance / security checks

---

> **Note**: For any critical task (database, security, API, migration), create a task spec at `tasks/[NNN-task-name]/task-TNNN.md` using `templates/task-template.md`.
