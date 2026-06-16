---
title: "2026-06-16_github_com_actionbook_ascent_research_research_cli_for_agent"
source: "https://github.com/actionbook/ascent-research"
author:
  - "[[@anthropic]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "#8"
  - "#1"
  - "github"
  - "@anthropic"
---

# actionbook/ascent-research: research cli for agent

[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](/codespaces/new/actionbook/ascent-research?resume=1)

| Name | Name | 
Last commit message

 | 

Last commit date

 |
| --- | --- | --- | --- |
| 

[Merge pull request](/actionbook/ascent-research/commit/83ac6e3f45d6a51ac2e0663020fdd5755c434ffe) [#8](https://github.com/actionbook/ascent-research/pull/8) [from ZhangHanDong/feature/rebrand-to-ascent-res…](/actionbook/ascent-research/commit/83ac6e3f45d6a51ac2e0663020fdd5755c434ffe)

[83ac6e3](/actionbook/ascent-research/commit/83ac6e3f45d6a51ac2e0663020fdd5755c434ffe) ·

[106 Commits](/actionbook/ascent-research/commits/main/)

 |
| 

[.github/ workflows](/actionbook/ascent-research/tree/main/.github/workflows "This path skips through empty directories")

 | 

[.github/ workflows](/actionbook/ascent-research/tree/main/.github/workflows "This path skips through empty directories")

 | 

[fix: CI workflow + codex review P2 items for rebrand](/actionbook/ascent-research/commit/383af8c61fbb80b2dddf039d1fa2fb4fa1315e52 "fix: CI workflow + codex review P2 items for rebrand
Three follow-ups on PR #8:
1. CI was failing because .github/workflows/test.yml still used
`cargo build -p research` / `-p research --all-targets`. Updated
clippy / build / test steps to `-p ascent-research`. Verified
locally with RUSTFLAGS="-D warnings" cargo test -p ascent-research
--all-targets — clean.
2. Codex P2: `research_root()` on v0.2 upgraders was "sticky legacy"
— if `~/.actionbook/research/` existed and the new path didn't,
ALL writes went to legacy forever, defeating the rename. Split
read vs write:
- `research_root()` now always returns the canonical
`~/.actionbook/ascent-research/` (never falls back; writes go
here unconditionally).
- New `legacy_research_root()` exposes the v0.2 path for
read-only lookup.
- New `root_for_slug(slug)` returns canonical if the slug lives
there, otherwise legacy if it's present there, otherwise
canonical (for the create-new case).
- `session_dir(slug)` routes through `root_for_slug` so
resume/show/status find legacy sessions without the write
path being polluted.
Upgraders see: legacy sessions still resume; anything new lands
in the canonical path; the rename is effective from the first
v0.3 command.
3. Codex P2: `skills/ascent-research/SKILL.md` still documented
`research <sub>` / `~/.cargo/bin/research` commands, so a user
installing only the renamed skill would hit command-not-found.
Rewrote all 83 command invocations to `ascent-research <sub>`,
updated the RBIN example, title, and the mental-model path
reference. The "research CLI" noun label in the ASCII
control-flow diagram stays — it's a name, not a command.
Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>")

 |  |
| 

[docs](/actionbook/ascent-research/tree/main/docs "docs")

 | 

[docs](/actionbook/ascent-research/tree/main/docs "docs")

 | 

[docs: add three-tier architecture diagram](/actionbook/ascent-research/commit/f4f2743bb1b69c7d03d2b4cee4e1affbc293b3e4 "docs: add three-tier architecture diagram
Self-contained HTML file under docs/ rendering the CLI architecture
as a stone + rust editorial diagram: LLM orchestration tier (active-
research skill) on top, research CLI core (entry + route / fetch /
session modules + persistence store) in the middle, subprocess
adapters (postagent send, actionbook browser, json-ui render) on
the bottom. Coral accent reserved for the key edge (LLM → CLI) and
the focal CLI entry box; dashed "smell test" badge calls out the
infra-enforced post-fetch quality gate in the fetch module.
Useful for README / PR description / onboarding — self-contained,
open with any browser, no external fonts embedded beyond Google
Fonts.")

 |  |
| 

[packages/ research](/actionbook/ascent-research/tree/main/packages/research "This path skips through empty directories")

 | 

[packages/ research](/actionbook/ascent-research/tree/main/packages/research "This path skips through empty directories")

 | 

[fix: CI workflow + codex review P2 items for rebrand](/actionbook/ascent-research/commit/383af8c61fbb80b2dddf039d1fa2fb4fa1315e52 "fix: CI workflow + codex review P2 items for rebrand
Three follow-ups on PR #8:
1. CI was failing because .github/workflows/test.yml still used
`cargo build -p research` / `-p research --all-targets`. Updated
clippy / build / test steps to `-p ascent-research`. Verified
locally with RUSTFLAGS="-D warnings" cargo test -p ascent-research
--all-targets — clean.
2. Codex P2: `research_root()` on v0.2 upgraders was "sticky legacy"
— if `~/.actionbook/research/` existed and the new path didn't,
ALL writes went to legacy forever, defeating the rename. Split
read vs write:
- `research_root()` now always returns the canonical
`~/.actionbook/ascent-research/` (never falls back; writes go
here unconditionally).
- New `legacy_research_root()` exposes the v0.2 path for
read-only lookup.
- New `root_for_slug(slug)` returns canonical if the slug lives
there, otherwise legacy if it's present there, otherwise
canonical (for the create-new case).
- `session_dir(slug)` routes through `root_for_slug` so
resume/show/status find legacy sessions without the write
path being polluted.
Upgraders see: legacy sessions still resume; anything new lands
in the canonical path; the rename is effective from the first
v0.3 command.
3. Codex P2: `skills/ascent-research/SKILL.md` still documented
`research <sub>` / `~/.cargo/bin/research` commands, so a user
installing only the renamed skill would hit command-not-found.
Rewrote all 83 command invocations to `ascent-research <sub>`,
updated the RBIN example, title, and the mental-model path
reference. The "research CLI" noun label in the ASCII
control-flow diagram stays — it's a name, not a command.
Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>")

 |  |
| 

[presets](/actionbook/ascent-research/tree/main/presets "presets")

 | 

[presets](/actionbook/ascent-research/tree/main/presets "presets")

 | 

[\[packages/research\]feat: add GitHub incremental-source-reading rules](/actionbook/ascent-research/commit/8fc1ead1e949c3051114e0a70e7c10dcbea35082 "[packages/research]feat: add GitHub incremental-source-reading rules
Adds three rules to the tech preset for incremental source-code reading
via postagent + GitHub APIs:
- github-file  (github.com/{o}/{r}/blob/{ref}/{...path})
→ raw.githubusercontent.com/{o}/{r}/{ref}/{path}
(raw host bypasses GitHub's 60/hr anonymous rate limit)
- github-tree  (github.com/{o}/{r}/tree/{ref}/{...path})
→ api.github.com/repos/{o}/{r}/contents/{path}?ref={ref}
- github-raw (raw.githubusercontent.com/...) passthrough
Path matcher gains a variable-length segment `{...name}` that captures
all remaining path segments joined by `/`. Enforced to be the last
segment at load time (SCHEMA_INVALID otherwise). Matches 0+ trailing
segments so `tree/main` with no trailing path still routes.
9 new tests (6 unit, 3 integration) — full suite stays green (118/118).
Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>")

 |  |
| 

[scripts](/actionbook/ascent-research/tree/main/scripts "scripts")

 | 

[scripts](/actionbook/ascent-research/tree/main/scripts "scripts")

 | 

[fix(spec): swap Reddit out, Hacker News in, for API-First MVP](/actionbook/ascent-research/commit/bd6a2cad5bf6a4f37b6495c1d440c68288a7952b "fix(spec): swap Reddit out, Hacker News in, for API-First MVP
Reddit locked down anonymous .json endpoints in 2023 — unauthenticated
requests return HTTP 403 even with User-Agent or old.reddit.com. The
functional niche "anonymous public JSON discussion forum" is filled by
Hacker News Firebase API instead. Reddit moves to out-of-scope (Phase 2,
requires OAuth); Hacker News moves into MVP.
- Spec: rewrite intent, decisions, out-of-scope
- Rename: tests/recipe_reddit_anonymous.sh -> tests/recipe_hackernews_anonymous.sh
- Script: assert_out_of_scope_markers.sh now checks for Reddit (not HN)
Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>")

 |  |
| 

[skills/ ascent-research](/actionbook/ascent-research/tree/main/skills/ascent-research "This path skips through empty directories")

 | 

[skills/ ascent-research](/actionbook/ascent-research/tree/main/skills/ascent-research "This path skips through empty directories")

 | 

[fix: CI workflow + codex review P2 items for rebrand](/actionbook/ascent-research/commit/383af8c61fbb80b2dddf039d1fa2fb4fa1315e52 "fix: CI workflow + codex review P2 items for rebrand
Three follow-ups on PR #8:
1. CI was failing because .github/workflows/test.yml still used
`cargo build -p research` / `-p research --all-targets`. Updated
clippy / build / test steps to `-p ascent-research`. Verified
locally with RUSTFLAGS="-D warnings" cargo test -p ascent-research
--all-targets — clean.
2. Codex P2: `research_root()` on v0.2 upgraders was "sticky legacy"
— if `~/.actionbook/research/` existed and the new path didn't,
ALL writes went to legacy forever, defeating the rename. Split
read vs write:
- `research_root()` now always returns the canonical
`~/.actionbook/ascent-research/` (never falls back; writes go
here unconditionally).
- New `legacy_research_root()` exposes the v0.2 path for
read-only lookup.
- New `root_for_slug(slug)` returns canonical if the slug lives
there, otherwise legacy if it's present there, otherwise
canonical (for the create-new case).
- `session_dir(slug)` routes through `root_for_slug` so
resume/show/status find legacy sessions without the write
path being polluted.
Upgraders see: legacy sessions still resume; anything new lands
in the canonical path; the rename is effective from the first
v0.3 command.
3. Codex P2: `skills/ascent-research/SKILL.md` still documented
`research <sub>` / `~/.cargo/bin/research` commands, so a user
installing only the renamed skill would hit command-not-found.
Rewrote all 83 command invocations to `ascent-research <sub>`,
updated the RBIN example, title, and the mental-model path
reference. The "research CLI" noun label in the ASCII
control-flow diagram stays — it's a name, not a command.
Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>")

 |  |
| 

[specs](/actionbook/ascent-research/tree/main/specs "specs")

 | 

[specs](/actionbook/ascent-research/tree/main/specs "specs")

 | 

[chore(local-wiki): release prep — v0.2.0](/actionbook/ascent-research/commit/4cbaf085808dd47aa564d84588c565dc2323933b "chore(local-wiki): release prep — v0.2.0
- Bump crate version 0.1.0 → 0.2.0 (minor, pure addition over v1).
- Add CHANGELOG.md documenting the v3 surfaces, changes, fixes, and
test counts for the 0.2 release.
- Update root README:
* v3 feature summary at the top
* session layout table now covers SCHEMA.md + wiki/
* new "Quick tour — local codebase" section
* full CLI reference grouped by phase (lifecycle / ingest / loop /
schema / wiki / output)
* build-target matrix by feature set
* current test counts (254 unit + 326 integration)
* "Agent integration" section pointing at the bundled SKILL
- Strip Chinese from skills/research-local-wiki/SKILL.md frontmatter
and body; the skill is now fully English so it surfaces reliably
under English-first agent routers.
- Append "Reconciliation — implementation notes" section to the v3
spec documenting every step's shipping commit, seven post-spec
corrective commits (divergence fixes, file:// scheme, figure-rich
contract, preserve_diagram_refs), two UX fixes, and the invariants
the code now holds that the spec didn't specify.
No code changes — documentation and metadata only.
Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>")

 |  |
| 

[tests](/actionbook/ascent-research/tree/main/tests "tests")

 | 

[tests](/actionbook/ascent-research/tree/main/tests "tests")

 | 

[test(e2e): L4 now runs synthesize so report.html lands on disk](/actionbook/ascent-research/commit/00d8ecfa8ecbcc5327b816e2bf3bceb85508154e "test(e2e): L4 now runs synthesize so report.html lands on disk
The loop finishing with report_ready=true doesn't give you anything you
can open — synthesize is the step that turns session.md + report.json
into report.html via json-ui. L3 already did this; L4 was inconsistent.")

 |  |
| 

[.gitignore](/actionbook/ascent-research/blob/main/.gitignore ".gitignore")

 | 

[.gitignore](/actionbook/ascent-research/blob/main/.gitignore ".gitignore")

 | 

[feat(research): scaffold CLI foundation (MVP](/actionbook/ascent-research/commit/222424e53b7021beabaee24bc0a2917b7d8c4ecb "feat(research): scaffold CLI foundation (MVP #1)
Implements research-cli-foundation.spec.md:
- Cargo workspace at research-api-adapter/; research crate in
packages/research/ producing `research` binary (edition 2024)
- 12 subcommands parsed by clap (new/list/show/status/resume/add/
sources/synthesize/close/rm/route/help). All stubs return the
canonical NOT_IMPLEMENTED envelope per output::Envelope
- Global flags: --json / --verbose / --no-color
- session::layout exports every contract path + marker constants
(SOURCES_START_MARKER / SOURCES_END_MARKER) + MarkerError enum
+ locate_sources_block helper
- session::slug: is_valid_slug + derive_slug + resolve_slug with
both policies (explicit=>Err(Exists), auto=>timestamp suffix)
- session::event: canonical SessionEvent enum with 10 variants +
RejectReason enum (5 values) + line-tolerant read_events that
skips malformed lines and unknown event types with stderr warnings
- session::active: get/set/clear with fs2 flock on .active.lock,
writes atomic via tempfile+rename
- output::Envelope: ok/fail builders, optional context/details,
JSON vs plain-text rendering
- Integration tests verify --help lists all subcommands + all stubs
return structured NOT_IMPLEMENTED in JSON mode
- .gitignore for target/ and Cargo.lock (binary crate convention)
Tests: 16 unit + 3 integration = 19/19 green.
Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>") [#1](https://github.com/actionbook/ascent-research/pull/1)[)](/actionbook/ascent-research/commit/222424e53b7021beabaee24bc0a2917b7d8c4ecb "feat(research): scaffold CLI foundation (MVP #1)
Implements research-cli-foundation.spec.md:
- Cargo workspace at research-api-adapter/; research crate in
packages/research/ producing `research` binary (edition 2024)
- 12 subcommands parsed by clap (new/list/show/status/resume/add/
sources/synthesize/close/rm/route/help). All stubs return the
canonical NOT_IMPLEMENTED envelope per output::Envelope
- Global flags: --json / --verbose / --no-color
- session::layout exports every contract path + marker constants
(SOURCES_START_MARKER / SOURCES_END_MARKER) + MarkerError enum
+ locate_sources_block helper
- session::slug: is_valid_slug + derive_slug + resolve_slug with
both policies (explicit=>Err(Exists), auto=>timestamp suffix)
- session::event: canonical SessionEvent enum with 10 variants +
RejectReason enum (5 values) + line-tolerant read_events that
skips malformed lines and unknown event types with stderr warnings
- session::active: get/set/clear with fs2 flock on .active.lock,
writes atomic via tempfile+rename
- output::Envelope: ok/fail builders, optional context/details,
JSON vs plain-text rendering
- Integration tests verify --help lists all subcommands + all stubs
return structured NOT_IMPLEMENTED in JSON mode
- .gitignore for target/ and Cargo.lock (binary crate convention)
Tests: 16 unit + 3 integration = 19/19 green.
Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>")

 |  |
| 

[CHANGELOG.md](/actionbook/ascent-research/blob/main/CHANGELOG.md "CHANGELOG.md")

 | 

[CHANGELOG.md](/actionbook/ascent-research/blob/main/CHANGELOG.md "CHANGELOG.md")

 | 

[feat(rebrand): rename to ascent-research (v0.3.0)](/actionbook/ascent-research/commit/e842621f8977a8bc6790f01bad7fa4b948d3230f "feat(rebrand): rename to ascent-research (v0.3.0)
Rename the project from `research-rs` to `ascent-research` to
foreground its defining property: every session resumes, every
turn goes higher — incremental research instead of one-shot
summarize-this.
### Renamed
- Crate + binary: `research` → `ascent-research`. Scripts calling
`research` need to switch to `ascent-research`.
- Bundled skill: `skills/research-cli/` → `skills/ascent-research/`
with frontmatter `name:` updated to match. Re-link
`~/.claude/skills/ascent-research → skills/ascent-research`.
- Crate version: 0.2.0 → 0.3.0. No on-disk session format change.
- 12 integration tests now reference `CARGO_BIN_EXE_ascent-research`
instead of `CARGO_BIN_EXE_research`.
### Backward compat
- Session root default: `~/.actionbook/ascent-research/` (new). If
the new path doesn't exist but the legacy `~/.actionbook/research/`
does, it's read as fallback so v0.2 sessions keep resolving
without manual mv. `ACTIONBOOK_RESEARCH_HOME` env override
unchanged.
### README rewrite
- Slogan at the top: "Your agent's next step up. Every session
picks up where you left off. Every turn goes higher."
- One-line usage block (new → add-local → loop → synthesize)
immediately after the pitch so readers see the shape in ~5 lines.
- New "Author's positioning" section: ascent-research as an
external long-term memory for agent self-evolution — stop
throwing the agent's research away every conversation.
- New "Two ways to use it" section distinguishing standalone
(CLI drives its own loop) from skill-in-CC-instance modes, noting
that sessions are portable between them.
- Trimmed internal-mechanism descriptions (smell test details, CLI
reference table, template internals) since they now live in
skills/ascent-research/SKILL.md. README is now a
positioning / quickstart / feature-summary document, ~50 lines
shorter.
- "Project lineage" footer cites karpathy/autoresearch,
pi-autoresearch, karpathy LLM-Wiki gist, and notes the rename.
### Tests
256 lib unit + full integration suite green under
`RUSTFLAGS="-D warnings" cargo test -p ascent-research --features autoresearch`.
All 12 integration tests exec the newly-named binary via
`env!("CARGO_BIN_EXE_ascent-research")`.
### Not done in this commit (tracked separately)
- `packages/research/` directory name — renaming it would touch
every spec file and commit SHA reference. The crate name is what
users and dependents see (`cargo build -p ascent-research`), so
the dir stays as-is for now.
- GitHub repo rename (needs to be done via the web UI by the owner).
Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>")

 |  |
|  |

## ascent-research

> **Your agent's next step up. Every session picks up where you left off. Every turn goes higher.**

**One-line pitch.**`ascent-research` is an incremental research workflow CLI for AI agents: point it at a topic / source tree / Obsidian vault, and it will *keep* researching across sessions — fetching, citing, diagramming, and accreting a durable wiki you can come back to tomorrow and pick up exactly where you stopped.

```
ascent-research new "tokio internals 2026" --slug tokio --preset tech
ascent-research add-local ~/tokio/tokio/src/runtime --glob '**/*.rs'
ascent-research loop tokio --provider claude --iterations 12
ascent-research synthesize tokio --open # figure-rich HTML report
# (next day)
ascent-research resume tokio && ascent-research loop tokio --iterations 8
```

Bookmark-ready: every session lives as plain files under `~/.actionbook/ascent-research/<slug>/`, so Obsidian, VS Code, `grep` and `git` all work.

A Claude Code or Codex conversation ends. The agent forgets everything. Next week you ask the same question — same search, same fetches, same half-formed understanding.

I built `ascent-research` because I want my AI agents to **get smarter over time, not reset every session**. The on-disk session (`session.md`,`session.jsonl`, `wiki/`, `SCHEMA.md`) is the agent's external long-term memory — survives process death, carries across tool switches, inspectable and editable by the human. Every `loop` run isn't "research this topic from scratch"; it's "continue the research we were doing, check what's unused from last time, append to the pages you've already written."

The agent-facing surface (actions like `write_wiki_page`,`append_wiki_page`, `digest_source`) exists specifically so the agent can *accrete* rather than *overwrite*. The infra-enforced rules (smell test, preserve\_diagram\_refs, figure-rich contract) exist so this long-term memory stays clean without human QA every turn.

Whether you use it standalone or as a skill inside a coding-agent instance, the pitch is the same: **stop throwing away your agent's research work at the end of every conversation.** Keep it on disk. Let the next turn stand on the last one's shoulders.

`ascent-research` is a CLI that calls an LLM provider (Claude via `cc-sdk`, Codex via `codex app-server`, or `fake` for tests). Which process hosts the agent decides the usage shape:

Run the CLI directly; it spawns the provider itself and drives the research loop end-to-end, no outer agent needed. Good for batch / CI / "I just want a report."

```
ascent-research new "tokio internals" --slug tokio
ascent-research add-local ~/tokio/tokio/src
ascent-research loop tokio --provider claude --iterations 12
ascent-research synthesize tokio --open
```

Drop the bundled skill into your Claude Code / Codex config and the outer agent invokes the CLI per-turn as a tool. Good for interactive sessions where you want to mix research with coding / writing work in the same conversation, or want the outer agent to plan the workflow (decide what to ingest, when to query, when to synthesize).

```
ln -s "$PWD/skills/ascent-research" ~/.claude/skills/ascent-research
# Then in a Claude Code session: /skill:ascent-research
# Or just describe the task — "research tokio's scheduler via source" —
# the skill triggers automatically.
```

Both modes share the same on-disk session format, so you can start a session in standalone mode and later resume it from inside a Claude Code / Codex instance, or vice versa.

* * *

Five properties — each validated end-to-end across four live research sessions (tokio internals, an Obsidian agent-SE series, a mixed online-plus-local AI coding agents comparison, and self-research on this repo):

Inherits the core loop architecture from [karpathy/autoresearch](https://github.com/karpathy/autoresearch) and [pi-autoresearch](https://github.com/davebcn87/pi-autoresearch): a fresh agent can resume any session from two files — `session.md` (human-readable living doc) + `session.jsonl` (append-only event log) — even after process death, context reset, or a week of inactivity. Where the original autoresearch optimizes a single scalar (training loss, bundle size, test speed) via `edit → benchmark → keep-or-revert`, `ascent-research` generalizes the same loop grammar to *research*:`plan → fetch → digest → write_section / write_wiki_page / write_diagram` producing a figure-rich report plus a durable cross-session wiki instead of a single optimized number.

`ascent-research resume <slug>` picks up exactly where a prior turn stopped. Wiki pages *accrue* via `append_wiki_page` — new findings grow existing entity pages instead of overwriting them. Coverage signals (`sources_unused`, `diagrams_referenced`, `wiki_pages`,`wiki_total_bytes`) let each loop run know *what's still open* from the previous turn, so it continues rather than restarts. One-shot DR tools can't do this — when they finish, they're done.

`add` (HTTP via `postagent`) + `add-local` (file trees) + browser fallback (via `actionbook browser` for JS-heavy pages) all flow through the same smell-test → event-log → wiki → report path. A single session can cite GitHub READMEs, arXiv papers, blog posts, and your private Obsidian notes side-by-side in one wiki page's sources list — the renderer doesn't care about URL scheme.

Narrative-only output is considered incomplete. The loop's system prompt carries a non-negotiable FIGURE-RICH CONTRACT: target ≥ 1 hand-drawn SVG per numbered section, bidirectional rule that every`![](diagrams/x.svg)` markdown reference must have a matching `write_diagram` action and vice versa, infra-level guarantee that section overwrites never drop figures. Every SVG is inline (no external assets, no screenshots) and the HTML report has a clickable wiki TOC + EN/ZH bilingual toggle.

Agents can't "just summarize this for me." Every fetch runs through a smell test at the CLI layer before the LLM sees it; rejections become typed events. Overwrites preserve figures. Wiki writes are append-safe. Coverage computes `sources_hallucinated` (URLs cited but never fetched) as a `report_ready` blocker. Every error returns a machine-readable code (`NO_ACTIVE_SESSION`, `SMELL_REJECTED`,`DIAGRAM_OUT_OF_BOUNDS`, `WIKI_EMPTY`, …) so agents route recovery deterministically without parsing prose.

* * *

## Install

```
git clone https://github.com/ZhangHanDong/ascent-research
cd ascent-research

# Full build (loop + Claude provider) — what live sessions need
cargo build -p ascent-research --release --features "autoresearch provider-claude"

export PATH="$PWD/target/release:$PATH"
ascent-research --help
```

Alternative feature sets:

```
# Minimal — no autonomous loop, no LLM
cargo build -p ascent-research --release

# Loop with fake provider only (for scripted tests)
cargo build -p ascent-research --release --features autoresearch

# Loop with Codex instead of Claude
cargo build -p ascent-research --release --features "autoresearch provider-codex"
```

Prereqs for online ingest: Rust stable (edition 2024),[`postagent`](https://github.com/actionbook/postagent) for HTTP API fetches, optionally [`actionbook`](https://github.com/actionbook/actionbook) for browser fallback on JS-heavy sites. Neither is required if you only use `add-local`.

* * *

```
ascent-research new "state-space models 2026" --slug ssm --preset tech
ascent-research batch \
  https://arxiv.org/abs/2111.00396 \
  https://arxiv.org/abs/2312.00752 \
  https://github.com/HazyResearch/state-spaces \
  --concurrency 4
ascent-research loop ssm --provider claude --iterations 10
ascent-research synthesize ssm --bilingual --open
```

```
ascent-research new "axum internals" --slug axum --preset tech
ascent-research schema edit # set your "what to emphasize"
ascent-research add-local ~/axum/axum/src --glob '**/*.rs'
ascent-research loop axum --provider claude --iterations 12
ascent-research synthesize axum --open
```

```
ascent-research new "my agent-SE notes" --slug notes --preset tech
ascent-research add-local ~/vault/agent-notes --glob '**/*.md'
ascent-research loop notes --provider claude --iterations 10
ascent-research wiki query "what's my stance on code review for AI?" \
  --save-as my-code-review-stance
```

Full command reference, error-code triage, loop contracts, and scenario playbooks: see [`skills/ascent-research/SKILL.md`](/actionbook/ascent-research/blob/main/skills/ascent-research/SKILL.md).

* * *

## Session layout

Each project is one directory under `~/.actionbook/ascent-research/<slug>/`. Everything is plain files — markdown, JSON lines, SVG, TOML — so your editor / grep / git / Obsidian all work without a custom client.

| File | Purpose |
| --- | --- |
| `session.md` | Narrative — numbered sections, overview, aside. Report spine. |
| `session.jsonl` | Append-only event log. Sources, attempts, loop steps. Authoritative. |
| `SCHEMA.md` | User-editable session guidance. Loop re-reads each turn. |
| `wiki/*.md` | Persistent entity / concept / analysis pages with cross-links. |
| `diagrams/*.svg` | Hand-drawn figures inlined into the HTML report. |
| `raw/` | Raw fetched content, one file per accepted source. |
| `report.html` | Rendered editorial output — wiki TOC, inline SVGs, optional bilingual toggle. |

Override the root via `ACTIONBOOK_RESEARCH_HOME=/some/path`. Legacy `~/.actionbook/research/` is read as a fallback so sessions from v0.2 keep working.

* * *

## Agent integration

`skills/ascent-research/SKILL.md` is a bundled Claude Code / Codex skill describing the full workflow with nine scenario playbooks, error-code triage, and build-target matrix. Expose it on your global skill path:

```
ln -s "$PWD/skills/ascent-research" ~/.claude/skills/ascent-research
```

* * *

## Development

```
cargo test -p ascent-research # core suite
cargo test -p ascent-research --features autoresearch # + loop suite (fake provider)
```

All integration tests use a `FakeProvider` replaying scripted JSON turns, so the full suite never hits a real LLM and needs no network.

* * *

## Project lineage

- Core 2-file resume loop inherited from [karpathy/autoresearch](https://github.com/karpathy/autoresearch)
- Per-session wiki layer inspired by karpathy's [LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- Widget / dashboard pattern borrowed from [pi-autoresearch](https://github.com/davebcn87/pi-autoresearch)
- Previously named `research-rs` (v0.1 / v0.2); renamed to `ascent-research` in v0.3 to foreground the incremental-research story

* * *

## License

Apache-2.0.

## Releases

No releases published

## Packages

No packages published

## Languages

- [Rust 93.7%](/actionbook/ascent-research/search?l=rust)
- [Shell 4.7%](/actionbook/ascent-research/search?l=shell)
- [HTML 1.6%](/actionbook/ascent-research/search?l=html)