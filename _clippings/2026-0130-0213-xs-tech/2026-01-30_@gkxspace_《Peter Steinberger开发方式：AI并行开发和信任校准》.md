---
title: "《Peter Steinberger开发方式：AI并行开发和信任校准》"
source: "https://x.com/gkxspace/status/2017012379523924115"
author:
  - "[[@gkxspace]]"
date: "2026-01-30T18:55:09+08:00"
created: 2026-01-30
description:
tags:
  - "@gkxspace #  AI开发 #  机器人 #  程序员 #  技术产品经理 #  代码生成 #  决策能力 #  SaaS #  内容矩阵"
---
**余温** @gkxspace 2026-01-29

“如果你能驾驭这些工具，你现在的产出速度能媲美一年前的一家公司。”

这话是Peter Steinberger说的。他用66天，8297次commit，创造了Moltbot。

我觉得他的开发方式挺有参考价值的：

同时运行4个AI Agent并行开发。

不同Agent负责不同模块。UI、测试、重构、新功能，各干各的。

用原子化commit作为同步点，冲突了再由他来仲裁。

这个“信任校准”也挺有参考意义的：

OpenAI Codex 95%信任度可直接合并，Claude Code 80%需要快速review，其他模型低于70%需仔细检查。

知道什么时候信任AI，什么时候人工把关，这点确实牛，也能看出，AI在有能力的人手里能发挥最大的价值。

尽管我还没玩起来Moltbot（我马上就去玩），但无论如何Peter Steinberger这套流程是真厉害，这篇文章也是一篇深度好文了。

或许，一人公司，不再是理想。

> 2026-01-29
> 
> ![Article cover image](https://pbs.twimg.com/media/G_y1Nn3bUAEHMgN?format=jpg&name=large)

---

**AI绍宇-翻身记** @ShaoyuL8844 [2026-01-30](https://x.com/ShaoyuL8844/status/2017149699225206909)

未来的“程序员”本质上都是“技术产品经理” (TPM)。

以前我们 80% 的时间在写 if-else，现在 80% 的时间应该花在定义架构、拆解原子化任务、以及做 Peter 所说的“冲突仲裁”上。代码生成能力已经溢出了，决策能力才是现在的稀缺资源。

感觉这一套流程跑通后，SaaS 的验证周期能从“月”压缩到“周”。有人试过用这套逻辑做非代码类的任务吗（比如内容矩阵）？感觉也通用

---

**OIAC: Organization of Iranian American Communities** @OrgIAC

We are proud supporters of the Ten-Point Plan for Iran’s Future which was first presented by Maryam Rajavi, the President Elect of the National Council of Resistance of Iran (NCRI) in December 2006 at a session of the Council of Europe.