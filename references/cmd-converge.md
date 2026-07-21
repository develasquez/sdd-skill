# Reference: /sdd-converge — Detailed Behavior

## What This Command ACTUALLY Does

> [!IMPORTANT]
> `/sdd-converge` is **APPEND-ONLY to `tasks.md`**. It does NOT modify `spec.md`, `plan.md`, or any application code.

The command:
1. Reads `spec.md`, `plan.md`, `tasks.md`, and `constitution.md` as the **sole source of intent**
2. Assesses the current codebase against those artifacts
3. Identifies gaps between what was specified and what was implemented
4. **Appends** remaining work as new tasks at the bottom of `tasks.md` under `## Phase N: Convergence`

This is **not** a diff tool — it assesses the present state of code vs. feature artifacts. No git, no branch comparison, no history.

---

## When to Run

Run `/sdd-converge` ONLY AFTER `/sdd-implement` has already processed the current `tasks.md`. It surfaces what `/sdd-implement` didn't complete or missed.

---

## Operating Constraints (APPEND-ONLY)

The command MUST NOT:
- Modify `spec.md` or `plan.md` in any way
- Rewrite, renumber, reorder, or delete any existing task
- Modify, create, or delete any application code (that's `/sdd-implement`'s job)

When the codebase already satisfies everything, leave `tasks.md` **byte-for-byte unchanged** (no empty Convergence header).

---

## Gap Classification

For each item in the intent inventory (FR-###, SC-###, user story acceptance criteria), inspect the current code and produce a `Finding` only where there is a gap:

| Gap Type | Description |
|---|---|
| `missing` | Required work is absent from the code entirely |
| `partial` | Work exists but doesn't fully satisfy the requirement/acceptance criterion |
| `contradicts` | Code does something conflicting with stated intent or a constitution MUST principle |
| `unrequested` | Code contains work not called for by spec/plan/tasks (surface for awareness only) |

**Edge cases:**
- Little or no code yet → treat entire specified scope as `missing` (don't fail)
- Nothing remains → produce zero findings, report "converged"

---

## Severity Assignment

| Severity | When |
|---|---|
| **CRITICAL** | Violates a constitution MUST; `missing`/`contradicts` gap blocking P1 user story |
| **HIGH** | Missing or partial gap on a core functional requirement or acceptance criterion |
| **MEDIUM** | Partial gap on secondary requirement; unrequested addition with unclear justification |
| **LOW** | Minor partial gaps, polish, low-risk unrequested additions |

---

## Findings Summary (In-Session Output)

Before appending anything, output a compact findings table:

```markdown
## Convergence Findings

| ID | Gap Type | Severity | Source | Evidence | Remaining Work |
|----|----------|----------|--------|----------|----------------|
| F1 | missing  | HIGH     | FR-008 | No append-only guard in tasks_writer.py | Add append-only enforcement |
| F2 | partial  | MEDIUM   | US1/AC2 | Auth check present but missing for /admin | Extend auth to admin routes |

**Summary metrics:**
- X requirements / acceptance criteria checked
- Y plan decisions checked
- Z constitution principles checked
- Findings: N missing, N partial, N contradicts, N unrequested
```

---

## Appending Convergence Tasks

**If there are actionable findings**, append to the END of `tasks.md`:

1. Scan all existing task IDs, find maximum M. Determine next phase number N (highest existing + 1)
2. Write ONE new section header: `## Phase N: Convergence`
3. Emit one checklist item per finding, ordered CRITICAL/HIGH first:
   ```
   - [ ] T042 <imperative description> per <source-ref> (missing)
   - [ ] T043 <description> per FR-008 (partial)
   ```
   Where `<source-ref>` is: `FR-003`, `SC-002`, `US1/AC2`, `plan: storage decision`, `Constitution II`
4. Constitution-violation tasks MUST be emitted first and described as `CRITICAL`
5. Never reuse or renumber existing IDs

---

## Outcomes

**`tasks_appended`**: State how many tasks were appended under which phase, recommend running `/sdd-implement` to complete them.

**`converged`**: Report "✅ Converged — the implementation satisfies the spec, plan, and tasks." Recommend proceeding to review/PR.
