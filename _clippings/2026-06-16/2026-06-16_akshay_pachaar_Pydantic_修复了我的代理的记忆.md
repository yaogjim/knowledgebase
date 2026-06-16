---
title: "2026-06-16_akshay_pachaar_Pydantic_修复了我的代理的记忆"
source: "https://x.com/akshay_pachaar/status/2058976178908885210"
author:
  - "[[@akshay_pachaar]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "x"
  - "@akshay_pachaar"
  - "project"
  - "https"
---

# Pydantic 修复了我的代理的记忆

**Akshay**

# Pydantic 修复了我的代理的记忆

你的代理记住一切，却什么都不理解。

智能体记忆始于向量数据库。将事实分块存储，通过相似度检索。

它一直有效，直到查询需要跨块连接事实。然后它就失效了。问题不在于相似度，而在于结构。

知识图谱就是解决方案。实体作为节点，关系作为边，采用遍历而非匹配。

但是大多数团队都会遇到不同的障碍。

当你给一个智能体一个用于记忆的知识图谱时，默认行为是处理提取的 LLM 自主决定结构。

它选取实体类型、关系标签和属性。

结果是通用的。

例如，你正在构建一个客户支持代理。你向它提供50条支持对话，这些对话涵盖客户、工单、功能和升级历史。

您询问：“哪些企业客户有未关闭的 sev-1 工单？”

The graph has the data. But every support ticket is stored as a “Topic” node. Every customer is an “Object.” Every relationship is “RELATES\_TO.”

There’s no way to filter by type, severity, or plan tier. The query returns noise.

The agent didn’t forget anything. Nobody told it what to pay attention to.

