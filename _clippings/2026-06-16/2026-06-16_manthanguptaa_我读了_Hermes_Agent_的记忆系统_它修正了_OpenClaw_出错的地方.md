---
title: "2026-06-16_manthanguptaa_我读了_Hermes_Agent_的记忆系统_它修正了_OpenClaw_出错的地方"
source: "https://x.com/manthanguptaa/status/2034849672985288957"
author:
  - "[[@manthanguptaa]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "x"
  - "@manthanguptaa"
  - "hermes"
  - "https"
---

# 我读了 Hermes Agent 的记忆系统，它修正了 OpenClaw 出错的地方

**Manthan Gupta**

# 我读了 Hermes Agent 的记忆系统，它修正了 OpenClaw 出错的地方

如果你读过我之前关于

[ChatGPT 记忆](https://manthanguptaa.in/posts/chatgpt_memory) 、

[Claude 记忆](https://manthanguptaa.in/posts/claude_memory)

、

[OpenClaw 记忆](https://manthanguptaa.in/posts/clawdbot_memory)

，你已经知道我一直回到同一个问题：这些智能体到底是如何记忆的？

Hermes Agent 对我来说特别有趣，因为这次我不需要仅仅从行为逆向工程一切。

[代码库](https://github.com/NousResearch/hermes-agent) 和

[文档](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)

都是公开的。因此，我没有用提示去试探一个黑盒，而是直接进入了构建提示状态、持久化会话、清空记忆以及查询过往对话的代码路径。

简短来说是这样的：Hermes 没有单一的内存系统。它有四个。

1\. 存储在 \`MEMORY.md\` 和 \`USER.md\` 中的非常小的、精心整理的提示词记忆。

2\. 一个可通过\`session\_search\`访问的、可搜索的 SQLite 格式过往会议归档。

3\. 代理管理的、类似于程序性记忆的技能

4\. 可选的

[Honcho](https://hermes-agent.nousresearch.com/docs/user-guide/features/honcho) 用于更深入用户建模的层

将所有这些联系在一起的关键设计选择很简单： 保持提示稳定以进行缓存，并将其他所有内容推送到工具中。

让我们直接开始吧。

# Hermes 的上下文结构

在理解记忆之前，有助于理解 Hermes 实际发送给模型的内容。

系统提示大致是这样构成的：

```text
[0] Default agent identity
[1] Tool-aware behavior guidance
[2] Honcho integration block (optional)
[3] Optional system message
[4] Frozen MEMORY.md snapshot
[5] Frozen USER.md snapshot
[6] Skills index
[7] Context files (AGENTS.md, SOUL.md, .cursorrules, .cursor/rules/*.mdc)
[8] Date/time + platform hints
[9] Conversation history
[10] Current user message
```

这很重要，因为 Hermes 正在优化提供方侧提示缓存 。提示构建器在源码中对此非常明确：稳定前缀应尽可能保持稳定。

那个决定解释了 Hermes 的大部分内存架构。

如果某条信息在每次交互中都需要，Hermes 会尽量将其精简并仅注入一次。如果信息体积较大、具有历史相关性，或仅偶尔有用，Hermes 会将其从提示中排除，并按需检索。

## Layer 1: 冻结的提示词记忆

内置的内存系统出人意料地小。

Hermes 将持久化内存存储在 \`~/.hermes/memories/\` 下的两个文件中：

```text
| File | Purpose | Limit |
|------|---------|-------|
| `MEMORY.md` | Agent notes about environment, conventions, tool quirks, lessons learned | 2,200 chars |
| `USER.md` | User profile: preferences, communication style, identity | 1,375 chars |
```

那不算多。大约总共 1300 个 token。

而这是故意的。

在会话开始时，Hermes 加载这两个文件，将它们渲染为一个提示块，然后 冻结该快照，在会话的其余部分 。会话中途的写入会立即持久化到磁盘，但它们不会修改已构建的系统提示。这些更改仅在新会话开始时，或在压缩触发的提示重建之后才会显示。

渲染后的格式看起来是这样的：

```text
══════════════════════════════════════════════
MEMORY (your personal notes) [67% — 1,474/2,200 chars]
══════════════════════════════════════════════
User's project is a Rust web service at ~/code/myapi using Axum + SQLx
§
This machine runs Ubuntu 22.04, has Docker and Podman installed
§
User prefers concise responses, dislikes verbose explanations
```

这里有一些我喜欢的微妙设计选择

它使用字符限制，而非标记限制

这使得内存逻辑与模型无关。Hermes 不需要为了判断内存是否已满而进行特定模型的分词。

2\. 它使用一种基于简单分隔符的文件格式

条目用 \`§\` 分隔。无向量数据库。无自定义二进制存储。仅为纯文本文件。

3\. 它故意将系统提示的内存保持得极小

这可能是整个设计中最重要的一点。Hermes 并不试图将其全部历史强行塞进提示内存中，它只想要其中最高价值的事实。

4\. 它将记忆视为 a 经过精心整理的状态，而非日记

这正是 Hermes 与 OpenClaw 有很大不同的地方。

OpenClaw 的日常日志具有只追加的特性。Hermes 则明确地朝相反方向推进。工具架构和测试表明：

- 保存用户偏好设置
- 保护环境的事实
- 保存重复修正
- 保存稳定的规范
- 不要保存任务进度
- Do not 保存会话结果
- 不要保存临时待办事项状态

事实是，Hermes 希望 \`MEMORY.md\` 和 \`USER.md\` 保持热点状态、紧凑且缓存友好。

## \`memory\`工具

Hermes 通过一个名为\`memory\`的工具管理这些文件，该工具具有三个操作：

- 添加
- 替换
- 移除

当前工具界面中没有实际的读取操作，因为在会话开始时内存已经被注入到提示中。

一个很好的可用性细节是，\`replace\` 和 \`remove\` 使用 子串匹配 。您不需要内部 ID，只需从现有条目中传递一个唯一子串即可。

示例

```python
memory(
 action="replace",
 target="memory",
 old_text="dark mode",
 content="User prefers light mode in VS Code, dark mode in terminal"
)
```

该系统还会拒绝完全重复的内容，并在危险内容进入提示内存之前阻止其进入。源系统扫描内存条目，以检测提示注入模式、凭证泄露字符串、SSH 后门线索以及不可见的 Unicode 字符。

这很有道理。写入内存的任何内容实际上正在成为未来系统提示的一部分。

## 第 2 层: \`session\_search\` 用于情景记忆

如果 \`MEMORY.md\` 和 \`USER.md\` 是 Hermes 的热记忆，那么 \`session\_search\` 是其长尾召回系统。

所有过去的会话都存储在 \`~/.hermes/state.db\` 中，这是一个 SQLite 数据库，包含：

- 一个 \`sessions\` 表
- 一个 \`messages\` 表
- 一个 FTS5 全文搜索索引
- 继承链通过 \`parent\_session\_id\` 关联

当模型需要从之前的对话中回忆某些内容时，Hermes 不会搜索\`MEMORY.md\`。 而是搜索会话数据库。

流程看起来是这样的：

```text
FTS5 search over past messages
-> group results by session
-> resolve parent/child lineage
-> load top matching sessions
-> truncate transcript around relevant matches
-> summarize each session with a cheap auxiliary model
-> return focused recaps to the main model
```

这是一种与那些试图对每一条记忆笔记进行语义索引的系统截然不同的理念。

Hermes 基本上是说：

- 保持始终注入的内存微小
- 将真实历史存储在 SQLite 中
- 仅在需要时搜索历史记录
- 先总结结果再交还

那是一个实用的设计。

它也比盲目地将长对话历史塞进每个提示词更便宜。

文档将 \`session\_search\` 描述为一种回答类似以下问题的方式：

- 我们上周讨论过这个吗？
- 我们关于 X 做了什么？
- 正如我之前提到的...

换句话说，\`MEMORY.md\` 用于持久事实，而 \`session\_search\` 用于情景回忆。

## 第3层：压缩和内存刷新

Hermes 的另一个巧妙之处是它压缩长对话之前发生的事情。

随着对话会话的增长，Hermes 最终会总结对话的中间部分以保持在模型的上下文窗口范围内。但总结是有损的，重要事实可能会消失。

所以 Hermes 首先会进行内存刷新 。

压缩之前，它会注入一条合成的系统/用户指令，其基本内容是：

```text
The session is being compressed.
Save anything worth remembering.
Prioritize user preferences, corrections, and recurring patterns over task-specific details.
```

然后它运行了一次额外的模型调用，此时仅\`memory\`工具可用。

如果模型决定某些内容应该在压缩中保留，它会在对话被总结之前将其写入 \`MEMORY.md\` 或 \`USER.md\`。

那是一个真正好的模式。

它给模型最后一次机会，在对话中间部分崩溃之前提炼持久的部分。

更妙的是，压缩后，Hermes 会使缓存的系统提示失效并重建，同时从磁盘重新加载内存。这意味着任何在压缩前被刷新的数据都会成为下一个稳定提示快照的一部分。

因此流程是：

```text
Long conversation
→ flush durable facts to memory
→ compress old turns
→ rebuild prompt
→ continue with smaller context and updated memory
```

这正是那种让 Hermes 感觉像是真正的内存架构，而非一个附加的笔记存储的东西。

## 第4层：技能作为程序性记忆

Hermes 的记忆故事不仅仅是事实和记录。

它还具备 技能 。

技能存储在 \`~/.hermes/skills/\` 目录下，其作用类似于可复用的知识文档。这些文档明确将它们描述为代理的过程性记忆。

当 Hermes 发现一个非平凡的工作流、修复一个棘手的问题，或者学习到一种更好的做事方法时，它可以将这些内容保存为技能并在之后重复使用。

这是件大事。

大多数记忆系统只关注语义记忆：名称、偏好、事实和摘要。但智能体还需要记住 如何做事，而不仅仅是 什么发生了什么。

Hermes 通过将程序性知识与提示记忆分离来处理这一点：

- \`MEMORY.md\` / \`USER.md\` 用于简洁、持久的事实
- session\_search 用于情景回忆
- 用于可复用工作流的技能

这里还有一个很好的 token 效率技巧。Hermes 不会盲目地将所有技能都注入到 prompt 中。它会注入一个紧凑的 技能索引并且只在需要时才加载完整的技能内容。

这使得过程内存保持可用，而无需在每次操作时支付全部令牌成本。

## 第5层：用户深度建模负责人

然后还有可选的 Honcho 层。

如果本地记忆是 Hermes 精心整理的笔记本，Honcho 就是它对更丰富用户模型的尝试。

Honcho 默认情况下以 \`hybrid\` 模式与内置内存系统同时运行。它增加了：

- 跨会话用户建模
- 跨机器和跨平台连续性
- 基于用户上下文的语义搜索
- 辩证法，关于用户或 AI 同类的 LLM 生成的回答

有趣的部分是 Hermes 如何在不破坏提示缓存的情况下进行集成。

第一轮 vs 后续轮次

在会话的第一次回合中，预先获取的 Honcho 上下文可以被嵌入到缓存的系统提示中。

在后续轮次中 ，Hermes 避免修改那个稳定的系统提示。相反，它仅在 API 调用时将 Honcho 记忆附加到当前用户的轮次中。这意味着：

- 稳定的前缀保持稳定
- 提示缓存仍然有效
- 轮次 N 可以消耗轮次 N-1 之后在后台预获取的上下文

这是一个非常明智的妥协。

Honcho 本身也建模 两个同级节点 ：

- 用户
- AI 助手

所以 Hermes 不仅仅是试图记住你。它还可以随着时间的推移构建一个关于自身的表示。

那既很酷又有点狂野。

# Hermes 与 OpenClaw 的区别

既然我最近写了关于 OpenClaw 的内容，这种比较值得明确。

## OpenClaw

- 内存更接近以 Markdown 为优先的存储
- 每日日志和长期存储文件充当主要事实来源
- 记忆检索依赖于对已存储笔记的混合搜索

## 爱马仕

- 提示记忆被严格限制
- 会话历史存储在 SQLite 中，而非提示记忆文件中
- 过往工作通过 \`session\_search\` 被检索
- 程序性记忆被转化为技能
- 更深入的用户建模可选地委托给 Honcho

这里的关键见解是，Hermes 比 OpenClaw 更缓存感知。

OpenClaw 更加强调“内存即可搜索的已存储知识”。Hermes 更加强调“内存即热工作集加冷检索层”。

我其实认为这是生产代理的正确方向。

并非所有事物都值得存在于系统提示中。

# Hermes 做对了什么

在浏览了代码仓库和文档之后，我认为 Hermes 把三件大事都做对了。

## 它将热内存与冷记忆分离

这是核心的架构优势。

小提示记忆用于始终重要的内容。搜索仅在某些时候重要的内容。

## 2\. 它将提示词稳定性视为一等约束

很多代理系统只谈论内存，却不提及缓存。Hermes 显然同时关注这两者。

冻结的快照、延迟的提示更新、回合级 Honcho 注入以及压缩会话重建，都指向同一个设计原则：如果希望获得良好的延迟和成本，不要随意修改你的提示。

## 3\. 它承认内存是复数。

Hermes 并不声称一个门店能解决所有问题。

它具有：

- 语义配置文件存储器
- 情景式会话回忆
- 通过技能的程序性记忆
- 可选的高阶用户建模通过 Honcho

那是对代理实际需求的一个更为现实的看法。

# 结论

Hermes 的记忆系统不是一个巨大的知识库，也不是一个被美化的向量存储。它是一个分层的连续性架构。

在中心是一个精心整理的小型提示记忆：\`MEMORY.md\` 和 \`USER.md\`。围绕它是可搜索的 SQLite 历史记录，用于情景式回忆。在那之外是一个用于过程化复用的技能系统。如果你启用 Honcho，Hermes 会在所有其他组件之上添加一个更深入的用户模型。

所有这些背后的设计原则最让我印象深刻： 记忆应该帮助智能体保持有用性，同时不破坏提示词的稳定性 。

那就是真正的诀窍。

不贪多记忆，而是记住正确的事物，在合适的层级，以合理的成本。

# 参考文献

- [Hermes Agent GitHub 代码仓库](https://github.com/NousResearch/hermes-agent)
 
- [Hermes 持久内存 文档](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory)
 
- [Hermes 提示组装文档](https://hermes-agent.nousresearch.com/docs/developer-guide/prompt-assembly)
 
- [Hermes 会话存储文档](https://hermes-agent.nousresearch.com/docs/developer-guide/session-storage)
 
- [Hermes 技能文档](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)
 
- [Hermes Honcho 文档](https://hermes-agent.nousresearch.com/docs/user-guide/features/honcho)
 

* * *

这篇文章基于直接阅读 Hermes 的源代码和文档，而非黑盒逆向工程，因此如果上游实现发生变化，本分析的部分内容可能会过时。如果您觉得这篇文章有趣，我很乐意听取您的看法。分享到

[X/ Twitter](https://twitter.com/manthanguptaa),

[LinkedIn](https://www.linkedin.com/in/manthanguptaa/)

，或通过 guptaamanthan01@gmail.com 联系。