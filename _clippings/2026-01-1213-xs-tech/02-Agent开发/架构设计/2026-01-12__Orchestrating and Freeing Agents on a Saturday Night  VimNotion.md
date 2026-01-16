---
title: "Orchestrating and Freeing Agents on a Saturday Night | VimNotion"
source: "https://www.vimnotion.com/blog/orchestrated-vs-free-agents"
author:
date: "2026-01-12T10:10:09+08:00"
created: 2026-01-12
description: "Let's compare how a strictly orchestrated agent compares to a sandboxed agent free to run in a loop"
tags:
---
[VimNotion](https://vimnotion.com/)

[docs](https://vimnotion.com/docs/editor) [blog](https://vimnotion.com/blog) [about](https://vimnotion.com/about)

[< Back to blog](https://vimnotion.com/blog)

Written by: Jack

发布于 2025 年 1 月 11 日

## 周六晚上：代理的编排与解放

是的，今天周六晚上。没错，我正花时间捣鼓不同的代理实现。不，这不是工作需要。

在把所有那些事情都处理妥当之后，我一直对开发两种类型的人工智能应用抱有浓厚兴趣：

1. 一个严格编排的代理工作流程
2. 一个“解放的代理”，能够自由循环并调用工具。

我想到一个任务，它对两种使用场景都非常适用。

> 从经常浏览以获取文章的网站创建一份定制新闻通讯

我们来看看会发生什么吧！

---

## 协调型代理 vs 自由代理

撰写新闻通讯这类任务可以分解成一系列子任务。如果我亲自来做，其撰写流程大概如下：

1. 我会快速浏览像 HackerNews 这样的网站，查看帖子标题
2. 我点击感兴趣的链接来阅读更多内容
3. 我为我喜欢的文章写摘要
4. 我挑选一个主题，把为通讯挑选的文章串联起来

不难想象这些步骤用代码编写，特别是借助 LLMs 来对非结构化数据进行结构化处理。

![ascii-workflow](https://api.vimnotion.com/image/5cad7fa8-7703-44c6-bb00-080ebf24da2b)

### 编排好的代理

编排好的代理是指我明确定义其工作流程的代理。每一步（或工作流图中的节点）要么运行

- 代码调用类似 Firecrawl 的 API 并重新组织数据
- 一个用于生成文本或结构化数据的 LLM 步骤

我的编排框架受到了诸如 ai-sdk 的工作流、LangChain 的 LangGraph 以及我的运筹学课程的启发。（我怀念曾经的单纯形法和最小割流算法，但跑题了。）

LLM 生成结构化数据的能力真是神奇。它就像一座桥梁，使我们能够从文本中提取信息，构建一个具备类型安全的结构化模式，以支持后续的代码步骤（将代码整合起来，没有语言模型是无法实现的）。

```typescript
const selectorNode = new GraphNode<MdLinks, EnrichedLinks, NodeNames>({
    nodeType: NodeNames.SELECTOR_NODE,
    description: "From a webpage, an agent will select the most interesting articles with links",
    exec: async (input: MdLinks) => {
        const systemPrompt: string = \`You are a content curator tasked with selecting article titles that will interest the unique reader. 
        Readers will give you a page with articles and you will select only the top "x" number of articles that they may like.
        Only respond with the list of article titles!\`;

        const filteredLinks: EnrichedLinks = {};
        for (const url of Object.keys(input)) {
            const prompt: string = \`${input[url]?.instructions} 
                        Select up to ${input[url]?.limit} articles from this page:
                        ${input[url]?.md}\`;
            const articleList: { title: string, url: string }[] = await retry<{ title: string, url: string }[]>(async () => {
                const { output } = await generateText({
                    model: "anthropic/claude-sonnet-4.5",
                    system: systemPrompt,
                    prompt: prompt,
                    output: Output.array({
                        element: z.object({
                            title: z.string().describe("Title of the article picked"),
                            url: z.string().describe("url of the article picked"),
                        }),
                    }),
                });
                return output
            }, 3, 1);
            filteredLinks[url] = { ...input[url], links: articleList }
        }
        return filteredLinks;
    },
    routing: (): NodeNames | null => {
        return NodeNames.SUMMARIZER_NODE;
    },
});
```

### 获得解放的自由代理人

自由代理是一种配备包含运行时、工具、提示词和文件系统的框架的智能体，会循环直到任务完成。我使用了 LangChain 的 deepagents，因为它内置了一个用于与子代理和文件系统工具配合使用的预配置框架。

```typescript
const agent = createAgent({
    model: "claude-sonnet-4-5-20250929",
    middleware: [
        toolCallLimitMiddleware({
            toolName: "markdown_search",
            threadLimit: 8,
            runLimit: 8,
        }),
        modelCallLimitMiddleware({
            threadLimit: 15,
            runLimit: 15,
            exitBehavior: "end",
        }),
        todoListMiddleware({}),
        createFilesystemMiddleware({
            backend: new FilesystemBackend({
                rootDir: "./"
            })
        }),
    ],
    tools: [markdownSearch],
});
```

我设置了一些限制，避免耗尽我的 Firecrawl 和 Anthropic 信用额度，不过除此之外，这个代理天生就想借助 DeepAgent 框架深入探索，并且在任何方向上都能随心所欲地走得尽可能远。

---

## 谁写的通讯更好？是结构化风格还是创意风格？

我给两个代理都提供了类似的输入提示。对于被编排的代理：

```typescript
const scriptInput: ScriptInput = {
    sources: [
        {
            url: "https://news.ycombinator.com",
            instructions: \`Pick articles that have to do with AI news, typescript, golang, architecture, product tastes, and game dev.
            Ignore posts about jobs, non-tech news, topics about medicine or hardware\`,
            limit: 2
        },
        {
            url: "https://theringer.com",
            instructions: \`I enjoy mostly reading about NBA, player features, and unusual trends about any sport really\`,
            limit: 2
        },
    ]
}
```

For the free agent:

> 请撰写一份包含 2 篇来自 hackernews.com 和 2 篇来自 theringer.com 的文章的新闻通讯。
> 
> 对于科技领域，我喜欢包含人工智能新闻、TypeScript、Go 语言、架构、产品风格和游戏开发的文章。
> 
> 我喜欢阅读体育相关内容，主要是 NBA、球员特写以及任何运动中的不寻常趋势。

这两封通讯，你可以自己判断一下

[结构化图代理精选的通讯](https://www.vimnotion.com/doc/94d52ee5-367e-4826-b7c8-3f9e2ed2ddd4)

[自由职业 DeepAgent 的精选通讯](https://www.vimnotion.com/doc/0fce5392-0a94-4675-8d98-7accb7a1c4d3)

我个人更喜欢自由代理通讯一些。也许是我在某些桥梁 LLM 节点中的提示词导致的，但统筹代理的通讯则更冗长，也更像标题党。

自我反思时，我对自由球员的简讯也更添了几分期待，因为不知道会写些什么。而在精心策划的工作流程中，由于我写了每一步骤，我清楚简讯的具体结构，这反而在一定程度上削弱了那份期待和未知的乐趣。

---

## 智能体设计的启示

这是一次有趣的尝试，用两种不同的设计理念构建代理。

我整体的体会其实并不以性能为考量（我认为两个代理都表现出色，并且编排式图代理更容易调优）：

### 更好的模型和更好的框架使得智能体能够运行更长时间，甚至可以完成复杂的任务

分解任务本质上就是利用“待办事项”工具构建自身工作流，通过在文件中写入大量文本保存上下文，以及从本地文件系统读取文件实现低延迟的检索增强生成（RAG）——这些都是为智能代理提供更优工具支持的典型例子。

### 2\. 编排就像是为代理进行推理

更好的模型和工具意味着构建一个智能体能够推理出复杂任务的世界。但在运行沙箱环境中的深度智能体时，我没有提到的是，token 和成本消耗比编排的智能体高出了天文数字般的水平。在我测试工具时，免费智能体运行这个提示词几次就花费了约 2 美元。控制编排智能体的精确输入极其节省 token 资源，并且所需的 LLM 轮次也少得多。

### 3\. 获得控制权，牺牲灵活性

代码一直以来都是一种非常直接地表达我们想法的方式。你可能会误解词语，但代码每次的解读都是一样的。能够控制每一个 LLM 调用，输入精确的内容并得到精确的输出，这会很有力量。但被编排的代理实际上只能做一件事。如果让同样的编排型图代理去校对文章，它会一败涂地。自由代理拥有通用的工具。提示词是它的脚本，也是它的代码。有时这些代码会被误解，但迭代一个提示词比迭代代码更容易（即使是对编码代理来说也是如此）。

仍然值得探讨的是，评估与迭代编排型代理还是自主运行型代理会更容易。为新的用例编写新的提示词，比创建新的编排流程更容易、更快；但在追踪、调优以及投产路径方面，编排型代理可能更高效。也许？

那得留到另一个周六晚上再讨论了。

:wq

\-Jack