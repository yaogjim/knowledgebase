---
title: "2026-03-06_Viking_Viking_这篇文章是今天看到最精彩的文章_是一篇技术深度逆向工程实验_成功从_Codex"
source: "https://x.com/vikingmute/status/2029539099636576361"
author:
  - "[[@Viking]]"
published: 2026-03-06
created: 2026-03-06
description:
tags:
  - "x"
  - "@Viking"
  - "codex"
  - "cli"
---

# Viking 这篇文章是今天看到最精彩的文章，是一篇技术深度逆向工程实验，成功从 Codex

**Viking**

这篇文章是今天看到最精彩的文章，是一篇技术深度逆向工程实验，成功从 Codex CLI 的 compact() API中提取出了隐藏的系统提示。 非常好地解释了 Codex CLI 在使用自己模型，在长上下文管理上的实际运行方式，几乎把黑箱内部机制扒得一清二楚。 1 当上下文太长时，不是简单丢弃历史，而是调用 compact() API 2 服务器用一个专用的 compactor LLM，把整个对话历史总结成一个精炼的“handoff summary”。 3 这个 summary 被 AES 加密成 blob 返回给客户端 4 下次 responses.create() 时，客户端把 blob 传回去，服务器解密后总结，一起喂给 codex 主模型。 5 模型无缝接力继续工作，不会因为压缩而严重失忆或漂移。 这解释了为什么 Codex 在长任务上连续性特别强。 配图也很棒，非常好的科普文章。

![图片](https://pbs.twimg.com/media/HCpe5TfawAA05TM?format=jpg&name=large)

* * *

### 热门回复

**@DanielW** ♥ 540 · 💬 8

Ai2绝对是我见过最无私、开发的ai lab 不仅开源模型，还开源预训练、微调脚本、训练代码（infra codebase）、训练数据、数据处理代码等等 是入门ai research的宝藏

**@Mr Panda** ♥ 368 · 💬 53

我有点后知后觉得了， 程序员出海， 也不用费劲吧啦搞产品了， 先把自己劳动力卖出去， 比如上upwork 或者是fiverr 去接单啊 ， 这是来钱最快的方式了。 我感觉月入万刀比搞SEO会容易一些。

**@victor-wu.eth** ♥ 346 · 💬 13

已经要被claude code在产品层面的能力震惊到说不出来话了，新上的Skill-Creator 可以用来改进用户自己创建的 skill 。其中有一个功能是这样的，直接进行变量控制，根据skill的功能，创建一份prompt，一份经过skill处理，一份不经过skill处理，只用原始的prompt，然后直接对比两份结果，作为下一步修改的基准参考。 我只能说当看到这个功能，我作为 PM 感觉到五体投地，claude code 在产品设计上真的是领先太多身位了，学吧，好好学吧，说的就是你 codex。

**@Tantan Fu** ♥ 171 · 💬 2

非常值得学习，如何利用 agent 完成更大的项目 不知 Ralph loop 是否是由此演化出来的 https:// anthropic.com/engineering/ef fective-harnesses-for-long-running-agents …

**@kensen Kensen** ♥ 17 · 💬 1

这玩意的代码不是开源的吗？什么时候需要逆向了