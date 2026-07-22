# Reference: /sdd-baseline — Detailed Behavior

## Purpose

Reverse-engineer an existing codebase into complete SDD artifacts under `specs/000-baseline/`. This creates the **specification foundation** for brownfield projects and legacy modernization: it documents what exists so that subsequent specs (`001`, `002`, …) have a known starting point and can describe the *target state*.

**Use cases:**
- **Legacy modernization**: take over a codebase, generate full specs, then use SDD to drive the rewrite/modernization
- **Team onboarding**: new member runs `/sdd-baseline` and gets architecture docs, data model, and contracts in minutes
- **Pre-audit snapshot**: before a large refactor, freeze a spec of the current state
- **M&A / handover**: incoming team gets structured documentation of what they inherited

---

## Output Directory

```
specs/000-baseline/
├── spec.md              # Full specification: FRs, User Stories, Edge Cases, Success Criteria (inferred)
├── plan.md              # Current architecture documentation
├── research.md          # Technology decisions, rationale, alternatives (inferred)
├── data-model.md        # Entities, relationships, migrations, validation rules (extracted)
├── contracts/           # API endpoints, event types, public interfaces (if project has external surface)
└── quickstart.md        # How to build, configure, and run the project
```

> `000-baseline` always occupies the `000` slot regardless of other spec directories. If `000-baseline` already exists, the command appends a timestamp: `000-baseline-YYYYMMDD/`.

---

## Execution Protocol

The command runs in **3 sequential phases**. The agent **reads only**, never writes application code. All writes go into `specs/000-baseline/`.

### Phase 1: Reconnaissance (shallow scan — build the map)

Scan the project root without entering deep source trees. Collect:

| Artifact | What to extract |
|---|---|
| `package.json` / `pyproject.toml` / `Cargo.toml` / `go.mod` / `Gemfile` / `build.gradle` / `composer.json` | Project name, description, language, framework, critical dependencies with versions, scripts |
| `README.md` | Project purpose, setup instructions, badges |
| `Dockerfile` / `compose.yaml` / `docker-compose.yml` | Runtime environment, services, ports |
| `.env.example` / `config/` / `settings/` | Required env vars, configuration structure |
| `Makefile` / `Taskfile.yml` / `Justfile` | Common dev commands |
| `.github/workflows/` / `.gitlab-ci.yml` / `Jenkinsfile` | CI/CD pipeline, test commands, deployment targets |
| `migrations/` / `alembic/` / `prisma/` / `sequelize/` | Schema evolution history |
| Directory listing (non-recursive) at root | Top-level module structure |
| `docs/` (if exists) | Existing documentation to incorporate |

**Output**: internal agent summary of project identity, stack, and shape. No files written yet.

### Phase 2: Deep Analysis (the agent reads source code)

The agent now reads key source files to extract architecture, entities, interfaces, and patterns. **Prioritize breadth over depth** — first map all modules, then dive into each module's core files.

#### 2a. Entry Points & Application Structure

- `main.py`, `app.py`, `src/main.rs`, `cmd/`, `cli.py`, `bin/` — how the application starts
- `index.js`, `app.js`, `pages/`, `app/` (Next.js App Router) — web entry points
- Middleware chain, route registration, DI container setup
- Error handlers, global exception mappers

**Extract**: startup flow, middleware stack, error handling strategy.

#### 2b. API Surface & Controllers

- Route files, controllers, handlers, views, resolvers
- Router definitions with HTTP method + path + handler
- Decorators/annotations for auth, validation, caching

**Extract**: complete endpoint inventory with method, path, auth, and brief purpose.

#### 2c. Domain Model / Entities

- ORM models, database schemas, Pydantic models, TypeScript types, protobuf definitions
- Migrations history (the schema evolves over time — capture the latest state)
- Foreign keys, relations, indexes, unique constraints
- Validation rules embedded in models (e.g., `max_length`, `regex`, `@validate`)

