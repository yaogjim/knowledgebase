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

许多代理系统每次运行都从零开始，系统及其代理会发现相同的上下文、调用相同的工具、犯同样的错误，每次都是如此。这不仅效率低下，还严重限制了代理系统的能力上限。

最直接的解决办法是在系统中附加某种记忆，存储一切内容，通过向量相似度进行检索，然后期望最好的结果。 但简单的内存实现会产生自身的问题，比如上下文膨胀、过时信息污染新执行、智能体产生幻觉，最终你只是用一个问题换了一个更糟的问题。

我们亲身经历了这一切，CrewAI 处理数十亿的智能体执行，我们看到了将记忆视为存储问题时会发生什么，也看到了不将其视为存储问题时会发生什么。

因此，我们从头重建了整个记忆系统，专注于真正支持生产级别的 agentic 系统。它并非作为一个带有搜索层的数据库，而是作为一种认知过程，能够进行选择性编码、解决自身矛盾、有意遗忘，并知道自己何时无知。我们有机会将 LanceDB 用作该实现背后的数据库，这也带来了诸多令人惊喜的特性——设置极其简便、运行速度极快，且极具前沿性。

以下是我们构建它的方法以及如何使用它。

# 为什么朴素记忆会使情况更糟

市场对无状态智能体的回应是通过附加“内存即服务”的方式，存储一切、嵌入数据并按相似度检索。有些方法实现得很简洁，而另一些方法仅提供带有命名空间的键值存储，其余部分由用户自行处理。

更复杂的方案构建时间知识图谱，以跟踪事实何时发生变化，所有这些都是令人印象深刻的基础设施，但仍然只是基础设施。

这种模式在各处都一样：记忆被视为一个存储和检索问题。开发者负责决定哪些值得记住、如何组织这些记忆、何时检索结果足够有信心从而采取行动，以及当两个记忆相互矛盾时该怎么做。你的智能体周一学到一件事，周五又学到另一件相互矛盾的事。现在它两者都记住了。

并且他们中没有人提出真正重要的问题：检索是否有足够的信心去采取行动？他们都返回结果，但没有人说“我不确定，让我再深入看看。”

这就是当你把记忆当作数据而非认知时，大规模发生的情况。

# 记忆是认知，而非存储

人类记忆并非通过存储一切并按相似性检索来工作，而是选择性地进行编码，确定哪些信息重要以及它在何处适用；它会进行巩固，解决你之前知道的内容和刚刚学到的内容之间的冲突。它会适应性地检索信息，有时能立即提取，有时则需要逐步梳理已有的信息来完成检索。并且它会遗忘，这并非偶然，而是因为遗忘本身正是使记忆保持有用性的原因。

如果你仔细想想，记忆本身与 Agentic 系统非常相似，这正是我们遵循的模型。CrewAI 的新认知记忆系统围绕五个认知操作构建：编码、巩固、回忆、提取和遗忘。每一个都是主动过程，而非被动的读写操作。因此，当你存储记忆时，系统会分析其内容、分配重要性、检测矛盾，并将其置于自组织的层级结构中。当你检索时，系统会评估自身的置信度，并决定是否深入检索。

结果是五种方法。以下是完整的 API。

# CrewAI 的新认知记忆

CrewAI 的新认知记忆本身就是一个代理系统，在幕后使用 CrewAI Flows，完全从头构建。它在你的所有代理系统中都可用：

- 你可以在单个 Agent 上使用它。
- 在 Crew 中开启它，所有代理将自动加载并跨任务持久化记忆，但在上下文相关时，它们也可以主动记忆和调用记忆作为工具。
- 在 Flow 中使用它，你会得到一个补充状态的持久化层，其中状态处理一次运行中短暂存在的内容，而记忆处理应该在多次运行中累积的内容。

该实现的另一个亮点是，你可以随身携带它，让不同的代理访问相同的记忆，同时对如何检索记忆有不同的设置——通过为参与检索的组件设置不同的权重，比如记忆的半衰期等。

原生实现采用了极其简单的 DSL 实现，以常规的 CrewAI 方式，因此这五项认知操作对应于五个方法：

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

每个方法触发它自己的认知流程。

remember()不仅仅是存储，它还会分析你正在保存的内容，检测与已有知识的矛盾，并解决这些矛盾。

recall()不仅仅是搜索，它会评估自己的置信度，并且在不确定时会进一步深入。

内存系统本身具有自主性，每一个操作都是一个推理过程，而非读或写。

在 Crew 中，这是一行：

```python
crew = Crew(
 agents=[researcher,  analyst],
 tasks=[...], 
 memory=True
)
```

智能体在每项任务之前加载相关上下文，并在之后持久化它们学到的内容。智能体还可以将“记忆”和“回忆”作为工具，由智能体自身决定什么内容值得存储，或者何时需要过往上下文。系统默认处理持久化，当智能体认为自己能做得更好时，由其接管。

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

你停止对那些本应只需记住的事物过度设计状态。 把状态看作是当下重要的事物，而记忆是下次重要的事物。

现在让我们看看内部实际发生的情况。

# 内存内部剖析：两种认知流

驱动这个认知记忆的主要智能体系统有两个：编码流程（Encoding Flow）和回忆流程（Recall Flow）。

## 编码智能体系统

当你调用 remember() 时，CrewAI Flow 会运行一个编码管道，该管道分析内容并生成 MemoryAnalysis：

```python
class MemoryAnalysis(BaseModel):
 scope: str # Where this belongs in the hierarchy
 categories: list  # What this is about
 importance: float  # How much this matters (0-1)
```

