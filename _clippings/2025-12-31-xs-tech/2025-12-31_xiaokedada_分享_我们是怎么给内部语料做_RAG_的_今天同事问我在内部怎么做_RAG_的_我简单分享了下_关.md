---
title: "2025-12-31_xiaokedada_分享_我们是怎么给内部语料做_RAG_的_今天同事问我在内部怎么做_RAG_的_我简单分享了下_关"
source: "https://x.com/xiaokedada/status/2006008132594696580"
author:
  - "[[@xiaokedada]]"
published: 2025-12-31
created: 2025-12-31
description:
tags:
  - "#分享"
  - "x"
  - "@xiaokedada"
  - "agent"
---

# #分享 我们是怎么给内部语料做 RAG 的 今天同事问我在内部怎么做 RAG 的，我简单分享了下，关

**nazha** @xiaokedada [2025-12-30](https://x.com/xiaokedada/status/2006008132594696580)

#分享 我们是怎么给内部语料做 RAG 的

今天同事问我在内部怎么做 RAG 的，我简单分享了下，关键词就叫「基于文件系统的的二次检索策略」。我们在做 Coding Agent 的时候，内部资料主要是组件文档、库文档和 api 文档这些偏结构性的文档。实践下来如果按照传统方案进行分块，反而效果不好。比方说，组件 A 的使用文档如下：

\## 组件名

描述

\## api

\## 示例

\### Demo1

\### Demo2

\### Demo3

...

如果只召回了 A 的描述，却没有召回 api 或者召回了 api 却没有召回某个特定使用的 Demo 种种边界问题。

我们的策略是做二次检索。它的步骤是先对文件做摘要处理，只把摘要文档送入 RAG 系统进行检索。然后让 Agent 做一次粗略检索，大概会有 5 到 10 个候选。再让 Agent 从这 5 到 10 个候选中找出匹配要求的全量文档。

为了减少 Token 和上下文，可以基于文件系统向 Agent 返回少量的数据，而其他内容进行渐进式披露。比方说，返回的全量文档的内容实际上可能是：

\## 组件名

描述

\## api

\[api\](./api.txt)

\## 示例

\[Demo1\](./demo1.txt)

\[Demo2\](./demo2.txt)

\[Demo3\](./demo3.txt)

这样既减少了上下文膨胀，也可以降低噪音对 LLM 的干扰。更重要的时候，基于文件系统，后续的对话 or Agent 可以直接进行本地 grep 检索而无需再次召回。

![Image](https://pbs.twimg.com/media/G9bFu6IbUAAA_li?format=jpg&name=large)