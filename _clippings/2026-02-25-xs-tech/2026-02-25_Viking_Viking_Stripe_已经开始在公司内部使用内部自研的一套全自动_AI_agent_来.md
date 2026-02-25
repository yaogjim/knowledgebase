---
title: "2026-02-25_Viking_Viking_Stripe_已经开始在公司内部使用内部自研的一套全自动_AI_agent_来"
source: "https://x.com/vikingmute/status/2025910069083414769"
author:
  - "[[@Viking]]"
published: 2026-02-25
created: 2026-02-25
description:
tags:
  - "x"
  - "@Viking"
  - "ai"
---

# Viking Stripe 已经开始在公司内部使用内部自研的一套全自动 AI agent 来

**Viking**

Stripe 已经开始在公司内部使用内部自研的一套全自动 AI agent 来写代码了，每周能独立完成并被 merge 超过 1300 个 pull request（全 AI 写，人工 review），这套系统叫 Minions [https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents…](https://t.co/OB82okhncE) 大体流程： 1 工程师在 Slack 里 at bot + 描述任务，或贴上 issue/ticket 链接 2 系统立即启动一个隔离的 devbox，和人类工程师一样的 AWS EC2 开发环境，预先加载了完整的 Stripe 代码库 + 开发服务 3 在 LLM 真正开始思考前，就通过内部工具 MCP + Toolshed（400+ 个工具）自动、确定性地拉取上下文： \* Slack 完整对话线程 \* 相关 Jira/ticket 内容 \* Sourcegraph 代码搜索结果 \* 内部文档、设计文档 4 核心执行 5 代码修改 & 测试策略 \* 本地跑 linter 和部分测试 \* 改完代码 → git push → 触发完整 CI（Stripe 有 300 万+ 测试用例） \* CI 失败 → 最多允许 两次 CI 重试 \* 超过两次就停止，不无限循环 6 CI 通过后，Minions 按 Stripe 标准 PR 模板自动创建 Pull Request 人类工程师 review → 批准 → merge 未来在大公司里面纯 AI 写代码也应该不远了，有严格的流程来管理对应的过程，有人类工程师最后 reivew 把关。

* * *

### 热门回复

**@David Protein** ♥ 363 · 💬 74

The Optimal Protein for Your Optimal Form. David delivers the most protein for the fewest calories. With 28g of protein, 150 calories, and 0g of sugar, David is where discipline meets indulgence. Buy 4 cartons on our site, and get the 5th free.

**@Clerk** ♥ 58 · 💬 0

Launch with orgs + billing built-in. - Org invites - RBAC - Subscription billing Clerk helps your SaaS grow and monetize faster.

**@Boyuan (Nemo) Chen** ♥ 11 · 💬 0

1300 PRs/周听着吓人，但Stripe的codebase可能是全行业最适合AI写的——文档齐、测试覆盖高、模块边界清楚。大部分公司搬不走这套，瓶颈不是agent不行，是代码库本身不够AI-friendly

**@小龙** ♥ 6 · 💬 2

就怕 Ai 跑起来之后，人类程序员兜不住Ai堆得屎山啊。

**@Cater Wang** ♥ 6 · 💬 0

只怕瓶颈出现在review那个阶段哈，完全看不过来