---
title: "2026-03-06_Jo_o_Moura_Jo_o_Moura_我们如何构建面向智能体系统的认知记忆_许多代理系统每次运行都从零开"
source: "https://x.com/joaomdmoura/status/2029625327778156682"
author:
  - "[[@João Moura]]"
published: 2026-03-06
created: 2026-03-06
description:
tags:
  - "x"
  - "@João Moura"
  - "memory"
  - "crewai"
---

# João Moura # 我们如何构建面向智能体系统的认知记忆 许多代理系统每次运行都从零开

**João Moura**

# 我们如何构建面向智能体系统的认知记忆

许多代理系统每次运行都从零开始，系统及其代理发现相同的上下文、调用相同的工具、犯同样的错误，每次都是如此。这不仅效率低下，还会给代理系统的能力设置一个巨大的上限。

明显的解决方案是在系统中加装某种存储器，存储所有内容，通过向量相似度进行检索，寄希望于最好的结果。 但朴素的内存实现会带来自身的问题，比如上下文膨胀、过时信息污染新的执行过程、智能体产生幻觉，最终你只是用一个问题换来了更糟的问题。

我们经历了这一切，CrewAI 处理数十亿代理式执行，我们看到了将内存视为存储问题时会发生什么，也看到了不将其视为存储问题时会发生什么。

因此，我们从头开始重建整个记忆系统，专注于真正支持生产环境中的智能代理系统。它不是一个带搜索层的数据库，而是一个认知过程，能够进行选择性编码、解决自身矛盾、有意遗忘，并且知道自己何时无知。在此次实现中，我们有机会使用 LanceDB 作为底层数据库，而这一选择也带来了诸多惊喜，包括设置极其简单、运行速度快以及非常前沿。

以下是我们构建它的方法以及如何使用它。

# 为什么朴素记忆会使情况更糟

市场对无状态代理的应对方式是附加内存即服务（MaaS），存储一切、嵌入内存、并基于相似度检索。有些方法实现得很简洁，另一些方案则提供带命名空间的键值存储，并将其余部分留给用户自行处理。

更复杂的选项构建时间知识图谱，以追踪事实何时发生变化，所有这些都是令人印象深刻的基础设施，但本质上仍然是基础设施。

模式无处不在：记忆被视为一个存储和检索的问题。开发者负责决定什么值得记忆、如何组织记忆、何时检索结果足够确定以采取行动，以及当两个记忆相互矛盾时该如何处理。你的智能体周一学到一件事，周五又学到一件相互矛盾的事。现在它两者都记住了。

而且他们中没有一个人提出真正重要的问题：检索是否有足够的信心采取行动？他们都会返回结果，但没有一个人说“我不确定，让我再深入看看。”

当你将内存视为数据而非认知时，在大规模场景下就会出现这样的情况。

# 记忆是认知，而非存储

人类记忆并非通过存储一切并按相似性检索来运作，而是有选择性地进行编码，决定哪些内容重要以及将其放置在何处；它会进行整合，解决你之前已知的内容与刚刚学到的内容之间的冲突。它会适应性地检索信息，有时即时完成，有时则通过逐步梳理已知内容来进行。并且，记忆的遗忘并非偶然，而是因为遗忘才使记忆保持有用性。

如果你仔细想想，记忆本身与自主代理系统（Agentic System）非常相似，这也是我们遵循的模型。CrewAI 的新认知记忆系统围绕五个认知操作构建：编码、巩固、回忆、提取和遗忘。每一个操作都是主动过程，而非被动的读取或写入。因此，当你存储记忆时，系统会分析内容、分配重要性、检测矛盾，并将其置于自组织的层级结构中。当你检索时，系统会评估自身的置信度，并决定是否深入。

结果是五种方法。以下是完整的 API。

# CrewAI 的新认知记忆

CrewAI 的新认知记忆本身就是一个代理型系统，其背后利用 CrewAI Flows，完全自启动。它在你的所有代理系统中都可用：

- 你可以在单个 Agent 上使用它。
- 在 Crew 中开启它后，所有代理将自动加载并跨任务持久化记忆，但在上下文相关的情况下，它们也可以主动记忆和回忆，作为工具使用。
- 在 Flow 中使用它，你会得到一个补充状态的持久化层，其中状态负责处理运行期间短暂存在的内容，而内存负责处理需要跨运行累积的内容。

另一个很酷的实现细节是，你可以随身携带它，让不同的智能体访问相同的记忆，同时对如何回忆记忆有不同的设置，通过为参与回忆的组件（比如记忆的半衰期等）设置不同的权重。

