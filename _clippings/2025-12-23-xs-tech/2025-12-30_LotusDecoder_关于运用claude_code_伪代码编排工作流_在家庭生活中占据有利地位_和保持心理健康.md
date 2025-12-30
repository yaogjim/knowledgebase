---
title: "2025-12-30_LotusDecoder_关于运用claude_code_伪代码编排工作流_在家庭生活中占据有利地位_和保持心理健康"
source: "https://x.com/LotusDecoder/status/2005469378532499612"
author:
  - "[[@LotusDecoder]]"
published: 2025-12-30
created: 2025-12-30
description:
tags:
  - "x"
  - "@LotusDecoder"
  - "gpt-search"
  - "code"
---

# 关于运用claude code 伪代码编排工作流， 在家庭生活中占据有利地位，和保持心理健康。 #

**LotusDecoder** @LotusDecoder [2025-12-29](https://x.com/LotusDecoder/status/2005469378532499612)

关于运用claude code 伪代码编排工作流，

在家庭生活中占据有利地位，和保持心理健康。

例子：

\# 任务：知心伙伴 + 多源信息融合

\## 变量定义

$开场 = "今天我遇到了老公不倒垃圾，我很烦恼"

$追问 = "所以说，我下一步是催老公做家务，还是自己改变自己心态，还是有什么别的办法？"

\## 并行准备（不阻塞聊天）

$经验 = grep @experiences/ "家务|夫妻|分工"

$数据 = /gpt-search "中国老公做家务的数据 2024" --context medium

\## 主流程

1\. /zhixin-new "$开场"

2\. \[等待回复后\] /zhixin "$追问。背景参考：$经验摘要，$数据摘要"

3\. /gpt-search "夫妻家务分歧创新型解决方案" → $创新方案（独立输出，不入聊天）

\## 最终输出

\- 知心伙伴对话记录

\- $创新方案（单独展示）

\--------------

\--------------

备注：

/zhixin 是已经搓好的 知心伙伴提示词前置首轮对话的 skills + command，背后直连 Opus-4.5 api，并不发送给 claude code ，以保证上下文干净，咨询能力满血。

/gpt-search 是直连 Gpt-5.2 + tool web search api。

/gpt-search 是直连 GPT-5.2 + 工具网页搜索 API。