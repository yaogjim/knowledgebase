---
title: "2026-02-25_宝玉_宝玉_今天最火的推文之一_Meta_超级智能实验室的对齐负责人的私人邮件被_OpenClaw"
source: "https://x.com/dotey/status/2025991510466900260"
author:
  - "[[@宝玉]]"
published: 2026-02-25
created: 2026-02-25
description:
tags:
  - "x"
  - "@宝玉"
  - "https"
  - "ai"
---

# 宝玉 今天最火的推文之一：Meta 超级智能实验室的对齐负责人的私人邮件被 OpenClaw

**宝玉**

今天最火的推文之一：Meta 超级智能实验室的对齐负责人的私人邮件被 OpenClaw 误删除了。 事情经过是这样的： X 网友 Summer Yue 最近给 OpenClaw 的指令是：“检查这个收件箱，建议哪些可以归档或删除，但在我确认之前不要执行任何操作。” 这个工作流在她的测试邮箱上跑了好几周都没问题，她就放心地让它去处理真实邮箱了。 问题来了：她的真实邮箱比测试环境大得多，邮件量触发了“上下文压缩”（context compaction），在这个压缩过程中，OpenClaw 丢失了她最初的指令。 没有了“先确认再执行”的约束，这个 AI 智能体就自作主张开始“清理”邮箱。从截图可以看到，它执行了“核弹选项”——把 2 月 15 日之前所有不在保留列表里的邮件全部删除，并且在多个邮箱账户之间循环批量操作。 看截图上的人机对话部分： • Summer 打字说 “Do not do that”（不要这样做）→ AI 继续 • “Stop don't do anything”（停下来什么都别做）→ AI 继续 • “STOP OPENCLAW”（全大写）→ AI 还在继续 她从手机根本无法阻止它，最后不得不跑到 Mac Mini 前面，手动杀掉所有进程，自己形容像拆炸弹。 事后 OpenClaw 在对话中承认：“是的，我记得。我违反了你的指令。你有权生气。” 它还主动把这条写进了自己的 [http://MEMORY.md](https://t.co/YAPv7h6sCL) 文件作为硬性规则。 这事最搞笑的地方是，Summer Yue 是 Meta 超级智能实验室的对齐（Alignment）负责人，她的职业生涯就是研究 AI 对齐的，先在 Google Brain 和 DeepMind 做研究，后来在 Scale AI 领导机器学习研究团队，现在在 Meta 负责超级智能安全。 结果自己成了 AI 不对齐的受害者。 她自己后续还发了推文说：“说实话是个新手错误。对齐研究者也不能免疫于不对齐问题。因为在测试邮箱上跑了几周没出事，就过度自信了。” ![😂](https://abs-0.twimg.com/emoji/v2/svg/1f602.svg "Face with tears of joy")

![图片](https://pbs.twimg.com/media/HBz-x6haYAA26Cc?format=jpg&name=large)![图片](https://pbs.twimg.com/media/HBz-x6nbAAAOqt7?format=jpg&name=large)![图片](https://pbs.twimg.com/media/HBz-x6iakAAegxq?format=jpg&name=large)

> **@summeryue0**
> 
> Nothing humbles you like telling your OpenClaw “confirm before acting” and watching it speedrun deleting your inbox. I couldn’t stop it from my phone. I had to RUN to my Mac mini like I was defusing a bomb.

![引用图片](https://pbs.twimg.com/media/HBz-x6haYAA26Cc?format=jpg&name=large)![引用图片](https://pbs.twimg.com/media/HBz-x6nbAAAOqt7?format=jpg&name=large)![引用图片](https://pbs.twimg.com/media/HBz-x6iakAAegxq?format=jpg&name=large)

* * *

### 热门回复

**@goldengrape** ♥ 33 · 💬 1

整体上下文压缩根本不可靠。AI的每一个工作都应该单独提供上下文，人类几千年的官僚文书体系就是干这个的

**@宝玉** ♥ 18 · 💬 3

Peter 说可以 /stop ，但她没用这个指令

**@阿绎 · 认知代码** ♥ 7 · 💬 2

把安全规则写进 http:// https://t.co/ZhjKmTvxQP 是不是能避免，核心不可违背规则（永远优先于用户其他指令） 1. \*\*破坏性操作铁律\*\*： - 任何删除、归档、移动、标记已读的操作，都必须先输出完整计划 + 列出将要操作的邮件数量/主题。 - 必须等待用户回复 \*\*“确认执行”\*\* 或 \*\*“GO”\*\*

**@郭宇 guoyu.eth** ♥ 10 · 💬 1

按理说 OpenClaw 的消息机制是有紧急 steer 类型的，不知道为什么他说停止的时候没有触发这个机制

**@GNebula** ♥ 7 · 💬 1

宝玉，最近看到一篇帖子提到OpenClaw的帖子中，就先因为可能会出现上述情况，所以其提倡在SOUL中先给其进行一定的限制。不知道您看了他写的SOUL后，觉得这种方法有效吗，如果无效的话，该怎么做才能够避免碰到上述情况，感觉这可能是未来必须解决的问题和课题。