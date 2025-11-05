---
title: "2025-11-04_vista8_我发现Agent生成的内容_甚至不如Prompt直接生成_咨询_Cydiar404_他给的一些"
source: "https://x.com/vista8/status/1984435830480650602"
author:
  - "[[@vista8]]"
published: 2025-11-04
created: 2025-11-04
description:
tags:
  - "@vista8"
  - "@Cydiar404"
  - "@dotey"
  - "@ZayenOne"
  - "agent"
  - "https"
  - "image"
  - "//pbs"
  - "twimg"
  - "x.com"
---

# 我发现Agent生成的内容，甚至不如Prompt直接生成。 咨询 @Cydiar404 ，他给的一些

**向阳乔木** @vista8 2025-10-31

我发现Agent生成的内容，甚至不如Prompt直接生成。

咨询 @Cydiar404 ，他给的一些经验分享。

为什么不推荐过度依赖快速 Agent 框架？

像CrewAI这种开箱即用的Agent框架虽然简单，但无法定制细致功能。

当产品需要深度交互时，框架力不从心了。比如 Agent Builder GUI、细致节点监测、特殊 Agent 定制，这些都做不了。

另外，市面上很多任务，一个 ReAct Loop 就能完成。

大多数场景根本用不到 Multi-Agent，因为很多任务都是完整基于上文的——上文没产生，就不会有下文。

甚至有些时候，Multi-Agent 的产出还不如单 ReAct 循环。

Agent 底层框架的真正意义在于对整个闭环监控的把控，可以真正实现 Agentic RL。

否则，很多任务根本不需要 Agent。

复杂任务真正考验的是上下文管理、规划能力，以及多 Agent 任务状态的同步。

快速框架的优势是 0-1 非常快，直接定义 Agent Instructions 就可以用。

但数据持久化是一个重点问题，因为这涉及到数据和形态之间的转换。

> 2025-10-31
> 
> 原来开发一个AI Agent比想象中简单。
> 
> 用CrewAI框架 + Nextjs，聊好需求，10分钟就开发好了。
> 
> 之前总觉会很复杂。
> 
> 迈出第一步，才有迭代优化。
> 
> 设定多角色的提示词Agent本身也不复杂。
> 
> ![Image](https://pbs.twimg.com/media/G4mp834bgAAP_GG?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G4mqDBSawAAXZaZ?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G4mqxOYbQAAvYnV?format=jpg&name=large)

* * *

**宝玉** @dotey [2025-11-01](https://x.com/dotey/status/1984437290664394854)

我唯一推荐的就是 Claude Agent SDK

* * *

**向阳乔木** @vista8 [2025-11-01](https://x.com/vista8/status/1984444711944536218)

我试试，没有Claude账号也可以用吧，只是个框架是吧。

* * *

**ZayenOne** @ZayenOne [2025-11-01](https://x.com/ZayenOne/status/1984541721183785081)

说的太好了，AI时代日新月异，迭代太快导致大伙都关注“术”的用法，天天折腾各种新框架和新应用，而忽视了“道”（基于术去搭建一个解决方案的方法论），大赞

* * *

**Appwrite** @appwrite

Appwrite is an open-source cloud platform built for developers who like to get stuff done.

Backend, auth, storage, serverless, real-time, web hosting, CDN.

All in one place.

Appwrite 是一个专为乐于高效完成工作的开发者打造的开源云平台。

后端、认证、存储、无服务器、实时、网站托管、内容分发网络。

一切尽在一处。