---
title: "electron 代码逆向还原之路"
source: "https://x.com/dotey/status/2018187857643417623"
author:
  - "[[@dotey]]"
date: "2026-05-07T22:57:17-07:00"
created: 2026-05-07
description: "我早年写了一个 Electron 画图程序，源码丢了，只剩一个编译后的版本。我想过重写，但一想到要从零复现那些细节就头大。看了 OpenAI 那篇“28 天用 Codex 做出 Sora Android App”的博客 (https://baoyu.io/blog/sora-an..."
tags:
  - "@dotey # electron # codex # electron-forge # typescript # electron-ui # asar # AGENT.md # PLAN.md # npm"
---
![Image](https://pbs.twimg.com/media/HAIKsgpWgAAo0QC?format=jpg&name=large)

我早年写了一个 Electron 画图程序，源码丢了，只剩一个编译后的版本。

我想过重写，但一想到要从零复现那些细节就头大。看了 OpenAI 那篇“28 天用 Codex 做出 Sora Android App”的博客 ([https://baoyu.io/blog/sora-android-85-ai-code-development-method](https://baoyu.io/blog/sora-android-85-ai-code-development-method) )，我突然有了个想法：既然编译后的代码还在，能不能让 Codex 帮我“逆向还原”出源代码？

**5 天后，我拿到了一份能正常运行的 TypeScript 源代码。**

![Image](https://pbs.twimg.com/media/HAIKvE0WcAA1oaB?format=jpg&name=large)

## 从混淆代码里挖出模块结构

Electron 应用打包后，代码都压在 asar 文件里。第一步是让 Codex 从里面把 js 和 css 文件提取出来。

提取出来的 js 是编译混淆过的，变量名全是 a、b、c，函数调用链乱成一团。人眼看着就晕，但对 Codex 来说，这只是另一段代码。

我让 Codex 分析主要的 js 文件，把里面的模块列表整理出来。它真的做到了。虽然原始的模块名已经丢失，但从代码结构和功能逻辑，它还原出了一份相当完整的模块清单。

有了这份清单，我让 Codex 制定还原计划：把每个模块从混淆后的 JavaScript 还原成可读的 TypeScript 代码。清单变成了一个 checklist，每完成一个模块就打个勾。

![Image](https://pbs.twimg.com/media/HAIKxtoXUAEURek?format=jpg&name=large)

## 第一个坑：Codex 太想"证明自己"

刚开始还原的时候，我遇到了一个问题。

Codex 有一种执念：它特别想验证生成的代码能跑。为了让代码能 build 通过，它会悄悄删减内容，跳过一些它觉得“暂时用不上”的部分。

这对于写新代码是好习惯，但对于还原旧代码是灾难。**我需要的是完整还原，不是能编译的最小子集。**

解决方法很简单，我在 AGENT.md 里加了一条强规则：

> “按照模块挨个还原即可，不需要保证编译通过。”

这一行字改变了一切。Codex 不再纠结于编译错误，开始老老实实地一个模块一个模块还原。

![Image](https://pbs.twimg.com/media/HAIK0ZAXMAA_SDM?format=jpg&name=large)

## 第二个坑：上下文满了，记忆就没了

Codex 的上下文窗口是有限的。早期版本跑到一定程度就会停止，我得不停输入 continue。新开会话的话，又要重新介绍任务背景。

我的解决方案是建立一套“外部记忆”系统：

1. 在 AGENT.md 里介绍当前任务的整体背景
2. 创建 PLAN.md 文件，记录还原计划和当前进度
3. 在 AGENT.md 里加一条规则：每次启动必须先读 PLAN.md，每轮任务结束后必须更新 PLAN.md

这样，每次新开会话只需要输入“continue”，Codex 就会自动读取进度，接着上次的位置继续干活。

后来我连手动新开会话都懒得做了。让 Codex 帮我写了一个脚本，定时检测上下文是否接近上限，自动新开会话并输入 continue。

于是我就看着它自己在那儿跑。过一会看看进度，又有几个模块完成了。

![Image](https://pbs.twimg.com/media/HAIK3G8XUAAZQ2j?format=jpg&name=large)

## 把碎片拼成完整的应用

几天后，所有模块都还原成了 TypeScript 文件。但这还只是一堆散落的零件。

下一步是把它们组装成一个真正能跑的 Electron 应用。我让 Codex 用 Electron Forge 脚手架创建了一个新项目，然后把还原的代码放进去。

这时候我重写了 AGENT.md 和 PLAN.md，告诉 Codex 如何编译和测试，然后用同样的套路：自动新开会话、continue、更新 PLAN。

我看着 Codex 不停地修复编译错误。它会去原来编译后的代码里验证逻辑，用 npm start 运行应用检查效果，发现问题就修，修完继续下一个。

等模块基本能编译通过后，我和 Codex 一起写了集成测试，覆盖几个主要的使用流程。写好测试后，又是同样的循环：让它自己生成代码、跑测试、修问题。

![Image](https://pbs.twimg.com/media/HAIK5wdWoAASVIt?format=jpg&name=large)

## 五天后

第五天结束的时候，我拿到了一个有完整源代码、能正常运行的 Electron 应用。

说“完美还原”肯定是夸张了。运行时还有一些小 bug，有些边缘功能的行为和原来不太一样。但主要功能都在，整体结构清晰，最重要的是，**我终于可以改代码了**。

## 我学到的东西

很多人说 Codex 不需要外部循环机制。我觉得这是错的。

对于长任务，Codex 需要一个类似 ralph-loop 的 plugin。否则你就得像我一样，自己写脚本去定时新开会话、输入 continue。这明明应该是内置功能。

**几点经验：**

![Image](https://pbs.twimg.com/media/HAIK8cYWYAE6L-E?format=jpg&name=large)

1. **Plan 和 checklist 对长任务至关重要。** 每一轮任务完成后必须更新进度，否则上下文一断，前面的工作就白费了。
2. **为 Codex 提供验证方法同样重要。** 我能让它自动修 bug，是因为它能自己跑 npm start 看效果、跑测试看结果。没有验证手段，Codex 就只能盲写。
3. **有时候你得明确告诉 Codex 什么不用做，它才能专注于真正需要做的事。** 那条“不需要保证编译通过”的规则就是例子。

OpenAI 那篇博客讲的是用 Codex 在 28 天内从零构建一个生产级应用。我的故事正好相反：用 Codex 在 5 天内把一个丢失了源码的应用“逆向还原”成源代码。

方向不同，核心方法论一样：把 Codex 当成一个能力很强但需要明确指令的队友，建立外部记忆系统保持连续性，提供验证手段让它能自我纠错。 