**Extract**: entity list with fields, types, relations, and validation constraints.

#### 2d. Business Logic / Services

- Service classes, use cases, domain services, helpers
- Key algorithms, state machines, workflow orchestrations
- External API clients, SDK wrappers, adapters

**Extract**: major service boundaries, external integrations, notable business rules.

#### 2e. Testing Strategy

- Test directory structure (unit / integration / e2e / contract)
- Test framework, fixtures, factories, test helpers
- Coverage config (`pyproject.toml` → `[tool.coverage]`, `jest.config.js` → `collectCoverageFrom`)
- CI test commands

**Extract**: testing approach, coverage targets, what's tested vs. not.

#### 2f. Configuration & Cross-Cutting

- Feature flags, toggles, dark launch configs
- Logging setup, monitoring, telemetry
- AuthN/AuthZ strategy (JWT, sessions, OAuth, API keys, RBAC)
- Caching layer (Redis, Memcached, CDN)
- Queue / message broker (RabbitMQ, SQS, Kafka)
- File storage (S3, GCS, local)

**Extract**: cross-cutting patterns, infrastructure dependencies.

#### 2g. Dependency Tree (critical only)

- Production dependencies with versions
- Peer dependencies, platform requirements (Python version, Node version, DB version)
- Build tools, bundlers, transpilers

**Extract**: stack table with critical dependency → purpose mapping.

#### 2h. Git History (shallow)

- `git log --oneline -50` — recent activity, active areas
- `git log --format="%an" | sort | uniq -c | sort -rn` — team composition
- Branch naming convention, if observable

**Extract**: activity hotspots, team size.

---

### Phase 3: Artifact Generation

Write all artifacts under `specs/000-baseline/`. Every inference must be traceable.

#### 3a. `spec.md` — Baseline Specification

Use the **same structure** as a normal spec (`templates/spec-template.md`) but the content describes *what exists*, not what should be built.

```
# Feature Specification: 000 — Project Baseline

**Feature Branch**: `000-baseline`
**Created**: [DATE]
**Status**: Baseline (reverse-engineered)
**Input**: Existing codebase at commit [CURRENT_SHA]

## User Scenarios & Testing

### User Story 1 - [Core Flow] (Priority: P1)
[Describe the primary user journey that dominates the codebase]

**Why this priority**: This is the main purpose of the application — all other features support it.

**Independent Test**: [CI test command that validates this flow — e.g., `pytest tests/integration/test_core.py`]

**Acceptance Scenarios**:
1. **Given** [setup from existing code], **When** [action], **Then** [expected result — INFERRED FROM: path/to/file]
2. **Given** [setup from existing code], **When** [action], **Then** [expected result — INFERRED FROM: path/to/file]

---

### User Story 2 - [Secondary Flow] (Priority: P2)

[Describe secondary journey]

---

### User Story 3 - [Edge / Admin Flow] (Priority: P3)

[Describe admin or edge-case journey]

---

### Edge Cases (inferred from existing handlers)
- [Boundary condition] → handled in [file:line] via [mechanism]
- [Error scenario] → caught by [error handler at file:line]

## Requirements

### Functional Requirements

Each FR maps to a coherent feature cluster detected in the codebase.

- **FR-001**: [Feature cluster name — e.g., "User Authentication"]
  System MUST [what it does — INFERRED FROM: files A, B, C]
- **FR-002**: [Feature cluster name]
  System MUST [what it does — INFERRED FROM: files D, E]

Use `[INFERRED FROM: path/to/file]` instead of `[NEEDS CLARIFICATION]`. If the evidence is weak, use `[NEEDS VALIDATION: inferred from X — confirm with team]`.

### Key Entities
- **[Entity 1]**: [what it represents — INFERRED FROM: path/to/model.py]
  Fields: [field list with types]
  Relations: [related entities]
- **[Entity 2]**: [what it represents]

## Success Criteria (inferred)

- **SC-001**: [Performance target inferred from configs/caching patterns — INFERRED FROM: file]
- **SC-002**: [Availability pattern — retries, circuit breaker, replica count — INFERRED FROM: file]
- **SC-00N**: [Not specified in code — mark as "Not defined in current codebase"]

## Assumptions

- [Assumption about the domain made by the current implementation]
- [Known gap in the current implementation]
```

