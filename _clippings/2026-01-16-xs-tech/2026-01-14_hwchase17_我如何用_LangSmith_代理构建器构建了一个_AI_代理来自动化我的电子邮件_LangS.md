---
title: "2026-01-14_hwchase17_我如何用_LangSmith_代理构建器构建了一个_AI_代理来自动化我的电子邮件_LangS"
source: "https://x.com/hwchase17/status/2011126016287113681"
author:
  - "[[@hwchase17]]"
published: 2026-01-14
created: 2026-01-14
description:
tags:
  - "x"
  - "@hwchase17"
  - "https"
  - "2026-01-13"
---

# ✒️ 我如何用 LangSmith 代理构建器构建了一个 AI 代理来自动化我的电子邮件 LangS

**Harrison Chase** @hwchase17 [2026-01-13](https://x.com/hwchase17/status/2011126016287113681)

✒️ 我如何用 LangSmith 代理构建器构建了一个 AI 代理来自动化我的电子邮件

LangSmith Agent Builder 是一个无代码代理构建器。我构建了一个邮件助手来监控和回复邮件，已经用了大约 3 个月。这是它的样子：

1/ 触发条件：由新邮件触发。我不用做任何操作来启动它——它会自动运行。

2/ 通过 MCP 的工具：连接到 Gmail（读取电子邮件，发送电子邮件）和 gcal（读取日历，读取事件，创建事件）

3/ 人工介入：“写入”操作（发送电子邮件、创建日历）需要人工审批才能执行。稍后再详细说，但想强调的是，它能彻底失控！

4/ 子代理用于日历日程安排：LLMs 在处理日历方面做得很差！所以我专门有一个子代理来查找我的空闲时间——它工作得好多了

5/ 代理收件箱待审核：如前所述，某些操作需要人工批准。LangSmith 代理构建器配备了一个代理收件箱，用于审核和批准代理想要执行的操作

6/ message\_user 用来提问：有时候我的代理不知道该做什么。它有个 message\_user 工具，可以用这个工具来问我问题！这也会出现在代理的收件箱里

7/ 记住我说的话：它会根据我对它的回应自动更新记忆！这让我不用重复自己

总的来说 - 我再也不看我的实际邮件了，就看这个！

我录制了一个关于我如何制作它以及如何使用它的简短视频：https://youtu.be/bzcAZJTxOrs

我们把它做成了一个模板，这样你就可以在这里轻松尝试：https://smith.langchain.com/agents/templates?viewingTemplateId=email-assistant&skipOnboarding=true…

如果你想构建自己的代理，不妨在这里尝试 LangSmith 代理构建器：https://smith.langchain.com/agents?skipOnboarding=true…

![Image](https://pbs.twimg.com/media/G-j0ZdobkAAkWnC?format=jpg&name=large)

* * *

**ZAZA** @OpinionAILtd [2026-01-13](https://x.com/OpinionAILtd/status/2011177740238778491)

这可真是个进步啊，我的朋友，从一年前我们讨论过的那些事来看

* * *

**EXAIR** @EXAIR

EXAIR 压缩空气产品解决各种制造问题，自 1983 年以来一直如此。访问我们的解决方案路径，了解你可以提高安全性和效率的不同方法，同时在此过程中节省资金！

* * *

**Cathy Chang** @Cathy\_c8i [2026-01-13](https://x.com/Cathy_c8i/status/2011127320774619159)

我得自己试试 LangChain，你自己的代理的 UI 怎么样？

* * *

**Sinan** @sinankprn [2026-01-14](https://x.com/sinankprn/status/2011285828149150094)

你的团队做得超棒！继续加油！@hwchase17

* * *

**AMN** @byteakp [2026-01-13](https://x.com/byteakp/status/2011137134137410007)

把日历逻辑委托给特定的子代理是个专业操作。整体式模型在时间推理方面仍然苦苦挣扎。关注点分离=可靠性

* * *

**Mykhailo Sorochuk** @sir4K\_zen [2026-01-14](https://x.com/sir4K_zen/status/2011232201921478885)

不错的设置。日历子代理这个设计很巧妙。