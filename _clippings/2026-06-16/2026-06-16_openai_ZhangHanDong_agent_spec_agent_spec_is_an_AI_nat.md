---
title: "2026-06-16_github_com_ZhangHanDong_agent_spec_agent_spec_is_an_AI_native"
source: "https://github.com/ZhangHanDong/agent-spec"
author:
  - "[[@openai]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "#14"
  - "#15"
  - "github"
  - "@openai"
---

# ZhangHanDong/agent-spec: `agent-spec` is an AI-native BDD/spec verification tool for task execution.

[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](/codespaces/new/ZhangHanDong/agent-spec?resume=1)

| Name | Name | 
Last commit message

 | 

Last commit date

 |
| --- | --- | --- | --- |
| 

and

[chore: update Cargo.lock for v0.2.7](/ZhangHanDong/agent-spec/commit/6479b16843ca5c6c12c54f5ad6786ce877037e1a)

[6479b16](/ZhangHanDong/agent-spec/commit/6479b16843ca5c6c12c54f5ad6786ce877037e1a) ·

[27 Commits](/ZhangHanDong/agent-spec/commits/main/)

 |
| 

[.claude/ skills](/ZhangHanDong/agent-spec/tree/main/.claude/skills "This path skips through empty directories")

 | 

[.claude/ skills](/ZhangHanDong/agent-spec/tree/main/.claude/skills "This path skips through empty directories")

 | 

