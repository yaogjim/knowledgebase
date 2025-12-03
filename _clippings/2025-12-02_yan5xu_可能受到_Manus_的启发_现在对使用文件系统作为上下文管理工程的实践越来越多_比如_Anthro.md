---
title: "2025-12-02_yan5xu_可能受到_Manus_的启发_现在对使用文件系统作为上下文管理工程的实践越来越多_比如_Anthro"
source: "https://x.com/yan5xu/status/1995301557538361698"
author:
  - "[[@yan5xu]]"
published: 2025-12-02
created: 2025-12-02
description:
tags:
  - "x"
  - "@yan5xu"
  - "https"
  - "2025-12-01"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-12-10"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---

# 可能受到 Manus 的启发，现在对使用文件系统作为上下文管理工程的实践越来越多，比如 Anthro

**yan5xu** @yan5xu [2025-12-01](https://x.com/yan5xu/status/1995301557538361698)

可能受到 Manus 的启发，现在对使用文件系统作为上下文管理工程的实践越来越多，比如 Anthropic 的 Skills，还有 LangChain 的 How agents can use filesystems for context engineering。

这些技巧背后，更深层次是对模型的认知理解或者说是 Agent 认知工程

我做了整理，希望能给大家一点启发

* * *

**yan5xu** @yan5xu [2025-12-01](https://x.com/yan5xu/status/1995302026394415349)

顺应模型的“直觉”（母语效应）

我们要承认一个底层逻辑：通用大模型本质上是基于互联网公开数据的“人类集体智慧模拟器”。

它表是在预测下一个字，而里是在模拟人类在海量数据（GitHub 代码、技术文档、论坛讨论）中展现出的行为模式。

好的标准协议（CodeAct/SQL/Shell）比自定义 Tool 更好用的原因是译文模型在训练阶段“看过”无数次人类使用 Python 处理数据、使用 SQL 查询数据库、使用 grep 检索文档。它不仅懂语法，更懂在什么场景下该用什么组合，以及报错了该怎么修。

自定义 Tool（外语）：模型需要先阅读说明书（In-context Learning），然后把逻辑“翻译”成调用动作，容易幻觉。

所以对于 Python、SQL、甚至是 Claude Skills 那种 YAML/Markdown 格式的知识库，模型不需要 Prompt 解释，它天生就会。Don't teach a native speaker how to speak.

* * *

**yan5xu** @yan5xu [2025-12-01](https://x.com/yan5xu/status/1995302260012994588)

认知负荷与注意力经济（Cognitive Load & Attention Budget）

我们在 Context Window（上下文窗口）往往只停留在字面上长度的限制，往往忽略了更深层级的 “认知极限”。

如果你定义的工具非常晦涩（Alien Tools），你需要在 Prompt 里写 500 字来解释这个工具怎么用。

这意味着你不仅占用了 500 个 Token 的空间，更消耗了模型宝贵的 Attention（注意力算力）。

而LLM 的单次推理“智商”是守恒的。如果它要把 30% 的精力花在“理解工具说明书”上，它处理核心业务逻辑的准确率就会下降。这就是为什么有时候工具给多了，模型反而变笨了。

所以在设计上，应该使用标准接口，说明书极短（甚至只需要函数名）。降低模型认知上的摩擦力，让模型能把全部算力用于解决真正的难题。

* * *

**yan5xu** @yan5xu [2025-12-01](https://x.com/yan5xu/status/1995302538296643673)

工具即流程（Tools shape Process）

工具的设计，直接决定了 Agent 的思维路径（Reasoning Path）。

反面教材（黑盒思维），设计一个 super\_analyze\_and\_fix(issue) 的万能工具。

他会Agent 变成了“填参数机器”，一旦报错，Agent 束手无策。另外模型不知道这个函数内部是如何工作的，它无法预测什么样的输入能得到最好的输出，只能“盲猜”。

正面教材（原子化思维 / Manus 模式）是提供 read\_file, grep, edit\_line 等原子工具。这种设计充分发挥了 LLM 的规划（Reasoning）能力。因为工具是透明且原子的，模型可以自己组合步骤，并根据报错动态调整策略（Self-Correction）。

这样我们通过设计工具，为模型的智能涌现提供了最佳环境。

* * *

**yan5xu** @yan5xu [2025-12-01](https://x.com/yan5xu/status/1995302868027654392)

当然也有例外。

上述逻辑主要适用于 GPT, Claude Sonnet 等通用基座模型。

如果你关注 OpenAI 的 基于o 系列 Deep Research，你会发现它们能极好地使用某些复杂工具。

原因它们经过了深度的 SFT（监督微调） 甚至 RL（强化学习）。在训练阶段，模型已经把特定工具的用法内化了。

所以如果你没有资源去专门训练一个模型，那么“顺应通用模型的直觉”依然是 ROI 最高的选择。

* * *

**yan5xu** @yan5xu [2025-12-01](https://x.com/yan5xu/status/1995305901268578351)

LangChain Blog 系统性总结了 "Scratchpad" 和 "Reference" 等文件系统交互模式。

https://blog.langchain.com/how-agents-can-use-filesystems-for-context-engineering/…

Manus 创始人 Yichao "Peak" Ji 的深度复盘，首次提出 "Filesystem is the Ultimate Context" 这一核心论断。

https://manus.im/blog/context-engineering-for-ai-agents…

Anthropic Agent Skills 官方详解 Skills 机制：通过 \`http://SKILL.md\` (YAML+Markdown) 将领域知识封装为文件，让 Agent 动态加载。这是最标准的“母语化”工具设计案例。

https://anthropic.com/news/equipping-agents-with-skills…

https://docs.anthropic.com/en/docs/build-with-claude/agent-skills…

CodeAct 论证了为什么“写代码”比“调 JSON 工具”更符合 LLM 的直觉（Action-as-Code）

https://arxiv.org/abs/2402.01030

* * *

**unixx** @unixecho [2025-12-01](https://x.com/unixecho/status/1995550918553772287)

文件系统做上下文管理，这个思路确实很 Agentic。感觉这才是解决长上下文痛点的正道。求整理的链接！我得好好研究一下。

* * *

**烟花老师（一支烟花）** @brad\_zhang2024 [2025-12-01](https://x.com/brad_zhang2024/status/1995417723329986897)

兄弟是懂行的👍