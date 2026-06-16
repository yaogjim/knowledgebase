---
title: "2026-06-16_github_com_rohitg00_agentmemory_1_Persistent_memory_for_AI_co"
source: "https://github.com/rohitg00/agentmemory"
author:
  - "[[@K]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "#311"
  - "#codex"
  - "github"
  - "@K"
---

# rohitg00/agentmemory: #1 Persistent memory for AI coding agents based on real-world benchmarks

[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](/codespaces/new/rohitg00/agentmemory?resume=1)

| Name | Name | 
Last commit message

 | 

Last commit date

 |
| --- | --- | --- | --- |
| 

[chore(release): v0.9.24 — --version flag + iii hard-pin enforcement (](/rohitg00/agentmemory/commit/fd9e3bd42d6208a33f0ee9de1442fdbb60eab106)[#…](https://github.com/rohitg00/agentmemory/pull/719)

[fd9e3bd](/rohitg00/agentmemory/commit/fd9e3bd42d6208a33f0ee9de1442fdbb60eab106) ·

[423 Commits](/rohitg00/agentmemory/commits/main/)

 |
| 

[.claude-plugin](/rohitg00/agentmemory/tree/main/.claude-plugin ".claude-plugin")

 | 

[.claude-plugin](/rohitg00/agentmemory/tree/main/.claude-plugin ".claude-plugin")

 |  |  |
| 

[.codex-plugin](/rohitg00/agentmemory/tree/main/.codex-plugin ".codex-plugin")

 | 

[.codex-plugin](/rohitg00/agentmemory/tree/main/.codex-plugin ".codex-plugin")

 | 

[feat(plugin): ship Codex plugin manifest + marketplace (](/rohitg00/agentmemory/commit/c21410e2875472f476aa4feddead4f9202972ad9 "feat(plugin): ship Codex plugin manifest + marketplace (#311)
* feat(plugin): ship Codex plugin manifest + marketplace (#codex-plugins)
OpenAI Codex shipped a plugin platform
(developers.openai.com/codex/plugins) with the same shape as Anthropic
Claude Code plugins: .codex-plugin/plugin.json manifest, optional
.mcp.json, hooks/hooks.json, and a skills/ directory.
Verified against openai/codex source
(codex-rs/hooks/src/engine/discovery.rs): Codex's hook engine
explicitly injects CLAUDE_PLUGIN_ROOT into hook subprocesses for
OOTB compat with existing Claude Code plugins. The wire-format
input schemas
(codex-rs/hooks/schema/generated/session-start.command.input.schema.json
and siblings) use the same field names as Claude Code
(session_id, cwd, hook_event_name, source, transcript_path, model,
permission_mode).
Net result: our existing plugin/ directory already works as a Codex
plugin with two small additions:
1. plugin/.codex-plugin/plugin.json — Codex manifest pointing at the
shared ./.mcp.json, ./skills/, and a Codex-specific ./hooks/
hooks.codex.json. Name (kebab-case), version, description match
the Claude Code manifest.
2. plugin/hooks/hooks.codex.json — Codex-compatible hook subset.
Drops SubagentStart, SubagentStop, SessionEnd, Notification,
TaskCompleted, PostToolUseFailure (Claude-Code-only). Keeps
SessionStart, UserPromptSubmit, PreToolUse, PostToolUse,
PreCompact, Stop. Adds Codex-specific `statusMessage` decorations
on the two hooks the user sees most (SessionStart + UserPromptSubmit).
The script commands themselves still reference ${CLAUDE_PLUGIN_ROOT}
because Codex's engine injects it.
3. .codex-plugin/marketplace.json at repo root — git-subdir source
pointing at ./plugin so `codex plugin marketplace add rohitg00/
agentmemory` works the same way `claude plugin marketplace add`
does. Mirrors the existing .claude-plugin/marketplace.json shape
but in Codex's marketplace schema (name + interface.displayName
+ plugins[].source.{source, url, path, ref} + plugins[].policy).
README updates:
- Codex CLI tile in the Works-with-every-agent grid now reads
"6 hooks + MCP + skills" instead of "MCP server" to surface the
upgraded surface.
- "Other agents" install table now distinguishes "Codex CLI (MCP
only)" (existing codex mcp add path) from "Codex CLI (full
plugin)" (new marketplace install).
- New Codex section in the "paste this prompt" block with the
two-command install (server + marketplace add + plugin install),
the list of registered surfaces, and the env-var-injection note
citing the Codex source line.
6 new tests in test/codex-plugin.test.ts cover:
1. .codex-plugin/plugin.json present with kebab-case name and
required references.
2. Manifest version matches main package.json (so future bumps
don't drift the Codex side).
3. Every path referenced in the manifest resolves to a real file or
directory on disk.
4. hooks.codex.json contains only events Codex supports — any
future addition has to be added to a Codex allowlist or the
test fails loudly.
5. Every ${CLAUDE_PLUGIN_ROOT}/scripts/* command references an
existing script file (catches typos before users hit them).
6. .codex-plugin/marketplace.json declares git-subdir source with
path: "./plugin" pointing at this repo.
874 / 874 tests pass.
* fix(plugin/codex): align manifest description + assert PreCompact hook
Two reviewer findings addressed:
1. plugin/.codex-plugin/plugin.json's description claimed "12 hooks"
but Codex only registers 6 (the Codex hook input schemas don't
define SubagentStart, SubagentStop, SessionEnd, Notification,
TaskCompleted, PostToolUseFailure). Updated the description to
"6 hooks, 51 MCP tools, 4 skills, real-time viewer." so the
marketplace listing matches the registered surface.
2. test/codex-plugin.test.ts asserted five lifecycle events
(SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, Stop)
but omitted PreCompact, leaving a regression hole: dropping
PreCompact from hooks.codex.json would still pass the test
because the allowlist loop only blocks UNKNOWN events. Added
expect(events).toContain("PreCompact") so the suite enforces
the full six-hook contract.
Skipped (with reason):
3. marketplace.json source.ref currently "main" — reviewer asked
for a fixed tag/SHA. Skipping because pinning to a tag forces
updating marketplace.json on every release; "main" matches our
convention where releases tag from main HEAD and pre-release
work is on feature branches. Users wanting an immutable cut
can pass --ref vX.Y.Z to `codex plugin marketplace add` per
Codex docs.
Validation: 6/6 codex tests pass; 874/874 full suite unchanged.")[#311](https://github.com/rohitg00/agentmemory/pull/311)[)](/rohitg00/agentmemory/commit/c21410e2875472f476aa4feddead4f9202972ad9 "feat(plugin): ship Codex plugin manifest + marketplace (#311)
* feat(plugin): ship Codex plugin manifest + marketplace (#codex-plugins)
OpenAI Codex shipped a plugin platform
(developers.openai.com/codex/plugins) with the same shape as Anthropic
Claude Code plugins: .codex-plugin/plugin.json manifest, optional
.mcp.json, hooks/hooks.json, and a skills/ directory.
Verified against openai/codex source
(codex-rs/hooks/src/engine/discovery.rs): Codex's hook engine
explicitly injects CLAUDE_PLUGIN_ROOT into hook subprocesses for
OOTB compat with existing Claude Code plugins. The wire-format
input schemas
(codex-rs/hooks/schema/generated/session-start.command.input.schema.json
and siblings) use the same field names as Claude Code
(session_id, cwd, hook_event_name, source, transcript_path, model,
permission_mode).
Net result: our existing plugin/ directory already works as a Codex
plugin with two small additions:
1. plugin/.codex-plugin/plugin.json — Codex manifest pointing at the
shared ./.mcp.json, ./skills/, and a Codex-specific ./hooks/
hooks.codex.json. Name (kebab-case), version, description match
the Claude Code manifest.
2. plugin/hooks/hooks.codex.json — Codex-compatible hook subset.
Drops SubagentStart, SubagentStop, SessionEnd, Notification,
TaskCompleted, PostToolUseFailure (Claude-Code-only). Keeps
SessionStart, UserPromptSubmit, PreToolUse, PostToolUse,
PreCompact, Stop. Adds Codex-specific `statusMessage` decorations
on the two hooks the user sees most (SessionStart + UserPromptSubmit).
The script commands themselves still reference ${CLAUDE_PLUGIN_ROOT}
because Codex's engine injects it.
3. .codex-plugin/marketplace.json at repo root — git-subdir source
pointing at ./plugin so `codex plugin marketplace add rohitg00/
agentmemory` works the same way `claude plugin marketplace add`
does. Mirrors the existing .claude-plugin/marketplace.json shape
but in Codex's marketplace schema (name + interface.displayName
+ plugins[].source.{source, url, path, ref} + plugins[].policy).
README updates:
- Codex CLI tile in the Works-with-every-agent grid now reads
"6 hooks + MCP + skills" instead of "MCP server" to surface the
upgraded surface.
- "Other agents" install table now distinguishes "Codex CLI (MCP
only)" (existing codex mcp add path) from "Codex CLI (full
plugin)" (new marketplace install).
- New Codex section in the "paste this prompt" block with the
two-command install (server + marketplace add + plugin install),
the list of registered surfaces, and the env-var-injection note
citing the Codex source line.
6 new tests in test/codex-plugin.test.ts cover:
1. .codex-plugin/plugin.json present with kebab-case name and
required references.
2. Manifest version matches main package.json (so future bumps
don't drift the Codex side).
3. Every path referenced in the manifest resolves to a real file or
directory on disk.
4. hooks.codex.json contains only events Codex supports — any
future addition has to be added to a Codex allowlist or the
test fails loudly.
5. Every ${CLAUDE_PLUGIN_ROOT}/scripts/* command references an
existing script file (catches typos before users hit them).
6. .codex-plugin/marketplace.json declares git-subdir source with
path: "./plugin" pointing at this repo.
874 / 874 tests pass.
* fix(plugin/codex): align manifest description + assert PreCompact hook
Two reviewer findings addressed:
1. plugin/.codex-plugin/plugin.json's description claimed "12 hooks"
but Codex only registers 6 (the Codex hook input schemas don't
define SubagentStart, SubagentStop, SessionEnd, Notification,
TaskCompleted, PostToolUseFailure). Updated the description to
"6 hooks, 51 MCP tools, 4 skills, real-time viewer." so the
marketplace listing matches the registered surface.
2. test/codex-plugin.test.ts asserted five lifecycle events
(SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, Stop)
but omitted PreCompact, leaving a regression hole: dropping
PreCompact from hooks.codex.json would still pass the test
because the allowlist loop only blocks UNKNOWN events. Added
expect(events).toContain("PreCompact") so the suite enforces
the full six-hook contract.
Skipped (with reason):
3. marketplace.json source.ref currently "main" — reviewer asked
for a fixed tag/SHA. Skipping because pinning to a tag forces
updating marketplace.json on every release; "main" matches our
convention where releases tag from main HEAD and pre-release
work is on feature branches. Users wanting an immutable cut
can pass --ref vX.Y.Z to `codex plugin marketplace add` per
Codex docs.
Validation: 6/6 codex tests pass; 874/874 full suite unchanged.")

 |  |
| 

[.github](/rohitg00/agentmemory/tree/main/.github ".github")

 | 

[.github](/rohitg00/agentmemory/tree/main/.github ".github")

 | 

[ci: cross-platform matrix + paths-ignore + concurrency (](/rohitg00/agentmemory/commit/e9dc710e5623106363cf2735beaff901eb1d5a46 "ci: cross-platform matrix + paths-ignore + concurrency (#556)
* ci: cross-platform matrix + paths-ignore + concurrency
1. **OS matrix** — Linux + Windows + macOS, both Node 20 + 22. 6 cells,
~3min each, ~18min wall time. Direct test against the class of
bug #487 caught: hooks crashing on Windows usernames with spaces.
Pre-merge Linux-only CI meant that bug landed in main + a release.
fail-fast: false so a flake on one cell doesn't mask whether the
same failure reproduces elsewhere.
2. **paths-ignore** — skip CI runs on README / CHANGELOG / docs /
website / assets / .md / .mdx pushes. ~half the runner minutes
back on doc-only churn. Source / config / workflow changes
always run.
3. **concurrency + cancel-in-progress** — PR force-pushes cancel
in-flight runs instead of piling them up. Push to main protected
(concurrency group still scoped to ref, no cancel for main pushes).
Plus minor hardening: persist-credentials: false on the checkout
step so the GITHUB_TOKEN doesn't land in .git/config.
What was NOT lifted (rationale per plan):
- Per-package reusable workflows (Rust/Python/Homebrew — non-TS).
- License-header check (no per-file Apache banners in agentmemory).
- CLA bot (defer until external PR volume justifies friction).
- tsc --noEmit lint job (codebase has ~10 pre-existing type errors
tsdown skips; gating CI on those would block every PR until
fixed; tracked as separate cleanup).
- Smoke test (`agentmemory demo + livez`) — defer to its own PR
with its own validation cycle.
- Codecov badge — defer until baseline is set.
* ci(windows): force bash shell so build script's POSIX idioms work
Windows runners default to cmd.exe for npm run scripts; the build
script uses POSIX patterns the build script's exit codes
(`cp ... 2>/dev/null || true`, `mkdir -p`) that cmd doesn't
parse. ubuntu + macos already use bash by default so this is
Windows-only behaviour change.
Alternative: rewrite the build script in Node. Bigger lift, not
minimal.
* ci(windows): point npm script-shell at git-bash before build
`shell: bash` on the step only sets the shell for the step's own
runner; `npm run` still spawns its inner script via npm's
`script-shell` config, which defaults to cmd.exe on Windows.
Configure npm to use Git-Bash (preinstalled on GitHub-hosted
Windows runners) so `npm run build` and `npm run test` execute
the build script the same way ubuntu + macos do.
Step is gated on `runner.os == 'Windows'` so it's a no-op on the
other matrix cells.
* ci: drop windows-latest from matrix (obsidian-export hardcoded POSIX paths)
Windows runners fail on test/obsidian-export.test.ts because the
test + src hardcode `/tmp/...` POSIX paths that don't resolve on
the D:\ drive Windows uses. Fixing it cleanly requires reworking
src/functions/obsidian-export.ts to use os.tmpdir() + path.join,
which is a separate scope.
Drop windows from the matrix for now. Ship ubuntu + macos coverage
(real darwin/linux divergence catch) and file a follow-up to make
obsidian-export cross-platform so Windows can be added back.
* test(fs-watcher): bump waits to 1500ms + describe retry for macos fsevents flake")[#556](https://github.com/rohitg00/agentmemory/pull/556)[)](/rohitg00/agentmemory/commit/e9dc710e5623106363cf2735beaff901eb1d5a46 "ci: cross-platform matrix + paths-ignore + concurrency (#556)
* ci: cross-platform matrix + paths-ignore + concurrency
1. **OS matrix** — Linux + Windows + macOS, both Node 20 + 22. 6 cells,
~3min each, ~18min wall time. Direct test against the class of
bug #487 caught: hooks crashing on Windows usernames with spaces.
Pre-merge Linux-only CI meant that bug landed in main + a release.
fail-fast: false so a flake on one cell doesn't mask whether the
same failure reproduces elsewhere.
2. **paths-ignore** — skip CI runs on README / CHANGELOG / docs /
website / assets / .md / .mdx pushes. ~half the runner minutes
back on doc-only churn. Source / config / workflow changes
always run.
3. **concurrency + cancel-in-progress** — PR force-pushes cancel
in-flight runs instead of piling them up. Push to main protected
(concurrency group still scoped to ref, no cancel for main pushes).
Plus minor hardening: persist-credentials: false on the checkout
step so the GITHUB_TOKEN doesn't land in .git/config.
What was NOT lifted (rationale per plan):
- Per-package reusable workflows (Rust/Python/Homebrew — non-TS).
- License-header check (no per-file Apache banners in agentmemory).
- CLA bot (defer until external PR volume justifies friction).
- tsc --noEmit lint job (codebase has ~10 pre-existing type errors
tsdown skips; gating CI on those would block every PR until
fixed; tracked as separate cleanup).
- Smoke test (`agentmemory demo + livez`) — defer to its own PR
with its own validation cycle.
- Codecov badge — defer until baseline is set.
* ci(windows): force bash shell so build script's POSIX idioms work
Windows runners default to cmd.exe for npm run scripts; the build
script uses POSIX patterns the build script's exit codes
(`cp ... 2>/dev/null || true`, `mkdir -p`) that cmd doesn't
parse. ubuntu + macos already use bash by default so this is
Windows-only behaviour change.
Alternative: rewrite the build script in Node. Bigger lift, not
minimal.
* ci(windows): point npm script-shell at git-bash before build
`shell: bash` on the step only sets the shell for the step's own
runner; `npm run` still spawns its inner script via npm's
`script-shell` config, which defaults to cmd.exe on Windows.
Configure npm to use Git-Bash (preinstalled on GitHub-hosted
Windows runners) so `npm run build` and `npm run test` execute
the build script the same way ubuntu + macos do.
Step is gated on `runner.os == 'Windows'` so it's a no-op on the
other matrix cells.
* ci: drop windows-latest from matrix (obsidian-export hardcoded POSIX paths)
Windows runners fail on test/obsidian-export.test.ts because the
test + src hardcode `/tmp/...` POSIX paths that don't resolve on
the D:\ drive Windows uses. Fixing it cleanly requires reworking
src/functions/obsidian-export.ts to use os.tmpdir() + path.join,
which is a separate scope.
Drop windows from the matrix for now. Ship ubuntu + macos coverage
(real darwin/linux divergence catch) and file a follow-up to make
obsidian-export cross-platform so Windows can be added back.
* test(fs-watcher): bump waits to 1500ms + describe retry for macos fsevents flake")

 |  |
| 

[READMEs](/rohitg00/agentmemory/tree/main/READMEs "READMEs")

 | 

[READMEs](/rohitg00/agentmemory/tree/main/READMEs "READMEs")

 | 

[docs(readme): 11 README translations + language picker (](/rohitg00/agentmemory/commit/26980a81c5ff3013d0b6e63daf82575387860bf4 "docs(readme): 11 README translations + language picker (#675)
* docs(readme): ko-KR + es-ES + pt-BR translations
* docs(readme): zh-CN + zh-TW + ja-JP translations
* docs(readme): tr-TR + hi-IN translations
* docs(readme): fr-FR + de-DE + ru-RU translations
* docs(readme): language picker for 11 translated locales
Adds top-of-README link row to READMEs/README.{locale}.md files. 11 translations land alongside: zh-CN, zh-TW, ja-JP, ko-KR, es-ES, pt-BR, fr-FR, de-DE, ru-RU, tr-TR, hi-IN.
* docs(readme): label bare fences as text + fix repo-root paths in de/fr/ru
MD040: add 'text' language tag to the 5 prose-only fenced blocks (lines 431, 482, 507, 705, 738) in source README and propagated to all 11 translations.
Path: de-DE, fr-FR, ru-RU had md links + html href/src to repo-root paths (integrations/, docs/, eval/, benchmark/, src/, deploy/, plugin/, examples/, CHANGELOG, LICENSE, assets/) without ../ prefix — files live in READMEs/, so paths resolved one level too high. Prepended ../ on all matched refs.
Reviewer-flagged ko-KR path issue verified false-positive: that file already had ../ prefix from initial translation.")[#675](https://github.com/rohitg00/agentmemory/pull/675)[)](/rohitg00/agentmemory/commit/26980a81c5ff3013d0b6e63daf82575387860bf4 "docs(readme): 11 README translations + language picker (#675)
* docs(readme): ko-KR + es-ES + pt-BR translations
* docs(readme): zh-CN + zh-TW + ja-JP translations
* docs(readme): tr-TR + hi-IN translations
* docs(readme): fr-FR + de-DE + ru-RU translations
* docs(readme): language picker for 11 translated locales
Adds top-of-README link row to READMEs/README.{locale}.md files. 11 translations land alongside: zh-CN, zh-TW, ja-JP, ko-KR, es-ES, pt-BR, fr-FR, de-DE, ru-RU, tr-TR, hi-IN.
* docs(readme): label bare fences as text + fix repo-root paths in de/fr/ru
MD040: add 'text' language tag to the 5 prose-only fenced blocks (lines 431, 482, 507, 705, 738) in source README and propagated to all 11 translations.
Path: de-DE, fr-FR, ru-RU had md links + html href/src to repo-root paths (integrations/, docs/, eval/, benchmark/, src/, deploy/, plugin/, examples/, CHANGELOG, LICENSE, assets/) without ../ prefix — files live in READMEs/, so paths resolved one level too high. Prepended ../ on all matched refs.
Reviewer-flagged ko-KR path issue verified false-positive: that file already had ../ prefix from initial translation.")

 |  |
| 

[assets](/rohitg00/agentmemory/tree/main/assets "assets")

 | 

[assets](/rohitg00/agentmemory/tree/main/assets "assets")

 | 

[chore(website): refresh agents grid + logos for v0.9.23 (](/rohitg00/agentmemory/commit/a9bc129430f922c9102ec43fd749a634f307ca52 "chore(website): refresh agents grid + logos for v0.9.23 (#710)
* chore(website): refresh agents grid + logos for v0.9.23
Agents section was stale relative to the supported agent matrix that
v0.9.23 ships:
- FEATURED cards bumped from 6 to 7 — adds Copilot CLI (full plugin
+ hooks + MCP from PR #534). Title updates from "SIX FIRST-PARTY"
to "SEVEN NATIVE PLUGINS".
- MARQUEE tiles expanded from 10 to 17 — adds Warp, Continue, Zed,
Droid (the 4 covered by `npx skills add` from PR #677) plus Qwen
Code, Antigravity, and Kiro (the 3 from PR #648).
- Logos switched from `github.com/<org>.png` avatars and stale
third-party CDNs (freelogovectors.net, exafunction.github.io) to
svgl.app brand SVGs where available (Anthropic, GitHub, OpenAI,
Cursor, Warp, Continue, Zed, Gemini, Google, Qwen, Windsurf) or
the agent's own website favicon where svgl doesn't carry the
brand (Factory.ai, Kiro, OpenCode, Cline, Roo, Kilo, Goose,
Aider, OpenClaw, Nous Research). Cursor and Windsurf logo paths
were specifically broken; the freelogovectors URL was unreliable
and Codeium → Cognition acquisition stale-dated the Windsurf path.
AgentInstall chip row adds Copilot CLI + Warp alongside the
existing Cursor / VS Code / Claude Code / Claude Desktop / Gemini /
Codex shortcuts. Universal MCP JSON hint and "show more" button
both updated to list the agents we actually support now.
* fix(website): use correct svgl.app slugs + add hostnames to remotePatterns
Previous commit's logo URLs all 404'd:
- svgl.app slugs were wrong (e.g. anthropic.svg vs anthropic_white.svg,
cursor.svg vs cursor_dark.svg). svgl exposes themed variants
(`_light`/`_dark`/`_white`/`_black`) but bare `<slug>.svg` only
exists for a few entries. Verified actual URLs via api.svgl.app for
every featured + marquee tile.
- Next.js Image `remotePatterns` didn't whitelist svgl.app or the
agent-domain favicon hosts (factory.ai, kiro.dev, opencode.ai,
cline.bot, etc.), so even valid URLs were rejected before fetch.
Now uses dark-bg-appropriate variants throughout (white/dark logos on
the black page background). For the few brands not in svgl
(continue, kiro, opencode, cline, roo, goose, aider, openclaw,
hermes, droid), falls back to the agent's own website favicon —
each URL HEAD-probed for 200.
Dropped stale remotePatterns: exafunction.github.io,
www.freelogovectors.net, block.github.io (replaced with goose.dev).
Added: continue.dev, goose.dev.
* revert(website): restore github.com avatars for existing agents
Only new logos (copilot-cli, warp, continue, zed, droid, antigravity,
qwen, kiro) and previously-broken ones (cursor, windsurf) use svgl /
own-site URLs. Original github.com/<org>.png avatars for claude-code,
codex, openclaw, hermes, claude-desktop, gemini, opencode, cline, roo,
kilo, goose, aider restored — they were never broken.
next.config remotePatterns trimmed to: svgl.app, www.factory.ai,
kiro.dev, continue.dev (the only non-github hosts still in use).
* fix(assets): pi logo fill white for dark website bg
User-provided SVG uses #09090b near-black; invisible on the agents
grid's dark background. Same path, fill swapped to #ffffff.")[#710](https://github.com/rohitg00/agentmemory/pull/710)[)](/rohitg00/agentmemory/commit/a9bc129430f922c9102ec43fd749a634f307ca52 "chore(website): refresh agents grid + logos for v0.9.23 (#710)
* chore(website): refresh agents grid + logos for v0.9.23
Agents section was stale relative to the supported agent matrix that
v0.9.23 ships:
- FEATURED cards bumped from 6 to 7 — adds Copilot CLI (full plugin
+ hooks + MCP from PR #534). Title updates from "SIX FIRST-PARTY"
to "SEVEN NATIVE PLUGINS".
- MARQUEE tiles expanded from 10 to 17 — adds Warp, Continue, Zed,
Droid (the 4 covered by `npx skills add` from PR #677) plus Qwen
Code, Antigravity, and Kiro (the 3 from PR #648).
- Logos switched from `github.com/<org>.png` avatars and stale
third-party CDNs (freelogovectors.net, exafunction.github.io) to
svgl.app brand SVGs where available (Anthropic, GitHub, OpenAI,
Cursor, Warp, Continue, Zed, Gemini, Google, Qwen, Windsurf) or
the agent's own website favicon where svgl doesn't carry the
brand (Factory.ai, Kiro, OpenCode, Cline, Roo, Kilo, Goose,
Aider, OpenClaw, Nous Research). Cursor and Windsurf logo paths
were specifically broken; the freelogovectors URL was unreliable
and Codeium → Cognition acquisition stale-dated the Windsurf path.
AgentInstall chip row adds Copilot CLI + Warp alongside the
existing Cursor / VS Code / Claude Code / Claude Desktop / Gemini /
Codex shortcuts. Universal MCP JSON hint and "show more" button
both updated to list the agents we actually support now.
* fix(website): use correct svgl.app slugs + add hostnames to remotePatterns
Previous commit's logo URLs all 404'd:
- svgl.app slugs were wrong (e.g. anthropic.svg vs anthropic_white.svg,
cursor.svg vs cursor_dark.svg). svgl exposes themed variants
(`_light`/`_dark`/`_white`/`_black`) but bare `<slug>.svg` only
exists for a few entries. Verified actual URLs via api.svgl.app for
every featured + marquee tile.
- Next.js Image `remotePatterns` didn't whitelist svgl.app or the
agent-domain favicon hosts (factory.ai, kiro.dev, opencode.ai,
cline.bot, etc.), so even valid URLs were rejected before fetch.
Now uses dark-bg-appropriate variants throughout (white/dark logos on
the black page background). For the few brands not in svgl
(continue, kiro, opencode, cline, roo, goose, aider, openclaw,
hermes, droid), falls back to the agent's own website favicon —
each URL HEAD-probed for 200.
Dropped stale remotePatterns: exafunction.github.io,
www.freelogovectors.net, block.github.io (replaced with goose.dev).
Added: continue.dev, goose.dev.
* revert(website): restore github.com avatars for existing agents
Only new logos (copilot-cli, warp, continue, zed, droid, antigravity,
qwen, kiro) and previously-broken ones (cursor, windsurf) use svgl /
own-site URLs. Original github.com/<org>.png avatars for claude-code,
codex, openclaw, hermes, claude-desktop, gemini, opencode, cline, roo,
kilo, goose, aider restored — they were never broken.
next.config remotePatterns trimmed to: svgl.app, www.factory.ai,
kiro.dev, continue.dev (the only non-github hosts still in use).
* fix(assets): pi logo fill white for dark website bg
User-provided SVG uses #09090b near-black; invisible on the agents
grid's dark background. Same path, fill swapped to #ffffff.")

 |  |
| 

[benchmark](/rohitg00/agentmemory/tree/main/benchmark "benchmark")

 | 

[benchmark](/rohitg00/agentmemory/tree/main/benchmark "benchmark")

 | 

[feat(bench): load-100k.ts harness with p50/p90/p99 output (](/rohitg00/agentmemory/commit/d1517465ca0e56b904f6a356fe0ea07fce3821b6 "feat(bench): load-100k.ts harness with p50/p90/p99 output (#363)
Adds a reproducible, dependency-free load harness so we can answer
"what's p99 at 100k memories under concurrency 100?" with a number
instead of a shrug.
The harness seeds N synthetic memories against a local agentmemory
daemon (defaults to http://localhost:3111, optional autostart via
AGENTMEMORY_BENCH_AUTOSTART=1), then drives a matrix of
(N, concurrency, endpoint) cells with hand-rolled Promise.allSettled
batches. Per-request latency is collected via performance.now() and
summarized as nearest-rank p50 / p90 / p99 plus min / max / errors
and wall-clock throughput. Results are written to
benchmark/results/load-100k-<short-git-sha>.json with a
schema_version field so future format changes don't silently break
consumers.
Defaults match issue #346: N in {1000, 10000, 100000} x C in
{1, 10, 100} x three endpoints (POST /agentmemory/remember,
POST /agentmemory/smart-search, GET /agentmemory/memories?latest=true).
Each cell issues BENCH_OPS=200 requests by default — enough samples
for stable p99 without dragging a 100k-seed run past tens of minutes.
Content is generated by a small noun/verb/concept vocabulary fed by a
mulberry32(BENCH_SEED) PRNG so re-running the harness against the
same daemon build yields the same seed corpus. Reproducibility, not
realism, is the point — latency variance comes from the daemon, not
JSON payload jitter.
Files:
- benchmark/load-100k.ts: main harness
- benchmark/lib/percentiles.ts: zero-dep pXX helper, nearest-rank
- benchmark/README.md: how to run, what gets measured, where results
land, and why p99 is the number you want for capacity planning
- benchmark/results/load-100k-96c0ed0.json: example result from a
small-N (N=1000, C=10) verification run against a fresh daemon
- package.json: wires `npm run bench:load`
- CHANGELOG.md: Unreleased entry + a Performance section placeholder
describing where per-release numbers should land going forward
Verified locally at BENCH_N=1000 BENCH_C=10 BENCH_OPS=200 — three
cells, zero errors, JSON written. Full 100k matrix is intentionally
deferred to CI/release time. Closes #346.")[#363](https://github.com/rohitg00/agentmemory/pull/363)[)](/rohitg00/agentmemory/commit/d1517465ca0e56b904f6a356fe0ea07fce3821b6 "feat(bench): load-100k.ts harness with p50/p90/p99 output (#363)
Adds a reproducible, dependency-free load harness so we can answer
"what's p99 at 100k memories under concurrency 100?" with a number
instead of a shrug.
The harness seeds N synthetic memories against a local agentmemory
daemon (defaults to http://localhost:3111, optional autostart via
AGENTMEMORY_BENCH_AUTOSTART=1), then drives a matrix of
(N, concurrency, endpoint) cells with hand-rolled Promise.allSettled
batches. Per-request latency is collected via performance.now() and
summarized as nearest-rank p50 / p90 / p99 plus min / max / errors
and wall-clock throughput. Results are written to
benchmark/results/load-100k-<short-git-sha>.json with a
schema_version field so future format changes don't silently break
consumers.
Defaults match issue #346: N in {1000, 10000, 100000} x C in
{1, 10, 100} x three endpoints (POST /agentmemory/remember,
POST /agentmemory/smart-search, GET /agentmemory/memories?latest=true).
Each cell issues BENCH_OPS=200 requests by default — enough samples
for stable p99 without dragging a 100k-seed run past tens of minutes.
Content is generated by a small noun/verb/concept vocabulary fed by a
mulberry32(BENCH_SEED) PRNG so re-running the harness against the
same daemon build yields the same seed corpus. Reproducibility, not
realism, is the point — latency variance comes from the daemon, not
JSON payload jitter.
Files:
- benchmark/load-100k.ts: main harness
- benchmark/lib/percentiles.ts: zero-dep pXX helper, nearest-rank
- benchmark/README.md: how to run, what gets measured, where results
land, and why p99 is the number you want for capacity planning
- benchmark/results/load-100k-96c0ed0.json: example result from a
small-N (N=1000, C=10) verification run against a fresh daemon
- package.json: wires `npm run bench:load`
- CHANGELOG.md: Unreleased entry + a Performance section placeholder
describing where per-release numbers should land going forward
Verified locally at BENCH_N=1000 BENCH_C=10 BENCH_OPS=200 — three
cells, zero errors, JSON written. Full 100k matrix is intentionally
deferred to CI/release time. Closes #346.")

 |  |
| 

[deploy](/rohitg00/agentmemory/tree/main/deploy "deploy")

 | 

[deploy](/rohitg00/agentmemory/tree/main/deploy "deploy")

 | 

[fix(coolify): use environment map syntax for Coolify v4 parser (](/rohitg00/agentmemory/commit/d271fb41cb8fa840cabb66e3d31cac38986627f5 "fix(coolify): use environment map syntax for Coolify v4 parser (#424)
Coolify v4's PHP-based docker-compose validator rejects the shorthand
environment list syntax ('- VAR' without =) with:
Error: non-string key in services.agentmemory.environment: 0
Switching to the map form with explicit variable substitution preserves
the original 'inherit from build env' behavior — Coolify still resolves
SERVICE_FQDN_AGENTMEMORY_3111 from the magic variable mechanism — while
satisfying the stricter parser.
Verified with:
SERVICE_FQDN_AGENTMEMORY_3111=https://example.com \
docker compose -f deploy/coolify/docker-compose.yml \
--project-directory deploy/coolify config
Tested live on a Coolify v4.0.0-beta.397 instance: deploy succeeds and
container reaches running:healthy on first try with this change.")[#424](https://github.com/rohitg00/agentmemory/pull/424)[)](/rohitg00/agentmemory/commit/d271fb41cb8fa840cabb66e3d31cac38986627f5 "fix(coolify): use environment map syntax for Coolify v4 parser (#424)
Coolify v4's PHP-based docker-compose validator rejects the shorthand
environment list syntax ('- VAR' without =) with:
Error: non-string key in services.agentmemory.environment: 0
Switching to the map form with explicit variable substitution preserves
the original 'inherit from build env' behavior — Coolify still resolves
SERVICE_FQDN_AGENTMEMORY_3111 from the magic variable mechanism — while
satisfying the stricter parser.
Verified with:
SERVICE_FQDN_AGENTMEMORY_3111=https://example.com \
docker compose -f deploy/coolify/docker-compose.yml \
--project-directory deploy/coolify config
Tested live on a Coolify v4.0.0-beta.397 instance: deploy succeeds and
container reaches running:healthy on first try with this change.")

 |  |
| 

[docs](/rohitg00/agentmemory/tree/main/docs "docs")

 | 

[docs](/rohitg00/agentmemory/tree/main/docs "docs")

 | 

[docs(pairings): stack agentmemory with codegraph + Understand Anythin…](/rohitg00/agentmemory/commit/ca0897504b3a47c2ebfdf6190396e50e415f1b96 "docs(pairings): stack agentmemory with codegraph + Understand Anything + Graphify (#641)
Adds docs/recipes/pairings.md walking through how agentmemory pairs with
three projects that ship the rest of the AI coding agent context layer:
- codegraph: pre-indexed code knowledge graph (MCP server)
- Understand Anything: multi-agent code-graph build + interactive dashboard
- Graphify: knowledge graph across code + docs + PDFs + images + videos
Doc includes a unified MCP config snippet, question-routing table mapping
question shapes to the right tool, install order for a new project, and
a pointer to eval/runner/adapters/ for anyone who wants to publish a
cross-project benchmark adapter.
Main README gets a one-line pointer to the recipe under the existing
benchmarks section.")

 |  |
| 

[eval](/rohitg00/agentmemory/tree/main/eval "eval")

 | 

[eval](/rohitg00/agentmemory/tree/main/eval "eval")

 | 

[feat(eval): pluggable benchmark harness with in-house coding-agent co…](/rohitg00/agentmemory/commit/7fb72f40108516e80979a4ebd142deab447d7aa9 "feat(eval): pluggable benchmark harness with in-house coding-agent corpus (#562)
* feat(eval): pluggable benchmark harness with in-house coding-agent corpus
Adds eval/ tree (outside files field so npm tarball stays thin) with Adapter
interface, three reference adapters (grep / vector / agentmemory-hybrid),
two benchmarks (LongMemEval _s public, coding-agent-life-v1 in-house 15
sessions), scoring (P@K, R@K, hit, top-gold-rank), NDJSON output,
sandbox script.
coding-agent-life-v1 published scorecard at
docs/benchmarks/2026-05-20-coding-agent-life-v1.md:
agentmemory-hybrid R@5=0.967 P@5=0.578 (100% hit) vs grep R@5=0.967 P@5=0.267.
2.2x better precision on identical input, sandbox-reproducible.
Adapter contract: init(sessions, config) -> State; query(q, state, k) -> RankedDoc[]
npm scripts:
npm run eval:coding-life (no download, no API key for grep)
npm run eval:longmemeval (needs OPENAI key + 278MB download)
eval/scripts/sandbox.sh boots clean agentmemory + iii-engine on ports
3411/3412 with isolated data dir; tears down on exit.
README headline updated. 1072/1072 tests pass + 5 new eval tests.
* fix(eval): address review findings on benchmark harness
- agentmemory adapter: prefer row.sessionId before observationToSession lookup
- vector adapter: validate embedBatch response (length, indexes, non-empty rows)
- coding-life: positive-int guard on --k; wrap query loop in try/finally so teardown runs
- longmemeval: positive-int guards on --k/--limit/--stratify; per-question try/finally
- load: throw on haystack_session_ids vs haystack_sessions length mismatch
- score: P@K denominator is k (requested cutoff) not topK.length
- sandbox.sh: guard rm -rf with non-empty + /tmp/ prefix check
- README: drop unsafe rm "$(which iii)"; instruct ~/.local/bin + PATH instead; add language tag to repo-layout fenced block
- sessions.json: fix "two-phase" -> "three-phase" wording mismatch")

 |  |
| 

[examples/ python](/rohitg00/agentmemory/tree/main/examples/python "This path skips through empty directories")

 | 

[examples/ python](/rohitg00/agentmemory/tree/main/examples/python "This path skips through empty directories")

 | 

[docs(python): iii-sdk example replaces standalone REST client (](/rohitg00/agentmemory/commit/f365d38c75e06752ef2681b11ca1fd2a70a3b0ab "docs(python): iii-sdk example replaces standalone REST client (#364)
Closes #342.
agentmemory functions register as mem::remember, mem::observe,
mem::context, mem::smart-search, mem::forget via sdk.registerFunction.
iii-sdk already ships in Python, Rust, and Node — any of them can call
those functions directly over the iii WebSocket transport. A standalone
Python REST client would duplicate the transport layer and fragment the
cross-language story.
This patch adds:
- examples/python/quickstart.py — minimal save + smart-search loop.
- examples/python/observe_and_recall.py — observation ingest + context
rendering at a token budget.
- examples/python/README.md — function map + install + usage.
- README "Programmatic access (Python / Rust / Node)" section pointing
at the example and the three SDK install commands.
REST on :3111 is unchanged for hosts without an iii runtime.")[#364](https://github.com/rohitg00/agentmemory/pull/364)[)](/rohitg00/agentmemory/commit/f365d38c75e06752ef2681b11ca1fd2a70a3b0ab "docs(python): iii-sdk example replaces standalone REST client (#364)
Closes #342.
agentmemory functions register as mem::remember, mem::observe,
mem::context, mem::smart-search, mem::forget via sdk.registerFunction.
iii-sdk already ships in Python, Rust, and Node — any of them can call
those functions directly over the iii WebSocket transport. A standalone
Python REST client would duplicate the transport layer and fragment the
cross-language story.
This patch adds:
- examples/python/quickstart.py — minimal save + smart-search loop.
- examples/python/observe_and_recall.py — observation ingest + context
rendering at a token budget.
- examples/python/README.md — function map + install + usage.
- README "Programmatic access (Python / Rust / Node)" section pointing
at the example and the three SDK install commands.
REST on :3111 is unchanged for hosts without an iii runtime.")

 |  |
|  |

[![agentmemory — Persistent memory for AI coding agents](/rohitg00/agentmemory/raw/main/assets/banner.png)](/rohitg00/agentmemory/blob/main/assets/banner.png)

**Your coding agent remembers everything. No more re-explaining. Built on [iii engine](https://github.com/iii-hq/iii)**

Persistent memory for Claude Code, GitHub Copilot CLI, Cursor, Gemini CLI, Codex CLI, Hermes, OpenClaw, pi, OpenCode, and any MCP client.

[English](/rohitg00/agentmemory/blob/main/README.md) | [简体中文](/rohitg00/agentmemory/blob/main/READMEs/README.zh-CN.md) | [繁體中文](/rohitg00/agentmemory/blob/main/READMEs/README.zh-TW.md) | [日本語](/rohitg00/agentmemory/blob/main/READMEs/README.ja-JP.md) | [한국어](/rohitg00/agentmemory/blob/main/READMEs/README.ko-KR.md) | [Español](/rohitg00/agentmemory/blob/main/READMEs/README.es-ES.md) | [Türkçe](/rohitg00/agentmemory/blob/main/READMEs/README.tr-TR.md) | [Русский](/rohitg00/agentmemory/blob/main/READMEs/README.ru-RU.md) | [हिन्दी](/rohitg00/agentmemory/blob/main/READMEs/README.hi-IN.md) | [Português](/rohitg00/agentmemory/blob/main/READMEs/README.pt-BR.md) | [Français](/rohitg00/agentmemory/blob/main/READMEs/README.fr-FR.md) | [Deutsch](/rohitg00/agentmemory/blob/main/READMEs/README.de-DE.md)

[![rohitg00/agentmemory | Trendshift](https://camo.githubusercontent.com/30f4b7d62f1b884b41ccdcf5605c30f3f8f99b39f3d85e882f277af57edea398/68747470733a2f2f7472656e6473686966742e696f2f6170692f62616467652f7265706f7369746f726965732f3235313233)](https://trendshift.io/repositories/25123)

[![Star History Chart](https://camo.githubusercontent.com/e60da4c7f18d7a5c028c39f8cf0f1385180010858e7f97ca9f75f373918b566e/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f63686172743f7265706f733d726f6869746730302f6167656e746d656d6f727926747970653d64617465266c6567656e643d746f702d6c656674)](https://www.star-history.com/?repos=rohitg00%2Fagentmemory&type=date&legend=top-left)

*The gist extends Karpathy's LLM Wiki pattern with confidence scoring, lifecycle, knowledge graphs, and hybrid search: agentmemory is the implementation.*

![95.2% retrieval R@5](/rohitg00/agentmemory/raw/main/assets/tags/stat-recall.svg) ![92% fewer tokens](/rohitg00/agentmemory/raw/main/assets/tags/stat-tokens.svg) ![53 MCP tools](/rohitg00/agentmemory/raw/main/assets/tags/stat-tools.svg) ![12 auto hooks](/rohitg00/agentmemory/raw/main/assets/tags/stat-hooks.svg) ![0 external DBs](/rohitg00/agentmemory/raw/main/assets/tags/stat-deps.svg) ![950+ tests passing](/rohitg00/agentmemory/raw/main/assets/tags/stat-tests.svg)

[![agentmemory demo](/rohitg00/agentmemory/raw/main/assets/demo.gif)](/rohitg00/agentmemory/blob/main/assets/demo.gif)

[Install](#install) • [Quick Start](#quick-start) • [Benchmarks](#benchmarks) • [vs Competitors](#vs-competitors) • [Agents](#works-with-every-agent) • [How It Works](#how-it-works) • [MCP](#mcp-server) • [Viewer](#real-time-viewer) • [iii Console](#iii-console) • [Powered by iii](#powered-by-iii) • [Config](#configuration) • [API](#api)

* * *

## Install

```
npm install -g @agentmemory/agentmemory # once — bare `agentmemory` on PATH
# If you hit EACCES on macOS/Linux system Node installs, retry with:
# sudo npm install -g @agentmemory/agentmemory
agentmemory # start the memory server on :3111
agentmemory demo # seed sample sessions + prove recall
agentmemory connect claude-code # wire MCP into your agent (also: copilot-cli, codex, cursor, gemini-cli, ...)
npx skills add rohitg00/agentmemory -y # install 8 native skills so your agent knows when to use the tools
```

Or via `npx` (no install):

```
npx @agentmemory/agentmemory
```

Heads-up — npx caches per version. If a bare `npx @agentmemory/agentmemory` serves an older release, force the latest with `npx -y @agentmemory/agentmemory@latest`, or clear the cache once with `rm -rf ~/.npm/_npx` (macOS/Linux; on Windows delete `%LOCALAPPDATA%\npm-cache\_npx`). The first npx run from v0.9.16+ prompts to install globally inline so the bare `agentmemory` command works everywhere afterwards.

Full options at [Quick Start](#quick-start) below. Agent-specific wiring at [Works with every agent](#works-with-every-agent).

* * *

agentmemory works with any agent that supports hooks, MCP, or REST API. All agents share the same memory server.

<table><tbody><tr><td align="center" width="12.5%"><a href="https://claude.com/product/claude-code"><img src="https://github.com/anthropics.png?size=120" alt="Claude Code" width="48" height="48"></a><br><strong>Claude Code</strong><br><sub>native plugin + 12 hooks + MCP</sub></td><td align="center" width="12.5%"><a href="https://github.com/openai/codex"><img src="https://github.com/openai.png?size=120" alt="Codex CLI" width="48" height="48"></a><br><strong>Codex CLI</strong><br><sub>native plugin + 6 hooks + MCP</sub></td><td align="center" width="12.5%"><a href="https://github.com/features/copilot"><img src="https://camo.githubusercontent.com/9528df2db3f308ed6ecd1cad432b477064250ccfe94a5ae4cc137ea91cce73bb/68747470733a2f2f6769746875622e6769746875626173736574732e636f6d2f696d616765732f6d6f64756c65732f736974652f636f70696c6f742f636f70696c6f742e706e67" alt="GitHub Copilot CLI" width="48" height="48"></a><br><strong>GitHub Copilot CLI</strong><br><sub>MCP + plugin hooks/skills</sub></td><td align="center" width="12.5%"><a href="/rohitg00/agentmemory/blob/main/integrations/openclaw"><img src="https://github.com/openclaw.png?size=120" alt="OpenClaw" width="48" height="48"></a><br><strong>OpenClaw</strong><br><sub>native plugin + MCP</sub></td><td align="center" width="12.5%"><a href="/rohitg00/agentmemory/blob/main/integrations/hermes"><img src="https://github.com/NousResearch.png?size=120" alt="Hermes" width="48" height="48"></a><br><strong>Hermes</strong><br><sub>native plugin + MCP</sub></td><td align="center" width="12.5%"><a href="/rohitg00/agentmemory/blob/main/integrations/pi"><img src="/rohitg00/agentmemory/raw/main/assets/agents/pi.svg" alt="pi" width="48" height="48"></a><br><strong>pi</strong><br><sub>native plugin + MCP</sub></td><td align="center" width="12.5%"><a href="https://github.com/tinyhumansai/openhuman"><img src="https://raw.githubusercontent.com/tinyhumansai/openhuman/main/app/src-tauri/icons/128x128.png" alt="OpenHuman" width="48" height="48"></a><br><strong>OpenHuman</strong><br><sub>native Memory trait backend</sub></td><td align="center" width="12.5%"><a href="https://cursor.com"><themed-picture><picture><img src="https://camo.githubusercontent.com/2ec79e0c43f28c05690973b98eeee08496d5bba56d1a52bdfca98da6e9cf8fea/68747470733a2f2f7376676c2e6170702f6c6962726172792f637572736f725f6c696768742e737667" alt="Cursor" width="48" height="48" srcset="https://camo.githubusercontent.com/2f31a92f3095b7cf6f83d01e574210fb237515952649ecdaee42a8069e8b970e/68747470733a2f2f7376676c2e6170702f6c6962726172792f637572736f725f6461726b2e737667"></picture></themed-picture></a><br><strong>Cursor</strong><br><sub>MCP server</sub></td><td align="center" width="12.5%"><a href="https://github.com/google-gemini/gemini-cli"><img src="https://github.com/google-gemini.png?size=120" alt="Gemini CLI" width="48" height="48"></a><br><strong>Gemini CLI</strong><br><sub>MCP server</sub></td></tr><tr><td align="center" width="12.5%"><a href="https://github.com/opencode-ai/opencode"><themed-picture><picture><img src="https://camo.githubusercontent.com/b69e9c448b9ad9a94b0b05a2e5db726df0ab5c26a85b18ceb996a78b93297573/68747470733a2f2f7376676c2e6170702f6c6962726172792f6f70656e636f64652e737667" alt="OpenCode" width="48" height="48" srcset="https://camo.githubusercontent.com/a23ad5f5d1c5c3df7e7036579ff536cf2c4f98d7c5905f54cd111bb7ded997ee/68747470733a2f2f7376676c2e6170702f6c6962726172792f6f70656e636f64652d6461726b2e737667"></picture></themed-picture></a><br><strong>OpenCode</strong><br><sub>22 hooks + MCP + plugin</sub></td><td align="center" width="12.5%"><a href="https://github.com/cline/cline"><img src="https://github.com/cline.png?size=120" alt="Cline" width="48" height="48"></a><br><strong>Cline</strong><br><sub>MCP server</sub></td><td align="center" width="12.5%"><a href="https://github.com/block/goose"><img src="https://github.com/block.png?size=120" alt="Goose" width="48" height="48"></a><br><strong>Goose</strong><br><sub>MCP server</sub></td><td align="center" width="12.5%"><a href="https://github.com/Kilo-Org/kilocode"><img src="https://github.com/Kilo-Org.png?size=120" alt="Kilo Code" width="48" height="48"></a><br><strong>Kilo Code</strong><br><sub>MCP server</sub></td><td align="center" width="12.5%"><a href="https://github.com/Aider-AI/aider"><img src="https://github.com/Aider-AI.png?size=120" alt="Aider" width="48" height="48"></a><br><strong>Aider</strong><br><sub>REST API</sub></td><td align="center" width="12.5%"><a href="https://claude.ai/download"><img src="https://github.com/anthropics.png?size=120" alt="Claude Desktop" width="48" height="48"></a><br><strong>Claude Desktop</strong><br><sub>MCP server</sub></td><td align="center" width="12.5%"><a href="https://windsurf.com"><themed-picture><picture><img src="https://camo.githubusercontent.com/4efeb2409587aaf51924724237d758782984d99580209a98c27fb3e78f79b8f9/68747470733a2f2f7376676c2e6170702f6c6962726172792f77696e64737572662d6c696768742e737667" alt="Windsurf" width="48" height="48" srcset="https://camo.githubusercontent.com/f81c5994c30bf7cd912f8611838e610a7c60557af179e71c4486da8d658c75ab/68747470733a2f2f7376676c2e6170702f6c6962726172792f77696e64737572662d6461726b2e737667"></picture></themed-picture></a><br><strong>Windsurf</strong><br><sub>MCP server</sub></td><td align="center" width="12.5%"><a href="https://github.com/RooCodeInc/Roo-Code"><img src="https://github.com/RooCodeInc.png?size=120" alt="Roo Code" width="48" height="48"></a><br><strong>Roo Code</strong><br><sub>MCP server</sub></td></tr><tr><td align="center" width="12.5%"><a href="https://www.warp.dev"><img src="https://github.com/warpdotdev.png?size=120" alt="Warp" width="48" height="48"></a><br><strong>Warp</strong><br><sub>connect + MCP + skills</sub></td></tr></tbody></table>

Works with **any** agent that speaks MCP or HTTP. One server, memories shared across all of them.

* * *

You explain the same architecture every session. You re-discover the same bugs. You re-teach the same preferences. Built-in memory (CLAUDE.md,.cursorrules) caps out at 200 lines and goes stale. agentmemory fixes this. It silently captures what your agent does, compresses it into searchable memory, and injects the right context when the next session starts. One command. Works across agents.

**What changes:** Session 1 you set up JWT auth. Session 2 you ask for rate limiting. The agent already knows your auth uses jose middleware in `src/middleware/auth.ts`, your tests cover token validation, and you chose jose over jsonwebtoken for Edge compatibility. No re-explaining. No copy-pasting. The agent just *knows*.

```
npx @agentmemory/agentmemory
```

> **New in v0.9.22** — Three new connect adapters (Qwen Code, Antigravity, Kiro), `AGENT_ID` multi-agent isolation with opt-in `AGENTMEMORY_AGENT_SCOPE=isolated` filtering, install ERESOLVE fixed, OpenAI thinking-model output handled, OpenCode auto-context + session creation, viewer graph settles on 1000+ nodes, 22 fixes total. Full notes in [CHANGELOG.md](/rohitg00/agentmemory/blob/main/CHANGELOG.md).

* * *

<table><tbody><tr><td width="50%"><h3 dir="auto">Retrieval Accuracy</h3><p dir="auto"><strong>coding-agent-life-v1</strong> (in-house corpus, sandbox-reproducible)</p><table><thead><tr><th>Adapter</th><th>P@5</th><th>R@5</th><th>Top-5 hit rate</th><th>p50 latency</th></tr></thead><tbody><tr><td><strong>agentmemory hybrid</strong></td><td><strong>0.578</strong></td><td><strong>0.967</strong></td><td><strong>15 / 15</strong></td><td>14 ms</td></tr><tr><td>grep baseline</td><td>0.267</td><td>0.967</td><td>15 / 15</td><td>0 ms</td></tr></tbody></table><p dir="auto">100% top-5 hit rate. <strong>2.2×</strong> better precision than the grep baseline on identical input. Full per-type breakdown: <a href="/rohitg00/agentmemory/blob/main/docs/benchmarks/2026-05-20-coding-agent-life-v1.md"><code>docs/benchmarks/2026-05-20-coding-agent-life-v1.md</code></a>.</p><p dir="auto"><strong>LongMemEval-S</strong> (ICLR 2025, 500 questions)</p><table><thead><tr><th>System</th><th>R@5</th><th>R@10</th><th>MRR</th></tr></thead><tbody><tr><td><strong>agentmemory</strong></td><td><strong>95.2%</strong></td><td><strong>98.6%</strong></td><td><strong>88.2%</strong></td></tr><tr><td>BM25-only fallback</td><td>86.2%</td><td>94.6%</td><td>71.5%</td></tr></tbody></table></td><td width="50%"><h3 dir="auto">Token Savings</h3><table><thead><tr><th>Approach</th><th>Tokens/yr</th><th>Cost/yr</th></tr></thead><tbody><tr><td>Paste full context</td><td>19.5M+</td><td>Impossible (exceeds window)</td></tr><tr><td>LLM-summarized</td><td>~650K</td><td>~$500</td></tr><tr><td><strong>agentmemory</strong></td><td><strong>~170K</strong></td><td><strong>~$10</strong></td></tr><tr><td>agentmemory + local embeddings</td><td>~170K</td><td><strong>$0</strong></td></tr></tbody></table></td></tr></tbody></table>

> Embedding model: `all-MiniLM-L6-v2` (local, free, no API key). Full reports: [`benchmark/LONGMEMEVAL.md`](/rohitg00/agentmemory/blob/main/benchmark/LONGMEMEVAL.md), [`benchmark/QUALITY.md`](/rohitg00/agentmemory/blob/main/benchmark/QUALITY.md), [`benchmark/SCALE.md`](/rohitg00/agentmemory/blob/main/benchmark/SCALE.md). Competitor comparison: [`benchmark/COMPARISON.md`](/rohitg00/agentmemory/blob/main/benchmark/COMPARISON.md) — agentmemory vs mem0, Letta, Khoj, claude-mem, Hippo.

**Reproduce locally:**[`eval/README.md`](/rohitg00/agentmemory/blob/main/eval/README.md) — adapter-pluggable harness for LongMemEval `_s` (public 500-Q) + `coding-agent-life-v1` (in-house 15-session corpus). Grep / vector / agentmemory adapters score side-by-side, NDJSON output, published scorecards land in [`docs/benchmarks/`](/rohitg00/agentmemory/blob/main/docs/benchmarks).

**Pairs with [codegraph](https://github.com/colbymchenry/codegraph), [Understand Anything](https://github.com/Lum1104/Understand-Anything), and [Graphify](https://github.com/safishamsi/graphify).** Code-graph indexing, multi-agent build pipelines, and broader knowledge graphs across docs / PDFs / images / videos. agentmemory remembers the work; those three projects light up the rest of the context layer. Recipes + question-routing table: [`docs/recipes/pairings.md`](/rohitg00/agentmemory/blob/main/docs/recipes/pairings.md).

* * *

|  | agentmemory | mem0 (53K ⭐) | Letta / MemGPT (22K ⭐) | Built-in (CLAUDE.md) |
| --- | --- | --- | --- | --- |
| **Type** | Memory engine + MCP server | Memory layer API | Full agent runtime | Static file |
| **Retrieval R@5** | **95.2%** | 68.5% (LoCoMo) | 83.2% (LoCoMo) | N/A (grep) |
| **Auto-capture** | 12 hooks (zero manual effort) | Manual `add()` calls | Agent self-edits | Manual editing |
| **Search** | BM25 + Vector + Graph (RRF fusion) | Vector + Graph | Vector (archival) | Loads everything into context |
| **Multi-agent** | MCP + REST + leases + signals | API (no coordination) | Within Letta runtime only | Per-agent files |
| **Framework lock-in** | None (any MCP client) | None | High (must use Letta) | Per-agent format |
| **External deps** | None (SQLite + iii-engine) | Qdrant / pgvector | Postgres + vector DB | None |
| **Memory lifecycle** | 4-tier consolidation + decay + auto-forget | Passive extraction | Agent-managed | Manual pruning |
| **Token efficiency** | ~1,900 tokens/session ($10/yr) | Varies by integration | Core memory in context | 22K+ tokens at 240 obs |
| **Real-time viewer** | Yes (port 3113) | Cloud dashboard | Cloud dashboard | No |
| **Self-hosted** | Yes (default) | Optional | Optional | Yes |

* * *

Compatibility: this release targets stable `iii-sdk` `^0.11.0` and iii-engine v0.11.x.

```
# Terminal 1: start the server
npx @agentmemory/agentmemory

# Terminal 2: seed sample data and see recall in action
npx @agentmemory/agentmemory demo
```

`demo` seeds 3 realistic sessions (JWT auth, N+1 query fix, rate limiting) and runs semantic searches against them. You'll see it find "N+1 query fix" when you search "database performance optimization" — keyword matching can't do that.

Open `http://localhost:3113` to watch the memory build live.

`npx` caches per-version. If you ran `npx @agentmemory/agentmemory@0.9.14` last week, a bare `npx @agentmemory/agentmemory` may serve the stale 0.9.14 from `~/.npm/_npx/`, not the latest release. Install once and the bare `agentmemory` command works everywhere:

```
npm install -g @agentmemory/agentmemory
# If you hit EACCES on macOS/Linux system Node installs, retry with:
# sudo npm install -g @agentmemory/agentmemory
agentmemory # start the server (same as the npx form)
agentmemory stop # tear it down
agentmemory remove # uninstall everything we created
agentmemory connect claude-code # wire one agent
agentmemory doctor # interactive diagnostics + fix prompts
```

From v0.9.16 onward, the first npx run prompts you to install globally inline — answer `Y` once and you're set. If you skip, fall back to either of these for a fresh fetch:

```
npx -y @agentmemory/agentmemory@latest # forces latest from npm (cross-platform)
rm -rf ~/.npm/_npx && npx @agentmemory/agentmemory # macOS/Linux only (POSIX shell)
```

On Windows / PowerShell, the equivalent cache clear is `Remove-Item -Recurse -Force "$env:LOCALAPPDATA\npm-cache\_npx"` — the `npx -y ...@latest` form above is the cross-platform option.

### Session Replay

Every session agentmemory records is replayable. Open the viewer, pick the **Replay** tab, and scrub through the timeline: prompts, tool calls, tool results, and responses render as discrete events with play/pause, speed control (0.5×–4×), and keyboard shortcuts (space to toggle, arrows to step).

Already have older Claude Code JSONL transcripts you want to bring in?

```
# Import everything under the default ~/.claude/projects
npx @agentmemory/agentmemory import-jsonl

# Or import a single file
npx @agentmemory/agentmemory import-jsonl ~/.claude/projects/-my-project/abc123.jsonl
```

Imported sessions show up in the Replay picker alongside native ones. Under the hood each entry routes through the `mem::replay::load`, `mem::replay::sessions`, and `mem::replay::import-jsonl` iii functions — no side-channel servers.

Use the maintenance command when you intentionally want to update your local runtime:

```
npx @agentmemory/agentmemory upgrade
```

Warning: this command mutates the current workspace/runtime. It can update JavaScript dependencies, may run `cargo install iii-engine --force`, and may pull Docker images.

Implementation details live in `src/cli.ts` (see `runUpgrade` around the `src/cli.ts:544-595` region).

```
Install agentmemory: run `npx @agentmemory/agentmemory` in a separate terminal to start the memory server. Then run `/plugin marketplace add rohitg00/agentmemory` and `/plugin install agentmemory` — the plugin registers all 12 hooks, 8 skills, AND auto-wires the `@agentmemory/mcp` stdio server via its `.mcp.json`, so you get 53 MCP tools (memory_smart_search, memory_save, memory_sessions, memory_governance_delete, etc.) without any extra config step. Verify with `curl http://localhost:3111/agentmemory/health`. The real-time viewer is at http://localhost:3113.
```

If you wire agentmemory's MCP server through `~/.claude.json` directly instead of using `/plugin install`, Claude Code never resolves `${CLAUDE_PLUGIN_ROOT}` and you have to point hook scripts at absolute paths in `~/.claude/settings.json`. Those paths typically embed the agentmemory version (e.g. `~/.codex/plugins/cache/agentmemory/agentmemory/0.9.22/scripts/…`), so the next upgrade silently breaks every hook ([#508](https://github.com/rohitg00/agentmemory/issues/508)).

Workaround:

```
agentmemory connect claude-code --with-hooks
```

This merges the same hook commands into `~/.claude/settings.json` with absolute paths resolved to the bundled `plugin/` directory of the currently installed `@agentmemory/agentmemory` package. Re-run the command after upgrading agentmemory to refresh the paths. User entries in the same file are preserved; only previous agentmemory entries are replaced. Using the `/plugin install` path remains the recommended approach. For remote or protected deployments, launch Claude Code with `AGENTMEMORY_URL` and `AGENTMEMORY_SECRET` set. The plugin passes both values through to its bundled MCP server; when `AGENTMEMORY_URL` is empty, the MCP shim uses `http://localhost:3111`.

The Codex plugin ships from the same `plugin/` directory as the Claude Code plugin. It registers:

- `@agentmemory/mcp` as an MCP server (proxies all 53 tools when `AGENTMEMORY_URL` points at a running agentmemory server; falls back to 7 tools locally when no server is reachable)
- 6 lifecycle hooks: `SessionStart`, `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `PreCompact`, `Stop`
- 8 skills: `/recall`, `/remember`, `/session-history`, `/forget`, `/recap`, `/handoff`, `/commit-context`, `/commit-history`

Codex's hook engine injects `CLAUDE_PLUGIN_ROOT` into hook subprocesses (per [`codex-rs/hooks/src/engine/discovery.rs`](https://github.com/openai/codex/blob/main/codex-rs/hooks/src/engine/discovery.rs)), so the same hook scripts work across both hosts without duplication. Subagent / SessionEnd / Notification / TaskCompleted / PostToolUseFailure events are Claude-Code-only and are not registered for Codex.

`CodexHooks` and `PluginHooks` are both stable + default-enabled in [`codex-rs/features/src/lib.rs`](https://github.com/openai/codex/blob/main/codex-rs/features/src/lib.rs), but Codex Desktop builds currently do not dispatch plugin-local `hooks.json` ([openai/codex#16430](https://github.com/openai/codex/issues/16430)). MCP tools still work; only the lifecycle observations are missing.

Until upstream lands the fix, mirror the same hook commands into the global `~/.codex/hooks.json`:

```
agentmemory connect codex --with-hooks
```

This adds an idempotent block to `~/.codex/hooks.json` referencing absolute paths to the bundled scripts (no `${CLAUDE_PLUGIN_ROOT}` expansion needed at user-scope). Re-run the same command after upgrading agentmemory to refresh paths. User entries in the same file are preserved; only previous agentmemory entries are replaced.

```
# MCP-only wiring
agentmemory connect copilot-cli

# Full hooks/skills plugin from the GitHub subdir
copilot plugin install rohitg00/agentmemory:plugin
```

`agentmemory connect copilot-cli` merges `mcpServers.agentmemory` into `~/.copilot/mcp-config.json` (or `$COPILOT_HOME/mcp-config.json` when `COPILOT_HOME` is set) and preserves existing servers. This adapter is Windows-safe even though other `connect` adapters still require manual Windows setup. Copilot picks up the MCP server on next launch or after `/mcp`. Install the plugin as well when you want the full hook/skill experience.

**OpenClaw (paste this prompt)**

```
Install agentmemory for OpenClaw. Run `npx @agentmemory/agentmemory` in a separate terminal to start the memory server on localhost:3111. Then add this to my OpenClaw MCP config so agentmemory is available with all 53 memory tools:

{
  "mcpServers": {
 "agentmemory": {
 "command": "npx",
 "args": ["-y", "@agentmemory/mcp"],
 "env": {
 "AGENTMEMORY_URL": "http://localhost:3111"
 }
 }
  }
}

Restart OpenClaw. Verify with `curl http://localhost:3111/agentmemory/health`. Open http://localhost:3113 for the real-time viewer. For deeper memory-slot integration, copy `integrations/openclaw` to `~/.openclaw/extensions/agentmemory` and enable `plugins.slots.memory = "agentmemory"` in `~/.openclaw/openclaw.json`.
```

Full guide: [`integrations/openclaw/`](/rohitg00/agentmemory/blob/main/integrations/openclaw)

**Hermes Agent (paste this prompt)**

```
Install agentmemory for Hermes. Run `npx @agentmemory/agentmemory` in a separate terminal to start the memory server on localhost:3111. Then add this to ~/.hermes/config.yaml so Hermes can use agentmemory as an MCP server with all 53 memory tools:

mcp_servers:
  agentmemory:
 command: npx
 args: ["-y", "@agentmemory/mcp"]

memory:
  provider: agentmemory

Verify with `curl http://localhost:3111/agentmemory/health`. Open http://localhost:3113 for the real-time viewer. For deeper 6-hook memory provider integration (pre-LLM context injection, turn capture, MEMORY.md mirroring, system prompt block), copy integrations/hermes from the agentmemory repo to ~/.hermes/plugins/agentmemory.
```

Full guide: [`integrations/hermes/`](/rohitg00/agentmemory/blob/main/integrations/hermes)

### Other agents

Start the memory server: `npx @agentmemory/agentmemory`

agentmemory ships 8 skills (`remember`, `recall`, `recap`, `handoff`, `forget`, `commit-context`, `commit-history`, `session-history`) in the Claude-Code-style `<dir>/SKILL.md` format. The [`skills`](https://npmjs.com/package/skills) CLI by vercel-labs auto-installs them into the calling agent's native skill directory across 50+ agents (Claude Code, Cursor, Cline, Continue, Droid, Warp, Codex, Antigravity, Kiro, OpenCode, Goose, Roo, Trae, Windsurf, and more):

```
npx skills add rohitg00/agentmemory -y # auto-detects the calling agent
npx skills add rohitg00/agentmemory -y -a warp  # explicit agent
npx skills add rohitg00/agentmemory -y -a '*' # install to every installed agent
```

This is **complementary** to `agentmemory connect <agent>`:

- `agentmemory connect <agent>` writes the MCP server config so the tools are available.
- `npx skills add rohitg00/agentmemory` installs the skills so the agent knows when to call them.

For the few agents the skills CLI doesn't cover yet (Zed v1.3.x and below), drop the 8 SKILL.md files under the agent's native skill directory yourself — same format works everywhere.

The agentmemory entry is the **same MCP server block** across every host that uses the `mcpServers` shape (Cursor, Claude Desktop, Cline, Roo Code, Windsurf, Gemini CLI, OpenClaw):

```
"agentmemory": {
  "command": "npx",
  "args": ["-y", "@agentmemory/mcp"],
  "env": {
 "AGENTMEMORY_URL": "${AGENTMEMORY_URL}",
 "AGENTMEMORY_SECRET": "${AGENTMEMORY_SECRET}"
  }
}
```

**Merge this entry into the existing `mcpServers` object** in the host's config file — don't replace the file. If the file already has other servers, add `agentmemory` next to them as another key inside `mcpServers`. If `mcpServers` is missing entirely, paste the block inside `{ "mcpServers": { ... } }`. The `${VAR}` placeholders inherit `AGENTMEMORY_URL` / `AGENTMEMORY_SECRET` from the shell at MCP-server launch — unset vars pass empty strings and the shim falls back to `http://localhost:3111`. One wired entry covers both local and remote (k8s / reverse-proxied) deployments.

| Agent | Config file | Notes |
| --- | --- | --- |
| **Cursor** | `~/.cursor/mcp.json` | Merge into `mcpServers`. One-click deeplink also available on the website. |
| **Claude Desktop** | `claude_desktop_config.json` (Application Support) | Merge into `mcpServers`. Restart Claude Desktop after editing. |
| **Cline / Roo Code / Kilo Code** | Cline MCP settings (Settings UI → MCP Servers → Edit) | Same `mcpServers` block. |
| **Windsurf** | `~/.codeium/windsurf/mcp_config.json` | Same `mcpServers` block. |
| **Gemini CLI** | `~/.gemini/settings.json` | `gemini mcp add agentmemory npx -y @agentmemory/mcp --scope user` (auto-merges). |
| **GitHub Copilot CLI (MCP only)** | `~/.copilot/mcp-config.json` | `agentmemory connect copilot-cli` merges `mcpServers.agentmemory`; Copilot picks it up on next launch or `/mcp`. |
| **GitHub Copilot CLI (full plugin)** | Copilot plugin install | `copilot plugin install rohitg00/agentmemory:plugin` for the plugin from the GitHub subdir. |
| **OpenClaw** | OpenClaw MCP config | Same `mcpServers` block, or use the deeper [memory plugin](/rohitg00/agentmemory/blob/main/integrations/openclaw). |
| **Codex CLI (MCP only)** | `.codex/config.toml` | TOML shape: `codex mcp add agentmemory -- npx -y @agentmemory/mcp`, or add `[mcp_servers.agentmemory]` manually. |
| **Codex CLI (full plugin)** | Codex plugin marketplace | `codex plugin marketplace add rohitg00/agentmemory` then `codex plugin add agentmemory@agentmemory`. Registers MCP + 6 lifecycle hooks (SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, PreCompact, Stop) + 8 skills. On Codex Desktop, also run `agentmemory connect codex --with-hooks` until [openai/codex#16430](https://github.com/openai/codex/issues/16430) lands — plugin hooks are currently silent there. |
| **OpenCode (MCP only)** | `opencode.json` | Different shape — top-level `mcp` key, command as array: `{"mcp": {"agentmemory": {"type": "local", "command": ["npx", "-y", "@agentmemory/mcp"], "enabled": true}}}`. |
| **OpenCode (full plugin)** | `plugin/opencode/` | 22 auto-capture hooks covering session lifecycle, messages, tools, errors. Two slash commands (`/recall`, `/remember`). Copy `plugin/opencode/` into your OpenCode workspace and add the plugin entry to `opencode.json`. See [`plugin/opencode/README.md`](/rohitg00/agentmemory/blob/main/plugin/opencode/README.md) for the full hook table + gap analysis. |
| **pi** | `~/.pi/agent/extensions/agentmemory` | Copy [`integrations/pi`](/rohitg00/agentmemory/blob/main/integrations/pi) and restart pi. |
| **Hermes Agent** | `~/.hermes/config.yaml` | Use the deeper [memory provider plugin](/rohitg00/agentmemory/blob/main/integrations/hermes) with `memory.provider: agentmemory`. |
| **Qwen Code** | `~/.qwen/settings.json` | `agentmemory connect qwen` writes the standard `mcpServers` block. Hook payload is field-compatible with Claude Code, so the existing 12-hook scripts work without modification — wire them via the `hooks` section in the same `settings.json`. |
| **Antigravity** (replaces Gemini CLI) | `mcp_config.json` (in Antigravity's User dir) | `agentmemory connect antigravity` writes the standard `mcpServers` block. macOS: `~/Library/Application Support/Antigravity/User/`. Linux: `~/.config/Antigravity/User/`. Use after the 2026-06-18 Gemini CLI sunset. |
| **Kiro** | `~/.kiro/settings/mcp.json` | `agentmemory connect kiro` writes the user-level config. Workspace overrides go in `.kiro/settings/mcp.json` next to your code. |
| **Warp** | `~/.warp/.mcp.json` | `agentmemory connect warp` writes the standard `mcpServers` block. Warp also auto-discovers skills from `.claude/skills/` — once the Claude Code plugin is installed the 8 agentmemory skills (`remember`, `recall`, `recap`, `handoff`, `forget`, `commit-context`, `commit-history`, `session-history`) appear natively in Warp's slash-command palette. |
| **Cline (CLI)** | `~/.cline/mcp.json` | `agentmemory connect cline` writes the standard `mcpServers` block. VS Code extension users: paste the same block via Cline Settings → MCP Servers → Edit JSON. |
| **Continue.dev** | `~/.continue/config.yaml` (preferred) or `config.json` (legacy) | `agentmemory connect continue` creates `config.yaml` from scratch when neither exists, or modifies existing `config.json`. **If you already have `config.yaml`** the adapter prints the exact block to paste under `mcpServers:` — it won't silently rewrite your yaml because preserving comments and anchors safely needs a YAML parser the package doesn't ship. Continue uses array form (not object) for `mcpServers`. |
| **Zed** | `~/.config/zed/settings.json` | `agentmemory connect zed` writes under `context_servers` (Zed's key, NOT `mcpServers`). Remote MCP servers can be wired via `{"url": "..."}` instead. |
| **Droid (Factory.ai)** | `~/.factory/mcp.json` | `agentmemory connect droid` writes the standard `mcpServers` block. Project-scoped overrides go in `<repo>/.factory/mcp.json`. The `/mcp` slash command inside droid lists configured servers. |
| **Goose** | Goose MCP settings UI | Same `mcpServers` block — use `goose configure` → Add Extension → MCP. Direct YAML edit at `~/.config/goose/config.yaml` is supported but the schema uses `extensions:` + `cmd` (not `mcpServers:` + `command`). |
| **Aider** | n/a | Talk to the REST API directly: `curl -X POST http://localhost:3111/agentmemory/smart-search -d '{"query": "auth"}'`. |
| **Any agent (32+)** | n/a | `npx skillkit install agentmemory` auto-detects the host and merges. |

**Sandboxed MCP clients** (Flatpak / Snap / restrictive containers) that can't reach the host's `localhost`: also set `"AGENTMEMORY_FORCE_PROXY": "1"` in the `env` block, and point `AGENTMEMORY_URL` at a route the sandbox can actually reach (e.g. your LAN IP). See [#234](https://github.com/rohitg00/agentmemory/issues/234) for the diagnostic walkthrough.

agentmemory registers its core operations as iii functions (`mem::remember`, `mem::observe`, `mem::context`, `mem::smart-search`, `mem::forget`). Any language with an iii SDK can call them directly over `ws://localhost:49134` — no separate REST client per language.

```
pip install iii-sdk # Python
cargo add iii-sdk # Rust
npm  install iii-sdk # Node
```

Worked example: [`examples/python/`](/rohitg00/agentmemory/blob/main/examples/python) (quickstart + observation/recall flow). REST on `:3111` remains available for hosts without an iii runtime.

### From source

```
git clone https://github.com/rohitg00/agentmemory.git && cd agentmemory
npm install && npm run build && npm start
```

This starts agentmemory with a local `iii-engine` if `iii` is already installed, or falls back to Docker Compose if Docker is available. REST, streams, and the viewer bind to `127.0.0.1` by default.

Install `iii-engine` manually. **agentmemory currently pins `iii-engine` to `v0.11.2`** — `v0.11.6` introduces a new sandbox-everything-via- `iii worker add` model that agentmemory hasn't been refactored for yet. Pin lifts once the refactor lands. Override with `AGENTMEMORY_III_VERSION=<version>` if you've migrated to the sandbox model manually.

- **macOS arm64:**`mkdir -p ~/.local/bin && curl -fsSL https://github.com/iii-hq/iii/releases/download/iii/v0.11.2/iii-aarch64-apple-darwin.tar.gz | tar -xz -C ~/.local/bin && chmod +x ~/.local/bin/iii`
- **macOS x64:** swap `aarch64-apple-darwin` for `x86_64-apple-darwin`
- **Linux x64:** swap for `x86_64-unknown-linux-gnu`
- **Linux arm64:** swap for `aarch64-unknown-linux-gnu`
- **Windows:** download `iii-x86_64-pc-windows-msvc.zip` from , extract `iii.exe`, add to PATH

Or use Docker (the bundled `docker-compose.yml` pulls `iiidev/iii:0.11.2`). Full docs: [iii.dev/docs](https://iii.dev/docs).

### Windows

agentmemory runs on Windows 10/11, but the Node.js package alone isn't enough — you also need the `iii-engine` runtime (a separate native binary) as a background process. The official upstream installer is a `sh` script and there is no PowerShell installer or scoop/winget package today, so Windows users have two paths:

**Option A — Prebuilt Windows binary (recommended):**

```
# 1. Open https://github.com/iii-hq/iii/releases/tag/iii%2Fv0.11.2 in your browser
# (we pin to v0.11.2 until agentmemory refactors for the new sandbox
# model that engine v0.11.6+ requires)
# 2. Download iii-x86_64-pc-windows-msvc.zip
# (or iii-aarch64-pc-windows-msvc.zip if you're on an ARM machine)
# 3. Extract iii.exe somewhere on PATH, or place it at:
# %USERPROFILE%\.local\bin\iii.exe
# (agentmemory checks that location automatically)
# 4. Verify:
iii --version
# Should print: 0.11.2

# 5. Then run agentmemory as usual:
npx -y @agentmemory/agentmemory
```

**Option B — Docker Desktop:**

```
# 1. Install Docker Desktop for Windows
# 2. Start Docker Desktop and make sure the engine is running
# 3. Run agentmemory — it will auto-start the bundled compose file:
npx -y @agentmemory/agentmemory
```

**Option C — standalone MCP only (no engine):** if you only need the MCP tools for your agent and don't need the REST API, viewer, or cron jobs, skip the engine entirely:

```
npx -y @agentmemory/agentmemory mcp
# or via the shim package:
npx -y @agentmemory/mcp
```

**Diagnostics for Windows:** if `npx @agentmemory/agentmemory` fails, re-run with `--verbose` to see the actual engine stderr. Common failure modes:

| Symptom | Fix |
| --- | --- |
| `iii-engine process started` then `did not become ready within 15s` | Engine crashed on startup — re-run with `--verbose`, check stderr |
| `Could not start iii-engine` | Neither `iii.exe` nor Docker is installed. See Option A or B above |
| Port conflict | `netstat -ano | findstr :3111` to see what's bound, then kill it or use `--port <N>` |
| Docker fallback skipped even though Docker is installed | Make sure Docker Desktop is actually running (system tray icon) |

> Note: there is no `cargo install iii-engine` — `iii` is not published to crates.io. The only supported install methods are the prebuilt binary above, the upstream `sh` install script (macOS/Linux only), and the Docker image.

* * *

## Deploy

One-click templates for managed hosts. Each one ships a self-contained Dockerfile that pulls `@agentmemory/agentmemory` from npm and copies the iii engine binary in from the official `iiidev/iii` Docker Hub image — no pre-built agentmemory image required. Persistent storage mounts at `/data`; the first-boot entrypoint overwrites the npm-bundled iii config (which binds `127.0.0.1`) with a deploy-tuned one that binds `0.0.0.0` and uses absolute `/data` paths, generates the HMAC secret, then drops privileges from `root` to `node` via `gosu` before exec'ing the agentmemory CLI.

Render's one-click deploy button requires `render.yaml` at the repository root, which we deliberately keep clean. Use the Render Blueprint flow documented in [`deploy/render/`](/rohitg00/agentmemory/blob/main/deploy/render/README.md) to point at the in-repo blueprint manually.

Full setup details (HMAC capture, viewer SSH tunnel, rotation, backup, cost floors) live in [`deploy/`](/rohitg00/agentmemory/blob/main/deploy/README.md):

- [`deploy/fly`](/rohitg00/agentmemory/blob/main/deploy/fly/README.md) — single machine with `auto_stop_machines = "stop"`; cheapest idle.
- [`deploy/railway`](/rohitg00/agentmemory/blob/main/deploy/railway/README.md) — Hobby plan flat fee, volume in the dashboard.
- [`deploy/render`](/rohitg00/agentmemory/blob/main/deploy/render/README.md) — Blueprint flow, automatic disk snapshots on paid plans.
- [`deploy/coolify`](/rohitg00/agentmemory/blob/main/deploy/coolify/README.md) — self-hosted on your own VPS via [Coolify](https://coolify.io/self-hosted); same Docker Compose stack, you own the host and the data.

Only port `3111` is published. The viewer on `3113` stays bound to loopback inside the container — every template's README documents the SSH-tunnel pattern for reaching it.

* * *

Every coding agent forgets everything when the session ends. You waste the first 5 minutes of every session re-explaining your stack. agentmemory runs in the background and eliminates that entirely.

```
Session 1: "Add auth to the API"
  Agent writes code, runs tests, fixes bugs
  agentmemory silently captures every tool use
  Session ends -> observations compressed into structured memory

Session 2: "Now add rate limiting"
  Agent already knows:
 - Auth uses JWT middleware in src/middleware/auth.ts
 - Tests in test/auth.test.ts cover token validation
 - You chose jose over jsonwebtoken for Edge compatibility
  Zero re-explaining. Starts working immediately.
```

Every AI coding agent ships with built-in memory — Claude Code has `MEMORY.md`, Cursor has notepads, Cline has memory bank. These work like sticky notes. agentmemory is the searchable database behind the sticky notes.

|  | Built-in (CLAUDE.md) | agentmemory |
| --- | --- | --- |
| Scale | 200-line cap | Unlimited |
| Search | Loads everything into context | BM25 + vector + graph (top-K only) |
| Token cost | 22K+ at 240 observations | ~1,900 tokens (92% less) |
| Cross-agent | Per-agent files | MCP + REST (any agent) |
| Coordination | None | Leases, signals, actions, routines |
| Observability | Read files manually | Real-time viewer on:3113 |

* * *

### Memory Pipeline

```
PostToolUse hook fires
  -> SHA-256 dedup (5min window)
  -> Privacy filter (strip secrets, API keys)
  -> Store raw observation
  -> LLM compress -> structured facts + concepts + narrative
  -> Vector embedding (6 providers + local)
  -> Index in BM25 + vector

Stop / SessionEnd hook fires
  -> Summarize session
  -> Knowledge graph extraction (if GRAPH_EXTRACTION_ENABLED=true)
  -> Slot reflection (if SLOT_REFLECT_ENABLED=true)

SessionStart hook fires
  -> Load project profile (top concepts, files, patterns)
  -> Hybrid search (BM25 + vector + graph)
  -> Token budget (default: 2000 tokens)
  -> Inject into conversation
```

Inspired by how human brains process memory — not unlike sleep consolidation.

| Tier | What | Analogy |
| --- | --- | --- |
| **Working** | Raw observations from tool use | Short-term memory |
| **Episodic** | Compressed session summaries | "What happened" |
| **Semantic** | Extracted facts and patterns | "What I know" |
| **Procedural** | Workflows and decision patterns | "How to do it" |

Memories decay over time (Ebbinghaus curve). Frequently accessed memories strengthen. Stale memories auto-evict. Contradictions are detected and resolved.

| Hook | Captures |
| --- | --- |
| `SessionStart` | Project path, session ID |
| `UserPromptSubmit` | User prompts (privacy-filtered) |
| `PreToolUse` | File access patterns + enriched context |
| `PostToolUse` | Tool name, input, output |
| `PostToolUseFailure` | Error context |
| `PreCompact` | Re-injects memory before compaction |
| `SubagentStart/Stop` | Sub-agent lifecycle |
| `Stop` | End-of-session summary |
| `SessionEnd` | Session complete marker |

### Key Capabilities

| Capability | Description |
| --- | --- |
| **Automatic capture** | Every tool use recorded via hooks — zero manual effort |
| **Semantic search** | BM25 + vector + knowledge graph with RRF fusion |
| **Memory evolution** | Versioning, supersession, relationship graphs |
| **Auto-forgetting** | TTL expiry, contradiction detection, importance eviction |
| **Privacy first** | API keys, secrets, `<private>` tags stripped before storage |
| **Self-healing** | Circuit breaker, provider fallback chain, health monitoring |
| **Claude bridge** | Bi-directional sync with MEMORY.md |
| **Knowledge graph** | Entity extraction + BFS traversal |
| **Team memory** | Namespaced shared + private across team members |
| **Citation provenance** | Trace any memory back to source observations |
| **Git snapshots** | Version, rollback, and diff memory state |

* * *

Triple-stream retrieval combining three signals:

| Stream | What it does | When |
| --- | --- | --- |
| **BM25** | Stemmed keyword matching with synonym expansion | Always on |
| **Vector** | Cosine similarity over dense embeddings | Embedding provider configured |
| **Graph** | Knowledge graph traversal via entity matching | Entities detected in query |

Fused with Reciprocal Rank Fusion (RRF, k=60) and session-diversified (max 3 results per session).

BM25 tokenizes Greek, Cyrillic, Hebrew, Arabic, and accented Latin out of the box. For Chinese / Japanese / Korean memories, install the optional segmenters (`npm install @node-rs/jieba tiny-segmenter`) to split CJK runs into word-level tokens; without them, agentmemory soft-falls to whole-run tokenization and prints a one-time hint on stderr.

### Embedding providers

agentmemory auto-detects your provider. For best results, install local embeddings (free):

```
npm install @xenova/transformers
```

| Provider | Model | Cost | Notes |
| --- | --- | --- | --- |
| **Local (recommended)** | `all-MiniLM-L6-v2` | Free | Offline, +8pp recall over BM25-only |
| Gemini | `gemini-embedding-001` | Free tier | 100+ languages, 768/1536/3072 dims (MRL), 2048-token input. Replaces `text-embedding-004` ([deprecated, shutdown Jan 14, 2026](https://ai.google.dev/gemini-api/docs/deprecations)) |
| OpenAI | `text-embedding-3-small` | $0.02/1M | Highest quality |
| Voyage AI | `voyage-code-3` | Paid | Optimized for code |
| Cohere | `embed-english-v3.0` | Free trial | General purpose |
| OpenRouter | Any model | Varies | Multi-model proxy |

* * *

53 tools, 6 resources, 3 prompts, and 8 skills — the most comprehensive MCP memory toolkit for any agent.

> **MCP shim vs full server:** the published `@agentmemory/mcp` package is a thin shim. It exposes the full 53-tool surface **only when it can reach a running agentmemory server** via `AGENTMEMORY_URL` (proxy mode). With no server reachable, the shim falls back to a 7-tool local set (`memory_save`, `memory_recall`, `memory_smart_search`, `memory_sessions`, `memory_export`, `memory_audit`, `memory_governance_delete`). The `AGENTMEMORY_TOOLS=core|all` env var is a *server-side* flag — setting it in the shim's `env` block has no effect. If you see only 7 tools in Cursor / OpenCode / Gemini CLI, start `npx @agentmemory/agentmemory` (or the Docker stack) and set `AGENTMEMORY_URL=http://localhost:3111`.

### 53 Tools

Core tools (always available)

| Tool | Description |
| --- | --- |
| `memory_recall` | Search past observations |
| `memory_compress_file` | Compress markdown files while preserving structure |
| `memory_save` | Save an insight, decision, or pattern |
| `memory_patterns` | Detect recurring patterns |
| `memory_smart_search` | Hybrid semantic + keyword search |
| `memory_file_history` | Past observations about specific files |
| `memory_sessions` | List recent sessions |
| `memory_timeline` | Chronological observations |
| `memory_profile` | Project profile (concepts, files, patterns) |
| `memory_export` | Export all memory data |
| `memory_relations` | Query relationship graph |

Extended tools (53 total — set AGENTMEMORY\_TOOLS=all)

| Tool | Description |
| --- | --- |
| `memory_patterns` | Detect recurring patterns |
| `memory_timeline` | Chronological observations |
| `memory_relations` | Query relationship graph |
| `memory_graph_query` | Knowledge graph traversal |
| `memory_consolidate` | Run 4-tier consolidation |
| `memory_claude_bridge_sync` | Sync with MEMORY.md |
| `memory_team_share` | Share with team members |
| `memory_team_feed` | Recent shared items |
| `memory_audit` | Audit trail of operations |
| `memory_governance_delete` | Delete with audit trail |
| `memory_snapshot_create` | Git-versioned snapshot |
| `memory_action_create` | Create work items with dependencies |
| `memory_action_update` | Update action status |
| `memory_frontier` | Unblocked actions ranked by priority |
| `memory_next` | Single most important next action |
| `memory_lease` | Exclusive action leases (multi-agent) |
| `memory_routine_run` | Instantiate workflow routines |
| `memory_signal_send` | Inter-agent messaging |
| `memory_signal_read` | Read messages with receipts |
| `memory_checkpoint` | External condition gates |
| `memory_mesh_sync` | P2P sync between instances |
| `memory_sentinel_create` | Event-driven watchers |
| `memory_sentinel_trigger` | Fire sentinels externally |
| `memory_sketch_create` | Ephemeral action graphs |
| `memory_sketch_promote` | Promote to permanent |
| `memory_crystallize` | Compact action chains |
| `memory_diagnose` | Health checks |
| `memory_heal` | Auto-fix stuck state |
| `memory_facet_tag` | Dimension:value tags |
| `memory_facet_query` | Query by facet tags |
| `memory_verify` | Trace provenance |

| Type | Name | Description |
| --- | --- | --- |
| Resource | `agentmemory://status` | Health, session count, memory count |
| Resource | `agentmemory://project/{name}/profile` | Per-project intelligence |
| Resource | `agentmemory://memories/latest` | Latest 10 active memories |
| Resource | `agentmemory://graph/stats` | Knowledge graph statistics |
| Prompt | `recall_context` | Search + return context messages |
| Prompt | `session_handoff` | Handoff data between agents |
| Prompt | `detect_patterns` | Analyze recurring patterns |
| Skill | `/recall` | Search memory |
| Skill | `/remember` | Save to long-term memory |
| Skill | `/session-history` | Recent session summaries |
| Skill | `/forget` | Delete observations/sessions |

### Standalone MCP

Run without the full server — for any MCP client. Either of these works:

```
npx -y @agentmemory/agentmemory mcp # canonical (always available)
npx -y @agentmemory/mcp # shim package alias
```

Or add to your agent's MCP config:

Most agents (Cursor, Claude Desktop, Cline, Roo Code, Windsurf, Gemini CLI):

```
{
  "mcpServers": {
 "agentmemory": {
 "command": "npx",
 "args": ["-y", "@agentmemory/mcp"],
 "env": {
 "AGENTMEMORY_URL": "http://localhost:3111"
 }
 }
  }
}
```

Merge the `agentmemory` entry into your host's existing `mcpServers` object rather than replacing the file. For sandboxed clients that can't reach the host's `localhost`, add `"AGENTMEMORY_FORCE_PROXY": "1"` to the env block and set `AGENTMEMORY_URL` to a route the sandbox can reach.

OpenCode (`opencode.json`):

```
{
  "mcp": {
 "agentmemory": {
 "type": "local",
 "command": ["npx", "-y", "@agentmemory/mcp"],
 "enabled": true
 }
  },
  "plugin": ["./plugins/agentmemory-capture.ts"]
}
```

Copy the plugin file from the repo:

```
mkdir -p ~/.config/opencode/plugins
cp plugin/opencode/agentmemory-capture.ts ~/.config/opencode/plugins/
cp plugin/opencode/commands/*.md ~/.config/opencode/commands/
```

* * *

Auto-starts on port `3113`. Live observation stream, session explorer, memory browser, knowledge graph visualization, and health dashboard.

```
open http://localhost:3113
```

The viewer server binds to `127.0.0.1` by default. The REST-served `/agentmemory/viewer` endpoint follows the normal `AGENTMEMORY_SECRET` bearer-token rules. CSP headers use a per-response script nonce and disable inline handler attributes (`script-src-attr 'none'`).

* * *

The viewer at `:3113` shows what your agent **remembered**. The [iii console](https://iii.dev/docs/console) shows what your agent **did** — every memory op as an OpenTelemetry trace, every KV entry editable, every function invocable, every stream tappable. Two windows on the same memory: one product-shaped, one engine-shaped.

Watch a `memory_smart_search` fire and see the BM25 scan → embedding lookup → RRF fusion → reranker as a waterfall. Edit a stuck consolidation timer in the KV browser. Replay a `PostToolUse` hook with a tweaked payload. Pin the WebSocket stream and watch observations land live.

agentmemory ships this for free because every function call and trigger fires through iii — nothing custom, nothing to instrument.

[![iii console Workers page — connected workers including agentmemory instances with live function counts and runtime metadata](/rohitg00/agentmemory/raw/main/assets/iii-console/workers.png)](/rohitg00/agentmemory/blob/main/assets/iii-console/workers.png)

*Workers page: every connected worker — including agentmemory itself — with PID, function count, runtime, and last-seen.*

**Already installed.** The console ships with `iii` — no separate installer.

**Launch alongside agentmemory:**

```
# agentmemory viewer holds port 3113, so run the console on 3114.
# Engine REST (3111), WebSocket (3112), and bridge (49134) defaults match agentmemory.
iii console --port 3114
```

Then open `http://localhost:3114`. Add `--enable-flow` for the experimental architecture-graph page.

Override engine endpoints only if you've moved them:

```
iii console --port 3114 \
  --engine-port 3111 \
  --ws-port 3112 \
  --bridge-port 49134
```

**What you can do from the console:**

| Page | Use it to |
| --- | --- |
| **Workers** | See every connected worker and its live metrics — including the agentmemory worker itself. |
| **Functions** | Invoke any of agentmemory's functions directly with a JSON payload — handy for testing `memory.recall`, `memory.consolidate`, `graph.query` without wiring a client. |
| **Triggers** | Replay HTTP, cron, event, and state triggers — fire the consolidation cron manually, retry an HTTP route, emit a state change. |
| **States** | KV browser with full CRUD — sessions, memory slots, lifecycle timers, embeddings index — edit values in place. |
| **Streams** | Live WebSocket monitor for memory writes, hook events, and observation updates as they flow through iii streams. |
| **Queues** | Durable queue topics + dead-letter management. Replay or drop failed embedding / compression jobs. |
| **Traces** | OpenTelemetry waterfall / flame / service-breakdown views. Filter by `trace_id` to see exactly which functions, DB calls, and embedding requests a single `memory.search` produced. |
| **Logs** | Structured OTEL logs filtered and correlated to trace/span IDs. |
| **Config** | Runtime configuration — see exactly which workers, providers, and ports your engine is running with. |
| **Flow** | (Optional, `--enable-flow`) Interactive architecture graph of every worker, trigger, and stream. |

[![iii console trace waterfall view showing per-span duration](/rohitg00/agentmemory/raw/main/assets/iii-console/traces-waterfall.png)](/rohitg00/agentmemory/blob/main/assets/iii-console/traces-waterfall.png)

*Traces: waterfall / flame / service breakdown for every memory operation.*

**Traces are already on:**

`iii-config.yaml` ships with the `iii-observability` worker enabled (`exporter: memory`, `sampling_ratio: 1.0`, metrics + logs). No extra config needed — the moment agentmemory starts, every memory operation emits a trace span and a structured log the console can read.

If you want to export to Jaeger/Honeycomb/Grafana Tempo instead, change `exporter: memory` to `exporter: otlp` and set the collector endpoint per iii's observability docs.

> **Heads-up:** no auth is enforced on the console itself — keep it bound to `127.0.0.1` (the default) and never expose it publicly.

* * *

agentmemory is **already a running [iii](https://iii.dev) instance**. Three primitives — worker, function, trigger — compose the runtime; KV state, streams, and OTEL traces come from iii-state, iii-stream, and iii-observability workers that ship with iii. You didn't install Postgres, Redis, Express, pm2, or Prometheus, because iii replaces them.

That means one more command extends agentmemory with an entire new capability.

```
iii worker add iii-pubsub # fan memory writes out to every connected instance
iii worker add iii-cron # scheduled consolidation, decay sweeps, snapshot rotation
iii worker add iii-queue # durable retries for embedding + compression jobs
iii worker add iii-observability # OTEL traces on every memory op (default on)
iii worker add iii-sandbox # run recalled code inside an isolated microVM
iii worker add iii-database # swap in a SQL-backed state adapter
iii worker add mcp # generic MCP host alongside the agentmemory MCP
```

Each `iii worker add` registers new functions and triggers into the same engine agentmemory is already running on. The viewer and console pick them up immediately — no reload, no new integration, no new container.

| `iii worker add` | What you get on top of agentmemory |
| --- | --- |
| [`iii-pubsub`](https://workers.iii.dev/workers/iii-pubsub) | Multi-instance memory: every `remember` fans out, every `search` reads the union |
| [`iii-cron`](https://workers.iii.dev/workers/iii-cron) | Scheduled lifecycle — nightly consolidation, weekly snapshots, decay on a fixed clock |
| [`iii-queue`](https://workers.iii.dev/workers/iii-queue) | Durable retries: failed embedding + compression jobs survive restart, no lost observations |
| [`iii-observability`](https://workers.iii.dev/workers/iii-observability) | OTEL traces, metrics, logs on every function — wired in `iii-config.yaml` from day one |
| [`iii-sandbox`](https://workers.iii.dev/workers/iii-sandbox) | Code that came out of `memory_recall` runs inside a throwaway VM, not your shell |
| [`iii-database`](https://workers.iii.dev/workers/iii-database) | SQL-backed state adapter when you outgrow the in-memory KV defaults |
| [`mcp`](https://workers.iii.dev/workers/mcp) | Stand up extra MCP servers next to agentmemory's, share the same engine |

Full registry: [workers.iii.dev](https://workers.iii.dev). Every worker there composes through the same primitives agentmemory uses — and the agentmemory you already have is one of them.

| Traditional stack | agentmemory uses |
| --- | --- |
| Express.js / Fastify | iii HTTP Triggers |
| SQLite / Postgres + pgvector | iii KV State + in-memory vector index |
| SSE / Socket.io | iii Streams (WebSocket) |
| pm2 / systemd | iii engine worker supervision |
| Prometheus / Grafana | iii OTEL + health monitor |
| Custom plugin systems | `iii worker add <name>` |

**118 source files · ~21,800 LOC · 950+ tests · 123 functions · 34 KV scopes** — all on three primitives. No `agentmemory plugin install`. The plugin system is iii itself.

* * *

### LLM Providers

agentmemory auto-detects from your environment. By default, no LLM calls are made unless you configure a provider or explicitly opt in to the Claude subscription fallback.

| Provider | Config | Notes |
| --- | --- | --- |
| **No-op (default)** | No config needed | LLM-backed compress/summarize is DISABLED. Synthetic BM25 compression + recall still work. See `AGENTMEMORY_ALLOW_AGENT_SDK` below if you used to rely on the Claude-subscription fallback. |
| Anthropic API | `ANTHROPIC_API_KEY` | Per-token billing |
| MiniMax | `MINIMAX_API_KEY` | Anthropic-compatible |
| Gemini | `GEMINI_API_KEY` | Also enables embeddings |
| OpenRouter | `OPENROUTER_API_KEY` | Any model |
| OpenAI API | `OPENAI_API_KEY` | Default `gpt-4o-mini`, override with `OPENAI_MODEL` |
| **Local (Ollama / LM Studio / vLLM / llama.cpp)** | `OPENAI_API_KEY=local` + `OPENAI_BASE_URL=http://localhost:11434/v1` (Ollama) or `http://localhost:1234/v1` (LM Studio) + `OPENAI_MODEL=<your model>` | Anything OpenAI-API-compatible. Zero cost, runs on your hardware. See [Local models](#local-models-ollama-lm-studio-vllm) below. |
| Claude subscription fallback | `AGENTMEMORY_ALLOW_AGENT_SDK=true` | Opt-in only. Spawns `@anthropic-ai/claude-agent-sdk` sessions — used to cause unbounded Stop-hook recursion (#149 follow-up) so it is no longer the default. |

agentmemory talks to any OpenAI-API-compatible server, so anything that exposes `/v1/chat/completions` works without code changes. No paid keys, no cloud, no rate limits — runs entirely on your hardware.

**Ollama** (default port `11434`):

```
ollama pull qwen2.5-coder:7b # or llama3.2:3b, mistral:7b, etc.
ollama serve
```

```
# ~/.agentmemory/.env
OPENAI_API_KEY=ollama # any non-empty string; Ollama ignores it
OPENAI_BASE_URL=http://localhost:11434/v1
OPENAI_MODEL=qwen2.5-coder:7b
```

**LM Studio** (default port `1234`):

Open LM Studio → Local Server tab → Start Server. Pick any chat model from the picker (Qwen 2.5 Coder, Llama 3.2, DeepSeek, etc.).

```
# ~/.agentmemory/.env
OPENAI_API_KEY=lmstudio # any non-empty string; LM Studio ignores it
OPENAI_BASE_URL=http://localhost:1234/v1
OPENAI_MODEL=qwen2.5-coder-7b-instruct # match the model name from LM Studio
```

**vLLM / llama.cpp / Text Generation Inference**: same shape — point `OPENAI_BASE_URL` at whatever URL your server exposes, set `OPENAI_MODEL` to a name your server will accept.

**Model picks for memory work**: compression and summarization are short tasks (<2K tokens in, <500 tokens out) where a 7B instruct model is plenty. Recommendations:

| Model | Size | Why |
| --- | --- | --- |
| `qwen2.5-coder:7b` | ~4.7 GB | Best at code-shaped sessions; trained on programming + tool-use traces |
| `llama3.2:3b` | ~2 GB | Smallest sane option — fine for compression, weaker for graph extraction |
| `mistral:7b-instruct` | ~4.4 GB | Good general-purpose baseline if you don't want code-specific |
| `deepseek-r1:7b` | ~4.7 GB | Reasoning-tier quality at 7B; slower but cleaner extractions |

Reasoning-class models (`o1` -style with `<think>` blocks) can return empty `content` with a `reasoning` field your local server may not surface. If extractions come back blank, switch to a non-reasoning model first. The `OPENAI_REASONING_EFFORT=none` env can also disable thinking on Ollama Cloud thinking models that mirror the OpenAI reasoning schema.

Local embeddings ship out of the box via `@xenova/transformers` — `EMBEDDING_PROVIDER=local` (default) gives you BGE-small entirely on-device. No extra config needed.

Background compression runs on every observation, so model choice meaningfully changes monthly spend. Captured workload data: 635 requests / 888K tokens / 35 hours of active use, run against three OpenRouter models at 2026-05-23 pricing.

| Tier | Model | Input / 1M | Output / 1M | Cost for the captured 35h | Notes |
| --- | --- | --- | --- | --- | --- |
| Recommended | `deepseek/deepseek-v4-pro` | $0.435 | $0.87 | ~$0.46 | Solid compression + summarization quality at ~10× lower cost than Sonnet. |
| Recommended | `deepseek/deepseek-chat` | $0.27 | $1.10 | ~$0.40 | Older but still fine for compression-only workloads. |
| Recommended | `qwen/qwen3-coder` | $0.45 | $1.80 | ~$0.55 | Strong code reasoning if your sessions are heavily code-shaped. |
| Premium | `anthropic/claude-sonnet-4.6` | $3.00 | $15.00 | ~$5.02 | High quality but expensive for always-on background work. |
| Premium | `openai/gpt-4o` | $2.50 | $10.00 | ~$4.20 | Similar tier to Sonnet. |
| Avoid | `anthropic/claude-opus-4.6` | $15.00 | $75.00 | ~$25+ | Reasoning-class model; massive overspend for compression. |

agentmemory prints a runtime warning when `OPENROUTER_MODEL` matches a premium-tier pattern. Set `AGENTMEMORY_SUPPRESS_COST_WARNING=1` to silence once you've made an informed choice.

Quality vs cost tradeoff for memory work: compression is a summarization task with relatively loose quality bars (the agent re-reads the summary, not the user). DeepSeek-V4-Pro / Qwen3-Coder land within rounding error of Sonnet on this task while costing ~10× less. Save the premium-tier models for queries you read directly.

Sources: [OpenRouter pricing for Sonnet 4.6](https://openrouter.ai/anthropic/claude-sonnet-4.6/pricing), [DeepSeek V4 Pro](https://openrouter.ai/deepseek/deepseek-v4-pro), [DeepSeek pricing notes](https://api-docs.deepseek.com/quick_start/pricing/).

In multi-agent setups where several roles share one agentmemory server (architect / developer / reviewer / researcher / support-agent), `AGENT_ID` tags every write with the role that made it. `AGENTMEMORY_AGENT_SCOPE` controls whether recall filters by that tag.

Two modes:

| Mode | Tag writes | Filter recall | When to use |
| --- | --- | --- | --- |
| `shared` (default) | yes | no | Cross-agent context with audit trail. Architect can see what developer noted, but every row records who said it. |
| `isolated` | yes | yes | Strict separation. Architect never sees developer's observations / memories / sessions. |

What gets tagged when `AGENT_ID` is set: `Session.agentId`, `RawObservation.agentId`, `CompressedObservation.agentId`, `Memory.agentId`. The role flows from `api::session::start` → `mem::observe` → `mem::compress` → KV.

What gets filtered in isolated mode: `mem::smart-search`, `/agentmemory/memories`, `/agentmemory/observations`, `/agentmemory/sessions`. Each endpoint accepts `?agentId=<role>` to override per-request, and `?agentId=*` to opt out of the env scope entirely. `/memories` also accepts `?includeOrphans=true` to surface pre-AGENT\_ID memories whose `agentId` is undefined.

Per-call override at the SDK / REST layer: every mutating endpoint (`/session/start`, `/remember`) accepts an `agentId` field in the request body that wins over the env. Useful for runtimes routing many roles through one server process.

When `AGENT_ID` is unset, memory remains unscoped (legacy behavior, no tags, no filters).

### Ports

agentmemory + iii-engine bind four ports by default. If a restart fails with `port in use`, this table tells you which process to look for.

| Port | Process | Purpose | Env override |
| --- | --- | --- | --- |
| `3111` | agentmemory | REST API + MCP HTTP + `/agentmemory/health` + `/agentmemory/livez` | `III_REST_PORT` |
| `3112` | iii-engine | Internal streams worker (consumed by agentmemory + viewer) | `III_STREAMS_PORT` |
| `3113` | agentmemory | Real-time viewer (`http://localhost:3113`) | `AGENTMEMORY_VIEWER_PORT` |
| `49134` | iii-engine | WebSocket — workers register here, OTel telemetry flows over it | `III_ENGINE_URL` (full URL, default `ws://localhost:49134`) |

Stale-process cleanup when ports stay bound after a crashed run:

```
# macOS / Linux — find whatever is on each port and kill it
lsof -i :3111,3112,3113,49134
pkill -f agentmemory || true
pkill -f 'iii ' || true

# Windows
netstat -ano | findstr ":3111 :3112 :3113 :49134"
taskkill /F /PID <pid>
```

`agentmemory stop` reaps both the worker and the engine pidfile cleanly on graceful shutdown (#640, #474). The manual cleanup above is only for the post-crash case where neither pidfile is left behind.

### Config File

Put agentmemory runtime configuration in `~/.agentmemory/.env` instead of exporting variables in every shell. If the viewer shows a setup hint like `export ANTHROPIC_API_KEY=...`, copy it into this file as `ANTHROPIC_API_KEY=...` without the `export` prefix, then restart agentmemory.

Process environment variables still work and take precedence over values in the file.

On Windows, the same file lives at `%USERPROFILE%\.agentmemory\.env`:

```
New-Item -ItemType Directory -Force $HOME\.agentmemory
notepad $HOME\.agentmemory\.env
```

To test with a Claude Code Pro/Max subscription instead of an API key, opt in explicitly:

```
AGENTMEMORY_ALLOW_AGENT_SDK=true
AGENTMEMORY_AUTO_COMPRESS=true
```

Consolidation (graph nodes, lessons, crystals) is on by default whenever an LLM provider is configured. Explicitly opt out with `CONSOLIDATION_ENABLED=false` if you want LLM-free operation. Graph extraction is a separate flag:

```
GRAPH_EXTRACTION_ENABLED=true
# CONSOLIDATION_ENABLED=false # opt out of auto-consolidation
```

### Environment Variables

Create `~/.agentmemory/.env`:

```
# LLM provider (pick one — default is the no-op provider: no LLM calls)
# ANTHROPIC_API_KEY=sk-ant-...
# ANTHROPIC_BASE_URL=... # Optional: Anthropic-compatible proxy / Azure
# GEMINI_API_KEY=...
# OPENROUTER_API_KEY=...
# MINIMAX_API_KEY=...
# OPENAI_API_KEY=*** # NOTE: this same key auto-activates BOTH the
# # OpenAI LLM provider (here) AND the OpenAI
# # embedding provider (further below). Set
# # OPENAI_API_KEY_FOR_LLM=false to scope it
# # to embeddings only.
# OPENAI_BASE_URL=https://api.openai.com # Optional: override for Azure / vLLM / LM Studio / proxies
# # Azure: https://<resource>.openai.azure.com/openai/deployments/<deployment>
# # Auto-detected from `.openai.azure.com` hostname; uses
# # api-key header + api-version query param.
# OPENAI_API_VERSION=2024-08-01-preview # Optional: Azure api-version query param
# OPENAI_MODEL=gpt-4o-mini # Optional: default model
# OPENAI_TIMEOUT_MS=60000 # Optional: OpenAI-scoped alias for the outbound fetch
# # timeout. Takes precedence over AGENTMEMORY_LLM_TIMEOUT_MS
# # for back-compat with v0.9.17. New configs should
# # prefer the global AGENTMEMORY_LLM_TIMEOUT_MS below.
# OPENAI_REASONING_EFFORT=none # Optional: "low" | "medium" | "high" | "none"
# # Honored only by OpenAI's reasoning models (o1, o3,
# # gpt-*-reasoning) and providers that mirror that
# # schema (Ollama Cloud thinking models). Standard
# # chat models reject this field with 400. Set to
# # "none" for thinking models that return reasoning
# # but no content.
# OPENAI_API_KEY_FOR_LLM=false # Optional: set to false to skip OpenAI auto-detection
# # for LLM (useful if you only want OpenAI for embeddings)
# Opt-in Claude-subscription fallback (spawns @anthropic-ai/claude-agent-sdk);
# leave OFF unless you understand the Stop-hook recursion risk (#149 follow-up):
# AGENTMEMORY_ALLOW_AGENT_SDK=true

# Embedding provider (auto-detected, or override)
# EMBEDDING_PROVIDER=local
# VOYAGE_API_KEY=...
# OPENAI_API_KEY=sk-...
# OPENAI_BASE_URL=https://api.openai.com # Override for Azure / vLLM / LM Studio / proxies
# OPENAI_EMBEDDING_MODEL=text-embedding-3-small
# OPENAI_EMBEDDING_DIMENSIONS=1536 # Required when the model is not in the known-models table

# Outbound LLM / embedding timeout
# AGENTMEMORY_LLM_TIMEOUT_MS=60000 # Default: 60 000 ms (60 s). Applies to every
 # raw-fetch provider (Gemini, OpenRouter, MiniMax,
 # OpenAI LLM, OpenAI/Cohere/Voyage/OpenRouter
 # embedding). For the OpenAI LLM path, the
 # OpenAI-scoped OPENAI_TIMEOUT_MS alias (above)
 # takes precedence when set, for back-compat
 # with v0.9.17.
 # Increase for slow networks or large batch calls;
 # decrease to fail-fast on rate-limit holds.

# Search tuning
# BM25_WEIGHT=0.4
# VECTOR_WEIGHT=0.6
# TOKEN_BUDGET=2000

# Auth
# AGENTMEMORY_SECRET=your-secret

# Ports (defaults: 3111 API, 3113 viewer)
# III_REST_PORT=3111

# Features
# AGENTMEMORY_AUTO_COMPRESS=false  # OFF by default (#138). When on,
 # every PostToolUse hook calls your
 # LLM provider to compress the
 # observation — expect significant
 # token spend on active sessions.
# AGENTMEMORY_SLOTS=false # OFF by default. Editable pinned
 # memory slots — persona,
 # user_preferences, tool_guidelines,
 # project_context, guidance,
 # pending_items, session_patterns,
 # self_notes. Size-limited; agent
 # edits via memory_slot_* tools.
 # Pinned slots addressable for
 # SessionStart injection.
# AGENTMEMORY_REFLECT=false # OFF by default. Requires SLOTS=on.
 # Stop hook fires mem::slot-reflect:
 # scans recent observations, auto-
 # appends TODOs to pending_items,
 # counts patterns in
 # session_patterns, records touched
 # files in project_context. Fire-
 # and-forget; does not block.
# AGENTMEMORY_INJECT_CONTEXT=false # OFF by default (#143). When on:
 # - SessionStart may inject ~1-2K
 # chars of project context into
 # the first turn of each session
 # (this is what actually reaches
 # the model — Claude Code treats
 # SessionStart stdout as context)
 # - PreToolUse fires /agentmemory/enrich
 # on every file-touching tool call
 # (resource cleanup, not a token
 # fix — PreToolUse stdout is debug
 # log only per Claude Code docs)
 # Observations are still captured via
 # PostToolUse regardless of this flag.
# GRAPH_EXTRACTION_ENABLED=false
# CONSOLIDATION_ENABLED=false # on by default when an LLM provider is configured
# LESSON_DECAY_ENABLED=true
# OBSIDIAN_AUTO_EXPORT=false
# AGENTMEMORY_EXPORT_ROOT=~/.agentmemory
# CLAUDE_MEMORY_BRIDGE=false
# SNAPSHOT_ENABLED=false

# Team
# TEAM_ID=
# USER_ID=
# TEAM_MODE=private

# Tool visibility: "core" (8 tools, lean fallback) or "all" (53 tools)
# AGENTMEMORY_TOOLS=core
```

* * *

125 endpoints on port `3111`. The REST API binds to `127.0.0.1` by default. Protected endpoints require `Authorization: Bearer <secret>` when `AGENTMEMORY_SECRET` is set, and mesh sync endpoints require `AGENTMEMORY_SECRET` on both peers.

Key endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/agentmemory/health` | Health check (always public) |
| `POST` | `/agentmemory/session/start` | Start session + get context |
| `POST` | `/agentmemory/session/end` | End session |
| `POST` | `/agentmemory/observe` | Capture observation |
| `POST` | `/agentmemory/smart-search` | Hybrid search |
| `POST` | `/agentmemory/context` | Generate context |
| `POST` | `/agentmemory/remember` | Save to long-term memory |
| `POST` | `/agentmemory/forget` | Delete observations |
| `POST` | `/agentmemory/enrich` | File context + memories + bugs |
| `GET` | `/agentmemory/profile` | Project profile |
| `GET` | `/agentmemory/export` | Export all data |
| `POST` | `/agentmemory/import` | Import from JSON |
| `POST` | `/agentmemory/graph/query` | Knowledge graph query |
| `POST` | `/agentmemory/team/share` | Share with team |
| `GET` | `/agentmemory/audit` | Audit trail |

Full endpoint list: [`src/triggers/api.ts`](/rohitg00/agentmemory/blob/main/src/triggers/api.ts)

* * *

```
npm run dev # Hot reload
npm run build # Production build
npm test # 950+ tests
npm run test:integration  # API tests (requires running services)
```

**Prerequisites:** Node.js >= 20, [iii-engine](https://iii.dev/docs) or Docker

[Apache-2.0](/rohitg00/agentmemory/blob/main/LICENSE)

## Releases 46

[\+ 45 releases](/rohitg00/agentmemory/releases)

## Packages

No packages published