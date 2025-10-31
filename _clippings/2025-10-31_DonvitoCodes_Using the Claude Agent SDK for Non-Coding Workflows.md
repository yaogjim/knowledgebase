---
title: "Using the Claude Agent SDK for Non-Coding Workflows"
source: "https://blog.donvitocodes.com/using-the-claude-agent-sdk-for-non-coding-workflows"
author:
  - "[[DonvitoCodes]]"
published: 2025-10-31
created: 2025-10-31
description: "I’ve been exploring the Claude Agent SDK, and I had this idea — why not use it for non-coding workflows instead of relying on other agent frameworks like CrewAI or LangChain?To validate the idea, I built a simple example: a news researcher agent tha..."
tags:
  - "DonvitoCodes"
---


## 利用 Claude 智能体 SDK 实现非编码工作流

我一直在研究 [**Claude Agent SDK**](https://docs.claude.com/en/api/agent-sdk/overview) ，突然有个想法——与其依赖其他智能体框架如 **CrewAI** 或 **LangChain** ，何不将其用于 *非编程工作流* 呢？

为了验证这个想法，我构建了一个简单示例：一个能查找最新人工智能新闻并将其翻译成韩语的 **新闻研究助手** 。

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1761825468875/cb2f638a-b742-429b-aa28-47ee752af6c0.png?auto=compress,format&format=webp)

## The Setup

这是核心脚本：

```python
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition
from claude_agent_sdk.types import McpHttpServerConfig
import os

async def main():
    firecrawl_api_key = os.environ['FIRECRAWL_API_KEY']
    firecrawl_mcp = McpHttpServerConfig(
        type="http",
        url="https://mcp.firecrawl.dev/v2/mcp",
        headers={"Authorization": f"Bearer {firecrawl_api_key}"}
    )

    translator_agent = AgentDefinition(
        description="Translate the content from any language to any other language.",
        prompt="You are an expert language translator.",
        tools=["Read", "Edit", "Bash", "Grep"],
        model="sonnet"
    )

    options = ClaudeAgentOptions(
        model="glm-4.6",
        system_prompt="You are an expert news researcher.",
        permission_mode='bypassPermissions',
        cwd="/Users/melvin/PycharmProjects/ClaudeCodeSDK/output",
        mcp_servers={"firecrawl_mcp": firecrawl_mcp},
        agents={"translator-agent": translator_agent}
    )

    async for message in query(
        prompt=(
            "What are the latest news topics in AI? "
            "Write the results to a markdown file with URLs as references. "
            "Then use the translator-agent to translate the content to Korean "
            "and save it to a separate markdown file."
        ),
        options=options
    ):
        print(message)

asyncio.run(main())
```

## 概念一：利用 MCP 进行数据检索

我使用了 [Firecrawl MCP](https://docs.firecrawl.dev/mcp-server) 来获取最新的人工智能新闻。

代理自动收集数据、进行总结，并将结果写入 Markdown 文件。

这展示了 MCP 如何像 API 插件层一样运作，使智能体能够超越简单提示执行现实世界的数据收集任务。

---

## 概念二：专用于特定任务的子代理

收集完新闻后，我想要一份翻译版本。

我没有硬编码翻译逻辑，而是专门为此创建了一个 **子代理** ——翻译代理。

主代理随后将翻译任务委派给了子代理。

[The output](https://firecrawl.dev/):

- ai\_news\_ [en.md](http://en.md/) – 英文摘要
- ai\_news\_ [ko.md](http://ko.md/) – 韩语翻译

---

## Why This Matters

**Claude Agent SDK** 现已支持：

- **工具** （读取、编辑、Bash 等）
- **MCPs** （外部能力服务器）
- **Skills**
- **Sub-agents**

这些正是其他 AI 智能体框架需要从零构建的组件——但在 Claude 生态系统中，它们都是原生集成的。

借助 **Claude AI** 构建的技术，开发者和研究人员能够快速编排超越对话功能的工作流——从文档生成到自动化流程皆可实现。

本例中我使用了 **GLM 4.6** 模型，不过它当然也能 [完美兼容](https://firecrawl.dev/) 像 **Haiku** 和 **Sonnet** 这样的 Claude 模型。

## AI Agent 框架的绝佳替代方案

像 CrewAI 和 LangChain 这样的框架非常适合构建复杂的智能体系统，但有时，简单才是制胜之道。

**Claude Agent SDK** 以轻量级封装为您提供相同的构建模块——工具、子代理和外部连接器——并能与 Claude 生态系统无缝集成。
