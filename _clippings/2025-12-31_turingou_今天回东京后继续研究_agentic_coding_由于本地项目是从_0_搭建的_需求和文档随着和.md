---
title: "2025-12-31_turingou_今天回东京后继续研究_agentic_coding_由于本地项目是从_0_搭建的_需求和文档随着和"
source: "https://x.com/turingou/status/2003090619749876142"
author:
  - "[[@turingou]]"
published: 2025-12-31
created: 2025-12-31
description:
tags:
  - "x"
  - "@turingou"
  - "https"
  - "coding"
---

# 今天回东京后继续研究 agentic coding，由于本地项目是从 0 搭建的，需求和文档随着和

**郭宇 guoyu.eth** @turingou [2025-12-22](https://x.com/turingou/status/2003090619749876142)

今天回东京后继续研究 agentic coding，由于本地项目是从 0 搭建的，需求和文档随着和 codex 和 cc 的沟通越来越明确，文档的复杂程度也逐渐加深。

这让我越来越觉得 agentic coding 本质上是文档管理的艺术，从 vibe coding 发展了一年后，自然语言编程似乎慢慢将软件工程转换为了文档工程。

最初，需求极其模糊。llm 会按照自己的想法为我们想做的事情设定一个 roadmap 和 mvp 版本，这是从零开始的第一步，它决定了迭代的大版本号。我一般会让 llm 在本地生成两个文件，第一个毫无疑问是 agent constitution，第二个是 http://roadmap.md 这是非常重要的文件，所有的需求，都会从这个文件的迭代 session 中派生出来，顺序是 roadmap:v0.1 -> stories/xxx.md 这里的 story 其实就是需求白板中的任务，它可能涉及到 API 或者 UI，包含几个甚至十几个复杂的任务，每一个 story 文件，都会是一个单独的文件，涵盖着某个可被测试的需求完整的结构，任务完成情况和相关联的文件路径。

stories 文件夹中每完成一个需求，我会要求 codex / cc 在 docs 对应的路径创建一系列 md 文档，以标记一个功能所涉及到的状态，如果这个功能产生了 bug，就在修复 bug 的过程中继续在这个文档中记录 bug 修复进度，于此同时，也要求它按照文档结构来组织 lib 或 api router 文件。以此类推，文档系统会形成一个巨大的网状结构，最终，它会成为整个产品的故事和描述文件。

传统的软件工程里，这个是产品经理干的活儿。但对于自然语言编程来说，这个任务变成了工程师的责任。一开始，我还设计了一个 architecture 文档，以要求 cc 用对应的技术栈来完成功能，后来，我发现随着软件的生长，强行要求一个万能的程序员按照人类的技术栈来实现功能并没有什么意义（维护已存在的项目除外）所以我废弃了这个文件，只维护产品故事和需求描述。

在整个 agentic coding 的过程中，我基本上只和文档打交道，在另外一个浏览器界面等待完成的需求被刷新，没关心过代码重构和其他技术问题，这让编程（如果还能这样定义它的话）成为了一种极其容易进入心流的对话情境，以我个人的体验来说，这是一件非常好的事儿。如果你没体验过 agentic coding，我推荐大家尝试一下！

* * *

**郭宇 guoyu.eth** @turingou [2025-12-22](https://x.com/turingou/status/2003091651217273059)

随着 llm 编程能力的进步，我们有可能不再需要管理源代码，转而管理源文档，同一份需求描述文档，也有可能在不同的 llm

* * *

**奶牛叔 MemeMax** @WWTLitee [2025-12-23](https://x.com/WWTLitee/status/2003342966140862648)

文档即代码 心流体验

* * *

**✧ 𝕀𝔸𝕄𝔸𝕀 ✧** @iamai\_eth [2025-12-22](https://x.com/iamai_eth/status/2003103226347037044)

后端尤其是涉及数据持久化，很难完全抛弃某种形式的架构约束。数据结构、索引、分库分表、迁移成本这些东西，一旦选错或频繁重构，代价就比较大了。

我的实践中，往往是把高代价层（数据结构+业务逻辑接口）人工把关，低代价层（UI/UX）放手给AI，既能享受文档驱动的心流，又不让系统在关键点失控。

* * *

**StarryDesert** @StarryDeserts [2025-12-22](https://x.com/StarryDeserts/status/2003119261729079388)

哥你说的对，我也有同感。我觉得在工程化和产品构建的维度上 agentic coding 的优势太大了，它能够自己将项目本身的架构清晰的反映在文档上，可维护性会高很多，但又不会像 vibe coding 那样容易产生技术债，因为在 vibe coding 里你还是需要懂代码才能指导 ai 修复 bug，而 在 agentic coding

* * *

**Sam** @CyberVoid77 [2025-12-22](https://x.com/CyberVoid77/status/2003247649005445565)

试试openspec

试试开放规范

* * *

**Smithjohn铜匠** @smithandai [2025-12-23](https://x.com/smithandai/status/2003462482996920443)

以后会不会就是ai自动迭代和更新,只要有电力和算力和数据~~~~