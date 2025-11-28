---
title: "2025-11-26_Stephen4171127_我现在正在用_AI_SDK_进行着项目实施_具备极大的便利性_它不是_Agent_的最佳选择_我都是"
source: "https://x.com/Stephen4171127/status/1993287739542741256"
author:
  - "[[@Stephen4171127]]"
published: 2025-11-26
created: 2025-11-26
description:
tags:
  - "x"
  - "@Stephen4171127"
  - "agent"
  - "sdk"
---

# 我现在正在用 AI SDK 进行着项目实施，具备极大的便利性，它不是 Agent 的最佳选择，我都是

**熊布朗** @Stephen4171127 2025-11-23

我现在正在用 AI SDK 进行着项目实施，具备极大的便利性，它不是 Agent 的最佳选择，我都是拿来当前端用。后端还是用 langgraph 或者其他更成熟的 Agent 框架，而不会直接用 AI SDK 的 Agent 组件。

——

另外，如果真的是要做 Agent，我更倾向于作者分享的用官方 SDK，比如 Claude Agent SDK。它经过官方模型的验证，经过 Claude Code 的验证，对于 Agent 不可或缺的tools 能力的发挥，更稳定、更方便。

——

Agent 还是要能自主决策的，gemini3、4.5 Opus的迭代更新让这件事从模型层面变得触手可达。

——

如果我今天做一个团队或者交付客户的 Agent 产品(我说的是 Agent，不是套壳的 AIGC 产品），如果能联网且不考虑 tokens 用量，我会先考虑 Claude Agent SDK + Skills 能不能快速实现，不满足才会考虑 langgraph

——

https://kit.deeptoai.com Try it. Powered by Claude Agent SDK

> 2025-11-23
> 
> 这篇文章分享了作者在构建 AI Agent 过程中的实践经验和教训，主要涵盖以下核心要点：
> 
> SDK 选择的反思作者
> 
> 团队最初选择了 Vercel AI SDK，但后来发现直接使用原生 SDK（如 Anthropic SDK）更合适。原因是：不同模型之间差异显著，需要自建 agent 抽象层；高层 SDK 在处理提供商侧工具（如 Anthropic

* * *

**Sam Song** @SamSongAI [2025-11-25](https://x.com/SamSongAI/status/1993296494015942969)

请教下熊佬Claudeagentsdk是在本地执行claudecodecli拿到输出结果后在前端进行渲染？所以拿到的是本地cli的能力是吧？包括MCP和skill

* * *

**熊布朗** @Stephen4171127 [2025-11-25](https://x.com/Stephen4171127/status/1993301328991600828)

不是，和 CLI 没关系，算是两个独立、平行、互不依赖的产品线。

* * *

**Keith** @keithhhchen [2025-11-25](https://x.com/keithhhchen/status/1993367150002946191)

请教下，Claude Agent SDK 怎么做部署？需要放沙盒/虚拟环境里吗？