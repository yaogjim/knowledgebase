---
title: "2026-01-27_Manthan Gupta on X How Clawdbot Remembers Everything"
source: "https://x.com/manthanguptaa/status/2015780646770323543"
author: ""
created: 2026-01-27 13:39:48
date: 2026-01-27 13:39:48
description: ""
tags: ""
---
Clawdbot 是一个开源的个人 AI 助手（MIT 许可证），由 创建，它迅速获得了关注，在 GitHub 上获得了超过 32,600 颗星， 在撰写本文时。与在云端运行的 ChatGPT 或 Claude 不同，Clawdbot 在你的设备上本地运行，并能与你已使用的聊天平台集成，比如 Discord、WhatsApp、Telegram 等等。

让 Clawdbot 脱颖而出的是它能够自主处理现实世界的任务：管理电子邮件、安排日历事件、处理航班值机，以及按计划运行后台任务。 持久记忆系统 ，它保持全天候的上下文保留，记住对话并无限期地基于之前的互动进行构建。

如果你读过我之前关于 ChatGPT 记忆和 Claude 记忆的帖子，你知道我对不同 AI 产品处理记忆的方式很着迷。Clawdbot 采用了截然不同的方法：它不使用基于云的、由公司控制的记忆，而是将所有内容都保存在本地，让用户完全掌控自己的上下文和技能。

在深入研究内存之前，让我们了解模型在每次请求时看到的内容：

```
[0] System Prompt (static + conditional instructions)
[1] Project Context (bootstrap files: AGENTS.md, SOUL.md, etc.)
[2] Conversation History (messages, tool calls, compaction summaries)
[3] Current Message
```

系统提示定义了代理的能力和可用工具。与记忆相关的是项目上下文，它包括用户可编辑的 Markdown 文件，这些文件被注入到每个请求中：

