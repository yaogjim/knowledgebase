---
title: "2026-06-16_AlphaSignalAI_规范驱动开发是人工智能编码的新默认做法"
source: "https://x.com/AlphaSignalAI/status/2057523186766377470"
author:
  - "[[@AlphaSignalAI]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "x"
  - "@AlphaSignalAI"
  - "code"
  - "ai"
---

# 规范驱动开发是人工智能编码的新默认做法

**AlphaSignal AI**

# 规范驱动开发是人工智能编码的新默认做法

## Top 5 repos defining it, the academic case for why, and who says it's wrong.

* * *

> In ~8 mins: what SDD is, why it became the default for AI coding, how the 5 leading repos implement it, and the one saying the whole category is wrong.

Spec-driven development crossed from blog-post topic to default architecture for AI coding in the last 12 months.

Thoughtworks、Martin Fowler、GitHub、Amazon 以及一份包含 67 个来源的学术综述都在 2025 年和 2026 年达成共识。

问题不再是是否使用 SDD，而是变成了哪种实现。

* * *

## 发生了什么

多个独立来源在18个月内汇聚到同一建议。

Thoughtworks 在《技术雷达》第 32 期中将规范驱动开发列为值得采用的技术。Martin Fowler 在他的网站上对此进行了介绍。

GitHub shipped Spec Kit, an MIT-licensed toolkit framed as the answer to vibe coding. Amazon launched Kiro, an agentic tool that walks users through requirements, design, and tasks before any code generation. Tessl launched at the radical end, with specs positioned as the new source code.

Red Hat published enterprise SDD guidance. InfoQ covered it at the architecture level.

Bryan Finster pushed back with the right critique. SDD is not a revolution, it's just BDD with branding.

That critique strengthens the case. The idea is not new. The context is.

BDD was an optional discipline that teams could adopt or ignore. With 84% of professional developers using or planning to use AI tools (Stack Overflow, 2025) and 46% of code output now AI-generated (GitHub, 2025), specification discipline became structurally necessary.

* * *

## Why it became necessary

Four academic papers landed in 12 months, mapping the same problem from different angles.

