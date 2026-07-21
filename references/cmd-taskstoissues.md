# Reference: /sdd-taskstoissues — Detailed Behavior

## Purpose

Converts tasks from `tasks.md` into GitHub Issues, one issue per task, with deduplication to avoid creating issues that already exist.

> [!NOTE]
> This command requires the **GitHub MCP server** to be available (`github/github-mcp-server` with `list_issues` and `issue_write` tools). If GitHub MCP is not configured, this command cannot run.

---

## Prerequisites

1. A `tasks.md` must exist in the active feature directory
2. The repository must have a GitHub remote URL (validated via `git config --get remote.origin.url`)

> [!CAUTION]
> ONLY proceed if the remote is a GitHub URL. UNDER NO CIRCUMSTANCES create issues in repositories that do not match the remote URL.

---

## Execution Steps

### 1. Extract Task IDs

Parse `tasks.md` for all task IDs (pattern: `T` followed by three digits, e.g., `T001`, `T002`). Strip leading `- [ ]`, `[P]`, and `[USx]` markers to recover the task ID and description.

### 2. Fetch Existing Issues (Deduplication)

Before creating anything, fetch existing issues from the GitHub repo:
- Use `list_issues` without a `state` filter (returns both open and closed)
- Request `perPage: 100`, paginate using `after` cursor
- For each issue title, match pattern `\bT\d{3}\b` (word boundaries to avoid false positives like `ST001` or `T0010`)
- Stop paginating as soon as all task IDs are accounted for
- Build a set of task IDs that already have issues

### 3. Create Issues

For each task that does NOT already have an issue:
- Create a single canonical title: `T001: <description>`
  - Example: `- [ ] T001 Create project structure` → title `T001: Create project structure`
- Skip tasks already in the existing-issues set and report: `T001 already has an issue, skipping`

### 4. Completion Report

Report:
- Total tasks processed
- Issues created (with links if available)
- Issues skipped (already existed)
- Any errors encountered
