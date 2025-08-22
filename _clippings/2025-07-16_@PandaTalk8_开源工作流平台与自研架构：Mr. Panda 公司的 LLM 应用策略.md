---
title: "Mr. Panda 公司的 LLM 应用架构解析"
source: "https://x.com/frxiaobei/status/1945131298164552124"
author:
  - "[[@PandaTalk8]]"
created: 2025-07-16
description:
tags:
  - "@PandaTalk8 #LLM #应用架构 #开源 #LangChain"
---
**Mr Panda** @PandaTalk8 [2025-07-15](https://x.com/PandaTalk8/status/1945109737303106006)

请问大佬们，你们公司现在的 LLM 应用架构是基于：

1\. 用开源工作流平台

2\. 基于langchain 自己开发，

3\. 又或者是采用的其他方案。

比如支持 AI Agent 场景、 Deep Resarch 场景、 RAG 场景等

---

**凡人小北** @frxiaobei [2025-07-15](https://x.com/frxiaobei/status/1945131298164552124)

大部分是 1 和 2。

1 是讲故事的，方便统一叙事、做生态、忽悠老板；

2 才是真正能跑业务的主力，用起来才能知道链路怎么断、数据怎么丢、反馈怎么慢。

AI 应用不一定非得程序员才能做，大量场景其实就是业务自己拖拖拽拽，把现成能力拼起来用。一边是LangChain + 自研搞定深度能力，一边把复杂技术封装进好用的 UI 里，让非技术同事也能搞定 80 分的场景。