**Mark every inference** with `[INFERRED FROM: path]` so a human reviewer can validate. If the inference is speculative, use `[NEEDS VALIDATION: reason]` — the spec is a starting point, not gospel.

#### 3b. `plan.md` — Architecture Documentation

```
# Current Architecture: 000 — Project Baseline

**Branch**: `000-baseline` | **Date**: [DATE]
**Input**: Reverse-engineered from codebase at commit [SHA]

## Summary

[1-2 paragraph description of what the system does and its architecture style]

## Architecture Overview

### Language & Runtime
- **Language**: [e.g., Python 3.11, TypeScript 5.3, Rust 1.75]
- **Runtime**: [e.g., Node 20, CPython, Go 1.22]

### Primary Framework
- **Framework**: [e.g., FastAPI, Next.js 14, Actix-web] ([version])

### Storage
- **Primary DB**: [e.g., PostgreSQL 15, SQLite, MongoDB]
- **Cache**: [Redis / Memcached / None]
- **File Storage**: [S3 / GCS / local]

### Architecture Pattern
- **Pattern**: [Monolith / Modular monolith / Microservices / Serverless]
- **Key modules**: [list of top-level modules/components]

## Project Structure

```text
[root structure — inferred from actual directory tree]
```

## Component Map

| Component | Responsibility | Key Files |
|---|---|---|
| [component name] | [what it does] | [file paths] |
| ... | ... | ... |

## Data Flow

[Description of the main data flow through the system — narrative with key entry points and handlers]

## Deployment

- **Container**: [Docker / serverless / bare metal]
- **CI/CD**: [GitHub Actions / GitLab CI / Jenkins]
- **Target**: [cloud provider / on-prem / hybrid]

## Key Dependencies

| Dependency | Version | Purpose |
|---|---|---|
| [pkg] | [ver] | [why it's used] |
```

#### 3c. `research.md` — Technology Decisions

Document **why** each technology was likely chosen (inferred from ecosystem, blog posts in code comments, commit messages).

```
## Decision: [Technology Name]
- **Rationale**: [inferred reason — e.g., "Framework choice inferred from ecosystem: project uses X, which pairs naturally with Y"]
- **Alternatives considered**: [what would also be reasonable — INFERRED FROM: domain requirements]
- **Evidence**: [commit message, comment, ecosystem fit]

## Decision: [Architecture Pattern]
- **Rationale**: [inferred from module boundaries, deployment configs]
- **Evidence**: [file:line that reveals the pattern]
```

#### 3d. `data-model.md` — Entities & Schema

Extracted from ORM models, type definitions, protobuf schemas, or migrations.

```
# Data Model: 000 — Project Baseline

## Entity: [EntityName]

| Field | Type | Constraints | Description |
|---|---|---|---|
| [field] | [type] | [required, unique, max_length] | [inferred purpose] |

**Relationships**:
- Belongs to [Entity2] via [foreign_key]
- Has many [Entity3] via [foreign_key]

**Validation Rules**:
- [rule — INFERRED FROM: file:line]

---

## Entity: [EntityName2]
...
```

#### 3e. `contracts/` — API & Interface Contracts

Create ONLY if the project has an external interface (web service, library, CLI tool).

```
contracts/
├── api-rest.md         # HTTP endpoints (method, path, params, response shape)
├── events.md           # Published/subscribed events (if event-driven)
├── cli-commands.md     # CLI command schema (if CLI tool)
└── public-api.md       # Library public API surface (if library)
```

