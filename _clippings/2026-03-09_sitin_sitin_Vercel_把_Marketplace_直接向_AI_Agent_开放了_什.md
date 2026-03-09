---
title: "2026-03-09_sitin_sitin_Vercel_把_Marketplace_直接向_AI_Agent_开放了_什"
source: "https://x.com/sitinme/status/2028672964951199934"
author:
  - "[[@sitin]]"
published: 2026-03-09
created: 2026-03-09
description:
tags:
  - "x"
  - "@sitin"
  - "ai"
  - "agent"
---

# sitin Vercel 把 Marketplace 直接向 AI Agent 开放了。 什

**sitin**

Vercel 把 Marketplace 直接向 AI Agent 开放了。

什么意思？一句话——以后基础设施这块，真的可以全自动了。

以前我们用 Claude Code、Cursor 这些 AI 编程工具，写代码已经很猛了，但真正上线一个项目，最麻烦的从来不是代码本身，而是那一堆“杂事”： 数据库要去注册，Redis 要单独开，认证服务要配，日志监控要接，邮箱服务要申请 API Key……

这些步骤过去基本都得人肉操作。AI 能写业务逻辑，却卡在基础设施这一步。

这次 Vercel 干了一件很关键的事： 不用搞 MCP Server，不用接新协议，直接把自家 CLI 包成一个 AI Skill。

一行命令： npx skills add vercel/vercel --skill vercel-cli

装完之后，Agent 就可以像人一样“逛 Marketplace”了。

它能做什么？ ·自动 discover 有哪些数据库、认证、日志服务 ·自动 add 安装 Neon、Upstash 这种服务 ·自动注入环境变量 ·自动读取接入文档 ·自己把集成代码写好

最后部署上线 你只需要说一句：“帮我做个带登录系统的待办 App，部署到 Vercel。” 剩下的流程，理论上 Agent 全跑完。

我觉得这件事的意义，不只是“方便”。也是在说：基础设施正在从“人操作”变成“Agent 可操作”。

以前：API 是给程序用的；文档是给人看的；CLI 是给人敲的

现在必须：返回结构化数据；支持无交互模式；提供机器可读文档；默认假设：调用者可能是 Agent 这其实是 SaaS 形态的一次升级。

未来能不能被 Agent 调用，可能会成为一个产品的生死线。 如果你的服务不能被自动发现、自动安装、自动配置，那在 AI 自动化流程里，它就会被绕开。

目前来说：项目搭建的“时间成本曲线”正在被压平。

过去从 0 到 1 搭一套完整基础设施，可能要 2～3 小时。 未来可能只是一句 prompt。

当部署成本无限接近 0，真正有价值的东西只剩两件： 1.你想解决什么问题 2.你是否有持续迭代能力

代码门槛在下降，基础设施门槛在消失。AI + 可编排基础设施，正在把“做产品”这件事，压缩到极致。

![图片](https://pbs.twimg.com/amplify_video_thumb/2028651804830162944/img/Ax4W-SY2P3CbGMlv.jpg)

[![视频](https://pbs.twimg.com/amplify_video_thumb/2028651804830162944/img/Ax4W-SY2P3CbGMlv.jpg)](https://x.com/sitinme/status/2028672964951199934)

* * *

### 热门回复

**@sitin** ♥ 4 · 💬 0

简单介绍下自己，方便大家交流 1. Python程序员，在成都，创业4年 2. 主要做知识付费，爬虫，RPA自动化机器人，AI工具等等。 这两天玩小龙虾OpenClaw，真的上瘾搞个小龙虾交流群，收49送50元 http:// aigocode.com 的Claude和codex算力。 感兴趣的欢迎添加vx：257735或扫码，联系付款进群。

**@Zhuxiaofeng** ♥ 2 · 💬 1

这个更新我今天第一时间测了。 一句「帮我加个数据库」，Agent直接跑去Marketplace找Neon、装好、配完环境变量。 以前这步要手动点半小时，现在真的全自动。 全栈项目的基础设施部分彻底解放了。

**@learner** ♥ 2 · 💬 1

我同意上线瓶颈一直在那些配置杂事，不在写代码本身。真放给 Agent 自动做之后，回滚和审计谁来兜底，你们现在怎么设这道闸？

**@Chaincruiser** ♥ 1 · 💬 1

确实，AI写写代码可能一小时，部署相关的数据库、账户认证、日志等各种配置可能得而消失

**@智算爱德华** ♥ 0 · 💬 1

AI 开始自动处理所有基础设施杂务，这是给程序员发退休证吗？