---
title: "2026-03-02_Kevin_Ma_Kevin_Ma_我在考虑基于_Pi_OpenClaw_底层的极简_agent_框架_做一个"
source: "https://x.com/kevinma_dev_zh/status/2028129766944227560"
author:
  - "[[@Kevin Ma]]"
published: 2026-03-02
created: 2026-03-02
description:
tags:
  - "x"
  - "@Kevin Ma"
  - "agent"
  - "tech"
---

# Kevin Ma 我在考虑基于 Pi（OpenClaw 底层的极简 agent 框架）做一个

**Kevin Ma**

我在考虑基于 Pi（OpenClaw 底层的极简 agent 框架）做一个 tech team agent 自用。按照我自己的编排习惯来设计和实现，它的角色相当于 tech leader——理解我的需求和意图后，编写准确的提示词分发给 Claude Code、Codex CLI、Gemini CLI、Droid 等本地已配置好的工具，就像我坐在电脑前亲自给每个工具下指令一样。每个工具本身就是一个独立的 agent，Pi agent 做的是理解意图、拆解任务、编排调度。 模型选择上，可以参考 Amp Code 的设计思路——不同任务角色匹配不同模型，由 agent 根据任务性质自动选择最合适的工具和模型组合，而不是手动指定。 安全策略上，Pi 本身不做任何权限限制，需要自己在上层实现目录隔离和命令执行的安全边界，确保 agent 只能在指定的 codebase 目录中操作，禁止访问或执行其它目录的任何命令。 交互上分两种模式：不在电脑前时，通过 Telegram 远程给 Pi agent 下任务、看进展、给反馈；回到电脑前，不经过 Pi agent，直接按自己的习惯在各个工具中编排指令和任务。两种模式各自独立，互不影响。如果整个编排流程做的很丝滑了，也可以做个 TUI 或 GUI 版本，在电脑前使用。 总之，目标就是把这套东西打造成最趁手的开发环境。

* * *

### 热门回复

**@Joel Horwitz** ♥ 28 · 💬 4

Careful with AI, it tends to create more slop than solutions without the right guardrails. @Sourcegraph MCP reduces this risk factor by a very LARGE factor. Do yourself a favor and invest early in code intelligence now or clean up the mess later. AI agent tech debt compounds.

**@Markus** ♥ 3 · 💬 0

希望和你以后能交流这个话题，我的项目演示性的实现了多模型协作

**@jian** ♥ 3 · 💬 0

I already built exactly this and you can just use it - Teams of agents (manager, coder, reviewer, tester, etc) - Claude code, Codex, Opencode CLIs - Office visualization

**@智算爱德华** ♥ 0 · 💬 0

让 AI 当 tech leader，它会不会自己涨薪？准备怎么管住这群码农模型？

**@stacof** ♥ 0 · 💬 0

这个思路有意思，玩法一下子就多起来了 消耗token实现自己的一万种想法