该系统决定记忆的归属、主题和重要性，所有这些都无需你进行任何指定。没有预先设计的模式，其结构实际上由系统自身涌现。当你需要控制权时，你可以覆盖范围、类别和重要性。

每次调用 remember() 方法时，还会触发对现有记忆的相似度搜索，这类似于人类在学习新事物时的做法——他们会找到方式将新事物聚类，甚至能基于这些信息推断出新的内容。

讲解示例：

你上个月记录了“我们使用 PostgreSQL 作为用户数据库”。现在你记录了“我们上周迁移到 MySQL”。

在其他系统中，两者并存，而检索结果则完全随机。在认知记忆中，整合逻辑会检测相似性、识别矛盾并生成一个计划：更新旧记录的内容、保留迁移上下文、删除过时的事实，从而得到一个连贯的记忆，而非两个相互冲突的记忆。

在 CrewAI 的记忆系统中，编码流程中的整合步骤会检测相似度、识别矛盾，并生成一个计划：更新旧记录的内容、保留迁移上下文、删除过时事实，最终得到一个连贯的记忆，而非两个相互冲突的记忆。

## 记忆唤起自主代理系统

Recall Flow 能做其他系统做不到的两件事：它根据真正重要的因素对结果进行评分，并且知道何时进行更深入的搜索。

复合评分融合了三个信号而非单一的一个，即相似度、时效性和重要性，并为每个信号分配特定权重（您也可以在内存的访问层完全控制自定义这些权重，同时内存本身保持不变）

```text
score = (similarity × w_sim) + (recency × w_rec) + (importance × w_imp)
```

这就是为什么六个月前的关键架构决策比昨天恰好提到“数据库”的琐碎记录优先级更高。纯向量搜索只会返回那个琐碎记录。但认知复合评分会返回该决策。

它分析查询，选择要搜索的范围，检索候选结果，然后评估自身的置信度。如果需要，它会进行更深入的搜索，拓宽搜索范围，并尝试不同的策略，在此过程中，它会跟踪缺失的内容作为证据缺口。

# 原子记忆

智能体不会以纯粹的、独立的事实来思考，比如研究智能体返回一份 500 字的摘要，而分析师会生成一份涵盖六个主题的报告。如果你将其中任何内容存储为一个记忆，就会回到“blob 问题”（即大杂烩问题）——检索时会把所有内容都调出来，而你只需要一个事实，并且整合无法解决段落中隐藏的矛盾。

作为我们新的认知记忆的一部分，系统能够从 agentic 执行过程和更大文本块中提取记忆，extract\_memories() 函数将原始输出分解为自包含的原子事实：

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

在上述示例中，每个提取的事实独立进入完整的认知流程。数据库推荐在 /infrastructure/database 路径下以高重要性进行编码，而合规要求在 /compliance 路径下有自己的范围。因此，当您后续存储“We're switching to MySQL”时，合并过程会专门针对 PostgreSQL 推荐进行解决，而非针对同时提及成本估算和团队偏好的信息块。

这也是驱动 Crews 中自动记忆功能的核心。当代理以 memory=True 完成任务时，系统会对输出进行提取，将其分解为原子事实，并将每个事实通过编码和巩固处理。你只需设置一个标志，系统就会为你处理所有事情。

## 这解锁了什么

真正的转变不是你的智能体记住事情，而是你的智能体系统能够复合。

没有记忆时，每次运行都是独立的，大致相同的成本、相同的延迟、相同的发现过程和相同的上限；但使用认知记忆后，每次运行都会让下一次运行变得更好。处理过一千个客户工单的智能体不只是拥有一千条记忆，它整合了模式、解决了矛盾，并构建了重要性层级，因此第1001次运行与第1次运行从根本上不同，它更快、更便宜、更可靠，因为系统已经学习并进化了。

这也极大地改变了你能构建的内容：

人在回路系统，从修正中学习。 带有 @human\_feedback(learn=True) 不仅仅是收集审批，而是将每一处修正提炼为可泛化的经验并存储在记忆中。下一次运行时，系统会在人类看到输出之前回忆起这些经验并加以应用。过去每次都要重写草稿的审核者现在只需批准，因为系统已经学会了他们关心的内容。

积累专业知识的研究系统。 每周运行的研究流程不会每次都从零开始，它会回顾之前的发现，识别已发生的变化，关注变化部分（delta），经过几次执行后，它不再进行研究，而是在维护一个随着每个循环变得更加完善的动态知识库。

多智能体团队拥有共享理解。智能体共享记忆但回忆方式不同，规划智能体重视重要性，而执行智能体重视时效性，因此你会发现自己拥有相同的知识，但能够通过不同的视角来运用这些知识。就像一个团队，其中架构师记得原则，而工程师记得上一个迭代中交付的内容。

从执行转向探索的系统。 这可能是最大的突破：无状态代理只能执行，即接收输入、产生输出。具有认知记忆的代理可以探索，尝试一种方法，记住哪些方法有效，并在下一次运行时进行优化。它们会制定策略，并且变得越来越擅长自我提升。

每一个在这篇文章中描述的认知操作——编码、巩固、自适应回忆——本身就是一个 CrewAI Flow。这个记忆系统是一个代理系统，构建在你用来构建自己系统的同一平台上。能够使用我们自己的产品来构建我们自己的产品，这真是太棒了，这证明了该架构在问题足够困难到需要它时是可靠的。

## 自己试试！

这已经作为 alpha 版本可用 1.10.1 就像这样简单：

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