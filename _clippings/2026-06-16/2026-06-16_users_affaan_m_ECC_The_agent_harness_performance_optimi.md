---
title: "2026-06-16_github_com_affaan_m_ECC_The_agent_harness_performance_optimiz"
source: "https://github.com/affaan-m/ECC"
author:
  - "[[@users]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "#1991"
  - "#2024"
  - "github"
  - "@users"
---

# affaan-m/ECC: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](/codespaces/new/affaan-m/ECC?resume=1)

| Name | Name | 
Last commit message

 | 

Last commit date

 |
| --- | --- | --- | --- |
| 

[64cd1ba](/affaan-m/ECC/commit/64cd1ba248e77e377e76f70fc4e6434bfdddd511) ·

[1,997 Commits](/affaan-m/ECC/commits/main/)

 |
| 

[.agents](/affaan-m/ECC/tree/main/.agents ".agents")

 | 

[.agents](/affaan-m/ECC/tree/main/.agents ".agents")

 | 

[chore: gate canonical ECC release identity (](/affaan-m/ECC/commit/8141f6904f14fa8a83131e1cb5b6507d687e25bb "chore: gate canonical ECC release identity (#1991)")[#1991](https://github.com/affaan-m/ECC/pull/1991)[)](/affaan-m/ECC/commit/8141f6904f14fa8a83131e1cb5b6507d687e25bb "chore: gate canonical ECC release identity (#1991)")

 |  |
| 

[.claude-plugin](/affaan-m/ECC/tree/main/.claude-plugin ".claude-plugin")

 | 

[.claude-plugin](/affaan-m/ECC/tree/main/.claude-plugin ".claude-plugin")

 | 

[Add React language track with agents, skills, rules, and commands (](/affaan-m/ECC/commit/04c68e483af8c2cc2717ad4b8013c3673124836c "Add React language track with agents, skills, rules, and commands (#2024)
* feat(rules): add rules/react/ track
Five rule files mirroring per-language convention (coding-style,
hooks, patterns, security, testing). Each has `paths:` glob
frontmatter for auto-activation when editing matching files.
- coding-style.md: file extensions, naming, JSX, RSC boundary
- hooks.md: React hooks (NOT Claude Code hooks) — rules-of-hooks,
dep arrays, cleanup, memoization, React 19 additions
- patterns.md: container/presentational split, state location
decision tree, Suspense + error boundaries, forms, data fetching
- security.md: dangerouslySetInnerHTML, unsafe URL schemes,
server-action validation, env-var leaks, CSP
- testing.md: RTL queries, userEvent, async, MSW, axe, anti-patterns
Each file extends typescript/* and common/* rules.
* feat(skills): add react-patterns, react-testing, react-performance
Three new skills under skills/ following the SKILL.md convention.
- react-patterns: React 18/19 idioms — hooks discipline, state
location decision tree, server/client component boundary,
Suspense + error boundaries, form actions (React 19), data
fetching matrix, composition recipes, accessibility-first.
- react-testing: React Testing Library + Vitest/Jest, query
priority order, userEvent, MSW network mocking, axe a11y
assertions, RTL vs Playwright CT boundary, TDD workflow.
- react-performance: 70-rule performance ruleset adapted from
Vercel Labs react-best-practices (MIT) across 8 priority
categories — waterfalls, bundle size, server-side, client
fetch, re-render, rendering, JS micro, advanced patterns.
Includes Lighthouse / Web Vitals mapping and attribution to
upstream.
Cross-links between the three skills and out to frontend-patterns,
accessibility, e2e-testing, tdd-workflow.
* feat(agents): add react-reviewer and react-build-resolver
Two new agents covering React-specific code review and build error
resolution, plus matching .kiro/ mirrors and a routing pointer
edit on typescript-reviewer.
- react-reviewer: slim React-only lanes (hooks rules,
dangerouslySetInnerHTML, unsafe URL schemes, key prop, state
mutation, derived-state-in-effect, server/client component
boundary, accessibility, render performance, Server Action
validation, env-var leaks). Explicitly delegates generic
TypeScript/async/Node concerns to typescript-reviewer. Both
agents should be invoked together on .tsx/.jsx PRs.
- react-build-resolver: React build/bundler/runtime hydration
failures across Vite, webpack, Next.js, CRA, Parcel, esbuild,
Bun, Rsbuild. Handles JSX/TSX compile errors, tsconfig fixes,
Next.js App Router server/client boundary errors, hydration
mismatches, duplicated React copies, Tailwind/PostCSS pipeline.
- .kiro/agents/react-reviewer.json + react-build-resolver.json:
Kiro IDE format mirrors following the per-language precedent.
- typescript-reviewer: routing pointer added to its MEDIUM React
block — defers to /react-review for React-specific concerns
while keeping its block as fallback for repos that only invoke
typescript-reviewer.
All agents carry the standard Prompt Defense Baseline stanza.
* feat(commands): add /react-review /react-build /react-test
Three new slash commands invoking the React agents.
- /react-review: invokes react-reviewer. Documents the routing
rule with typescript-reviewer — both should run together on
TSX/JSX PRs. Lists CRITICAL/HIGH/MEDIUM rule categories and
the automated checks (eslint with react-hooks + jsx-a11y,
tsc --noEmit, npm audit).
- /react-build: invokes react-build-resolver. Documents bundler
detection, common failure patterns, fix strategy, and stop
conditions.
- /react-test: enforces TDD with React Testing Library + Vitest
or Jest, behavior-focused queries, userEvent + MSW patterns,
axe accessibility assertions, coverage targets.
Each command file has the required description: frontmatter and
follows the per-language command convention (cpp-test, go-test,
kotlin-test, etc.).
* chore: wire react track into manifests and stack mappings
- agent.yaml: add react-patterns, react-performance, react-testing
to the skills array; add react-build, react-review, react-test to
the commands array (alphabetically inserted to satisfy the
ci/agent-yaml-surface sync test).
- config/project-stack-mappings.json: extend the `react` stack
entry — add "react" to rules array (was ["common","typescript",
"web"]); add react-patterns, react-performance, react-testing,
accessibility to the skills array.
- docs/COMMAND-REGISTRY.json: bump totalCommands 75 -> 78; add
three new entries (react-build, react-review, react-test) with
primaryAgents / allAgents / skills wiring. react-review's
allAgents includes typescript-reviewer to reflect the dual-agent
routing convention.
- CLAUDE.md: add Skills-table row mapping *.tsx / *.jsx /
components/** to react-patterns + react-testing skills and
the /react-review, /react-build, /react-test commands.
* chore(catalog): sync counts to 62 agents / 78 commands / 235 skills
Auto-generated via `node scripts/ci/catalog.js --write --text`
after the react track additions:
- 2 new agents: react-reviewer, react-build-resolver (60 -> 62)
- 3 new commands: react-build, react-review, react-test (75 -> 78)
- 3 new skills: react-patterns, react-performance, react-testing
(232 -> 235)
Files updated by the catalog sync:
- .claude-plugin/plugin.json description string
- .claude-plugin/marketplace.json plugin description
- README.md quick-start summary, project tree, feature parity tables
- README.zh-CN.md quick-start summary
- AGENTS.md project structure summary
- docs/zh-CN/README.md parity table
- docs/zh-CN/AGENTS.md project structure summary
All counts now match the filesystem catalog (verified by
ci/catalog.test.js).
* feat(kiro): add react agent markdown companions to JSON entries
* feat(kiro): add react skills into manifests
* fix(ci): sync catalog counts, registry, and package files for react track
- .claude-plugin/{plugin,marketplace}.json: bump description counts to 62/235/78
- docs/COMMAND-REGISTRY.json: regenerate to include quality-gate and react commands
- package.json: add skills/react-{patterns,performance,testing}/ to files allowlist so npm-publish-surface aligns with install-modules manifest
* fix(react): address PR #2024 review feedback
Critical:
- Remove undefined/.claude/session-aliases.json containing __proto__ prototype-pollution
fixture committed by accident in a7333c14
High:
- agents/react-build-resolver.md: replace brittle `test -o $(grep -l ...)` and
`test -a -n $(grep ...)` detection with explicit `{ ... || grep -q ...; }` so
bundler detection no longer breaks when grep returns empty
- agents/react-build-resolver.md: drop hardcoded `npm i react@^19 react-dom@^19`
remediation; replace with version-agnostic pair-upgrade note that honors the
project's installed major (17/18/19) — surgical fix principle
- commands/react-review.md: guard `tsc --noEmit -p tsconfig.json` with
`[ -f tsconfig.json ] &&` so the review skips cleanly on JS-only projects
Medium:
- rules/react/security.md: correct the React-18-blocks-javascript-URL claim
(React only warns in dev; production navigation is not blocked)
- rules/react/security.md: correct CRA env-var exposure row (CRA exposes
REACT_APP_*, NODE_ENV, PUBLIC_URL — not 'all' variables)
- skills/react-testing/SKILL.md: instantiate QueryClient once outside the
wrapper closure so React Query cache survives re-renders (flaky-test fix)
- skills/react-testing/SKILL.md: restore console.error spy with mockRestore()
in a try/finally so the mock does not leak across tests
- commands/react-test.md: switch outer example-session fence to 4 backticks
so the inner ```tsx/```bash blocks don't prematurely terminate it
* fix(kiro): mirror react-build-resolver react 19 conditional remediation
Discussion r3272907106 flagged the kiro json variant still carrying the hardcoded
'npm i react@^19 react-dom@^19' line that the .md companion already dropped.
Replace with the same conditional, version-agnostic guidance so both variants
stay in sync.
* fix(react): bump react-build example session fence to 4 backticks
Discussion r3272907144 flagged the same nested-fence issue in
commands/react-build.md that we fixed earlier in commands/react-test.md.
The outer triple-backtick text block was being prematurely terminated by
the inner bash/tsx fences inside the Example Session.
* fix(react): bump react-review example usage fence to 4 backticks
Discussion r3272907201 flagged the same nested-fence issue in
commands/react-review.md. The outer triple-backtick text block was
being prematurely terminated by the inner tsx/ts fences inside the
Example Usage transcript.
* fix(docs): clarify commands row as legacy shims in feature parity table
Discussion r3272912003: README comparison table said 'PASS: 78 commands'
while the install-section and quick-start prose use 'legacy command shims'.
Aligned the comparison-table cell to 'PASS: 78 commands (legacy shims)' so
the count word survives the catalog-validator regex while making the legacy
nature explicit.
Widened the catalog comparison-table commands regex to tolerate an optional
parenthetical after the count word, so both the existing 'X commands' and
the new 'X commands (legacy shims)' phrasings validate without breaking
older READMEs/translations.
* Update rules/react/security.md
Co-authored-by: cubic-dev-ai[bot] <191113872+cubic-dev-ai[bot]@users.noreply.github.com>
* fix(react): guard tsc in react-build-resolver diagnostic commands
Discussion r3288910205: the agent prompt instructed an unconditional
'tsc --noEmit -p tsconfig.json', which adds noise (or hard-fails) on
JavaScript-only projects with no tsconfig.json or no installed TypeScript.
Replaced with 'test -f tsconfig.json && npx --yes tsc --noEmit -p tsconfig.json'
in both variants:
- agents/react-build-resolver.md
- .kiro/agents/react-build-resolver.json (prompt string mirrored)
Mirrors the same guard already applied to commands/react-review.md in de135f61.
* fix(react): pin tsc resolution to local install in build resolver
Discussion r3289054157: previous fix used 'npx --yes tsc' which auto-installs
the latest TypeScript from npm when none is local, producing version drift
and non-reproducible typecheck results across machines.
Switched to 'npx --no-install tsc' in both variants so the diagnostic uses
only the project's pinned TypeScript and fails fast if it isn't installed:
- agents/react-build-resolver.md
- .kiro/agents/react-build-resolver.json (prompt string mirrored)
* feat(counts): resolve counts for agents, skills...
* fix(ci): regen command registry for golang-testing entry
Removes stale kotlin-patterns entry to satisfy command-registry:check.
* fix: keep local Claude settings out of React track PR
---------
Co-authored-by: AlexisLeDain <a.ledain@docoon.com>
Co-authored-by: cubic-dev-ai[bot] <191113872+cubic-dev-ai[bot]@users.noreply.github.com>
Co-authored-by: Affaan Mustafa <affaan@dcube.ai>")[#2024](https://github.com/affaan-m/ECC/pull/2024)

 |  |
| 

[.claude](/affaan-m/ECC/tree/main/.claude ".claude")

 | 

[.claude](/affaan-m/ECC/tree/main/.claude ".claude")

 | 

[docs: add prompt defense baselines](/affaan-m/ECC/commit/393d397efa40a9e9b6c7296df8181860ebf5047e "docs: add prompt defense baselines
Add compact prompt-defense baselines to active ECC prompt surfaces and copied CLAUDE examples. AgentShield prompt-defense findings are now zero; local tests passed 2366/2366.")

 |  |
| 

[.codebuddy](/affaan-m/ECC/tree/main/.codebuddy ".codebuddy")

 | 

[.codebuddy](/affaan-m/ECC/tree/main/.codebuddy ".codebuddy")

 | 

[feat(install): add CodeBuddy(Tencent) adaptation with installation sc…](/affaan-m/ECC/commit/c38bc799fd4f1c5c15d916e3694dda806f6f78c0 "feat(install): add CodeBuddy(Tencent) adaptation with installation scripts (#1038)
* feat(install): add CodeBuddy(Tencent) adaptation with installation scripts
* fix: add codebuddy to SUPPORTED_INSTALL_TARGETS
* fix(codebuddy): resolve installer path issues, unused vars, and uninstall safety")

 |  |
| 

[.codex-plugin](/affaan-m/ECC/tree/main/.codex-plugin ".codex-plugin")

 | 

[.codex-plugin](/affaan-m/ECC/tree/main/.codex-plugin ".codex-plugin")

 | 

[chore: gate canonical ECC release identity (](/affaan-m/ECC/commit/8141f6904f14fa8a83131e1cb5b6507d687e25bb "chore: gate canonical ECC release identity (#1991)")[#1991](https://github.com/affaan-m/ECC/pull/1991)[)](/affaan-m/ECC/commit/8141f6904f14fa8a83131e1cb5b6507d687e25bb "chore: gate canonical ECC release identity (#1991)")

 |  |
| 

[.codex](/affaan-m/ECC/tree/main/.codex ".codex")

 | 

[.codex](/affaan-m/ECC/tree/main/.codex ".codex")

 | 

[fix: harden agent instruction surfaces](/affaan-m/ECC/commit/c9962bf83e38ac8ffcc174dc768ff002b8b731b2 "fix: harden agent instruction surfaces")

 |  |
| 

[.cursor](/affaan-m/ECC/tree/main/.cursor ".cursor")

 | 

[.cursor](/affaan-m/ECC/tree/main/.cursor ".cursor")

 | 

[fix: install native Cursor hook and MCP config (](/affaan-m/ECC/commit/92e0c7e9ff9202b60da34659204420aea487f71f "fix: install native Cursor hook and MCP config (#1543)
* fix: install native cursor hook and MCP config
* fix: avoid false healthy stdio mcp probes")[#1543](https://github.com/affaan-m/ECC/pull/1543)[)](/affaan-m/ECC/commit/92e0c7e9ff9202b60da34659204420aea487f71f "fix: install native Cursor hook and MCP config (#1543)
* fix: install native cursor hook and MCP config
* fix: avoid false healthy stdio mcp probes")

 |  |
| 

[.gemini](/affaan-m/ECC/tree/main/.gemini ".gemini")

 | 

[.gemini](/affaan-m/ECC/tree/main/.gemini ".gemini")

 | 

[feat: add gemini install target](/affaan-m/ECC/commit/1744e1ef0e32e397840b7bfa24b388eafe049280 "feat: add gemini install target")

 |  |
| 

[.github](/affaan-m/ECC/tree/main/.github ".github")

 | 

[.github](/affaan-m/ECC/tree/main/.github ".github")

 | 

[chore(deps): bump actions/stale to 10.3.0 (](/affaan-m/ECC/commit/870c5eb21bac6dd241eb752bec5c607cda507942 "chore(deps): bump actions/stale to 10.3.0 (#2045)
Bumps actions/stale from 10.2.0 to 10.3.0. Verified by the full CI matrix on the PR.")[#2045](https://github.com/affaan-m/ECC/pull/2045)[)](/affaan-m/ECC/commit/870c5eb21bac6dd241eb752bec5c607cda507942 "chore(deps): bump actions/stale to 10.3.0 (#2045)
Bumps actions/stale from 10.2.0 to 10.3.0. Verified by the full CI matrix on the PR.")

 |  |
| 

[.kiro](/affaan-m/ECC/tree/main/.kiro ".kiro")

 | 

[.kiro](/affaan-m/ECC/tree/main/.kiro ".kiro")

 | 

[Add React language track with agents, skills, rules, and commands (](/affaan-m/ECC/commit/04c68e483af8c2cc2717ad4b8013c3673124836c "Add React language track with agents, skills, rules, and commands (#2024)
* feat(rules): add rules/react/ track
Five rule files mirroring per-language convention (coding-style,
hooks, patterns, security, testing). Each has `paths:` glob
frontmatter for auto-activation when editing matching files.
- coding-style.md: file extensions, naming, JSX, RSC boundary
- hooks.md: React hooks (NOT Claude Code hooks) — rules-of-hooks,
dep arrays, cleanup, memoization, React 19 additions
- patterns.md: container/presentational split, state location
decision tree, Suspense + error boundaries, forms, data fetching
- security.md: dangerouslySetInnerHTML, unsafe URL schemes,
server-action validation, env-var leaks, CSP
- testing.md: RTL queries, userEvent, async, MSW, axe, anti-patterns
Each file extends typescript/* and common/* rules.
* feat(skills): add react-patterns, react-testing, react-performance
Three new skills under skills/ following the SKILL.md convention.
- react-patterns: React 18/19 idioms — hooks discipline, state
location decision tree, server/client component boundary,
Suspense + error boundaries, form actions (React 19), data
fetching matrix, composition recipes, accessibility-first.
- react-testing: React Testing Library + Vitest/Jest, query
priority order, userEvent, MSW network mocking, axe a11y
assertions, RTL vs Playwright CT boundary, TDD workflow.
- react-performance: 70-rule performance ruleset adapted from
Vercel Labs react-best-practices (MIT) across 8 priority
categories — waterfalls, bundle size, server-side, client
fetch, re-render, rendering, JS micro, advanced patterns.
Includes Lighthouse / Web Vitals mapping and attribution to
upstream.
Cross-links between the three skills and out to frontend-patterns,
accessibility, e2e-testing, tdd-workflow.
* feat(agents): add react-reviewer and react-build-resolver
Two new agents covering React-specific code review and build error
resolution, plus matching .kiro/ mirrors and a routing pointer
edit on typescript-reviewer.
- react-reviewer: slim React-only lanes (hooks rules,
dangerouslySetInnerHTML, unsafe URL schemes, key prop, state
mutation, derived-state-in-effect, server/client component
boundary, accessibility, render performance, Server Action
validation, env-var leaks). Explicitly delegates generic
TypeScript/async/Node concerns to typescript-reviewer. Both
agents should be invoked together on .tsx/.jsx PRs.
- react-build-resolver: React build/bundler/runtime hydration
failures across Vite, webpack, Next.js, CRA, Parcel, esbuild,
Bun, Rsbuild. Handles JSX/TSX compile errors, tsconfig fixes,
Next.js App Router server/client boundary errors, hydration
mismatches, duplicated React copies, Tailwind/PostCSS pipeline.
- .kiro/agents/react-reviewer.json + react-build-resolver.json:
Kiro IDE format mirrors following the per-language precedent.
- typescript-reviewer: routing pointer added to its MEDIUM React
block — defers to /react-review for React-specific concerns
while keeping its block as fallback for repos that only invoke
typescript-reviewer.
All agents carry the standard Prompt Defense Baseline stanza.
* feat(commands): add /react-review /react-build /react-test
Three new slash commands invoking the React agents.
- /react-review: invokes react-reviewer. Documents the routing
rule with typescript-reviewer — both should run together on
TSX/JSX PRs. Lists CRITICAL/HIGH/MEDIUM rule categories and
the automated checks (eslint with react-hooks + jsx-a11y,
tsc --noEmit, npm audit).
- /react-build: invokes react-build-resolver. Documents bundler
detection, common failure patterns, fix strategy, and stop
conditions.
- /react-test: enforces TDD with React Testing Library + Vitest
or Jest, behavior-focused queries, userEvent + MSW patterns,
axe accessibility assertions, coverage targets.
Each command file has the required description: frontmatter and
follows the per-language command convention (cpp-test, go-test,
kotlin-test, etc.).
* chore: wire react track into manifests and stack mappings
- agent.yaml: add react-patterns, react-performance, react-testing
to the skills array; add react-build, react-review, react-test to
the commands array (alphabetically inserted to satisfy the
ci/agent-yaml-surface sync test).
- config/project-stack-mappings.json: extend the `react` stack
entry — add "react" to rules array (was ["common","typescript",
"web"]); add react-patterns, react-performance, react-testing,
accessibility to the skills array.
- docs/COMMAND-REGISTRY.json: bump totalCommands 75 -> 78; add
three new entries (react-build, react-review, react-test) with
primaryAgents / allAgents / skills wiring. react-review's
allAgents includes typescript-reviewer to reflect the dual-agent
routing convention.
- CLAUDE.md: add Skills-table row mapping *.tsx / *.jsx /
components/** to react-patterns + react-testing skills and
the /react-review, /react-build, /react-test commands.
* chore(catalog): sync counts to 62 agents / 78 commands / 235 skills
Auto-generated via `node scripts/ci/catalog.js --write --text`
after the react track additions:
- 2 new agents: react-reviewer, react-build-resolver (60 -> 62)
- 3 new commands: react-build, react-review, react-test (75 -> 78)
- 3 new skills: react-patterns, react-performance, react-testing
(232 -> 235)
Files updated by the catalog sync:
- .claude-plugin/plugin.json description string
- .claude-plugin/marketplace.json plugin description
- README.md quick-start summary, project tree, feature parity tables
- README.zh-CN.md quick-start summary
- AGENTS.md project structure summary
- docs/zh-CN/README.md parity table
- docs/zh-CN/AGENTS.md project structure summary
All counts now match the filesystem catalog (verified by
ci/catalog.test.js).
* feat(kiro): add react agent markdown companions to JSON entries
* feat(kiro): add react skills into manifests
* fix(ci): sync catalog counts, registry, and package files for react track
- .claude-plugin/{plugin,marketplace}.json: bump description counts to 62/235/78
- docs/COMMAND-REGISTRY.json: regenerate to include quality-gate and react commands
- package.json: add skills/react-{patterns,performance,testing}/ to files allowlist so npm-publish-surface aligns with install-modules manifest
* fix(react): address PR #2024 review feedback
Critical:
- Remove undefined/.claude/session-aliases.json containing __proto__ prototype-pollution
fixture committed by accident in a7333c14
High:
- agents/react-build-resolver.md: replace brittle `test -o $(grep -l ...)` and
`test -a -n $(grep ...)` detection with explicit `{ ... || grep -q ...; }` so
bundler detection no longer breaks when grep returns empty
- agents/react-build-resolver.md: drop hardcoded `npm i react@^19 react-dom@^19`
remediation; replace with version-agnostic pair-upgrade note that honors the
project's installed major (17/18/19) — surgical fix principle
- commands/react-review.md: guard `tsc --noEmit -p tsconfig.json` with
`[ -f tsconfig.json ] &&` so the review skips cleanly on JS-only projects
Medium:
- rules/react/security.md: correct the React-18-blocks-javascript-URL claim
(React only warns in dev; production navigation is not blocked)
- rules/react/security.md: correct CRA env-var exposure row (CRA exposes
REACT_APP_*, NODE_ENV, PUBLIC_URL — not 'all' variables)
- skills/react-testing/SKILL.md: instantiate QueryClient once outside the
wrapper closure so React Query cache survives re-renders (flaky-test fix)
- skills/react-testing/SKILL.md: restore console.error spy with mockRestore()
in a try/finally so the mock does not leak across tests
- commands/react-test.md: switch outer example-session fence to 4 backticks
so the inner ```tsx/```bash blocks don't prematurely terminate it
* fix(kiro): mirror react-build-resolver react 19 conditional remediation
Discussion r3272907106 flagged the kiro json variant still carrying the hardcoded
'npm i react@^19 react-dom@^19' line that the .md companion already dropped.
Replace with the same conditional, version-agnostic guidance so both variants
stay in sync.
* fix(react): bump react-build example session fence to 4 backticks
Discussion r3272907144 flagged the same nested-fence issue in
commands/react-build.md that we fixed earlier in commands/react-test.md.
The outer triple-backtick text block was being prematurely terminated by
the inner bash/tsx fences inside the Example Session.
* fix(react): bump react-review example usage fence to 4 backticks
Discussion r3272907201 flagged the same nested-fence issue in
commands/react-review.md. The outer triple-backtick text block was
being prematurely terminated by the inner tsx/ts fences inside the
Example Usage transcript.
* fix(docs): clarify commands row as legacy shims in feature parity table
Discussion r3272912003: README comparison table said 'PASS: 78 commands'
while the install-section and quick-start prose use 'legacy command shims'.
Aligned the comparison-table cell to 'PASS: 78 commands (legacy shims)' so
the count word survives the catalog-validator regex while making the legacy
nature explicit.
Widened the catalog comparison-table commands regex to tolerate an optional
parenthetical after the count word, so both the existing 'X commands' and
the new 'X commands (legacy shims)' phrasings validate without breaking
older READMEs/translations.
* Update rules/react/security.md
Co-authored-by: cubic-dev-ai[bot] <191113872+cubic-dev-ai[bot]@users.noreply.github.com>
* fix(react): guard tsc in react-build-resolver diagnostic commands
Discussion r3288910205: the agent prompt instructed an unconditional
'tsc --noEmit -p tsconfig.json', which adds noise (or hard-fails) on
JavaScript-only projects with no tsconfig.json or no installed TypeScript.
Replaced with 'test -f tsconfig.json && npx --yes tsc --noEmit -p tsconfig.json'
in both variants:
- agents/react-build-resolver.md
- .kiro/agents/react-build-resolver.json (prompt string mirrored)
Mirrors the same guard already applied to commands/react-review.md in de135f61.
* fix(react): pin tsc resolution to local install in build resolver
Discussion r3289054157: previous fix used 'npx --yes tsc' which auto-installs
the latest TypeScript from npm when none is local, producing version drift
and non-reproducible typecheck results across machines.
Switched to 'npx --no-install tsc' in both variants so the diagnostic uses
only the project's pinned TypeScript and fails fast if it isn't installed:
- agents/react-build-resolver.md
- .kiro/agents/react-build-resolver.json (prompt string mirrored)
* feat(counts): resolve counts for agents, skills...
* fix(ci): regen command registry for golang-testing entry
Removes stale kotlin-patterns entry to satisfy command-registry:check.
* fix: keep local Claude settings out of React track PR
---------
Co-authored-by: AlexisLeDain <a.ledain@docoon.com>
Co-authored-by: cubic-dev-ai[bot] <191113872+cubic-dev-ai[bot]@users.noreply.github.com>
Co-authored-by: Affaan Mustafa <affaan@dcube.ai>")[#2024](https://github.com/affaan-m/ECC/pull/2024)

 |  |
|  |

**Language:** English | [Português (Brasil)](/affaan-m/ECC/blob/main/docs/pt-BR/README.md) | [简体中文](/affaan-m/ECC/blob/main/README.zh-CN.md) | [繁體中文](/affaan-m/ECC/blob/main/docs/zh-TW/README.md) | [日本語](/affaan-m/ECC/blob/main/docs/ja-JP/README.md) | [한국어](/affaan-m/ECC/blob/main/docs/ko-KR/README.md) | [Türkçe](/affaan-m/ECC/blob/main/docs/tr/README.md) | [Русский](/affaan-m/ECC/blob/main/docs/ru/README.md) | [Tiếng Việt](/affaan-m/ECC/blob/main/docs/vi-VN/README.md) | [ไทย](/affaan-m/ECC/blob/main/docs/th/README.md) | [Deutsch](/affaan-m/ECC/blob/main/docs/de-DE/README.md)

## ECC

[![ECC - the harness-native operator system for agentic work](/affaan-m/ECC/raw/main/assets/hero.png)](/affaan-m/ECC/blob/main/assets/hero.png)

> **182K+ stars** | **28K+ forks** | **170+ contributors** | **12+ language ecosystems** | **Cross-harness agent workflows**

* * *

**Language / 语言 / 語言 / Dil / Язык / Ngôn ngữ**

[**English**](/affaan-m/ECC/blob/main/README.md) | [Português (Brasil)](/affaan-m/ECC/blob/main/docs/pt-BR/README.md) | [简体中文](/affaan-m/ECC/blob/main/README.zh-CN.md) | [繁體中文](/affaan-m/ECC/blob/main/docs/zh-TW/README.md) | [日本語](/affaan-m/ECC/blob/main/docs/ja-JP/README.md) | [한국어](/affaan-m/ECC/blob/main/docs/ko-KR/README.md) | [Türkçe](/affaan-m/ECC/blob/main/docs/tr/README.md) | [Русский](/affaan-m/ECC/blob/main/docs/ru/README.md) | [Tiếng Việt](/affaan-m/ECC/blob/main/docs/vi-VN/README.md) | [ไทย](/affaan-m/ECC/blob/main/docs/th/README.md) | [Deutsch](/affaan-m/ECC/blob/main/docs/de-DE/README.md)

* * *

**The harness-native operator system for agentic work. Built from real-world multi-harness engineering workflows.**

Not just configs. A complete system: skills, instincts, memory optimization, continuous learning, security scanning, and research-first development. Production-ready agents, skills, hooks, rules, MCP configurations, and legacy command shims evolved over 10+ months of intensive daily use building real products.

Works across **Codex**, **Claude Code**, **Cursor**, **OpenCode**, **Gemini**, **Zed**, **GitHub Copilot**, and other AI agent harnesses.

ECC v2.0.0-rc.1 adds the public Hermes operator story on top of that reusable layer: start with the [Hermes setup guide](/affaan-m/ECC/blob/main/docs/HERMES-SETUP.md), then review the [rc.1 release notes](/affaan-m/ECC/blob/main/docs/releases/2.0.0-rc.1/release-notes.md) and [cross-harness architecture](/affaan-m/ECC/blob/main/docs/architecture/cross-harness.md).

* * *

<table><tbody><tr><td width="25%" align="center"><a href="https://ecc.tools/pricing"><strong>ECC Pro</strong><br><sub>Private repos · GitHub App · $19/seat/mo</sub></a></td><td width="25%" align="center"><a href="https://github.com/sponsors/affaan-m"><strong>Sponsor</strong><br><sub>Fund the OSS · From $5/mo</sub></a></td><td width="25%" align="center"><a href="https://github.com/affaan-m/ECC/discussions"><strong>Community</strong><br><sub>Discussions · Q&amp;A · Show &amp; Tell</sub></a></td><td width="25%" align="center"><a href="https://github.com/apps/ecc-tools"><strong>GitHub App</strong><br><sub>Install · PR audits · Free tier</sub></a></td></tr></tbody></table>

**OSS stays free.** This repo is MIT-licensed forever. ECC Pro is the hosted GitHub App for private repos. [Sponsors](https://github.com/sponsors/affaan-m) and [Pro subscribers](https://ecc.tools/pricing) fund the work — that's why a single maintainer ships weekly across 7 harnesses.

* * *

## The Guides

This repo is the raw code only. The guides explain everything.

<table><tbody><tr><td width="33%"><a href="https://x.com/affaanmustafa/status/2012378465664745795"><img src="/affaan-m/ECC/raw/main/assets/images/guides/shorthand-guide.png" alt="The Shorthand Guide to ECC"></a></td><td width="33%"><a href="https://x.com/affaanmustafa/status/2014040193557471352"><img src="/affaan-m/ECC/raw/main/assets/images/guides/longform-guide.png" alt="The Longform Guide to ECC"></a></td><td width="33%"><a href="https://x.com/affaanmustafa/status/2033263813387223421"><img src="/affaan-m/ECC/raw/main/assets/images/security/security-guide-header.png" alt="The Shorthand Guide to Everything Agentic Security"></a></td></tr><tr><td align="center"><b>Shorthand Guide</b><br>Setup, foundations, philosophy. <b>Read this first.</b></td><td align="center"><b>Longform Guide</b><br>Token optimization, memory persistence, evals, parallelization.</td><td align="center"><b>Security Guide</b><br>Attack vectors, sandboxing, sanitization, CVEs, AgentShield.</td></tr></tbody></table>

| Topic | What You'll Learn |
| --- | --- |
| Token Optimization | Model selection, system prompt slimming, background processes |
| Memory Persistence | Hooks that save/load context across sessions automatically |
| Continuous Learning | Auto-extract patterns from sessions into reusable skills |
| Verification Loops | Checkpoint vs continuous evals, grader types, pass@k metrics |
| Parallelization | Git worktrees, cascade method, when to scale instances |
| Subagent Orchestration | The context problem, iterative retrieval pattern |

* * *

## What's New

- **Dashboard GUI** — New Tkinter-based desktop application (`ecc_dashboard.py` or `npm run dashboard`) with dark/light theme toggle, font customization, and project logo in header and taskbar.
- **Public surface synced to the live repo** — metadata, catalog counts, plugin manifests, and install-facing docs now match the actual OSS surface: 63 agents, 249 skills, and 79 legacy command shims.
- **Operator and outbound workflow expansion** — `brand-voice`, `social-graph-ranker`, `connections-optimizer`, `customer-billing-ops`, `ecc-tools-cost-audit`, `google-workspace-ops`, `project-flow-ops`, and `workspace-surface-audit` round out the operator lane.
- **Media and launch tooling** — `manim-video`, `remotion-video-creation`, and upgraded social publishing surfaces make technical explainers and launch content part of the same system.
- **Framework and product surface growth** — `nestjs-patterns`, richer Codex/OpenCode install surfaces, and expanded cross-harness packaging keep the repo usable beyond Claude Code alone.
- **Itô prediction-market skill pack** — `ito-market-intelligence`, `ito-basket-compare`, `ito-trade-planner`, `ito-data-atlas-agent`, `prediction-market-oracle-research`, and `prediction-market-risk-review` add public, non-advisory market/basket workflows while keeping live Itô API access gated and separate from ECC Tools billing.
- **Optimization skill pack** — `parallel-execution-optimizer`, `benchmark-optimization-loop`, `data-throughput-accelerator`, `latency-critical-systems`, and `recursive-decision-ledger` turn repeated speed/recursion prompts into bounded benchmark, throughput, and decision-ledger workflows.
- **ECC 2.0 alpha is in-tree** — the Rust control-plane prototype in `ecc2/` now builds locally and exposes `dashboard`, `start`, `sessions`, `status`, `stop`, `resume`, and `daemon` commands. It is usable as an alpha, not yet a general release.
- **Operator status snapshots** — `ecc status --markdown --write status.md` turns the local state store into a portable handoff covering readiness, active sessions, skill-run health, install health, pending governance events, and linked work items from Linear/GitHub/handoffs. Use `ecc work-items upsert ...` for manual entries, `ecc work-items sync-github --repo owner/repo` for PR/issue queue state, and `ecc status --exit-code` to fail automation when readiness needs attention.
- **Ecosystem hardening** — AgentShield, ECC Tools cost controls, billing portal work, and website refreshes continue to ship around the core plugin instead of drifting into separate silos.

- **Selective install architecture** — Manifest-driven install pipeline with `install-plan.js` and `install-apply.js` for targeted component installation. State store tracks what's installed and enables incremental updates.
- **6 new agents** — `typescript-reviewer`, `pytorch-build-resolver`, `java-build-resolver`, `java-reviewer`, `kotlin-reviewer`, `kotlin-build-resolver` expand language coverage to 10 languages.
- **New skills** — `pytorch-patterns` for deep learning workflows, `documentation-lookup` for API reference research, `bun-runtime` and `nextjs-turbopack` for modern JS toolchains, plus 8 operational domain skills and `mcp-server-patterns`.
- **Session & state infrastructure** — SQLite state store with query CLI, session adapters for structured recording, skill evolution foundation for self-improving skills.
- **Orchestration overhaul** — Harness audit scoring made deterministic, orchestration status and launcher compatibility hardened, observer loop prevention with 5-layer guard.
- **Observer reliability** — Memory explosion fix with throttling and tail sampling, sandbox access fix, lazy-start logic, and re-entrancy guard.
- **12 language ecosystems** — New rules for Java, PHP, Perl, Kotlin/Android/KMP, C++, and Rust join existing TypeScript, Python, Go, and common rules.
- **Community contributions** — Korean and Chinese translations, biome hook optimization, video processing skills, operational skills, PowerShell installer, Antigravity IDE support.
- **CI hardening** — 19 test failure fixes, catalog count enforcement, install manifest validation, and full test suite green.

- **Harness-first release** — ECC is now explicitly framed as an agent harness performance system, not just a config pack.
- **Hook reliability overhaul** — SessionStart root fallback, Stop-phase session summaries, and script-based hooks replacing fragile inline one-liners.
- **Hook runtime controls** — `ECC_HOOK_PROFILE=minimal|standard|strict` and `ECC_DISABLED_HOOKS=...` for runtime gating without editing hook files.
- **New harness commands** — `/harness-audit`, `/loop-start`, `/loop-status`, `/quality-gate`, `/model-route`.
- **NanoClaw v2** — model routing, skill hot-load, session branch/search/export/compact/metrics.
- **Cross-harness parity** — behavior tightened across Claude Code, Cursor, OpenCode, and Codex app/CLI.
- **997 internal tests passing** — full suite green after hook/runtime refactor and compatibility updates.

- **Codex app + CLI support** — Direct `AGENTS.md` -based Codex support, installer targeting, and Codex docs
- **`frontend-slides` skill** — Zero-dependency HTML presentation builder with PPTX conversion guidance and strict viewport-fit rules
- **5 new generic business/content skills** — `article-writing`, `content-engine`, `market-research`, `investor-materials`, `investor-outreach`
- **Broader tool coverage** — Cursor, Codex, and OpenCode support tightened so the same repo ships cleanly across all major harnesses
- **992 internal tests** — Expanded validation and regression coverage across plugin, hooks, skills, and packaging

- **Codex CLI support** — New `/codex-setup` command generates `codex.md` for OpenAI Codex CLI compatibility
- **7 new skills** — `search-first`, `swift-actor-persistence`, `swift-protocol-di-testing`, `regex-vs-llm-structured-text`, `content-hash-cache-pattern`, `cost-aware-llm-pipeline`, `skill-stocktake`
- **AgentShield integration** — `/security-scan` skill runs AgentShield directly from Claude Code; 1282 tests, 102 rules
- **GitHub Marketplace** — ECC Tools GitHub App live at [github.com/marketplace/ecc-tools](https://github.com/marketplace/ecc-tools) with free/pro/enterprise tiers
- **30+ community PRs merged** — Contributions from 30 contributors across 6 languages
- **978 internal tests** — Expanded validation suite across agents, skills, commands, hooks, and rules

- **Fixed instinct import content loss** — `parse_instinct_file()` was silently dropping all content after frontmatter (Action, Evidence, Examples sections) during `/instinct-import`. ([#148](https://github.com/affaan-m/ECC/issues/148), [#161](https://github.com/affaan-m/ECC/pull/161))

- **Interactive installation wizard** — New `configure-ecc` skill provides guided setup with merge/overwrite detection
- **PM2 & multi-agent orchestration** — 6 new commands (`/pm2`, `/multi-plan`, `/multi-execute`, `/multi-backend`, `/multi-frontend`, `/multi-workflow`) for managing complex multi-service workflows
- **Multi-language rules architecture** — Rules restructured from flat files into `common/` + `typescript/` + `python/` + `golang/` directories. Install only the languages you need
- **Chinese (zh-CN) translations** — Complete translation of all agents, commands, skills, and rules (80+ files)
- **GitHub Sponsors support** — Sponsor the project via GitHub Sponsors
- **Enhanced CONTRIBUTING.md** — Detailed PR templates for each contribution type

- **Full OpenCode integration** — 12 agents, 24 commands, 16 skills with hook support via OpenCode's plugin system (20+ event types)
- **3 native custom tools** — run-tests, check-coverage, security-audit
- **LLM documentation** — `llms.txt` for comprehensive OpenCode docs

- **Python/Django support** — Django patterns, security, TDD, and verification skills
- **Java Spring Boot skills** — Patterns, security, TDD, and verification for Spring Boot
- **Session management** — `/sessions` command for session history
- **Continuous learning v2** — Instinct-based learning with confidence scoring, import/export, evolution

See the full changelog in [Releases](https://github.com/affaan-m/ECC/releases).

* * *

## Quick Start

Get up and running in under 2 minutes:

Most Claude Code users should use exactly one install path:

- **Recommended default:** install the Claude Code plugin, then copy only the rule folders you actually want.
- **Use the manual installer only if** you want finer-grained control, want to avoid the plugin path entirely, or your Claude Code build has trouble resolving the self-hosted marketplace entry.
- **Do not stack install methods.** The most common broken setup is: `/plugin install` first, then `install.sh --profile full` or `npx ecc-install --profile full` afterward.

If you already layered multiple installs and things look duplicated, skip straight to [Reset / Uninstall ECC](#reset--uninstall-ecc).

If hooks feel too global or you only want ECC's rules, agents, commands, and core workflow skills, skip the plugin and use the minimal manual profile:

```
./install.sh --profile minimal --target claude
```

```
.\install.ps1 --profile minimal --target claude
# or
npx ecc-install --profile minimal --target claude
```

This profile intentionally excludes `hooks-runtime`.

If you want the normal core profile but need hooks off, use:

```
./install.sh --profile core --without baseline:hooks --target claude
```

Add hooks later only if you want runtime enforcement:

```
./install.sh --target claude --modules hooks-runtime
```

If you are not sure which ECC profile or component to install, ask the packaged advisor from any project:

```
npx ecc consult "security reviews" --target claude
```

It returns matching components, related profiles, and preview/install commands. Use the preview command before installing if you want to inspect the exact file plan.

For production ML/MLOps workflows, keep the install opt-in and component-scoped:

```
npx ecc consult "mlops training model deployment" --target claude
npx ecc install --profile minimal --target claude --with capability:machine-learning
```

> NOTE: The plugin is convenient, but the OSS installer below is still the most reliable path if your Claude Code build has trouble resolving self-hosted marketplace entries.

```
# Add marketplace
/plugin marketplace add https://github.com/affaan-m/ECC

# Install plugin
/plugin install ecc@ecc
```

ECC now has three public identifiers, and they are not interchangeable:

- GitHub source repo: `affaan-m/ECC`
- Claude marketplace/plugin identifier: `ecc@ecc`
- npm package: `ecc-universal`

This is intentional. Anthropic marketplace/plugin installs are keyed by a canonical plugin identifier, so ECC uses `ecc@ecc` to keep tool names and slash-command namespaces short enough for strict Desktop/API validators. Older posts may still show the former long marketplace identifier; treat that as a legacy alias only. Separately, the npm package stayed on `ecc-universal`, so npm installs and marketplace installs intentionally use different names.

> WARNING: **Important:** Claude Code plugins cannot distribute `rules` automatically.
> 
> If you already installed ECC via `/plugin install`, **do not run `./install.sh --profile full`, `.\install.ps1 --profile full`, or `npx ecc-install --profile full` afterward**. The plugin already loads ECC skills, commands, and hooks. Running the full installer after a plugin install copies those same surfaces into your user directories and can create duplicate skills plus duplicate runtime behavior.
> 
> For plugin installs, manually copy only the `rules/` directories you want under `~/.claude/rules/ecc/`. Start with `rules/common` plus one language or framework pack you actually use. Do not copy every rules directory unless you explicitly want all of that context in Claude.
> 
> Use the full installer only when you are doing a fully manual ECC install instead of the plugin path.
> 
> If your local Claude setup was wiped or reset, that does not mean you need to repurchase ECC. Start with `node scripts/ecc.js list-installed`, then run `node scripts/ecc.js doctor` and `node scripts/ecc.js repair` before reinstalling anything. That usually restores ECC-managed files without rebuilding your setup. If the problem is account or marketplace access for ECC Tools, handle billing/account recovery separately.

```
# Clone the repo first
git clone https://github.com/affaan-m/ECC.git
cd ECC

# Install dependencies (pick your package manager)
npm install # or: pnpm install | yarn install | bun install

# Plugin install path: copy only ECC rules into an ECC-owned namespace
mkdir -p ~/.claude/rules/ecc
cp -R rules/common ~/.claude/rules/ecc/
cp -R rules/typescript ~/.claude/rules/ecc/

# Fully manual ECC install path (use this instead of /plugin install)
# ./install.sh --profile full
```

```
# Windows PowerShell

# Plugin install path: copy only ECC rules into an ECC-owned namespace
New-Item -ItemType Directory -Force -Path "$HOME/.claude/rules/ecc" | Out-Null
Copy-Item -Recurse rules/common "$HOME/.claude/rules/ecc/"
Copy-Item -Recurse rules/typescript "$HOME/.claude/rules/ecc/"

# Fully manual ECC install path (use this instead of /plugin install)
# .\install.ps1 --profile full
# npx ecc-install --profile full
```

For manual install instructions see the README in the `rules/` folder. When copying rules manually, copy the whole language directory (for example `rules/common` or `rules/golang`), not the files inside it, so relative references keep working and filenames do not collide.

Use this only if you are intentionally skipping the plugin path:

```
./install.sh --profile full
```

```
.\install.ps1 --profile full
# or
npx ecc-install --profile full
```

If you choose this path, stop there. Do not also run `/plugin install`.

If ECC feels duplicated, intrusive, or broken, do not keep reinstalling it on top of itself.

- **Plugin path:** remove the plugin from Claude Code, then delete the specific rule folders you manually copied under `~/.claude/rules/ecc/`.
- **Manual installer / CLI path:** from the repo root, preview removal first:

```
node scripts/uninstall.js --dry-run
```

Then remove ECC-managed files:

```
node scripts/uninstall.js
```

You can also use the lifecycle wrapper:

```
node scripts/ecc.js list-installed
node scripts/ecc.js doctor
node scripts/ecc.js repair
node scripts/ecc.js uninstall --dry-run
```

ECC only removes files recorded in its install-state. It will not delete unrelated files it did not install.

If you stacked methods, clean up in this order:

1.  Remove the Claude Code plugin install.
2.  Run the ECC uninstall command from the repo root to remove install-state-managed files.
3.  Delete any extra rule folders you copied manually and no longer want.
4.  Reinstall once, using a single path.

```
# Skills are the primary workflow surface.
# Existing slash-style command names still work while ECC migrates off commands/.

# Plugin install uses the canonical namespaced form
/ecc:plan "Add user authentication"

# Manual install keeps the shorter slash form:
# /plan "Add user authentication"

# Check available commands
/plugin list ecc@ecc
```

**That's it!** You now have access to 63 agents, 249 skills, and 79 legacy command shims.

### Dashboard GUI

Launch the desktop dashboard to visually explore ECC components:

```
npm run dashboard
# or
python3 ./ecc_dashboard.py
```

**Features:**

- Tabbed interface: Agents, Skills, Commands, Rules, Settings
- Dark/Light theme toggle
- Font customization (family & size)
- Project logo in header and taskbar
- Search and filter across all components

> WARNING: `multi-*` commands are **not** covered by the base plugin/rules install above.
> 
> To use `/multi-plan`, `/multi-execute`, `/multi-backend`, `/multi-frontend`, and `/multi-workflow`, you must also install the `ccg-workflow` runtime.
> 
> Initialize it with `npx ccg-workflow`.
> 
> That runtime provides the external dependencies these commands expect, including:
> 
> - `~/.claude/bin/codeagent-wrapper`
> - `~/.claude/.ccg/prompts/*`
> 
> Without `ccg-workflow`, these `multi-*` commands will not run correctly.

* * *

## Cross-Platform Support

This plugin now fully supports **Windows, macOS, and Linux**, alongside tight integration across major IDEs (Cursor, Zed, OpenCode, Antigravity) and CLI harnesses. All hooks and scripts have been rewritten in Node.js for maximum compatibility.

The plugin automatically detects your preferred package manager (npm, pnpm, yarn, or bun) with the following priority:

1.  **Environment variable**: `CLAUDE_PACKAGE_MANAGER`
2.  **Project config**: `.claude/package-manager.json`
3.  **package.json**: `packageManager` field
4.  **Lock file**: Detection from package-lock.json, yarn.lock, pnpm-lock.yaml, or bun.lockb
5.  **Global config**: `~/.claude/package-manager.json`
6.  **Fallback**: First available package manager

To set your preferred package manager:

```
# Via environment variable
export CLAUDE_PACKAGE_MANAGER=pnpm

# Via global config
node scripts/setup-package-manager.js --global pnpm

# Via project config
node scripts/setup-package-manager.js --project bun

# Detect current setting
node scripts/setup-package-manager.js --detect
```

Or use the `/setup-pm` command in Claude Code.

Use runtime flags to tune strictness or disable specific hooks temporarily:

```
# Hook strictness profile (default: standard)
export ECC_HOOK_PROFILE=standard

# Comma-separated hook IDs to disable
export ECC_DISABLED_HOOKS="pre:bash:tmux-reminder,post:edit:typecheck"

# Cap SessionStart additional context (default: 8000 chars)
export ECC_SESSION_START_MAX_CHARS=4000

# Disable SessionStart additional context entirely for low-context/local-model setups
export ECC_SESSION_START_CONTEXT=off

# Keep context/scope/loop warnings but suppress API-rate cost estimates
export ECC_CONTEXT_MONITOR_COST_WARNINGS=off
```

Windows PowerShell:

```
[Environment]::SetEnvironmentVariable('ECC_CONTEXT_MONITOR_COST_WARNINGS', 'off', 'User')
```

* * *

## What's Inside

This repo is a **Claude Code plugin** - install it directly or copy components manually.

```
ECC/
|-- .claude-plugin/ # Plugin and marketplace manifests
| |-- plugin.json # Plugin metadata and component paths
| |-- marketplace.json # Marketplace catalog for /plugin marketplace add
|
|-- agents/ # 63 specialized subagents for delegation
| |-- planner.md # Feature implementation planning
| |-- architect.md # System design decisions
| |-- tdd-guide.md # Test-driven development
| |-- code-reviewer.md # Quality and security review
| |-- security-reviewer.md # Vulnerability analysis
| |-- build-error-resolver.md
| |-- e2e-runner.md # Playwright E2E testing
| |-- refactor-cleaner.md  # Dead code cleanup
| |-- doc-updater.md # Documentation sync
| |-- docs-lookup.md # Documentation/API lookup
| |-- chief-of-staff.md # Communication triage and drafts
| |-- loop-operator.md # Autonomous loop execution
| |-- harness-optimizer.md # Harness config tuning
| |-- cpp-reviewer.md # C++ code review
| |-- cpp-build-resolver.md # C++ build error resolution
| |-- fsharp-reviewer.md # F# functional code review
| |-- go-reviewer.md # Go code review
| |-- go-build-resolver.md # Go build error resolution
| |-- python-reviewer.md # Python code review
| |-- database-reviewer.md # Database/Supabase review
| |-- typescript-reviewer.md # TypeScript/JavaScript code review
| |-- java-reviewer.md # Java/Spring Boot code review
| |-- java-build-resolver.md # Java/Maven/Gradle build errors
| |-- kotlin-reviewer.md # Kotlin/Android/KMP code review
| |-- kotlin-build-resolver.md # Kotlin/Gradle build errors
| |-- harmonyos-app-resolver.md # HarmonyOS/ArkTS app development
| |-- rust-reviewer.md # Rust code review
| |-- rust-build-resolver.md # Rust build error resolution
| |-- pytorch-build-resolver.md # PyTorch/CUDA training errors
| |-- mle-reviewer.md # Production ML pipeline, eval, serving, and monitoring review
|
|-- skills/ # Workflow definitions and domain knowledge
| |-- coding-standards/ # Language best practices
| |-- clickhouse-io/ # ClickHouse analytics, queries, data engineering
| |-- backend-patterns/ # API, database, caching patterns
| |-- frontend-patterns/ # React, Next.js patterns
| |-- frontend-slides/ # HTML slide decks and PPTX-to-web presentation workflows (NEW)
| |-- article-writing/ # Long-form writing in a supplied voice without generic AI tone (NEW)
| |-- content-engine/ # Multi-platform social content and repurposing workflows (NEW)
| |-- market-research/ # Source-attributed market, competitor, and investor research (NEW)
| |-- investor-materials/ # Pitch decks, one-pagers, memos, and financial models (NEW)
| |-- investor-outreach/ # Personalized fundraising outreach and follow-up (NEW)
| |-- continuous-learning/ # Legacy v1 Stop-hook pattern extraction
| |-- continuous-learning-v2/ # Instinct-based learning with confidence scoring
| |-- iterative-retrieval/ # Progressive context refinement for subagents
| |-- strategic-compact/ # Manual compaction suggestions (Longform Guide)
| |-- tdd-workflow/ # TDD methodology
| |-- security-review/ # Security checklist
| |-- eval-harness/ # Verification loop evaluation (Longform Guide)
| |-- verification-loop/ # Continuous verification (Longform Guide)
| |-- videodb/ # Video and audio: ingest, search, edit, generate, stream (NEW)
| |-- golang-patterns/ # Go idioms and best practices
| |-- golang-testing/ # Go testing patterns, TDD, benchmarks
| |-- cpp-coding-standards/ # C++ coding standards from C++ Core Guidelines (NEW)
| |-- cpp-testing/ # C++ testing with GoogleTest, CMake/CTest (NEW)
| |-- django-patterns/ # Django patterns, models, views (NEW)
| |-- django-security/ # Django security best practices (NEW)
| |-- django-tdd/ # Django TDD workflow (NEW)
| |-- django-verification/ # Django verification loops (NEW)
| |-- laravel-patterns/ # Laravel architecture patterns (NEW)
| |-- laravel-security/ # Laravel security best practices (NEW)
| |-- laravel-tdd/ # Laravel TDD workflow (NEW)
| |-- laravel-verification/ # Laravel verification loops (NEW)
| |-- python-patterns/ # Python idioms and best practices (NEW)
| |-- python-testing/ # Python testing with pytest (NEW)
| |-- quarkus-patterns/ # Java Quarkus patterns (NEW)
| |-- quarkus-security/ # Quarkus security (NEW)
| |-- quarkus-tdd/ # Quarkus TDD (NEW)
| |-- quarkus-verification/ # Quarkus verification (NEW)
| |-- springboot-patterns/ # Java Spring Boot patterns (NEW)
| |-- springboot-security/ # Spring Boot security (NEW)
| |-- springboot-tdd/ # Spring Boot TDD (NEW)
| |-- springboot-verification/ # Spring Boot verification (NEW)
| |-- configure-ecc/ # Interactive installation wizard (NEW)
| |-- security-scan/ # AgentShield security auditor integration (NEW)
| |-- java-coding-standards/ # Java coding standards (NEW)
| |-- jpa-patterns/ # JPA/Hibernate patterns (NEW)
| |-- postgres-patterns/ # PostgreSQL optimization patterns (NEW)
| |-- nutrient-document-processing/ # Document processing with Nutrient API (NEW)
| |-- docs/examples/project-guidelines-template.md  # Template for project-specific skills
| |-- database-migrations/ # Migration patterns (Prisma, Drizzle, Django, Go) (NEW)
| |-- api-design/ # REST API design, pagination, error responses (NEW)
| |-- deployment-patterns/ # CI/CD, Docker, health checks, rollbacks (NEW)
| |-- docker-patterns/ # Docker Compose, networking, volumes, container security (NEW)
| |-- e2e-testing/ # Playwright E2E patterns and Page Object Model (NEW)
| |-- content-hash-cache-pattern/  # SHA-256 content hash caching for file processing (NEW)
| |-- cost-aware-llm-pipeline/ # LLM cost optimization, model routing, budget tracking (NEW)
| |-- regex-vs-llm-structured-text/ # Decision framework: regex vs LLM for text parsing (NEW)
| |-- swift-actor-persistence/ # Thread-safe Swift data persistence with actors (NEW)
| |-- swift-protocol-di-testing/ # Protocol-based DI for testable Swift code (NEW)
| |-- search-first/ # Research-before-coding workflow (NEW)
| |-- skill-stocktake/ # Audit skills and commands for quality (NEW)
| |-- liquid-glass-design/ # iOS 26 Liquid Glass design system (NEW)
| |-- foundation-models-on-device/ # Apple on-device LLM with FoundationModels (NEW)
| |-- swift-concurrency-6-2/ # Swift 6.2 Approachable Concurrency (NEW)
| |-- mle-workflow/ # Production ML data contracts, evals, deployment, monitoring (NEW)
| |-- perl-patterns/ # Modern Perl 5.36+ idioms and best practices (NEW)
| |-- perl-security/ # Perl security patterns, taint mode, safe I/O (NEW)
| |-- perl-testing/ # Perl TDD with Test2::V0, prove, Devel::Cover (NEW)
| |-- autonomous-loops/ # Autonomous loop patterns: sequential pipelines, PR loops, DAG orchestration (NEW)
| |-- plankton-code-quality/ # Write-time code quality enforcement with Plankton hooks (NEW)
|
|-- commands/ # Maintained slash-entry compatibility; prefer skills/
| |-- plan.md # /plan - Implementation planning
| |-- code-review.md # /code-review - Quality review
| |-- build-fix.md # /build-fix - Fix build errors
| |-- refactor-clean.md # /refactor-clean - Dead code removal
| |-- quality-gate.md # /quality-gate - Verification gate
| |-- learn.md # /learn - Extract patterns mid-session (Longform Guide)
| |-- learn-eval.md # /learn-eval - Extract, evaluate, and save patterns (NEW)
| |-- checkpoint.md # /checkpoint - Save verification state (Longform Guide)
| |-- setup-pm.md # /setup-pm - Configure package manager
| |-- go-review.md # /go-review - Go code review (NEW)
| |-- go-test.md # /go-test - Go TDD workflow (NEW)
| |-- go-build.md # /go-build - Fix Go build errors (NEW)
| |-- skill-create.md # /skill-create - Generate skills from git history (NEW)
| |-- instinct-status.md  # /instinct-status - View learned instincts (NEW)
| |-- instinct-import.md  # /instinct-import - Import instincts (NEW)
| |-- instinct-export.md  # /instinct-export - Export instincts (NEW)
| |-- evolve.md # /evolve - Cluster instincts into skills
| |-- prune.md # /prune - Delete expired pending instincts (NEW)
| |-- pm2.md # /pm2 - PM2 service lifecycle management (NEW)
| |-- multi-plan.md # /multi-plan - Multi-agent task decomposition (NEW)
| |-- multi-execute.md # /multi-execute - Orchestrated multi-agent workflows (NEW)
| |-- multi-backend.md # /multi-backend - Backend multi-service orchestration (NEW)
| |-- multi-frontend.md # /multi-frontend - Frontend multi-service orchestration (NEW)
| |-- multi-workflow.md # /multi-workflow - General multi-service workflows (NEW)
| |-- sessions.md # /sessions - Session history management
| |-- test-coverage.md # /test-coverage - Test coverage analysis
| |-- update-docs.md # /update-docs - Update documentation
| |-- update-codemaps.md  # /update-codemaps - Update codemaps
| |-- python-review.md # /python-review - Python code review (NEW)
|-- legacy-command-shims/ # Opt-in archive for retired shims such as /tdd and /eval
| |-- tdd.md # /tdd - Prefer the tdd-workflow skill
| |-- e2e.md # /e2e - Prefer the e2e-testing skill
| |-- eval.md # /eval - Prefer the eval-harness skill
| |-- verify.md # /verify - Prefer the verification-loop skill
| |-- orchestrate.md # /orchestrate - Prefer dmux-workflows or multi-workflow
|
|-- rules/ # Always-follow guidelines (copy to ~/.claude/rules/ecc/)
| |-- README.md # Structure overview and installation guide
| |-- common/ # Language-agnostic principles
| | |-- coding-style.md # Immutability, file organization
| | |-- git-workflow.md # Commit format, PR process
| | |-- testing.md # TDD, 80% coverage requirement
| | |-- performance.md # Model selection, context management
| | |-- patterns.md # Design patterns, skeleton projects
| | |-- hooks.md # Hook architecture, TodoWrite
| | |-- agents.md # When to delegate to subagents
| | |-- security.md # Mandatory security checks
| |-- typescript/ # TypeScript/JavaScript specific
| |-- python/ # Python specific
| |-- golang/ # Go specific
| |-- swift/ # Swift specific
| |-- php/ # PHP specific (NEW)
| |-- arkts/ # HarmonyOS / ArkTS specific
|
|-- hooks/ # Trigger-based automations
| |-- README.md # Hook documentation, recipes, and customization guide
| |-- hooks.json # All hooks config (PreToolUse, PostToolUse, Stop, etc.)
| |-- memory-persistence/ # Session lifecycle hooks (Longform Guide)
| |-- strategic-compact/ # Compaction suggestions (Longform Guide)
|
|-- scripts/ # Cross-platform Node.js scripts (NEW)
| |-- lib/ # Shared utilities
| | |-- utils.js # Cross-platform file/path/system utilities
| | |-- package-manager.js # Package manager detection and selection
| |-- hooks/ # Hook implementations
| | |-- session-start.js # Load context on session start
| | |-- session-end.js # Save state on session end
| | |-- pre-compact.js # Pre-compaction state saving
| | |-- suggest-compact.js # Strategic compaction suggestions
| | |-- evaluate-session.js  # Extract patterns from sessions
| |-- setup-package-manager.js # Interactive PM setup
|
|-- tests/ # Test suite (NEW)
| |-- lib/ # Library tests
| |-- hooks/ # Hook tests
| |-- run-all.js # Run all tests
|
|-- contexts/ # Dynamic system prompt injection contexts (Longform Guide)
| |-- dev.md # Development mode context
| |-- review.md # Code review mode context
| |-- research.md # Research/exploration mode context
|
|-- examples/ # Example configurations and sessions
| |-- CLAUDE.md # Example project-level config
| |-- user-CLAUDE.md # Example user-level config
| |-- saas-nextjs-CLAUDE.md # Real-world SaaS (Next.js + Supabase + Stripe)
| |-- go-microservice-CLAUDE.md # Real-world Go microservice (gRPC + PostgreSQL)
| |-- django-api-CLAUDE.md # Real-world Django REST API (DRF + Celery)
| |-- laravel-api-CLAUDE.md # Real-world Laravel API (PostgreSQL + Redis) (NEW)
| |-- rust-api-CLAUDE.md # Real-world Rust API (Axum + SQLx + PostgreSQL) (NEW)
|
|-- mcp-configs/ # MCP server configurations
| |-- mcp-servers.json # GitHub, Supabase, Vercel, Railway, etc.
|
|-- ecc_dashboard.py  # Desktop GUI dashboard (Tkinter)
|
|-- assets/ # Assets for dashboard
| |-- images/
| |-- ecc-logo.png
|
|-- marketplace.json  # Self-hosted marketplace config (for /plugin marketplace add)
```

* * *

## Ecosystem Tools

### Skill Creator

Two ways to generate Claude Code skills from your repository:

Use the `/skill-create` command for local analysis without external services:

```
/skill-create # Analyze current repo
/skill-create --instincts # Also generate instincts for continuous-learning-v2
```

This analyzes your git history locally and generates SKILL.md files.

For advanced features (10k+ commits, auto-PRs, team sharing):

[Install GitHub App](https://github.com/apps/skill-creator) | [ecc.tools](https://ecc.tools)

```
# Comment on any issue:
/skill-creator analyze

# Or auto-triggers on push to default branch
```

Both options create:

- **SKILL.md files** - Ready-to-use skills for Claude Code
- **Instinct collections** - For continuous-learning-v2
- **Pattern extraction** - Learns from your commit history

> Built at the Claude Code Hackathon (Cerebral Valley x Anthropic, Feb 2026). 1282 tests, 98% coverage, 102 static analysis rules.

Scan your Claude Code configuration for vulnerabilities, misconfigurations, and injection risks.

```
# Quick scan (no install needed)
npx ecc-agentshield scan

# Auto-fix safe issues
npx ecc-agentshield scan --fix

# Deep analysis with three Opus 4.6 agents
npx ecc-agentshield scan --opus --stream

# Generate secure config from scratch
npx ecc-agentshield init
```

**What it scans:** CLAUDE.md, settings.json, MCP configs, hooks, agent definitions, and skills across 5 categories — secrets detection (14 patterns), permission auditing, hook injection analysis, MCP server risk profiling, and agent config review.

**The `--opus` flag** runs three Claude Opus 4.6 agents in a red-team/blue-team/auditor pipeline. The attacker finds exploit chains, the defender evaluates protections, and the auditor synthesizes both into a prioritized risk assessment. Adversarial reasoning, not just pattern matching.

**Output formats:** Terminal (color-graded A-F), JSON (CI pipelines), Markdown, HTML. Exit code 2 on critical findings for build gates.

Use `/security-scan` in Claude Code to run it, or add to CI with the [GitHub Action](https://github.com/affaan-m/agentshield).

[GitHub](https://github.com/affaan-m/agentshield) | [npm](https://www.npmjs.com/package/ecc-agentshield)

The instinct-based learning system automatically learns your patterns:

See `skills/continuous-learning-v2/` for full documentation. Keep `continuous-learning/` only when you explicitly want the legacy v1 Stop-hook learned-skill flow.

* * *

## Requirements

**Minimum version: v2.1.0 or later**

This plugin requires Claude Code CLI v2.1.0+ due to changes in how the plugin system handles hooks.

Check your version:

```
claude --version
```

> WARNING: **For Contributors:** Do NOT add a `"hooks"` field to `.claude-plugin/plugin.json`. This is enforced by a regression test.

Claude Code v2.1+ **automatically loads** `hooks/hooks.json` from any installed plugin by convention. Explicitly declaring it in `plugin.json` causes a duplicate detection error:

```
Duplicate hooks file detected: ./hooks/hooks.json resolves to already-loaded file
```

**History:** This has caused repeated fix/revert cycles in this repo ([#29](https://github.com/affaan-m/ECC/issues/29), [#52](https://github.com/affaan-m/ECC/issues/52), [#103](https://github.com/affaan-m/ECC/issues/103)). The behavior changed between Claude Code versions, leading to confusion. We now have a regression test to prevent this from being reintroduced.

* * *

## Installation

The easiest way to use this repo - install as a Claude Code plugin:

```
# Add this repo as a marketplace
/plugin marketplace add https://github.com/affaan-m/ECC

# Install the plugin
/plugin install ecc@ecc
```

Or add directly to your `~/.claude/settings.json`:

```
{
  "extraKnownMarketplaces": {
 "ecc": {
 "source": {
 "source": "github",
 "repo": "affaan-m/ECC"
 }
 }
  },
  "enabledPlugins": {
 "ecc@ecc": true
  }
}
```

This gives you instant access to all commands, agents, skills, and hooks.

> **Note:** The Claude Code plugin system does not support distributing `rules` via plugins ([upstream limitation](https://code.claude.com/docs/en/plugins-reference)). You need to install rules manually:
> 
> ```
> # Clone the repo first
> git clone https://github.com/affaan-m/ECC.git
> cd ECC
> 
> # Option A: User-level rules (applies to all projects)
> mkdir -p ~/.claude/rules/ecc
> cp -r rules/common ~/.claude/rules/ecc/
> cp -r rules/typescript ~/.claude/rules/ecc/ # pick your stack
> cp -r rules/python ~/.claude/rules/ecc/
> cp -r rules/golang ~/.claude/rules/ecc/
> cp -r rules/php ~/.claude/rules/ecc/
> 
> # Option B: Project-level rules (applies to current project only)
> mkdir -p .claude/rules/ecc
> cp -r rules/common .claude/rules/ecc/
> cp -r rules/typescript .claude/rules/ecc/ # pick your stack
> ```

* * *

If you prefer manual control over what's installed:

```
# Clone the repo
git clone https://github.com/affaan-m/ECC.git
cd ECC

# Copy agents to your Claude config
cp agents/*.md ~/.claude/agents/

# Copy rules directories (common + language-specific)
mkdir -p ~/.claude/rules/ecc
cp -r rules/common ~/.claude/rules/ecc/
cp -r rules/typescript ~/.claude/rules/ecc/ # pick your stack
cp -r rules/python ~/.claude/rules/ecc/
cp -r rules/golang ~/.claude/rules/ecc/
cp -r rules/php ~/.claude/rules/ecc/
cp -r rules/arkts ~/.claude/rules/ecc/

# Copy skills first (primary workflow surface)
# Recommended (new users): core/general skills only
mkdir -p ~/.claude/skills/ecc
cp -r .agents/skills/* ~/.claude/skills/ecc/
cp -r skills/search-first ~/.claude/skills/ecc/

# Optional: add niche/framework-specific skills only when needed
# for s in django-patterns django-tdd laravel-patterns springboot-patterns quarkus-patterns; do
# cp -r skills/$s ~/.claude/skills/ecc/
# done

# Optional: keep maintained slash-command compatibility during migration
mkdir -p ~/.claude/commands
cp commands/*.md ~/.claude/commands/

# Retired shims live in legacy-command-shims/commands/.
# Copy individual files from there only if you still need old names such as /tdd.
```

#### Install hooks

Do not copy the raw repo `hooks/hooks.json` into `~/.claude/settings.json` or `~/.claude/hooks/hooks.json`. That file is plugin/repo-oriented and is meant to be installed through the ECC installer or loaded as a plugin, so raw copying is not a supported manual install path.

Use the installer to install only the Claude hook runtime so command paths are rewritten correctly:

```
# macOS / Linux
bash ./install.sh --target claude --modules hooks-runtime
```

```
# Windows PowerShell
pwsh -File .\install.ps1 --target claude --modules hooks-runtime
```

That writes resolved hooks to `~/.claude/hooks/hooks.json` and leaves any existing `~/.claude/settings.json` untouched.

If you installed ECC via `/plugin install`, do not copy those hooks into `settings.json`. Claude Code v2.1+ already auto-loads plugin `hooks/hooks.json`, and duplicating them in `settings.json` causes duplicate execution and cross-platform hook conflicts.

Windows note: the Claude config directory is `%USERPROFILE%\\.claude`, not `~/claude`.

#### Configure MCPs

Claude plugin installs intentionally do not auto-enable ECC's bundled MCP server definitions. This avoids overlong plugin MCP tool names on strict third-party gateways while keeping manual MCP setup available.

Use Claude Code's `/mcp` command or CLI-managed MCP setup for live Claude Code server changes. Use `/mcp` for Claude Code runtime disables; Claude Code persists those choices in `~/.claude.json`.

For repo-local MCP access, copy desired MCP server definitions from `mcp-configs/mcp-servers.json` into a project-scoped `.mcp.json`.

If you already run your own copies of ECC-bundled MCPs, set:

```
export ECC_DISABLED_MCPS="github,context7,exa,playwright,sequential-thinking,memory"
```

ECC-managed install and Codex sync flows will skip or remove those bundled servers instead of re-adding duplicates. `ECC_DISABLED_MCPS` is an ECC install/sync filter, not a live Claude Code toggle.

**Important:** Replace `YOUR_*_HERE` placeholders with your actual API keys.

* * *

## Key Concepts

### Agents

Subagents handle delegated tasks with limited scope. Example:

```
---
name: code-reviewer
description: Reviews code for quality, security, and maintainability
tools: ["Read", "Grep", "Glob", "Bash"]
model: opus
---

You are a senior code reviewer...
```

### Skills

Skills are the primary workflow surface. They can be invoked directly, suggested automatically, and reused by agents. ECC still ships maintained `commands/` during migration, while retired short-name shims live under `legacy-command-shims/` for explicit opt-in only. New workflow development should land in `skills/` first.

```
# TDD Workflow

1. Define interfaces first
2. Write failing tests (RED)
3. Implement minimal code (GREEN)
4. Refactor (IMPROVE)
5. Verify 80%+ coverage
```

### Hooks

Hooks fire on tool events. Example - warn about console.log:

```
{
  "matcher": "tool == \"Edit\" && tool_input.file_path matches \"\\\\.(ts|tsx|js|jsx)$\"",
  "hooks": [{
 "type": "command",
 "command": "#!/bin/bash\ngrep -n 'console\\.log' \"$file_path\" && echo '[Hook] Remove console.log' >&2"
  }]
}
```

### Rules

Rules are always-follow guidelines, organized into `common/` (language-agnostic) + language-specific directories:

```
rules/
  common/ # Universal principles (always install)
  typescript/ # TS/JS specific patterns and tools
  python/ # Python specific patterns and tools
  golang/ # Go specific patterns and tools
  swift/ # Swift specific patterns and tools
  php/ # PHP specific patterns and tools
  arkts/ # HarmonyOS / ArkTS patterns and constraints
```

See [`rules/README.md`](/affaan-m/ECC/blob/main/rules/README.md) for installation and structure details.

* * *

Not sure where to start? Use this quick reference. Skills are the canonical workflow surface; maintained slash entries stay available for command-first workflows.

| I want to... | Use this surface | Agent used |
| --- | --- | --- |
| Plan a new feature | `/ecc:plan "Add auth"` | planner |
| Design system architecture | `/ecc:plan` + architect agent | architect |
| Write code with tests first | `tdd-workflow` skill | tdd-guide |
| Review code I just wrote | `/code-review` | code-reviewer |
| Fix a failing build | `/build-fix` | build-error-resolver |
| Run end-to-end tests | `e2e-testing` skill | e2e-runner |
| Find security vulnerabilities | `/security-scan` | security-reviewer |
| Remove dead code | `/refactor-clean` | refactor-cleaner |
| Update documentation | `/update-docs` | doc-updater |
| Review Go code | `/go-review` | go-reviewer |
| Review Python code | `/python-review` | python-reviewer |
| Review F# code | *(invoke `fsharp-reviewer` directly)* | fsharp-reviewer |
| Review TypeScript/JavaScript code | *(invoke `typescript-reviewer` directly)* | typescript-reviewer |
| Develop HarmonyOS apps | *(invoke `harmonyos-app-resolver` directly)* | harmonyos-app-resolver |
| Audit database queries | *(auto-delegated)* | database-reviewer |
| Review production ML changes | `mle-workflow` skill + `mle-reviewer` agent | mle-reviewer |

### Common Workflows

Slash forms below are shown where they remain part of the maintained command surface. Retired short-name shims such as `/tdd` and `/eval` live in `legacy-command-shims/` for explicit opt-in only.

**Starting a new feature:**

```
/ecc:plan "Add user authentication with OAuth"
 → planner creates implementation blueprint
tdd-workflow skill → tdd-guide enforces write-tests-first
/code-review → code-reviewer checks your work
```

**Fixing a bug:**

```
tdd-workflow skill → tdd-guide: write a failing test that reproduces it
 → implement the fix, verify test passes
/code-review → code-reviewer: catch regressions
```

**Preparing for production:**

```
/security-scan → security-reviewer: OWASP Top 10 audit
e2e-testing skill → e2e-runner: critical user flow tests
/test-coverage → verify 80%+ coverage
```

* * *

## FAQ

**How do I check which agents/commands are installed?**

```
/plugin list ecc@ecc
```

This shows all available agents, commands, and skills from the plugin.

**My hooks aren't working / I see "Duplicate hooks file" errors**

This is the most common issue. **Do NOT add a `"hooks"` field to `.claude-plugin/plugin.json`.** Claude Code v2.1+ automatically loads `hooks/hooks.json` from installed plugins. Explicitly declaring it causes duplicate detection errors. See [#29](https://github.com/affaan-m/ECC/issues/29), [#52](https://github.com/affaan-m/ECC/issues/52), [#103](https://github.com/affaan-m/ECC/issues/103).

**Can I use ECC with Claude Code on a custom API endpoint or model gateway?**

Yes. ECC does not hardcode Anthropic-hosted transport settings. It runs locally through Claude Code's normal CLI/plugin surface, so it works with:

- Anthropic-hosted Claude Code
- Official Claude Code gateway setups using `ANTHROPIC_BASE_URL` and `ANTHROPIC_AUTH_TOKEN`
- Compatible custom endpoints that speak the Anthropic API Claude Code expects

Minimal example:

```
export ANTHROPIC_BASE_URL=https://your-gateway.example.com
export ANTHROPIC_AUTH_TOKEN=your-token
claude
```

If your gateway remaps model names, configure that in Claude Code rather than in ECC. ECC's hooks, skills, commands, and rules are model-provider agnostic once the `claude` CLI is already working.

Official references:

- [Claude Code LLM gateway docs](https://docs.anthropic.com/en/docs/claude-code/llm-gateway)
- [Claude Code model configuration docs](https://docs.anthropic.com/en/docs/claude-code/model-config)

**My context window is shrinking / Claude is running out of context**

Too many MCP servers eat your context. Each MCP tool description consumes tokens from your 200k window, potentially reducing it to ~70k. SessionStart context is capped at 8000 characters by default; lower it with `ECC_SESSION_START_MAX_CHARS=4000` or disable it with `ECC_SESSION_START_CONTEXT=off` for local-model or low-context setups.

**Fix:** Disable unused MCPs from Claude Code with `/mcp`. Claude Code writes those runtime choices to `~/.claude.json`; `.claude/settings.json` and `.claude/settings.local.json` are not reliable toggles for already-loaded MCP servers.

Keep under 10 MCPs enabled and under 80 tools active.

**Can I use only some components (e.g., just agents)?**

Yes. Use Option 2 (manual installation) and copy only what you need:

```
# Just agents
cp agents/*.md ~/.claude/agents/

# Just rules
mkdir -p ~/.claude/rules/ecc/
cp -r rules/common ~/.claude/rules/ecc/
```

Each component is fully independent.

**Does this work with Cursor / OpenCode / Codex / Antigravity / GitHub Copilot?**

Yes. ECC is cross-platform:

- **Cursor**: Pre-translated configs in `.cursor/`. See [Cursor IDE Support](#cursor-ide-support).
- **Gemini CLI**: Experimental project-local support via `.gemini/GEMINI.md` and shared installer plumbing.
- **OpenCode**: Full plugin support in `.opencode/`. See [OpenCode Support](#opencode-support).
- **Codex**: First-class support for both macOS app and CLI, with adapter drift guards and SessionStart fallback. See PR [#257](https://github.com/affaan-m/ECC/pull/257).
- **GitHub Copilot (VS Code)**: Instruction and prompt layer via `.github/copilot-instructions.md`, `.vscode/settings.json`, and `.github/prompts/`. See [GitHub Copilot Support](#github-copilot-support).
- **Antigravity**: Tightly integrated setup for workflows, skills, and flattened rules in `.agent/`. See [Antigravity Guide](/affaan-m/ECC/blob/main/docs/ANTIGRAVITY-GUIDE.md).
- **JoyCode / CodeBuddy**: Project-local selective install adapters for commands, agents, skills, and flattened rules. See [JoyCode Adapter Guide](/affaan-m/ECC/blob/main/docs/JOYCODE-GUIDE.md).
- **Qwen CLI**: Home-directory selective install adapter for commands, agents, skills, rules, and Qwen config. See [Qwen CLI Adapter Guide](/affaan-m/ECC/blob/main/docs/QWEN-GUIDE.md).
- **Zed**: Project-local selective install adapter for `.zed/settings.json`, flattened rules, commands, agents, and skills.
- **Non-native harnesses**: Manual fallback path for Grok and similar interfaces. See [Manual Adaptation Guide](/affaan-m/ECC/blob/main/docs/MANUAL-ADAPTATION-GUIDE.md).
- **Claude Code**: Native — this is the primary target.

**How do I contribute a new skill or agent?**

See [CONTRIBUTING.md](/affaan-m/ECC/blob/main/CONTRIBUTING.md). The short version:

1.  Fork the repo
2.  Create your skill in `skills/your-skill-name/SKILL.md` (with YAML frontmatter)
3.  Or create an agent in `agents/your-agent.md`
4.  Submit a PR with a clear description of what it does and when to use it

* * *

## Running Tests

The plugin includes a comprehensive test suite:

```
# Run all tests
node tests/run-all.js

# Run individual test files
node tests/lib/utils.test.js
node tests/lib/package-manager.test.js
node tests/hooks/hooks.test.js
```

* * *

## Contributing

**Contributions are welcome and encouraged.**

This repo is meant to be a community resource. If you have:

- Useful agents or skills
- Clever hooks
- Better MCP configurations
- Improved rules

Please contribute! See [CONTRIBUTING.md](/affaan-m/ECC/blob/main/CONTRIBUTING.md) for guidelines.

- Language-specific skills (Rust, C#, Kotlin, Java) — Go, Python, Perl, Swift, TypeScript, and HarmonyOS/ArkTS already included
- Framework-specific configs (Rails, FastAPI) — Django, NestJS, Spring Boot, and Laravel already included
- DevOps agents (Kubernetes, Terraform, AWS, Docker)
- Testing strategies (different frameworks, visual regression)
- Domain-specific knowledge (ML, data engineering, mobile)

These are not bundled with ECC and are not audited by this repo, but they are worth knowing about if you are exploring the broader Claude Code skills ecosystem:

- [claude-seo](https://github.com/AgriciDaniel/claude-seo) — SEO-focused skill and agent collection
- [claude-ads](https://github.com/AgriciDaniel/claude-ads) — Ad-audit and paid-growth workflow collection
- [claude-cybersecurity](https://github.com/AgriciDaniel/claude-cybersecurity) — Security-oriented skill and agent collection

* * *

ECC provides Cursor IDE support with hooks, rules, agents, skills, commands, and MCP configs adapted for Cursor's project layout.

```
# macOS/Linux
./install.sh --target cursor typescript
./install.sh --target cursor python golang swift php
```

```
# Windows PowerShell
.\install.ps1 --target cursor typescript
.\install.ps1 --target cursor python golang swift php
```

### What's Included

| Component | Count | Details |
| --- | --- | --- |
| Hook Events | 15 | sessionStart, beforeShellExecution, afterFileEdit, beforeMCPExecution, beforeSubmitPrompt, and 10 more |
| Hook Scripts | 16 | Thin Node.js scripts delegating to `scripts/hooks/` via shared adapter |
| Rules | 34 | 9 common (alwaysApply) + 25 language-specific (TypeScript, Python, Go, Swift, PHP) |
| Agents | 48 | `.cursor/agents/ecc-*.md` when installed; prefixed to avoid collisions with user or marketplace agents |
| Skills | Shared + Bundled | `.cursor/skills/` for translated additions |
| Commands | Shared | `.cursor/commands/` if installed |
| MCP Config | Shared | `.cursor/mcp.json` if installed |

ECC does not install root `AGENTS.md` into `.cursor/`. Cursor treats nested `AGENTS.md` files as directory context, so copying ECC's repo identity into a host project would pollute that project.

Cursor-native loading behavior can vary by Cursor build. ECC installs agents as `.cursor/agents/ecc-*.md`; if your Cursor build does not expose project agents, those files still work as explicit reference definitions instead of hidden global prompt context.

Cursor has **more hook events than Claude Code** (20 vs 8). The `.cursor/hooks/adapter.js` module transforms Cursor's stdin JSON to Claude Code's format, allowing existing `scripts/hooks/*.js` to be reused without duplication.

```
Cursor stdin JSON → adapter.js → transforms → scripts/hooks/*.js
 (shared with Claude Code)
```

Key hooks:

- **beforeShellExecution** — Blocks dev servers outside tmux (exit 2), git push review
- **afterFileEdit** — Auto-format + TypeScript check + console.log warning
- **beforeSubmitPrompt** — Detects secrets (sk-, ghp\_, AKIA patterns) in prompts
- **beforeTabFileRead** — Blocks Tab from reading.env,.key,.pem files (exit 2)
- **beforeMCPExecution / afterMCPExecution** — MCP audit logging

### Rules Format

Cursor rules use YAML frontmatter with `description`, `globs`, and `alwaysApply`:

```
---
description: "TypeScript coding style extending common rules"
globs: ["**/*.ts", "**/*.tsx", "**/*.js", "**/*.jsx"]
alwaysApply: false
---
```

* * *

ECC provides **first-class Codex support** for both the macOS app and CLI, with a reference configuration, Codex-specific AGENTS.md supplement, and shared skills.

```
# Run Codex CLI in the repo — AGENTS.md and .codex/ are auto-detected
codex

# Automatic setup: sync ECC assets (AGENTS.md, skills, MCP servers) into ~/.codex
npm install && bash scripts/sync-ecc-to-codex.sh
# or: pnpm install && bash scripts/sync-ecc-to-codex.sh
# or: yarn install && bash scripts/sync-ecc-to-codex.sh
# or: bun install && bash scripts/sync-ecc-to-codex.sh

# Or manually: copy the reference config to your home directory
cp .codex/config.toml ~/.codex/config.toml
```

The sync script safely merges ECC MCP servers into your existing `~/.codex/config.toml` using an **add-only** strategy — it never removes or modifies your existing servers. Run with `--dry-run` to preview changes, or `--update-mcp` to force-refresh ECC servers to the latest recommended config.

For Context7, ECC uses the canonical Codex section name `[mcp_servers.context7]` while still launching the `@upstash/context7-mcp` package. If you already have a legacy `[mcp_servers.context7-mcp]` entry, `--update-mcp` migrates it to the canonical section name.

Codex macOS app:

- Open this repository as your workspace.
- The root `AGENTS.md` is auto-detected.
- `.codex/config.toml` and `.codex/agents/*.toml` work best when kept project-local.
- The reference `.codex/config.toml` intentionally does not pin `model` or `model_provider`, so Codex uses its own current default unless you override it.
- Optional: copy `.codex/config.toml` to `~/.codex/config.toml` for global defaults; keep the multi-agent role files project-local unless you also copy `.codex/agents/`.

### What's Included

| Component | Count | Details |
| --- | --- | --- |
| Config | 1 | `.codex/config.toml` — top-level approvals/sandbox/web\_search, MCP servers, notifications, profiles |
| AGENTS.md | 2 | Root (universal) + `.codex/AGENTS.md` (Codex-specific supplement) |
| Skills | 32 | `.agents/skills/` — SKILL.md + agents/openai.yaml per skill |
| MCP Servers | 6 | GitHub, Context7, Exa, Memory, Playwright, Sequential Thinking (7 with Supabase via `--update-mcp` sync) |
| Profiles | 2 | `strict` (read-only sandbox) and `yolo` (full auto-approve) |
| Agent Roles | 3 | `.codex/agents/` — explorer, reviewer, docs-researcher |

### Skills

Skills at `.agents/skills/` are auto-loaded by Codex:

Canonical Anthropic skills such as `claude-api`, `frontend-design`, and `skill-creator` are intentionally not re-bundled here. Install those from [`anthropics/skills`](https://github.com/anthropics/skills) when you want the official versions.

| Skill | Description |
| --- | --- |
| agent-introspection-debugging | Debug agent behavior, routing, and prompt boundaries |
| agent-sort | Sort agent catalogs and assignment surfaces |
| api-design | REST API design patterns |
| article-writing | Long-form writing from notes and voice references |
| backend-patterns | API design, database, caching |
| brand-voice | Source-derived writing style profiles from real content |
| bun-runtime | Bun as runtime, package manager, bundler, and test runner |
| coding-standards | Universal coding standards |
| content-engine | Platform-native social content and repurposing |
| crosspost | Multi-platform content distribution across X, LinkedIn, Threads |
| deep-research | Multi-source research with synthesis and source attribution |
| dmux-workflows | Multi-agent orchestration using tmux pane manager |
| documentation-lookup | Up-to-date library and framework docs via Context7 MCP |
| e2e-testing | Playwright E2E tests |
| eval-harness | Eval-driven development |
| everything-claude-code | Development conventions and patterns for the project |
| exa-search | Neural search via Exa MCP for web, code, company research |
| fal-ai-media | Unified media generation for images, video, and audio |
| frontend-patterns | React/Next.js patterns |
| frontend-slides | HTML presentations, PPTX conversion, visual style exploration |
| investor-materials | Decks, memos, models, and one-pagers |
| investor-outreach | Personalized outreach, follow-ups, and intro blurbs |
| market-research | Source-attributed market and competitor research |
| mcp-server-patterns | Build MCP servers with Node/TypeScript SDK |
| nextjs-turbopack | Next.js 16+ and Turbopack incremental bundling |
| product-capability | Translate product goals into scoped capability maps |
| security-review | Comprehensive security checklist |
| strategic-compact | Context management |
| tdd-workflow | Test-driven development with 80%+ coverage |
| verification-loop | Build, test, lint, typecheck, security |
| video-editing | AI-assisted video editing workflows with FFmpeg and Remotion |
| x-api | X/Twitter API integration for posting and analytics |

### Key Limitation

Codex does **not yet provide Claude-style hook execution parity**. ECC enforcement there is instruction-based via `AGENTS.md`, optional `model_instructions_file` overrides, and sandbox/approval settings.

### Multi-Agent Support

Current Codex builds support stable multi-agent workflows.

- Enable `features.multi_agent = true` in `.codex/config.toml`
- Define roles under `[agents.<name>]`
- Point each role at a file under `.codex/agents/`
- Use `/agent` in the CLI to inspect or steer child agents

ECC ships three sample role configs:

| Role | Purpose |
| --- | --- |
| `explorer` | Read-only codebase evidence gathering before edits |
| `reviewer` | Correctness, security, and missing-test review |
| `docs_researcher` | Documentation and API verification before release/docs changes |

* * *

## Zed Support

ECC provides Zed project support through a conservative `.zed` adapter for project-local settings, flattened rules, agents, commands, and skills.

```
./install.sh --profile minimal --target zed
```

```
.\install.ps1 --profile minimal --target zed
```

The adapter writes ECC-managed files under `.zed/` and keeps BYOK/OpenRouter credentials out of the repo. Configure Zed account or API keys through Zed's own settings UI or your local user settings.

* * *

## OpenCode Support

ECC provides **full OpenCode support** including plugins and hooks.

### Quick Start

```
# Install OpenCode
npm install -g opencode

# Run in the repository root
opencode
```

The configuration is automatically detected from `.opencode/opencode.json`.

### Feature Parity

| Feature | Claude Code | OpenCode | Status |
| --- | --- | --- | --- |
| Agents | PASS: 63 agents | PASS: 12 agents | **Claude Code leads** |
| Commands | PASS: 79 commands | PASS: 35 commands | **Claude Code leads** |
| Skills | PASS: 249 skills | PASS: 37 skills | **Claude Code leads** |
| Hooks | PASS: 8 event types | PASS: 11 events | **OpenCode has more!** |
| Rules | PASS: 29 rules | PASS: 13 instructions | **Claude Code leads** |
| MCP Servers | PASS: 14 servers | PASS: Full | **Full parity** |
| Custom Tools | PASS: Via hooks | PASS: 6 native tools | **OpenCode is better** |

OpenCode's plugin system is MORE sophisticated than Claude Code with 20+ event types:

| Claude Code Hook | OpenCode Plugin Event |
| --- | --- |
| PreToolUse | `tool.execute.before` |
| PostToolUse | `tool.execute.after` |
| Stop | `session.idle` |
| SessionStart | `session.created` |
| SessionEnd | `session.deleted` |

**Additional OpenCode events**: `file.edited`, `file.watcher.updated`, `message.updated`, `lsp.client.diagnostics`, `tui.toast.show`, and more.

| Command | Description |
| --- | --- |
| `/plan` | Create implementation plan |
| `/code-review` | Review code changes |
| `/build-fix` | Fix build errors |
| `/refactor-clean` | Remove dead code |
| `/learn` | Extract patterns from session |
| `/checkpoint` | Save verification state |
| `/quality-gate` | Run the maintained verification gate |
| `/update-docs` | Update documentation |
| `/update-codemaps` | Update codemaps |
| `/test-coverage` | Analyze coverage |
| `/go-review` | Go code review |
| `/go-test` | Go TDD workflow |
| `/go-build` | Fix Go build errors |
| `/python-review` | Python code review (PEP 8, type hints, security) |
| `/multi-plan` | Multi-model collaborative planning |
| `/multi-execute` | Multi-model collaborative execution |
| `/multi-backend` | Backend-focused multi-model workflow |
| `/multi-frontend` | Frontend-focused multi-model workflow |
| `/multi-workflow` | Full multi-model development workflow |
| `/pm2` | Auto-generate PM2 service commands |
| `/sessions` | Manage session history |
| `/skill-create` | Generate skills from git |
| `/instinct-status` | View learned instincts |
| `/instinct-import` | Import instincts |
| `/instinct-export` | Export instincts |
| `/evolve` | Cluster instincts into skills |
| `/promote` | Promote project instincts to global scope |
| `/projects` | List known projects and instinct stats |
| `/prune` | Delete expired pending instincts (30d TTL) |
| `/learn-eval` | Extract and evaluate patterns before saving |
| `/setup-pm` | Configure package manager |
| `/harness-audit` | Audit harness reliability, eval readiness, and risk posture |
| `/loop-start` | Start controlled agentic loop execution pattern |
| `/loop-status` | Inspect active loop status and checkpoints |
| `/quality-gate` | Run quality gate checks for paths or entire repo |
| `/model-route` | Route tasks to models by complexity and budget |

### Plugin Installation

**Option 1: Use directly**

```
cd ECC
opencode
```

**Option 2: Install as npm package**

```
npm install ecc-universal
```

Then add to your `opencode.json`:

```
{
  "plugin": ["ecc-universal"]
}
```

That npm plugin entry enables ECC's published OpenCode plugin module (hooks/events and plugin tools). It does **not** automatically add ECC's full command/agent/instruction catalog to your project config.

For the full ECC OpenCode setup, either:

- run OpenCode inside this repository, or
- copy the bundled `.opencode/` config assets into your project and wire the `instructions`, `agent`, and `command` entries in `opencode.json`

### Documentation

- **Migration Guide**: `.opencode/MIGRATION.md`
- **OpenCode Plugin README**: `.opencode/README.md`
- **Consolidated Rules**: `.opencode/instructions/INSTRUCTIONS.md`
- **LLM Documentation**: `llms.txt` (complete OpenCode docs for LLMs)

* * *

ECC provides **GitHub Copilot support** for VS Code via Copilot Chat's native instruction and prompt file system — no extra tooling required.

### What's Included

| Component | File | Purpose |
| --- | --- | --- |
| Core instructions | `.github/copilot-instructions.md` | Always-loaded rules: coding style, security, testing, git workflow |
| VS Code settings | `.vscode/settings.json` | Per-task instruction files for code gen, test gen, review, and commit messages |
| Plan prompt | `.github/prompts/plan.prompt.md` | Phased implementation planning |
| TDD prompt | `.github/prompts/tdd.prompt.md` | Red-Green-Improve cycle |
| Code review prompt | `.github/prompts/code-review.prompt.md` | Quality and security review |
| Security review prompt | `.github/prompts/security-review.prompt.md` | Deep OWASP-aligned security analysis |
| Build fix prompt | `.github/prompts/build-fix.prompt.md` | Systematic build and CI error resolution |
| Refactor prompt | `.github/prompts/refactor.prompt.md` | Dead code cleanup and simplification |

The files are already in place — open any repo that contains this project and GitHub Copilot Chat will automatically pick up `.github/copilot-instructions.md`. The committed `.vscode/settings.json` enables `chat.promptFiles` so VS Code can load the reusable prompts from `.github/prompts/`.

To use the workflow prompts in Copilot Chat:

1.  Open the Copilot Chat panel in VS Code.
2.  Click the **paperclip / attach** icon and select **Prompt...**, or type `/` and choose a prompt.
3.  Select the prompt (e.g. `plan`, `tdd`, `code-review`).

GitHub Copilot in VS Code reads two types of files automatically:

- **`.github/copilot-instructions.md`** — repository-level instructions, always injected into every Copilot Chat request. Contains ECC's core coding standards, security checklist, testing requirements, and git workflow.
- **`.github/prompts/*.prompt.md`** — reusable prompt files users invoke on demand. Each prompt walks Copilot through a specific ECC workflow (plan → TDD → review → ship).

The **`.vscode/settings.json`** adds per-task instruction overlays so Copilot receives the right context depending on whether you are generating code, writing tests, reviewing a selection, or drafting a commit message.

### Feature Coverage

| ECC Feature | Copilot equivalent |
| --- | --- |
| Coding standards | Always-on via `copilot-instructions.md` |
| Security checklist | Always-on + `security-review` prompt |
| Testing / TDD | Always-on + `tdd` prompt |
| Implementation planning | `plan` prompt |
| Code review | `code-review` prompt |
| Build error resolution | `build-fix` prompt |
| Refactoring | `refactor` prompt |
| Commit message format | Per-task instruction in `settings.json` |
| Hooks / automation | Not supported (Copilot has no hook system) |
| Agents / delegation | Not supported (Copilot has no subagent API) |

### Limitations

GitHub Copilot does not have a hook system or a subagent API, so ECC's hook automations (auto-format, TypeScript check, session persistence, dev-server guard) and agent delegation are unavailable. The instruction and prompt layer still brings the full ECC coding philosophy — standards, security, TDD, and workflow — into every Copilot Chat session.

* * *

ECC is the **first plugin to maximize every major AI coding tool**. Here's how each harness compares:

| Feature | Claude Code | Cursor IDE | Codex CLI | OpenCode | GitHub Copilot |
| --- | --- | --- | --- | --- | --- |
| **Agents** | 63 | Shared (AGENTS.md) | Shared (AGENTS.md) | 12 | N/A |
| **Commands** | 79 | Shared | Instruction-based | 35 | 6 prompts |
| **Skills** | 249 | Shared | 10 (native format) | 37 | Via instructions |
| **Hook Events** | 8 types | 15 types | None yet | 11 types | None |
| **Hook Scripts** | 20+ scripts | 16 scripts (DRY adapter) | N/A | Plugin hooks | N/A |
| **Rules** | 34 (common + lang) | 34 (YAML frontmatter) | Instruction-based | 13 instructions | 1 always-on file |
| **Custom Tools** | Via hooks | Via hooks | N/A | 6 native tools | N/A |
| **MCP Servers** | 14 | Shared (mcp.json) | 7 (auto-merged via TOML parser) | Full | N/A |
| **Config Format** | settings.json | hooks.json + rules/ | config.toml | opencode.json | copilot-instructions.md + settings.json |
| **Context File** | CLAUDE.md + AGENTS.md | AGENTS.md | AGENTS.md | AGENTS.md | copilot-instructions.md |
| **Secret Detection** | Hook-based | beforeSubmitPrompt hook | Sandbox-based | Hook-based | Instruction-based |
| **Auto-Format** | PostToolUse hook | afterFileEdit hook | N/A | file.edited hook | N/A |
| **Version** | Plugin | Plugin | Reference config | 2.0.0-rc.1 | Instruction layer |

**Key architectural decisions:**

- **AGENTS.md** at root is the universal cross-tool file (read by Claude Code, Cursor, Codex, and OpenCode — GitHub Copilot uses `.github/copilot-instructions.md` instead)
- **DRY adapter pattern** lets Cursor reuse Claude Code's hook scripts without duplication
- **Skills format** (SKILL.md with YAML frontmatter) works across Claude Code, Codex, and OpenCode
- Codex's lack of hooks is compensated by `AGENTS.md`, optional `model_instructions_file` overrides, and sandbox permissions

* * *

## Background

I've been using Claude Code since the experimental rollout. Won the Anthropic x Forum Ventures hackathon in Sep 2025 with [@DRodriguezFX](https://x.com/DRodriguezFX) — built [zenith.chat](https://zenith.chat) entirely using Claude Code.

These configs are battle-tested across multiple production applications.

* * *

## Token Optimization

Claude Code usage can be expensive if you don't manage token consumption. These settings significantly reduce costs without sacrificing quality.

### Recommended Settings

Add to `~/.claude/settings.json`:

```
{
  "model": "sonnet",
  "env": {
 "MAX_THINKING_TOKENS": "10000",
 "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "50"
  }
}
```

| Setting | Default | Recommended | Impact |
| --- | --- | --- | --- |
| `model` | opus | **sonnet** | ~60% cost reduction; handles 80%+ of coding tasks |
| `MAX_THINKING_TOKENS` | 31,999 | **10,000** | ~70% reduction in hidden thinking cost per request |
| `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` | 95 | **50** | Compacts earlier — better quality in long sessions |
| `ECC_CONTEXT_MONITOR_COST_WARNINGS` | on | **off for subscription users** | Suppresses agent-facing API-rate estimate warnings while keeping context/scope/loop warnings |

Switch to Opus only when you need deep architectural reasoning:

```
/model opus
```

| Command | When to Use |
| --- | --- |
| `/model sonnet` | Default for most tasks |
| `/model opus` | Complex architecture, debugging, deep reasoning |
| `/clear` | Between unrelated tasks (free, instant reset) |
| `/compact` | At logical task breakpoints (research done, milestone complete) |
| `/cost` | Monitor token spending during session |

If you use a Claude subscription and the context monitor's API-rate estimates are not useful, set `ECC_CONTEXT_MONITOR_COST_WARNINGS=off`. This only suppresses the agent-facing cost warnings; it does not disable context exhaustion, scope, or loop warnings.

### Strategic Compaction

The `strategic-compact` skill (included in this plugin) suggests `/compact` at logical breakpoints instead of relying on auto-compaction at 95% context. See `skills/strategic-compact/SKILL.md` for the full decision guide.

**When to compact:**

- After research/exploration, before implementation
- After completing a milestone, before starting the next
- After debugging, before continuing feature work
- After a failed approach, before trying a new one

**When NOT to compact:**

- Mid-implementation (you'll lose variable names, file paths, partial state)

**Critical:** Don't enable all MCPs at once. Each MCP tool description consumes tokens from your 200k window, potentially reducing it to ~70k.

- Keep under 10 MCPs enabled per project
- Keep under 80 tools active
- Use `/mcp` to disable unused Claude Code MCP servers; those runtime choices persist in `~/.claude.json`
- Use `ECC_DISABLED_MCPS` only to filter ECC-generated MCP configs during install/sync flows

Agent Teams spawns multiple context windows. Each teammate consumes tokens independently. Only use for tasks where parallelism provides clear value (multi-module work, parallel reviews). For simple sequential tasks, subagents are more token-efficient.

* * *

### Token Optimization

Hitting daily limits? See the **[Token Optimization Guide](/affaan-m/ECC/blob/main/docs/token-optimization.md)** for recommended settings and workflow tips.

Quick wins:

```
// ~/.claude/settings.json
{
  "model": "sonnet",
  "env": {
 "MAX_THINKING_TOKENS": "10000",
 "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "50",
 "CLAUDE_CODE_SUBAGENT_MODEL": "haiku"
  }
}
```

Use `/clear` between unrelated tasks, `/compact` at logical breakpoints, and `/cost` to monitor spending.

### Customization

These configs work for my workflow. You should:

1.  Start with what resonates
2.  Modify for your stack
3.  Remove what you don't use
4.  Add your own patterns

* * *

## Community Projects

Projects built on or inspired by ECC:

| Project | Description |
| --- | --- |
| [EVC](https://github.com/SaigonXIII/evc) | Marketing agent workspace — 42 commands for content operators, brand governance, and multi-channel publishing. [Visual overview](https://saigonxiii.github.io/evc). |
| [trading-skills](https://github.com/VictorVVedtion/trading-skills) | 68 trading-themed Claude Code skills with pre-trade review prompts and risk gates inspired by market operators. |

Built something with ECC? Open a PR to add it here.

* * *

## Sponsors

This project is free and open source. Sponsors help keep it maintained and growing.

[**Become a Sponsor**](https://github.com/sponsors/affaan-m) | [Sponsor Tiers](/affaan-m/ECC/blob/main/SPONSORS.md) | [Sponsorship Program](/affaan-m/ECC/blob/main/SPONSORING.md)

* * *

## Star History

[![Star History Chart](https://camo.githubusercontent.com/17589e705dc9b9e877e7e45acb7281c298fdc5a55f3e86d61fa1acf10677493a/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d61666661616e2d6d2f45434326747970653d44617465)](https://star-history.com/#affaan-m/ECC&Date)

* * *

## Links

- **Shorthand Guide (Start Here):**[The Shorthand Guide to Everything Claude Code](https://x.com/affaanmustafa/status/2012378465664745795)
- **Longform Guide (Advanced):**[The Longform Guide to Everything Claude Code](https://x.com/affaanmustafa/status/2014040193557471352)
- **Security Guide:**[Security Guide](/affaan-m/ECC/blob/main/the-security-guide.md) | [Thread](https://x.com/affaanmustafa/status/2033263813387223421)
- **Follow:**[@affaanmustafa](https://x.com/affaanmustafa)

* * *

## License

MIT - Use freely, modify as needed, contribute back if you can.

* * *

**Star this repo if it helps. Read both guides. Build something great.**

## Releases 13

[\+ 12 releases](/affaan-m/ECC/releases)

## Sponsor this project

- [**affaan-m** Affaan Mustafa](/affaan-m)

- [https://ecc.tools](https://ecc.tools)

[Learn more about GitHub Sponsors](/sponsors)

## Packages

No packages published