**REST API contract example:**

```
## GET /api/users/{id}

**Auth**: Required (Bearer token — INFERRED FROM: middleware/ path)
**Query**: none
**Response 200**:
```json
{
  "id": "string",
  "email": "string",
  "name": "string",
  "created_at": "datetime"
}
```
**Response 404**: `{ "error": "User not found" }`

**INFERRED FROM**: `src/api/users.py:42-58`, `src/models/user.py`
```

#### 3f. `quickstart.md` — How to Run

Extracted from `README.md`, `Makefile`, Docker config, and scripts.

```
# Quickstart: 000 — Project Baseline

## Prerequisites
- [Language runtime and version — INFERRED FROM: .nvmrc, .python-version, Dockerfile]
- [Database — INFERRED FROM: compose.yaml]
- [Other services]

## Setup
```bash
# Commands inferred from Makefile / README / scripts
[setup commands]
```

## Configuration
[Required env vars — INFERRED FROM: .env.example, config files]

## Run
```bash
[run commands — INFERRED FROM: package.json scripts, Makefile, Dockerfile]
```

## Test
```bash
[test commands — INFERRED FROM: CI config, package.json scripts]
```
```

---

## Inference Rules

The agent must follow these rules when inferring intent from code:

| If you find… | Infer… | Tag as… |
|---|---|---|
| Auth middleware, JWT utils, login route | FR: User Authentication | `[INFERRED FROM: files]` |
| CRUD routes for an entity | User Story: Manage [Entity] | `[INFERRED FROM: files]` |
| Error handler, exception class | Edge Case: [error scenario] | `[INFERRED FROM: file:line]` |
| Cache config, Redis client | SC: Performance target (cached reads) | `[INFERRED FROM: file]` |
| Migration with added column | Entity field evolution | `[INFERRED FROM: migration file]` |
| TODO / FIXME / HACK comment | Known debt area | `[DEBT: file:line — description]` |
| Test file for module X | Module X is important enough to test | Used in P1/P2 priority assignment |
| No tests for module Y | Module Y may be untested or new | `[UNTESTED: file]` |
| Retry decorator, circuit breaker | SC: Resilience requirement | `[INFERRED FROM: file]` |
| env var for external URL | External integration | Listed in dependencies |

---

## `[INFERRED FROM]` vs `[NEEDS CLARIFICATION]` vs `[NEEDS VALIDATION]`

| Tag | When to use |
|---|---|
| `[INFERRED FROM: path]` | High-confidence inference backed by clear code evidence |
| `[NEEDS VALIDATION: reason — INFERRED FROM: path]` | Moderate-confidence inference — the code suggests it but the intent is unclear |
| `[NEEDS CLARIFICATION: question]` | No evidence in code — the agent cannot determine the answer from the codebase alone |

Maximum **5** `[NEEDS CLARIFICATION]` or `[NEEDS VALIDATION]` markers across all generated artifacts. Present them to the user at the end.

---

## Completion Report

After finishing, report:

```
✅ Baseline complete: specs/000-baseline/

Artifacts generated:
  - spec.md            (## FRs, ## User Stories, ## Edge Cases, ## SC)
  - plan.md            (architecture, components, deployment)
  - research.md        (## decisions with rationale)
  - data-model.md      (## entities with fields and relations)
  - contracts/         (## API endpoints / interfaces)
  - quickstart.md      (setup, run, test commands)

Scanner stats:
  - Files scanned: ##
  - FRs inferred: ##
  - User Stories inferred: ## (P1: #, P2: #, P3: #)
  - Entities extracted: ##
  - Endpoints documented: ##
  - Dependencies catalogued: ##

Markers:
  - [INFERRED FROM]: ##
  - [NEEDS VALIDATION]: ##
  - [NEEDS CLARIFICATION]: ##

Review required: spec.md sections tagged with NEEDS VALIDATION / NEEDS CLARIFICATION
```
