---
title: "2026-01-14_neoragex2002_刚深扒了一下_MiroThinker_1_5_他们这套_Agent_压缩方式有点邪门_但看懂了觉得确"
source: "https://x.com/neoragex2002/status/2011075996158738606"
author:
  - "[[@neoragex2002]]"
published: 2026-01-14
created: 2026-01-14
description:
tags:
  - "x"
  - "@neoragex2002"
  - "https"
  - "2026-01-13"
---

# 刚深扒了一下 MiroThinker 1.5，他们这套 Agent 压缩方式有点邪门，但看懂了觉得确

**yan5xu** @yan5xu [2026-01-13](https://x.com/yan5xu/status/2010985530889289869)

刚深扒了一下 MiroThinker 1.5，他们这套 Agent 压缩方式有点邪门，但看懂了觉得确实有用。

核心解决的是「怎么在 256K 上下文里塞进去 400 次 Tool Use」的问题。

他们做了一个极其大胆的操作：对ReAct历史上 think-action-observation 中的的 Observation（工具返回结果）进行物理掩码。

除了最近 K

![Image](https://pbs.twimg.com/media/G-h0jnUa0AAvBom?format=jpg&name=large)

* * *

**neoragex2025** @neoragex2002 [2026-01-13](https://x.com/neoragex2002/status/2011063272162918715)

thoughts究竟是信息压缩还是信息扩展是不能假设的。但有一点，所有涉及到fc调用的agentic loop都会提醒llm注意fc调用的时效性，因此llm才在后文中会以各种形式嵌入前文fc调用结果信息（thoughts只是形式之一），逐步降低对长程fc调用结果的依赖，这才是后继可以直接mask掉历史fc调用结果的主要原因。

* * *

**yan5xu** @yan5xu [2026-01-13](https://x.com/yan5xu/status/2011068654574764460)

求展开说说

* * *

**neoragex2025** @neoragex2002 [2026-01-13](https://x.com/neoragex2002/status/2011075996158738606)

即fc调用只是特定时刻的特定结果。比方说查询个传感器、数据库之类。LLM可以从fc描述获悉其调用结果究竟是ephemeral还是persistent的，并在后继会话中有意识降低对失效结果的关注，于是高度动态的fc调用结果，后继删了也无妨，而时效稳定的fc结果，信息也早就分散到下文thought或正文里去了。