原生实现带有极其简单的 DSL 实现，以常规的 CrewAI 方式，因此这五项认知操作对应于五个方法：

```python
from crewai.memory import Memory
# New Coginitive Memory Class
memory = Memory ()

# Adding new memories directly
memory, remember("We decided to use PostgreSQL for the user database.")

# Recalling memories directly
results = memory.recall("What database are we using?")

# Extracting memorable facts from a string
facts = memory.extract_memories("Long text with many possible facts")

# Getting the memory tree
memory.tree()

# Forget certain memories
from datetime import datetime, timedelta
memory.forget(scope="/", older_than=datetime.utcnow() - timedelta(days=30))
```

每个方法触发它自己的认知流水线。

remember()不仅仅是存储，它还会分析你正在保存的内容，检测与它已有的知识相矛盾的地方，并解决这些矛盾。

recall() 不只是搜索，它会评估自身的置信度，当不确定时会深入挖掘。

内存系统本身是自主的，每一个操作都是一个推理过程，而不是读或写。

在一个 Crew 中，它是一行：

```python
crew = Crew(
 agents=[researcher,  analyst],
 tasks=[...], 
 memory=True
)
```

代理在每个任务前加载相关上下文，并在之后持久化它们学到的内容。它们也可以将“记忆”和“调用”作为工具，代理自身决定何时值得存储某些信息，或者何时需要过往上下文。系统默认处理持久化，当代理认为自己更了解时则接手处理。

在流程中：

```python
class ResearchFlow(Flow):

 @start ()
 def research(self):
 past = self.recall("previous findings on this topic")
 self. remember(f"Found: {findings}", scope="/research")

 @listen (research)
 def analyze(self):
 context = self.recall("all research findings")
```

你停止对本应只需记住的事情进行过度状态设计。 状态用于当前关键事项，而内存用于下次关键事项。

现在让我们看看内部实际发生的事情。

# 在记忆之罩下：两种认知流

驱动这个认知记忆的主要有2个代理系统：编码流和检索流。

## 编码能动系统

当你调用 remember() 时，CrewAI Flow 会运行一个编码管道，该管道会分析内容并生成 MemoryAnalysis：

```python
class MemoryAnalysis(BaseModel):
 scope: str # Where this belongs in the hierarchy
 categories: list  # What this is about
 importance: float  # How much this matters (0-1)
```

系统会决定记忆属于哪里、内容是什么以及重要性如何，全程无需你进行任何指定。无需预先设计架构，其结构实际上是由系统自身生成的。当你需要控制权时，可以覆盖范围、类别和重要性。

每次调用 remember() 方法也会触发对现有记忆的相似度搜索，这类似于人类在学习新事物时将信息聚类并基于这些信息推断新内容的方式。

演示示例：

你上个月保存了“我们使用 PostgreSQL 作为用户数据库”。现在你正在保存“我们上周迁移到了 MySQL”。

在其他系统中，两者并存且检索结果全凭运气。在认知记忆中，整合逻辑会检测相似性、识别矛盾并生成一个方案：更新旧记录的内容、保留迁移上下文、删除过时事实，从而得到一个连贯的记忆，而非两个相互冲突的记忆。

在 CrewAI 的记忆中，编码流程中的合并步骤会检测相似性、识别矛盾，并生成一个计划：更新旧记录的内容、保留迁移上下文、删除陈旧事实，从而最终形成一个连贯的记忆，而非两个相互冲突的记忆。

## 记忆能动系统

Recall Flow 能做两件其他系统做不到的事：它根据真正重要的因素对结果进行评分，并且它知道何时需要进行更深入的搜索。

复合评分融合了三个信号而非单一的，即相似度、最近性和重要性，为每个信号应用特定的权重（你可以在内存的访问层完全控制对这些权重进行自定义，同时内存本身保持完整）

```text
score = (similarity × w_sim) + (recency × w_rec) + (importance × w_imp)
```

这就是为什么六个月前的一个关键架构决策比昨天恰好提到“数据库”的琐碎备注优先级更高。纯向量搜索只能检索到那个琐碎的备注，但认知复合评分会返回那个决策。

它分析查询，选择搜索范围，检索候选，然后评估自身置信度。必要时会进行更深入的搜索，扩大搜索范围，尝试不同策略，同时跟踪缺失的部分作为证据缺口。

# 原子记忆

