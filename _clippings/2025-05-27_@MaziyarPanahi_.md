---
title:
source: "https://x.com/MaziyarPanahi/status/1926966732054307250"
author:
  - "[[@MaziyarPanahi]]"
created: 2025-05-27
description:
tags:
  - "@MaziyarPanahi #人工智能 #大型语言模型"
---
**Maziyar PANAHI** @MaziyarPanahi [2025-05-26](https://x.com/MaziyarPanahi/status/1926966732054307250)

  
好的，我已经下定决心了。

在诸如智能体工作流、并行函数调用、基于检索的生成（RAG）、多模态内容处理（MCP）、问答（QA）、长对话、长上下文等实际任务中对 Qwen3 模型进行测试之后……

🔥 通义千问 3-4B = 具备推理能力

🧠 通义千问 32B = 无推理能力

规模并非一切，推理才是。

---

**Maziyar PANAHI** @MaziyarPanahi [2025-05-26](https://x.com/MaziyarPanahi/status/1926966736168878300)

  
我真的试图为 8B 和 14B 模型找到一个合适的位置，不管推理功能是开启还是关闭，但它们就是不行。

开启推理功能后，它们速度太慢且不够智能。

在推理功能关闭的情况下，它们速度很快，但仍不如 4B 和 32B 强大。

---

**Maziyar PANAHI** @MaziyarPanahi [2025-05-26](https://x.com/MaziyarPanahi/status/1927025491476627572)

  
这是具备推理能力的通义千问 3 4B！正在进行并行函数调用。

![Image](https://pbs.twimg.com/media/Gr4rXAGXAAAuid7?format=jpg&name=large)

---

**Vaibhav (VB) Srivastav** @reach\_vb [2025-05-26](https://x.com/reach_vb/status/1926991859823391225)

  
有意思，4B 在带有推理功能的 MCP 任务中表现如何？

我猜你需要大得多的上下文窗口吧？

---

**Maziyar PANAHI** @MaziyarPanahi [2025-05-26](https://x.com/MaziyarPanahi/status/1927023673652772995)

  
对于一个不算太复杂的多轮对话（MCP），它表现得很棒！这个模型大小对于处理长文本上下文来说恰到好处，因为即使是 80 亿参数的模型在处理长文本时也会变得超级慢，而且有点无意义！

但是 4B 开启推理功能后，这就很合理了！这些任务中的大多数（多轮对话、函数调用等）并没有那么复杂，你只需要先进行推理。

---

**Faith Defender** @faithdefender [2025-05-27](https://x.com/faithdefender/status/1927235125395247245)

  
在 CrewAI 中同样使用了抓取和搜索 MCP 服务器工具。Qwen3:4b 非常厉害。

---

**Maziyar PANAHI** @MaziyarPanahi [2025-05-27](https://x.com/MaziyarPanahi/status/1927305394612847066)

  
太棒了！没想到 CrewAI 支持本地大语言模型，更不用说支持 40 亿参数的模型了！你是通过 vLLM 使用它的吗？

---

**Kevin Lin** @KevinQHLin [2025-05-26](https://x.com/KevinQHLin/status/1927055087827845388)

  
我们强烈认同这是一个重要问题，并制定了一种训练策略，以使模型能够自我决定是否进行思考。

> 2025-05-23
> 
>   
> 🧐 我们如何像人类一样教导多模态模型或智能体“何时思考”？
> 
> 👉 查看：思考与否（TON）
> 
> 通过强化学习实现视觉语言模型的选择性推理
> 
> arXiv: https://arxiv.org/pdf/2505.16854
> 
> （注：这里的内容看起来像是一个链接，直接保留英文链接是比较合适的做法，如果一定要翻译链接部分，可以是“arXiv: https:// 阿列克谢夫论文预印本库.org/pdf/2505.16854 ，但一般链接不建议翻译，以免影响其可用性。）
> 
> 代码：https://github.com/kokolerk/TON
> 
> 我们引入了“思维丢弃”
> 
> ![Image](https://pbs.twimg.com/media/GrnPwXSXgAAUxop?format=jpg&name=large)

---

**Maziyar PANAHI** @MaziyarPanahi [2025-05-26](https://x.com/MaziyarPanahi/status/1927098983266038129)

  
这非常有趣！我认为开放模型的下一步将是自动选择是否进行推理以及推理的程度！

---

**Dmitry Starkov** @starkov100 [2025-05-26](https://x.com/starkov100/status/1926976491906068705)

  
比起 30B - A3B，你更喜欢 4B 吗？

---

**Maziyar PANAHI** @MaziyarPanahi [2025-05-26](https://x.com/MaziyarPanahi/status/1926982356126007409)

  
没错！我在中间的人工智能工作流程步骤中使用启用了推理功能的 Qwen3 4B，包括函数调用、工具使用、RAG 后过滤和评估。它在这些任务中快速且有效。

对于面向用户的聊天或最终答案，我使用通义千问 32B。

---

**SUN YOUNG HWANG ᯅ** @SOSOHAJALAB [2025-05-26](https://x.com/SOSOHAJALAB/status/1927006953730981974)

  
哇，这信息真的很棒！多谢！

---

**Maziyar PANAHI** @MaziyarPanahi [2025-05-26](https://x.com/MaziyarPanahi/status/1927035950355390612)

  
非常欢迎！每个人的用例可能不同，但就我的用例而言，我就是无法用 8B、14B 和 30B 的混合专家模型来击败这两个！

---

**EdgeAI Geek** @edgeaiguy [2025-05-26](https://x.com/edgeaiguy/status/1926975047467438092)

  
与开启推理相比，Qwen3 - 32B 在关闭推理时表现更好吗？

---

**Maziyar PANAHI** @MaziyarPanahi [2025-05-26](https://x.com/MaziyarPanahi/status/1926981838079221790)

  
不！我只能使用那种关闭推理功能的模型，否则对我的用例来说会太慢。关闭推理功能后，我很满意！它比开启推理功能的 140 亿参数模型还快，而且仍然更智能。这太棒了！

---

**EdgeAI Geek** @edgeaiguy [2025-05-26](https://x.com/edgeaiguy/status/1926983140305735754)

  
有没有人知道推理功能关闭的 Qwen3 - 32B 与 llama3.3 70B 相比如何？

---

**Maziyar PANAHI** @MaziyarPanahi [2025-05-26](https://x.com/MaziyarPanahi/status/1927023018875785246)

  
这在很大程度上取决于任务，但我不建议一直开启推理功能的 32B 密集模型。除非该任务只能通过推理来完成，否则我会通过 extra\_body 标志将其开启，然后在其他所有任务中关闭它。

启用推理功能的话成本会非常高

---

**GopiNath** @Gopinath876 [2025-05-26](https://x.com/Gopinath876/status/1926991539126862016)

  
抄送

@reach\_vb

---

[2025-05-26](https://x.com/ChelseaMCMV/status/1927067136721100942)

  
哇……非常有趣，根据我目前的经验，通常在上下文很大的情况下，模型大小很重要，如果推理能力能在这方面有所提升，那我们真的要进入一个小型专业化推理语言模型的世界了

---

**Maziyar PANAHI** @MaziyarPanahi [2025-05-26](https://x.com/MaziyarPanahi/status/1927098520953053640)

  
在功能调用和内部步骤方面，推理部分使得 4B（模型）相较于 14B（模型）表现出色！完美的规模！

对于面向人类的最终答案，我将使用没有推理功能的通义千问 32B。 🔥

---

**Prathmesh** @psv2522 [2025-05-26](https://x.com/psv2522/status/1927005815006720268)

  
就我测试的情况来看，4B 在多轮对话规划（MCP）和工具调用方面表现不佳

---

**Maziyar PANAHI** @MaziyarPanahi [2025-05-26](https://x.com/MaziyarPanahi/status/1927024808727920918)

  
没有推理可不行！但要是有了推理，要是你有一个好的提示（不是 vllm 里常用的那种工具）并进行少样本学习，那就能创造奇迹！！！

我把我的 llama - 3.3 70B 换成了开启推理功能的 qwen3 4B。我需要良好的并行函数调用功能。

---

**Physics Memes** @ThePhysicsMemes [2025-05-26](https://x.com/ThePhysicsMemes/status/1926995244504986106)

  
你让它们做什么任务？小模型似乎太笨了没什么用，很多时候它们连一个简单的指令都执行不了。

需要说明的是，使用这样不尊重和带有歧视性的语言去描述模型是不恰当和不专业的行为，在交流中应尽量保持客观、理性和尊重

---

**Maziyar PANAHI** @MaziyarPanahi [2025-05-27](https://x.com/MaziyarPanahi/status/1927225608443957567)

  
不适用於：

\- 函数调用（甚至是并行调用）

\- 结构化输出

\- 检索增强生成（RAG），评估来源、筛选来源、引用等的第一步……

开启推理功能会让 4B 轻易击败 8B，并接近 14B！然后我用 32B 来得出最终答案。

---

**s.h** @hebbarmp [2025-05-27](https://x.com/hebbarmp/status/1927192477842202866)

  
用于编码？