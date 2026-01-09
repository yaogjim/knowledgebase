---
title: "2026-01-09_LotusDecoder_claude_code_的新功能_给skills_加上_contextfork_将让该项skil"
source: "https://x.com/LotusDecoder/status/2009328418735988817"
author:
  - "[[@LotusDecoder]]"
published: 2026-01-09
created: 2026-01-09
description:
tags:
  - "x"
  - "@LotusDecoder"
  - "https"
  - "lotusdecoder"
---

# claude code 的新功能，给skills 加上 contextfork ，将让该项skil

**LotusDecoder** @LotusDecoder [2026-01-08](https://x.com/LotusDecoder/status/2009328418735988817)

claude code 的新功能，给skills 加上 context:fork ，将让该项skills独立运行在子代理空间，不污染主空间上下文，只返回结果。

这一条不适合加给 planning-with-files，因为这一类skills 是对主对话持续导航的。

适合加给 web search 类的skills，因为大多数情况，这一类调研收集类只要一个结果。

* * *

**Yuanhao** @yuanhao [2026-01-08](https://x.com/yuanhao/status/2009360775065055524)

最近 planning-with-files 很火，新东西层出不穷，完全跟不上节奏 😅 我打算试试 /feature-dev 和 planning-with-files 能不能协同工作

* * *

**LotusDecoder** @LotusDecoder [2026-01-09](https://x.com/LotusDecoder/status/2009418353639825820)

估计可以的，因为 planning-with-files 和 插件 ralph-wiggum:ralph-loop 都可以协作

* * *

**忒修斯的船板** @Arcadia\_Bao [2026-01-08](https://x.com/Arcadia_Bao/status/2009366670272340442)

等同于在规划skill时候说：设计为sub-agent 只返回结果？

* * *

**LotusDecoder** @LotusDecoder [2026-01-09](https://x.com/LotusDecoder/status/2009417998478823465)

是的， 相当于设计为 sub-agent 去写了 md ，然后把 计划目标给附加在 subagent 的尾部了。