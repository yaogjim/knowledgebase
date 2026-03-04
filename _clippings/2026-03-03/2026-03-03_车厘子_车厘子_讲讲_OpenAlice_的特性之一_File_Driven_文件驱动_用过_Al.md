---
title: "2026-03-03_车厘子_车厘子_讲讲_OpenAlice_的特性之一_File_Driven_文件驱动_用过_Al"
source: "https://x.com/0xcherry/status/2028389161817022671"
author:
  - "[[@车厘子]]"
published: 2026-03-03
created: 2026-03-03
description:
tags:
  - "x"
  - "@车厘子"
  - "ai"
  - "alice"
---

# 车厘子 讲讲 OpenAlice 的特性之一：File-Driven（文件驱动） 用过 Al

**车厘子**

讲讲 OpenAlice 的特性之一：File-Driven（文件驱动） 用过 Alice 的朋友们应该有个体会：这玩意的启动简单到离谱。除了要配一堆 API KEY ，就没什么需要折腾的地方了。 而且 Alice 不吃设备。2GB 的内存对 Alice 来说绰绰有余。甚至更小点都没有问题。连我家里的老红米 K20 pro 也能顺利运行。 OpenAlice 最早的定位跟 OpenClaw 类似，是“运行在用户电脑上的长命 Trading Agent”。 交易是个长周期的 Loop，有买有卖有调仓，因此处理交易的 Agent 也必须是持久运行的。这一点跟 OpenClaw 也很像。 mac mini 最近卖的好，是因为 OpenClaw 需要持久运行，而 mac mini 是最适合持久运行且系统稳定的消费级设备。 对于不擅长折腾、手头没有多余设备的用户来说，配 OpenClaw 就很麻烦了。500 块钱上门安装 OpenClaw 的服务就这么出来的。 所以。任何需要长期运行在终端上的 Agent，都会面对一连串的问题。因为吃性能，所以挑设备；因为挑设备，所以更不好配置；因为不好配置，所以大部分人折腾不来。 因此我们做了一个简单的处理：把 Alice 的状态和持久化部分转入文件。 具体的来说，我们做了如下的选择： - 没有依赖 PG 或 Redis 等数据库，使用文件进行持久化。 - 对于 Alice 如何执行任务的指导，使用 prompt 形式存储在 markdown 文件里，人类/AI 可读可写 - 当文件被修改时，引入版本管理的设计，任何文件的修改都是可以回溯的 当我们引入 File-Driven 的设计理念后，这几个问题全解决了。 - 文件是免配置的，是系统就能跑。有手就行。 - 文件配置的初始内存占用非常低。一套 redis+PG 能轻松吃进去 1到2GB 的内存。租个云实例 2GB 内存全被这玩意吃了。而文件占用的是容量，谁电脑还没个 128GB 容量。 我们希望 OpenAlice 开箱即用、占用更小。这样，无论是新手还是老手都不会觉得有压力。File-Driven 的特性很好地解决了这些问题。 不仅如此，我们发现这个特性的潜力很大： - 文件是 OS 的一等公民，能操作文件就能操作 OS，长期功能规划的潜力更大 - 文件对人类和 AI 都是可读可修改的，即使完全没写过代码的人，至少也会编辑文本。在 AI 运行的过程中如果需要监控或手动调节状态，直接看文件改文件就行了。 - AI 编程的本质就是文件读写，现在许多 AI 公司都会对编程场景进行单独优化。当我们把 Trading 等效为文件读写问题后，所有现有 AI 模型对编程场景的优化都会提高 Trading 的性能。 这么诡异的思路，我是怎么想到的？ 我第一次接触到 File-Driven 的概念，是因为我搭信息源服务的时候用了 Crawlee 的爬虫框架，发现可以做到免配置启动。 Crawlee 的基础理念就是File-Driven+单租户，云端跑实例就等于跑了一个单租户的爬虫服务器，因为File-Driven 的缘故，导致服务器实例可以开的特别小。他们就靠这个来降低门槛。 然后我学点阴招全给 Alice 用上了。希望大家喜欢吧。 项目地址：[https://github.com/TraderAlice/OpenAlice…](https://github.com/TraderAlice/OpenAlice)

![图片](https://pbs.twimg.com/media/HCZHLmobsAArLGO?format=jpg&name=large)

* * *

### 热门回复

**@Steve Shultz** ♥ 4.8K · 💬 0

Pulling out your ID is normal in America. Why shouldn’t voting be the same? Election integrity isn’t extreme. It’s common sense. Follow for more conversations like this.

**@karminski-牙医** ♥ 960 · 💬 26

Apple ANE 被成功逆向! 38TOPS 算力其实是数字游戏? 刚刷到博主 maderix 开源了个硬核项目: 逆向 Apple 的私有 API, 绕过 CoreML, 直接在 Apple Neural Engine (ANE) 上实现了神经网络训练! 等会? 啥是 ANE? ANE是苹果芯片内部的神经网络加速单元, M4 上目前已经是 16 核的运算单元了,

**@KevinZ 𝟎𝐱𝐔** ♥ 489 · 💬 13

目前使用Claude下来，个人觉得最值得花精力迭代维护的文档： 你的工作准则 Claude.md 术语表与定义库 glossary.md 外部接口与资源 toolbox.md 你的技能树 Skills.md 每次任务的记录与复盘 memory.md

**@歸藏(guizang.ai)** ♥ 337 · 💬 19

牛批，还是 Telegram 开放！ 第一个为 OpenClaw 专门适配机器人 API 的，目前Telegram 所有类型聊天机器人都已经支持流式传输 具体适配方式可以让你的 AI 查找 API 文档中的 sendMessageDraft 方法 或者直接把我下面的链接发给他

**@✧ 𝕀𝔸𝕄𝔸𝕀 ✧** ♥ 181 · 💬 11

不需要100万美元，不需要10万美元，也不需要1万美元，只需要一块RTX3090华强北加强版，你就能永久性脱离贫困，实现富足生活。