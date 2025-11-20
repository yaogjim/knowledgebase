---
title: "2025-11-20_blog_langchain_com_By_Liam_Bush"
source: "https://blog.langchain.com/rebuilding-chat-langchain/"
author:
  - "[[@tool]]"
published: 2025-11-20
created: 2025-11-20
description:
tags:
  - "#stream"
  - "#L3273"
  - "blog"
  - "@tool"
---

# By Liam Bush

*By Liam Bush*

## Background

每个成功的平台都需要可靠的支持，但我们发现自己的团队花费大量时间追踪技术问题的答案。这种阻力不仅拖慢了工程师的效率——对用户而言更是一个关键的 **瓶颈** 。

我们决定用我们最推崇的工具来解决这个问题： **LangChain、LangGraph** 和 **LangSmith** 。我们最初将 [**chat.langchain.com**](http://chat.langchain.com/?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b) 构建为原型，明确设计用于实现两大功能：

1.  **产品问答：** 帮助用户及内部团队快速获取权威的产品问题解答。
2.  **客户原型：** 作为生动范例，展示客户如何利用 LangChain 技术栈构建复杂可靠的智能体。

我们怀揣着坚定的目标，打造了一款功能完善的产品。但不得不承认：我们的技术支持工程师并未真正使用 LangChain 聊天机器人。这正是我们真正学习的起点。本文将讲述 **我们如何修复自有智能体** 的历程——以及我们在构建真正可靠、可供客户适配使用的生产级应用过程中获得的洞见。

我们团队并非因 Chat LangChain 存在缺陷或对其失去信心而停止使用。真正的原因在于，当有人提出 *"为什么生产环境中流式传输不工作？"* 这类问题时，仅依赖文档作为唯一资源显得捉襟见肘。众所周知，文档永远无法面面俱到。

于是他们建立了自己的工作流程：

- **第一步：** 查阅我们的文档（ [docs.langchain.com](http://docs.langchain.com/?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b) ）了解该功能的预期用途。
- **第二步：** 查阅我们的知识库（ [support.langchain.com](http://support.langchain.com/?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b) ），查看其他用户是否遇到相同问题及其解决方案。
- **第三步：** 打开 `Claude Code` ，搜索实际实现代码，验证代码的真实功能。

**官方文档承载着标准叙事。知识库直面现实难题。代码库揭示底层真相。**

* * *

## 我们决定将其自动化

这套三步流程效果出奇地好。我们每天目睹他们重复几十次后不禁思考： *要是直接把这条工作流自动化会怎样？*

于是我们构建了一个内部的 [`深度智能体`](https://docs.langchain.com/oss/python/deepagents/overview?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b) （用于构建能处理复杂多步骤任务的智能体库），它包含三个专业子智能体——分别负责文档处理、知识库检索和代码库搜索——每个子智能体在将洞察结果传递给主协调智能体之前，都会进行追问并筛选结果。

主智能体将综合所有信息，并给出如下答案：

> Example output:
> 
> *若要从子图中启用流式传输，请根据* [*LangGraph 流式传输文档*](https://docs.langchain.com/oss/python/langgraph/use-subgraphs?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b#stream-subgraph-outputs) *，在流配置中将 subgraphs 设置为 true。支持文章《\[升级后为何令牌流式传输失效\](*[*https://support.langchain.com/articles/7150806184-Why-is-token-by-token-streaming-not-working-after-upgrading-LangGraph?)\[?\](https://www.notion.so/263808527b1780db9f26fa75aed5e7e3?pvs=21)*](https://support.langchain.com/articles/7150806184-Why-is-token-by-token-streaming-not-working-after-upgrading-LangGraph?%29%5B%3F%5D%28https%3A%2F%2Fwww.notion.so%2F263808527b1780db9f26fa75aed5e7e3%3Fpvs=21%29&ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b) *》专门解释了此问题——您需要启用子图流式传输才能获取嵌套代理的令牌级更新。具体实现位于* [pregel/main.py 第 3373-3279 行，](https://github.com/langchain-ai/langgraph/blob/main/libs/langgraph/langgraph/pregel/main.py?ref=blog.langchain.com#L3273-L3279) *其中 subgraphs 标志控制嵌套图的输出是否包含在流中。*

我们的工程师对此赞不绝口。

这每周为他们节省了数小时复杂的调试时间。他们只需描述一个生产问题，就能得到详尽的解答，其中引用了文档、参考了已知解决方案，并指出了相关的具体代码行。

* * *

## 于是我们恍然大悟

这时有人提出了显而易见的问题： **既然这套方案对我们如此有效，为什么我们公开的 Chat LangChain 不采用这种方式呢？**

说得有道理。我们的公共工具将文档分割成片段，生成嵌入向量，存入向量数据库。随着文档更新，我们不得不频繁重建索引。用户虽然能获得答案，但引用来源需要完善，上下文也显得支离破碎。

我们无意中通过复制成功经验，在内部构建了更出色的方案。现在正是将这一方法应用于公开产品的时机。

在着手重构时，我们很快意识到需要融合两种由不同问题类型驱动的架构。大多数问题可以通过文档和知识库解决，而剩余问题则需要对代码基础进行分析。

* * *

## 我们如何构建新型智能体

### 为简易文档：创建代理

我们为 [chat.langchain.com](https://chat.langchain.com/?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b) 选择 [`createAgent`](https://docs.langchain.com/oss/javascript/releases/langchain-v1?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b#createagent) （ [`langchain`](https://docs.langchain.com/oss/javascript/langchain/overview?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b) 中的智能体抽象）作为默认模式，因为它最有利于 **速度** 。

没有规划阶段，没有编排开销——只有即时工具调用与答案生成。代理程序会搜索文档，必要时查阅知识库，若结果不明确则优化查询，最终返回答案。大多数文档问题通过 **3-6 次工具调用** 即可解决，而 Create Agent 能在数秒内完成这些操作。

**Model options:**

我们为终端用户提供了多种模型选择—— `Claude Haiku 4.5` 、 `GPT-4o Mini` 和 `GPT-4o-nano` ——通过实践发现 **Haiku 4.5 在工具调用方面具有惊人的速度优势** ，同时保持着出色的准确率。createAgent 与 Haiku 4.5 的组合能为大多数查询带来 **低于 15 秒的响应速度** ，这恰好符合文档问答场景的实时性需求。

**我们如何优化它：**

我们利用 [`LangSmith`](https://smith.langchain.com/?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b) 追踪每次对话，识别智能体在哪些环节进行了不必要的工具调用，并优化提示词。数据显示，如果我们教会智能体提出更精准的追问，大多数问题只需 3-6 次工具调用即可解决。LangSmith 的评估套件让我们能够对不同的提示策略进行 A/B 测试，同时衡量响应速度和准确率的提升效果。

![](https://blog.langchain.com/content/images/2025/11/langsmith-jewel.png)

这段 30 秒的追踪记录包含 7 次工具调用：4 次文档搜索、1 次知识库文章查询和 2 次文章阅读，其中 20 秒用于流式传输最终响应。 查看详情

### 使用代码回答：基于子图的深度智能体

除了利用文档、知识库和交叉参考已知问题作为资源外，许多问题还需要深入代码库以核实实现细节。

**The architecture:**

针对这些任务，我们构建了一个 `深度智能体` ，它配备了 **专用子图模块** ：一个用于 **文档检索** ，一个用于 **知识库搜索** ，另一个用于 **代码库查询** 。

每个子代理独立运作，在将信息传递给主协调代理之前，会自主提出后续问题、筛选信息并提取最关键的内容。这种机制既防止了主代理被海量上下文淹没，又确保了各领域专家能够进行必要深度的信息挖掘。

**代码库搜索优势：**

代码库搜索子代理功能尤为强大。它能够通过模式匹配搜索我们的私有代码库，浏览文件结构以理解上下文，并能精确到具体行号读取特定实现。

**The tradeoff:**

这种深度智能体架构运行时间较长——复杂查询有时需要 **1-3 分钟** ——但其全面性值得等待。当初始响应未能触及核心问题时，我们就会启动深度智能体。

免责声明：此模式在发布初期仅面向部分用户开放，预计将在数日内全面上线。

* * *

## 我们为何放弃向量嵌入

标准文档检索方法——将文档分块、生成嵌入向量、存入向量数据库、按相似度检索——对于 PDF 等非结构化内容效果尚可。但面对结构化产品文档时，我们始终面临三大难题。

**分块处理会破坏结构。** 当你将文档切分成 500 个词元的片段时，就会丢失标题、子章节和上下文信息。智能体可能会引用 `"set streaming=True"` 这样的代码片段，却不解释为何或何时使用。用户不得不翻遍整篇文档才能找到所需内容。

**频繁的索引重建。** 我们的文档每天更新多次。每次变更都意味着重新分块、重新嵌入和重新上传，这严重拖慢了我们的进度。

**引用模糊。** 用户无法核实答案或追溯信息来源。

突破在于意识到我们一直在解决错误的问题。文档已有其组织方式，知识库已有分类体系，代码库已有导航结构。我们需要的不是更智能的检索——而是让智能体直接接入这些现成的架构。

* * *

## 更优方案：直接 API 访问与智能提示

我们不再采用分块和嵌入的方式，而是让智能体直接访问原始资料。对于文档处理，我们使用 `Mintlify 的 API` ，它能返回 **完整的页面** ，包含所有标题、子章节和完整的代码示例。在知识库方面，我们首先通过标题检索支持文章，然后完整阅读最相关的内容。对于代码库搜索， **我们将代码库上传至 LangGraph 云端部署环境** ，并运用 `ripgrep` 进行模式匹配，通过目录遍历理解代码结构，再通过文件读取提取具体实现。

智能体并非基于相似度评分进行检索，而是 **像人类一样进行搜索** ——通过关键词、优化调整和后续追问来实现。

这里正是魔法发生的地方。我们不只是让智能体搜索一次就返回结果，而是引导它 **批判性思考** 现有信息是否足够。当搜索结果模糊或不完整时，智能体会优化查询再次搜索；当文档提及概念却未解释时，它会针对该概念专项检索；当存在多种解读可能时，智能体将锁定最相关的解释。

* * *

## 工具设计：为人工作流程而构建

我们设计的工具旨在反映人类真实的搜索方式，而非检索算法的运作原理。

文档搜索工具查询 `Mintlify's API` 并返回 **完整页面** 。当用户询问流式传输相关问题时，智能体获取的不是来自不同章节的三个割裂段落——而是获得完整的流式传输文档页面，其结构完全符合人类阅读习惯。

```python
@tool
def SearchDocsByLangChain(query: str, page_size: int = 5, language: Optional[str] = None) -> str:
 """Search LangChain documentation via Mintlify API"""
 params = {"query": query, "page_size": page_size}
 if language:
 params["language"] = language
 response = requests.get(MINTLIFY_API_URL, params=params)
 return _format_search_results(response.json())
```

但我们并不止步于此。我们会引导智能体评估初始结果是否真正回答了问题。 *这是正确的章节吗？是否有相关概念需要澄清？使用更具体的搜索词是否会更好？*

该代理拥有 **4-6 次工具调用** 的预算，我们鼓励其在回应前策略性地使用这些调用来完善理解。

**实际效果如下：**

用户问道： *"如何为我的智能体添加记忆功能？"*

代理搜索 `"memory"` 后得到的结果涵盖了检查点、对话历史记录和存储 API。它没有随机选择，而是意识到这个问题存在歧义——"memory"可能指在单次对话中保持会话状态，也可能指跨多个对话存储事实信息。

它再次使用 `"checkpointing"` 进行搜索以缩小线程级持久化范围，获取支持文章 *"如何在 LangGraph 中配置检查点？"* 并意识到该文章未涵盖跨线程内存。

于是它搜索 `"store API"` 来填补这个空白。

最终答案同时涵盖了对话历史的检查点机制和用于长期记忆的 Store API，并精确引用了所使用的支持文章和文档。

* * *

借助 Create Agent，这种迭代搜索过程能在几秒内完成，但它从根本上改变了回答的质量。智能体不仅仅是检索——它还在推理用户的真实需求。

我们之所以将知识库（由 Pylon 驱动）搜索设计为 **两步流程** ，是因为这符合人类使用知识库的自然习惯。

首先，智能体会检索文章标题——有时多达数十篇——并快速浏览以识别哪些标题具有相关性。随后，它仅会完整阅读那些被判定相关的文章。

```python
@tool
def search_support_articles(collections: str = "all", limit: int = 50) -> str:
 """Step 1: Get article titles to scan"""
 articles = pylon_client.list_articles(collections=collections, limit=limit)
 return json.dumps([{
 "id": a["id"],
 "title": a["title"],
 "url": a["url"]
 } for a in articles])

@tool
def get_article_content(article_ids: List[str]) -> str:
 """Step 2: Read the most relevant articles"""
 articles = pylon_client.get_articles(article_ids)
 return "\\n\\n---\\n\\n".join([
 f"# {a['title']}\\n\\n{a['content']}\\n\\nSource: {a['url']}"
 for a in articles
 ])
```

**Why this works:**

这避免了智能体被信息淹没。它不再将30篇完整文章塞进上下文窗口，而是筛选出真正重要的2-3篇进行精读，并提炼出核心见解。

提示语进一步强调： *注重质量而非数量，必要时缩小搜索范围，只返回直接回答问题的信息。*

* * *

这正是我们 `深度智能体` 大放异彩之处。

我们为智能体配备了三种工具，这些工具复现了开篇描述的工作流程——这正是我们工程师使用 `Claude Code` 时遵循的相同模式

```python
@tool
def search_public_code(pattern: str, path: Optional[str] = None) -> str:
 """Step 1: Find code matching a pattern"""
 cmd = ["rg", pattern, str(path or search_path)]
 return subprocess.run(cmd, capture_output=True, text=True).stdout

@tool
def list_public_directory(path: str, max_depth: int = 2) -> str:
 """Step 2: Understand the file structure"""
 cmd = ["tree", "-L", str(max_depth), str(path)]
 return subprocess.run(cmd, capture_output=True, text=True).stdout

@tool
def read_public_file(file_path: str, start_line: int = 1, num_lines: int = 100) -> str:
 """Step 3: Read the actual implementation"""
 with open(file_path, "r") as f:
 lines = f.readlines()
 return "\\n".join(lines[start_line-1:start_line-1+num_lines])
```

**How it works:**

首先，它使用 `ripgrep` 在代码库中搜索特定模式。接着列出目录结构以理解文件组织方式。最后读取具体文件，聚焦相关代码段，并返回带行号的实现代码。

**Real-world example:**

用户报告生产环境中流式令牌传输出现卡顿。文档子代理发现流式配置涉及缓冲区设置，知识库子代理则调出一篇关于升级后令牌流传输问题的支持文章。

但代码库子代理才是找到实际实现的那个——它搜索 `"streaming buffer"` ，导航到 `callbacks/streaming.py` ，并返回 **第 47-83 行** ，其中默认缓冲区大小是硬编码的。

这正是那种能解决实际问题的深度探究。

**区别何在？** `深度智能体` 能够并行处理所有三个领域的任务，并将阶段性发现整合成一个连贯的答案。

* * *

## Deep Agent 与子图如何解决上下文过载问题

当初我们将深度智能体设计成一个能同时调用三种工具的单体系统时，它会返回所有查询结果。主智能体常常一次性收到五份文档页、十二篇知识库文章和二十段代码片段。

上下文窗口会爆炸式增长，最终响应要么充斥着无关细节，要么完全遗漏关键见解。

于是我们采用专门的子图对其进行了重构。

**How it works:**

每个子代理独立运作。它在自己的领域内进行搜索，提出后续问题以澄清模糊之处，筛选结果，并仅提取 **黄金数据** ——即回答问题所需的关键事实、引用和背景信息。

主协调智能体从不查看原始搜索结果，它只接收来自各领域专家的精炼见解。完整追踪记录及提示词可\*\* [在此查看](https://smith.langchain.com/public/c1059a52-d045-4013-a17f-3bdc07ef3f0d/r/67669d45-0065-47de-b0ee-0b4ca2687060?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b) \*\*。

**Why this matters:**

文档子代理可能阅读了整整五页内容，但仅返回两个关键段落。知识库子代理或许扫描了二十篇文章标题，却只提炼出三篇相关摘要。代码库子代理即使搜索了五十个文件，最终也仅提供带行号的具体实现代码。

主代理接收经过筛选的纯净信息，能够将其整合成全面的答案。

* * *

## 实现生产就绪

即便再优雅的智能体设计，也需要生产级基础设施来应对真实用户的考验。我们构建了模块化 [中间件](https://docs.langchain.com/oss/javascript/langchain/middleware?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b#middleware) 来处理运维问题，从而避免提示词被琐碎事务污染。

```python
middleware = [
 guardrails_middleware, # Filter off-topic queries
 model_retry_middleware, # Retry on API failures
 model_fallback_middleware,  # Switch models if needed
 anthropic_cache_middleware  # Cache expensive calls
]
```

**各层功能说明：**

**防护栏** 会过滤掉无关查询，确保智能体始终专注于 LangChain 相关问题。

**重试中间件** 能优雅处理临时性 API 故障，让用户永远看不到晦涩的错误提示。

**备用中间件** 可在模型不可用时，在 Haiku、GPT-4o Mini 和 Gemini Nano 之间进行切换。

**缓存** 通过复用相同查询的结果来降低成本。

这些层次对用户不可见，但对可靠性至关重要。它们让智能体专注于推理，而基础设施则负责处理故障模式、成本优化和质量控制。

* * *

## 让智能体触达用户

打造出色的智能体只是成功的一半。另一半？是让它以既迅捷又智能的方式触达用户。

我们使用 **LangGraph SDK** 来处理所有流式处理和状态管理的复杂性。

当用户打开 Chat LangChain 时，我们通过 LangGraph SDK 获取其对话历史记录：

```tsx
const userThreads = await client.threads.search({
  metadata: { user_id: userId },
  limit: THREAD_FETCH_LIMIT,
})
```

每个线程都会将用户 ID 存储在元数据中，确保对话在不同会话间保持私密性和持久性。LangGraph SDK 会自动处理筛选逻辑。

### 实时流式响应：

当用户发送消息时，LangGraph SDK 会在生成过程中实时流式传输响应：

typescript

```tsx
const streamResponse = client.runs.stream(threadId, "docs_agent", {
  input: { messages: [{ role: "user", content: userMessage }] },
  streamMode: ["values", "updates", "messages"],
  streamSubgraphs: true,
})

for await (const chunk of streamResponse) {
  if (chunk.event === "messages/partial") {
 setMessages(prev => updateWithPartialContent(chunk.data.content))
  }
}
```

**What users see:**

三种流模式展示智能体的完整思考过程：

- **`messages`** — 智能体书写时，令牌会逐次显现
- **`updates`** — 工具调用揭示智能体正在搜索的内容
- **`values`** — 处理完成后的最终完整状态

用户能实时观察智能体思考、检索文档、查阅知识库，并逐字逐句构建响应过程——全程无需加载动画。

### Conversation Memory

在消息间传递相同的 `thread_id` ，LangGraph 的检查点机制便会自动处理后续流程。它会存储对话历史记录、为每个回合检索上下文，并保持跨会话的状态持久化。我们设置了 7 天的存活时间，仅此而已。

* * *

## The Results

自新系统上线以来，我们见证了显著的改进。

在公开版 Chat LangChain 中，用户可获得 **15 秒内的响应速度** 及精准溯源。由于答案直接关联至相关文档页面或知识库文章，用户能即时验证信息。我们也不再需要耗费数小时重建索引——文档现已实现自动更新。

在内部，我们的技术支持工程师使用 `深度代理` 来处理最复杂的工单。它能搜索文档、交叉引用已知问题，并深入我们的私有代码库，找到真正解释问题根源的实现细节。 **这个代理并非取代工程师——而是赋能他们** ，通过处理调研工作让工程师能专注于解决问题本身。

* * *

## Key Takeaways

- **遵循用户工作流程：** 无需重复造轮子，将优秀用户（或内部专家）已验证成功的工作流程自动化。对 LangChain 而言，这意味着复现检查 **文档、** **知识库** 和 **代码库** 的三步式标准流程。
- **评估向量嵌入是否适用：** 对于产品文档和代码这类结构化内容，使用向量嵌入可能会破坏文档结构，导致引用模糊，并需要持续重新索引。向量嵌入在处理非结构化内容、较短文本块或聚类应用场景时表现卓越。
- **赋予智能体直接访问结构的能力：** 这种方法让智能体能够通过 API 直接访问内容的现有结构。这使得智能体可以像人类一样，通过关键词和细化调整进行搜索。
- **优先推理而非检索：** 设计工具时应模拟人类工作流程：先浏览文章标题再阅读内容，代码处理采用模式匹配和目录导航。当初始结果模糊时，应引导智能体提出追问并优化查询，确保最终答案能覆盖用户的真实需求。
- **利用深度智能体与子图管理上下文：** 面对复杂的跨领域问题时，采用配备专用 **子图** 的 **深度智能体** 可避免主协调智能体被原始搜索结果淹没。每个子智能体会先从其专业领域筛选并提取"黄金数据"，再将精炼后的核心洞察向上传递。
- **生产级中间件的必要性：** 即使是最优雅的智能体设计也需要稳健的基础设施来保证可靠性。为实现生产级可靠性、成本优化和质量控制，实施模块化中间件来支持 **防护机制** （过滤无关查询）、 **重试机制** （应对 API 故障）、 **降级方案** （切换模型）以及 **缓存策略** 至关重要。

* * *

## What's Next

**公共代码库搜索** （未来几天内上线）——当文档和知识库信息不足时，智能体将搜索我们的公共代码库以验证实现方案，并引用精确的行号

* * *

## Try It Yourself

Chat LangChain 已上线 [chat.langchain.com](https://chat.langchain.com/?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b) 。使用 `Claude Haiku 4.5` 可获得最快响应速度，或尝试 `GPT-5 Mini` 与 `GPT-5 Nano` 来体验不同模型的表现差异。

* * *

## 加入对话

构建兼顾速度与深度的智能体充满挑战，我们仍在探索中。如果您正致力于解决类似问题，我们非常期待了解您的发现。

加入 LangChain 社区，参与我们的 [论坛](https://forum.langchain.com/?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b) 讨论，或在 [Twitter](https://twitter.com/LangChainAI?ref=blog.langchain.com) 上关注我们。

订阅我们的新闻通讯，获取团队和社区的最新动态。