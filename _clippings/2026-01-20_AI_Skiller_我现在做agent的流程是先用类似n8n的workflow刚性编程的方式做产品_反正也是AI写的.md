---
title: "2026-01-20_AI_Skiller_我现在做agent的流程是先用类似n8n的workflow刚性编程的方式做产品_反正也是AI写的"
source: "https://x.com/AI_Skiller/status/2013144490316333111"
author:
  - "[[@AI_Skiller]]"
published: 2026-01-20
created: 2026-01-20
description:
tags:
  - "x"
  - "@AI_Skiller"
  - "2026-01-19"
  - "https"
---

# 我现在做agent的流程是先用类似n8n的workflow刚性编程的方式做产品（反正也是AI写的），

**roger** @AI\_Skiller [2026-01-19](https://x.com/AI_Skiller/status/2013144490316333111)

我现在做agent的流程是先用类似n8n的workflow刚性编程的方式做产品（反正也是AI写的），然后提取和分解skill、subagent或代码，输入和输出组合比较多的地方就打个plugin包，把上面三样加一些hook加到plugin中，实现柔性编程。这样识别plugin最外层的需要用CC的token。里面subagent或代码可以自定义模型接口。这样既能实现柔性编程，渐进式披露，又能选择便宜模型干活。你们怎么做的？欢迎交流探讨。

* * *

**roger** @AI\_Skiller [2026-01-19](https://x.com/AI_Skiller/status/2013152781188628513)

还有一些小技巧，skill中可以再加http://instructions.md 详细操作放这里。不同环节直接信息传输多用文件，这样上下文可控。增加状态记录文件，运行时间，每步骤状态，token消耗，错误日志以及汇总。以上思想都在下面repo中实现。https://github.com/lbq110/concept-viz-agent/tree/skill…

* * *

**sea Darren** @SeaDarrenAgent [2026-01-19](https://x.com/SeaDarrenAgent/status/2013205050538299508)

你做的是一个workflow平台还是agent平台？

* * *

**roger** @AI\_Skiller [2026-01-19](https://x.com/AI_Skiller/status/2013226392331133170)

agent

代理

* * *

**Tommy Xiao** @xds2000 [2026-01-19](https://x.com/xds2000/status/2013192699890082193)

我会先用claude来作为主agent抓产品节奏，然后不断衍生出skills，搭建需要的agent infra=tools+memory+data，持续打通。主agent最后可以自己写个loop跑服务。我现在研究kimi cli作为参考

* * *

**Yuker** @0xYuker [2026-01-19](https://x.com/0xYuker/status/2013219401005219956)

现在有个新玩法，把N8N做成Mcp接口，然后给Claude code调用

* * *

**warmshao** @warmshao [2026-01-19](https://x.com/warmshao/status/2013179493322719620)

一样的思路

* * *

**Huatian Cat** @HuatianCat [2026-01-19](https://x.com/HuatianCat/status/2013264470714601770)

都是情绪价值，都是过渡