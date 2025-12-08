---
title: "Why We Rebuilt LangChain’s Chatbot and What We Learned"
source: "https://blog.langchain.com/rebuilding-chat-langchain/"
author:
  - "[[LangChain]]"
published: 2025-11-06
created: 2025-11-06
description: "By Liam BushBackgroundEvery successful platform needs reliable support, but we realized our own team was spending hours tracking down answers to technical questions. This friction wasn't just slowing down our engineers—it was a critical bottleneck for our users.We set out to solve this using the very"
tags:
  - "LangChain"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-11-13"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---
*By Liam Bush*

## Background

每个成功的平台都需要可靠的支持，但我们发现自己的团队花费大量时间追查技术问题的答案。这种阻力不仅拖慢了工程师的效率，更成为了用户面临的关键 **瓶颈** 。

我们决定利用我们所倡导的工具来解决这个问题： **LangChain、LangGraph** 和 **LangSmith** 。最初，我们构建了 [**chat.langchain.com**](http://chat.langchain.com/?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b) 作为原型，明确设计用于实现两大功能：

1. **产品问答：** 帮助用户及我们团队快速获取产品相关问题的权威解答。
2. **客户原型：** 作为生动实例，展示客户如何利用 LangChain 技术栈构建复杂且可靠的智能体。

我们怀揣着坚定的目标，打造了一款功能完备的产品。但不得不承认：我们的技术支持工程师并未真正使用 LangChain 聊天机器人。而这，正是我们真正学习的起点。本文将讲述 **我们如何修复自身智能体** 的故事——以及我们在构建客户能够适配使用的、真正可靠的生产级应用过程中获得的经验教训。

我们团队并非因 Chat LangChain 存在故障或对其缺乏信心而未积极使用。实则当有人提出 *“为什么在生产环境中流式传输不工作？”* 时，他们需要的不仅是仅依赖文档作为唯一资源——毕竟文档永远不够详尽。

于是他们构建了自己的工作流程：

- **第一步：** 查阅我们的文档（ [docs.langchain.com](http://docs.langchain.com/?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b) ），了解该功能的设计用途。
- **第二步：** 查阅我们的知识库（ [support.langchain.com](http://support.langchain.com/?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b) ），查看其他用户是否遇到相同问题及其解决方案。
- **第三步：** 打开 `Claude Code` ，搜索实际实现代码，并验证代码的实际功能。

**官方故事的文档库。现实问题的知识库。基础事实的代码库。**

---

## 我们决定将其自动化

这个三步流程效果出奇地好。我们每天看着他们重复几十次，不禁想到： *要是能把这个流程自动化该多好？*

因此，我们构建了一个内部的 [`Deep Agent`](https://docs.langchain.com/oss/python/deepagents/overview?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b) （用于构建能处理复杂多步骤任务的智能代理库），它包含三个专业子代理——分别负责文档、知识库和代码库搜索。每个子代理在将洞察结果传递给主协调代理之前，都会进行追问并筛选结果。

主代理会综合所有信息，并像这样给出答案：

> Example output:  
>   
> *若要从子图进行流式传输，请根据* [*LangGraph 流式传输文档*](https://docs.langchain.com/oss/python/langgraph/use-subgraphs?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b#stream-subgraph-outputs) *，在流配置中设置 subgraphs: true。支持文章《* [*升级后令牌流式传输为何失效*](https://support.langchain.com/articles/7150806184-Why-is-token-by-token-streaming-not-working-after-upgrading-LangGraph?%29%5B%3F%5D%28https%3A%2F%2Fwww.notion.so%2F263808527b1780db9f26fa75aed5e7e3%3Fpvs=21%29&ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b) *》详细解释了此问题——您需要启用子图流式功能才能获取嵌套代理的令牌级更新。该实现位于* [pregel/main.py 第 3373-3279 行](https://github.com/langchain-ai/langgraph/blob/main/libs/langgraph/langgraph/pregel/main.py?ref=blog.langchain.com#L3273-L3279) *，其中 subgraphs 标志控制嵌套图的输出是否包含在流中。*

我们的工程师们对此赞不绝口。

这每周为他们节省了数小时处理复杂调试的时间。他们只需描述生产环境中的问题，就能得到详尽的解答，其中引用了相关文档、已知解决方案，并精准指出了关键代码行。

---

## 于是我们恍然大悟

接着有人提出了一个显而易见的问题： **既然这对我们如此有效，为何我们公开的 Chat LangChain 不采用这种方式运作呢？**

说得有道理。我们的公共工具确实将文档分割成片段，生成嵌入向量，再存入向量数据库。随着文档不断更新，我们不得不频繁重建索引。用户虽然能获得答案，但引用部分有待完善，上下文也显得支离破碎。

我们无意中通过复制成功经验，在内部构建出了更优的方案。现在正是将这一方法应用于公开产品的时候。

在着手重构时，我们很快意识到需要融合两种由不同问题类型驱动的架构。大多数问题可通过文档和知识库解决，其余问题则需对代码基础进行分析。

---

## 我们如何构建新代理

### 对于简单文档：创建代理

我们选择将 [`createAgent`](https://docs.langchain.com/oss/javascript/releases/langchain-v1?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b#createagent) （ [`langchain`](https://docs.langchain.com/oss/javascript/langchain/overview?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b) 中的智能体抽象）作为 [chat.langchain.com](https://chat.langchain.com/?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b) 的默认模式，因为它最有利于实现 **高速响应** 。

没有规划阶段，没有编排开销——只有即时工具调用与答案生成。代理程序会搜索文档，必要时查阅知识库，若结果不明确则优化查询，最终返回答案。大多数文档问题通过 **3-6 次工具调用** 即可解决，而 Create Agent 能在数秒内完成这些操作。

**Model options:**

我们为终端用户提供了多种模型选择—— `Claude Haiku 4.5` 、 `GPT-4o Mini` 和 `GPT-4o-nano` ——并发现 **Haiku 4.5 在工具调用方面速度极快** ，同时保持高准确度。createAgent 与 Haiku 4.5 的组合能为大多数查询带来 **低于 15 秒的响应时间** ，这正符合文档问答场景的需求。

**我们是如何优化的：**

我们利用 [`LangSmith`](https://smith.langchain.com/?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b) 追踪每次对话，识别智能体在哪些环节进行了不必要的工具调用，并据此优化提示设计。数据显示，若能指导智能体提出更精准的后续问题，大多数查询只需 3-6 次工具调用即可解决。通过 LangSmith 的评估套件，我们得以对多种提示策略进行 A/B 测试，并量化评估响应速度与准确性的提升效果。

![](https://blog.langchain.com/content/images/size/w600/2025/11/langsmith-jewel.png)

这段 30 秒的追踪记录包含 7 次工具调用：4 次文档搜索、1 次知识库文章查询和 2 次文章阅读，其中 20 秒用于流式传输最终响应。 查看详情

### 对于使用代码进行回答：采用子图的深度代理

除了利用文档、知识库和交叉参考已知问题作为资源外，许多问题还需要深入我们的代码库以核实实现细节。

**The architecture:**

针对这些任务，我们构建了一个 `深度代理 ` ，它配备了 **专用子图** ：一个用于 **文档搜索** ，一个用于 **知识库搜索** ，还有一个用于 **代码库搜索** 。

每个子代理独立运作，提出后续问题、筛选信息，并仅提取最相关的见解后传递给主协调代理。这样既避免了主代理淹没在信息中，又让各领域专家能够根据需要深入挖掘。

**代码库搜索优势：**

代码库搜索子代理功能尤为强大。它能通过模式匹配搜索我们的私有代码库，浏览文件结构以理解上下文，并能精确到具体行号读取特定实现。

**The tradeoff:**

这种深度代理架构的运行时间较长——对于复杂查询有时需要 **1-3 分钟** ——但其全面性值得等待。当初始响应未能触及核心问题时，我们便会启用 DeepAgent。

免责声明：此模式在发布初期仅面向部分用户开放，预计将在数日内全面上线。

---

## 我们为何放弃向量嵌入技术

标准文档搜索方法——将文档分块、生成嵌入向量、存入向量数据库、通过相似度检索——对于 PDF 等非结构化内容效果尚可。但面对结构化产品文档时，我们始终面临三大难题。

**分块处理会破坏结构。** 当你将文档切割成 500 个标记的片段时，会丢失标题、子章节和上下文信息。智能体可能会引用 `"set streaming=True"` 却不解释原因或适用场景，导致用户不得不翻遍文档才能找到所需内容。

**频繁的重新索引。** 我们的文档每日更新多次。每次变更都意味着需要重新分块、重新嵌入和重新上传，这大大拖慢了我们的进度。

**引用模糊。** 用户无法验证答案或追溯信息来源。

突破在于我们意识到自己一直在解决错误的问题。文档已有其组织结构，知识库已有分类体系，代码库已具备可导航性。我们需要的不是更智能的检索——而是要让智能体直接接入这些现成的架构。

---

## 更佳方案：直接 API 访问与智能提示

我们不再采用分块和嵌入的方式，而是让智能体直接访问原始内容。对于文档处理，我们使用 `Mintlify 的 API` ，它能返回 **完整的页面** ，包含所有标题、子章节和完整的代码示例。对于知识库检索，我们首先通过标题查询支持文章，然后完整阅读最相关的条目。在代码库搜索方面， **我们将代码库上传至 LangGraph 云端部署环境** ，并运用 `ripgrep` 进行模式匹配、目录遍历以理解结构，以及文件读取来提取具体实现。

该代理并非基于相似度评分进行检索，它 **像人类一样进行搜索** ——通过关键词、细化调整和后续提问来完成。

这里正是神奇之处。我们并非简单地让智能体搜索一次就返回结果，而是引导它 **批判性思考** 已有信息是否充足。当结果存在歧义或不完整时，智能体会优化查询再次搜索；若文档提及未解释的概念，它会针对该概念专项检索；遇到多重解读可能时，则自动聚焦到最相关的解释。

---

## 工具设计：围绕人类工作流程构建

我们设计工具时，旨在反映人类真实的搜索方式，而非检索算法的运作原理。

文档搜索工具查询 `Mintlify 的 API` 并返回 **完整页面** 。当用户询问流媒体相关问题时，智能体获取的不是来自不同章节的三个零散段落——而是获得完整的流媒体文档页面，其结构完全符合人类阅读习惯。

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

但我们并未止步于此。我们会引导智能体评估初始结果是否真正解答了疑问。 *这是正确的部分吗？是否有相关概念需要澄清？使用更具体的搜索词是否会更好？*

该代理拥有 **4 到 6 次工具调用** 的预算，我们鼓励其在回应前策略性地使用这些调用来完善理解。

**实践中是这样的：**

一位用户问道： *“如何为我的智能体添加记忆功能？”*

代理在搜索 `"memory"` 时，获得了涵盖检查点、对话历史记录和存储 API 的结果。它并未随机选择，而是意识到问题存在歧义——"memory"可能指在单次对话中保持会话状态，也可能意味着跨多个对话存储事实信息。

它再次使用 `"checkpointing"` 进行搜索以缩小线程级持久化的范围，获取了支持文章 *"如何在 LangGraph 中配置检查点？"* ，并意识到该文章未涵盖跨线程内存的内容。

因此，它搜索 `“store API”` 来填补这一空白。

最终答案涵盖了对话历史的检查点设置和用于长期记忆的存储 API，并精确引用了所使用的支持文章和文档。

---

使用 Create Agent，这种迭代搜索过程在几秒钟内完成，但它从根本上改变了回答的质量。该代理不仅是在检索——它还在推理用户真正需要什么。

我们之所以将知识库（由 Pylon 驱动）搜索设计为 **两步流程** ，是因为这符合人类使用知识库的习惯。

首先，智能体检索文章标题——有时多达数十个——并通过扫描筛选出看似相关的文章，随后仅深入阅读这些选定的文章。

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

这避免了智能体被信息淹没。它不会将30篇完整文章全部传入上下文窗口，而是筛选出真正重要的2-3篇进行精读，并提取关键见解。

提示语进一步强调： *注重质量而非数量，必要时缩小搜索范围，仅返回直接回答问题的信息。*

---

这里正是我们的 `Deep Agent` 大放异彩之处。

我们为智能体配备了三种工具，这些工具复现了开篇所述的工作流程——这正是我们的工程师使用 `Claude Code` 时遵循的相同模式

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

首先，它使用 `ripgrep` 在代码库中搜索特定模式。接着，它会列出目录结构以理解文件组织方式。最后，它会读取具体文件，重点关注相关部分，并附带行号返回实现内容。

**Real-world example:**

用户报告在生产环境中流式传输令牌出现卡顿。文档子代理发现流式配置涉及缓冲区设置。知识库子代理调出一篇关于升级后令牌流传输问题的支持文章。

但代码库子代理才是找到实际实现的那个——它搜索 `"streaming buffer"` ，导航到 `callbacks/streaming.py` 文件，并返回 **第 47 至 83 行** ，其中默认缓冲区大小是硬编码的。

这正是那种能解决实际问题的深度探究。

**区别何在？** ` 深度代理` 能够并行处理所有三个领域的工作，并将阶段性发现汇总成一个连贯的答案。

---

## 深度代理与子图如何解决上下文过载问题

当我们最初将深度代理构建为一个能同时访问三种工具的单一系统时，它会返回所有发现的内容。主代理会一次性获得五份文档页面、十二篇知识库文章和二十个代码片段。

上下文窗口会急剧膨胀，而最终响应要么充斥着无关细节，要么完全遗漏关键见解。

就在那时，我们利用专门的子图对其进行了重构。

**How it works:**

每个子代理独立运作。它在自己的领域内搜索，提出后续问题以澄清模糊之处，筛选结果，并仅提取 **黄金数据** ：即回答问题所需的关键事实、引用和背景信息。

主协调代理从不查看原始搜索结果，它只接收来自各领域专家的精炼见解。查看完整追踪记录及提示请\*\* [点击此处](https://smith.langchain.com/public/c1059a52-d045-4013-a17f-3bdc07ef3f0d/r/67669d45-0065-47de-b0ee-0b4ca2687060?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b) \*\*。

**Why this matters:**

文档子代理可能阅读了整整五页内容，却仅返回两个关键段落；知识库子代理或许扫描了二十篇文章标题，最终只提供三篇相关摘要；而代码库子代理即便搜索了五十个文件，也仅会返回带有行号的具体实现代码。

主代理获取到经过筛选的清晰信息，能够将其综合成全面的答案。

---

## 使其具备生产就绪性

即便是优雅的智能体设计，也需要生产级基础设施来应对真实用户的考验。我们构建了模块化 [中间件](https://docs.langchain.com/oss/javascript/langchain/middleware?ref=blog.langchain.com&ajs_aid=52fc5c7a-ee15-4113-91a9-edd21e24400b#middleware) 来处理运维问题，从而避免这些琐碎事务干扰核心提示词设计。

```python
middleware = [
    guardrails_middleware,      # Filter off-topic queries
    model_retry_middleware,     # Retry on API failures
    model_fallback_middleware,  # Switch models if needed
    anthropic_cache_middleware  # Cache expensive calls
]
```

**每一层的作用：**

**防护栏** 能过滤掉离题查询，确保智能体专注于 LangChain 相关问题。

**重试中间件** 能优雅处理临时性 API 故障，让用户永远看不到晦涩的错误信息。

**回退中间件** 在模型不可用时，会在 Haiku、GPT-4o Mini 和 Gemini Nano 之间进行切换。

**缓存** 通过重用相同查询的结果来降低成本。

这些层次对用户不可见，但对于确保可靠性至关重要。它们让智能体专注于推理，而基础设施则处理故障模式、成本优化和质量控制。

---

## 让智能体触达用户

打造出色的智能体仅是成功的一半。另一半呢？是以既迅捷又智能的方式将其呈现给用户。

我们使用 **LangGraph SDK** 来处理所有流式处理和状态管理的复杂性。

当有人打开 Chat LangChain 时，我们使用 LangGraph SDK 获取他们的对话历史：

```tsx
const userThreads = await client.threads.search({
  metadata: { user_id: userId },
  limit: THREAD_FETCH_LIMIT,
})
```

每个线程都会在元数据中存储用户 ID，确保对话在会话间保持私密性和持久性。LangGraph SDK 会自动处理筛选工作。

### 实时流式响应：

当用户发送消息时，LangGraph SDK 会在生成过程中实时流式传输响应

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

三种流模式展示代理的完整思考过程：

- **`messages`** — 随着代理程序的写入，令牌会逐步显示
- **`更新 `** — 工具调用揭示了智能体正在搜索的内容
- **`values`** — 处理完成后的最终完整状态

用户能实时观察智能体思考、搜索文档、查阅知识库，并逐词构建响应的全过程。全程无需加载动画。

### Conversation Memory

在消息间传递相同的 `thread_id` ，LangGraph 的检查点机制便会自动处理后续流程。它会存储对话历史记录、为每轮对话检索上下文，并保持跨会话的状态持久化。我们设置了 7 天的存活时间，仅此而已。

---

## The Results

自新系统上线以来，我们见证了显著的改进。

对于公开的 Chat LangChain，用户可获得 **15 秒以内的响应速度** 及精准引用。由于我们直接链接至相关文档页面或知识库文章，他们能即时验证答案。此外，我们不再需要花费数小时重新索引——文档已实现自动更新。

在内部，我们的技术支持工程师运用 `Deep Agent` 处理最复杂的工单。它能搜索文档、交叉引用已知问题，并深入我们的私有代码库，找出真正解释问题根源的实现细节。 **该智能体并非取代工程师，而是增强他们的能力** ——由它负责调研工作，让工程师能专注于解决问题本身。

---

## Key Takeaways

- **遵循用户工作流程：** 无需重复造轮子，将优秀用户（或内部专家）已验证的高效工作流程自动化。对 LangChain 而言，这意味着复现查阅 **文档、** **知识库** 与 **代码库** 的三步式操作惯例。
- **评估向量嵌入是否适用：** 对于产品文档和代码这类结构化内容，使用向量嵌入可能会破坏文档结构，导致引用模糊，并需要频繁重新索引。向量嵌入在处理非结构化内容、较短文本块或聚类应用场景时表现卓越。
- **赋予代理直接访问结构的权限：** 这种方法使代理能够直接通过 API 访问内容的现有结构，从而让代理能够像人类一样使用关键词和细化条件进行搜索。
- **优先推理而非检索：** 设计工具时应模拟人类工作流程：先浏览文章标题再阅读内容，代码处理采用模式匹配与目录导航。当初步结果不明确时，应引导智能体提出追问并优化查询，确保最终答案能覆盖用户的真实需求。
- **运用深度代理与子图管理上下文：** 面对复杂的跨领域问题，采用具备专业 **子图** 的 **深度代理** 可避免主协调代理被原始搜索结果淹没。每个子代理会先在其领域内筛选并提取仅有的“黄金数据”，再将精炼后的洞察结果向上传递。
- **生产级中间件的必要性：** 即便是优雅的智能体设计也需要健壮的基础设施来保证可靠性。为实现生产级可靠性、成本优化和质量控制，实施模块化中间件来处理 **防护机制** （过滤无关查询）、 **重试机制** （应对 API 故障）、 **降级方案** （切换模型）以及 **缓存策略** 至关重要。

---