---
title: "2026-03-06_陈成_陈成_OpenAI_昨天低调开源了一个框架_叫_Symphony_它能把你的_Line"
source: "https://x.com/chenchengpro/status/2029741601975849132"
author:
  - "[[@陈成]]"
published: 2026-03-06
created: 2026-03-06
description:
tags:
  - "x"
  - "@陈成"
  - "agent"
  - "symphony"
---

# 陈成 OpenAI 昨天低调开源了一个框架，叫 Symphony 🎵 它能把你的 Line

**陈成**

OpenAI 昨天低调开源了一个框架，叫 Symphony 🎵 它能把你的 Linear 看板变成一条全自动的研发流水线。 我扒了一遍代码，说说它到底怎么运作的 👇 1/ 核心逻辑只有一句话： 监控 Issue → 分配 Agent → 写代码 → 提 PR → 循环 2/ 技术栈是 Elixir，OTP 架构，天然支持多 Agent 并发。 每个 Issue 对应一个独立 Workspace，互不干扰。 3/ 最有意思的设计是 WORKFLOW.md： 把 Agent 的行为策略写进项目仓库，随代码一起提交、review、回滚。 Agent 怎么干活，团队说了算。 4/ 开源地址：[http://github.com/openai/symphony](http://github.com/openai/symphony) 你们团队用 Linear 吗？这东西值得试试。

[GitHub - openai/symphony: Symphony turns project work into isolated, autonomous implementation...](https://t.co/kSf9Ns9eUz)