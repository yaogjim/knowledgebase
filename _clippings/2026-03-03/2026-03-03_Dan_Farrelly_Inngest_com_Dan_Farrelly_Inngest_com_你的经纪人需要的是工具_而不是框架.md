---
title: "2026-03-03_Dan_Farrelly_Inngest_com_Dan_Farrelly_Inngest_com_你的经纪人需要的是工具_而不是框架"
source: "https://x.com/djfarrelly/status/2028556984396452250"
author:
  - "[[@Dan Farrelly | Inngest.com]]"
published: 2026-03-03
created: 2026-03-03
description:
tags:
  - "x"
  - "@Dan Farrelly | Inngest.com"
  - "inngest"
  - "llm"
---

# Dan Farrelly  Inngest.com # 你的经纪人需要的是工具，而不是框架

**Dan Farrelly | Inngest.com**

# 你的经纪人需要的是工具，而不是框架。

在所有工程领域，“线束”都扮演着相同的角色：它是连接、保护和协调各个组件的层，但自身并不执行任何工作。例如，线束负责在发动机、传感器和仪表盘之间传输信号；测试线束提供框架，使代码可重复运行且可观察；安全带则在你跌倒时起到保护作用。

代理运行时需要同样的东西。LLM 是引擎，工具是外围设备，内存是存储。但是什么将它们连接起来？当 LLM 在第五次迭代超时时，是什么捕获了故障？是什么防止两条消息冲突？是什么将事件从 webhook 路由到正确的处理程序，再路由到正确的回复通道？

这就是基础架构。每个代理框架都在从零开始构建它——它们自己的重试逻辑、状态持久化、任务队列、事件路由。

持久化的事件驱动型基础设施已经解决了这个问题。每次 LLM 调用或工具调用都会成为一个步骤——一个可独立重试的工作单元。如果流程在第五次迭代时终止，前四次迭代的数据已经持久化。事件在函数之间路由触发器。并发控制防止冲突。步骤级跟踪使您可以全面观察代理循环的每一次迭代。基础设施就是框架。

我们构建了 Utah（ 通用触发代理框架 ）来验证这一点。它是一个可与 Telegram 或 Slack 对话的代理，具备工具、内存、子代理委托和完全持久性。使用极简的 TypeScript，无需任何框架。 摄函数、步骤和事件构成了一个标准的“思考→行动→观察”循环。 可以把它想象成一个持久耐用 、可部署在云端的 OpenClaw。

“通用触发”这一点至关重要：无论是 Telegram 或 Slack Webhook、定时任务、子代理调用还是函数间事件——代理本身并不知道或关心它是如何被激活的。触发器与实际工作是解耦的。即使明天添加了一个 Slack 机器人，代理的循环也不会改变。系统会自动处理路由。

运作方式如下。

## 建筑

Utah 与大多数工具链的不同之处在于，它是事件驱动的，并且将编排与代理循环解耦。它还利用 Inngest Cloud 来弥合公共 Webhook 和本地工作进程之间的差距。

犹他州英格斯特项目建筑

Telegram 或 Slack 的 Webhook 请求会到达 Inngest Cloud，在那里，Webhook 转换器会将原始的 HTTP 有效负载转换为类型化的 Inngest 事件。本地运行的 worker 会获取该事件，运行代理函数，并触发一个回复事件，该事件会触发另一个函数，通过频道自身的 API 将响应发送回频道（详见下文）。任何支持 Webhook 的通信渠道（或任何服务）都适用。

该工作进程使用 Inngest 的 connect()API，该 API 可以从您的本地计算机（或 Mac mini 或远程服务器）建立到 Inngest Cloud 的持久 WebSocket 连接，而无需公共端点。

工作进程中运行的代理循环很简单：它是一个带有“步骤”的 while 循环，这些步骤会调用 LLM 并运行工具。我们使用了 Pi 的提供程序接口及其工具，因为它们都很棒 ，但您也可以使用任何其他工具。您可以替换为 AI SDK、TanStack AI，创建自己的工具，或者接入 MCP。

## 如果是本地应用，为什么还要用 Inngest？为什么不直接用 OpenClaw 呢？

OpenClaw 和 pi 编码代理库是本项目的灵感来源。它们都在内部使用进程内事件，因此事件和编排都在内存中处理。Ingest 本身就是一个事件驱动的编排层，因此本项目将执行与编排解耦。

这样一来，安全带就能实现以下几个功能：

- 编排层通过跟踪和步骤级检查提供可观测性。
- 内置的持久执行机制提供了可靠性和重试机会。
- 解耦为多人分布式代理编排奠定了基础。
- 事件历史记录提供了系统内发生事件的审计跟踪。
- 调度功能内置于 cron 或定时/延迟函数中。

