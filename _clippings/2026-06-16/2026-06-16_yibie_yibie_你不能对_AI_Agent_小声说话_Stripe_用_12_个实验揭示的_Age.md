---
title: "2026-06-16_yibie_yibie_你不能对_AI_Agent_小声说话_Stripe_用_12_个实验揭示的_Agent_"
source: "https://x.com/yibie/status/2066359813240713285"
author:
  - "[[@yibie]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "#Stripe"
  - "#AIAgent"
  - "x"
  - "@yibie"
---

# yibie: # 你不能对 AI Agent 小声说话：Stripe 用 12 个实验揭示的 Agent 行为规律 Stripe 的 Minions 系列我们已经翻过两篇了

**yibie**

\# 你不能对 AI Agent 小声说话：Stripe 用 12 个实验揭示的 Agent 行为规律

Stripe 的 Minions 系列我们已经翻过两篇了。最近他们又发了一篇，不是讲怎么造 Agent，而是讲一个更底层的问题：\*\*Agent 到底是什么行为模式？你怎么让它做对的事？\*\*

两位作者——James Beswick（开发者关系负责人）和 Peter Epsteen（Growth 团队工程师）——跑了大约 12 个实验，核心问题只有一个：\*\*怎么让 AI Agent 正确使用 Stripe 的 API？\*\*

"正确"在这里的意思是：用最新 API 版本、遵循集成最佳实践、不写出隐含安全隐患的代码。

实验结果可以用一句话总结：\*\*AI Agent 不像勤奋的初级工程师。它像一个只读任务描述、其他什么都不看的合同工。\*\*

\---

\## 三类引导，三种结果

Stripe 把实验分成了三种引导方式，结果截然不同。

\### 1. 被动提示（Passive Hints）——全部无效

团队在 SDK 里嵌入了提示、在 API 响应里加了警告字段、在依赖目录里放了 AGENTS.md 文件——这些都是人类开发者自然会看到的地方。

\*\*全部被 Agent 忽略。\*\*

\- SDK 注释、README 补充、代码内联注释：Agent 不看

\- 依赖目录里的 AGENTS.md：Agent 几乎从不读取依赖文件夹里的文件

\- API 响应中的"警告哈希"字段：Agent 解析响应时只提取需要的数据，警告字段被当作噪音跳过

\*\*结论：Agent 不会浏览。它只会提取任务需要的最小信息，然后走。\*\*

\### 2. 主动提示（Active Prompts）——有效，但不保证

两种做法有明显效果：

\- \*\*模块化 skill 文件\*\*（把一个大文档拆成短小、聚焦的子文件，按需加载）：Agent 表现提升约 \*\*10%\*\*，token 消耗也下降了。

\- \*\*CLI 登录后的安装提示\*\*（\`stripe login\` 之后直接展示安装命令）：\*\*30-35%\*\* 的用户复制了安装命令。

\*\*结论：信息必须在 Agent 的必经路径上。不在路径上的东西，等于不存在。\*\*

\### 3. 硬信号（Hard Signals）——最有效

当 Agent 使用了过期的 API 版本时，如果返回的是一个"降级响应 + 礼貌警告"，Agent 不会修正。但如果返回的是一个\*\*明确的错误\*\*——"你用了 v1，当前是 v2，请修正"——Agent 可靠地检测到了错误、识别了版本不匹配、并修正了请求。

不需要读提示、不需要读文档。\*\*错误本身就是指令。\*\*

\---

\## 为什么软引导失效？

这 12 个实验揭示的不是一个技术限制，而是一个结构性特征：\*\*AI Agent 是超聚焦的任务完成器。它们扫描可操作数据，提取所需信息，然后继续往前走。\*\* 警告、提示、邻近文档、微妙的上下文线索——这些都在它们的优化函数之外。

Stripe 对这个现象有一个精确的命名：\*\*"hard versus soft steering"（硬引导 vs 软引导）。\*\*

软引导 = 任何不在 Agent 当前任务路径上的信息。Agent 看不到它，因为它没有理由去看。

硬引导 = Agent 为了完成任务必须处理的东西。一个错误、一个阻塞性提示、一段已经加载到上下文中的明确指令。

\*\*这不是内容质量问题，是分发问题。\*\* Stripe 的文档质量是业界公认的。问题在于 Agent 有没有实际加载它。

\---

\## 模块化设计的好处在人也在 Agent

一个意外收获：模块化的 skill 文件不仅在 Agent 表现上好于单一巨型文件，在可维护性上也更好。

支付团队维护支付的 skill。订阅团队维护订阅的 skill。\*\*对人类更好，对 Agent 也更好。\*\* 这是一个少见的、两个优化方向恰好一致的产品决策。

\---

\## 为什么这很重要

\### 1. 它解释了 Ponytail 为什么有效

回顾上一篇 Ponytail article 里的"梯子"逻辑——Agent 在写任何代码之前先问六个问题，在第一个能站稳的台阶停下。这本质上就是一种硬引导：它不是给 Agent "建议"，而是在它的推理路径上强制插入决策点。

\### 2. 它对所有做开发者工具的人都是一个信号

如果你在做一个会被 AI Agent 使用的 API 或 SDK，这篇实验告诉你：\*\*放在文档里是不够的。放在 SDk 注释里是不够的。Agent 的上下文加载路径和人类完全不同。\*\*

你需要把关键信息放在 Agent 必经的地方：错误消息、CLI 输出、MCP 工具描述。那些"人类会自己去翻文档"的假设在 Agent 时代不成立。

\### 3. 它暗示了一个被低估的技能：Agent 体验设计

我们讨论了很多"Agent 工程"——怎么让 Agent 更聪明、处理更长的上下文、更好地规划。但 Stripe 的这篇实验指向的是另一个方向：\*\*不是让 Agent 更聪明，而是让环境更适配 Agent 的认知模式。\*\*

就像 UX 设计理解人类怎么扫描页面、怎么点按钮，Agent 体验设计需要理解 Agent 怎么扫描信息、怎么加载上下文、在什么时候做决策。

\---

\## 局限

Stripe 明确说这不是正式研究论文，是观察性实验。没有公开样本量、置信区间、或测试的具体模型/框架。这些发现反映的是 2026 年初的 Agent 行为，Agent 进步很快，未来模型可能会更好地浏览上下文。

但核心结论——\*\*你不能对 Agent 小声说话\*\*——是一个不太可能随着模型进步而消失的结构性特征。Agent 优化的是任务完成，不是环境理解。这和模型聪明不聪明没关系，和目标函数的定义有关系。

\---

原文：[https://stripe.dev/blog/ai-steering-experiments…](https://stripe.dev/blog/ai-steering-experiments)

作者：James Beswick, Peter Epsteen (Stripe)

[#Stripe](/hashtag/Stripe?src=hashtag_click) [#AIAgent](/hashtag/AIAgent?src=hashtag_click) [#开发者体验](/hashtag/开发者体验?src=hashtag_click) [#Agent设计](/hashtag/Agent设计?src=hashtag_click)

[你不能对 AI 代理低语](https://t.co/VZ9ke7gwXf)

![图片](https://pbs.twimg.com/card_img/2064816072998477824/oCreKODv?format=jpg&name=large)

* * *

### 热门回复

**@yibie** ♥ 33 · 💬 1

一篇来自 Stripe 关于 Agent 的经典文章，值得一读再读：

\# Stripe 的 Minions：一次性端到端编码 Agent

在整个行业中，AI Agent 编码已经从新鲜事物变成了基本要求。随着底层模型的持续进步，无人值守的编码 Agent 已经从可能性变成了现实。

Minions 是 Stripe 自研的编码