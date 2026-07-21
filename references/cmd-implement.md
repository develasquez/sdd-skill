# Reference: /sdd-implement — Detailed Behavior

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
| `constitution.md` | If exists — governance constraints |
| `quickstart.md` | If exists — integration test scenarios |

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

### Order
1. **Phase-by-phase**: complete each phase before moving to the next
2. **Within a phase**: sequential tasks in order; parallel tasks `[P]` can run together
3. **TDD**: if test tasks exist in `tasks.md`, run tests BEFORE their implementation tasks
4. **File conflicts**: tasks affecting the same file MUST run sequentially

### Error Handling
- Non-parallel task fails → **halt execution**, report error with context
- Parallel task `[P]` fails → continue with successful tasks, report failed ones

### Progress Tracking
- Report progress after each completed task
- **Mark completed tasks** in `tasks.md`: change `- [ ] T001` → `- [x] T001`
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
