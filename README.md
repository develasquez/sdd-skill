# SDD Skill - Specification-Driven Development

A portable, universal **Skill** for AI Coding Assistants (**Claude Code**, **Antigravity IDE / CLI**, **OpenCode**, **Cursor**, **Codex**, **Gemini CLI**).

This skill brings **Specification-Driven Development (SDD)** directly to your AI agent without requiring complex CLI tool installations or heavy dependencies. Under SDD, specifications and technical plans are the primary, executable source of truth — code is a continuously generated expression of the specification.

---

## 📁 What's Included

```text
SDD-Skill/
├── SKILL.md                              # Main Skill definition & agent instruction set
├── templates/                            # Ready-to-use SDD templates
│   ├── spec-template.md                  # Feature specification template
│   ├── plan-template.md                  # Technical implementation plan template
│   ├── tasks-template.md                 # Task breakdown template
│   ├── constitution-template.md          # Project constitution template
│   └── checklist-template.md             # Quality checklist template
├── references/                           # Deep-dive command references & methodology
│   ├── sdd-principles.md                 # Power Inversion & core principles
│   ├── workflow-guide.md                 # Complete workflow breakdown
│   ├── cmd-specify.md                    # Feature creation & naming algorithm
│   ├── cmd-clarify.md                    # 9-category ambiguity resolution
│   ├── cmd-plan.md                       # Architecture, research & contracts
│   ├── cmd-tasks.md                      # Task breakdown format & rules
│   ├── cmd-analyze.md                    # 6-pass cross-artifact consistency check
│   ├── cmd-checklist.md                  # Domain quality checklist generation
│   ├── cmd-implement.md                  # Task execution & checklist gates
│   ├── cmd-converge.md                   # Codebase drift detection & convergence
│   └── cmd-taskstoissues.md              # GitHub Issues export
├── scripts/                              # Cross-platform Python helper
│   └── sdd_helper.py                     # Zero-dependency feature & template manager
└── README.md                             # Quick installation & usage guide
```

---

## 🚀 Installation

### npx (recommended)
```sh
npx skills add https://github.com/develasquez/sdd-skill
```

### Google Antigravity (AGY)
Copy or symlink into your skills directory:
- **Project level**: `<project-root>/.gemini/skills/sdd-skill/` or `.agents/skills/sdd-skill/`
- **Global level**: `~/.gemini/skills/sdd-skill/`

### Claude Code
Copy or symlink into your Claude skills directory:
- **Project level**: `<project-root>/.claude/skills/sdd-skill/`
- **Global level**: `~/.claude/skills/sdd-skill/`

### OpenCode / Cursor / Codex
Copy or symlink into your workspace skills folder:
- `.agents/skills/sdd-skill/`

---

## 💡 Commands Reference

| Command | What it does | Key output |
|---|---|---|
| `/sdd-constitution` | Establish or update non-negotiable project governance rules (TDD, CLI-first, zero secrets, etc.) | `specs/constitution.md` |
| `/sdd-specify <description>` | Create a feature specification from a natural language description. Generates user stories (P1/P2/P3), functional requirements, success criteria, and auto-detects ambiguities | `specs/[NNN-feature]/spec.md` + `checklists/requirements.md` |
| `/sdd-clarify` | Interactively resolve ambiguities in the specification using a 9-category taxonomy. Asks one targeted question at a time (max 5) | Updated `spec.md` with clarifications |
| `/sdd-plan <tech stack>` | Produce technical architecture, data model, research decisions, API contracts, and a runnable quickstart guide. Checks constitution gates first | `plan.md`, `research.md`, `data-model.md`, `contracts/`, `quickstart.md` |
| `/sdd-tasks` | Break down the plan into prioritized, actionable tasks grouped by phase (Setup → Foundational → User Stories → Polish) | `tasks.md` with task IDs, priority, and US labels |
| `/sdd-analyze` | Read-only cross-artifact consistency check across 6 categories (duplication, ambiguity, underspecification, constitution alignment, coverage gaps, inconsistency) | Structured report with CRITICAL→LOW severity |
| `/sdd-checklist <type>` | Generate domain-specific quality checklists ("Unit Tests for English") to validate specification quality before implementation | `checklists/[type].md` (append-only, max 40 items) |
| `/sdd-implement` | Execute tasks sequentially, auto-creates ignore files, gates on checklists, pauses at user story checkpoints | Working code + updated `tasks.md` |
| `/sdd-converge` | After implementation, assess codebase against spec/plan/tasks and append any missing work to `tasks.md` (never modifies specs or code) | `tasks.md` with appended convergence phase |
| `/sdd-taskstoissues` | Export `tasks.md` tasks to GitHub Issues (requires GitHub MCP server) | GitHub Issues with `T###:` prefix titles |

---

## 🎯 Key Benefits

- **Zero External Dependencies**: Uses native Markdown templates and standard Python 3.
- **Power Inversion**: Specifications are executable source code blueprints, eliminating spec-code drift.
- **MVP Priority (P1/P2/P3)**: User Story 1 (P1) is always designed as an independent MVP slice.
- **Universal AI Agent Compatibility**: Works out-of-the-box in Claude, Antigravity, OpenCode, Cursor, and any Agent Skills-compliant system.
