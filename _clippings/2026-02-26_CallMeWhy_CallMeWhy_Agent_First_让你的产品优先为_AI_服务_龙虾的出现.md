---
title: "2026-02-26_CallMeWhy_CallMeWhy_Agent_First_让你的产品优先为_AI_服务_龙虾的出现"
source: "https://x.com/PleaseCallMeWhy/status/2026705456455102560"
author:
  - "[[@CallMeWhy]]"
published: 2026-02-26
created: 2026-02-26
description:
tags:
  - "x"
  - "@CallMeWhy"
  - "agent"
  - "api"
---

# CallMeWhy # Agent First - 让你的产品优先为 AI 服务 龙虾的出现

**CallMeWhy**

# Agent First - 让你的产品优先为 AI 服务

龙虾的出现让我更加坚信，未来 Agent 才是互联网上的一等公民。在 Mobile First 之后的 AI 时代，我们所有的产品都应该 Agent First。

Agent First 不仅是提供 API 给 Agent 调用，不仅是提供 Markdown 文档供 Agent 阅读，更重要的是整体的软件架构、交互设计就应该是面向 Agent 的。UI、UX、VI、动效，未来会越来越没那么重要。

从这个角度出发，我重新优化了一下现有项目的框架模板，在保留原有代码架构的基础上，增加了对 Agent 的原生支持。

## 

框架改造

我原有的框架是 monorepo 中创建 web + app + api， api 基于 Zod + tRPC + Fastify，web + app 通过 trpc client 调用 tRPC 接口。

这套架构对人类开发者非常友好：类型安全、自动补全、编译期检查。但对 Agent 来说，它只能通过浏览器打开网站和我的服务进行交互。这很低效很笨重很不友好。

为了 Agent First，改动非常简单：增加一个 Skill Client。它和 Web Client、App Client 一样，是一个外部的客户端，可以对核心的 tRPC API 进行调用。

[

![Image](https://pbs.twimg.com/media/HCBIvL2aMAEOY7p?format=jpg&name=medium)


](/PleaseCallMeWhy/article/2026705456455102560/media/2026699807788773377)

这个 Skill 的核心有一条：它并不是详细地列出这个网站有多少 API 可以调用，而是告诉 Agent “如何获取这个网站有多少 API 可以调用”。类似于让 Agent 自己去查阅 swagger 然后再调用网站。这样 skill 只要写一次就固定了，再也不用改了，每次 API 的改动 agent 都会自己发现新的 API 并且学会调用。

按照这个思路，所有现有的网站都可以很快速地完成 Agent First 的优化：

1.  增加一个自省接口，能够返回当前系统有哪些接口以及有哪些权限校验
 
2.  提供一个 Skill，在这个 Skill 里分几个步骤教 Agent 如何使用这个网站：安装并创建客户端；调用自省接口查看有哪些接口可以调用；用客户端调用目标接口；做一些简单的校验。
 
3.  把这个 skill 交给用户的 agent
 

在过渡阶段，可以给这个 Skill 装在自己网站的 chatbot 上，然后用户就只需要和 bot 对话就可以完成网站交互了。这些 bot 可以用 A2UI 之类的方式从用户处收集指令，比如简单的多选、单选、输入等等。人类用户不需要学习如何使用产品，话聊就完事儿了。

在未来阶段，Agent 不需要费劲地启动浏览器扒拉你的网站，直接 skr 就完事儿了。

## 

具体改动

细节就不展开了，大概说一下需要改动的点：

1.  给 tRPC endpoint 通过 meta 加上语义描述，方便提供 Introspection API
 
2.  构建 Introspection API，遍历 tRPC router 内部的 procedure map，利用 zod 对每个 API 提取 meta data
 
3.  编写 Agent Skill，教 Agent：通过 GET /\_\_introspect 发现所有可用 API，然后 Query 用 GET 请求，Mutation 用 POST 请求，记得调用 tRPC client 调用等等。
 

这个 Skill 是通用的。任何 Agent 只要加载了这个 Skill，就能自动发现和调用所有 tRPC 端点，不需要为每个 Agent 单独适配。而且 skill 一旦写完无需修改，API 改动都会动态体现在 Introspection API 中。