[feat: add flag-combination-coverage + platform-decision-tag linters, …](/ZhangHanDong/agent-spec/commit/537b9abafe951a5deec8877d8d7ab3e1a38fe414 "feat: add flag-combination-coverage + platform-decision-tag linters, rewrite-parity template, clippy CI fix
New linters (#14, #15):
- flag-combination-coverage: warns when 2+ output-affecting flags lack combo scenarios
- platform-decision-tag: flags untagged platform-specific terms in decisions
CLI:
- `agent-spec init --template rewrite-parity` generates parity-aware task contracts
with behavior matrix and verification metadata examples (en/zh/both)
CI:
- clippy now uses --all-targets --all-features in both workflows
- contract-guard-minimal.yml adds fmt + clippy + test steps
- test modules get targeted #[allow] for unwrap/expect (clippy clean on --all-targets)
Formatting:
- cargo fmt applied to all files (fixes CI fmt check failures)
Skills:
- authoring checklist expanded with Flag Combinations, Platform-Specific, Architectural Invariants
- tool-first catches list updated to 20 linters
- proposal status table updated (rewrite-parity template: Done)
Co-Authored-By: Codex <noreply@openai.com>
Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")

 |  |
| 

[.github/ workflows](/ZhangHanDong/agent-spec/tree/main/.github/workflows "This path skips through empty directories")

 | 

[.github/ workflows](/ZhangHanDong/agent-spec/tree/main/.github/workflows "This path skips through empty directories")

 | 

[feat: add flag-combination-coverage + platform-decision-tag linters, …](/ZhangHanDong/agent-spec/commit/537b9abafe951a5deec8877d8d7ab3e1a38fe414 "feat: add flag-combination-coverage + platform-decision-tag linters, rewrite-parity template, clippy CI fix
New linters (#14, #15):
- flag-combination-coverage: warns when 2+ output-affecting flags lack combo scenarios
- platform-decision-tag: flags untagged platform-specific terms in decisions
CLI:
- `agent-spec init --template rewrite-parity` generates parity-aware task contracts
with behavior matrix and verification metadata examples (en/zh/both)
CI:
- clippy now uses --all-targets --all-features in both workflows
- contract-guard-minimal.yml adds fmt + clippy + test steps
- test modules get targeted #[allow] for unwrap/expect (clippy clean on --all-targets)
Formatting:
- cargo fmt applied to all files (fixes CI fmt check failures)
Skills:
- authoring checklist expanded with Flag Combinations, Platform-Specific, Architectural Invariants
- tool-first catches list updated to 20 linters
- proposal status table updated (rewrite-parity template: Done)
Co-Authored-By: Codex <noreply@openai.com>
Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")

 |  |
| 

[docs](/ZhangHanDong/agent-spec/tree/main/docs "docs")

 | 

[docs](/ZhangHanDong/agent-spec/tree/main/docs "docs")

 | 

[feat: add flag-combination-coverage + platform-decision-tag linters, …](/ZhangHanDong/agent-spec/commit/537b9abafe951a5deec8877d8d7ab3e1a38fe414 "feat: add flag-combination-coverage + platform-decision-tag linters, rewrite-parity template, clippy CI fix
New linters (#14, #15):
- flag-combination-coverage: warns when 2+ output-affecting flags lack combo scenarios
- platform-decision-tag: flags untagged platform-specific terms in decisions
CLI:
- `agent-spec init --template rewrite-parity` generates parity-aware task contracts
with behavior matrix and verification metadata examples (en/zh/both)
CI:
- clippy now uses --all-targets --all-features in both workflows
- contract-guard-minimal.yml adds fmt + clippy + test steps
- test modules get targeted #[allow] for unwrap/expect (clippy clean on --all-targets)
Formatting:
- cargo fmt applied to all files (fixes CI fmt check failures)
Skills:
- authoring checklist expanded with Flag Combinations, Platform-Specific, Architectural Invariants
- tool-first catches list updated to 20 linters
- proposal status table updated (rewrite-parity template: Done)
Co-Authored-By: Codex <noreply@openai.com>
Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")

 |  |
| 

[examples](/ZhangHanDong/agent-spec/tree/main/examples "examples")

 | 

[examples](/ZhangHanDong/agent-spec/tree/main/examples "examples")

 | 

[feat: add behavior completeness linters, verification metadata, and r…](/ZhangHanDong/agent-spec/commit/19b69b90a0e41dc0290c9e1f85e1daedbed4562c "feat: add behavior completeness linters, verification metadata, and rewrite/parity guidance
Three areas of improvement:
1. Behavior completeness linters (5 new, 18 total):
- observable-decision-coverage: warns when behavioral decisions lack scenarios
- output-mode-coverage: warns when multiple output modes are uncovered
- precedence-fallback-coverage: warns when ordered behavior has no scenario
- external-io-error-strength: warns on weak mock-only I/O error scenarios
- verification-metadata-suggestion: suggests Level/TestDouble/Targets metadata
2. Scenario verification metadata:
- TestSelector now supports Level/Test Double/Targets (层级/替身/命中)
- Parser, AST, JSON, contract rendering, and Evidence all preserve metadata
- Fully backward compatible — all fields optional
3. Rewrite/parity authoring guidance:
- Behavior Surface Checklist in authoring skill
- Unbound Observable Behavior review step in tool-first skill
- New example: rewrite-parity-contract.spec
- Improvement proposal: behavior-contract-improvement-proposal.md
- 2 task specs moved to roadmap (incomplete test bindings)
Co-Authored-By: Codex <noreply@openai.com>
Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")

 |  |
| 

[skills](/ZhangHanDong/agent-spec/tree/main/skills "skills")

 | 

[skills](/ZhangHanDong/agent-spec/tree/main/skills "skills")

 | 

[feat: add flag-combination-coverage + platform-decision-tag linters, …](/ZhangHanDong/agent-spec/commit/537b9abafe951a5deec8877d8d7ab3e1a38fe414 "feat: add flag-combination-coverage + platform-decision-tag linters, rewrite-parity template, clippy CI fix
New linters (#14, #15):
- flag-combination-coverage: warns when 2+ output-affecting flags lack combo scenarios
- platform-decision-tag: flags untagged platform-specific terms in decisions
CLI:
- `agent-spec init --template rewrite-parity` generates parity-aware task contracts
with behavior matrix and verification metadata examples (en/zh/both)
CI:
- clippy now uses --all-targets --all-features in both workflows
- contract-guard-minimal.yml adds fmt + clippy + test steps
- test modules get targeted #[allow] for unwrap/expect (clippy clean on --all-targets)
Formatting:
- cargo fmt applied to all files (fixes CI fmt check failures)
Skills:
- authoring checklist expanded with Flag Combinations, Platform-Specific, Architectural Invariants
- tool-first catches list updated to 20 linters
- proposal status table updated (rewrite-parity template: Done)
Co-Authored-By: Codex <noreply@openai.com>
Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")

 |  |
| 

[specs](/ZhangHanDong/agent-spec/tree/main/specs "specs")

 | 

[specs](/ZhangHanDong/agent-spec/tree/main/specs "specs")

 | 

[feat: add behavior completeness linters, verification metadata, and r…](/ZhangHanDong/agent-spec/commit/19b69b90a0e41dc0290c9e1f85e1daedbed4562c "feat: add behavior completeness linters, verification metadata, and rewrite/parity guidance
Three areas of improvement:
1. Behavior completeness linters (5 new, 18 total):
- observable-decision-coverage: warns when behavioral decisions lack scenarios
- output-mode-coverage: warns when multiple output modes are uncovered
- precedence-fallback-coverage: warns when ordered behavior has no scenario
- external-io-error-strength: warns on weak mock-only I/O error scenarios
- verification-metadata-suggestion: suggests Level/TestDouble/Targets metadata
2. Scenario verification metadata:
- TestSelector now supports Level/Test Double/Targets (层级/替身/命中)
- Parser, AST, JSON, contract rendering, and Evidence all preserve metadata
- Fully backward compatible — all fields optional
3. Rewrite/parity authoring guidance:
- Behavior Surface Checklist in authoring skill
- Unbound Observable Behavior review step in tool-first skill
- New example: rewrite-parity-contract.spec
- Improvement proposal: behavior-contract-improvement-proposal.md
- 2 task specs moved to roadmap (incomplete test bindings)
Co-Authored-By: Codex <noreply@openai.com>
Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")

 |  |
| 

[src](/ZhangHanDong/agent-spec/tree/main/src "src")

 | 

[src](/ZhangHanDong/agent-spec/tree/main/src "src")

 | 

[feat: add flag-combination-coverage + platform-decision-tag linters, …](/ZhangHanDong/agent-spec/commit/537b9abafe951a5deec8877d8d7ab3e1a38fe414 "feat: add flag-combination-coverage + platform-decision-tag linters, rewrite-parity template, clippy CI fix
New linters (#14, #15):
- flag-combination-coverage: warns when 2+ output-affecting flags lack combo scenarios
- platform-decision-tag: flags untagged platform-specific terms in decisions
CLI:
- `agent-spec init --template rewrite-parity` generates parity-aware task contracts
with behavior matrix and verification metadata examples (en/zh/both)
CI:
- clippy now uses --all-targets --all-features in both workflows
- contract-guard-minimal.yml adds fmt + clippy + test steps
- test modules get targeted #[allow] for unwrap/expect (clippy clean on --all-targets)
Formatting:
- cargo fmt applied to all files (fixes CI fmt check failures)
Skills:
- authoring checklist expanded with Flag Combinations, Platform-Specific, Architectural Invariants
- tool-first catches list updated to 20 linters
- proposal status table updated (rewrite-parity template: Done)
Co-Authored-By: Codex <noreply@openai.com>
Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")

 |  |
| 

[.aider.conf.yml](/ZhangHanDong/agent-spec/blob/main/.aider.conf.yml ".aider.conf.yml")

 | 

[.aider.conf.yml](/ZhangHanDong/agent-spec/blob/main/.aider.conf.yml ".aider.conf.yml")

 | 

[v0.2.0: explain/stamp, jj VCS, caller-mode AI, Skills v3.1](/ZhangHanDong/agent-spec/commit/d33a021c38c6df149165aeefccd25916e06072fd "v0.2.0: explain/stamp, jj VCS, caller-mode AI, Skills v3.1
Features:
- explain command: human-readable contract review summary for Contract Acceptance
- stamp command: git trailer preview (Spec-Name, Spec-Passing, Spec-Summary)
- jj VCS integration: --change-scope jj, VcsContext, Spec-Change trailer,
jj diff between runs in explain --history
- Caller-mode AI verification: --ai-mode caller emits AiRequest JSON,
resolve-ai command merges external AiDecision back into report
- Skills v3.1: retry protocol, VCS awareness, bidirectional escalation,
caller mode documentation
Fixes:
- Run log path consistency (write and read both use .agent-spec/runs/)
- refund.spec lint smell (vague qualifier → quantified constraint)
Documentation:
- README: complete commands list, jj scope, explain/stamp workflow steps,
caller mode AI docs
- AGENTS.md/.cursorrules/.aider.conf.yml: retry protocol, verdict semantics
- Project website (docs/index.html)
- commands.md: resolve-ai reference
118 tests pass across 7 crates, 0 warnings.
Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")

 |  |
| 

[.cursorrules](/ZhangHanDong/agent-spec/blob/main/.cursorrules ".cursorrules")

 | 

[.cursorrules](/ZhangHanDong/agent-spec/blob/main/.cursorrules ".cursorrules")

 | 

[v0.2.0: explain/stamp, jj VCS, caller-mode AI, Skills v3.1](/ZhangHanDong/agent-spec/commit/d33a021c38c6df149165aeefccd25916e06072fd "v0.2.0: explain/stamp, jj VCS, caller-mode AI, Skills v3.1
Features:
- explain command: human-readable contract review summary for Contract Acceptance
- stamp command: git trailer preview (Spec-Name, Spec-Passing, Spec-Summary)
- jj VCS integration: --change-scope jj, VcsContext, Spec-Change trailer,
jj diff between runs in explain --history
- Caller-mode AI verification: --ai-mode caller emits AiRequest JSON,
resolve-ai command merges external AiDecision back into report
- Skills v3.1: retry protocol, VCS awareness, bidirectional escalation,
caller mode documentation
Fixes:
- Run log path consistency (write and read both use .agent-spec/runs/)
- refund.spec lint smell (vague qualifier → quantified constraint)
Documentation:
- README: complete commands list, jj scope, explain/stamp workflow steps,
caller mode AI docs
- AGENTS.md/.cursorrules/.aider.conf.yml: retry protocol, verdict semantics
- Project website (docs/index.html)
- commands.md: resolve-ai reference
118 tests pass across 7 crates, 0 warnings.
Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")

 |  |
| 

[.gitignore](/ZhangHanDong/agent-spec/blob/main/.gitignore ".gitignore")

 | 

[.gitignore](/ZhangHanDong/agent-spec/blob/main/.gitignore ".gitignore")

 | 

[v0.2.0: explain/stamp, jj VCS, caller-mode AI, Skills v3.1](/ZhangHanDong/agent-spec/commit/d33a021c38c6df149165aeefccd25916e06072fd "v0.2.0: explain/stamp, jj VCS, caller-mode AI, Skills v3.1
Features:
- explain command: human-readable contract review summary for Contract Acceptance
- stamp command: git trailer preview (Spec-Name, Spec-Passing, Spec-Summary)
- jj VCS integration: --change-scope jj, VcsContext, Spec-Change trailer,
jj diff between runs in explain --history
- Caller-mode AI verification: --ai-mode caller emits AiRequest JSON,
resolve-ai command merges external AiDecision back into report
- Skills v3.1: retry protocol, VCS awareness, bidirectional escalation,
caller mode documentation
Fixes:
- Run log path consistency (write and read both use .agent-spec/runs/)
- refund.spec lint smell (vague qualifier → quantified constraint)
Documentation:
- README: complete commands list, jj scope, explain/stamp workflow steps,
caller mode AI docs
- AGENTS.md/.cursorrules/.aider.conf.yml: retry protocol, verdict semantics
- Project website (docs/index.html)
- commands.md: resolve-ai reference
118 tests pass across 7 crates, 0 warnings.
Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")

 |  |
|  |

## agent-spec

`agent-spec` is an AI-native BDD/spec verification tool for task execution.

The core idea is simple:

- humans review the contract
- agents implement against the contract
- the machine verifies whether the code satisfies the contract

The primary planning surface is the **Task Contract**. The older `brief` view remains available as a compatibility alias, but new workflows should use `contract`.

## Task Contract

A task contract is a structured spec with four core parts:

- `Intent`: what to do, and why
- `Decisions`: technical choices that are already fixed
- `Boundaries`: what may change, and what must not change
- `Completion Criteria`: BDD scenarios that define deterministic pass/fail behavior

The DSL supports English and Chinese headings and step keywords.

## Example

```
spec: task
name: "User Registration API"
tags: [api, contract]
---

## Intent

Implement a deterministic user registration API contract that an agent can code against
and a verifier can check with explicit test selectors.

## Decisions

- Use `POST /api/v1/users/register` as the only public entrypoint
- Persist a new user only after password hashing succeeds

## Boundaries

### Allowed Changes
- crates/api/**
- tests/integration/register_api.rs

### Forbidden
- Do not change the existing login endpoint contract
- Do not create a session during registration

## Completion Criteria

Scenario: Successful registration
  Test: test_register_api_returns_201_for_new_user
  Given no user with email "alice@example.com" exists
  When client submits the registration request:
 | field | value |
 | email | alice@example.com |
 | password | Str0ng!Pass#2026  |
  Then response status should be 201
  And response body should contain "user_id"
```

Chinese authoring is also supported:

```
## 意图
## 已定决策
## 边界
## 完成条件

场景: 全额退款保持现有返回结构
  测试: test_refund_service_keeps_existing_success_payload
  假设 存在一笔金额为 "100.00" 元的已完成交易 "TXN-001"
  当 用户对 "TXN-001" 发起全额退款
  那么 响应状态码为 202
```

## Workflow

Start from a template:

```
cargo run -q --bin agent-spec -- init --level task --lang en --name "User Registration API"
```

For rewrite/parity tasks, start from the parity-aware task template:

```
cargo run -q --bin agent-spec -- init --level task --template rewrite-parity --lang en --name "CLI Parity Contract"
```

Or study the examples in [`examples/`](/ZhangHanDong/agent-spec/blob/main/examples).

This repo ships three agent skills under [`skills/`](/ZhangHanDong/agent-spec/blob/main/skills):

- **`agent-spec-tool-first`**: the default integration path — tells the agent to use `agent-spec` as a CLI tool and drive tasks through `contract`, `lifecycle`, and `guard`.
- **`agent-spec-authoring`**: the authoring path — helps write or revise Task Contracts in the DSL.
- **`agent-spec-estimate`**: the estimation path — maps Task Contract elements (scenarios, decisions, boundaries) to round-based effort estimates.

For rewrite/parity work, the authoring path should explicitly bind observable behavior before coding:

- command x output mode
- local x remote
- warm cache x cold start
- success x partial failure x hard failure

See [`examples/rewrite-parity-contract.spec`](/ZhangHanDong/agent-spec/blob/main/examples/rewrite-parity-contract.spec) for a concrete parity-oriented contract.

```
./install-skills.sh
```

This installs the `agent-spec` CLI via `cargo install` (if not already present) and copies all three skills to `~/.claude/skills/`.

```
# Copy to your global skills directory
cp -r skills/agent-spec-tool-first ~/.claude/skills/
cp -r skills/agent-spec-authoring ~/.claude/skills/
cp -r skills/agent-spec-estimate ~/.claude/skills/
```

Or symlink for auto-updates:

```
ln -s "$(pwd)/skills/agent-spec-tool-first" ~/.claude/skills/
ln -s "$(pwd)/skills/agent-spec-authoring" ~/.claude/skills/
ln -s "$(pwd)/skills/agent-spec-estimate" ~/.claude/skills/
```

The equivalent guidance for Codex lives in [`AGENTS.md`](/ZhangHanDong/agent-spec/blob/main/AGENTS.md). Copy it to your project root:

```
cp AGENTS.md /path/to/your/project/
```

Copy [`.cursorrules`](/ZhangHanDong/agent-spec/blob/main/.cursorrules) to your project root.

#### Workflow

1.  Use `agent-spec-tool-first` to inspect the target spec and render `agent-spec contract`.
2.  Implement code against the rendered Task Contract.
3.  Run `agent-spec lifecycle` for the task-level gate.
4.  Run `agent-spec guard` for repo-level validation when needed.

Before step 2, if the task is a rewrite, migration, or parity effort, use the tool-first workflow to review which observable behaviors are still unbound. If stdout/stderr, `--json`, `-o/--output`, local/remote, cache state, or fallback order are only described in prose, go back to authoring mode and add scenarios first.

This keeps the main integration mode tool-first. Library embedding remains available for advanced Rust-host integration, but it is not the default path.

```
cargo run -q --bin agent-spec -- contract specs/my-task.spec
```

Use `--format json` if another tool or agent runtime needs structured output.

```
cargo run -q --bin agent-spec -- lifecycle specs/my-task.spec --code . --format json
```

`lifecycle` runs:

- lint
- verification
- reporting

The run fails if:

- lint emits an `error`
- any scenario fails
- any scenario is still `skip` or `uncertain`
- the quality score is below `--min-score`

```
cargo run -q --bin agent-spec -- guard --spec-dir specs --code .
```

`guard` is intended for pre-commit / CI use. It lints all specs in `specs/` and verifies them against the current change set.

```
cargo run -q --bin agent-spec -- explain specs/my-task.spec --code . --format markdown
```

`explain` renders a reviewer-friendly summary of the Contract + verification results. Use `--format markdown` for direct PR description paste. Use `--history` to include retry trajectory from run logs.

The reviewer judges two questions: (1) Is the Contract definition correct? (2) Did all verifications pass?

```
cargo run -q --bin agent-spec -- stamp specs/my-task.spec --code . --dry-run
```

Outputs git trailers (`Spec-Name`, `Spec-Passing`, `Spec-Summary`) for the commit message. Currently only `--dry-run` is supported.

Task-level scenarios should declare an explicit `Test:` / `测试:` selector.

If package scoping matters, use the structured selector block:

```
场景: 超限退款返回稳定错误码
  测试:
 包: refund-service
 过滤: test_refund_service_rejects_refund_exceeding_original_amount
```

This is the default quality rule for self-hosting and new task specs. The older `// @spec:` source annotation is still accepted as a compatibility fallback, but it should not be the primary authoring path.

`Boundaries` can contain both natural-language constraints and path constraints. Path-like entries are mechanically enforced against a change set.

Examples:

```
## Boundaries

### Allowed Changes
- crates/spec-parser/**
- crates/spec-gateway/src/lifecycle.rs

### Forbidden
- tests/golden/**
- docs/archive/**
```

The relevant commands accept repeatable `--change` flags:

```
cargo run -q --bin agent-spec -- verify specs/my-task.spec --code . --change crates/spec-parser/src/parser.rs
cargo run -q --bin agent-spec -- lifecycle specs/my-task.spec --code . --change crates/spec-parser/src/parser.rs
```

Single-task commands also support optional VCS-backed change discovery:

```
cargo run -q --bin agent-spec -- verify specs/my-task.spec --code . --change-scope staged
cargo run -q --bin agent-spec -- lifecycle specs/my-task.spec --code . --change-scope worktree
cargo run -q --bin agent-spec -- lifecycle specs/my-task.spec --code . --change-scope jj
```

Available scopes: `none` (default for verify/lifecycle), `staged`, `worktree`, `jj`.

When a `.jj/` directory is detected (even colocated with `.git/`), use `--change-scope jj` to discover changes via `jj diff --name-only`. The `stamp` command also outputs a `Spec-Change:` trailer with the jj change ID, and `explain --history` shows file-level diffs between adjacent runs via jj operation IDs.

`agent-spec` now includes a minimal AI verifier surface intended to make `uncertain` results explicit and inspectable before a real model backend is wired in.

The relevant commands accept:

```
cargo run -q --bin agent-spec -- verify specs/my-task.spec --code . --ai-mode stub
cargo run -q --bin agent-spec -- lifecycle specs/my-task.spec --code . --ai-mode stub
```

Available modes:

- `off`: default, preserves the current mechanical-verifier-only behavior
- `stub`: turns otherwise-uncovered scenarios into `uncertain` results with `AiAnalysis` evidence
- `caller`: the calling Agent acts as the AI verifier (two-step protocol)

`caller` mode enables the Agent running `agent-spec` to also serve as the AI verifier. When `lifecycle --ai-mode caller` finds skipped scenarios, it writes `AiRequest` objects to `.agent-spec/pending-ai-requests.json`. The Agent reads the requests, analyzes each scenario, writes `ScenarioAiDecision` JSON, then calls `resolve-ai --decisions <file>` to merge decisions back into the report.

`stub` mode does not claim success. It is only a scaffold for:

- explicit `uncertain` semantics
- structured AI evidence in reports
- future integration of a real model-backed verifier

Internally, the AI layer now uses a pluggable backend shape:

- `AiRequest`: structured verifier input
- `AiDecision`: structured verifier output
- `AiBackend`: provider abstraction used by `AiVerifier`
- `StubAiBackend`: built-in backend for deterministic local behavior

No real model provider is wired in yet. The current value is that the contract/reporting surface is now stable enough to add a real backend later without redesigning the verification pipeline.

Provider selection and configuration are intentionally out of scope for `agent-spec` itself. The intended embedding model is:

- the host agent owns provider/model/auth/timeout policy
- the host agent injects an `AiBackend` into `spec-gateway`
- `agent-spec` stays focused on contracts, evidence, and verification semantics

`guard` resolves change paths in this order:

1.  explicit `--change` arguments
2.  auto-detected git changes according to `--change-scope`, if the current workspace is inside a git repo
3.  an empty change set, if no git repo is available

`guard` defaults to `--change-scope staged`, which keeps pre-commit behavior stable.

If you want stronger boundary checks against the full current workspace, use:

```
cargo run -q --bin agent-spec -- guard --spec-dir specs --code . --change-scope worktree
```

`worktree` includes:

- staged files
- unstaged tracked changes
- untracked files

This makes `guard` practical for both pre-commit usage and broader local worktree validation without forcing users to enumerate changed files manually.

For consistency, `verify` and `lifecycle` use the same precedence when `--change-scope` is provided. The practical default is:

- `verify`: `none`
- `lifecycle`: `none`
- `guard`: `staged`

## Commands

- `parse`: parse `.spec` files and show the AST
- `lint`: analyze spec quality
- `verify`: verify code against a single spec
- `contract`: render the Task Contract view
- `lifecycle`: run lint + verify + report
- `guard`: lint all specs and verify them against the current change set
- `explain`: generate a human-readable contract review summary (for Contract Acceptance)
- `stamp`: preview git trailers for a verified contract (`--dry-run`)
- `resolve-ai`: merge external AI decisions into a verification report (caller mode)
- `checkpoint`: preview VCS-aware checkpoint status
- `install-hooks`: install git hooks for automatic checking
- `brief`: compatibility alias for `contract`
- `measure-determinism`: \[experimental\] measure contract verification variance

## Examples

See [`examples/`](/ZhangHanDong/agent-spec/blob/main/examples):

- [`examples/user-registration-contract.spec`](/ZhangHanDong/agent-spec/blob/main/examples/user-registration-contract.spec)
- [`examples/refactor-payment-service.spec`](/ZhangHanDong/agent-spec/blob/main/examples/refactor-payment-service.spec)
- [`examples/refund.spec`](/ZhangHanDong/agent-spec/blob/main/examples/refund.spec)
- [`examples/no-unwrap.spec`](/ZhangHanDong/agent-spec/blob/main/examples/no-unwrap.spec)

## Current Status

The current system is strongest when the contract can be checked by:

- explicit tests selected from `Completion Criteria`
- structural checks
- boundary checks against an explicit or staged change set

More advanced verifier layers can still be added, but the current model is already sufficient for self-hosting `agent-spec` with task contracts.

## Contributing

agent-spec is self-bootstrapping: the project uses itself to govern its own development. When you contribute, you follow the same Contract-driven workflow that agent-spec teaches.

Every change starts with a Task Contract. Before writing code, create a `.spec` file in `specs/` that defines what you're building — the intent, the technical decisions that are already fixed, the files you'll touch, and the BDD scenarios that define "done." Then implement against the Contract and verify with `lifecycle`.

```
# 1. Create a task contract for your change
agent-spec init --level task --lang en --name "my-feature"
# Edit the generated spec: fill in Intent, Decisions, Boundaries, Completion Criteria

# 2. Check that the contract itself is well-written
agent-spec lint specs/my-feature.spec --min-score 0.7

# 3. Implement your change

# 4. Verify against the contract
agent-spec lifecycle specs/my-feature.spec --code . --change-scope worktree --format json

# 5. Run the repo-wide guard before committing
agent-spec guard --spec-dir specs --code .

# 6. Generate the PR description
agent-spec explain specs/my-feature.spec --code . --format markdown
```

The `guard` pre-commit hook is installed via `agent-spec install-hooks`. It checks all specs in `specs/` against your staged changes — your commit will be blocked if any contract fails.

### Project-level rules

The file `specs/project.spec` defines constraints that every task spec inherits. Read it before writing your first Contract — it tells you what the project enforces globally (e.g. "all public CLI behavior must have regression tests," "verification results must distinguish pass/fail/skip/uncertain").

### Roadmap specs

Future work lives in `specs/roadmap/`. These are real Task Contracts but they are not checked by the default `guard` run. When a roadmap spec is ready for implementation, promote it to the top-level `specs/` directory. See `specs/roadmap/README.md` for the promotion rule.

If you use Claude Code, Codex, Cursor, or another AI coding agent, install the skills from the [`skills/`](/ZhangHanDong/agent-spec/blob/main/skills) directory (see [AI Agent Skills](#ai-agent-skills) above).

The `agent-spec-tool-first` skill tells the agent to read the Contract first, implement within its Boundaries, run `lifecycle` to verify, and retry on failure without modifying the spec. The `agent-spec-authoring` skill helps the agent draft or revise Task Contracts in the DSL. The `agent-spec-estimate` skill maps Contract elements to round-based effort estimates for sprint planning.

For agents without skill support, the project includes `AGENTS.md` (Codex), `.cursorrules` (Cursor), and `.aider.conf.yml` (Aider) with the essential command reference.

Pull requests are evaluated through Contract Acceptance, not line-by-line code review. The reviewer checks two things: is the Contract definition correct (does it capture the right intent and edge cases), and did all verifications pass (lifecycle reports all-green). If both are yes, the PR is approved.

This means the quality of your Contract matters as much as the quality of your code. A well-written Contract with thorough exception-path scenarios is a stronger contribution than clever code with a thin spec.

## Releases

[8 tags](/ZhangHanDong/agent-spec/tags)

## Deployments 17

- [github-pages](/ZhangHanDong/agent-spec/deployments/github-pages)

[\+ 16 deployments](/ZhangHanDong/agent-spec/deployments)

## Packages

No packages published