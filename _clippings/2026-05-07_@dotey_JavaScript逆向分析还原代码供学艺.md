---
title: "JavaScript逆向分析还原代码供学艺"
source: "https://x.com/dotey/status/1981586724988858442"
author:
  - "[[@dotey]]"
date: "2026-05-07T22:59:07-07:00"
created: 2026-05-07
description: "我其实也经常逆向优秀的 JavaScript 代码，以前手动，现在借助 AI 效率奇高，绝大部分代码都能借助 AI 还原。这事一是要有耐心，另一个就是要懂技术实现。 给 Codex/Claude Code 提示词也很简单： 我不小心把源码弄丢了，只剩下编译后 js 文件 aaa"
tags:
  - "@dotey # JavaScript逆向分析 # AI逆向工具 # 源码还原 # TypeScript"
---
我其实也经常逆向优秀的 JavaScript 代码，以前手动，现在借助 AI 效率奇高，绝大部分代码都能借助 AI 还原。这事一是要有耐心，另一个就是要懂技术实现。

给 Codex/Claude Code 提示词也很简单：

我不小心把源码弄丢了，只剩下编译后 js 文件 aaa.js，请你帮我还原成命名友好的 TypeScript 版本，保存到 xxx 目录下，先从 yyy 开始，还原所有相关代码，不需要编译通过，只需要 1:1 还原。 https://x.com/manateelazycat/manateelazycat/status/1981572409200373846…

> **Andy Stewart @manateelazycat** · 2025-10-24
> 
> 逆向不是每个人都可以学习的
> 
> 我认识的一个人，国内微信逆向第一人，他的气质才适合做逆向
> 
> 锲而不舍的研究代码，看超级长的汇编，他为了攻克一个问题，可以十多天不出门，就一直死磕汇编和寄存器的变化。
> 
> 现在成为国内微信逆向工具的鼻祖，基本上你们要的所有微信的工具他都可以实现。 x.com/GitHub\_Daily/s…

---

比如这是 Claude Code VSCode Extension 逆向后代码😂

![Image](https://pbs.twimg.com/media/G4ANrGrWAAAAdyw?format=jpg&name=large)

---

对目录进行逆向，需要在 Agents .md（CC就是 Claude md） 里面：

1\. 定义好目录结构，源文件夹路径、逆向后文件夹路径

2\. 先让它分析并生成一个 Plan 文件，再基于 Plan 生成一个 TODO 文件跟踪进度

3\. 引导 Agent 开始任务前阅读 Plan 和 TODO，完成任务后更新 TODO

> **artest @tearilize** · 2025-10-24
> 
> 单个文件效果不错，不知道大神有没有对整个目录文件的逆向提示词。

---

## Comments

> **耳朵 @RookieRicardoR** · [2026-02-03](https://x.com/RookieRicardoR/status/2018694952780259721)
> 
> 今天让它从一堆混淆 js 中找代码，它一直是调用 Python 帮我找的，不知道为啥
> 
> > **宝玉 @dotey** · [2026-02-03](https://x.com/dotey/status/2018696418530124053)
> > 
> > 这是codex特色，更喜欢用python代码
> > 
> > > **耳朵 @RookieRicardoR** · [2026-02-04](https://x.com/RookieRicardoR/status/2018986132420345974)
> > > 
> > > 我专门写过一篇🌚
> > > 
> > > > **耳朵 @RookieRicardoR** · 2026-01-19
> > > > 
> > > > 这个问题我思考了两天，先说结论：Codex 的 Python 优先策略更好。
> > > > 
> > > > 1️⃣ 兼容性
> > > > 
> > > > 从兼容性来讲，Bash 脚本中的一些同名命令，在 Macos 和 Linux 平台执行的结果是完全不一样的，因为 MacOS 基于 BSD Unix，而 Linux 基于 GNU。
> > > > 
> > > > Windows 就不用提了，完全没有内置的 Bash命令。
> > > > 
> > > > 2️⃣ 可移植性 x.com/dotey/status/2…
> > > > 
> > > > ![Image](https://pbs.twimg.com/media/G-9dRqvWIAAYfhe?format=jpg&name=large)

> **ImCola @AliMobile** · [2025-10-24](https://x.com/AliMobile/status/1981595749491134917)
> 
> 已学习👍

> **kkos @kkos27385050** · [2025-10-25](https://x.com/kkos27385050/status/1982100310207455690)
> 
> 1、逆向一个网站的JS代码？还是一两个js文件？token长度不够用吧？
> 
> 2、js的逆向还是比汇编简单太多了。
> 
> > **宝玉 @dotey** · [2025-10-25](https://x.com/dotey/status/1982121259132473421)
> > 
> > 1\. agent会检索部分代码，而不会加载所有，不会长度不够
> > 
> > 2\. 是

> **Steven @0xStevenX** · [2025-10-24](https://x.com/0xStevenX/status/1981592805874307538)
> 
> 这提示词可以😆

> **Micro Bubbles @Micr0\_Bubbles** · [2025-10-24](https://x.com/Micr0_Bubbles/status/1981723457995132956)
> 
> 如果是jsc文件就很难逆向复原了

> **thu @P37940Thu** · [2025-10-24](https://x.com/P37940Thu/status/1981706854515593609)
> 
> 怎么防止逆向编程被破解了，是常规混淆加密都不行是吗

> **嘣呒哏儿 @bengmugenr** · [2025-10-24](https://x.com/bengmugenr/status/1981630587950768636)
> 
> 给 AI 的提示词非得这么客气吗？说“逆向分析还原代码供学艺”，它干不？

> **zeromike @coolzeromike** · [2025-10-24](https://x.com/coolzeromike/status/1981645385845346495)
> 
> 学到了，nb

> **Max @erdaye\_2o25** · [2025-10-26](https://x.com/erdaye_2o25/status/1982287956540088670)
> 
> 真优秀。

> **taichi @0xtaichim** · [2025-10-24](https://x.com/0xtaichim/status/1981620007131115604)
> 
> 宝玉老师说的是逆向混淆后的JS代码，Andy提到的是逆向国内微信那种，涉及更底层的协议分析和反编译，HOOK，注入，栈帧，基址，汇编，破解那种

> **artest @tearilize** · [2025-10-24](https://x.com/tearilize/status/1981777321871696064)
> 
> 单个文件效果不错，不知道大神有没有对整个目录文件的逆向提示词。

> **信天翁大跌眼镜 @wenhuiwang10** · [2025-10-24](https://x.com/wenhuiwang10/status/1981623697380348127)
> 
> 如果混淆的文件太多要怎么办呢