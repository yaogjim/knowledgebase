---
title: "2026-06-16_github_com_multica_ai_andrej_karpathy_skills_A_single_CLAUDE_"
source: "https://github.com/multica-ai/andrej-karpathy-skills"
author:
  - "[[@anthropic]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "#95"
  - "github"
  - "@anthropic"
  - "md"
---

# multica-ai/andrej-karpathy-skills: A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.

[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](/codespaces/new/multica-ai/andrej-karpathy-skills?resume=1)

| Name | Name | 
Last commit message

 | 

Last commit date

 |
| --- | --- | --- | --- |
| 

[Sync Chinese README with English version (add Cursor section) (](/multica-ai/andrej-karpathy-skills/commit/2c606141936f1eeef17fa3043a72095b4765b9c2)[#95](https://github.com/multica-ai/andrej-karpathy-skills/pull/95)[)](/multica-ai/andrej-karpathy-skills/commit/2c606141936f1eeef17fa3043a72095b4765b9c2)

[2c60614](/multica-ai/andrej-karpathy-skills/commit/2c606141936f1eeef17fa3043a72095b4765b9c2) ·

[28 Commits](/multica-ai/andrej-karpathy-skills/commits/main/)

 |
| 

[.claude-plugin](/multica-ai/andrej-karpathy-skills/tree/main/.claude-plugin ".claude-plugin")

 | 

[.claude-plugin](/multica-ai/andrej-karpathy-skills/tree/main/.claude-plugin ".claude-plugin")

 | 

[Fix plugin.json schema validation errors](/multica-ai/andrej-karpathy-skills/commit/68b67a5bd77bddcbe88704abd9211e1de14e0860 "Fix plugin.json schema validation errors
- Change author from string to object with name property
- Remove invalid displayName field
- Point skills to directory instead of file (auto-discovery)
Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>")

 |  |
| 

[.cursor/ rules](/multica-ai/andrej-karpathy-skills/tree/main/.cursor/rules "This path skips through empty directories")

 | 

[.cursor/ rules](/multica-ai/andrej-karpathy-skills/tree/main/.cursor/rules "This path skips through empty directories")

 |  |  |
| 

[skills/ karpathy-guidelines](/multica-ai/andrej-karpathy-skills/tree/main/skills/karpathy-guidelines "This path skips through empty directories")

 | 

[skills/ karpathy-guidelines](/multica-ai/andrej-karpathy-skills/tree/main/skills/karpathy-guidelines "This path skips through empty directories")

 | 

[refactor: restructure repo for skills.sh compatibility](/multica-ai/andrej-karpathy-skills/commit/64723a49ea6117894304eb491f0d32a60570bf45 "refactor: restructure repo for skills.sh compatibility")

 |  |
| 

[CLAUDE.md](/multica-ai/andrej-karpathy-skills/blob/main/CLAUDE.md "CLAUDE.md")

 | 

[CLAUDE.md](/multica-ai/andrej-karpathy-skills/blob/main/CLAUDE.md "CLAUDE.md")

 | 

[Add Karpathy-inspired Claude Code guidelines](/multica-ai/andrej-karpathy-skills/commit/8462496b34419f20b32778610571ac723e91f94c "Add Karpathy-inspired Claude Code guidelines
Behavioral guidelines to reduce common LLM coding mistakes:
1. Think Before Coding - surface assumptions and tradeoffs
2. Simplicity First - minimum code, nothing speculative
3. Surgical Changes - touch only what you must
4. Goal-Driven Execution - define success criteria, loop until verified
Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>")

 |  |
| 

[CURSOR.md](/multica-ai/andrej-karpathy-skills/blob/main/CURSOR.md "CURSOR.md")

 | 

[CURSOR.md](/multica-ai/andrej-karpathy-skills/blob/main/CURSOR.md "CURSOR.md")

 |  |  |
| 

[EXAMPLES.md](/multica-ai/andrej-karpathy-skills/blob/main/EXAMPLES.md "EXAMPLES.md")

 | 

[EXAMPLES.md](/multica-ai/andrej-karpathy-skills/blob/main/EXAMPLES.md "EXAMPLES.md")

 | 

[Add examples of coding principles and common mistakes](/multica-ai/andrej-karpathy-skills/commit/4f6e050640cb6039c3320774b8a7521684e135f2 "Add examples of coding principles and common mistakes
Add real-world code examples demonstrating principles of effective coding, highlighting common mistakes and their corrections.")

 |  |
| 

[README.md](/multica-ai/andrej-karpathy-skills/blob/main/README.md "README.md")

 | 

[README.md](/multica-ai/andrej-karpathy-skills/blob/main/README.md "README.md")

 |  |  |
| 

[README.zh.md](/multica-ai/andrej-karpathy-skills/blob/main/README.zh.md "README.zh.md")

 | 

[README.zh.md](/multica-ai/andrej-karpathy-skills/blob/main/README.zh.md "README.zh.md")

 | 

[Sync Chinese README with English version (add Cursor section) (](/multica-ai/andrej-karpathy-skills/commit/2c606141936f1eeef17fa3043a72095b4765b9c2 "Sync Chinese README with English version (add Cursor section) (#95)")[#95](https://github.com/multica-ai/andrej-karpathy-skills/pull/95)[)](/multica-ai/andrej-karpathy-skills/commit/2c606141936f1eeef17fa3043a72095b4765b9c2 "Sync Chinese README with English version (add Cursor section) (#95)")

 |  |
|  |

> Check out my new project [Multica](https://github.com/multica-ai/multica) — an open-source platform for running and managing coding agents with reusable skills.
> 
> Follow me on X: [https://x.com/jiayuan\_jy](https://x.com/jiayuan_jy)

A single `CLAUDE.md` file to improve Claude Code behavior, derived from [Andrej Karpathy's observations](https://x.com/karpathy/status/2015883857489522876) on LLM coding pitfalls.

English | [简体中文](/multica-ai/andrej-karpathy-skills/blob/main/README.zh.md)

## The Problems

From Andrej's post:

> "The models make wrong assumptions on your behalf and just run along with them without checking. They don't manage their confusion, don't seek clarifications, don't surface inconsistencies, don't present tradeoffs, don't push back when they should."

> "They really like to overcomplicate code and APIs, bloat abstractions, don't clean up dead code... implement a bloated construction over 1000 lines when 100 would do."

> "They still sometimes change/remove comments and code they don't sufficiently understand as side effects, even if orthogonal to the task."

## The Solution

Four principles in one file that directly address these issues:

| Principle | Addresses |
| --- | --- |
| **Think Before Coding** | Wrong assumptions, hidden confusion, missing tradeoffs |
| **Simplicity First** | Overcomplication, bloated abstractions |
| **Surgical Changes** | Orthogonal edits, touching code you shouldn't |
| **Goal-Driven Execution** | Leverage through tests-first, verifiable success criteria |

**Don't assume. Don't hide confusion. Surface tradeoffs.**

LLMs often pick an interpretation silently and run with it. This principle forces explicit reasoning:

- **State assumptions explicitly** — If uncertain, ask rather than guess
- **Present multiple interpretations** — Don't pick silently when ambiguity exists
- **Push back when warranted** — If a simpler approach exists, say so
- **Stop when confused** — Name what's unclear and ask for clarification

**Minimum code that solves the problem. Nothing speculative.**

Combat the tendency toward overengineering:

- No features beyond what was asked
- No abstractions for single-use code
- No "flexibility" or "configurability" that wasn't requested
- No error handling for impossible scenarios
- If 200 lines could be 50, rewrite it

**The test:** Would a senior engineer say this is overcomplicated? If yes, simplify.

**Touch only what you must. Clean up only your own mess.**

When editing existing code:

- Don't "improve" adjacent code, comments, or formatting
- Don't refactor things that aren't broken
- Match existing style, even if you'd do it differently
- If you notice unrelated dead code, mention it — don't delete it

When your changes create orphans:

- Remove imports/variables/functions that YOUR changes made unused
- Don't remove pre-existing dead code unless asked

**The test:** Every changed line should trace directly to the user's request.

**Define success criteria. Loop until verified.**

Transform imperative tasks into verifiable goals:

| Instead of... | Transform to... |
| --- | --- |
| "Add validation" | "Write tests for invalid inputs, then make them pass" |
| "Fix the bug" | "Write a test that reproduces it, then make it pass" |
| "Refactor X" | "Ensure tests pass before and after" |

For multi-step tasks, state a brief plan:

```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let the LLM loop independently. Weak criteria ("make it work") require constant clarification.

## Install

**Option A: Claude Code Plugin (recommended)**

From within Claude Code, first add the marketplace:

```
/plugin marketplace add forrestchang/andrej-karpathy-skills
```

Then install the plugin:

```
/plugin install andrej-karpathy-skills@karpathy-skills
```

This installs the guidelines as a Claude Code plugin, making the skill available across all your projects.

**Option B: CLAUDE.md (per-project)**

New project:

```
curl -o CLAUDE.md https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md
```

Existing project (append):

```
echo "" >> CLAUDE.md
curl https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md >> CLAUDE.md
```

This repository includes a committed Cursor project rule ([`.cursor/rules/karpathy-guidelines.mdc`](/multica-ai/andrej-karpathy-skills/blob/main/.cursor/rules/karpathy-guidelines.mdc)) so the same guidelines apply when you open the project in Cursor. See **[CURSOR.md](/multica-ai/andrej-karpathy-skills/blob/main/CURSOR.md)** for setup, using the rule in other projects, and how this relates to Claude Code.

## Key Insight

From Andrej:

> "LLMs are exceptionally good at looping until they meet specific goals... Don't tell it what to do, give it success criteria and watch it go."

The "Goal-Driven Execution" principle captures this: transform imperative instructions into declarative goals with verification loops.

These guidelines are working if you see:

- **Fewer unnecessary changes in diffs** — Only requested changes appear
- **Fewer rewrites due to overcomplication** — Code is simple the first time
- **Clarifying questions come before implementation** — Not after mistakes
- **Clean, minimal PRs** — No drive-by refactoring or "improvements"

## Customization

These guidelines are designed to be merged with project-specific instructions. Add them to your existing `CLAUDE.md` or create a new one.

For project-specific rules, add sections like:

```
## Project-Specific Guidelines

- Use TypeScript strict mode
- All API endpoints must have tests
- Follow the existing error handling patterns in `src/utils/errors.ts`
```

## Tradeoff Note

These guidelines bias toward **caution over speed**. For trivial tasks (simple typo fixes, obvious one-liners), use judgment — not every change needs the full rigor.

The goal is reducing costly mistakes on non-trivial work, not slowing down simple tasks.

## License

MIT

## Releases

No releases published

## Packages

No packages published