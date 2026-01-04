---
title: "2025-12-31_koylanai_使用_WisprFlow_代码片段作为技能_来编写生成技能的技能提示词_2025_12_21"
source: "https://x.com/koylanai/status/2003709550927429867"
author:
  - "[[@koylanai]]"
published: 2025-12-31
created: 2025-12-31
description:
tags:
  - "x"
  - "@koylanai"
  - "https"
  - "llm"
---

# 使用 @WisprFlow 代码片段作为技能，来编写生成技能的技能提示词。  2025-12-21

**Muratcan Koylan** @koylanai [2025-12-24](https://x.com/koylanai/status/2003688232257749383)

使用 @WisprFlow 代码片段作为技能，来编写生成技能的技能提示词。

> 2025-12-21
> 
> 我很兴奋地分享一个新仓库：智能体上下文工程技能
> 
> Instead of just offering a black-box tool library, it acts as a "Meta-Agent" knowledge base. It provides a standard set of skills, written in Markdown and code, that you can feed to an agent so it x.com/koylanai/statu…
> 
> ![Image](https://pbs.twimg.com/media/G8tds0UXoAAagSR?format=jpg&name=large)

* * *

**Muratcan Koylan** @koylanai [2025-12-24](https://x.com/koylanai/status/2003689446798151720)

这是 @eugeneyan 的 https://eugeneyan.com/writing/llm-evaluators/… 博客到 LLM 作为评审技能的查询的输出

Opus 4.5 在 Cursor 中一次性完成了这个。还构建了带有 @aisdk 6 的内部测试

![Image](https://pbs.twimg.com/media/G86IXr8XkAAFXTa?format=jpg&name=large)

* * *

**Muratcan Koylan** @koylanai [2025-12-24](https://x.com/koylanai/status/2003709550927429867)

以 LLM 为评判者的技能上线了！https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/examples/llm-as-judge-skills… 你如何可靠地评估 LLM 的输出？我读了一篇关于 LLM 评估工具的博客，发现了一些实用模式，这些模式可能会成为 AI 代理的可复用技能。但我不想仅仅阅读后就置之不理，而是想将这些知识付诸实践。我已经有一个 Context Engineering Skills 代码仓库，里面有基础技能，比如 context-fundamentals 和 tool-design。这些是教 AI 代理如何思考问题的指令。我开始爬取 Eugene Yan 的《以 LLM 为评判者》博客，以理解核心概念。他的研究中的关键见解是，以 LLM 为评判者不是单一的方法，而是一系列方法。然后我审视了自己现有的技能。context-fundamentals 技能教会代理如何结构化信息以最大化有效信号。tool-design 技能展示了如何构建具有合适模式、清晰输入输出以及优雅错误处理的工具。我们还分析了 Vercel 的 AI SDK 6 文档，以了解如何使用 TypeScript 构建代理系统。 在这个基础上，Cursor 中的 Opus 4.5 设计了一种架构。其核心思路是分离关注点：技能作为 Markdown 中的基础知识点，提示词作为可复用模板，工具作为实际实现，代理作为串联一切的编排层。每个组件都有独立的文件夹和文档，这使得系统具有模块化和可维护性。我们构建了三个核心工具。

第一个是 directScore，它使用评分细则根据加权标准评估单个响应。它要求进行思维链解释，评估者必须在给出分数前说明推理过程，研究表明这能将可靠性提高 15-25%。第二个是 pairwiseCompare，它比较两个响应并选出更优的那个。这里的关键创新是位置互换：我们将两个响应互换位置后进行两次比较，然后检查结果是否一致。如果互换位置后获胜者改变，说明位置偏差影响了判断，我们就改为平局。第三个是 generateRubric，它创建特定领域的评分细则以确保评估的一致性。我们将这些工具封装在一个 EvaluatorAgent 类中，该类为所有评估任务提供简洁的接口。该代理可以对响应进行评分、比较、生成评分细则，或执行完整工作流程——即先生成评分细则，再用它来评分。然后我们编写了测试。测试中调用了实际的 OpenAI API，使用真实提示词并验证系统端到端工作正常。 我们测试了好的回答得分高于差的回答，相同的回答打平，位置交换能正确检测偏差，以及生成的评分标准包含领域相关术语。所有十九项都通过了。README 解释了研究背景，展示了架构，包含实际测试日志，并记录了关键收获。我们还为主要的 Context Engineering 代码仓库创建了一个“高级评估”技能，这是一份全面指南，涵盖何时使用每种评估方法、如何减轻偏差、不同场景下使用哪些指标，以及需要避免的常见反模式。

我认为，这是代理设计和技能使用过程递归特性的一个很好例子。我使用了上下文工程相关的技能构建了一个系统，而这个系统本身又成为了一项技能和其他人可以使用的示例。上下文基础技能帮助构建了评估提示词的结构。工具设计技能指导了我们如何使用 Zod 模式构建 TypeScript 工具。评估技能提供了高级评估技能扩展的基础。每一层都以前一层为基础。最终成果是一个生产就绪的评估系统，包含经过测试的代码、全面的文档，以及一项可复用的技能，该技能可教 AI 代理如何评估其他 AI 的输出。

![Image](https://pbs.twimg.com/media/G86Yq_lXkAAJa_2?format=png&name=large)