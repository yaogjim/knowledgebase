---
title: "Context Engineering with Agents using LangGraph: A Guide for Modern AI Development | by Ankush k Singal | in AI Artistry - Freedium"
source: "https://freedium.cfd/https://medium.com/ai-artistry/context-engineering-with-agents-using-langgraph-a-guide-for-modern-ai-development-7434ffec3aa8"
author:
published:
created: 2025-07-07
description: "Ankush k Singal"
tags:
  - "clippings"
---
[< 返回原文](https://medium.com/ai-artistry/context-engineering-with-agents-using-langgraph-a-guide-for-modern-ai-development-7434ffec3aa8#bypass)

![Preview image](https://miro.medium.com/v2/resize:fit:700/1*XJjv3c4py09Spssj1VzmbA.jpeg)

## 使用 LangGraph 通过智能体进行上下文工程：现代人工智能开发指南

## 安库什·K·辛加尔[人工智能艺术](https://medium.com/ai-artistry "Your AI knowledge hub!")

无障碍模式 - 浅色 约5分钟阅读时长 · 2025年6月25日（更新：2025年6月25日） · 免费：否

#### 引言

随着大语言模型（LLMs）演变成通用的推理引擎，我们设计、引导和管理其行为的方式正在迅速改变。LLMs 不再局限于单轮提示，现在它已成为复杂的 **人工智能代理** 背后的认知引擎，这些代理系统能够进行自主推理、使用工具并执行长期任务。这个新时代让一个强大的概念成为焦点： **上下文工程** 。

上下文工程是管理大型语言模型（LLM）用于思考、行动和决策的信息的艺术与科学。就如同操作系统管理进入中央处理器（CPU）随机存取存储器（RAM）的数据一样，如今开发者必须确定哪些内容进入大型语言模型有限的上下文窗口。对于智能体而言，这一挑战变得更加关键且更加复杂。

在本文中，我们将剖析在人工智能代理时代上下文工程意味着什么、它为何重要，以及如何通过代码有效地实现它。

### 在我们开始之前！🦸🏻♀️

如果你喜欢这个话题并且想支持我：

1. 给我的文章鼓掌50次；那真的会帮到我。👏
2. 在 Medium 上关注我并订阅，即可免费获取我的最新文章🫶
3. 加入我们的大家庭——订阅 **[YouTube 频道](https://www.youtube.com/@andy111007)**
![None](https://miro.medium.com/v2/resize:fit:700/1*LZ0JeHfzubxmkjVU-HJ28g.png)

来源： [上下文工程](https://rlancemartin.github.io/2025/06/23/context_engineering/)

### 什么是上下文工程？

由人工智能从业者创造并得到 Anthropic 和 Cognition 的研究人员强调， **上下文工程** 是指在大语言模型（LLM）运行的任何给定时刻，对呈现给它的数据进行的策略性打包和管理。这包括：

- **提示：** 用户指令或系统消息。
- **检索到的内容：** 实时提取的文档或事实。
- **工具输出：** 来自 API 或函数调用的响应。

安德烈·卡帕西（Andrej Karpathy）将大语言模型（LLMs）比作一种新型的中央处理器（CPU），其中上下文窗口（context window）的功能类似于随机存取存储器（RAM）。由于这种“工作内存”是有限的——通常限制在数万或数十万个词元——有效的上下文工程对于性能、成本效益和任务成功至关重要。

#### 为何上下文工程对智能体至关重要

与简单的聊天机器人不同，人工智能代理可在长时间会话、多次工具调用和动态工作流程中运行。它们旨在：

- 做出决策
- 执行计划
- 持久化知识
- 与其他智能体协作

这些功能中的每一个都需要仔细的 **上下文管理** 。如果不加以控制，上下文窗口会变得臃肿，工具输出会消耗资源，模型的性能也会下降——这种现象被称为 **上下文退化综合征** 。

**有效上下文工程的好处**

1. **性能提升：** 减少令牌过载并增强 LLM 的专注度。
2. **降低成本：** 更少的令牌 = 更便宜的运行。
3. **更智能的智能体：** 从精心策划的相关上下文中做出更好的决策。
4. **可扩展性：** 支持长期或多智能体工作流程。
5. **一致性：** 在不同会话或任务中持久保存知识。

#### 上下文工程与提示工程有何不同？

为什么从“提示”转向“上下文”？早期，开发者专注于巧妙措辞提示以引出更好的答案。但随着应用变得越来越复杂，很明显，为人工智能提供完整且结构化的上下文远比任何神奇的措辞重要得多。

我还要指出， **提示工程是上下文工程的一个子集** 。即使你拥有所有的上下文信息，如何在提示中组织这些信息仍然至关重要。不同之处在于，你构建提示的目的不是为了与单一的输入数据集良好配合，而是为了处理一组动态数据并对其进行正确格式化。

上下文的一个关键部分通常是关于大语言模型（LLM）应如何表现的核心指令。这往往是提示工程的一个关键部分。你会说为智能体应如何表现提供清晰详细的指令是上下文工程还是提示工程呢？我认为两者都有一点。

#### LangGraph 如何实现上下文工程

当我们构建 LangGraph 时，我们的目标是使其成为最可控的智能体框架。这也使其能够完美地实现上下文工程。

使用 LangGraph，你可以掌控一切。你决定运行哪些步骤。你确切地决定将什么输入到你的 LLM 中。你决定将输出存储在哪里。你掌控一切。

这使你能够进行所有你想要的上下文工程。代理抽象（大多数其他代理框架所强调的）的缺点之一是它们限制了上下文工程。可能存在一些地方，你无法确切更改进入大语言模型（LLM）的内容，或者无法确切更改事先运行的步骤。

**示例：简化图调用**

```python
# Current (still supported)
agent.invoke(
    state,
    config={"configurable": {"user_id": "user_123", "thread_id": "12345"}}
)

# New (recommended)
agent.invoke(
    state,
    config={"thread_id": "12345"},
    context={"user_id": "user_123"},
)
```

**示例：增强型节点函数签名**

```python
# Current approach
def my_node(state: StateSchema, config: RunnableConfig):
    user_id = config["configurable"]["user_id"]  # Deep nesting
    # ...

# New approach
class Runtime(Generic[ContextT]):
    context: ContextT
    config: LangGraphConfig  # Cleaner config with top-level properties

    @property
    def stream_writer(self) -> StreamWriter:
        """Access streaming utilities without complex injection into node signatures."""

def my_node(state: StateSchema, runtime: Runtime):
    user_id = runtime.context.user_id  # Clean, typed access
    thread_id = runtime.config.thread_id  # No more nesting under "configurable"
    # ...
```

#### 结论

随着大语言模型（LLM）应用的成熟，性能的标准不再仅仅取决于你使用的是哪个模型，而是在于你与它的沟通效果如何。 **上下文工程** 是一种使这种沟通变得精确、完整且一致的实践方法。

这不仅仅是一个技术问题，更是一种设计理念。当你将上下文视为系统架构的头等重要部分时，一切都会变得更好：模型输出、用户体验以及开发速度。

随着这一概念得到更广泛的理解，我们很高兴能不断突破 LLMs 的能力边界——不仅通过更好的模型，还通过更好的交流方式。

#### 资源

- [上下文工程的兴起](https://blog.langchain.com/the-rise-of-context-engineering/)
- [智能体的上下文工程](https://rlancemartin.github.io/2025/06/23/context_engineering/)

通过各种平台保持联系并支持我的工作：

[GitHub](https://github.com/andysingal) [Patreon](https://www.patreon.com/AndyShanu) [Kaggle](https://www.kaggle.com/alphasingal) [拥抱脸](https://huggingface.co/Andyrasika) [YouTube](https://www.youtube.com/@andy111007) [GumRoad](https://rasikasingal.gumroad.com/) [Calendly](http://calendly.com/alphasingal) 需注意，“Hugging-Face”常见的中文译法是“拥抱脸” ，但在一些专业领域可能有更特定的译法，如果这是一个特定的技术或平台名称，可能需要根据具体情况进一步优化

喜欢我的内容吗？欢迎 [请我喝杯咖啡☕](https://paypal.me/alphasingal?country.x=US&locale.x=en_US) ！

请求与问题：如果你有一个希望我参与的项目，或者对我所解释的概念有任何疑问，请随时告诉我。我一直在为未来的笔记本寻找新想法，并且很乐意帮助解决你可能存在的任何疑惑。

请记住，每一次“点赞”、“分享”和“加星标”都对我的工作有很大帮助，并激励我继续创作更多优质内容。感谢您的支持！

如果你喜欢这个故事，欢迎 [订阅](https://medium.com/@andysingal) Medium，这样当我的新文章发布时你会收到通知，并且可以获得完全访问权限