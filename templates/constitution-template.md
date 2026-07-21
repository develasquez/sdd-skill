# [PROJECT_NAME] Constitution

## Core Principles

### I. Executable Specifications First (NON-NEGOTIABLE)
All features MUST start with a clear, unambiguous specification in `specs/`. Code serves specifications; specifications are the single source of truth.

### II. Test-Driven & Modular Architecture
Modules and features MUST be self-contained and independently testable. High coupling between unrelated modules is prohibited.

### III. Minimal Complexity (YAGNI)
Start simple. Do not over-architect for hypothetical future scale unless explicitly required by business metrics in the specification.

### IV. Observability & Error Handling
All failure modes must be explicitly handled. Silent failures are prohibited. Log meaningful context at boundary interfaces.

### V. Security & Privacy
No plain text secrets in code or configuration repositories. Validate and sanitize all user input at the boundaries.

## Governance

- This Constitution supersedes arbitrary design preferences.
- Any architectural violation in `plan.md` must be explicitly justified in the Complexity Tracking section.
- Amendments require updating this document and re-evaluating active implementation plans.

**Version**: 1.0.0 | **Ratified**: [DATE]