所有这些问题都是基础设施问题，而不是人工智能问题。

## 代理循环步骤

Utah 的核心是一个“思考→行动→观察”的循环。每次迭代都会调用 LLM（逻辑学习模型），检查是否需要使用工具，执行这些工具，并将结果反馈给系统。关键在于： 每次 LLM 调用和每次工具执行都是一个信息采集步骤。

```typescript
// Simplified — the actual implementation uses pi-ai's provider-agnostic types
while (!done && iterations < config.loop.maxIterations) {
  iterations++;

  // Prune old tool results to keep context focused
  pruneOldToolResults(messages);

  // Budget warnings when running low on iterations
  const messagesForLLM = addBudgetWarning(messages, iterations);

  // Think: call the LLM
  const llmResponse = await step.run("think", async () => {
 return await callLLM(systemPrompt, messagesForLLM, tools);
  });

  const toolCalls = llmResponse.toolCalls;

  if (toolCalls.length > 0) {
 messages.push(llmResponse.message);

 // Act: execute each tool as a separate step
 for (const tc of toolCalls) {
 const result = await step.run(`tool-${tc.name}`, async () => {
 validateToolArguments(tool, tc);
 return await executeTool(tc.id, tc.name, tc.arguments);
 });
 // Observe: feed results back into messages
 messages.push(toolResultMessage(tc, result));
 }
  } else if (llmResponse.text) {
 // No tools — the text response IS the reply
 finalResponse = llmResponse.text;
 done = true;
  }
}
```

需要注意以下几点：

Inngest 会自动索引重复的步骤 ID。 当步骤运行 （"think") 在循环中被调用十次，Ingest 内部会将它们跟踪为 think:0、think:1 等。您无需自己管理唯一的步骤 ID – SDK 会处理它。

每个步骤都可以独立重试。 如果 LLM API 在第三次迭代中返回 500 错误，Ingest 会重试该特定步骤。第一次和第二次迭代的结果已被持久化，不会重新执行。这就是持久执行，它完全按照设计用途运行，只是应用于代理循环而不是结账工作流。

文本回复表示操作完成。 当 LLM 以文本形式回复且没有工具调用时，操作轮次结束。无需明确的“完成”信号。

## 你不需要自己构建工具

犹他州不手动处理文件 I/O 和 shell 执行。它会调用 pi-coding-agent— 来自 OpenClaw/Pi 生态系统的久经考验的工具实现：

- 读取 、 写入 、 编辑 ——支持图像的文件操作，具备二进制检测和智能截断功能（编辑工具在上下文窗口中表现出色）。
- bash— 具有可配置超时和输出截断的 shell 执行
- grep、find、ls——搜索和导航操作会尊重.gitignore 文件。

除此之外，犹他州还添加了一些自定义工具：remember（将笔记保存到每日日志中）、web\_fetch 和 delegate\_task（稍后会详细介绍）。

关键在于：人工智能代理的工具开发与其他软件开发并无二致。使用现有的库，将其封装在 Inngest 步骤中，就完成了。

```typescript
import { createReadTool, createWriteTool, createBashTool, /* ... */ } from "@mariozechner/pi-coding-agent";

const tools = [
  createReadTool(config.workspace.root),
  createWriteTool(config.workspace.root),
  createBashTool(config.workspace.root),
  // ...
];
```

简单。复制、粘贴，即可使用。

## 六个功能，而非单一整体

事件解耦的六个关键功能

犹他州并非一个包罗万象的单一职能部门，而是由六个职能部门通过各种活动进行沟通协作：

```typescript
const functions = [
  handleMessage, // The main agent loop
  sendReply, // Send responses back to the channel
  acknowledgeMessage,// Typing indicator — fires immediately
  failureHandler, // Global error handler across all functions
  heartbeat, // Periodic scheduled check-ins
  subAgent, // Isolated sub-agent runs via step.invoke()
];
```

这种分离至关重要。输入指示器会在收到消息时立即触发，无需等待代理循环。回复函数负责处理 Telegram/Slack 特有的格式和错误处理（例如，当 LLM 生成格式错误的 HTML 时回退到纯文本）。故障处理程序会捕获所有函数中未处理的错误并通知用户。

每个函数都有自己的重试策略、并发控制和触发条件。这在 Inngest 中很自然——你是由事件连接的小型、功能明确的函数组合而成的行为。

至于 sendReply 函数？它可以从任何地方触发，因此如果我们想允许子代理或扇出的工作流在循环过程中发送回复以更新用户，我们只需从新工具发送事件即可。

