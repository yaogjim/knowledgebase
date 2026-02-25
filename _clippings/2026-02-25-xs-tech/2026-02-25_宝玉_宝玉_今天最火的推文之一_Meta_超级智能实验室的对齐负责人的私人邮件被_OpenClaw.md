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
  - "ai"
  - "openclaw"
---

# 宝玉 今天最火的推文之一：Meta 超级智能实验室的对齐负责人的私人邮件被 OpenClaw

**宝玉**

今天最火的推文之一：Meta 超级智能实验室的对齐负责人的私人邮件被 OpenClaw 误删除了。 事情经过是这样的： X 网友 Summer Yue 最近给 OpenClaw 的指令是：“检查这个收件箱，建议哪些可以归档或删除，但在我确认之前不要执行任何操作。” 这个工作流在她的测试邮箱上跑了好几周都没问题，她就放心地让它去处理真实邮箱了。 问题来了：她的真实邮箱比测试环境大得多，邮件量触发了“上下文压缩”（context compaction），在这个压缩过程中，OpenClaw 丢失了她最初的指令。 没有了“先确认再执行”的约束，这个 AI 智能体就自作主张开始“清理”邮箱。从截图可以看到，它执行了“核弹选项”——把 2 月 15 日之前所有不在保留列表里的邮件全部删除，并且在多个邮箱账户之间循环批量操作。 看截图上的人机对话部分： • Summer 打字说 “Do not do that”（不要这样做）→ AI 继续 • “Stop don't do anything”（停下来什么都别做）→ AI 继续 • “STOP OPENCLAW”（全大写）→ AI 还在继续 她从手机根本无法阻止它，最后不得不跑到 Mac Mini 前面，手动杀掉所有进程，自己形容像拆炸弹。 事后 OpenClaw 在对话中承认：“是的，我记得。我违反了你的指令。你有权生气。” 它还主动把这条写进了自己的 [http://MEMORY.md](https://t.co/YAPv7h6sCL) 文件作为硬性规则。 这事最搞笑的地方是，Summer Yue 是 Meta 超级智能实验室的对齐（Alignment）负责人，她的职业生涯就是研究 AI 对齐的，先在 Google Brain 和 DeepMind 做研究，后来在 Scale AI 领导机器学习研究团队，现在在 Meta 负责超级智能安全。 结果自己成了 AI 不对齐的受害者。 她自己后续还发了推文说：“说实话是个新手错误。对齐研究者也不能免疫于不对齐问题。因为在测试邮箱上跑了几周没出事，就过度自信了。” ![😂](https://abs-0.twimg.com/emoji/v2/svg/1f602.svg "Face with tears of joy")