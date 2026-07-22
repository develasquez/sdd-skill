# Reference: /sdd-implement — Detailed Behavior

## Step 0: Constitution Injection

**CRITICAL**: Before any implementation begins, the agent MUST:
1. Look for `specs/constitution.md` or `.specify/constitution.md`
2. If found, **inject its content into the system prompt** as active governance context
3. Verify that every task in the current phase aligns with all MUST principles
4. If a task violates a constitution MUST → **HALT** and report the violation

This ensures the agent operates under the project's non-negotiable constraints natively, preventing architectural regressions.

---

## Step 1: Checklist Gate

Before starting implementation, if `specs/[###-feature]/checklists/` exists, scan all checklist files and build a status table:

```
| Checklist    | Total | Completed | Incomplete | Status  |
|--------------|-------|-----------|------------|---------|
| ux.md        | 12    | 12        | 0          | ✓ PASS  |
| test.md      | 8     | 5         | 3          | ✗ FAIL  |
| security.md  | 6     | 6         | 0          | ✓ PASS  |
```

- **All PASS** → automatically proceed
- **Any FAIL** → display table and ask: "Some checklists are incomplete. Do you want to proceed with implementation anyway? (yes/no)"
  - "no" / "wait" / "stop" → halt execution
  - "yes" / "proceed" / "continue" → proceed

---

## Step 2: Load Implementation Context

| File | Requirement |
|---|---|
| `tasks.md` | **REQUIRED** — complete task list and execution plan |
| `plan.md` | **REQUIRED** — tech stack, architecture, file structure |
| `data-model.md` | If exists — entities and relationships |
| `contracts/` | If exists — API specifications |
| `research.md` | If exists — technical decisions and constraints |
| `constitution.md` | **ALWAYS load and inject into prompt** — governance constraints |
| `quickstart.md` | If exists — integration test scenarios |
| `tasks/task-*.md` | If exists — detailed specs for individual critical tasks |

### Task Spec Resolution

Before executing any task TNNN:
1. Check if `tasks/*/task-TNNN.md` exists
2. If found, **load and inject** its execution directives into the current context
3. Follow the `Before / During / After` phases defined in the task spec
4. Apply mandatory security checks and migration policies from the task spec

---

## Step 3: Project Setup Verification (Ignore Files)

Auto-detect and create/verify ignore files based on tech stack from `plan.md`:

| File | When to create |
|---|---|
| `.gitignore` | Always (if git repo detected) |
| `.dockerignore` | If Dockerfile exists or Docker mentioned in plan.md |
| `.eslintignore` | If .eslintrc* exists |
| `.prettierignore` | If .prettierrc* exists |

**Common patterns by tech stack:**

- **Node.js/TypeScript**: `node_modules/`, `dist/`, `build/`, `*.log`, `.env*`
- **Python**: `__pycache__/`, `*.pyc`, `.venv/`, `venv/`, `dist/`, `*.egg-info/`
- **Java**: `target/`, `*.class`, `*.jar`, `.gradle/`, `build/`
- **Go**: `*.exe`, `*.test`, `vendor/`, `*.out`
- **Rust**: `target/`, `debug/`, `release/`, `*.rs.bk`
- **Universal**: `.DS_Store`, `Thumbs.db`, `*.tmp`, `*.swp`

If ignore file already exists: verify it contains essential patterns, append only missing critical patterns.

---

## Step 4: Task Execution Rules

### Per-Task Phase Protocol (Before / During / After)

Every task — especially those with a task spec — follows this three-phase protocol:

#### Before (each task)
1. Load `constitution.md` and confirm task alignment with MUST principles
2. If a task spec exists at `tasks/*/task-TNNN.md`, load its directives
3. Consult decision history in memory store or `.specify/decisions/`
4. Search codebase for reference patterns to maintain consistency
5. Verify that all dependency tasks are completed

#### During (each task)
1. Implement code in isolation — modify ONLY files relevant to this task
2. Follow modular patterns from `plan.md` and existing code conventions
3. Do NOT over-engineer; implement the minimum required to satisfy the task
4. If `[P]` (parallel), can run concurrently with other `[P]` tasks
5. If `[DATABASE]` or `[MIGRATION]` tag is set, follow the migration policy

#### After (each task)
1. Run unit tests for the affected modules
2. Run security analysis if `[SECURITY-CRITICAL]` tag is set
3. Run database migration validation if `[DATABASE]` or `[MIGRATION]` tag is set
4. Register new architectural decisions in `.specify/decisions/` or equivalent
5. Mark task as completed in `tasks.md`: `- [x] TNNN`

### Order
1. **Phase-by-phase**: complete each phase before moving to the next
2. **Within a phase**: sequential tasks in order; parallel tasks `[P]` can run together
3. **TDD**: if test tasks exist in `tasks.md`, run tests BEFORE their implementation tasks
4. **File conflicts**: tasks affecting the same file MUST run sequentially

### Error Handling
- Non-parallel task fails → **halt execution**, report error with context
- Parallel task `[P]` fails → continue with successful tasks, report failed ones
- Constitution violation → **halt immediately**, report with severity

### Progress Tracking
- Report progress after each completed task
- **Mark completed tasks** in `tasks.md`: change `- [ ] TNNN` → `- [x] TNNN`
- Pause at phase checkpoints to validate before proceeding

---

## Step 5: Completion Validation

- Verify all required tasks are completed
- Check implemented features match the original specification
- Validate tests pass (if tests were included)
- Confirm implementation follows the technical plan

---

## Completion Report

Final status summary including:
- Tasks completed vs total
- Any failures or skipped tasks
- Recommended next steps (e.g., run `/sdd-converge` if scope drifted)