![Image](https://pbs.twimg.com/media/HI3JNVFWsAATNRO?format=jpg&name=large)

Sabry Farrag at the University of East London ran a 67-source systematic review of the productivity paradox. AI coding tools deliver real individual-level gains and real system-level damage at the same time.

Peng et al. measured 55.8% faster completion in a 95-developer RCT. Becker et al.'s METR study found a 19% slowdown for experienced developers working on mature codebases.

DORA reported that 25% AI adoption correlates with a 7.2% drop in delivery stability. Faros AI tracked over 10,000 developers and saw 98% more merged PRs, 91% more review time, and 9% more bugs.

Shuvendu Lahiri at Microsoft Research named the underlying gap. AI-generated code is plausible by construction, not correct by construction. The semantic distance between what a user means and what a program does is the central reliability bottleneck.

An AIware 2026 vision paper named a second gap. Code review evaluates plausibility, not compliance. Most AI-generated changes pass tests, look reasonable, and still drift from the rules they were supposed to follow.

Deepak Babu Piskala wrote the practitioner manual that ties it together. He frames SDD across three rigor levels and a four-phase workflow.

Farrag's economic argument closes the loop. Code generated for a specific codebase has high asset specificity. LLMs introduce high behavioral uncertainty.

Developers invoke AI hundreds of times daily. In Transaction Cost Economics terms, that combination makes a written, executable contract the rational governance response. SDD is that contract.

* * *

## How it actually works

![Image](https://pbs.twimg.com/media/HI3HfpjXEAAX1yd?format=jpg&name=large)

SDD compresses to three things a practitioner needs to hold.

A four-phase workflow. Specify what the software should do. Plan how to build it. Implement in small, validated increments. Validate that the code meets the spec. Each phase produces an artifact that constrains the next.

Three rigor levels. Spec-first means a specification is written before coding but may drift after. Spec-anchored means the spec lives alongside the code and tests enforce alignment. Spec-as-source means the spec is the only artifact humans edit, with code regenerated rather than manually changed.

A governance spectrum. Farrag's paper ranks four mechanisms by constraint intensity:

- Post-hoc review is the loosest, where a developer reviews AI output after the fact.
- Natural-language specification is next, putting requirements before generation.
- Executable contract follows, with tests and structured spec documents the agent must satisfy.
- Constitutional governance is the tightest, a meta-specification of non-negotiable principles that every change must honor.

The higher the asset specificity, behavioral uncertainty, and frequency, the further up the spectrum the rational choice sits. Production code in a mature codebase invoked by AI hundreds of times daily lands at constitutional. A throwaway prototype lands at post-hoc.

* * *

## The five SDD repos, by philosophy

Each repo encodes a different theory of where complexity belongs.

> Full comparison table at the end. Links are in replies.

![Image](https://pbs.twimg.com/media/HI3H9JIW0AAAWl0?format=jpg&name=large)

## Spec Kit: constitution as authority

GitHub 的官方工具包，MIT 授权，Python 命令行界面（指定初始化）。

The theory of complexity: put it in the constitution. A non-negotiable principles file at .specify/memory/constitution.md sits above every spec and every implementation. The agent obeys it on every change, every session.

The workflow runs through nine slash commands:

- /speckit.constitution
- /speckit.specify
- /speckit.clarify
- /speckit.plan
- /speckit.tasks
- /speckit.taskstoissues
- /speckit.checklist
- /speckit.analyze
- /speckit.implement

The constitution and analyze steps are where the formal governance lives.

Farrag's paper evaluates Spec Kit as the direct instantiation of constitutional governance. The reported result: 12 hours to 15 minutes for upstream artifact production (PRD, design, structure, technical specs, test plans).

A pilot study saw late-stage hotfixes drop from 3-to-5 per sprint to 1-to-2, and rollbacks drop from 2-to-4 per month to 0-to-1.

30+ AI agent integrations including Claude, Codex, Copilot, Cursor, Gemini.

This is the only repo with explicit constitutional governance. The highest tier on Farrag's spectrum, and the steepest setup cost.

* * *

## BMAD-METHOD: named agents as authority

BMad Code LLC, MIT, npm (npx bmad-method install). V6, with 34+ workflows.

The theory of complexity: put it in the roles. Six named personas, each with domain expertise:

- Analyst Mary handles brainstorming and research.
- PM John owns PRDs.
- Architect Winston runs the 8-step architecture workflow.
- Developer Amelia handles dev stories, sprint planning, and code review.
- UX Designer Sally owns interface decisions.
- Tech Writer Paige owns documentation.

Party Mode brings multiple personas into one session to argue from different professional perspectives.

The lifecycle has four phases: Analysis, Planning, Solutioning, Implementation. Each phase has its own workflows.

一个.decision-log.md 记录每个决策作为审计跟踪。实施就绪检查点（PASS、CONCERNS 或 FAIL）会在有任何缺失时阻止代码的提交。

规划深度会根据项目需求自动调整。业余项目只需 2 页的 PRD，发布项目则需完整规格说明。bmad-help 技能会回答关于下一步该做什么的自由格式问题。

The module ecosystem extends the core with specialized domains: BMM (core), BMB (custom agents), TEA (test architecture), BMGD (game dev), CIS (creative intelligence).

This is the only repo that treats specifications as the inter-agent communication protocol of a multi-agent organization.

* * *

## OpenSpec: change folders as the unit

Fission AI, MIT, npm (openspec init).

复杂性理论：将其融入变更中。每个功能都有自己的文件夹，其中包含 proposal.md（为什么进行此变更）、specs/（需求和场景）、design.md（技术方案）以及 tasks.md（实现清单）。

当变更发布时，/opsx:archive 将变更规范纳入一个不断增长的事实源文档。

The core surface is three commands:

- /opsx:propose creates the change folder.
- /opsx:apply has the AI implement the task checklist.
- /opsx:archive 完成它

一个可选择加入的扩展个人资料新增了六个：/opsx:new、/opsx:continue、/opsx:ff、/opsx:verify、/opsx:bulk-archive、/opsx:onboard。

The positioning is explicitly brownfield-first. Most SDD tools optimize for greenfield projects. OpenSpec is built to retrofit existing codebases. The delta-spec format (additions, modifications, removals tracked per change) is what makes that work.

Works with 25+ AI assistants via slash commands.

Executable contract at the lightest possible weight. No constitution, no named agents, no ceremony. The spec discipline survives without the process.

* * *

## GSD: context as the bottleneck

TÂCHES, MIT, npm (npx get-shit-done-cc@latest). Built by a solo developer for solo developers.

The theory of complexity: put it in context engineering. The main session context stays at 30 to 40 percent. Heavy work runs in fresh subagent contexts, each getting a full 200K-token window.

The hypothesis the rest of the architecture rests on: as a session grows, AI output degrades, so the architecture should keep the session small.

The loop is six commands:

- /gsd-new-project runs questions, research, requirements, roadmap.
- /gsd-map-codebase does the same for existing code.
- /gsd-discuss-phase captures decisions before planning.
- /gsd-plan-phase runs research, plan, verify in a loop.
- /gsd-execute-phase dispatches parallel waves of subagents.
- /gsd-verify-work walks through what was built and diagnoses failures.

五个持久化状态文件在会话边界之外仍然存在：PROJECT.md（愿景）、REQUIREMENTS.md（范围）、ROADMAP.md（方向）、STATE.md（当前位置）、CONTEXT.md（各阶段决策）。

The .planning/config.json controls mode (interactive or yolo), model profiles (quality, balanced, budget), and quality-agent toggles. Package legitimacy checks are built into the install path.

Executable contract delivered through context discipline rather than process ceremony. The repo treats the context window as the bottleneck, not the methodology.

* * *

## Superpowers: auto-triggering as discipline

Built by Jesse Vincent and Prime Radiant. MIT, zero-dependency plugin.

The theory of complexity: put it in the agent's behavior shaping. Skills auto-trigger at the right moments. No manual invocation. Mandatory workflows, not suggestions.

该 using-superpowers 技能在会话开始时加载，并且这是使自动触发功能生效的原因。仅复制技能文件并非真正的集成。

Seven core skills run the workflow:

- brainstorming refines rough ideas before any code.
- using-git-worktrees isolates the workspace.
- writing-plans breaks work into 2 to 5 minute tasks with exact file paths and complete code.
- subagent-driven-development dispatches a fresh subagent per task with two-stage review (spec compliance, then code quality).
- test-driven-development deletes any code written before its test.
- requesting-code-review blocks critical issues.
- finishing-a-development-branch verifies tests and presents merge options.

The TDD enforcement is the unusual move. Most TDD tooling encourages the loop. Superpowers' skill deletes code that violates it.

Distributed through the official Claude plugin marketplace, the official Codex plugin marketplace, Factory Droid, Gemini extensions, Cursor, GitHub Copilot CLI, and OpenCode.

Executable contract enforced at the agent layer rather than the user layer. The user never has to remember to invoke the right skill.

* * *

## The sixth repo, and the case against the category

Matt Pocock's Skills For Real Engineers sits on the same list of repos by accident. He argues against the category.

His talk Software Fundamentals Matter More Than Ever lands the thesis directly. "Code is not cheap. In fact, bad code is the most expensive it's ever been."

On the spec-driven movement specifically: "Specs to code, we are not investing in the design of the system. We are divesting from it."

His position rests on a software-engineering claim. Bad codebases have always been expensive because they resist change. AI accelerates that. A bad codebase compounded by AI throughput is the most expensive failure mode of the new era.

His repo is composable practices, not a workflow framework. Each skill stands alone:

- /grill-me runs a relentless interview to establish what Frederick Brooks calls a shared design concept.
- /grill-with-docs adds a Domain-Driven Design ubiquitous language file that humans and AI both reference.
- /tdd enforces red-green-refactor as the rate limiter on AI speed.
- /improve-codebase-architecture rebuilds shallow modules into deep modules, per John Ousterhout.

The default pattern is gray boxes: design the interface, delegate the implementation.

The data on his side: the METR finding that experienced developers on mature codebases were 19% slower with AI suggests the bottleneck is codebase quality, not specification quality. His argument is that the five SDD repos optimize for the wrong thing.

> 真实工程所需技能一个编码真实 Claude Code 工作流的 21 技能提示词集合，首先安装什么以及如何安装。 更新 4/29：仓库突破了 37k！并且刚刚发布了重大更新，附带一个全新的 README 文件……
> 
> — AlphaSignal AI
> 
> [https://x.com/AlphaSignalAI/status/2048809516993556845](https://x.com/AlphaSignalAI/status/2048809516993556845)
> 
> ![Square profile picture](https://pbs.twimg.com/profile_images/2014100845189529600/Ff1Xc28-_x96.jpg)![Article cover image](https://pbs.twimg.com/media/HG7O1xGaoAAhDbb?format=jpg&name=large)![Download](chrome-extension://jfphcjkiccfhcmggdncpidahnkfpngfa/blueicon.jpg)

他的代码仓库仅凭/grill-me 就迅速走红。这个职位值得认真对待。

* * *

![Image](https://pbs.twimg.com/media/HI3IbnqXMAACMYa?format=jpg&name=large)

* * *

## The AlphaSignal take

The five SDD repos and Pocock's dissent are not answering the same question.

SDD optimizes for the plausibility-to-correctness gap. Pocock optimizes for the design-entropy gap. Both gaps are real. Both data sets support both positions.

A team that picks one and ignores the other is solving half the problem.

The reliability case for SDD is strongest at the constitutional and executable-contract levels. Spec Kit's constitution mechanism and BMAD's implementation-readiness gate are where the math actually pays off.

The case is weakest at the natural-language end, where SDD collapses into renamed prompt engineering.

Three things none of the six repos solve, drawn from the open problems sections of the four papers.

Oracle adequacy. Current evaluations collapse model quality, tool reliability, and harness quality into one end-task number. There is no metric for what a specification is actually worth.

Evidence bundles. Every accepted change should ship with a record of what was checked, what was not, and what risks remain. No current SDD tool produces this.

Self-evolving harnesses. The SDD frameworks themselves are software. They will change. None of them have a change-contract for their own evolution.

Read each of these repos as a specific theory of where reliability comes from. Pick the one whose theory matches the bottleneck you actually have. If you don't know your bottleneck, Pocock's critique applies first.

* * *

Which theory of reliability does your stack depend on, constitution, roles, change folders, context, auto-triggering, or design discipline?

* * *

All source links are in the first reply.

Full breakdown of recent updates + daily signals in our newsletter (link in bio).