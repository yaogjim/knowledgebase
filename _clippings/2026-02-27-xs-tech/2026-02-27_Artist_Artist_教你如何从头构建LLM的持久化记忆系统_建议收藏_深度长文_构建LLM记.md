---
title: "2026-02-27_Artist_Artist_教你如何从头构建LLM的持久化记忆系统_建议收藏_深度长文_构建LLM记"
source: "https://x.com/ArtistZhou/status/2026976235365028213"
author:
  - "[[@Artist]]"
published: 2026-02-27
created: 2026-02-27
description:
tags:
  - "#LLM"
  - "#AIArchitecture"
  - "x"
  - "@Artist"
---

# Artist # 教你如何从头构建LLM的持久化记忆系统【建议收藏】 深度长文：构建LLM记

**Artist**

# 教你如何从头构建LLM的持久化记忆系统【建议收藏】

# 

深度长文：构建LLM记忆系统技术指南

🧠 如何从零构建企业级 LLM 记忆系统？

一条深度技术推文串，详解 Mem0 架构的工程实现与上下文工程的本质挑战 👇

（基于 Towards Data Science 深度技术文章，作者：Avishek Biswas）

[https://towardsdatascience.com/how-to-build-your-own-custom-llm-memory-layer-from-scratch/](https://towardsdatascience.com/how-to-build-your-own-custom-llm-memory-layer-from-scratch/)

1/ 🎯 核心问题：为什么 LLM 需要记忆层？

LLM 的“无状态”特性是双刃剑： • 优势：并行处理能力强、安全性高（请求间无信息泄漏） • 劣势：每次请求都是冷启动，无法保持跨会话的上下文连续性

这导致了一个根本性问题：如果用户今天说“我喜欢茶”，明天再次对话时，模型已经“忘记”了这个信息。

真正的个性化 AI 助手必须突破这一限制。

[#LLM](https://x.com/search?q=%23LLM&src=hashtag_click)

[#AIArchitecture](https://x.com/search?q=%23AIArchitecture&src=hashtag_click)

[#ContextEngineering](https://x.com/search?q=%23ContextEngineering&src=hashtag_click)

[

![Image](https://pbs.twimg.com/media/HCFDWQHbkAAMrB7?format=jpg&name=medium)


](/ArtistZhou/article/2026976235365028213/media/2026975356855750656)

2/ 💡 核心洞察：记忆是上下文工程的最高形

构建记忆系统不是简单的“存储历史记录”，而是需要解决 6 个关键技术挑战：

1.  结构化信息提取：从非结构化对话流中提取原子化事实
 
2.  智能摘要：避免上下文窗口爆炸
 
3.  向量检索：语义相似度匹配而非关键词匹配
 
4.  查询生成与后处理：理解用户真实意图
 
5.  重排序：从候选记忆中筛选最相关的信息
 
6.  智能体工具调用：动态决策何时检索、如何更新
 

这就是为什么记忆系统被称为“最难也最有趣的上下文工程问题”。

[#MachineLearning](https://x.com/search?q=%23MachineLearning&src=hashtag_click)

[#SystemDesign](https://x.com/search?q=%23SystemDesign&src=hashtag_click)

3/ 🏗️ 系统架构的四个核心组件

Mem0 架构将记忆系统解耦为独立模块：

提取层（Extraction） 使用 DSPy Signature 将对话转录文本转换为原子化事实列表。关键：每个事实必须是独立、自包含的，不能依赖外部上下文。

嵌入层（Embedding） 采用 OpenAI text-embedding-3-small，固定 64 维向量。为什么是 64 维？在短文本（记忆通常是短句）场景下，过高维度会引入噪声，64 维在存储效率与语义表达间取得平衡。

存储层（Vector DB） QDrant 提供混合过滤能力：向量相似度搜索 + SQL-like 属性过滤（user\_id、时间戳、类别标签）。

维护层（Maintenance） ReAct 智能体循环决定 ADD/UPDATE/DELETE/NOOP 操作。

[

![Image](https://pbs.twimg.com/media/HCFDcaBa0AADKGY?format=jpg&name=medium)


](/ArtistZhou/article/2026976235365028213/media/2026975462594105344)

4/ 🔧 Step 1：记忆提取的工程实现

使用 DSPy 定义提取任务的核心代码：

class MemoryExtract(dspy.Signature): """ Extract relevant information from the conversation. Memories are atomic independent factoids that we must learn about the user. If transcript does not contain any information worth extracting, return empty list. """ transcript: str = dspy.InputField() memories: list\[str\] = dspy.OutputField() memory\_extractor = dspy.Predict(MemoryExtract) ​

关键设计决策： • 使用 docstring 作为系统提示，零样板代码 • 输出为字符串列表而非结构化对象，保持灵活性 • 显式处理“无信息可提取”情况，避免幻觉

示例：输入“我喜欢咖啡…… 其实，不，我更喜欢茶。我也喜欢足球” 输出：\[“用户曾经喜欢茶但现在不喜欢了”, “用户喜欢咖啡”, “用户喜欢足球”\]

注意：系统正确识别了“曾经喜欢但现在不喜欢”的时态变化。

[#DSPy](https://x.com/search?q=%23DSPy&src=hashtag_click)

[#PromptEngineering](https://x.com/search?q=%23PromptEngineering&src=hashtag_click)

5/ 💾 Step 2：向量化的工程细节

为什么选择 64 维？

短文本嵌入存在一个有趣的现象：过高维度（如 1536 维的 ada-002）对于“用户喜欢咖啡”这样的短句是过度表达。text-embedding-3-small 支持通过 dimensions 参数压缩，64 维在实验中表现出： • 存储成本降低 24 倍 • 检索速度提升 3-5 倍 • 准确率损失 < 2%

嵌入代码：

async def generate\_embeddings(strings: list\[str\]): out = await client.embeddings.create( input=strings, model="text-embedding-3-small", dimensions=64 # 关键参数 ) return \[item.embedding for item in

[out.data](//out.data)

\] ​

QDrant 集合配置：

await client.create\_collection( collection\_name="memories", vectors\_config=VectorParams( size=64, distance=

[Distance.DOT](//Distance.DOT)

\# 点积距离适合归一化嵌入 ), ) # 关键：为用户隔离创建 payload 索引 await client.create\_payload\_index( collection\_name="memories", field\_name="user\_id", field\_schema=models.PayloadSchemaType.INTEGER ) ​

[#VectorDB](https://x.com/search?q=%23VectorDB&src=hashtag_click)

[#Embeddings](https://x.com/search?q=%23Embeddings&src=hashtag_click)

[

![Image](https://pbs.twimg.com/media/HCFDixBbEAAwSmT?format=jpg&name=medium)


](/ArtistZhou/article/2026976235365028213/media/2026975571847352320)

6/ 🔍 Step 3：智能检索的“可选性”设计哲

传统 RAG 系统的通病：每次查询都盲目检索，导致： • 延迟增加 100-500ms • 引入无关信息干扰模型判断 • 计算资源浪费

Mem0 的关键创新：检索应该是“按需”的。

实现机制：

class ResponseGenerator(dspy.Signature): """ You have the option to look up past memories from a vector database to fetch relevant context if required. If you can't find the answer from transcript or internal knowledge, use the provided search tool calls. """ transcript: list\[dict\] = dspy.InputField() question: str = dspy.InputField() response: str = dspy.OutputField() save\_memory: bool = dspy.OutputField( description="True if new memory needs to be created" ) ​

工具定义让 LLM 自主决策：

async def fetch\_similar\_memories(search\_text: str): """ Search memories from vector database if conversation requires additional context. """ search\_vector = (await generate\_embeddings(\[search\_text\]))\[0\] memories = await search\_memories( search\_vector, user\_id=user\_id, score\_threshold=0.1, # 相似度阈值过滤 limit=5 ) return {"memories": memories} ​

ReAct 智能体最多允许 4 次检索迭代，然后必须生成回答。

[#RAG](https://x.com/search?q=%23RAG&src=hashtag_click)

[#AgenticAI](https://x.com/search?q=%23AgenticAI&src=hashtag_click)

[

![Image](https://pbs.twimg.com/media/HCFDoIea8AEr3qN?format=jpg&name=medium)


](/ArtistZhou/article/2026976235365028213/media/2026975664042340353)

7/ 🔄 Step 4：记忆维护的状态机设

记忆不是日志，而是动态知识图谱。当新信息到来时，系统必须决定：

• ADD：全新信息 → 创建新记忆 • UPDATE：信息演化 → 替换旧记忆（如“喜欢茶”→“讨厌茶”） • DELETE：信息失效 → 删除过时记忆 • NOOP：冗余信息 → 忽略

为什么 UPDATE 是先删除再插入，而非原地修改？

向量数据库中，文本修改意味着嵌入向量改变，而向量索引不支持“更新”操作。因此 UPDATE 的底层实现是：

1.  删除旧向量记录
 
2.  重新嵌入新文本
 
3.  插入新向量记录
 

维护智能体的核心代码：

class UpdateMemorySignature(dspy.Signature): """ Decide how to combine new memories into the database. Actions: ADD | UPDATE | DELETE | NOOP Think less and do actions. """ messages: list\[dict\] = dspy.InputField() existing\_memories: list\[MemoryWithIds\] = dspy.InputField() summary: str = dspy.OutputField( description="Summarize what you did (< 10 words)" ) memory\_updater = dspy.ReAct( UpdateMemorySignature, tools=\[add\_memory, update, delete, noop\], max\_iters=3 ) ​

[#MemoryManagement](https://x.com/search?q=%23MemoryManagement&src=hashtag_click)

[#StateMachine](https://x.com/search?q=%23StateMachine&src=hashtag_click)

[

![Image](https://pbs.twimg.com/media/HCFDttza4AAqMXa?format=jpg&name=medium)


](/ArtistZhou/article/2026976235365028213/media/2026975759961874432)

8/ 🎨 三大设计哲学：深度解

① 可选性（Optionality） 不是所有对话都需要记忆。闲聊、事实问答等场景，强行检索只会引入噪声。系统的智能体现在“知道何时不知道”。

② 自主性（Agency） 不硬编码检索逻辑（如“如果问题包含‘你记得’则检索”），而是提供工具，让 LLM 基于上下文自主决策。这要求： • 工具描述必须清晰准确 • 给予足够的上下文信息 • 设置合理的迭代限制防止无限循环

③ 原子化（Atomicity） 记忆的粒度控制是关键： • 太粗：“用户喜欢饮料” → 无法精确检索 • 太细：“用户”、“喜欢”、“茶” → 失去语义 • 恰到好处：“用户喜欢茶，尤其是绿茶” → 可独立嵌入和检索

[#DesignPatterns](https://x.com/search?q=%23DesignPatterns&src=hashtag_click)

9/ 🚀 生产环境的技术优势

多租户隔离 通过 QDrant 的 payload 索引，单次查询可在毫秒级完成用户数据过滤，确保企业级数据安全。

水平扩展性 • 向量数据库原生支持分片 • 提取和维护模块无状态，可水平扩展 • 嵌入计算可异步化，降低响应延迟

检索策略可插拔 当前使用余弦相似度，可无缝替换为： • 关键词匹配（BM25） • 时间衰减（越新的记忆权重越高） • 混合策略（相似度 + 关键词 + 时间）

成本优化 • 64 维嵌入将存储成本降低 24 倍 • 可选性设计减少 60-80% 的无用检索调用 • DSPy 的自动提示优化降低 token 消耗

[#Production](https://x.com/search?q=%23Production&src=hashtag_click)

[#Scalability](https://x.com/search?q=%23Scalability&src=hashtag_click)

10/ 🔮 未来演进方向的技术前瞻

① 图记忆系统（Graph Memory） 用 Neo4j 等图数据库替代向量数据库，存储三元组（实体-关系-实体）： • “用户” -「喜欢」→ “茶” • “用户” -「讨厌」→ “咖啡”

优势：支持多跳推理（“用户喜欢的东西中，哪些与编程相关？”）

② 元数据增强检索 当前仅按 user\_id 过滤，可扩展为：

filter = { "user\_id": 123, "category": "food", "created\_at": {">": "2024-01-01"} } ​

③ 提示注入优化 对于高度稳定的用户信息（如“用户是 Python 开发者”），可直接注入系统提示，避免每次检索：

system\_prompt = f"""用户背景：{persistent\_facts} 当前对话：{recent\_context}""" ​

④ 文件系统替代 用 .md 文件存储记忆，配合 ripgrep 或语义搜索引擎（如 vector-sqlite）。优势：可版本控制、人类可读、无外部依赖。

[#FutureOfAI](https://x.com/search?q=%23FutureOfAI&src=hashtag_click)

11/ 💻 实践价值与适用场景

这套架构特别适合以下场景：

客户支持聊天机器人 记住用户的历史问题、产品偏好、VIP 状态，提供千人千面的服务。

个人 AI 助手 长期记忆用户的日程偏好、工作习惯、人际关系，成为真正的“个人助理”而非“通用助手”。

教育辅导系统 追踪学生的知识掌握情况、学习风格、常见错误模式，动态调整教学策略。

医疗问诊助手 （需严格合规）记住患者病史、用药记录、过敏信息，辅助医生诊断。

实际对话效果展示：

📷

[

![Image](https://pbs.twimg.com/media/HCFD2YsaIAAWQhv?format=jpg&name=medium)


](/ArtistZhou/article/2026976235365028213/media/2026975908914143232)

注意：即使退出会话后重新进入，系统仍记得之前的对话细节

[#UseCases](https://x.com/search?q=%23UseCases&src=hashtag_click)

12/ 🛠️ 开源实现与扩展建议

完整代码仓库：

[github.com/avbiswas/mem0-dspy](http://github.com/avbiswas/mem0-dspy)

建议的扩展方向：

1.  增量学习优化：当前每次重新嵌入整个记忆，可优化为仅更新变更部分
 
2.  记忆压缩：长期记忆自动摘要，减少存储和检索开销
 
3.  冲突解决：当新信息与多条旧记忆矛盾时，智能决策保留哪些
 
4.  隐私合规：GDPR 合规的记忆删除、数据导出功能
 
5.  A/B 测试框架：测试不同嵌入模型、检索策略的效果
 

性能基准： • 提取延迟：~200ms（GPT-4） • 嵌入延迟：~50ms（批量） • 检索延迟：~10ms（QDrant，10 万条记忆）

[#OpenSource](https://x.com/search?q=%23OpenSource&src=hashtag_click)

[#DeveloperTools](https://x.com/search?q=%23DeveloperTools&src=hashtag_click)

13/ 📚 资源汇总与学习路径

必读论文与文章： • Mem0 架构论文：

[arxiv.org/abs/2504.19413](http://arxiv.org/abs/2504.19413)

• 本文原文：Towards Data Science • DSPy 框架文档：

[dspy-docs.vercel.app](//dspy-docs.vercel.app)

相关技术栈： • QDrant 向量数据库：

[qdrant.tech](//qdrant.tech)

• OpenAI Embedding API:

[platform.openai.com](http://platform.openai.com/)

• Pydantic 数据验证：

[docs.pydantic.dev](//docs.pydantic.dev)

进阶学习： • “Context Engineering with DSPy” - 深度教程 • “Vector Databases: From Embeddings to Applications” - 系统设计

想要深入构建自己的记忆层？这套架构为你提供了从概念到实现的完整蓝图。

[#LearningResources](https://x.com/search?q=%23LearningResources&src=hashtag_click)

[#BuildInPublic](https://x.com/search?q=%23BuildInPublic&src=hashtag_click)

💬 你在构建 LLM 应用时遇到过哪些记忆/上下文的挑战？

欢迎在评论区分享你的经验，或提出技术问题！

如果觉得有价值，请收藏 + 点赞 + 转发让更多朋友看到 🔁

🧵 /end