代理不会以清晰、独立的事实为思考方式。比如，一个研究代理返回一份 500 字的摘要，同时分析师生成一份涵盖六个主题的报告。如果将这些内容中的任何一部分作为一个记忆存储，你就会回到“blob 问题”，即当你需要某个事实时，检索会把所有内容都调出来，而且整合无法解决段落中隐藏的矛盾。

作为我们新的认知记忆（Cognitive Memory）的一部分，我们能够从智能体执行过程和更大的文本块中提取记忆，extract\_memories() 将原始输出分解为自包含的原子事实：

```python
raw = """After reviewing the infrastructure options, the team
recommends PostgreSQL for the user database due to its JSONB
The compliance support. Estimated cost is $2,400/month on RDS.
The compliance team flagged that all user data must stay in EU regions.
DevOps prefers managed services over self-hosted to
reduce on-call burden."""

facts = memory.extract_memories(raw)
# → "Team recommends PostgreSQL for user database due to JSONB support"
# → "Estimated database cost is $2,400/month on RDS"
# → "Compliance requires all user data to remain in EU regions"
# → "Devops prefers managed services over self-hosted"
```

在上例中，每个提取的事实独立进入完整的认知流程。数据库推荐在 /infrastructure/database 路径下被编码为高重要性，而合规要求在 /compliance 路径下拥有其自身的范围。因此，当你后来存储“我们正在切换到 MySQL”时，整合过程专门针对 PostgreSQL 推荐进行解析，而非针对一个也提到成本估算和团队偏好的数据块（blob）。

这也是 Crews 中自动记忆功能的动力所在。当代理完成任务（设置 memory=True）时，系统会对输出结果执行提取操作，将其分解为原子事实，并对每个事实进行编码和整合处理。你只需设置一个标志，系统就会为你处理所有事情。

## 这解锁了什么

真正的转变不在于你的代理记住事情，而在于你的智能体系统能够复合。

没有记忆时，每次运行都是独立的，成本、延迟、发现过程和上限大致相同；但使用认知记忆时，每次运行都会让下一次运行更优。一个处理过一千个客户工单的智能体不只是拥有一千段记忆，它整合了模式、解决了矛盾、构建了关键事项的层级结构。因此第1001次运行与第1次运行本质上截然不同，它更快、成本更低、更可靠，因为系统已学习并进化。

这也极大地改变了你能构建的东西：

Human-in-the-loop systems that learn from corrections. A Flow with @human\_feedback(learn=True) doesn't just collect approvals, it distills each correction into a generalizable lesson and stores it in memory. Next run, the system recalls those lessons and applies them before the human even sees the output. The reviewer who used to rewrite every draft now just approves, because the system learned what they care about.

Research systems that accumulate expertise.A research Flow that runs weekly doesn't start from scratch each time, it recalls what it found before, identifies what's changed, and focuses on the delta and after a few executions, it's not doing research, it's maintaining a living knowledge base that gets more refined with every cycle. 研究系统，积累专业知识。 每周运行的研究流程不会每次从头开始，它会回顾之前的发现，识别变化，关注变化量，经过几次执行后，它不再进行研究，而是在维护一个动态知识库，该知识库会随着每个周期变得更加完善。

具有共同理解的多智能体团队。智能体共享记忆但回忆方式不同，规划型智能体重视重要性，执行型智能体重视最近性，因此你会发现自己拥有相同的知识，却能通过不同视角加以利用。就像一个团队，架构师记得原则，工程师记得上一个迭代周期交付的内容。

Systems that shift from execution to exploration. This is probably the biggest unlock: Stateless agents can only execute, given input, produce output. Agents with cognitive memory can explore, try an approach, remember what worked, refine on the next run. They develop strategies. They get better at getting better.

而本文中描述的每一项认知操作——编码、巩固、自适应回忆——本身都是一个 CrewAI Flow。记忆系统是一个基于智能体的系统，构建在你用来构建自己系统的同一平台上。我们能用自己的产品构建自己的产品，这真是太棒了，这证明了当问题足够复杂需要它时，该架构依然成立。

## 自己试试！

This is already available as an alpha version 1.10.1 as simple as:

```text
pip install crewai
```

然后你可以在 Python shell 中快速尝试使用一个单一的代理：

```python
from crewai import Agent

agent = Agent (
 role="Technical Advisor",
 goal="Help the team make infrastructure decisions"
 backstory="Senior engineer with deep knowledge of agentic systems",
 memory=True
)

agent.kickoff("what are the benefits of using CrewAI to build agentic systems?")
```

之后你实际上可以浏览所有由运行生成的记忆，在同一个目录中：

```text
crewai memory
```