## 通过 step.invoke() 调用子代理

有时，智能体需要执行的任务规模庞大，足以超出其上下文窗口——例如重构文件、研究主题或撰写文档。对于像 OpenClaw 这样运行在单线程对话（例如 Telegram）中的通用智能体而言，一些持续数天的长时间会话可能会出现上下文窗口问题。解决方法是：生成一个子智能体。

犹他州有一个 delegate\_task 工具。当主代理调用它时，它会使用步骤.调用() 启动一个完全独立的代理函数运行。子代理会将会话上下文分叉到自己的子会话（具有自己的会话密钥）中，并针对特定任务执行特定结果：

```typescript
// In the main agent loop, when delegate_task is called:
const subResult = await step.invoke("sub-agent", {
  function: subAgent,
  data: {
 task: tc.arguments.task,
 subSessionKey: `sub-${sessionKey}-${Date.now()}`,
  },
});
```

子代理函数运行一个新的代理循环，使用自己的上下文窗口、相同的工具（除了 delegate\_task—— 没有递归生成），并向父代理返回摘要：

```typescript
// Simplified sub-agent
export const subAgent = inngest.createFunction(
  { id: "agent-sub-agent", retries: 1 },
  { event: "agent.subagent.spawn" },
  async ({ event, step }) => {
 const { task, subSessionKey } = event.data;
 const agentLoop = createAgentLoop(task, subSessionKey, {
 tools: SUB_AGENT_TOOLS, // No delegate_task
 isSubAgent: true,
 });
 return await agentLoop(step);
  }
);
```

