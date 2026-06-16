---
title: "2026-06-16_chenchengpro_陈成_每个做_AI_编码工具的团队都该认真看这个_https_t"
source: "https://x.com/chenchengpro/status/2036357008388239562"
author:
  - "[[@chenchengpro]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "x"
  - "@chenchengpro"
  - "\-"
  - "ai"
---

# 陈成: 每个做 AI 编码工具的团队都该认真看这个——https://t

**陈成**

每个做 AI 编码工具的团队都该认真看这个——[http://Factory.ai](http://Factory.ai) 发布了 Missions，从"对话式助手"跃迁到"自主工程系统"。

最反直觉的设计决策：不同环节用不同模型。Opus 4.6 做规划，Sonnet/Opus 写代码，GPT-5.3-Codex 跑验证，Kimi K2.5 做调研。没有一个模型通吃所有场景。这是对"单一模型万能论"最直接的否定——编排需要强推理，实现需要高效编码，验证需要精确理解，调研需要大上下文。按角色分配模型，每个环节拿到最优解。

架构上也很讲究：每个 worker 启动时拿到干净上下文，避免长链路下的注意力退化；验证层不只跑测试，还能模拟用户操作浏览器检查 UI 渲染；通过 git 协调所有交接，失败自动恢复。

数据很硬：中位任务跑 2 小时，37% 超 4 小时，14% 超 24 小时，最长一个任务跑了 16 天。每分钟持续消耗 4.5 万 token，单条消息 1.9 万 token——少说话，说重点。

用例也不再是"帮我写个函数"，而是"帮我建一个 CRM"、"把 PHP 项目迁移到 TypeScript"、"给这个无文档 API 补全测试覆盖"，甚至"COBOL 迁移到 Java Spring Boot"。这些是传统团队要花几周的工程项目。

最加分的一点：Factory 坦诚列出了未解决的问题——并行度与协调开销的平衡、长链路错误累积、worker 粒度优化。做产品的人在认真做，而不是只讲故事。

AI 编程的竞争维度变了，不再是"谁的补全更快"，而是"谁能自主跑完一个真实项目"。

[https://factory.ai/news/missions](https://factory.ai/news/missions)

[Factory | Agent-Native Software Development](https://t.co/YM6e8XbDNX)

![图片](https://pbs.twimg.com/card_img/2034874953225707522/fUTCIaH5?format=png&name=large)

* * *

### 热门回复

**@MicroSectors** ♥ 5.6K · 💬 0

$SHNY $DULL ±3X daily resetting GLD-linked ETNs.

**@Orange AI** ♥ 666 · 💬 78

大多数语音输入法都在变得越来越臃肿：

要登录、要订阅、要联网、要加一堆新功能，要学习一堆新交互。

世界，不应该这样。

输入，就应该专注。

于是我们做了 TypeNo。

TypeNo 是一款面向 macOS 的极简语音输入法：

\- 永远免费，永远开源

\- 本地模型，保护隐私

\- 轻量模型，节省内存

按下

**@Leo** ♥ 259 · 💬 6

Anthropic 的 Thariq 把他写的 Claude/Agent 技术文章做了一个索引，即将上 Claude 官方博客。几个核心观点：

\- Skills 是所有 agent 的基础抽象

\- Agent 应该用文件系统

\- Bash is all you need

\- Prompt caching 是最高 alpha

\- 构建 agent 是艺术不是科学

跑了半年 Claude

**@陈成** ♥ 226 · 💬 13

AI Coding 军备竞赛里，大家都在卷模型能力。但 Cursor 最新的技术博客揭示了一个被忽视的瓶颈：不是模型不够聪明，而是 grep 不够快。

在大型 monorepo 里，ripgrep 单次搜索要 15 秒以上。而 AI Agent

**@Ray Wang** ♥ 220 · 💬 1

Anthropic 新发的这篇多 Agent Harness 实践值得一读

借鉴 GAN（生成对抗网络）的思路，把 agent 拆成 Generator + Evaluator，解决两个关键问题：

上下文焦虑：模型在长任务中越来越差，接近 context 上限时会匆忙收工。解法不是 compaction（压缩对话），而是 context