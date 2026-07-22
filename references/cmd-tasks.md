# Reference: /sdd-tasks — Detailed Behavior

## CRITICAL: Task Format

Every task MUST strictly follow this format:

```
- [ ] [TaskID] [P?] [Story?] Description with exact file path
```

**Components:**

| Component | Rules |
|---|---|
| `- [ ]` | ALWAYS start with markdown checkbox |
| `T001` | Sequential zero-padded 3-digit ID in execution order |
| `[P]` | Include ONLY if task is parallelizable (different files, no dependencies on incomplete tasks) |
| `[USx]` | **REQUIRED** for user story phase tasks. **NOT included** in Setup or Foundational phases |
| Description | Clear action with EXACT file path |

### Examples — CORRECT ✅

```
- [ ] T001 Create project structure per implementation plan
- [ ] T005 [P] Implement authentication middleware in src/middleware/auth.py
- [ ] T012 [P] [US1] Create User model in src/models/user.py
- [ ] T014 [US1] Implement UserService in src/services/user_service.py
```

### Examples — WRONG ❌

```
- [ ] Create User model                          ← missing ID and Story label
T001 [US1] Create model                         ← missing checkbox
- [ ] [US1] Create User model                   ← missing Task ID
- [ ] T001 [US1] Create model                   ← missing file path
```

---

## Tests are OPTIONAL

**CRITICAL**: Only generate test tasks if **explicitly requested** in the feature specification or by the user (e.g., "use TDD approach"). Do NOT add test tasks by default.

---

## Phase Structure

| Phase | Label Rules | Purpose |
|---|---|---|
| **Phase 1: Setup** | No [USx] label | Project initialization, directory structure, config |
| **Phase 2: Foundational** | No [USx] label | Blocking prerequisites for ALL user stories. MUST complete before any story |
| **Phase 3+: User Story N** | `[USx]` REQUIRED | One phase per user story, in priority order (P1, P2, P3...) |
| **Final Phase: Polish** | No [USx] label | Cross-cutting concerns, cleanup, optimization |

**Within each User Story phase** (ordered):
1. Tests (if requested) → mark `[P]`
2. Models → mark `[P]` if independent
3. Services → depends on models
4. Endpoints/UI → depends on services
5. Integration

**Checkpoint** after each User Story phase: the story should be fully functional and independently testable.

---

## [USx] Label Mapping

Map each user story from `spec.md` to a phase:
- Each user story (P1, P2, P3...) gets its own phase
- All tasks in that phase get the corresponding `[USx]` label
- US1 = Priority P1, US2 = Priority P2, etc.

---

## Task Organization Sources

| Source | What to extract |
|---|---|
| `plan.md` | Tech stack, libraries, project structure |
| `spec.md` | User stories with priorities → phase organization |
| `data-model.md` | Entities → map to user stories (put shared entities in earliest story or Foundational) |
| `contracts/` | Interface contracts → map to the user story they serve |
| `research.md` | Tech decisions → setup tasks |

---

---

## Task Spec Generation for Critical Tasks

When a task is identified as **architecturally significant, high-risk, or complex**, generate an individual task specification file using `templates/task-template.md`.

### Criteria for Task Spec Generation

Generate a task spec when a task involves any of the following:

| Criteria | Examples |
|---|---|
| Database schema changes | New tables, migrations, indexes, data backfills |
| Security-sensitive operations | Authentication, authorization, encryption, secrets management |
| External API integration | Third-party services, webhooks, payment gateways |
| Cross-cutting infrastructure | Caching layer, message queues, service mesh |
| Breaking changes | Contract changes, data format migrations, API versioning |
| High business risk | Payment flows, compliance, data loss prevention |

### Task Spec Output

Place the file at `tasks/[NNN-task-short-name]/task-TNNN.md`:

```
tasks/
└── 001-user-auth/
    ├── task-T001.md
    └── task-T005.md
```

### Task Spec Content

Fill `templates/task-template.md` with:
- **Operational Classification**: Apply one or more tags: `[DATABASE]`, `[SECURITY-CRITICAL]`, `[API]`, `[MIGRATION]`, `[UI]`, `[INFRASTRUCTURE]`
- **Before**: Consult decision history, search reference patterns, verify constitution alignment
- **During**: Implement in isolation, modular patterns
- **After**: Run tests, run security analysis if `[SECURITY-CRITICAL]`, run migration validation if `[DATABASE]`/`[MIGRATION]`, log decisions, commit with structured message
- **Database & Migration Policy**: ⛔ No production migrations without validated rollback plan, backup strategy, and seed data definition
- **Security Requirements**: Mandatory checks when `[SECURITY-CRITICAL]` is set

### Tag Propagation to `tasks.md`

Update the task line in `tasks.md` to include the classification tag:

```
- [ ] T012 [P] [US1] [DATABASE] Create User model in src/models/user.py
- [ ] T042 [SECURITY-CRITICAL] Encrypt PII fields at rest in src/models/user.py
```

### Report

Include in the completion report:
- Number of task specs generated
- List of task spec paths
- Classification tags used

---

## Completion Report

After generating `tasks.md`, report:
- Total task count
- Task count per user story
- Task specs generated (paths and tags)
- Parallel opportunities identified
- Independent test criteria for each story
- Suggested MVP scope (typically User Story 1 only)
- Format validation: confirm ALL tasks follow the checklist format (checkbox, ID, labels, file paths)
