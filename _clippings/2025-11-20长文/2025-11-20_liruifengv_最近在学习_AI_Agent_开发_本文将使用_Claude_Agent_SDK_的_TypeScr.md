---
title: "2025-11-20_liruifengv_最近在学习_AI_Agent_开发_本文将使用_Claude_Agent_SDK_的_TypeScr"
source: "https://liruifengv.com/posts/cladue-agent-sdk-demo/"
author:
  - "[[@liruifengv]]"
published: 2025-11-20
created: 2025-11-20
description:
tags:
  - "liruifengv"
  - "@liruifengv"
  - "message"
  - "const"
---

# 最近在学习 AI Agent 开发，本文将使用 Claude Agent SDK 的 TypeScr

最近在学习 AI Agent 开发，本文将使用 Claude Agent SDK 的 TypeScript 版本, 构建一个 AI Agent Demo。

全部代码在我的 GitHub 仓库 [liruifengv/claude-agent-demo](https://github.com/liruifengv/claude-agent-demo) 。

## Claude Agent SDK 介绍

Claude Agent SDK 的前身是 Claude Code SDK，是 Claude Code 的底层框架，现在改为通用的 Agent SDK，其中具备了 Claude Code 所拥有的一些基础能力，包括上下文管理，内置丰富的工具，权限控制等，如果你也想构建一个 Agent，使用这个 SDK 能快速搭建起来。更多详情请看 [Claude Agent SDK 的文档](https://docs.claude.com/en/docs/agent-sdk/overview)

## 环境配置

首先我们需要初始化一个 Node.js 的空项目。

其次是环境变量，需要配置 Claude 的模型的 BASE\_URL 和 API\_KEY

两种方式：

- 可以在系统的环境变量里配置：

```bash
ANTHROPIC_BASE_URL=ANTHROPIC_BASE_URL
ANTHROPIC_API_KEY=ANTHROPIC_API_KEY
```

- 或者在项目的 `.env` 文件中配置：

```bash
ANTHROPIC_BASE_URL=ANTHROPIC_BASE_URL
ANTHROPIC_API_KEY=ANTHROPIC_API_KEY
```

然后安装 `@anthropic-ai/claude-agent-sdk` 这个 npm 包：

```bash
npm install @anthropic-ai/claude-agent-sdk
```

## 基础用法

首先是 `query` 函数，他是跟 Agent 交互的主要函数，用于向 Agent 发送请求。

我们来看下用法：

```ts
import { query, Query } from "@anthropic-ai/claude-agent-sdk";

export async function basicExample() {
 // query 函数接受一个 prompt 参数
 const result: Query = query({prompt: "你好"})

 // 这里使用 for await of 循环 result
 for await (const message of result){
 // message.type 有几种：'assistant', 'user', 'system', 'result' 等
 // 根据不同的消息类型做业务逻辑
 switch (message.type){
 case 'assistant':
 // message.message.content 是一个数组，我们循环所有的 msg
 for (const msg of message.message.content) {
 // 打印 text 类型的输出
 if (msg.type === "text") {
 console.log(msg.text)
 }
 }
 }
 }
  }
```

在 `index.ts` 中调用 `basicExample` 函数：

```ts
import { basicExample } from "./core/basic-example";

async function main() {
  console.log('Starting Claude Agent Demo...');
  await basicExample();
}

main();
```

执行 `tsx src/index.ts`

可以在终端看到

```bash
> claude-agent-demo@1.0.0 dev
> tsx src/index.ts

Starting Claude Agent Demo...
你好！很高兴见到你！我是 Claude，一个 AI 助手。我可以帮助你：

- 编写和调试代码
- 搜索和分析代码库
- 执行命令和运行脚本
- 管理文件和项目
- 回答技术问题

有什么我可以帮助你的吗？
```

## Session 会话管理

Claude Agent SDK 自带了会话管理功能，当新建一个 query 时，它会返回一个 session ID，你可以使用这个 ID 来保存和恢复会话。例如，你可以将 session ID 存储在数据库中，以便在用户下次登录时恢复会话。

```ts
import {query, Query} from "@anthropic-ai/claude-agent-sdk";

export async function sessionExample() {
 let sessionId: string | undefined

 const result: Query = query({
 prompt: "你好",
 options: {
 // options 的 resume 参数传入记录的 sessionId，就可以继续对话了
 resume: sessionId
 }
  })

  for await (const message of result) {
 switch (message.type) {
 // message.type === 'assistant' && message.subtype === 'init' 的时候
 // 会返回一个 session_id，需要把这个 session_id 存下来
 case 'system':
 if (message.subtype === 'init') {
 sessionId = message.session_id
 console.log(`Current Session ID: ${sessionId}`)
 }
 break
 case 'assistant':
 for (const msg of message.message.content) {
 if (msg.type === "text") {
 console.log(`Assistant: ${msg.text}`)
 }
 }
 break
 }
  }
}
```

## 实现连续对话

接下来我们会在终端使用 node 做一下简单的交互，使得用户可输入内容，然后使用 session ID 实现连续对话。

创建一个 `tui-chat.ts`:

```ts
export async function tuiChat() {
 const rl = readline.createInterface({
 input: process.stdin,
 output: process.stdout,
 prompt: 'User: '
 })

 rl.prompt()

 rl.on('line', async (input: string) => {
 const userInput = input.trim()
 console.log(`User: ${userInput}`)
 rl.prompt()
 })

 rl.on('close', () => {
 console.log("exit the chat")
 process.exit(0);
 });

}
```

以上代码就能实现用户在终端连续输入内容。 接着写 AI 对话的代码：

```ts
// 这个函数接收两个参数，一个 prompt 用户输入，一个当前会话 id
export async function chatExample(prompt: string, sessionId: string | undefined) {

  // 函数内部定义会话 id
  let _sessionId: string | undefined

  const result: Query = query({
 prompt: prompt,
 options: {
 // options 的 resume 参数传入记录的 sessionId，就可以继续对话了
 resume: sessionId
 }
  })
  for await (const message of result) {
 switch (message.type) {
 case 'system':
 if (message.subtype === 'init') {
 // 系统初始化时记录会话ID
 _sessionId = message.session_id
 }
 break
 case 'assistant':
 for (const msg of message.message.content) {
 if (msg.type === "text") {
 console.log(`Assistant: ${msg.text}`)
 }
 }
 break
 }
  }

  // 把当前会话 id 返回给调用者
  return _sessionId
}
```

然后调用这个 `chatExample` 就行：

```ts
export async function tuiChat() {
  // 记录 sessionId
  let sessionId: string | undefined

  const rl = readline.createInterface({
 input: process.stdin,
 output: process.stdout,
 prompt: 'User: '
  })

  rl.prompt()

  rl.on('line', async (input: string) => {
 const userInput = input.trim()
 // 赋值返回的 sessionId
 sessionId = await chatExample(userInput, sessionId)

 rl.prompt()
  })

  rl.on('close', () => {
 console.log("exit the chat")
 process.exit(0);
  });
}
```

好的，现在我们来执行一下看看效果：

```bash
Starting Claude Agent Demo...
User: hello
Assistant: Hello! 👋 How can I help you today? I'm Claude, and I can assist you with a variety of tasks like:

- Writing, editing, or reviewing code
- Searching through codebases and files
- Running commands and tests
- Creating pull requests and managing git operations
- Answering questions about your project
- And much more!

What would you like to work on?
User: 你是谁
Assistant: 你好！我是 Claude，由 Anthropic 开发的 AI 助手。

在这个环境中，我是 Claude Code - 一个专门用于编程和开发任务的版本。我可以帮助你：

- 编写、编辑和审查代码
- 搜索和分析代码库
- 运行命令和测试
- 管理 Git 操作和创建 Pull Request
- 回答关于项目的问题
- 还有更多其他功能！

有什么我可以帮助你的吗？
User: 我跟你说的上一句话是什么
Assistant: 你上一句话是"你是谁"。
```

完美，我们可以在终端和 Agent 连续对话了，它能记住我们上一句话，说明当前会话是有效的。

## 工具调用

接下来我们会自定义一个用于数学计算的工具，和一个 MCP Server。

先安装 [`mathjs`](https://mathjs.org/) 和 [`zod`](https://zod.dev/)

```bash
npm install mathjs
npm install zod@3.25.76
```

Claude Agent SDK 内部使用的 zod 还是 3.25 版本，而最新版已经是 4.1.12，会有兼容问题，所以我们安装了指定版本。

`mathjs` 是一个数学计算的库，他有一个 `evaluate` 方法，可以执行字符串表达式，例如：

```ts
import math from 'mathjs';

math.evaluate('1.2 * (2 + 4.5)')
```

创建一个 `tools/calc-tool.ts` ：

```ts
import { tool } from "@anthropic-ai/claude-agent-sdk";

import { z } from "zod"
import { calculator } from "../utils/calculator";

// 使用 tool 函数创建一个工具
// 前两个参数是工具名称和描述
export const calcTool = tool(
  "calculator",
  "Perform a calculation using an expression string. The strings used here are executed using mathjs evaluate function. eg  " + "1.2 * (2 + 4.5)",
  // 第三个参数是 inputSchema，使用 zod 来定义
  {
 expression: z.string().describe("The expression to be evaluated")
  },
  async (args) =>{
 // 回调函数里执行工具的具体业务逻辑
 const result = calculator(args.expression)

 // 返回这个结构即可
 return {
 content: [
 {
 type: "text",
 text: result
 }
 ]
 }
  }
)
```

创建一个 `utils/calculator.ts` ：

```ts
import * as math from 'mathjs'

export function calculator(expression:string) : string{
  const result = math.evaluate(expression)
  return result.toString()
}
```

工具定义完毕，Claude Agent SDK 要求我们必须定义一个 MCP Server 来使用工具。

我们创建一个 `mcps/mcp-example-server.ts` 文件：

```ts
import { createSdkMcpServer } from "@anthropic-ai/claude-agent-sdk";
import { calcTool } from "../tools/calc-tool";

// createSdkMcpServer 是定义 MCP Server 的函数
export const utilitiesServer = createSdkMcpServer({
  name: "utilities",
  version: "1.0.0",
  tools: [calcTool],
})
```

好的，MCP Server 创建完毕。

接我们回到 `chatExample` 函数：

```ts
import { utilitiesServer } from "../mcps/mcp-example-server";

export async function chatExample(prompt: string, sessionId: string | undefined) {
  let _sessionId: string | undefined

  const result: Query = query({
 prompt: prompt,
 options: {
 resume: sessionId,
 // systemPrompt 可以自定义系统提示词
 systemPrompt: "You are a helpful assistant that can use tools to get information. You can use the following tools: calculator",
 // mcpServers 是一个对象参数，传入自定义的 MCP utilitiesServer
 mcpServers: {
 utilities: utilitiesServer
 },
 // 必须在 allowedTools 里指定的工具才能使用
 // 工具的命名格式是固定的：mcp__{server_name}__{tool_name}
 // 这里就是 mcp__utilities__calculator
 allowedTools: [
 "mcp__utilities__calculator",
 ]
 }
  })
  for await (const message of result) {
 switch (message.type) {
 case 'system':
 if (message.subtype === 'init') {
 _sessionId = message.session_id
 }
 break
 case 'assistant':
 for (const msg of message.message.content) {
 if (msg.type === "text") {
 console.log(`Assistant: ${msg.text}`)
 }
 // 打印 tool_use 类型的的消息
 else if (msg.type === "tool_use") {
 process.stdout.write(`Using tool:  ${msg.name} `)
 if (msg.input) {
 // tool 得到的表达式
 process.stdout.write(` - Input: ${msg.input.expression} `)
 }

 process.stdout.write('\n')
 }
 }
 break
 case 'user':
 for (const msg of message.message.content) {
 // 打印 tool_result 类型的消息
 if (msg.type === "tool_result") {
 process.stdout.write("Tool Results: ")
 for (const result of msg.content) {
 if (result.type === "text") {
 process.stdout.write(result.text)
 process.stdout.write(" - ")
 }
 }
 process.stdout.write('\n')
 }
 }
 break
 }
  }

  return _sessionId
}
```

我们运行看看效果：

```bash
Starting Claude Agent Demo...
User: 你好
Assistant: 你好！很高兴见到你。我是 Claude，一个 AI 助手。我可以帮你进行计算、回答问题、解决问题等。有什么我可以帮助你的吗？
User: 2454+23546，再平方，再除以 32，等于多少？
Assistant: 我来帮你计算这个问题。
Using tool:  mcp__utilities__calculator  - Input: (2454 + 23546)^2 / 32
Tool Results: 21125000 -
Assistant: 计算结果是：**21,125,000**

让我展示一下计算步骤：
1. 首先：2454 + 23546 = 26000
2. 然后平方：26000² = 676,000,000
3. 最后除以 32：676,000,000 ÷ 32 = 21,125,000
```

我们提问了一个数学问题，它把他解析为工具需要的表达式，然后使用了工具，得到了正确结果，完美！

## 结尾

使用 Claude Agent SDK，我们用很少的代码就写了一个简单的 Agent，这个 SDK 应该是学习 Agent 开发起手比较简单的工具了，当然还有很多优秀的 Agent 框架，比如 [Vercel AI SDK](https://vercel.com/docs/ai-sdk), [Mastra](https://mastra.ai/), 等等，后续也会学习使用。

加我微信 `liruifengv2333` ，进群交流，抱团取暖。

- 新生代程序员群
- Astro 学习交流群

关注公众号 `程序员李瑞丰` ，带来更多原创内容。

![](https://bucket.liruifengv.com/qrcode.png?v=1) 很高兴见到你，欢迎来玩儿~