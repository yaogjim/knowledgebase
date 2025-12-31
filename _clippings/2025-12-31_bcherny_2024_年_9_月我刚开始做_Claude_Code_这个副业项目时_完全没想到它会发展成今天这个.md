---
title: "2025-12-31_bcherny_2024_年_9_月我刚开始做_Claude_Code_这个副业项目时_完全没想到它会发展成今天这个"
source: "https://x.com/bcherny/status/2004887829252317325"
author:
  - "[[@bcherny]]"
published: 2025-12-31
created: 2025-12-31
description:
tags:
  - "x"
  - "@bcherny"
  - "https"
  - "2025-12-27"
---

# 2024 年 9 月我刚开始做 Claude Code 这个副业项目时，完全没想到它会发展成今天这个

**Boris Cherny** @bcherny [2025-12-27](https://x.com/bcherny/status/2004887829252317325/history)

2024 年 9 月我刚开始做 Claude Code 这个副业项目时，完全没想到它会发展成今天这个样子。看到它成为这么多工程师的核心开发工具，社区有多热情，以及人们如何用它来做从编码、DevOps、研究到非技术用例的各种事情，真的让我感到很荣幸。这项技术既陌生又神奇，它让人们构建和创造变得容易得多。越来越多的是，代码不再是瓶颈了。

一年前，Claude 难以生成没有转义问题的 bash 命令。它每次只能工作几秒钟或几分钟。我们看到早期迹象，表明它有一天可能会在编程方面有广泛的用途。

快进到今天。过去 30 天里，我合并了 259 个 PR——497 次提交，新增 40,000 行代码，删除 38,000 行代码。每一行代码都是由 Claude Code 和 Opus 4.5 生成的。Claude 会持续运行数分钟、数小时乃至数天（使用 Stop hooks）。软件工程正在发生变革，我们正进入编码历史的新纪元。而我们还只是刚刚开始...

![Image](https://pbs.twimg.com/media/G9LGAh3WkAAbnBJ?format=png&name=large)

* * *

**Simon Willison** @simonw [2025-12-27](https://x.com/simonw/status/2004916070973645242)

Claude 持续运行几分钟、几小时甚至几天（使用 Stop hooks）

能再展开说说吗？我不明白 Stop hooks 如何能增加使用时长

* * *

**Boris Cherny** @bcherny [2025-12-27](https://x.com/bcherny/status/2004916410687050167)

当 Claude 停止时，你可以使用停止钩子来戳它以继续运行。例如，查看 https://github.com/anthropics/claude-plugins-official/tree/main/plugins/ralph-wiggum…

* * *

**Loredana Cirstea** @lorecirstea [2025-12-27](https://x.com/lorecirstea/status/2004901936496066674)

你已经有我还不知道的针对这个的解决办法了吗？

tldr: 如果 Claude 看到用户编写的现有代码，应该认为该代码有其用途，即使它与内部数据冲突；并且，与其重写代码，不如询问用户。

Claude 会吗？

* * *

**Boris Cherny** @bcherny [2025-12-27](https://x.com/bcherny/status/2004903500497781246)

Claude 理解用户何时修改了代码，何时代码被修改，特别是在使用较新模型时。

* * *

**Model Moment** @vibercoding [2025-12-27](https://x.com/vibercoding/status/2004941333941895601)

具体是哪一天？那将是一个值得铭记的日子，也应该成为一个基准，看看其他竞争对手是更早还是更晚。

* * *

**Boris Cherny** @bcherny [2025-12-27](https://x.com/bcherny/status/2004942545265295462)

❯ 你第一次提交是什么时候？

● Bash( Git 提交记录 --逆序 --格式="%H %ci %s" | 取第一行 )

⎿ 6dc1dc3 2024 年 9 月 14 日 20 时 33 分 01 秒 -0700 🌅

● 第一个提交是在2024年9月14日20:33:01（太平洋夏令时），提交信息为：🌅。

* * *

**Tino Wening** @TinoWening [2025-12-27](https://x.com/TinoWening/status/2004933932446372347)

但你怎么知道模型不会通过简单的字符串比较来写测试，从而即使有明确的成功标准，测试也能通过呢？模型往往很有用。哪些任务或功能不需要人工干预？

* * *

**Boris Cherny** @bcherny [2025-12-27](https://x.com/bcherny/status/2004935051545321685)

这在 Sonnet 3.7 版本时是个问题，但随着模型变得更强大，我发现它现在不再会这样了。随着模型的改进，最困难的部分是不断调整你对它能力的预期。对于模型做得不完美的那些事情，把它加入到你的...

* * *

**Louie** @gmitslouie [2025-12-27](https://x.com/gmitslouie/status/2004900307877409038)

你使用 Claude Code 的最大技巧是什么，以及你个人会在哪些方面避免使用它？

* * *

**Boris Cherny** @bcherny [2025-12-27](https://x.com/bcherny/status/2004901145727340665)

* * *

**Abubakar Tanko** @maigadohcrypto [2025-12-28](https://x.com/maigadohcrypto/status/2005299362910572793)

我对它唯一的问题是回滚更改，它不像在 Cursor 里那样能回滚更改，我们需要能回滚会话中某些更改的功能

* * *

**Boris Cherny** @bcherny [2025-12-28](https://x.com/bcherny/status/2005300079880712559)

按两次 ESC 键

* * *

**Yash Gourav Kar** @YashGouravKar1 [2025-12-27](https://x.com/YashGouravKar1/status/2004891837597974906)

你过去 30 天里没有为 Claude Code 写过一行代码？？

* * *

**Boris Cherny** @bcherny [2025-12-27](https://x.com/bcherny/status/2004897269674639461)

对的。在过去三十天里，我对 Claude Code 的 100%贡献都是由 Claude Code 编写的。

* * *

**Levon** @levon96 [2025-12-27](https://x.com/levon96/status/2004905494495043595)

你如何管理 Claude 在长时间运行任务中的上下文？

它不会在最初几分钟内就被填满吗？

* * *

**Boris Cherny** @bcherny [2025-12-27](https://x.com/bcherny/status/2004905659603845256)

Claude 一般都能自己弄明白。我唯一手动做的事情就是在大多数会话开始时进入计划模式。

* * *

**Rohan Seth** @rohan\_seth18 [2025-12-29](https://x.com/rohan_seth18/status/2005616877767467405)

当 CC 已经运行了好几天并且边运行边压缩时，你如何确保它在压缩时有正确的上下文？

最好能有一个紧凑阈值的选项，你可以把它设为 token 的 60%，然后使用一个 preCompact 钩子，在你提供确切信息时

* * *

**Boris Cherny** @bcherny [2025-12-29](https://x.com/bcherny/status/2005634865438572717)

Claude 应该会自动弄明白。如果你发现它偏离了轨道，请告诉我们。

* * *

**Jitesh Ghanchi** @JiteshGhanchi [2025-12-27](https://x.com/JiteshGhanchi/status/2004900562547200449)

请添加 UI 到它

* * *

**Boris Cherny** @bcherny [2025-12-27](https://x.com/bcherny/status/2004900832366809475)