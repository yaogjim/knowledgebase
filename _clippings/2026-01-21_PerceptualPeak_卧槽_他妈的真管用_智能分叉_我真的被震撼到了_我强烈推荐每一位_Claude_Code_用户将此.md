---
title: "2026-01-21_PerceptualPeak_卧槽_他妈的真管用_智能分叉_我真的被震撼到了_我强烈推荐每一位_Claude_Code_用户将此"
source: "https://x.com/PerceptualPeak/status/2012741829683224584"
author:
  - "[[@PerceptualPeak]]"
published: 2026-01-21
created: 2026-01-21
description:
tags:
  - "x"
  - "@PerceptualPeak"
  - "https"
  - "2026-01-18"
---

# 卧槽，他妈的真管用！ 智能分叉。我真的被震撼到了。我强烈推荐每一位 Claude Code 用户将此

**Zac** @PerceptualPeak 2026-01-17

卧槽，他妈的真管用！

智能分叉。我真的被震撼到了。我强烈推荐每一位 Claude Code 用户将此应用到自己的工作流程中。

你是否有一个想在现有项目中实现的功能，而无需重复解释？众所周知，聊天会话的相关上下文越多，就能越有效地实现你的请求。为什么不利用你从数百/数千次其他 Claude 代码会话中获得的知识呢？别让这些宝贵的上下文浪费掉！！

这就是智能分叉发挥作用的地方。调用/fork-detect 工具，告诉它你想做什么。然后它会将你的提示词通过嵌入模型处理，将嵌入结果与一个向量化的 RAG 数据库进行交叉引用，该数据库包含你之前所有的聊天记录（当你继续进行更多对话时，该数据库会自动更新）。

然后它会返回你之前进行的、与你想要做的事情相关的前 5 个聊天会话列表，为每个分配一个相关性分数并按从高到低排序。然后你选择想要分叉的会话，系统会给出 fork 命令，你可以复制粘贴到新终端中。

然后，搞定！无缝高效的功能实现。

很高兴快速制定一个实施计划，如果有人感兴趣的话，我会把它分享到 Git 仓库里！

> 2026-01-17
> 
> Claude 代码想法：智能分叉检测。
> 
> 让每次会话记录自动通过 RAG 加载到向量数据库中。创建一个 /detect-fork 命令。调用这个命令时，会首先提示 Claude 询问你想要做什么。你告诉它，然后它会调度一个
> 
> ![Image](https://pbs.twimg.com/media/G-6tTiBXsAAatzC?format=png&name=large) ![Image](https://pbs.twimg.com/media/G-6xCE0WYAAQOfG?format=png&name=large) ![Image](https://pbs.twimg.com/media/G-6xV9EWMAAUdKQ?format=png&name=large)

* * *

**Zac** @PerceptualPeak [2026-01-18](https://x.com/PerceptualPeak/status/2012742405783458222)

@DanielleFong 我觉得你可能会喜欢这个

* * *

**Zac** @PerceptualPeak [2026-01-18](https://x.com/PerceptualPeak/status/2012744805621661704)

使用的综合评分公式：(最佳相似度×0.40)+(平均相似度×0.20)+(块比例×0.05)+(时效性×0.25)+(链质量×0.10)

* * *

**Zac** @PerceptualPeak [2026-01-19](https://x.com/PerceptualPeak/status/2013148545818481038)

关于仓库的更新 - 今晚没法赶出来了。结果是，昨天我把向量数据库迁移到 nomic 嵌入时，不小心用了旧的守护进程，并且又用了 384 维的嵌入，而不是 768 维。 🙄 哦，更糟糕的是，我真是个大笨蛋，还没考虑到

* * *

**David** @dzhng [2026-01-18](https://x.com/dzhng/status/2013037287278252123)

这基本上是另一种针对记忆的实现吗？

* * *

**Connor Martin** @ConnorYMartin [2026-01-18](https://x.com/ConnorYMartin/status/2012904399236907400)

分享仓库吧

* * *

**Zac** @PerceptualPeak [2026-01-18](https://x.com/PerceptualPeak/status/2012906116116627897)

现在正往北走，准备去一日单板滑雪小旅行～等我回家后，一定弄个可分享的仓库出来！

* * *

**Saad Naja** @SaadNaja [2026-01-18](https://x.com/SaadNaja/status/2012963451568783745)

所以我们终于不再每次新聊天都浪费自己的智慧了。不错。

* * *

**Zac** @PerceptualPeak [2026-01-18](https://x.com/PerceptualPeak/status/2012976512979325056)

懒惰主宰着我的生活，这包括将我每一个工作流程都优化到最大效率。更少的工作换来更多的产出 = 好的，求之不得 💅

* * *

**Ben Cera** @bencera\_ [2026-01-18](https://x.com/bencera_/status/2012967131692900593)

成功率和基础提示相比怎么样？

* * *

**Zac** @PerceptualPeak [2026-01-18](https://x.com/PerceptualPeak/status/2012975831136539108)

100%成功，我用的时候效果很好，但具体效果确实取决于使用场景。我开发这个是因为我想对我自己做的自定义 Claude 会话仪表盘做个小改动，但改动不够大，不需要重新加载整个该死的项目。

* * *

**Alex.Dev** @AlexBoudreaux13 [2026-01-18](https://x.com/AlexBoudreaux13/status/2012945020962197508)

喜欢这个想法

我担心找到完美的对话，但剩下的上下文窗口可能不够了

如果流程给你分叉命令和一个简洁命令，基于你正在尝试构建的内容以及它对过去对话的了解呢？