![Image](https://pbs.twimg.com/media/HJKtp0JaAAA0zu9?format=jpg&name=large)

修复方法很简单： 预先定义模式。 告诉提取模型在你的领域中存在哪些类型的实体、哪些关系是有效的，以及每个实体包含哪些属性。

那个组织蓝图被称为本体 。可以把它看作是你的智能体大脑的模式 。

让我们了解一下为什么这很重要，没有它会出什么问题，以及如何使用它它一个

[100%开源的解决方案](https://github.com/getzep/graphiti) 。

# Why flat retrieval breaks on multi-hop reasoning

Vector-based memory stores facts as text chunks and retrieves them by semantic similarity. That works until a query requires connecting facts that don’t appear in the same chunk.

Consider three facts stored about a project.

- Alice manages Project Atlas
- Project Atlas runs on PostgreSQL
- The PostgreSQL cluster went down Tuesday

A query like “was Alice’s project affected by Tuesday’s outage” needs all three.

![Image](https://pbs.twimg.com/media/HJKu6QBaYAAINyy?format=jpg&name=large)

Vector search will retrieve just facts 1 and 3 because both mention relevant terms. Fact 2 is the bridge connecting Alice to PostgreSQL through Project Atlas, but it mentions neither Alice nor Tuesday. Similarity search misses it.

A knowledge graph stores entities as nodes and relationships as edges. Instead of matching text, it traverses connections.

That chain (Alice → manages → Project Atlas → runs on → PostgreSQL) is what makes multi-hop reasoning work, and it is invisible to flat vector retrieval.

# The memory pipeline and where extraction fits

Every graph-based agent memory system follows a common pipeline:

1.  数据摄入: 原始数据进入(对话消息、文档、JSON 业务数据)
2.  提取： 一个 LLM 读取原始数据，并确定存在哪些实体、哪些关系连接这些实体，以及哪些属性是重要的
3.  存储： 提取的实体成为节点，关系成为边，所有这些都持久化在图中
4.  检索： 在查询时，系统搜索图并整合相关事实
5.  交付： 检索到的事实被格式化为一个上下文块并注入到代理的提示中

The extraction step is where everything is decided. It determines what your graph contains, how it’s structured, and what’s queryable downstream.

![Image](https://pbs.twimg.com/media/HJKu_uTbUAAtvP6?format=jpg&name=large)

Here’s the problem. In most frameworks, this step is a black box. You pass in text, an LLM pulls out “entities” and “relationships,” and you get nodes and edges. The LLM decides the types, the labels, the attributes on its own.

You have zero control over what it classifies or how.

Let's understand how to fix it.

# 

[Defining the schema with Pydantic](https://github.com/getzep/graphiti)

The fix is the same pattern used everywhere in the AI stack.

- FastAPI endpoints get Pydantic response models.
- Function calling tools get Pydantic schemas.
- Agent memory works the same way in Zep.

Define custom entity types using EntityModel (a subclass of Pydantic’s BaseModel) with EntityText fields and descriptions that guide the extraction model.

```python
from zep_cloud.external_clients.ontology import EntityModel, EntityText
from pydantic import Field

class Project(EntityModel):
 """
 Represents a specific software project, application, 
 or codebase that the user is building or contributing to.
 """

 project_status: EntityText = Field(
 description="Current status: active, completed, paused, or archived.",
 )
 project_type: EntityText = Field(
 description="Type of project: web app, mobile app, API, CLI tool, etc.",
 )
```

The docstrings and field descriptions are important here because good descriptions with concrete examples give the extractor enough signal to classify accurately.

The Pydantic descriptions above aren’t just classification instructions. They teach the extractor vocabulary it doesn’t know.

A Technology entity follows the same pattern.

```python
class Technology(EntityModel):
 """
 Represents a programming language, framework, library, 
 database, or tool that the user works with.
 """

 tech_category: EntityText = Field(
 description="Category: programming language, framework, database, etc.",
 )
```

Edge types use EdgeModel and carry their own attributes.

```python
from zep_cloud.external_clients.ontology import EdgeModel

class WorksOn(EdgeModel):
 """The user is currently working on, building, or contributing to a project."""
 role: EntityText = Field(
 description="User's role: lead developer, contributor, maintainer, etc.",
 )

class UsesTechnology(EdgeModel):
 """The user actively uses or works with a specific technology."""
 proficiency: EntityText = Field(
 description="Proficiency level: beginner, intermediate, advanced, or expert.",
 )
```

Finally, wire these into the graph with source/target constraints using EntityEdgeSourceTarget, which defines which entity types can connect through which edge types:

```python
from zep_cloud import EntityEdgeSourceTarget

client.graph.set_ontology(
 entities={"Project": Project, "Technology": Technology},
 edges={
 "WORKS_ON": (
 WorksOn,
 [EntityEdgeSourceTarget(source="User", target="Project")],
 ),
 "USES_TECHNOLOGY": (
 UsesTechnology,
 [EntityEdgeSourceTarget(source="User", target="Technology")],
 ),
 },
)
```

The code enforces that

- WORKS\_ON can only connect a User to a Project
- USES\_TECHNOLOGY can only connect a User to a Technology.
- Any relationship that doesn't match these constraints won't produce a typed edge.

To summarise, this is what we’ve got so far:

![Image](https://pbs.twimg.com/media/HJKwmn9a4AAv9DP?format=jpg&name=large)

# What happens under the hood

When a conversation is ingested with a schema active, Zep’s extraction pipeline runs five steps:

1.  实体抽取识别文本中的命名实体
2.  实体解析合并重复项（”Nexus”和“the Nexus 项目”合并为一个节点）
3.  事实抽取 识别关系并将它们作为带类型的边输出
4.  事实解析检测矛盾并使过时事实失效（保留历史）
5.  时间提取解析时间引用并将它们映射到每个边缘的有效性窗口

[![视频](https://pbs.twimg.com/tweet_video_thumb/HJKyJvDakAA1jt8.jpg)](https://x.com/akshay_pachaar/status/2058976178908885210)[![视频](https://pbs.twimg.com/tweet_video_thumb/HJKyJvDakAA1jt8.jpg)](https://x.com/akshay_pachaar/status/2058976178908885210)

Your pydantic schema guides steps 1 and 3. Entity types tell the extractor what to look for. Edge types with their constraints tell it what relationships to classify. Resolution and temporal processing happen automatically.

# Practical walkthrough of how it looks

We ingest a conversation where a developer named Alex discusses their work (an active web app called Nexus, their tech stack, proficiency levels):

![Image](https://pbs.twimg.com/media/HJKw-WEbsAAFsIL?format=jpg&name=large)

Querying for Project nodes returns Nexus with populated project\_status and project\_type attributes.

![Image](https://pbs.twimg.com/media/HJKxDS3aQAA4y2G?format=jpg&name=large)

The node isn’t a generic “Topic” or “Object.” It’s a Project with structured fields as defined in the schema.

The edges are typed too.

- WORKS\_ON carries role: lead developer

![Image](https://pbs.twimg.com/media/HJKxGAibMAA6XE-?format=jpg&name=large)

- USES\_TECHNOLOGY carries proficiency: advanced for Python and Docker, proficiency: intermediate for TypeScript.

![Image](https://pbs.twimg.com/media/HJKxJ56bEAAfcUz?format=jpg&name=large)

This can now filter projects by status, technologies by category, and query “which active projects use PostgreSQL” with a precise answer.

# Context templates

The final piece is context templates, which assemble typed facts into a prompt-ready block.

You can define which edge types and entity types to include, and Zep formats them with temporal annotations into a single string injected into the agent’s prompt.

```python
client.context.create_context_template(
 template_id="dev-context",
 template="""# PROJECTS
%{edges types=[WORKS_ON] limit=5}

# TECH STACK
%{edges types=[USES_TECHNOLOGY] limit=10}

# PROJECT DETAILS
%{entities types=[Project] limit=5}

# TECHNOLOGIES
%{entities types=[Technology] limit=10}""",
)
```

It looks like this:

![Image](https://pbs.twimg.com/media/HJKxWNMacAET_un?format=jpg&name=large)

Every entry in the resulting context block is typed, temporally annotated, and carries the attributes defined. Save the template once, reference it by ID in agent calls.

# The 10/10/10 constraint and schema as a reasoning boundary

Zep enforces a hard limit of 10 custom entity types, 10 custom edge types, and 10 fields per type.

![Image](https://pbs.twimg.com/media/HJKxcHNboAEfD0H?format=jpg&name=large)

That’s intentional to force a dev to think about what matters in a domain rather than modeling everything.

The source/target constraints also act as guardrails on what an agent is allowed to remember. If a schema doesn’t include an edge type connecting Project to Competitor, the extraction model won’t create that relationship, even if a conversation mentions both.

The schema defines the space of valid memories.

This is the same principle behind typed function calling, where we constrain the LLM’s output space so that it can’t produce invalid arguments. Memory schemas apply that same constraint to what the agent stores.

Start with 3-4 entity types and 3-4 edge types that capture 80% of your domain logic, and add complexity incrementally.

* * *

Agent memory without schema discipline is a graph that behaves like a vector store.

In a way, you pay the cost of graph construction without getting the benefit of structured retrieval.

The schema is how you get that benefit back, and the fact that it’s Pydantic means there’s nothing new to learn.

This is especially true for domain-specific applications. LLM extraction works reasonably well on general knowledge, but the moment your domain has internal terminology, product names that collide with common words, or jargon absent from the training data, unguided extraction produces nonsense. The schema closes that gap. It carries the domain vocabulary directly into the extraction step, so the LLM doesn't need to have seen your terminology before. It just needs the definitions you wrote.

![Image](https://pbs.twimg.com/media/HJK0eA6bIAAfZ8w?format=jpg&name=large)

[你可以在这里找到 Zep 的 GitHub 仓库→](https://github.com/getzep/graphiti) (别忘了给它加星标 🌟)

Thanks for reading!

* * *

### 热门回复

**@darkzodchi** ♥ 7.5K · 💬 146

Anthropic 工程师

你不应该看着 Claude Code 工作。你应该醒来并检查它交付的内容。

22分钟内，她通过直播镜头实时构建了整个工作流程。

大多数人关闭他们的终端，一切都停止了。

此设置在您持续运输

**@Asteri** ♥ 3.8K · 💬 130

Karpathy 找到了一种减少 token 消耗 90%的方法

问题在于 LLM 会反复阅读相同的文件，在文档之间丢失上下文，因此提供的答案不够准确

该解决方案被称为 Wiki Layer，其中 LLM 进行清洗、结构化处理，并且

**@Rohit** ♥ 455 · 💬 44

两个月前，我写了《The Harness Is Everything》，获得了 130 万次浏览。

上周的 Life-Harness 论文：126 个模型环境设置中有 116 个仅通过修补 harness 就得到了改善。

模型已冻结。18个骨干模型的平均提升为88.5%。

↓ Claude Code 和 Codex 实际上是如何工作的

**@francesco rosciano** ♥ 14 · 💬 3

412ms median first-token latency.

Voice AI that feels real-time. Open-source SDK.

**@Sergei Babichev** ♥ 2 · 💬 1

谢谢，这个非常有用。我正在研究长期智能体记忆，而“本体论约束记忆”正是我从这里获得的缺失的抽象概念。