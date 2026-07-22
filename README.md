# SDD Skill - Specification-Driven Development

A portable, universal **Skill** for AI Coding Assistants (**Claude Code**, **Antigravity IDE / CLI**, **OpenCode**, **Cursor**, **Codex**, **Gemini CLI**).

This skill brings **Specification-Driven Development (SDD)** directly to your AI agent without requiring complex CLI tool installations or heavy dependencies.

---

## 📁 What's Included

```text
SDD-Skill/
├── SKILL.md                          # Main Skill definition & agent instruction set
├── templates/                        # Ready-to-use SDD templates
│   ├── spec-template.md              # Feature specification template
│   ├── plan-template.md              # Technical implementation plan template
│   ├── tasks-template.md             # Task breakdown template
│   ├── constitution-template.md      # Project constitution template
│   └── checklist-template.md         # Quality checklist template
├── references/                       # Background knowledge & methodology guides
│   ├── sdd-principles.md             # Power Inversion & core principles
│   └── workflow-guide.md             # Complete workflow breakdown
├── scripts/                          # Cross-platform Python helper
│   └── sdd_helper.py                 # Zero-dependency feature & template manager
└── README.md                         # Quick installation & usage guide
```

---

## 🚀 Installation

### 0. npx
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

## 💡 Quick Start Workflow

Once installed, invoke SDD commands in your AI Coding Assistant:

```bash
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

# 7. Execute implementation step-by-step
/sdd-implement
```

---

## 🎯 Key Benefits

- **Zero External Dependencies**: Uses native Markdown templates and standard Python 3.
- **Power Inversion**: Specifications are executable source code blueprints, eliminating spec-code drift.
- **MVP Priority (P1/P2/P3)**: User Story 1 (P1) is always designed as an independent MVP slice.
- **Universal AI Agent Compatibility**: Works out-of-the-box in Claude, Antigravity, OpenCode, Cursor, and any Agent Skills-compliant system.