\`step.invoke()\` 函数正是按照其设计用途执行的——调用另一个 Inngest 函数作为步骤，等待其结果，然后继续执行。子代理拥有自己的重试机制、步骤级可观测性和持久执行能力。父代理看到的只是工具返回的结果：“这就是我执行的操作。”

编排已完成。无需代理间协议。只需函数调用函数即可。

## 单例并发：一次只处理一个对话

每个“频道”（例如 Slack）都使用频道特定的会话密钥来定义“对话”。对于像 Telegram 这样的单线程频道，会话密钥是聊天 ID；对于像 Slack 这样的线程平台，会话密钥则与频道和线程相关。

如果对话中发送了多条消息，您不希望第一个代理循环一直运行，然后下一个循环才响应——您希望代理能够同时拥有两条消息的上下文。因此，您要么需要取消第一个循环，让第二个循环来处理，要么需要在循环内部进行“引导”。在这个项目中，我们认为取消并重启是最简洁的循环方式，因为这样循环会带着所有上下文重新启动。

在消息处理函数中，我们设置了一行配置来处理这种情况：

```typescript
singleton: { key: "event.data.sessionKey", mode: "cancel" },
```

两件事正在发生：

1.  单例并发基于 sessionKey 进行交互——每次聊天只运行一个代理。无竞态条件。无交错响应。
2.  收到新消息时取消 — 如果用户在代理仍在处理消息时发送新消息，则当前运行将被取消，并从最新消息开始新的运行。

传统方案中，你需要为每个用户创建一个队列，管理锁定，并自行处理取消操作。而使用 Inngest，只需一行配置即可。

## 我们付出惨痛代价才学到的教训

上下文管理才是真正的挑战

最难的问题不是打电话给 LLM（法学硕士），而是如何管理 LLM 电话会议的内容。

犹他州使用的工具每次调用可能会返回数千个字符。经过几次迭代后，对话内容变得庞杂，模型开始无法正确处理。我们看到代理程序不断循环调用工具，却始终没有产生任何响应。

我们通过两层上下文剪枝解决了这个问题：

```typescript
const PRUNING = {
  keepLastAssistantTurns: 3,
  softTrim: { maxChars: 4000, headChars: 1500, tailChars: 1500 },
  hardClear: { threshold: 50_000, placeholder: "[Tool result cleared]" },
};
```

当上下文数据量过大时，旧工具的运行结果会被软性修剪（保留头部和尾部）或完全清除。最后三次迭代的结果始终保持不变。

此外，会话本身还有一个独立的压缩系统 ——当预估的令牌数量超过阈值时，会话历史记录会被汇总，然后再输入到下一次运行中。修剪处理运行内的上下文，而压缩处理跨运行的累积。

我们还添加了预算警告——当代理迭代次数不足时，系统会注入消息，提示其结束运行。此外，我们还加入了溢出恢复机制：如果 LLM 在运行过程中返回上下文过大的错误，我们会强制压缩消息并重试，而不会浪费一次迭代。通过剪枝、压缩、预算压力和溢出恢复机制，代理能够保持正常运行。

多提供商 LLM 支持

犹他州并没有直接调用 Anthropico SDK，而是使用了 pi-ai 这是一个与提供商无关的 LLM 抽象层，支持 Anthropic、OpenAI 和 Google。切换提供商只需更改配置即可：

```typescript
llm: {
  provider: "anthropic", // or "openai" or "google"
  model: "claude-sonnet-4-20250514",
},
```

展望未来，如果子代理能够发展使用不同的模型（甚至可能来自不同的供应商），这将变得非常有趣。例如，编码子代理可以使用 Codex，而研究代理可以使用 Opus。更多相关内容敬请期待。

转向是一个尚未解决的问题

当用户在代理运行过程中发送新消息时，应该如何处理？我们目前使用单例模式——取消当前运行并启动新的运行。这种方法可行，但所有正在进行的工作都会丢失。新的运行会从持久化的会话状态继续执行，但这并不流畅。我们正在积极探索这方面的解决方案。

流媒体或循环中实时更新的机会

Inngest 的每个步骤都是原子性的——它运行、产生结果，并将结果持久化。本项目目前尚未包含流式传输或利用功能。Inngest 的实时功能方面，Telegram 和 Slack 都支持单个事件，但我们希望在这个项目中添加一个 Web 应用和一个 TUI，以探索如何选择性地向支持流式传输的客户端发送循环中的进度更新。未来版本还会添加更多功能。

## 接下来我们将探索什么

Utah 是一款个人单人游戏平台，可在本地计算机或服务器上运行。其核心架构功能远不止于此。在接下来的几周里，我们将探索如何让 Utah 真正成为一款多人游戏。

为了实现多人游戏，我们将探索可交换沙盒、外部状态和内存。这将使 Utah 能够在无服务器架构下运行（如果有人需要的话）。

我们计划基于 Inngest API 和 Insights 功能添加许多有趣的 UX 功能，用于构建编码会话监控。此外，我们还将探索使用 step.waitForEvent() 来创建需要更多输入的人工审批流程。

为了真正实现“普遍触发”，我们正在探索的最后一个环节是让犹他州能够自我编写代码——构建新的代理和工作流程、创建新的 Webhook，并通过 API 进行自我监控。如果您感兴趣，欢迎在 GitHub 代码库中分享您的想法。

## 自己试试

犹他州源代码已作为参考实现发布：https://github.com/inngest/utah

其中包括：

- 代理循环包含 Inngest 步骤和 pi-ai 的与提供商无关的 LLM 层
- 来自 pi-coding-agent 的工具（读取、写入、编辑、bash、grep、find、ls）以及自定义工具
- 通过 step.invoke() 进行子代理委托
- 通过 Inngest webhook 转换实现 Telegram 和 Slack webhook 集成
- 上下文修剪、压缩和溢出恢复
- 会话感知单例并发

前往自述文件不妨试一试。

这种代理循环模式适用于任何对话式人工智能——Slack 机器人、Discord 机器人、客服代理、代码助手等等。添加任何新频道只需进行 webhook 转换并添加回复函数即可。

如果你在构建 AI 代理时遇到了同样的难题——状态管理、重试、并发、可观测性——不妨试试 Inngest。你需要的底层组件可能已经存在了。

* * *

### 热门回复

**@Pavel Durov** ♥ 8.7K · 💬 573

现在所有 Telegram 聊天机器人都可以实时向用户发送回复——这对人工智能助手来说非常棒。

**@@levelsio** ♥ 3.4K · 💬 78

如果你正在使用人工智能进行编程，这位老兄有很多很棒的安全技巧，值得关注。 @elvissun

**@Dan Farrelly | Inngest.com** ♥ 5 · 💬 1

Pi 很棒，犹他州的项目没有使用它的代理循环，所以我无法直接评论这一点，但是 @joelhooks 他用它搭建了自己的定制版“JoelClaw”，这很酷。我觉得大家喜欢树莓派是因为它可扩展、非常灵活，而且能兼容任何服务提供商。我不太清楚。

**@iury souza** ♥ 1 · 💬 1

嘿 @djfarrelly 谢谢你的文章！ 我正在研究如何构建个人智能助手，而树莓派也是我的首选。我查阅了一些资料，发现有很多 SDK/框架，比如 LangChain 和其他一些实验室的 SDK。 你认为主要的是什么？

**@Richard Scheiwe** ♥ 1 · 💬 1

哈哈，老兄……你这么一说，感觉这道理显而易见。所谓的“基础架构”（重试、状态持久化、并发、事件路由）其实都是已经解决的问题。每个代理框架都只是从头开始，拙劣地重建了这些功能而已。 我是 Inngest 的忠实粉丝。