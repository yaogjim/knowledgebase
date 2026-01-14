---
title: "2026-01-14_yan5xu_对_miroFlow_Observation_Mask_的理解_有一个挑战_是如何看待_think"
source: "https://x.com/yan5xu/status/2011250574411645229"
author:
  - "[[@yan5xu]]"
published: 2026-01-14
created: 2026-01-14
description:
tags:
  - "x"
  - "@yan5xu"
  - "2026-01-13"
  - "thought"
---

# 对 miroFlow Observation Mask 的理解，有一个挑战，是如何看待 think，

**yan5xu** @yan5xu 2026-01-13

对 miroFlow Observation Mask 的理解，有一个挑战，是如何看待 think，所谓的推理过程。

推理过程本身就是会携带大量信息，关键信息的识别和对前面过程的反思，都会把信息从过去整个过程重新整理到 thought 中。

而且整个 thought 链路，路径本身也是信息。

> 2026-01-13
> 
> 即fc调用只是特定时刻的特定结果。比方说查询个传感器、数据库之类。LLM可以从fc描述获悉其调用结果究竟是ephemeral还是persistent的，并在后继会话中有意识降低对失效结果的关注，于是高度动态的fc调用结果，后继删了也无妨，而时效稳定的fc结果，信息也早就分散到下文thought或正文里去了。