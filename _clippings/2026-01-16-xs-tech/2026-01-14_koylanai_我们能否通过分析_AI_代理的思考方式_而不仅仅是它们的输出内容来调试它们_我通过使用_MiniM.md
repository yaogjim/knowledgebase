---
title: "2026-01-14_koylanai_我们能否通过分析_AI_代理的思考方式_而不仅仅是它们的输出内容来调试它们_我通过使用_MiniM"
source: "https://x.com/koylanai/status/2010561785095438363"
author:
  - "[[@koylanai]]"
published: 2026-01-14
created: 2026-01-14
description:
tags:
  - "x"
  - "@koylanai"
  - "https"
  - "2026-01-12"
---

# 我们能否通过分析 AI 代理的思考方式，而不仅仅是它们的输出内容来调试它们？ 我通过使用@MiniM

**Muratcan Koylan** @koylanai [2026-01-12](https://x.com/koylanai/status/2010561785095438363)

我们能否通过分析 AI 代理的思考方式，而不仅仅是它们的输出内容来调试它们？

我通过使用@MiniMax\_AI M2.1 的交错式思考来捕捉和分析 AI 代理在调用工具之间的推理过程，然后根据检测到的失败模式自动改进系统提示。现在它是我 Context Engineering Skills 代码仓库的一部分。https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/main/examples/interleaved\_thinking…大多数提示词优化方法都关注输出：“代理是否给出了正确答案？”但这忽略了一点：

两个智能体可能因为完全不同的原因产生相同的错误输出。一个可能推理正确但用了错误工具，另一个可能中途放弃了目标，第三个可能陷入循环推理的怪圈。在这个关于推理轨迹优化的例子中，我们采用这样的流程：

Agent → \[捕获每次行动间的思考\] → 分析原因 → 调整提示词

M2.1 每次工具调用间交替思考并说明原因：思考→行动→思考→行动→思考→完成

这使我们能够洞悉：

如何代理解读每个工具结果

推理哪里出错了

它考虑过哪些替代方案（或者没考虑的）

\- 为什么它做出了某些决定推理追踪优化器;

记录推理轨迹 - 记录 M2.1 在每次调用工具之间的思维模块

2\. 分析模式 - 检测到故障模式例如：

\- 目标放弃 - 代理在完成任务前停止

循环推理 - 重复类似的搜索却毫无进展

missing\_validation - 未验证工具结果就继续

过早结论 - 完成而未确认成功

工具误用 - 错误的工具选择或低效使用

\`上下文退化\` - 忘记之前的信息

3\. 生成改进 - 创建具体的提示词修改并附带解释

4\. 产出可分享的技能 - 将经验转化为可复用的最佳实践

上下文工程关注的是“你给智能体提供什么信息以及如何组织这些信息”。推理轨迹准确揭示了上下文失效的具体位置：

这个代理是不是忘了之前的指令？(上下文退化)

它没有利用自己已有的语境吗？(推理不完整)

是误读工具结果吗？（缺少验证）通过分析推理，我们可以为提示词添加正确的指导——不是通用指令，而是针对特定失败模式的具体干预措施。如果你想改进代理的提示词，看看它是如何思考的。推理轨迹能揭示仅看输出的评估所遗漏的失败点。

* * *

**Muratcan Koylan** @koylanai [2026-01-12](https://x.com/koylanai/status/2010565291135426670)

仓库里还有更多例子，但我认为这也是尝试那些具有生命力并不断自我提升的 agent 技能的好方法。

![Image](https://pbs.twimg.com/media/G-b1_fsWwAAg1Rq?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G-b2M9vX0AAA3HH?format=jpg&name=large)

* * *

**Oxylabs** @Oxylabs\_io

顶级网页抓取 API，行业领先的 98.5%成功率，还有免费高级功能。

* * *

**Timo Verbeek** @TimoV765 [2026-01-12](https://x.com/TimoV765/status/2010784259875975245)

这太神奇了！

* * *

**Muratcan Koylan** @koylanai [2026-01-12](https://x.com/koylanai/status/2010785815417536688)

谢谢。交错思维是探索智能体如何思考的一种很棒的方式。

* * *

**Shamim Hossain** @shamimai1 [2026-01-12](https://x.com/shamimai1/status/2010569426270363807)

太棒了

* * *

**SynthesisLedger** @SynthesisLedger [2026-01-12](https://x.com/SynthesisLedger/status/2010605316887761092)

完全同意，结果会骗人，但推理能揭示混乱。我多次在代理在工具链中途脱轨的问题上碰壁；从交错轨迹中自动优化提示词感觉就是我们需要的解决方案。

* * *

**United Records** @RecordsUni63959 [2026-01-12](https://x.com/RecordsUni63959/status/2010822085686235148)

疯狂

* * *

**Art Intelligence** @Art\_Intelligo [2026-01-12](https://x.com/Art_Intelligo/status/2010793316426932426)

这是我见过的最精彩的提示工程技术。而且不仅仅适用于提示词。Claude Code 的技能和插件用这个方法可以提升 100 倍。你绝对应该基于这个开发一个 Claude 插件。它将成为未来几年的黄金标准...