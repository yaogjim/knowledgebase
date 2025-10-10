---
title: "Here's How To Build Fullstack Agent Apps (Gemini, CopilotKit & LangGraph)"
source: "https://dev.to/copilotkit/heres-how-to-build-fullstack-agent-apps-gemini-copilotkit-langgraph-15jb"
author:
  - "[[Anmol Baranwal]]"
published: 2025-09-19
created: 2025-09-19
description: "AI agents are getting close to real world applications, but most developers still find it complex to... Tagged with programming, webdev, opensource, ai."
tags:
  - "Anmol Baranwal"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-10-17"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---
人工智能代理正逐渐接近实际应用，但大多数开发者仍然觉得构建一个人工智能代理很复杂。

所以我们要构建两个实用的智能体： **帖子生成器** ，它利用实时网络搜索来起草领英/推特内容；以及 **堆栈分析器** ，它检查 GitHub 仓库并创建结构化报告。

我们将使用 Next.js 前端、FastAPI 后端、 [CopilotKit](https://go.copilotkit.ai/copilot) 、 [LangGraph](https://www.langchain.com/langgraph) 工作流以及 [Google Gemini](https://gemini.google.com/) 。你会看到架构、概念、提示以及实际操作内容。

Let's build it.

---

## 1\. 我们要构建什么？

我们正在使用全栈设置构建两个实用代理：

✅ **帖子生成代理** ：根据实时谷歌搜索结果创建领英/推特帖子。

以下是用户生成一篇文章时将会发生的简化调用序列。  

✅ **堆栈分析器代理** ：分析一个公共的 GitHub 仓库（元数据、README、代码清单）并推断其堆栈。

以下是当用户分析一个仓库的技术栈时将会发生的事情的简化调用序列。  

```
[User pastes GitHub URL]
     ↓
Next.js UI (/stack‑analyzer)
     ↓
/api/copilotkit → FastAPI
     ↓
Stack Analysis graph nodes (gather_context → analyze → end)
     ↓
Streaming tool‑logs & structured analysis cards
```

这就是我们要构建的东西！

![](https://www.youtube.com/watch?v=DJMkP28TdBQ)

---

## 2\. 技术栈与架构

从核心来讲，我们将使用这个技术栈来构建这些智能体。

- [Next.js 15](https://nextjs.org/) ：带有 TypeScript 的前端框架
- [副驾驶套件软件开发工具包](https://go.copilotkit.ai/copilot) ：将智能体嵌入用户界面（ `@copilotkit/react-core` ， `@copilotkit/runtime` ， `@copilotkit/react-ui` ）
- [FastAPI](https://fastapi.tiangolo.com/) 与 [Uvicorn](https://www.uvicorn.org/) ：用于将智能体作为 API 提供服务的后端框架
- [LangGraph（状态图）](https://www.langchain.com/langgraph) ：用于构建有状态代理工作流
- 通过 `google - genai` 使用的谷歌 Gemini（官方软件开发工具包）：用于推理和文本生成的语言模型
- [LangChain 的谷歌适配器](https://python.langchain.com/docs/integrations/llms/google_ai/) ：将 Gemini 接入 LangChain 工作流程
- [皮迪 antic](https://docs.pydantic.dev/latest/) ：用于结构化 JSON 工具输出 （注：这里原文的“Pydantic”可能有误，一般常见的是“Pydantic”，可根据实际情况修改，这里暂且按原文翻译）

以下是该项目的高层架构。

```
┌───────────────┐        GraphQL / HTTP           ┌───────────────────┐
        
        
          

           │               │  <——————— /api/copilotkit ————> │                   │
        
        
          

           │   Next.js     │                                 │   FastAPI Agent   │
        
        
          

           │  Frontend     │                                 │   (agent/main.py) │
        
        
          

           │ (React + UI)  │                                 │                   │
        
        
          

           └───────────────┘                                 └───────────────────┘
        
        
          

                  ▲                                                 ▲
        
        
          

                  │                                                 │
        
        
          

                  │                                                 │
        
        
          

                  │                                                 │
        
        
          

           /api/copilotkit route                                  CopilotKitSDK
        
        
          

           (CopilotKit Runtime endpoint)                    + LangGraphAgent workflows
        
        
          

                                                                    ▼
        
        
          

                                                         ┌────────────────────┐
        
        
          

                                                         │  Gemini + Tools    │
        
        
          

                                                         │  (Google Search)   │
        
        
          

                                                         └────────────────────┘
```

### Project structure

这就是我们的目录结构。\`agent\` 目录将存放托管 LangGraph 代理的 Python/FastAPI 后端，而 \`frontend\` 目录则托管 Next.js 15 应用程序，包括用户界面路由、API 路由和共享组件。  

```
.
├── assets/                  
├── frontend/                ← Next.js 15 App (UI + API routes)
│   ├── app/
│   │   ├── layout.tsx       ← Wraps the app with \`<CopilotKit>\`
│   │   ├── post-generator/  ← Post Generator UI routes
│   │   ├── stack-analyzer/  ← Stack Analyzer UI routes
│   │   └── api/             ← Next.js API routes used by the UI
│   │   ...
│   ├── contexts/LayoutContext.tsx
│   ├── wrapper.tsx            ← CopilotKit provider wrapper
│   ├── components/          ← Shared UI components
│   │   ...
├── agent/                   ← FastAPI + LangGraph “agents” (Python)
│   ├── main.py              ← Registers agents and exposes them via FastAPI
│   ├── posts_generator_agent.py  ← Workflow for content creation agent
│   ├── stack_agent.py       ← Workflow for repo analysis agent
│   ├── prompts.py           ← Shared prompt templates
│   ├── agent.py             ← Core agent classes and helpers
│   ...
└── README.md                ← Project overview and setup instructions
```

这是 [GitHub 代码仓库](https://github.com/CopilotKit/CopilotKit-Deepmind) ，如果你想亲自探索一下，它已部署在 [copilot-kit-deepmind.vercel.app](https://copilot-kit-deepmind.vercel.app/) 上实时运行。在接下来的部分中，我将介绍所有关键概念的实现。

最简单的跟进方式是克隆仓库，但我将解释如何从头开始构建它。  

```
git clone https://github.com/CopilotKit/CopilotKit-Deepmind.git
cd copilotkit-deepmind
```

### 添加必要的 API 密钥。

在\`agent\`和\`frontend\`目录下都创建一个\`.env\`文件，并将你的 [Gemini API 密钥](https://aistudio.google.com/apikey) 添加到该文件中。我已附上文档链接，方便你参考。

这两个目录的命名规范是相同的。  

```
GOOGLE_API_KEY=<<your-gemini-key-here>>
```

[![google gemini api key](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ftf3sy64ruzpdctcgq3a7.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ftf3sy64ruzpdctcgq3a7.png)

---

## 3\. Frontend

让我们创建前端。我再次附上前端的项目结构，这样你就能更轻松地跟上整个布局。  

如果你没有前端部分，可以创建一个新的带有 TypeScript 的 Next.js 应用，然后安装 Copilotkit 包。在克隆的代码仓库中，它已经存在了，所以你只需要在 `frontend` 目录下使用 `pnpm i` 来安装依赖项。  

```
// creates a nextjs app with typescript  
npx create-next-app@latest frontend
```

[![nextjs frontend](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F51fhtbamxap5kd1mgmhp.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F51fhtbamxap5kd1mgmhp.png)

### 步骤 1：CopilotKit 提供程序与布局

安装必要的 CopilotKit 包。  

```
pnpm install copilotkit @copilotkit/react-core @copilotkit/react-ui @copilotkit/runtime @copilotkit/runtime-client-gql
```
- \`copilotkit\` 是一个底层软件开发工具包（SDK），它为 Python 捆绑了后端实用工具。这里用于连接状态图、发出状态更新以及与 Gemini 进行交互。
- \`@copilotkit/react-core\` 提供了核心上下文和逻辑，用于将你的 React 应用与 CopilotKit 后端和 MCP 服务器连接起来。
- \`@copilotkit/react-ui\` 提供了像 \`\` 这样的现成 UI 组件，以便快速构建人工智能聊天或助手界面。
- \`@copilotkit/runtime\` 是服务器端运行时库。它允许你声明代理，将它们连接到 LangGraph 工作流，并通过 API 端点公开这些代理。
- `@copilotkit/runtime-client-gql` 是一个用于 GraphQL 传输的客户端。Next.js API 路由在底层使用它来在浏览器和你的后端之间进行代理。

[![install copilotkit packages](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fxs87ycbylpo9fxsk2ddi.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fxs87ycbylpo9fxsk2ddi.png)

\`\` 组件必须包裹应用程序中感知 Copilot 的部分。在大多数情况下，最好将其放置在整个应用程序周围，就像在 \`layout.tsx\` 中那样。

根布局将所有内容包裹在一个布局提供器和 CopilotKit 客户端包装器中：  

```
import "./globals.css"
import { LayoutProvider } from "./contexts/LayoutContext"
import Wrapper from "./wrapper"

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <LayoutProvider>
        <Wrapper>
          <body>{children}</body>
        </Wrapper>
      </LayoutProvider>
    </html>
  )
}
```

布局提供程序（ `frontend\app\contexts\LayoutContext.tsx` ）为布局状态设置一个 React 上下文，并使用 `usePathname()` 检测路径，根据当前路由（ `/post-generator` 或其他）选择活动代理。  

```
"use client"

import { usePathname } from "next/navigation"
import React, { createContext, useContext, useState } from "react"

interface LayoutState { … }

interface LayoutContextType {
  layoutState: LayoutState
  updateLayout: (updates: Partial<LayoutState>) => void
}

const LayoutContext = createContext<LayoutContextType | undefined>(undefined)

const defaultLayoutState = { agent: "post_generation_agent", … }
export function LayoutProvider({ children }) {
  const pathname = usePathname()

  const [layoutState, setLayoutState] = useState({
    ...defaultLayoutState,
    agent: (pathname == "/post-generator"
      ? "post_generation_agent"
      : "stack_analysis_agent"),
  })

  const updateLayout = (updates) =>
    setLayoutState((prev) => ({ ...prev, ...updates }))

  return (
    <LayoutContext.Provider value={{ layoutState, updateLayout }}>
      {children}
    </LayoutContext.Provider>
  )
}

export function useLayout() {
  return useContext(LayoutContext)
}
...
```

以下是 CopilotKit 客户端包装器的代码（ `frontend\app\wrapper.tsx` ）。每个页面都在其内部渲染，以便 UI 组件知道要调用哪个代理以及调用位置。  

```
"use client"
import { CopilotKit } from "@copilotkit/react-core";
import { useLayout } from "./contexts/LayoutContext";

export default function Wrapper({ children }: { children: React.ReactNode }) {
  const { layoutState } = useLayout()
  return (
    <CopilotKit runtimeUrl="/api/copilotkit" agent={layoutState.agent}>
      {children}
    </CopilotKit>
  )
}
```

### 步骤 2：Next.js API 路由：代理到 FastAPI

CopilotKit 运行时端点位于 Next.js API 路由 `app/api/copilotkit/route.ts` ，它只是将所有代理/图形调用转发到 FastAPI 后端。

我们不是直接从浏览器调用 Python 代理，而是引入了一个轻量级代理。

Why?

- 避免跨域资源共享（CORS）和跨源问题
- 让 Next.js 处理认证、特定环境的路由和打包
- 为 React UI 提供统一的 GraphQL/REST 形状（无 Python 负载泄露到客户端）

在这个示例中，我们只使用了单个智能体，但如果你想运行多个 LangGraph 智能体，请查看 [官方多智能体指南](https://docs.copilotkit.ai/coagents/multi-agent-flows) 。  

```
import { CopilotRuntime, copilotRuntimeNextJSAppRouterEndpoint, GoogleGenerativeAIAdapter } from "@copilotkit/runtime";
import { NextRequest } from "next/server";

// You can use any service adapter here for multi-agent support.
const serviceAdapter = new GoogleGenerativeAIAdapter();
const runtime = new CopilotRuntime({
  remoteEndpoints: [{ url: process.env.NEXT_PUBLIC_LANGGRAPH_URL || "http://localhost:8000/copilotkit" }],
});

export const POST = async (req: NextRequest) => {
  const { handleRequest } = copilotRuntimeNextJSAppRouterEndpoint({
    runtime,
    serviceAdapter,
    endpoint: "/api/copilotkit",
  });
  return handleRequest(req);
};
```

以下是对上述代码的简单解释：

- [`CopilotRuntime`](https://docs.copilotkit.ai/reference/classes/CopilotRuntime) ：将支持 Copilot 的用户界面与代理端点相连接的内部引擎。
- [`Google 生成式 AI 适配器 `](https://docs.copilotkit.ai/reference/classes/llm-adapters/GoogleGenerativeAIAdapter) ：此适配器将 Google Gemini 作为智能体工作流程的底层语言模型接入。
- \`remoteEndpoints\`：指定代理逻辑所在的位置（例如由后端提供服务的端点）。
- `copilotRuntimeNextJSAppRouterEndpoint` ：一个辅助函数，它包装传入的 <法典> 并将其路由到 Copilot 运行时进行代理处理。它返回一个 <方法>。 （需注意，这里“ ``”翻译为“<法典>”不太准确，通常在代码语境中应翻译为“<代码>”，但按照你给定的规则进行了翻译。） 实际准确译文应该是： `copilotRuntimeNextJSAppRouterEndpoint` ：一个辅助函数，它包装传入的 <代码>req`` 并将其路由到 Copilot 运行时进行代理处理。它返回一个 <代码>handleRequest 方法。

### 步骤3：自动重定向到帖子生成器

最后一件事是，每当有人在 \`frontend\\app\\page.tsx\` 中访问主页 \`/\` 路由时，重定向到 \`/post-generator\` 路由。  

### 步骤4：发布生成器代理用户界面

让我们使用 CopilotChat 用户界面（\` `<CopilotChat>` \`）、建议以及一个用于渲染最终帖子的自定义操作来创建帖子生成器（ `frontend/app/post-generator/page.tsx` ）的前端。

实际的代码库还包括诸如代理切换、快速操作和实时工具日志等用户界面附加功能。为了清晰起见，我在此处对其进行了精简，因此请查看 [完整用户界面的代码](https://github.com/CopilotKit/CopilotKit-Deepmind/blob/main/frontend/app/post-generator/page.tsx) 。  

系统和建议提示来自 `app/prompts/prompts.ts` 。  

```
export const initialPrompt  = "Hi! I am a Langgraph x Gemini-powered AI agent capable of performing web search and generating LinkedIn and X (Twitter) posts.\n\n Click on the suggestions to get started."

export const suggestionPrompt = "Generate suggestions that revolve around the creation/generation of LinkedIn and X (Twitter) posts on any specific topics."
```

在完整的用户界面代码中，我们还使用 `useCopilotAction` 来定义一个 `generate_post` 操作。这使得智能体能够返回结构化的领英/推特帖子，然后渲染成预览。为了简单起见，以下是精简后的代码。  

```
import { useCopilotAction } from "@copilotkit/react-core"
import { XPostCompact, LinkedInPostCompact } from "@/components/ui/posts"

useCopilotAction({
  name: "generate_post",
  description: "Render a LinkedIn and X post",
  parameters: {
    tweet: { title: "string", content: "string" },
    linkedIn: { title: "string", content: "string" }
  },
  render: ({ args }) => (
    <>
      {args.tweet?.content && (
        <XPostCompact title={args.tweet.title} content={args.tweet.content} />
      )}
      {args.linkedIn?.content && (
        <LinkedInPostCompact title={args.linkedIn.title} content={args.linkedIn.content} />
      )}
    </>
  )
})
```

为了进行调试，我们还使用 `useCoAgentStateRender` 来渲染 `tool_logs` ，它会在智能体工作时显示实时的工具调用情况。  

```
import { useCoAgentStateRender } from "@copilotkit/react-core"
import { ToolLogs } from "@/components/ui/tool-logs"

useCoAgentStateRender({
  name: "post_generation_agent",
  render: (state) => (
    <ToolLogs logs={state?.state?.tool_logs || []} />
  )
})
```

这是代码的最终输出。

[![post generator ui](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fgy0yvd3svjd1ngjuvums.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fgy0yvd3svjd1ngjuvums.png)

我不会介绍像 `徽章 ` 、 `  文本框  ` 、 `x 帖子 ` 、 ` 领英帖子` 和 `按钮` 这样的基本组件的代码。你可以在 `frontend/components/ui` 的代码仓库中查看所有组件。 [（点击此处查看）](https://github.com/CopilotKit/CopilotKit-Deepmind/tree/main/frontend/components/ui)

### 步骤 5：堆栈分析器代理用户界面

堆栈分析页面（ `frontend/app/stack-analyzer/page.tsx` ）接入了 `stack_analysis_agent` 并渲染出一组卡片。和之前一样，我去除了诸如代理切换、快速操作和实时工具日志等用户界面额外内容。你可以查看 [完整用户界面的代码](https://github.com/CopilotKit/CopilotKit-Deepmind/blob/main/frontend/app/stack-analyzer/page.tsx) 。

这与我们之前做的一样，所以我就不解释这段代码了。  

系统和建议提示来自 `app/prompts/prompts.ts` 。  

```
export const initialPrompt1 = 'Hi! I am a Langgraph x Gemini-powered AI agent capable of performing analysis of Public GitHub Repositories.\n\n Click on the suggestions to get started.'

export const suggestionPrompt1 = \`Generate suggestions that revolve around the analysis of Public GitHub Repositories. Only provide suggestions from these public URLs:
[
  "https://github.com/freeCodeCamp/freeCodeCamp",
  "https://github.com/EbookFoundation/free-programming-books",
  "https://github.com/jwasham/coding-interview-university",
  "https://github.com/kamranahmedse/developer-roadmap",
  "https://github.com/public-apis/public-apis",
  "https://github.com/donnemartin/system-design-primer",
  "https://github.com/facebook/react",
  "https://github.com/tensorflow/tensorflow",
  "https://github.com/trekhleb/javascript-algorithms",
  "https://github.com/twbs/bootstrap",
  "https://github.com/vinta/awesome-python",
  "https://github.com/ohmyzsh/ohmyzsh",
  "https://github.com/tldr-pages/tldr",
  "https://github.com/ytdl-org/youtube-dl",
  "https://github.com/taigaio/taiga-back"
]\`
```

这是代码的最终输出。

[![stack analyzer ui](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F2im028ae76zrvqo5y4he.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F2im028ae76zrvqo5y4he.png)

我不会涵盖像 `徽章 ` 、 `  文本框  ` 、 ` 堆栈分析卡片` 和 `按钮` 等基本组件的代码。你可以在 `frontend/components/ui` 的代码仓库中查看所有组件。 你可以在 `frontend/components/ui` 的 [代码仓库](https://github.com/CopilotKit/CopilotKit-Deepmind/tree/main/frontend/components/ui) 中 [查看所有组件](https://github.com/CopilotKit/CopilotKit-Deepmind/tree/main/frontend/components/ui) 。

---

### 4\. 后端代理服务（FastAPI + CopilotKit SDK）

在 `/agent` 目录下有一个 FastAPI 服务器，它公开了两个基于 LangGraph 的代理。下面是后端的项目结构，这样你就能更轻松地理解整个布局。  

```
agent/
├── main.py                  ← FastAPI + CopilotKitSDK wiring
├── posts_generator_agent.py ← “Post Generator” graph & nodes
├── stack_agent.py           ← “Stack Analysis” graph & nodes
├── prompts.py               ← system prompts
├── pyproject.toml
└── agent.py                 ← Core agent classes and helpers
```

后端使用 [Poetry](https://python-poetry.org/docs/) 而非 `requirements.txt` 。如果你的系统中没有安装，请进行安装。  

```
pip install poetry
```

然后，在你的 `agent` 目录中，使用以下命令初始化一个新的 Poetry 项目。  

```
cd agent
poetry init  # creates a pyproject.toml here (answer prompts or skip with --no-interaction)
```

这将生成一个全新的 `pyproject.toml` 和 `poetry.lock` ，这意味着你的后端现在有了自己的虚拟环境。

[![poetry init](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fst0l0blyrpdnz3btqser.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fst0l0blyrpdnz3btqser.png)

目前，大多数人工智能生态系统（LangChain、LangGraph、Google SDK）仅支持 Python 3.12 及以下版本，因此请确保通过使用此命令告诉 Poetry 使用兼容的 Python 版本：<法典>poetry env use python3.12。

[![check if python 3.12 is installed](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F7vuoiawiwtbcy2xqs8f9.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F7vuoiawiwtbcy2xqs8f9.png)

然后安装依赖项。  

```
poetry add fastapi uvicorn copilotkit langgraph langchain langchain-google-genai google-genai pydantic python-dotenv
```

[![install backend dependencies](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F02haw7avkg1bur5t3c1a.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F02haw7avkg1bur5t3c1a.png)

- \`fastapi\`：用于提供代理端点（\`/copilotkit\`）的 Web 框架。
- \`uvicorn\`：用于在生产或开发模式下运行 FastAPI 的 ASGI 服务器。
- \`copilotkit\`：CopilotKit Python 软件开发工具包，它将 LangGraph 工作流程与 CopilotKit 状态流集成在一起。
- \`langgraph\`：一种状态机框架，用于将智能体定义为节点（聊天、分析、结束）的图结构。
- \`langchain\`：提供节点内部使用的核心抽象（\`RunnableConfig\`、消息类型等）。
- \`langchain-google-genai\`：用于 Google Gemini 模型的 LangChain 包装器（例如\`ChatGoogleGenerativeAI\`）。
- \`google-genai\`：用于 Gemini 的 Google 官方客户端软件开发工具包，用于底层调用（例如\`genai.Client\`）。
- \`pydantic\`：模式验证（\`StructuredStackAnalysis\`）以强制输出严格的 JSON 格式。
- \`python-dotenv\` → 加载 \`.env\` 文件以管理 API 密钥（如 \`GOOGLE\_API\_KEY\`）。

现在运行以下命令以生成一个固定了精确版本的 `poetry.lock` 文件。  

```
poetry install
```

[![poetry install](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fhgibhllhezawi25kjxm7.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fhgibhllhezawi25kjxm7.png)

### FastAPI 服务器与软件开发工具包设置

所有代理都运行在一个 FastAPI 服务器（ `agent/main.py` ）之后，该服务器将它们挂载到 `/copilotkit` 上。  

```
from fastapi import FastAPI
import uvicorn
from copilotkit.integrations.fastapi import add_fastapi_endpoint
from copilotkit import CopilotKitSDK, LangGraphAgent
from posts_generator_agent import post_generation_graph
from stack_agent import stack_analysis_graph

app = FastAPI()

sdk = CopilotKitSDK(
    agents=[
        LangGraphAgent(
            name="post_generation_agent",
            description="An agent that can help with the generation of LinkedIn posts and X posts.",
            graph=post_generation_graph,
        ),
        LangGraphAgent(
            name="stack_analysis_agent",
            description="Analyze a GitHub repository URL to infer purpose and tech stack (frontend, backend, DB, infra).",
            graph=stack_analysis_graph,
        ),
    ]
)

add_fastapi_endpoint(app, sdk, "/copilotkit")

# A simple endpoint to confirm the server is alive
@app.get("/healthz")
def health():
    return {"status": "ok"}

def main():
    """Run the uvicorn server."""
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=True,
    )

if __name__ == "__main__":
    main()
```

以下是幕后发生的事情：

- 它会启动一个 FastAPI 服务器
- 在 CopilotKit 中注册两个 LangGraph 代理（ `post_generation_agent` ， `stack_analysis_agent` ）
- 将它们暴露在 `/copilotkit` 上，以便前端可以与它们进行通信
- Runs with Uvicorn

---

## 5\. 代理工作流程（LangGraph 状态图）

这两个智能体都被表示为 LangGraph 状态机，并通过几个异步节点拼接在一起。

每个智能体文件（无论是 `posts_generator_agent.py` 还是 `stack_agent.py` ）都遵循相同的 LangGraph 框架：

- Define a `StateGraph`
- 添加节点（每个节点 = 异步函数）
- 连接边（ `START → … → END` ）
- Compile with `MemorySaver()`

但发生变化的是 **每个节点实际执行的操作** 。

### 帖子生成器图表

“文章生成器”工作流程在 [`posts_generator_agent.py`](https://github.com/CopilotKit/CopilotKit-Deepmind/blob/main/agent/posts_generator_agent.py) 中定义。它将三个节点（ `chat_node` 、 `fe_actions_node` 、 `end_node` ）连接成一个已编译的状态图。  

```
# Standard library
import os, uuid, asyncio
from typing import Dict, List, Any, Optional

# Environment
from dotenv import load_dotenv

# Google GenAI
from google import genai
from google.genai import types
from langchain_google_genai import ChatGoogleGenerativeAI

# LangGraph
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import Command
from langchain_core.runnables import RunnableConfig
from langchain_core.messages import AIMessage

# CopilotKit
from copilotkit import CopilotKitState
from copilotkit.langgraph import copilotkit_emit_state
from copilotkit.langchain import copilotkit_customize_config

# Local
from prompts import system_prompt, system_prompt_3

load_dotenv()

class AgentState(CopilotKitState):
    tool_logs: List[Dict[str, Any]]
    response: Dict[str, Any]

# --- Nodes ---

async def chat_node(state: AgentState, config: RunnableConfig):

    model = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    state["tool_logs"].append(
        {
            "id": str(uuid.uuid4()),
            "message": "Analyzing the user's query",
            "status": "processing",
        }
    )
    await copilotkit_emit_state(config, state)

    if state["messages"][-1].type == "tool":
        client = ChatGoogleGenerativeAI(
            model="gemini-2.5-pro",
            temperature=1.0,
            max_retries=2,
            google_api_key=os.getenv("GOOGLE_API_KEY"),
        )
        messages = [*state["messages"]]
        messages[-1].content = (
            "The posts had been generated successfully. Just generate a summary of the posts."
        )
        resp = await client.ainvoke(
            [*state["messages"]],
            config,
        )
        state["tool_logs"] = []
        await copilotkit_emit_state(config, state)
        return Command(goto="fe_actions_node", update={"messages": resp})

    grounding_tool = types.Tool(google_search=types.GoogleSearch())
    model_config = types.GenerateContentConfig(
        tools=[grounding_tool],
    )
    # Define config for the model
    if config is None:
        config = RunnableConfig(recursion_limit=25)
    else:
        # Use CopilotKit's custom config functions to properly set up streaming
        config = copilotkit_customize_config(
            config, emit_messages=True, emit_tool_calls=True
        )

    # Bind the tools to the model
    response = model.models.generate_content(
        model="gemini-2.5-pro",
        contents=[
            types.Content(role="user", parts=[types.Part(text=system_prompt)]),
            types.Content(
                role="model",
                parts=[
                    types.Part(
                        text="I understand. I will use the google_search tool when needed to provide current and accurate information."
                    )
                ],
            ),
            types.Content(
                role="user", parts=[types.Part(text=state["messages"][-1].content)]
            ),
        ],
        config=model_config,
    )
    state["tool_logs"][-1]["status"] = "completed"
    await copilotkit_emit_state(config, state)
    state["response"] = response.text
    # Define the system message by which the chat model will be run
    for query in response.candidates[0].grounding_metadata.web_search_queries:
        state["tool_logs"].append(
            {
                "id": str(uuid.uuid4()),
                "message": f"Performing Web Search for '{query}'",
                "status": "processing",
            }
        )
        await asyncio.sleep(1)
        await copilotkit_emit_state(config, state)
        state["tool_logs"][-1]["status"] = "completed"
        await copilotkit_emit_state(config, state)
    return Command(goto="fe_actions_node", update=state)

async def fe_actions_node(state: AgentState, config: RunnableConfig):
    try:
        if state["messages"][-2].type == "tool":
            return Command(goto="end_node", update=state)
    except Exception as e:
        print("Moved")

    state["tool_logs"].append(
        {
            "id": str(uuid.uuid4()),
            "message": "Generating post",
            "status": "processing",
        }
    )
    await copilotkit_emit_state(config, state)
    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-pro",
        temperature=1.0,
        max_retries=2,
        google_api_key=os.getenv("GOOGLE_API_KEY"),
    )
    await copilotkit_emit_state(config, state)
    response = await model.bind_tools([*state["copilotkit"]["actions"]]).ainvoke(
        [system_prompt_3.replace("{context}", state["response"]), *state["messages"]],
        config,
    )
    state["tool_logs"] = []
    await copilotkit_emit_state(config, state)
    return Command(goto="end_node", update={"messages": response})

async def end_node(state: AgentState, config: RunnableConfig):
    print("inside end node")
    return Command(goto=END, update={"messages": state["messages"], "tool_logs": []})

def router_function(state: AgentState, config: RunnableConfig):
    if state["messages"][-2].role == "tool":
        return "end_node"
    else:
        return "fe_actions_node"

# --- Graph wiring ---
workflow = StateGraph(AgentState)
workflow.add_node("chat_node", chat_node)
workflow.add_node("fe_actions_node", fe_actions_node)
workflow.add_node("end_node", end_node)
workflow.set_entry_point("chat_node")
workflow.set_finish_point("end_node")
workflow.add_edge(START, "chat_node")
workflow.add_edge("chat_node", "fe_actions_node")
workflow.add_edge("fe_actions_node", END)

post_generation_graph = workflow.compile(checkpointer=MemorySaver())
```

大致流程如下：

1. \`chat\_node\`：通过\`genai.Client\`调用 Google Gemini，可选择调用网络搜索工具，将中间工具日志流式传输回用户界面
2. \`fe\_actions\_node\`: 对聊天结果进行后处理，以生成最终的领英/推特帖子
3. \`end\_node\`：结束工作流程

### 堆栈分析图

同样，“堆栈分析器”工作流程在 `stack_agent.py` 中定义。它还将三个节点（ `gather_context_node` 、 `analyze_with_gemini_node` 、 `end_node` ）连接到一个编译后的状态图中。  

```
# OpenAI‑style tool that ensures the JSON schema is enforced
@tool("return_stack_analysis", args_schema=StructuredStackAnalysis)
def return_stack_analysis_tool(**kwargs) -> Dict[str, Any]:
    """Return the final stack analysis in strict JSON."""
    # …validate and return…
    validated = StructuredStackAnalysis(**kwargs)
    return validated.model_dump(exclude_none=True)

# ...
workflow = StateGraph(StackAgentState)
workflow.add_node("gather_context", gather_context_node)
workflow.add_node("analyze", analyze_with_gemini_node)
workflow.add_node("end", end_node)
workflow.add_edge(START, "gather_context")
workflow.add_edge("gather_context", "analyze")
workflow.add_edge("analyze", END)
workflow.set_entry_point("gather_context")
workflow.set_finish_point("end")

stack_analysis_graph = workflow.compile(checkpointer=MemorySaver())
```

与文章生成器不同，这个智能体要大得多（约500行）。我不会粘贴所有内容，而是会通过关键代码片段逐一讲解每个节点。

你可以查看仓库以获取 [完整实现](https://github.com/CopilotKit/CopilotKit-Deepmind/blob/main/agent/stack_agent.py) （包含重试、详细日志记录和模式验证）。

每个节点及其实际功能：

✅ 1. `gather_context_node` ：此节点从用户消息中解析 GitHub URL，通过 GitHub API 获取元数据（仓库信息、语言、README、根文件、清单），并将其存储在 `state["context"]` 中以供下游分析。  

```
async def gather_context_node(state: StackAgentState, config: RunnableConfig):
    last_user_content = state["messages"][-1].content if state["messages"] else ""
    parsed = _parse_github_url(last_user_content)

    if not parsed:
        return Command(goto="analyze", update={...})

    owner, repo = parsed
    repo_info = _fetch_repo_info(owner, repo)
    languages = _fetch_languages(owner, repo)
    readme = _fetch_readme(owner, repo)
    root_items = _list_root(owner, repo)
    manifests = _fetch_manifest_contents(owner, repo, repo_info.get("default_branch"), root_items)

    context = {"owner": owner, "repo": repo, "repo_info": repo_info,
               "languages": languages, "readme": readme,
               "root_files": _summarize_root_files(root_items),
               "manifests": manifests}

    return Command(goto="analyze", update={"context": context, ...})
```

✅ 2. `analyze_with_gemini_node` ：根据仓库上下文构建一个结构化输出提示，并要求 Gemini（ `gemini-2.5-pro` ）进行分析。Gemini 需要调用 `return_stack_analysis` 工具，该工具强制执行严格的 JSON 模式。  

```
async def analyze_with_gemini_node(state: StackAgentState, config: RunnableConfig):
    prompt = _build_analysis_prompt(state["context"])
    messages = [
        SystemMessage(content="You are a senior software architect..."),
        HumanMessage(content=prompt),
    ]

    model = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.4, ...)
    bound = model.bind_tools([return_stack_analysis_tool])
    tool_msg = await bound.ainvoke(messages, config)

    # Extract structured payload (stack details)
    for call in getattr(tool_msg, "tool_calls", []):
        if call.get("name") == "return_stack_analysis":
            args = call.get("args", {})
            state["analysis"] = json.dumps(args)
            state["show_cards"] = True
```

✅ 3. `end_node` ：此最终节点清除工具日志，并将完成的分析结果发送回用户界面。  

```
async def end_node(state: StackAgentState, config: RunnableConfig):
    state["tool_logs"] = []
    await copilotkit_emit_state(config or RunnableConfig(recursion_limit=25), state)
    return Command(goto=END, update={
        "messages": state["messages"],
        "show_cards": state["show_cards"],
        "analysis": state["analysis"]
    })
```

---

## 6\. 提示词与工具

在连接图和节点之前，智能体在很大程度上依赖于 `  提示和工具  ` 。提示定义了模型应如何表现（例如 “始终使用谷歌搜索” 或 “以领英风格生成帖子”），而工具则提供了捕获输出的结构化方法。

让我们介绍一下这两种代理共有的核心构建块：系统提示、结构化输出工具以及用于构建分析提示的辅助函数。

### ✅ 生成帖子后的系统提示

文章生成器的所有“系统和用户提示”模板都位于 `agent/prompts.py` 中。这些模板充当代理的角色。

将提示词保存在不同的文件中，这样就可以独立于工作流逻辑轻松地进行调整。  

```
system_prompt = """You have access to a google_search tool …
You MUST ALWAYS use the google_search tool for EVERY query…"""

system_prompt_2 = """
You are an Amazing artist. You need to generate an image …
"""

system_prompt_3 = """
You are an amazing assistant. You are familiar with the LinkedIn and X (Twitter) algorithms…
Always use the generate_post tool to generate the post.
{context}
"""
```

**How it is used:**

- \`system\_prompt\` 被注入到 \`chat\_node\` 内部，迫使 Gemini 使用 \`google\_search\` 工具来给出有依据的答案。
- 在\`fe\_actions\_node\`内部使用\`system\_prompt\_3\`来告知 Gemini 如何组织领英/推特帖子的内容。

### ✅ 构建堆栈分析提示

在堆栈分析器中，我们使用一个辅助函数将 GitHub 仓库上下文注入到单个“分析堆栈”提示中。此函数位于 `agent/stack_agent.py` 中。

与提示不同，这个助手与栈分析逻辑（模式、上下文解析）紧密耦合，所以它在同一个代理文件中。  

```
def _build_analysis_prompt(context: Dict[str, Any]) -> str:
    return (
        "You are a senior software architect. Analyze the following GitHub repository at a high level.\n"
        "Goals: Provide a concise, structured overview of what the project does and the tech stack.\n\n"
        f"Repository metadata:\n{json.dumps(context['repo_info'], indent=2)}\n\n"
        f"Languages:\n{json.dumps(context['languages'], indent=2)}\n\n"
        "Root items:\n" + json.dumps(context['root_files'], indent=2) + "\n\n"
        "README content (truncated):\n" + context["readme"][:8000] + "\n\n"
        "Infer the stack with specific frameworks and libraries when possible…"
    )
```

**How it is used:**

- \`\_build\_analysis\_prompt\` 在 \`analyze\_with\_gemini\_node\` 中被传入 Gemini，提供仓库元数据、语言、清单和 README 的综合视图。

### ✅ 用于堆栈分析的结构化输出工具

在\`stack\_agent.py\`中，我们声明了一个强制输出 JSON 格式的 OpenAI 风格的工具。  

```
@tool("return_stack_analysis", args_schema=StructuredStackAnalysis)
def return_stack_analysis_tool(**kwargs) -> Dict[str, Any]:
    """Return the final stack analysis in a strict JSON structure."""
    validated = StructuredStackAnalysis(**kwargs)
    return validated.model_dump(exclude_none=True)
```

**How it is used:**

- \`return\_stack\_analysis\_tool\` 在 \`analyze\_with\_gemini\_node\` 中与 Gemini 绑定，因此它必须输出 JSON 而不是自由格式的文本。

该模式确保每个仓库分析都具有相同的结构，这样界面就能可靠地显示出来。

---

## 7\. Complete flow

一旦我们整合了所有部分，端到端的数据流就是这样的。如果你跟进了那篇博客，理解起来会更容易。

```
┌────────────────┐
        
        
          

          │  Browser UI    │
        
        
          

          │ (CopilotChat)  │
        
        
          

          └───────┬────────┘
        
        
          

                  │ POST /api/copilotkit (GraphQL)
        
        
          

                  ▼
        
        
          

          ┌────────────────────────────────────────────────┐
        
        
          

          │ Next.js API Route                              │
        
        
          

          │ (copilotRuntimeNextJSAppRouterEndpoint)        │
        
        
          

          └───────┬────────────────────────────────────────┘
        
        
          

                  │ proxies to
        
        
          

                  ▼
        
        
          

          ┌────────────────────────────────────────────────┐
        
        
          

          │ FastAPI + CopilotKitSDK                        │
        
        
          

          │ (agent/main.py)                                │
        
        
          

          │   • pick agent by name                         │
        
        
          

          │   • feed LangGraphAgent → graph.run()          │
        
        
          

          └───────┬────────────────────────────────────────┘
        
        
          

                  │ invokes
        
        
          

                  ▼
        
        
          

          ┌────────────────────────────────────────────────┐
        
        
          

          │ LangGraph StateGraph                           │
        
        
          

          │   • chat_node / gather_context_node…           │
        
        
          

          │   • streams intermediate state via             │
        
        
          

          │     copilotkit_emit_state()                    │
        
        
          

          └───────┬────────────────────────────────────────┘
        
        
          

                  │ calls
        
        
          

                  ▼
        
        
          

          ┌────────────────────────────────────────────────┐
        
        
          

          │ Google Gemini (LLM) + google_search tool       │
        
        
          

          │ (ChatGoogleGenerativeAI)                       │
        
        
          

          │   • generate_content()                         │
        
        
          

          └───────┬────────────────────────────────────────┘
        
        
          

                  │ streaming responses & tool_calls
        
        
          

                  ▼
        
        
          

          ┌────────────────────────────────────────────────┐
        
        
          

          │ CopilotKitSDK streams back messages, logs…     │
        
        
          

          └───────┬────────────────────────────────────────┘
        
        
          

                  │ consumed by
        
        
          

                  ▼
        
        
          

          ┌─────────────────┐
        
        
          

          │ Browser UI      │
        
        
          

          │ (renders chat,  │
        
        
          

          │  tool‑logs,     │
        
        
          

          │  post cards or  │
        
        
          

          │  analysis cards)│
        
        
          

          └─────────────────┘
```

---

## 8\. The Final Demo

完成代码的所有部分后，就该在本地运行它了。请确保你已将 Google Gemini 凭证添加到 `.env` 文件中。

### 启动后端（FastAPI 代理）

在 `agent` 目录中运行以下命令。  

```
cd agent
poetry install
# set GOOGLE_API_KEY in agent/.env
poetry run python main.py
```

[![running backend locally](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fqf1mjt0rkxu84zzc4nap.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fqf1mjt0rkxu84zzc4nap.png)

### Start Frontend

运行以下命令以在本地的 `frontend` 下启动服务器，然后在浏览器中导航到 [localhost:3000/copilotkit](http://localhost:3000/copilotkit) 以查看你的前端。  

```
cd frontend
pnpm install # if you have cloned the repo
pnpm run dev
```

[![frontend running locally](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F4q9qd3gdvmhwxoaqdcfn.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F4q9qd3gdvmhwxoaqdcfn.png)

### 🎯 文章生成代理的输出

默认路由将通向 `post-generator` 代理。如你所见，它通过深入研究正确地生成了帖子。

它会发出中间的“工具日志”，这样用户界面就能实时显示每个研究/搜索/生成步骤，而且你还能找到一些预建的起始提示，一键即可开始。

![](https://www.youtube.com/watch?v=HCXhFovyv8U)

### 🎯 堆栈分析器代理的输出

它会分析一个公开的 GitHub 仓库（元数据、README、代码清单）并推断其技术栈。

如我之前所述，它使用一个 Pydantic 数据模型（ `StructuredStackAnalysis` ）来强制实现一个严格定义的 JSON 输出，涵盖：

- Project purpose
- 前端技术栈（框架/语言/库）
- 后端技术栈（框架/语言库/架构）
- Database details
- 基础设施/托管
- CI/CD setup
- Key root files
- 运行说明
- Risk/notes sections

![](https://www.youtube.com/watch?v=DJMkP28TdBQ)

与帖子生成器类似，它会将每个步骤（URL 解析→获取元数据→分析→总结）流式传输回用户界面。

---

就是这样。这里用户使用的模式（有状态图、工具绑定、结构化输出）将为你节省数小时的时间。

我希望你在这本实践指南中发现了一些有价值的东西。如果你之前构建过什么东西，请在评论中分享。

祝你度过美好的一天！下次见 ：）

| You can check   我在 [anmolbaranwal.com](https://anmolbaranwal.com/) 的工作。   感谢阅读！🥰 |  |
| --- | --- |

在 [推特](https://go.copilotkit.ai/socials-twitter) 上关注 CopilotKit 并打招呼，如果你想构建一些很酷的东西，加入 [Discord](https://go.copilotkit.ai/discord-community) 社区。