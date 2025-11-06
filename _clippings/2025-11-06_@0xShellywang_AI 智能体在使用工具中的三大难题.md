---
title: "AI 智能体在使用工具中的三大难题"
source: "https://x.com/0xShellywang/status/1986292862850609281"
author:
  - "[[@0xShellywang]]"
published: 2025-11-06
created: 2025-11-06
description:
tags:
  - "@0xShellywang # AI #智能体 #工具 #使用 #模型 # token"
---
**Shelly** @0xShellywang 2025-11-05

我们算是最早一批用 MCP 做 agent 的。 真的是一路摸索过来。  
  
一开始也是让 LLM 动态生成代码调工具。 理论上很美好。 实际跑起来，各种问题：  
  
忘记 await，参数写错，类型对不上。 最头疼的是边界条件处理。 数据空了，流程就挂了。  
  
优化了很多轮，还是有 20%+ 的失败率。 每次执行都像开盲盒。  
  
后来调整了思路，不在运行时生成代码了。 在 planning阶段就准备好。planning → 生成代码 → 固化/验证 → 执行。它更接近 vibe coding，但同时保留一定灵活性和解析度。  
  
更准确说，是生成 DSL 去组合已有组件。 这些组件都是验证过的 lego 块。 很多来自开源生态，被大量应用验证过。  
  
LLM 只需要选择和组合。 不需要从头写代码。数据流和控制流也分开了。  
  
控制流在 planning 阶段确定。 数据流在运行时走DataFrame。因为 tools 的数据的参数在输入和输出端要先做对齐。  
  
我们还做了个 MCP++，直接对接 tools。 数据不经过LLM。 可以处理远超 context window 的数据量。方便数据的批量稳定准确处理，也更低成本。LLM 通过 preview 看到数据的 summary。 保持交互，但不被数据撑爆。  
  
所以我们不算纯 agent 模式。 更像 hybrid。LLM 负责planning 和决策。 但执行层是确定的代码组件。  
  
文章里提到的问题，我们确实都踩过。 现在的方案也还在迭代。

> 2025-11-05
> 
> 这篇总结也很好：
> 
> https://x.com/omarsar0/status/1986099467914023194…
> 
> Anthropic 又发布了一篇神级指南。
> 
> 这次的主题是：如何构建更高效的 AI 智能体 (AI Agent)，让它们能更聪明地使用工具，并且极大地节省 Token 。
> 
> 如果你是 AI 开发者，这篇文章绝对不容错过！
> 
> 它主要解决了 AI 智能体在调用工具时遇到的三大难题：Token

---

**宝玉** @dotey [2025-11-06](https://x.com/dotey/status/1986296036659278260)

你们那时候用的模型版本是啥？现在的模型写代码能力还是可以的，比如 codex cli 就是实时写代码的

---

**Shelly** @0xShellywang [2025-11-06](https://x.com/0xShellywang/status/1986299439015993765)

CC。单看一次代码生成，成功率是很高。但是写代码能力强，不等于在生产环境稳定。一个用户的任务，可能涉及复杂的多次工具调用，那它就不是写一次代码了。多步骤流程中，错误会累积，即使单步成功率高，整体成功率也会显著下降。

更麻烦的是上下文的复杂度。Codex CLI 写的是独立的代码片段。

---

**axtrur** @axtrur [2025-11-06](https://x.com/axtrur/status/1986352073450135765)

可以加上skills，我觉得所有事情都是分而治之，skill很好解决技能分组，以及技能内的lego模块组合

---

**Shelly** @0xShellywang [2025-11-06](https://x.com/0xShellywang/status/1986353978737848595)

嗯嗯。加快补充中。

---

**sky.up** @skyuper [2025-11-06](https://x.com/skyuper/status/1986364098066678044)

智能体每次运行的时候都需要从头planning 吗？还是可以利用之前planning的控制流代码？

---

**Shelly** @0xShellywang [2025-11-06](https://x.com/0xShellywang/status/1986365299076309050)

plan 一次后，后面就固化下来，可以重复运行了的。用户输出去替换 variable，user input。

我们这个不是做智能体，做的是工作流。

---

**繁霜** @mylanyuer [2025-11-06](https://x.com/mylanyuer/status/1986342472448921651)

skills是不是能进一步降低实时写脚本的概率，增加复用和确定性

---

**Shelly** @0xShellywang [2025-11-06](https://x.com/0xShellywang/status/1986344277438583057)

嗯嗯，是的。如果没有 skill，planner 会倾向生成完整的代码逻辑。如果有 skill，它会更清楚应该调用哪些工具，做组合去完成当前的任务。特别是在我们做业务流，excel 表格类的处理场景下，plan 的成功率会更高，run 的稳定性也更好。我们也在逐步落地 skill

---

**sky.up** @skyuper [2025-11-06](https://x.com/skyuper/status/1986362676440695184)

控制流是LLM生成的代码来实现的吗？

---

**Shelly** @0xShellywang [2025-11-06](https://x.com/0xShellywang/status/1986365029986541689)

生成 DSL

---

**日拱一卒王小楼.edge** @wang\_xiaolou [2025-11-06](https://x.com/wang_xiaolou/status/1986322169996222798)

一路走来不容易

---

**Shelly** @0xShellywang [2025-11-06](https://x.com/0xShellywang/status/1986322460418134088)

感谢小楼老师一直不离不弃。

---

**JacyL4** @JacyL4 [2025-11-06](https://x.com/JacyL4/status/1986353301085098074)

手动方式中，claude 评审，出修改方案，codex 直接读起来做，效果就还不错。一直担心 codex 偷懒少做，实践下来覆盖率还好。一些复杂的确实会略过，但没关系，再 claude 读 codex 写，来回几次就能覆盖到。

流程应该跟模型特点有很大关系，换别的效果就起不来。
