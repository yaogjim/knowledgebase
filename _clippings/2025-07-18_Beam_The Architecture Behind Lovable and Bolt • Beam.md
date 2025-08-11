---
title: "The Architecture Behind Lovable and Bolt • Beam"
source: "https://www.beam.cloud/blog/agentic-apps"
author:
  - "[[Beam]]"
published: 2025-07-11
created: 2025-07-18
description: "A Deep Dive into Production-Grade Agentic Apps"
tags:
  - "clippings"
---
## 可爱多与博尔特背后的架构

卢克·隆巴迪

2025年7月3日

教程

![](https://cdn.sanity.io/images/eb1odxxp/blogs/bd4fcdaac28d920fac6b0b6c958c25b344849337-2400x1350.jpg)

人工智能编码应用程序正在迅速发展。

有一天，我们看到一家人工智能编码初创公司给出的一张荒唐的营收图表，然后心想： *这背后到底是怎么回事* ？

如果你从事软件行业，今年你可能已经尝试过人工智能应用程序构建器了。也许你试用过 [Lovable](https://lovable.dev/) 、 [Bolt](https://bolt.new/) 或 [v0](https://v0.dev/) 。

这些应用程序的突然爆火，不只是因为模型更出色。而是因为我们这个行业终于弄清楚了实用的智能应用背后的工程原理（ *提示* ：这更多是软件工程，而非人工智能魔法）。

我们想要深入了解在现实世界中构建这类应用程序所使用的具体工作流程，所以我们创建了自己的 Lovable 克隆版本来一探究竟。

*在 Beam，我们为人工智能应用程序提供了一个无服务器基础设施平台。一个常见的用例是使用我们的 [沙盒](https://docs.beam.cloud/v2/sandbox/overview) 功能安全地运行由 LLM 生成的代码，该功能为我们将在下面构建的应用程序提供支持。*

![content-image](https://cdn.sanity.io/images/eb1odxxp/blogs/ec0f6933353bb44601a737b681eea578be1c43a5-2360x1422.png)

## 代理应用程序的实际工作原理

一个人工智能编码应用程序有四个组件：

1. **模型客户端。** 可以将提示视为远程过程调用（RPC）。
2. **一个供用户/模型进行交互的环境** 。这通常采用代码沙盒（小型虚拟机或容器）+ MCP 服务器的形式（本质上是另一个 RPC 框架，带有一些元数据，能为模型提供更多关于 *如何* 与之交互的上下文信息）
3. **智能体。** 一个维护状态、将用户输入路由到模型并协调前端、提示和执行环境之间交互的循环。
4. **一个前端。** 通常通过实时协议（如 WebSocket）连接到“代理”。

在这种情况下，由于我们正在构建一个类似 Lovable 的克隆产品，其用户体验如下：

- 用户输入他们想要构建的内容
- 模型接收提示，尝试为其实现代码
- 在“预览”iframe 中渲染网站
- 重复操作，直到用户对该网站满意为止
![content-image](https://cdn.sanity.io/images/eb1odxxp/blogs/ba562a3f524eaad6003ebc7dafcbd944a1d18faf-1746x1130.png)

## 使用 BAML 进行提示工程

让我们从提示开始。我们将提示视为一个具有逻辑和状态的函数。

我们正在使用 [BAML](https://github.com/BoundaryML/baml) ，这是一种与模型无关的领域特定语言（DSL），它能帮助我们以简化的方式迭代提示。在 BAML 中，一个提示只是一个函数。

```yaml
class File {
  path string
  content string
  @@stream.done
}

class Message {
  role string
  content string
}

class CodeChanges {
  plan string @stream.with_state
  files File[]
  package_json string
}

client<llm> OpenAIClient {
  provider openai
  options {
    model o4-mini
    api_key env.OPENAI_API_KEY
  }
}

function EditCode(
  history: Message[],
  feedback: string,
  code_files: File[],
  package_json: string
) -> CodeChanges {
  client OpenAIClient
  prompt #"
You are BeamO. Given the feedback: {{ feedback }}, update the code files.

{% for file in code_files %}
{{ file.path }}
{{ file.content }}
{% endfor %}

Use only dependencies from:
{{ package_json }}

Conversation history:
{% for msg in history %}
{{ msg.role }}: {{ msg.content }}
{% endfor %}

Return a plan and updated files.
"#
}
```

> 你可以在此处查看 [完整提示](https://gist.github.com/mernit/86d34644096518db97709eadf9aa8622) 。

请注意，我们可以编写测试用例，这使我们能够在继续并开始将其集成到智能体循环之前，对提示进行反复改进。

核心思想是传入一堆带分隔符的代码，并告诉模型根据用户反馈进行修改。还有一些额外的指导方针，试图引导模型使用正确的依赖项、样式等。

## 启动 MCP 服务器

一旦我们有了一个可行的提示，下一步就是围绕它构建基础设施。

我们将使用 [FastMCP](https://github.com/jlowin/fastmcp) （一个用于构建 MCP 服务器的轻量级框架）以及 Beam 在云端无服务器地托管计算服务器。

这里的流程是：

- 用户在文本输入框中输入他们想要构建的内容
- 启动一个 Beam 沙盒计算环境，并克隆一个基本模板存储库以便开始工作（使用 MCP 服务器）
- 该智能体与其他工具进行交互，这些工具将使模型能够在沙盒中下载和编辑代码。

要以编程方式设置沙盒环境，我们将使用一个 [Beam 沙盒](https://docs.beam.cloud/v2/sandbox/overview) ：

```python
from beam import Image, Sandbox
from beam.integrations import MCPServer
from fastmcp import FastMCP

mcp = FastMCP(name="lovable-mcp")
image = (
   Image()
   .from_registry("node:20")
   .add_commands(
       [
           "apt-get update && apt-get install -y git curl",
           "git clone https://github.com/beam-cloud/react-vite-shadcn-ui.git /app",
           "cd /app && rm -f pnpm-lock.yaml && npm install && echo 'npm install done'",
           "cd /app && npm install @tanstack/react-query react-router-dom recharts sonner zod react-hook-form @hookform/resolvers date-fns uuid",
       ]
   )
)

DEFAULT_CODE_PATH = "/app/src"
DEFAULT_PROJECT_ROOT = "/app"

@mcp.tool
def create_app_environment() -> dict:
   print("Creating app environment...")

   sandbox = Sandbox(
       name="lovable-clone",
       cpu=1,
       memory=1024,
       image=image,
       keep_warm_seconds=300,
   ).create()

   url = sandbox.expose_port(3000)
   print(f"React app created and started successfully! Access it at: {url}")
   sandbox.process.exec(
       "sh",
       "-c",
       "cd /app && __VITE_ADDITIONAL_SERVER_ALLOWED_HOSTS=.beam.cloud npm run dev -- --host :: --port 3000",
   )

   print("Created app environment...")
   return {
       "url": url,
       "sandbox_id": sandbox.sandbox_id(),
   }
```

你可以在 Github 上 [此处](https://github.com/beam-cloud/lovable-clone/blob/main/src/tools.py) 查看 MCP 服务器的其余代码。

## 部署一个功能性人工智能应用构建器

最后一个组件是代理本身，它只是一个处理来自客户端事件的 WebSocket 服务器。

> 在这里查看代理的代码 [此处](https://github.com/beam-cloud/lovable-clone/blob/main/src/agent.py) 。

当客户端/用户连接到 WebSocket 服务器时，我们将为预览环境启动一个新的沙盒。

当用户消息传入时，我们将持续调用 `EditCode` 提示/RPC，并更新 [沙盒](https://docs.beam.cloud/v2/sandbox/overview) 中的代码。

这是通过添加一个 [`@realtime`](https://docs.beam.cloud/v2/endpoint/realtime#realtime-and-streaming) 装饰器创建的，它只是一个简单的装饰器，可让您在云中启动一个无服务器的 WebSocket 服务器。

## 成品

前端运行起来后，我们将得到一个功能完备的人工智能应用构建器。

其结果是一个完全交互式的应用程序构建器，它能实时响应用户反馈并即时生成实时预览。

用户可以输入一个提示（“为我构建一个 YouTube 克隆版”），然后获得一个可运行的实时 Web 应用程序，该应用程序托管在云端的 HTTP URL 后面。

[在这里自己试试。](https://website-builder-demo-f5340af-v7.app.beam.cloud/)

![content-image](https://cdn.sanity.io/images/eb1odxxp/blogs/8208cd12a530ce9ac2ccd483b1b65f6e4d4d0960-3120x1532.png)

## 我们学到了什么

在构建这个之前，我们认为可爱风格的应用是可行的，因为模型在不断改进。但结果发现这只是其中很小的一部分原因。以下是我们学到的最重要的几点见解：

- **提示工程很重要。** 你可以使用 [这份系统提示列表](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/) 找到优秀提示的示例。
- **上下文工程更为重要。** 没有正确的上下文，一个好的提示词是无用的。像 Lovable 这样的应用程序需要长上下文才能良好运行。使这些应用程序发挥作用的不是大语言模型（LLMs），而是用诸如带有 BAML 的类型化提示词、测试和重试等护栏将它们包裹起来。
- **像对待代码一样测试提示被低估了。** BAML 是一个非常强大的工具，因为它使迭代提示变得容易，并且可以像测试驱动开发一样对待提示工程。

人工智能编码应用背后的架构是可重复的。

要构建一个人工智能编码应用程序，你不需要更好的模型，而是需要更好的系统设计：提示结构、上下文管理、沙盒化以及一个良好的测试框架。

这就是像 Lovable 这样的应用程序能够真正运行的原因。

这不是魔法。这只是软件工程。

本文的代码可在 [GitHub 上获取](https://github.com/beam-cloud/lovable-clone) 。如果你使用此架构构建了什么东西，我们很乐意 [收到你的消息](https://join.slack.com/t/beam-cloud/shared_invite/zt-2uiks0hc6-UbBD97oZjz8_YnjQ2P7BEQ) ！

## Notes

感谢德克斯特·霍西（Dexter Horthy）和维巴夫·古普塔（Vaibhav Gupta）为本文提供建议。

### 继续阅读

[![card-cover-image](https://cdn.sanity.io/images/eb1odxxp/blogs/53bd8d69ff7d598a50ce0d01c267e42fafc67c14-2400x1350.jpg)](https://www.beam.cloud/blog/top-comfyui-workflows)

教程

## 顶级 ComfyUI 工作流程

探索 ComfyUI 中最佳的工作流程

莉亚·蔡尔德斯

[![card-cover-image](https://cdn.sanity.io/images/eb1odxxp/blogs/0e535689776ef886fa80ca17908db7e4b24c9d83-2400x1350.jpg)](https://www.beam.cloud/blog/how-to-use-comfyui)

教程

## 如何使用 ComfyUI

一份关于使用 ComfyUI 的完整指南，涵盖从安装说明到参数及工作流程优化的内容。

莉亚·蔡尔德斯

## 在几分钟内部署您的应用程序

获得30美元免费信用额度，开启体验之旅