[

![Image](https://pbs.twimg.com/media/G_l6OxEXIAIUC-x?format=png&name=900x900)



](https://x.com/manthanguptaa/article/2015780646770323543/media/2015776702333394946)

这些文件存于代理的工作区，与记忆文件一同存在，使得整个代理配置透明且可编辑。

理解上下文和记忆之间的区别是理解 Clawdbot 的基础。

```
Context = System Prompt + Conversation History + Tool Results + Attachments
```

-   短暂的 \- 仅存在于此次请求中
    
-   有界的 - 受模型上下文窗口限制（例如，200K tokens）
    
-   昂贵的 - 每个 token 都计入 API 成本和速度
    

```
Memory = MEMORY.md + memory/*.md + Session Transcripts
```

-   持久性 ——重启后、数天、数月后仍然存在。
    
-   无界 ——可以无限增长
    
-   便宜 \- 存储无 API 费用
    
-   可搜索 \- 已建立语义检索索引
    

```
{
  "name": "memory_search",
  "description": "Mandatory recall step: semantically search MEMORY.md + memory/*.md before answering questions about prior work, decisions, dates, people, preferences, or todos",
  "parameters": {
    "query": "What did we decide about the API?",
    "maxResults": 6,
    "minScore": 0.35
  }
}
```

```
{
  "results": [
    {
      "path": "memory/2026-01-20.md",
      "startLine": 45,
      "endLine": 52,
      "score": 0.87,
      "snippet": "## API Discussion\nDecided to use REST over GraphQL for simplicity...",
      "source": "memory"
    }
  ],
  "provider": "openai",
  "model": "text-embedding-3-small"
}
```

```
{
  "name": "memory_get",
  "description": "Read specific lines from a memory file after memory_search",
  "parameters": {
    "path": "memory/2026-01-20.md",
    "from": 45,
    "lines": 15
  }
}
```

```
{
  "path": "memory/2026-01-20.md",
  "text": "## API Discussion\n\nMet with the team to discuss API architecture.\n\n### Decision\nWe chose REST over GraphQL for the following reasons:\n1. Simpler to implement\n2. Better caching\n3. Team familiarity\n\n### Endpoints\n- GET /users\n- POST /auth/login\n- GET /projects/:id"
}
```

没有专门的 memory\_write 工具。代理使用标准的写入和编辑工具（这些工具也用于处理任何文件）来向内存写入内容。由于内存本质上是 Markdown 格式，你也可以手动编辑这些文件（它们会自动重新索引）。

[

![Image](https://pbs.twimg.com/media/G_l62FfbYAAe439?format=png&name=900x900)



](https://x.com/manthanguptaa/article/2015780646770323543/media/2015777377830526976)

自动写入也会在预压缩刷新和会话结束期间发生（将在后续章节中说明）。

Clawdbot 的记忆系统建立在“记忆是智能体工作区中的纯 Markdown”这一原则之上。

记忆存在于代理的工作区（默认：~/clawd/）：

```
~/clawd/
├── MEMORY.md              - Layer 2: Long-term curated knowledge
└── memory/
    ├── 2026-01-26.md      - Layer 1: Today's notes
    ├── 2026-01-25.md      - Yesterday's notes
    ├── 2026-01-24.md      - ...and so on
    └── ...
```

第一层：每日日志 (memory/YYYY-MM-DD.md)

这些是只追加的每日笔记，是代理全天在此记录的内容。代理会在想要记住某件事或被明确告知要记住某件事时进行记录。

```
# 2026-01-26

## 10:30 AM - API Discussion
Discussed REST vs GraphQL with user. Decision: use REST for simplicity.
Key endpoints: /users, /auth, /projects.

## 2:15 PM - Deployment
Deployed v2.3.0 to production. No issues.

## 4:00 PM - User Preference
User mentioned they prefer TypeScript over JavaScript.
```

这是精心整理的、持久的知识。当重要事件、想法、决策、观点和学到的经验教训出现时，Agent 会记录到这里。

```
# Long-term Memory

## User Preferences
- Prefers TypeScript over JavaScript
- Likes concise explanations
- Working on project "Acme Dashboard"

## Important Decisions
- 2026-01-15: Chose PostgreSQL for database
- 2026-01-20: Adopted REST over GraphQL
- 2026-01-26: Using Tailwind CSS for styling

## Key Contacts
- Alice (alice@acme.com) - Design lead
- Bob (bob@acme.com) - Backend engineer
```

```
## Every Session

Before doing anything else:
1. Read SOUL.md - this is who you are
2. Read USER.md - this is who you are helping
3. Read memory/YYYY-MM-DD.md (today and yesterday) for recent context
4. If in MAIN SESSION (direct chat with your human), also read MEMORY.md

Don't ask permission, just do it.
```

```
┌─────────────────────────────────────────────────────────────┐
│  1. File Saved                                              │
│     ~/clawd/memory/2026-01-26.md                            │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  2. File Watcher Detects Change                             │
│     Chokidar monitors MEMORY.md + memory/**/*.md            │
│     Debounced 1.5 seconds to batch rapid writes             │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  3. Chunking                                                │
│     Split into ~400 token chunks with 80 token overlap      │
│                                                             │
│     ┌────────────────┐                                      │
│     │ Chunk 1        │                                      │
│     │ Lines 1-15     │──────┐                               │
│     └────────────────┘      │                               │
│     ┌────────────────┐      │ (80 token overlap)            │
│     │ Chunk 2        │◄─────┘                               │
│     │ Lines 12-28    │──────┐                               │
│     └────────────────┘      │                               │
│     ┌────────────────┐      │                               │
│     │ Chunk 3        │◄─────┘                               │
│     │ Lines 25-40    │                                      │
│     └────────────────┘                                      │
│                                                             │
│     Why 400/80? Balances semantic coherence vs granularity. │
│     Overlap ensures facts spanning chunk boundaries are     │
│     captured in both. Both values are configurable.         │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  4. Embedding                                               │
│     Each chunk -> embedding provider -> vector              │
│                                                             │
│     "Discussed REST vs GraphQL" ->                          │
│         OpenAI/Gemini/Local ->                              │
│         [0.12, -0.34, 0.56, ...]  (1536 dimensions)         │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  5. Storage                                                 │
│     ~/.clawdbot/memory/<agentId>.sqlite                     │
│                                                             │
│     Tables:                                                 │
│     - chunks (id, path, start_line, end_line, text, hash)   │
│     - chunks_vec (id, embedding)      -> sqlite-vec         │
│     - chunks_fts (text)               -> FTS5 full-text     │
│     - embedding_cache (hash, vector)  -> avoid re-embedding │
└─────────────────────────────────────────────────────────────┘
```

> sqlite-vec 是一个 SQLite 扩展，可直接在 SQLite 中启用向量相似度搜索，无需外部向量数据库。

> FTS5FTS5 是 SQLite 的内置全文搜索引擎，它驱动 BM25 关键词匹配。它们一起让 Clawdbot 能够从单个轻量级数据库文件中运行混合搜索（语义+关键词）。

当你搜索记忆时，Clawdbot 会并行运行两种搜索策略。向量搜索（语义）会找到语义相同的内容，而 BM25 搜索（关键词）会找到包含精确词元的内容。

```
finalScore = (0.7 * vectorScore) + (0.3 * textScore)
```

为什么是 70/30？语义相似度是记忆召回的主要信号，但 BM25 关键词匹配能捕捉到向量可能遗漏的精确词汇（名称、ID、日期）。低于 minScore 阈值（默认 0.35）的结果会被过滤掉。所有这些值都是可配置的。

这能确保你无论搜索概念（“那个数据库的东西”）还是具体信息（“POSTGRES\_URL”）都能获得良好的结果。

Clawdbot 支持多个代理，每个都有完全的内存隔离：

```
~/.clawdbot/memory/              # State directory (indexes)
├── main.sqlite                  # Vector index for "main" agent
└── work.sqlite                  # Vector index for "work" agent

~/clawd/                         # "main" agent workspace (source files)
├── MEMORY.md
└── memory/
    └── 2026-01-26.md

~/clawd-work/                    # "work" agent workspace (source files)
├── MEMORY.md
└── memory/
    └── 2026-01-26.md
```

Markdown 文件（真相来源）存放在每个工作区中，而 SQLite 索引（派生数据）存放在状态目录中。每个代理都有自己的工作区和索引。内存管理器以 agentId + 工作区目录 为键，因此不会自动发生跨代理的内存搜索。

代理能读取彼此的记忆吗？默认情况下不能。每个代理只能看到自己的工作区。不过，工作区是一个软沙箱（默认工作目录），并非硬边界。理论上，代理可以通过绝对路径访问其他工作区，除非开启严格沙箱。

这种隔离有助于区分不同场景。一个用于 WhatsApp 的“个人”助手和一个用于 Slack 的“工作”助手，每个都有不同的记忆和个性。

每个 AI 模型都有上下文窗口限制。Claude 有 20 万 token，GPT-5.1 有 100 万。长对话最终会碰到这个瓶颈。

当这种情况发生时，Clawdbot 使用压缩：总结较旧的对话形成一个简洁的条目，同时保留最近的消息完整。

```
┌─────────────────────────────────────────────────────────────┐
│  Before Compaction                                          │
│  Context: 180,000 / 200,000 tokens                          │
│                                                             │
│  [Turn 1] User: "Let's build an API"                        │
│  [Turn 2] Agent: "Sure! What endpoints do you need?"        │
│  [Turn 3] User: "Users and auth"                            │
│  [Turn 4] Agent: *creates 500-line schema*                  │
│  [Turn 5] User: "Add rate limiting"                         │
│  [Turn 6] Agent: *modifies code*                            │
│  ... (100 more turns) ...                                   │
│  [Turn 150] User: "What's the status?"                      │
│                                                             │
│  ⚠️ APPROACHING LIMIT                                       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  Compaction Triggered                                       │
│                                                             │
│  1. Summarize turns 1-140 into a compact summary            │
│  2. Keep turns 141-150 intact (recent context)              │
│  3. Persist summary to JSONL transcript                     │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  After Compaction                                           │
│  Context: 45,000 / 200,000 tokens                           │
│                                                             │
│  [SUMMARY] "Built REST API with /users, /auth endpoints.    │
│   Implemented JWT auth, rate limiting (100 req/min),        │
│   PostgreSQL database. Deployed to staging v2.4.0.          │
│   Current focus: production deployment prep."               │
│                                                             │
│  [Turn 141-150 preserved as-is]                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

-   你会看到：🧹 自动压缩完成
    
-   原始请求将使用压缩后的上下文重试
    

与某些优化不同，整理操作会持久化到磁盘。摘要会被写入会话的 JSONL 转录文件，因此未来的会话将从整理后的历史记录开始。

基于 LLM 的压缩是一个有损过程。重要信息可能被总结掉，甚至可能丢失。为了应对这一点，Clawdbot 使用了预压缩内存刷新。

```
┌─────────────────────────────────────────────────────────────┐
│  Context Approaching Limit                                  │
│                                                             │
│  ████████████████████████████░░░░░░░░  75% of context       │
│                              ↑                              │
│                    Soft threshold crossed                   │
│                    (contextWindow - reserve - softThreshold)│
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  Silent Memory Flush Turn                                   │
│                                                             │
│  System: "Pre-compaction memory flush. Store durable        │
│           memories now (use memory/YYYY-MM-DD.md).          │
│           If nothing to store, reply with NO_REPLY."        │
│                                                             │
│  Agent: reviews conversation for important info           │
│         writes key decisions/facts to memory files        │
│         -> NO_REPLY (user sees nothing)                     │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  Compaction Proceeds Safely                                 │
│                                                             │
│  Important information is now on disk                       │
│  Compaction can proceed without losing knowledge            │
└─────────────────────────────────────────────────────────────┘
```

内存刷新可在 clawdbot.yaml 文件或 clawdbot.json 文件中配置。

```
{
  agents: {
    defaults: {
      compaction: {
        reserveTokensFloor: 20000,
        memoryFlush: {
          enabled: true,
          softThresholdTokens: 4000,
          systemPrompt: "Session nearing compaction. Store durable memories now.",
          prompt: "Write lasting notes to memory/YYYY-MM-DD.md; reply NO_REPLY if nothing to store."
        }
      }
    }
  }
}
```

工具结果可能会很大。单个 exec 命令可能会输出 50,000 个字符的日志。修剪会修剪这些旧输出而不重写历史。这是一个有损过程，旧输出无法恢复。

```
┌─────────────────────────────────────────────────────────────┐
│  BEFORE PRUNING (in-memory)                                 │
│                                                             │
│  Tool Result (exec): [50,000 chars of npm install output]   │
│  Tool Result (read): [Large config file, 10,000 chars]      │
│  Tool Result (exec): [Build logs, 30,000 chars]             │
│  User: "Did the build succeed?"                             │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼ (Soft trim + hard clear)
┌─────────────────────────────────────────────────────────────┐
│  AFTER PRUNING (sent to model)                              │
│                                                             │
│  Tool Result (exec): "npm WARN deprecated...[truncated]     │
│                       ...Successfully installed."           │
│  Tool Result (read): "[Old tool result content cleared]"    │
│  Tool Result (exec): [Kept - too recent to prune]           │
│  User: "Did the build succeed?"                             │
└─────────────────────────────────────────────────────────────┘
```

Anthropic 缓存提示前缀长达 5 分钟，以减少重复调用时的延迟和成本。当相同的提示前缀在 TTL 窗口内发送时，缓存的 token 成本降低约 90%。TTL 过期后，下一次请求必须重新缓存整个提示。

问题：如果会话闲置超过 TTL，下一个请求会丢失缓存，必须按全额“缓存写入”价格重新缓存完整的会话历史。

缓存-TTL 修剪通过检测缓存何时过期并在下一次请求前修剪旧的工具结果来解决这个问题。更小的重新缓存提示意味着更低的成本:

```
{
  agent: {
    contextPruning: {
      mode: "cache-ttl",      // Only prune after cache expires
      ttl: "600",              // Match your cacheControlTtl
      keepLastAssistants: 3,  // Protect recent tool results
      softTrim: {
        maxChars: 4000,
        headChars: 1500,
        tailChars: 1500
      },
      hardClear: {
        enabled: true,
        placeholder: "[Old tool result content cleared]"
      }
    }
  }
}
```

会话不会永远持续。它们会根据可配置的规则重置，为内存创建自然的边界。默认行为是每天重置。但还有其他可用的模式。

[

![Image](https://pbs.twimg.com/media/G_l8JPUWoAA1FpY?format=png&name=900x900)



](https://x.com/manthanguptaa/article/2015780646770323543/media/2015778806397575168)

当你运行 /new 以启动一个新的会话，会话内存钩子可以自动保存上下文:

```
/new
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  SESSION-MEMORY HOOK TRIGGERED                              │
│                                                             │
│  1. Extract last 15 messages from ending session            │
│  2. Generate descriptive slug via LLM                       │
│  3. Save to ~/clawd/memory/2026-01-26-api-design.md         │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  NEW SESSION STARTS                                         │
│                                                             │
│  Previous context is now searchable via memory_search       │
└─────────────────────────────────────────────────────────────┘
```

Clawdbot 的记忆系统之所以成功，是因为它秉持了几个关键原则：

Memory 是纯 Markdown。你可以阅读、编辑和进行版本控制。没有不透明的数据库或专有格式。

与其把所有东西都塞进上下文里，代理只搜索相关的内容。这样能让上下文更聚焦，还能降低成本。

重要信息会保存在磁盘文件里，不只是对话记录。数据压缩无法销毁已保存的内容。

单独的向量搜索会错过精确匹配。单独的关键词搜索会错过语义。混合搜索能同时满足两者。

-   Clawdbot 文档 Clawdbot 文档 - 官方文档，涵盖设置、配置及所有功能
    

如果你觉得这个有趣，我很想听听你的想法。在 Twitter、LinkedIn 上分享，或者通过 guptaamanthan01@gmail.com 联系。