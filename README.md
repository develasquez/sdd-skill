# SDD Skill - Specification-Driven Development

A portable, universal **Skill** for AI Coding Assistants (**Claude Code**, **Antigravity IDE / CLI**, **OpenCode**, **Cursor**, **Codex**, **Gemini CLI**).

This skill brings **Specification-Driven Development (SDD)** directly to your AI agent without requiring complex CLI tool installations or heavy dependencies.

---

## 📁 What's Included

```text
SDD-Skill/
├── SKILL.md                          # Main Skill definition & 10 SDD commands
├── templates/                        # Ready-to-use SDD templates
│   ├── spec-template.md              # Feature specification template
│   ├── plan-template.md              # Technical implementation plan template
│   ├── tasks-template.md             # Task breakdown template
│   ├── constitution-template.md      # Project constitution template
│   └── checklist-template.md         # Quality checklist template
├── references/                       # Deep-dive command references & methodology
│   ├── cmd-baseline.md               # /sdd-baseline — reverse-engineer existing codebase
│   ├── cmd-specify.md                # /sdd-specify — create feature specifications
│   ├── cmd-plan.md                   # /sdd-plan — technical architecture & contracts
│   ├── cmd-tasks.md                  # /sdd-tasks — prioritized task breakdown
│   ├── cmd-clarify.md                # /sdd-clarify — ambiguity resolution
│   ├── cmd-analyze.md                # /sdd-analyze — cross-artifact consistency
│   ├── cmd-checklist.md              # /sdd-checklist — domain quality gates
│   ├── cmd-implement.md              # /sdd-implement — sequential execution
│   ├── cmd-converge.md               # /sdd-converge — spec-code realignment
│   ├── sdd-principles.md             # Power Inversion & core SDD philosophy
│   └── workflow-guide.md             # Complete workflow diagram & descriptions
├── scripts/                          # Cross-platform Python helper
│   └── sdd_helper.py                 # Zero-dependency feature & template manager
└── README.md                         # Quick installation & usage guide
```

---

## 🚀 Installation

### npx (recommended)

```sh
npx skills add https://github.com/develasquez/sdd-skill
```

### 1. Google Antigravity (AGY)
Copy or symlink `SDD-Skill` into your skills directory:
- **Project level**: `<project-root>/.gemini/skills/sdd-skill/` or `.agents/skills/sdd-skill/`
- **Global level**: `~/.gemini/skills/sdd-skill/`

### 2. Claude Code
Copy or symlink `SDD-Skill` into your Claude skills directory:
- **Project level**: `<project-root>/.claude/skills/sdd-skill/`
- **Global level**: `~/.claude/skills/sdd-skill/`

### 3. OpenCode / Codex / AI Agents
Copy or symlink `SDD-Skill` into your workspace skills folder:
- `.agents/skills/sdd-skill/`

---

## 💡 Workflow

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
               │       sdd-tasks       │  (Task breakdown by User Story P1/P2/P3…)
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
               │     sdd-implement     │  (Sequential execution)
               └───────────┬───────────┘
                           │
                           ▼
               ┌───────────────────────┐
               │      sdd-converge     │  (Re-align spec & code if diverged)
               └───────────────────────┘
```

Once installed, invoke SDD commands in your AI Coding Assistant:

```bash
# 0. Reverse-engineer existing codebase (brownfield projects)
/sdd-baseline

# 1. Establish project rules & constitution (optional)
/sdd-constitution

# 2. Create a new feature specification
/sdd-specify Real-time chat system with message history

# 3. Interactively clarify ambiguities
/sdd-clarify

# 4. Generate technical implementation plan & contracts
/sdd-plan FastAPI, PostgreSQL, WebSockets, Redis

# 5. Break plan into prioritized, actionable tasks
/sdd-tasks

# 6. Perform cross-artifact consistency check (read-only)
/sdd-analyze

# 7. Generate domain quality checklists
/sdd-checklist security

# 8. Execute implementation step-by-step
/sdd-implement

# 9. Detect drift between spec and codebase
/sdd-converge
```

---

## 🎯 Key Benefits

- **Zero External Dependencies**: Uses native Markdown templates and standard Python 3.
- **Power Inversion**: Specifications are executable source code blueprints, eliminating spec-code drift.
- **MVP Priority (P1/P2/P3…)**: User Story 1 (P1) is always designed as an independent MVP slice.
- **Brownfield Ready**: `/sdd-baseline` reverse-engineers existing code into full SDD artifacts.
- **Universal AI Agent Compatibility**: Works out-of-the-box in Claude, Antigravity, OpenCode, Cursor, and any Agent Skills-compliant system.
