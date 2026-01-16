---
title: "Agent-native Architectures: How to Build Apps After Code Ends"
source: "https://every.to/guides/agent-native"
author: ""
created: 2026-01-14 14:57:45
date: 2026-01-14 14:57:45
description: ""
tags: ""
---
## Why now

现在软件代理能够可靠工作。Claude Code 展示，一个能够使用 bash 和文件工具、循环运行直至实现目标的大型语言模型（LLM），能够自主完成复杂的多步骤任务。

令人惊讶的发现：一个真正出色的编码代理实际上是一个真正优秀的通用代理。正是让 Claude Code 重构代码库的相同架构，也能让代理整理你的文件、管理你的阅读列表或自动化你的工作流程。

Claude Code SDK 使这一能力变得可实现。你可以构建这样的应用：其功能并非你编写的代码，而是你所描述的成果，由一个借助工具的智能体通过循环运作直至达成该成果。

这开辟了一个新领域：一种以 Claude Code 工作方式运行的软件，其应用范畴远不止编码领域。

## 保持 AI 前沿，你唯一需要的订阅

开始使用 Every 推出代理原生产品。

![Email](https://every.to/assets/icons/email-10ff3ba37cc5acd6148e8d02a1968f35810765415fd1aef2ecdfe22c5fd25af3.svg)

## Core principles

用户在用户界面上能执行的任何操作，代理都应该能够通过工具完成。

这是根本原则。没有它，其他一切都无关紧要。确保智能体配备有能完成 UI 所有功能的工具。

测试：选择任意一个用户界面操作，代理能否完成该操作？

2

### Granularity

工具应该是原子级原语。功能是智能体循环运行实现的成果。

工具是一种基础能力。功能是一种在提示中描述的结果，由使用工具的智能体通过循环操作直至实现。

测试：若要改变行为，你是会编辑提示词还是重构代码？

3

### Composability

借助原子化工具和同等能力，你只需编写新的提示词就能创建新功能。

想要一个“周回顾”功能吗？这只是一个提示：

```
"Review files modified this week. Summarize key changes.
Based on incomplete items and approaching deadlines,
suggest three priorities for next week."
```

代理使用 `list_files` 、 `read_file` 和自身判断。你描述了一个结果，代理会循环执行直到达成。

4

### Emergent capability

这个智能体能够完成你未明确设计的任务。

The flywheel:

1\. 以原子化工具和奇偶校验进行构建

2\. 用户提出了你没有预料到的需求

3\. 代理通过组合工具来完成任务（或者失败，暴露出不足）

你会发现请求内容中的模式

5\. 添加领域工具或提示词，以提升通用模式的效率

6\. Repeat

测试：它能否处理你所在领域的开放式请求？

代理原生应用通过积累上下文和优化提示词，会持续变得更好。

与传统软件不同，代理原生应用无需发布代码就能改进。

累积的上下文：状态通过上下文文件在不同会话间持续存在

### Parity

想象一个拥有精美界面的笔记应用，可用于创建、组织和标记笔记。用户要求：“创建一份总结我会议的笔记，并标记为紧急。” 如果用户界面（UI）能完成该操作，但代理无法做到，那么代理就会陷入困境。

改进措施：确保代理具备能够完成用户界面可执行的任何操作的工具（或工具组合）。这并非是将 UI 按钮与工具进行一对一映射，而是达成相同的目标。

这一原则：在添加任何用户界面能力时，需询问：代理能否实现这一目标？若不能，则添加必要的工具或原语。

能力图谱有助于：

| User Action | 智能体如何实现 |
| --- | --- |
| Create a note | " `write_file` 到笔记目录，或 `create_note` 工具" |
| 将一条笔记标记为紧急 | 元数据（ `update_file` ）或工具（ `tag_note` ） |
| Search notes | `search_files` or `search_notes` tool |
| Delete a note | `delete_file` or `delete_note` tool |

测试：请选择用户在界面中可执行的任意操作，向代理描述该操作，然后判断代理能否完成该结果。

### Granularity

关键转变：代理不再执行预先编排的流程，而是凭借判断追求结果。它会遇到意外情况、调整方法或提出澄清问题，循环持续直到实现目标结果。

你的工具越原子化，智能体就越能灵活运用它们。如果将决策逻辑整合到工具中，就等于把判断重新嵌入代码里。

### Composability

这对开发者和用户都适用。你可以通过添加提示词来推出新功能。用户可以通过修改或创建自己的提示词来自定义行为。

这个限制是：只有当工具足够原子化，能够以你未曾预料到的方式进行组合，并且代理与用户能力相当的时候，该条件才能成立。如果工具编码了过多逻辑，组合就会失效。

### Emergent Capability

示例：将我的会议记录与任务清单交叉参考，并告诉我我承诺了但尚未安排的事项。你没有构建承诺跟踪器，但如果代理能够读取会议记录和任务，它就能完成这项任务。

这揭示了潜在需求。与其猜测用户想要什么功能，不如观察用户让代理完成的操作。当模式出现时，你可以借助领域特定工具或专门的提示词来优化这些模式。但你无需预先预料这些需求，而是发现了它们。

这改变了你构建产品的方式。你不再试图在一开始就设想所有功能。你正在打造一个可靠的基础，并从实际出现的情况中学习。

###   随时间的改进

累积的上下文：代理在跨会话中维护状态——包括已存在的内容、用户的操作以及哪些做法有效。

多层面提示词优化：开发者级更新、用户级自定义，以及（高级）基于反馈的代理级调整。

高级自我修改：能够编辑自身提示词或代码的智能体需设置安全护栏——包括审批闸门、检查点、回滚路径和健康检查。

这些机制仍在探索中。上下文和提示词优化已被证实；自我修改正在兴起。

工具应是原子级基本单元。功能是代理通过循环操作达成的结果。代理做出决策，提示则描述结果。

### Less granular

```
Tool: classify_and_organize_files(files)
→ You wrote the decision logic
→ Agent executes your code
→ To change behavior, you refactor
```

将判断整合到工具中，这限制了灵活性。

### More granular

```
Tools: read_file, write_file, move_file, bash
Prompt: "Organize the downloads folder..."
→ Agent makes the decisions
→ To change behavior, edit the prompt
```

代理通过判断追求成果，从而赋予灵活性。

## 从基础原语到领域工具

从最基础的元素开始：bash、文件操作、基础存储。这证明了该架构的有效性，并揭示了代理的实际需求。

随着模式的出现，刻意添加领域特定工具。用这些工具来锚定词汇、设置防护栏或提升效率。

Vocabulary

一个 `create_note` 工具向代理解释“note”在你的系统中的含义。

Guardrails

某些操作需要验证，而这些验证不应由代理判断决定。

Efficiency

常用操作可打包以提升速度并降低成本。

`analyze_and_publish(input)`

将判断结果打包到工具中

`publish(content)`

一个动作：代理决定了要发布什么

领域工具的规则是：它们应从用户视角代表一个概念性操作。它们可包含机械验证，但关于做什么或是否做的判断应放在提示中。

保持原语可用。领域工具是捷径，而非闸门。除非有特定理由限制访问（如安全、数据完整性），否则代理仍应能在边缘情况中使用底层原语。这能保持可组合性和涌现能力。默认是开放的；将设置访问控制（闸门）作为有意识的决定。

## Graduating to code

一些操作需要从代理编排转向优化代码，以提升性能或可靠性。

2

为常用操作添加领域专用工具

更快，依旧由智能体编排

3

针对热路径，采用优化后的代码实现

Fast, deterministic

需要注意的是：即使一个操作升级为代码，代理也应能够自行触发优化后的操作，并在优化路径无法处理的边缘情况中回退到基础操作。升级的核心是效率，一致性仍然保持。

-   •  代理可以直接触发优化操作
-   •  对于边缘情况，智能体可以回退到基础原语

## 以文件作为通用接口

代理天生擅长处理文件。Claude Code 之所以能奏效，是因为 bash + 文件系统是最久经考验的代理接口。

Already Known

智能体已经了解 `cat` 、 `grep` 、 `mv` 、 `mkdir` 。文件操作是它们最擅长的基本操作。

Inspectable

用户可以查看代理创建的内容，编辑、移动或删除它。不存在黑箱。

Portable

导出简单，备份简单，数据归用户所有。

  跨设备同步

在移动设备上借助 iCloud，所有设备共享同一个文件系统。Agent 的工作无处不在——无需搭建服务器。

Self-Documenting

" `/projects/acme/notes/` 具有自文档化特性，而 `SELECT * FROM notes WHERE project_id = 123` 不具备这种特性。"

代理原生设计的一个通用原则是：设计要围绕代理能够推理的内容展开。对此，最有效的替代方式是让内容对人类而言易于理解。如果人类能看懂你的文件结构并明白其中的情况，那么代理大概率也能做到。

Needs validation

克劳德在构建工作中的贡献；丹仍在形成自己的看法。这些惯例是目前行之有效的一种方法，而非规定。还应考虑更好的解决方案。

### Directory naming

-   • Entity-scoped: `{entityType}/{entityId}/`
-   • 集合： `{type}/` （例如： `AgentCheckpoints/` ）
-   • 惯例：使用小写字母，用下划线连接，而非驼峰式命名

Markdown 用于易读内容，JSON 用于结构化数据。

### 一种命名方法：

| File | Naming Pattern | Example |
| --- | --- | --- |
| Entity data | `{entity}.json` | `library.json`, `status.json` |
|   人类可读内容 | `{content_type}.md` | `introduction.md`, `profile.md` |
| Agent reasoning | `agent_log.md` | 每个实体的代理历史 |
| Primary content | `full_text.txt` | 已下载/已提取的文本 |
| Multi-volume | `volume{N}.txt` | `volume1.txt`, `volume2.txt` |
| External sources | `{source_name}.md` | `wikipedia.md`, `sparknotes.md` |
| Checkpoints | `{sessionId}.checkpoint` | UUID-based |
| Configuration | `config.json` | Feature settings |

### Directory structure

```
Documents/
├── AgentCheckpoints/     # Ephemeral
│   └── {sessionId}.checkpoint
├── AgentLogs/            # Debugging
│   └── {type}/{sessionId}.md
└── Research/             # User's work
    └── books/{bookId}/
        ├── full_text.txt
        ├── notes.md
        └── agent_log.md
```

###   context.md 模板

```
# Context

## Who I Am
Reading assistant for the Every app.

## What I Know About This User
- Interested in military history and Russian literature
- Prefers concise analysis
- Currently reading *War and Peace*

## What Exists
- 12 notes in /notes
- three active projects
- User preferences at /preferences.md

## Recent Activity
- User created "Project kickoff" (two hours ago)
- Analyzed passage about Austerlitz (yesterday)

## My Guidelines
- Don't spoil books they're reading
- Use their interests to personalize insights

## Current State
- No pending tasks
- Last sync: 10 minutes ago
```

代理在每个会话开始时读取该文件，并随状态变化更新它——一种无需修改代码的可移植工作内存。

### Files vs. database

Needs validation

这种思路是一种思考方式，具体受移动开发的启发。对于网页应用，利弊权衡有所不同——Dan 对此尚无明确意见。

#### Use files for...

-   •  用户需要阅读/编辑的内容
-   •  受益于版本控制的配置
-   •  代理生成的内容
-   •  任何得益于透明度的事物
-   • Large text content

#### Use database for...

-   •  大容量结构化数据
-   •  需要复杂查询的数据
-   •  临时状态（会话、缓存）
-   •  具有关系的数据
-   •  需要被索引的数据

原则是：文件用于清晰可读，数据库用于结构化存储。当不确定时，优先选择文件——它们更透明，用户可以随时检查它们。

文件优先的方法在以下情况适用：

-   • 规模较小（仅一个用户的库，而非数百万条记录）
-   透明度优于查询速度
-   • 云同步（iCloud、Dropbox）与文件的同步效果良好

Hybrid approach

即使出于性能考虑需要数据库，也可考虑维护一个基于文件的“事实来源”，代理可使用该来源，并与数据库同步以支持用户界面。

### Conflict model

如果代理和用户写入相同的文件，就需要一个冲突模型。

Last write wins

简单来说，变更可能会丢失

Separate spaces

Agent 指向草稿/，用户发起

Append-only logs

增量式，从不覆盖

实用指南：日志和状态文件很少发生冲突。对于用户编辑的内容，建议进行明确处理或分开存储代理输出。iCloud 会因创建冲突副本而增加复杂性。

## 代理执行模式

### Completion signals

代理需要一种明确的方式来宣告“我完成了”。不要通过启发式方法来检测完成状态。

```
struct ToolResult {
  let success: Bool
  let output: String
  let shouldContinue: Bool
}

.success("Result")  // continue
.error("Message")   // continue (retry)
.complete("Done")   // stop loop
```

完成与成功/失败是不同的概念：一个工具可以成功并停止循环，或者失败并发出继续的信号以进行恢复。

目前尚未标准化的是：更丰富的控制流信号（如）：

•

升级处理——当代理需要在职责范围外进行人工决策时

目前，如果代理需要输入，它会在文本响应中询问。不存在正式的“等待输入阻塞”状态。这是一个仍在探索的领域。

###   模型层选择

并非所有代理操作都需要同等的智能水平

| Task Type | Tier | Reasoning |
| --- | --- | --- |
| Research agent | Balanced | 工具循环，良好推理 |
| Chat | Balanced | 足够快适合对话 |
| Complex synthesis | Powerful |   多源分析 |
|   快速分类 | Fast | 高工作量、简单任务 |

原则：在添加新代理时，需根据任务复杂度明确选择其层级，不要总是默认选择“最强”。

### Partial completion

```
struct AgentTask {
    var status: TaskStatus  // pending, in_progress, completed, failed, skipped
    var notes: String?      // Why it failed, what was done
}

var isComplete: Bool {
    tasks.allSatisfy { $0.status == .completed || $0.status == .skipped }
}
```

对于多步骤任务，需在任务级别跟踪进度。界面显示的内容：

进度：已完成 3/5 项任务（60%）

✓ \[1\] 查找原始资料

✓ "2. 下载全文"

✓ 提取关键段落（参考步骤 3）

✗ \[4\] 生成摘要 - 出错：上下文限制

○ \[5\] Create outline

#### 部分完成的场景：

智能体达到最大迭代次数

部分任务已完成，部分待处理。检查点已保存。继续从上次停止的地方恢复。

代理在一项任务中失败

任务标记为失败，注释里有错误。其他任务可继续（由代理决定）。

  任务中途发生网络错误

当前迭代抛出异常。会话被标记为失败。检查点保留了到该点为止的消息。

### Context limits

代理会话可以无限延长，但上下文窗口无法无限延长。设计上下文边界：

工具应该支持迭代式优化（先摘要，再细节，最后完整），而非非此即彼

为代理提供在会话期间整合学习内容的方式（“总结所学并继续”）

假设上下文最终会被填充——从一开始就为它设计

## Implementation patterns  实现模式

### Shared workspace

代理和用户应在同一个数据空间中协作，而非各自处于独立的沙箱环境中。

```
UserData/
├── notes/           ← Both agent and user read/write here
├── projects/        ← Agent can organize, user can override
└── preferences.md   ← Agent reads, user can edit
```

#### Benefits:

这应该是默认设置。只有在有特定需求时（如安全考虑、防止关键数据损坏）才使用沙箱。

### Context injection

代理需要明确其处理对象。系统提示应包含：

#### Available resources

```
## Available Data
- 12 notes in /notes
- Most recent: "Project kickoff"
- three projects in /projects
- Preferences at /preferences.md
```

#### Capabilities

```
## What You Can Do
- Create, edit, tag, delete notes
- Organize files into projects
- Search across all content
- Set reminders (write_file)
```

#### Recent activity

```
## Recent Context
- User created "Project kickoff"
  note (two hours ago)
- User asked about Q3 deadlines
  yesterday
```

在长时间会话中，提供一种刷新上下文的方法，确保智能体保持最新状态。

### 智能体与用户界面的通信

当代理行动时，用户界面应立即反映其动作。聊天集成的事件类型：

```
enum AgentEvent {
    case thinking(String)        // → Show as thinking indicator
    case toolCall(String, String) // → Show tool being used
    case toolResult(String)       // → Show result (optional)
    case textResponse(String)     // → Stream to chat
    case statusChange(Status)     // → Update status bar
}
```

关键：不能有无声操作。代理的变更必须立即可见。

#### Real-time progress:

####   通信模式：

有些工具过于冗余；考虑使用 `ephemeralToolCalls` 标志隐藏内部检查，同时显示有意义的操作。

沉默的代理会显得失效。可见的进展有助于建立信任。

##   产品的影响

基于智能体的架构不仅影响产品的构建方式，更影响产品给人的使用感受。

###   渐进式展示

上手简单，功能却强劲无穷。简单指令可立即响应。资深用户能探索出意想不到的应用方向。

Excel 是典型的例子：无论是购物清单还是财务模型，都使用同一个工具。Claude Code 也有这样的特点。界面保持简洁，能力随需求扩展。

-   •  简单入门：基本请求无需学习门槛即可正常使用
-   •  可发现的深度：用户在探索时发现新的力量
-   •  没有天花板：高级用户超出预期

代理在用户所在的地方与用户碰面。

###   潜在需求发现

构建一个坚实的基础。观察用户对代理的请求。正式化出现的模式。你是在发现，而非猜测。

传统产品开发：想象用户需求，构建产品，看看是否正确。

代理原生的产品开发：构建一个坚实的基础，观察用户要求代理执行的任务，使出现的模式规范化。

当用户向代理提出请求并成功时，这是一种信号。而当他们请求却失败时，这同样是一种信号——它揭示了你的工具或能力存在差距。

Over time, you can:

-   •  引入针对常见模式的领域工具（使这些工具更快、更可靠）
-   •  为频繁出现的请求创建专门的提示词（使其更易被发现）
-   •  移除闲置工具，简化系统

智能代理成为理解用户真实需求的研究工具。

### 审批和用户机构

Needs validation

这个框架是 Claude 的贡献，它源于在 Every 公司开发多款应用的过程中。但它尚未经过实战考验，Dan 在这里仍在形成自己的看法。

当代理采取未经请求的行动（即自主行事而非响应明确请求）时，你需要决定授予多少自主权。需考虑风险和可逆转性：

| Stakes | Reversibility | Pattern | Example |
| --- | --- | --- | --- |
| Low | Easy | Auto-apply | Organizing files |
| Low | Hard | Quick confirm | Publishing to feed |
| High | Easy | Suggest + apply | Code changes |
| High | Hard | Explicit approval | Sending emails |

*注意：这适用于代理未经请求的操作。如果用户明确要求代理执行某项操作（比如“发送那封邮件”），这本身就构成了批准——代理直接执行即可。*

自我修改应当清晰可读

当智能体能够修改自身行为（比如修改提示词、更新偏好设置、调整工作流程）时，目标是：

-   • 对变化内容的可见性
-   • 理解影响
-   回滚能力

审批流程是实现这一目标的一种方式，而具备易于回滚功能的审计日志则是另一种途径。其原则是：确保清晰易懂。

## Mobile

移动平台是代理原生应用的一流平台，拥有独特的约束与机遇。

A File System

代理可以自然地与文件交互，使用在其他所有场景中同样适用的基本操作。

Rich Context

一个你能进入的封闭花园。健康数据、位置、照片、日历——这些是桌面或网页上不存在的上下文信息。

Local Apps

每个人都有自己的应用副本。这类应用能够自我修改、自我分叉，并为每个用户进化。

App State Syncs

通过 iCloud，所有设备共享同一个文件系统。Agent 的工作会在所有设备上显示——无需服务器。

### The challenge

代理程序会长期运行，而移动应用不会。

一个应用可能需要 30 秒、5 分钟或 1 小时来完成一项任务。但 iOS 会在应用闲置几秒钟后将其置于后台，并且可能会为了释放内存而彻底关闭该应用。用户可能会在任务进行过程中切换应用、接电话或锁定手机。

这意味着，移动代理应用需要一套经过深思熟虑的方法来：

Checkpointing

保存状态，避免工作丢失

On-device vs. cloud

决定哪些在本地运行，哪些需要服务器

### Cloud file states

文件可能存在于 iCloud 中，但未下载到本地。阅读前请确保文件已下载。

```
await StorageService.shared
    .ensureDownloaded(folder: .research,
                      filename: "full_text.txt")
```

### Storage abstraction

使用存储抽象层。不要使用原生的 FileManager。对 iCloud 和本地存储进行抽象，这样代码的其他部分就不用关心具体实现了。

```
let url = StorageService.shared
    .url(for: .researchBook(bookId: id))
```

###   后台运行

Needs validation

Claude 在构建过程中的贡献；Dan 还在形成自己的意见。

iOS 为你提供有限的后台运行时间：

```
func prepareForBackground() {
    backgroundTaskId = UIApplication.shared
        .beginBackgroundTask(withName: "AgentProcessing") {
            handleBackgroundTimeExpired()
        }
}

func handleBackgroundTimeExpired() {
    for session in sessions where session.status == .running {
        session.status = .backgrounded
        Task { await saveSession(session) }
    }
}

func handleForeground() {
    for session in sessions where session.status == .backgrounded {
        Task { await resumeSession(session) }
    }
}
```

你大约有 30 秒时间，用它来：

-   "如果可能的话，请完成当前工具调用"
-   保存会话状态
-   • 优雅过渡到后台状态

对于真正长时间运行的代理程序：考虑使用一个能够运行数小时的服务器端编排器，移动应用作为查看器和输入工具。

### On-device vs. cloud

| Component | On-device | Cloud |
| --- | --- | --- |
| Orchestration | ✓ |  |
| 工具执行（文件、照片、HealthKit） | ✓ |  |
| LLM calls |  |   ✓（Anthropic API） |
| Checkpoints |   "✓（本地文件）" | Optional via iCloud |
| Long-running agents | Limited by iOS |   使用服务器是可行的 |

该应用在推理时需要联网，但可以离线访问数据。设计工具，使其在网络不可用时能优雅降级。

## Advanced patterns

### 动态能力发现

Needs validation

Claude 在构建过程中的贡献；Dan 还在形成自己的看法。这是我们比较看好的一种方法，但具体哪种方法更合适可能要根据你的使用场景来定。

为外部 API 中的每个端点单独构建工具的一种替代方案是：构建工具，让代理在运行时发现可用的接口

静态映射存在的问题：

```
// You built 50 tools for 50 data types
read_steps()
read_heart_rate()
read_sleep()
// When a new metric is added... code change required
// Agent can only access what you anticipated
```

动态能力发现:

```
// Two tools handle everything
list_available_types() → returns ["steps", "heart_rate", "sleep", ...]
read_data(type) → reads any discovered type

// When a new metric is added... agent discovers it automatically
// Agent can access things you didn't anticipate
```

这是粒度概念的逻辑终点。你的工具变得如此原子化，以至于它们能处理你构建时都未曾知晓的类型。

#### When to use this:

-   •  你希望代理拥有完全的用户级别访问权限的外部 API（例如 HealthKit、HomeKit、GraphQL 端点）
-   •  能够随时间添加新功能的系统
-   •  当你希望代理能够执行 API 支持的任何操作

#### 当静态映射合适时：

-   •  有意约束、范围有限的代理
-   •  当你需要对代理可访问的内容进行严格控制时
-   •  简单的 API，具有稳定且广为人知的端点

这种模式：一个工具用于发现可用能力，另一个工具用于与任何已发现的能力交互。让 API 负责输入验证，而非在枚举定义中重复验证逻辑。

### CRUD completeness

对于系统中的每个实体，验证代理具备完整的创建、读取、更新、删除（CRUD）能力：

审计：列出系统中的所有实体，确认所有四项操作对代理均可用

常见错误：你构建了 `create_note` 和 `read_notes` ，却遗漏了 `update_note` 和 `delete_note` 。用户让助手修正会议记录里的那个拼写错误，但助手帮不上忙。

## Anti-patterns

### 常见的方法并非完全原生代理

这些不一定错——它们可能适合你的使用场景。但值得注意的是，它们与本文档描述的架构有所不同。

#### Agent as router

智能体先明确用户需求，再调用正确的函数。智能体的智能用于路由，而非直接执行操作。这虽然可行，但你只发挥了智能体能力的一小部分。

#### 构建应用后，再添加代理

你以传统方式（以代码形式）构建功能，然后将这些功能暴露给智能体。智能体只能执行你现有功能所支持的操作，因此你不会获得涌现能力。

#### 请求/响应的思考

代理接收输入，完成一项任务，返回输出。但这忽略了循环的逻辑：代理需要达成某个目标，会持续执行直到完成，并在过程中处理意外状况。

####   工具的防御性设计

你过度约束工具输入，因为你习惯了防御性编程。严格的枚举类型、每一层的验证。这虽然安全，但却会阻止代理执行你未预料到的操作。

#### 在代码的正常流程中，代理仅执行

传统软件在代码中处理边缘情况——你编写逻辑来应对 X 出错时的情况。而原生代理架构则让代理凭借判断处理边缘情况。如果你的代码处理了所有边缘情况，代理就只是一个调用者。

### Specific anti-patterns  特定的反模式

#### 代理执行你的工作流程，而非追求结果

你编写了逻辑，代理只需调用它。决策存在于代码中，而非代理的判断。

```
# Wrong - you wrote the workflow
def process_request(input):
    category = categorize(input)      # your code decides
    priority = score_priority(input)   # your code decides
    store(input, category, priority)
    if priority > 3: notify()          # your code decides

# Right - agent pursues outcome in a loop
tools: store_item, send_notification
prompt: "Evaluate urgency 1-5, store with your assessment, notify if >= 4"
```

####   工作流形态的工具

将判断整合到工具中，然后将其分解为基本单元，让智能体进行组合。

#### Orphan UI actions

用户可以通过 UI 执行一些代理无法完成的操作。修复建议：保持功能对等。

#### Context starvation

代理不清楚有什么。用户说“整理我的笔记”，但代理不知道有笔记。

修复：将可用资源和能力注入到系统提示中。

####   无缘无故的门

领域工具是做某件事的唯一方式，而且你并没有打算限制访问。

修复：默认开启。除非有特定理由需要限制，否则保持基本组件可用。

#### 人工智能的能力限制

因模糊的安全顾虑而非具体风险，限制代理的行为。

代理通常应能执行用户可执行的操作。对于破坏性操作，应采用审批流程，而非完全移除相关功能。

#### 在动态映射更合适的情况下，应避免使用静态映射

与其为 50 个 API 端点构建 50 个工具，不如采用发现+访问模式，这样能带来更大的灵活性并使系统更具前瞻性。

#### 启发式补全检测

通过启发式方法（如连续迭代且无工具调用、检查预期输出文件）来检测代理完成情况的方式是不可靠的。

修复：要求代理通过完成工具明确发出完成信号。

## Success criteria

### Architecture

-   代理能够完成用户通过 UI 能做的一切（功能对等）
-   工具是原子原语；领域工具是快捷方式，而非门（粒度）
-   可以通过编写新的提示词来新增功能（可组合性）
-   代理能够完成你未明确设计的任务（涌现能力）
-   改变行为意味着编辑提示词，而非重构代码

### Implementation

-   系统提示包含可用的资源和能力
-   代理和用户在同一数据空间中工作
-   代理的操作会立即反映在应用界面中
-   每个实体都具备完整的 CRUD 能力
-   外部 API 在适当情况下采用动态能力发现
-   智能体明确表明完成（无启发式检测）

### Product

-   简单的请求能立即起作用，无需学习成本
-   高级用户能够推动系统向意外方向发展
-   你正通过观察用户对代理的请求，来了解用户的需求
-   审批要求需符合利益相关方利益并具备可逆性

### Mobile

-   检查点/恢复功能处理应用中断
-   优先采用 iCloud 存储，本地作为备用
-   后台执行能够明智地利用可用时间

### The ultimate test

向代理描述一个属于你应用领域内的结果，但你并未为此构建特定功能

它能找到完成它的方法，并循环操作直到成功吗？