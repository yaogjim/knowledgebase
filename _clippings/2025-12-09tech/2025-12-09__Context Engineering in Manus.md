---
title: "Context Engineering in Manus"
source: "https://rlancemartin.github.io/2025/10/15/manus/"
author:
date: "2025-12-09T16:06:38+08:00"
created: 2025-12-09
description: "Manus approaches to context engineering."
tags:
---
[Lance Martin](https://x.com/RLanceMartin)

## 为何需要语境工程

> 本周早些时候，我与 [Manus 联合创始人兼首席科学官季一超（Peak）](https://luma.com/819i5ime) 进行了一场网络研讨会。您可 [在此处](https://youtu.be/6_BcCthVvb8?si=o8ovK6YNWOXtq7j7) 观看视频， [此处](https://drive.google.com/file/d/1QGJ-BrdiTGslS71sYH4OJoidsry3Ps9g/view) 查看我的幻灯片， [此处](https://docs.google.com/presentation/d/1Z-TFQpSpqtRqWcY-rBpf7D3vmI0rnMhbhbfv01duUrk/edit?usp=sharing) 查看 Peak 的幻灯片。以下是我的笔记。

[Anthropic 将智能体定义为](https://www.anthropic.com/engineering/building-effective-agents) 由 LLMs 自主调度流程与工具使用的系统，全程掌控任务执行方式。简而言之，就是 LLM 在循环中调用工具的工作模式。

[Manus](https://en.wikipedia.org/wiki/Manus_\(AI_agent\)) 是最受欢迎的 [通用消费级智能体](https://x.com/manusai_hq?lang=en) 之一。典型的 Manus 任务会使用 [50 次工具调用](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) 。若不进行上下文工程处理，这些工具调用结果将在 LLM 上下文窗口中不断累积。随着上下文窗口逐渐填满，许多研究者观察到 LLM 性能会出现明显下降。

例如，Chroma 公司对 [上下文衰减](https://research.trychroma.com/context-rot) 现象进行了深入研究，而 Anthropic 则 [阐释](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) 了不断扩展的上下文如何消耗 LLM 的注意力资源。因此，在构建智能体时审慎管理输入 LLM 上下文窗口的内容至关重要。 [Karpathy 对此有过清晰阐述](https://x.com/karpathy/status/1937902205765607626?ref=blog.langchain.com) ：

> 语境工程是一门精妙的艺术与科学，旨在为智能体行动轨迹的下一步精准填充恰到好处的上下文信息

## 语境工程方法

每个 Manus 会话都使用 [专属的云端虚拟机](https://e2b.dev/blog/how-manus-uses-e2b-to-provide-agents-with-virtual-computers) ，为智能体提供一个配备文件系统的虚拟计算机，使其能够在沙箱环境中使用文件导航工具并执行命令（例如预置实用程序和标准 Shell 指令）。

![](https://rlancemartin.github.io/assets/manus_sandbox.png)

在这片试验场中，Manus 运用三种核心策略进行语境工程，这些策略既与 Anthropic [此处所述](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) 的方法不谋而合，也 [贯穿于我经手的众多项目](https://docs.google.com/presentation/d/1Z-TFQpSpqtRqWcY-rBpf7D3vmI0rnMhbhbfv01duUrk/edit?usp=sharing) 之中：

- **Reduce Context**
- **Offload Context**
- **Isolate Context**

## Context Reduction

Manus 中的工具调用具有“完整”和“紧凑”两种呈现形式。完整版本包含工具调用的原始内容（例如完整的搜索结果），这些内容存储在沙箱环境（如文件系统）中。紧凑版本则存储对完整结果的引用（例如文件路径）。

![](https://rlancemartin.github.io/assets/manus_compaction.png)

Manus 对陈旧的工具结果应用压缩处理。具体做法是将完整的工具结果替换为压缩版本。这样，智能体在需要时仍能获取完整结果，同时通过移除已用于决策的"陈旧"结果来节省令牌消耗。

较新的工具结果会完整保留，以指导智能体做出 *下一步* 决策。这似乎是实现 *上下文精简* 的通用策略，我注意到这与 Anthropic 的 [上下文编辑](https://www.anthropic.com/news/context-management) 功能类似：

> 上下文编辑功能会在接近令牌限制时，自动清除上下文窗口中的陈旧工具调用和结果。当您的智能体执行任务并积累工具结果时，该功能会移除过时内容，同时保持对话流程的连贯性，从而有效延长智能体无需人工干预的运行时长。

当压缩效果趋于边际递减（见下图）时，Manus 会对执行轨迹进行摘要处理。摘要生成采用 *完整工具运行结果* ，并通过预定义架构规范摘要字段。这种机制能为任何智能体的执行轨迹生成结构统一的摘要对象。

![](https://rlancemartin.github.io/assets/manus_reduction.png)

## Context Isolation

Manus 对多智能体系统采取务实的态度，避免拟人化的分工模式。人类因认知局限而按角色（设计师、工程师、项目经理）组织协作，但 LLMs 未必受限于同样的约束。

有鉴于此，Manus 中子智能体的核心目标在于 *隔离上下文* 。例如，当出现待处理任务时，Manus 会将该任务分配给拥有独立上下文窗口的子智能体。

Manus 采用多智能体架构，其中规划器负责分配任务，知识管理器负责审阅对话并确定应保存至文件系统的内容，执行器子智能体则执行规划器分配的具体任务。

Manus 最初使用 `todo.md` 进行任务规划，但发现约三分之一的操作时间都耗费在更新待办清单上，浪费了宝贵的计算资源。随后他们转向采用专用规划代理，通过调用执行子代理来完成任务。

在最近的一期播客中，Anthropic 的多智能体研究员 Erik Schluntz 提到，他们 [同样采用规划器来设计多智能体系统](https://youtu.be/uhJJgc-0iTQ?si=VhuFOy9uf6rDc9ya&t=688) ，通过任务分配机制，以函数调用作为通信协议来启动子智能体。Erik 与 Cognition 公司的 Walden Yan 共同提出的核心挑战在于 [规划器与子智能体间的上下文共享](https://cognition.ai/blog/dont-build-multi-agents) 。

Manus 通过两种方式解决这一问题。对于简单任务（例如规划者 *仅需子智能体输出结果* 的独立任务），规划者只需创建指令并通过函数调用传递给子智能体。这种方式类似于 [Claude Code 的任务工具](https://claudelog.com/faqs/what-is-task-tool-in-claude-code/) 。

![](https://rlancemartin.github.io/assets/manus_isolation.png)

在处理更复杂的任务时（例如子代理需要写入规划器也在使用的文件），规划器会将其 *完整* 上下文共享给子代理。子代理仍保留自身的行为空间（工具）和指令，但会接收到规划器同样有权访问的 *完整* 上下文。

![](https://rlancemartin.github.io/assets/manus_isolation_share.png)

在这两种情况下，规划器都会定义子代理的输出模式。子代理配备 `提交结果` 工具，用于在向规划器返回结果前填充该模式，同时 Manus 采用约束解码技术确保输出内容严格遵循既定模式。

### Tools Definitions

我们常常希望智能体能够执行多种多样的操作。当然，我们可以为 LLM 绑定大量工具集合并提供详细的使用说明。但工具描述会消耗宝贵的 token 资源，且过多（常常存在重叠或歧义）的工具 [可能导致模型混乱](https://www.anthropic.com/news/context-management) 。

我注意到一个趋势：智能体倾向于使用 *少量* 通用工具 [来获得计算机操作权限](https://simonwillison.net/2025/Oct/16/claude-skills/#skills-depend-on-a-coding-environment) 。例如，仅凭一个 Bash 工具和几个文件系统访问工具，智能体就能执行广泛的操作！

马努斯将这一构想视为一个分层的行动空间，融合了函数/工具调用及其虚拟计算机沙箱功能。皮克曾提到，马努斯采用少量（少于 20 个）原子函数集，其中包括 Bash 工具、文件系统管理工具以及代码执行工具等。

与其臃肿地堆砌功能调用层，Manus 选择将大多数操作 *卸载* 到沙箱层。通过内置的 Bash 工具，Manus 可直接在沙箱中执行多种实用程序，而 [MCP 工具](https://modelcontextprotocol.io/docs/getting-started/intro) 则通过命令行界面暴露，智能体同样能借助 Bash 工具调用这些功能。

![](https://rlancemartin.github.io/assets/manus_offloading.png)

的 [技能](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) 功能采用了类似理念： [技能存储在文件系统中](https://simonwillison.net/2025/Oct/16/claude-skills/#skills-depend-on-a-coding-environment) 而非作为绑定工具存在，Claude 仅需通过少量简单函数调用（Bash、文件系统）即可逐步发现并运用这些技能。

> 渐进式呈现是使智能体技能具备灵活性与可扩展性的核心设计原则。正如一本编排精良的手册，从目录概览到具体章节，再到详细附录，技能允许 Claude 按需加载信息——拥有文件系统和代码执行工具的智能体在处理特定任务时，无需将整个技能内容全部载入其上下文窗口。

### Tool Results

由于 Manus 能够访问文件系统，它还能 *卸载* 上下文（例如工具执行结果）。如前所述，这对上下文精简至关重要：工具结果被卸载至文件系统以生成简洁版本，并用于从智能体上下文窗口中清理过期令牌。与 Claude Code 类似，Manus 通过基础工具（如 `glob` 和 `grep` ）实现文件系统检索，无需依赖索引（如向量数据库）。

## Model Choice

Manus 并不固守单一模型，而是采用任务级路由策略：可能使用 Claude 处理编程任务，Gemini 应对多模态需求，OpenAI 则负责数学推理。总体而言，Manus 的模型选择机制主要由成本考量驱动， [其中 KV 缓存效率起着核心作用](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) 。

Manus 采用缓存机制（例如用于存储系统指令、过往工具结果等），以降低多轮代理交互中的成本与延迟。Peak 指出，分布式键值缓存基础设施在开源模型中实施颇具挑战，但 [前沿模型供应商能提供完善支持](https://www.anthropic.com/news/prompt-caching) 。这种缓存支持使得前沿模型在实际应用场景（如代理任务）中具备更优的成本效益。

## 铭记苦涩教训而构建

我们以讨论 [“苦涩的教训”](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) 作为对话收尾。我一直对 [其在人工智能工程领域的启示](https://rlancemartin.github.io/2025/07/30/bitter_lesson/) 深感兴趣。鲍里斯·切尔尼（Claude Code 创始人）提到， [《苦涩的教训》](https://www.youtube.com/watch?v=Lue8K2jqfKk) 促使他决定保持 Claude Code 的中立性设计理念，使其能更灵活地适配模型迭代升级。

基于不断优化的模型意味着要接受持续的变化。Peak 提到，Manus 自三月份推出以来已经进行了五次重构！

此外，皮克警告称，随着模型不断进步，智能体的约束机制可能成为性能瓶颈——这正是"苦涩教训"所指出的核心挑战。我们为提升即时性能而增设的结构框架，在算力（模型）持续增长时反而可能制约其发展潜力。

为防止这种情况，皮克建议在不同模型强度下运行智能体评估。如果性能未随模型增强而提升，则可能是测试框架限制了智能体能力。这种方法有助于检验测试框架是否具备"未来适应性"。

郑亨元（OpenAI/MSL）关于此主题的 [演讲](https://youtu.be/orDKvo8h71o?si=fsZesZuP25BU6SqZ) 进一步强调，随着模型不断进步，需要持续重新评估结构（例如你的测试框架/假设）。

> *根据当前可用的计算能力和数据水平，添加必要的结构。随后移除这些结构，因为这些捷径会阻碍进一步的改进。*

![](https://rlancemartin.github.io/assets/bitter_lesson_timeline.png)

## Conclusions

赋予智能体访问计算机（如文件系统、终端、实用工具）的权限，是我们在 众多智能体 （包括 Manus）中常见的模式。这种能力催生了几种情境工程策略：

**1\. Offload Context**

- **外部存储工具结果** ：将完整工具结果保存至文件系统（不存入上下文），并通过 `glob` 、 `grep` 等工具按需调用
- **推送操作至沙箱** ：利用少量函数调用（Bash、文件系统访问）在沙箱中执行多种实用程序，而非将每个实用程序都绑定为工具

**2\. Reduce Context**

- **压缩陈旧结果** ：当上下文填满时，用引用（如文件路径）替换较早的工具结果；保留近期完整结果以指导后续决策
- **必要时进行总结** ：当压缩效果达到边际递减时，对完整轨迹采用基于模式的总结方法

**3\. Isolate Context**

- **为独立任务启用子代理** ：将任务分配给拥有独立上下文窗口的子代理，主要目的是实现上下文隔离（而非按角色分工）
- **有意识地共享上下文** ：简单任务仅传递指令；复杂任务需传递完整上下文（如执行轨迹和共享文件系统），以便子代理获取更多背景信息

最后一点需要考虑的是，确保你的测试框架不会随着模型性能提升而成为限制因素（例如要"吸取苦涩教训"）。通过在不同性能等级的模型上进行测试来验证这一点。简单、不预设倾向的设计通常能更好地适应模型的改进。最后，不要害怕随着模型进步而重构你的智能体（Manus 自 3 月以来已重构了 5 次）！