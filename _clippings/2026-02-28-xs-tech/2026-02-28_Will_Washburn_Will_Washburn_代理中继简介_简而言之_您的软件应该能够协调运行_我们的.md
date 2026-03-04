---
title: "2026-02-28_Will_Washburn_Will_Washburn_代理中继简介_简而言之_您的软件应该能够协调运行_我们的"
source: "https://x.com/willwashburn/status/2027536741456863504"
author:
  - "[[@Will Washburn]]"
published: 2026-02-28
created: 2026-02-28
description:
tags:
  - "x"
  - "@Will Washburn"
  - "relay"
  - "await"
---

# Will Washburn # 代理中继简介 简而言之： 您的软件应该能够协调运行。我们的

**Will Washburn**

# 代理中继简介

简而言之： 您的软件应该能够协调运行。我们的 SDK 可以帮助您实现这一点。

告诉我这听起来是不是很熟悉。

你打开了多个终端。一个代理正在构建计划，另一个正在执行计划。你像个非常有耐心的中层经理一样在它们之间切换。你从 CI 复制错误信息，然后粘贴到 Claude 中。你把 Codex 的反馈粘贴到 OpenCode 中。你按下回车键，表示同意 Claude 只运行一次 \`find . -type f -name "\*.ts" -print0 | xargs -0 grep -Hn "any"\` 命令。你的研究代理发现了一些有趣的东西，并将其写入 SUPER\_DETAILED\_RESEARCH.md 文档。你的计划器需要这个文档，但在粘贴 Markdown 后，计划器又发现了一些需要上下文的信息。于是你找到另一个终端，把 Markdown 复制回研究提示符。然后你调整计划。然后你调整运行计划的 Codex 终端。然后你检查输出。然后你又重新开始，因为它不太对劲。唉，又要压缩了？！天哪……我累死了。以前做软件开发很有趣！你知道什么不好玩吗？沦为一群法学硕士的豪华宣传巴士。

今天我很高兴向大家展示一种更好的方法，在这种方法中，你不再是瓶颈。

与其让你从中调解……如果他们能够互相交流呢？

## 

Agent Relay SDK

Relay 为多智能体系统提供了一个确定性的基础：

- 实时推送通信
 
- 生成和释放代理
 
- 频道、表情符号反应、已读回执——基本上就是 Slack，但专为无头代理打造。
 

Relay 并非定制线束，因此您可以根据自己的喜好进行配置。您的技能和配置应该能够直接使用。

想象一下让两个智能体玩井字棋。使用 Relay SDK，这很简单：

typescript

```typescript
import { AgentRelay, Models } from "@agent-relay/sdk";

const relay = new AgentRelay();

relay.onMessageReceived = (msg) =>
  console.log(`[${msg.from} → ${msg.to}]: ${msg.text}`);

const channel = ["tic-tac-toe"];

const x = await relay.claude.spawn({
  name: "PlayerX",
  model: Models.Claude.SONNET,
  channels: channel,
  task: "Play tic-tac-toe as X against PlayerO. You go first.",
});

const o = await relay.codex.spawn({
  name: "PlayerO",
  model: Models.Codex.GPT_5_3_CODEX_SPARK,
  channels: channel,
  task: "Play tic-tac-toe as O against PlayerX.",
});

await Promise.all([
  relay.waitForAgentReady("PlayerX"),
  relay.waitForAgentReady("PlayerO"),
]);

relay.system().sendMessage({ to: "PlayerX", text: "Start." });

await AgentRelay.waitForAny([x, o], 5 * 60 * 1000);
await relay.shutdown();
```

无需中继：

- 你需要在代理之间复制棋盘状态。
 
- 由你来决定轮到谁。
 
- 看着平局以慢动作发生，你会感到无聊和沮丧。
 

同样的简单方法也适用于其他更复杂的任务。对于长时间运行的工作流程，在工作进行过程中获得反馈非常有益；规划人员、执行人员和研究人员都可以讨论和评估后续计划， 而无需等待人说“k”。

当然，你可以观察并在需要时介入，但令人惊讶的是，这些特工即使没有你也能把事情做好。

## 

我们不是已经有次级代理商了吗？

虽然这感觉上与子代理人类似，但它们实际上截然不同，而且是互补的。

1.  子代理是层级式的（例如，父代理 → 子代理 → 结果）。这种结构适用于“执行此子任务”，但对于系统或长时间运行的任务来说就不适用了。当需要实时调整或获得反馈时该怎么办？借助 Relay，您仍然可以利用子代理（而且应该这样做！）来完成子任务。通过 Relay，您可以与子代理进行双向对话，从而达成共识。这通常有助于产生更具创造性和涌现性的解决方案。
 
2.  子代理无法跨提供商工作。您希望能够从多个提供商中选择最适合特定任务的模型，并且希望它能与其他代理无缝协作。
 

## 

开源且欢迎贡献

如果你觉得自己管理的工程团队节奏很快，但记忆力却很差……那么这篇文章就是为你准备的。请访问（或者直接让你的代理人访问）

[https://github.com/AgentWorkforce/relay](https://github.com/AgentWorkforce/relay)

试试看。

构建一个不需要你作为运行时环境的系统。