---
title: "2026-03-09_Tomasz_Tunguz_9_Observations_from_Building_with_AI_Agents_Tomasz"
source: "https://tomtunguz.com/9-observations-using-ai-agents/"
author:
  - "[[@Tomasz Tunguz]]"
published: 2026-03-09
created: 2026-03-09
description:
tags:
  - "tomtunguz"
  - "@Tomasz Tunguz"
  - "ai"
  - "rllm"
---

# 9 Observations from Building with AI Agents | Tomasz Tunguz

过去一年里我一直在构建 AI 代理系统。以下是九个观察结果。 1. Prototype with the Best 当输入不可预测时，对于电子邮件解析、语音转录、混乱数据提取等任务，应采用最先进的技术。确定哪些方法在最佳模型中有效，然后随着时间的推移对其进行专门化处理。 2. Polish Small Gems 我使用 rLLM 1 微调了 Qwen 3 以进行任务分类。8B 模型在零样本提示中优于 GPT 5.2，并且可以在我的笔记本电脑上本地运行。微调在任务定义明确且输入分布稳定时表现出色。 3. Use Built-In Spell-Check 静态类型迫使 AI 面对拼写检查/编译器。Ruby 让代理能够生成看似有效的代码，但这些代码在运行时会失败。Rust 检查代码的语法。对于中等复杂度的任务，一次性成功率大幅提高。 4. 哄劝你的代理对手团队 构建你的代理型智囊团。让 Claude 制定一个计划。然后促使 Gemini 和 Codex 对计划进行评论；Claude 回应这些评论并实现代码。一旦实现后，让 Gemini 和 Codex 对实施情况相对于计划进行评论，并让 Claude 进行修改。代理是出色的微观管理者。 5. 把所有黏土放进一个锅里 构建 AI 代理就像玩培乐多一样。有些是黄色的，有些是红色的，有些是绿色的黏土。每一种都来自不同的罐子。我希望所有工具都集中在一个地方：管理我的记忆、管理我的提示词、捕获我的日志，因为这一切都是与模型改进相关的单一闭环。提示词 → 输出 → 评估 → 优化 → 提示词。 6. 认识到 iPhone 15 的人工智能时代 Qwen 3、GLM、DeepSeek V3 和 Kimi K2.5 以 成本的一小部分 就能提供出色的性能。这些模型现在已经足够强大，可用于工作流工具调用，在这种情况下，更多的智能可能不会带来更具体的好处。 Tau2 2 表明许多模型已经达到了这一阈值，现在我们正在比较它们的成本而非准确性。 7. Document FTW 正如 Harrison Chase 所说 ：“在软件中，代码记录应用程序；在人工智能中，痕迹也记录。”我们的系统运行一个夜间提示词优化系统。它收集最近 100 次代理对话，提取失败案例（任务超时、输出错误、用户修正），并使用作为评判者的 LLM 3 生成改进后的提示词。这种闭环改进每周无需人工干预即可逐步提高任务成功率。 8. Prompt Musical Chairs 我们不能为新的提示词导致系统停机。AI 代理会监控提示词文件，当文件发生变化时自动重新加载。这将部署与实验分离开来，并使 DSPy 4 风格的优化能够自动运行。结合版本化的提示词文件，即可获得完整的回滚能力。 9. Who Do You Work For?技能用于交互式对话。代码用于代理。技能更容易调试。当技能失败时，你确切地知道从哪里查找。当代理串联十个函数调用且输出错误时，你需要在日志中查找。 What have you learned?1分钟阅读，将技术数据转化为战略优势。 被15万+创始人及运营者阅读。 Theory Ventures 的普通合伙人。前 Google 产品经理。分享关于人工智能、web3 和风险投资的数据驱动见解。 Bloomberg • WSJ • Economist RLLM 是 Hugging Face 的一个用于语言模型的基于人类反馈的强化学习库。 ↩ Tau2 是一个衡量各模型工具调用准确性的智能体基准测试工具。 ↩ LLM 作为评判者使用一个语言模型来评估另一个语言模型的输出。 ↩ DSPy 是斯坦福大学用于通过编程方式优化提示词和少样本示例的框架。 ↩