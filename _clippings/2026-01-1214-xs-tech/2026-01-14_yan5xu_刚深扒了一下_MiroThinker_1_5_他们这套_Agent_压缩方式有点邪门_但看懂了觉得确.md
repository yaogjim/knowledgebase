---
title: "2026-01-14_yan5xu_刚深扒了一下_MiroThinker_1_5_他们这套_Agent_压缩方式有点邪门_但看懂了觉得确"
source: "https://x.com/yan5xu/status/2010985530889289869"
author:
  - "[[@yan5xu]]"
published: 2026-01-14
created: 2026-01-14
description:
tags:
  - "x"
  - "@yan5xu"
  - "https"
  - "2026-01-13"
---

# 刚深扒了一下 MiroThinker 1.5，他们这套 Agent 压缩方式有点邪门，但看懂了觉得确

**yan5xu** @yan5xu [2026-01-13](https://x.com/yan5xu/status/2010985530889289869)

刚深扒了一下 MiroThinker 1.5，他们这套 Agent 压缩方式有点邪门，但看懂了觉得确实有用。

核心解决的是「怎么在 256K 上下文里塞进去 400 次 Tool Use」的问题。

他们做了一个极其大胆的操作：对ReAct历史上 think-action-observation 中的的 Observation（工具返回结果）进行物理掩码。

除了最近 K 轮保留原文，之前的几百轮 Tool Result 全部替换成一句 "Tool result is omitted to save tokens"。但是完整保留了所有的 <thought>。

这里面有一个非常反直觉的地方，这个 agent 本身就是在做 deep research，那他只留最近 K 轮，也就是 5 轮的原文，前面都没有了，还怎么能回答问题。

这就有一个非常隐晦但关键的前提：只要 Thought 足够密，它其实就是在无限逼近 Summary。

每一次 Thought 的生成，本质上都是模型对当前 Observation 的一次信息切片。T1 产生时已经把 O1 里的关键数据“吃”进脑子了。

虽然 O1 被替换成了占位符，但 T1 还在。T1 就成了 O1 的“信息压缩包”。不需要额外挂一个 Summary Agent，这条完整的 Thought 链，本身就是一份不断增量更新的、高保真的「动态摘要」。

![Image](https://pbs.twimg.com/media/G-h0jnUa0AAvBom?format=jpg&name=large)

* * *

**yan5xu** @yan5xu [2026-01-13](https://x.com/yan5xu/status/2010986304050503728)

对照可以看看这个压缩办法，也是保留 tao 过程

> 2026-01-05
> 
> 我想到一个很棒的低成本压缩方式，agentic loop 里面每个 fc 有结果之后，拿到小模型总结这次调用做了什么，形成一个 log，因为缓存命中了，所以成本不会太高；到达上下文阈值之后，就可以通过 log+summary，开新 session；上下文最大限度保留

* * *

**第九比特** @ninthbit\_ai [2026-01-13](https://x.com/ninthbit_ai/status/2011008086224617584)

这算是 Observation Masking（观察遮蔽）吗？

* * *

**yan5xu** @yan5xu [2026-01-13](https://x.com/yan5xu/status/2011025555815342165)

observeation masking 是啥 我还不太了解🤔

* * *

**Atom.com** @atomHQ

Five seconds. ⏱️

One name.

Make it unforgettable.

Find your unforgettable name on Atom.

五秒钟。 ⏱️

一个名字。

让它难以忘怀。

在 Atom 上找到你难忘的名字

* * *

**Ted Li** @FallMonkey [2026-01-13](https://x.com/FallMonkey/status/2010997532642721951)

这个做法完全不如你老东家和现在流行的offload做法啊，后者本来也会保存一部分调用信息。一旦遇到那种天马行空思考的模型就抓瞎了。

* * *

**yan5xu** @yan5xu [2026-01-13](https://x.com/yan5xu/status/2010997963167056363)

他们这个屌就屌仔，模型和 agent 结构是一体的啊😂。thought 吐什么，他们肯定也做了优化。

* * *

**coconut** @CoconutTcringo [2026-01-13](https://x.com/CoconutTcringo/status/2011025125119050230)

那不是每次都没办法命中 kvcache

* * *

**yan5xu** @yan5xu [2026-01-13](https://x.com/yan5xu/status/2011025701181567058)

omitted 之后也还是命中了啊

* * *

**neoragex2025** @neoragex2002 [2026-01-13](https://x.com/neoragex2002/status/2011063272162918715)

thoughts究竟是信息压缩还是信息扩展是不能假设的。但有一点，所有涉及到fc调用的agentic loop都会提醒llm注意fc调用的时效性，因此llm才在后文中会以各种形式嵌入前文fc调用结果信息（thoughts只是形式之一），逐步降低对长程fc调用结果的依赖，这才是后继可以直接mask掉历史fc调用结果的主要原因。

* * *

**yan5xu** @yan5xu [2026-01-13](https://x.com/yan5xu/status/2011068654574764460)

求展开说说

* * *

**jiangjin** @JiangJin\_PKU [2026-01-13](https://x.com/JiangJin_PKU/status/2011120514849497305)

有个工作infity think，和这思想很像

* * *

**yan5xu** @yan5xu [2026-01-14](https://x.com/yan5xu/status/2011242016261489058)

有资料吗

* * *

**laoda** @laoda2000 [2026-01-14](https://x.com/laoda2000/status/2011251311262777418)

https://x.com/i/status/2011246442497859869…

看看這個

刚深扒了一下 MiroThinker 1.5，他们这套 Agent 压缩方式有点邪门，但看懂了觉得确实有用。 核心解决的是「怎么在 256K 上下文里塞进去 400 次 Tool Use」的问题。 他们做了一个极其大胆的操作：对 ReAct 历史上 think-action-observation 中的的 Observation（工具返回结果）进行物理掩码。 除了最近 K https://t.co/UvPqYE6pdD

看看这个

> 2026-01-14

* * *

**yan5xu** @yan5xu [2026-01-14](https://x.com/yan5xu/status/2011252639896572312)

这是 offload 到文件里了

* * *

**edgeful** @edgeful

only for people that are serious about trading.

仅面向那些认真对待交易的人。

* * *

**蛋黄堡.ai** @Hamburgerai [2026-01-13](https://x.com/Hamburgerai/status/2011040645063029132)

那我可以理解成每一次的T其实都是对O的summary？这样会不会影响action的质量？

* * *

**ztoh** @ZtohAic [2026-01-13](https://x.com/ZtohAic/status/2011225989809160474)

是一种带有赌注性质的设计：用最少的介入换取最大的上下文利用率，牺牲旧有观察的可读性，以换取思维链的纯粹性和长度。一旦Thought未能抓住关键细节，后续推理就可能出问题。

* * *

**es05** @es05988399 [2026-01-13](https://x.com/es05988399/status/2011064408806735926)

There’s a growing habit of turning obvious engineering trade-offs into exotic-sounding terms.

This one is just refolding the stack.

Rename it back, and the magic vanishes.

将明显的工程权衡转化为听起来很奇特的术语的习惯日益普遍。

这个只是重新折叠了栈。

改回原来的名字，魔力就消失了。