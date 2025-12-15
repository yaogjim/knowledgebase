---
title: "TinyShip 上线了！"
source: "https://x.com/vikingmute/status/1998566358779617506"
author:
  - "[[@vikingmute]]"
date: "2025-12-12T12:06:48+08:00"
created: 2025-12-12
description:
tags:
  - "@vikingmute #TinyShip #SaaS #独立开发 #前端 #后端 #FullStack #Next.js #Nuxt.js #TailwindCSS #TypeScript #Vercel #Monorepo"
---
**Viking** @vikingmute [2025-12-10](https://x.com/vikingmute/status/1998566358779617506)

我的第三个独立开发的项目 TinyShip 今天上线了 🎉🎉 http://tinyship.cn

看起来是 another SaaS template，但我认为完全不是重复造轮子，市面上确实有非常多的 SaaS 模板，但我想创造的是一个全新不一样的体验。

1 支持双框架 ，为了满足不同框架爱好者，才用了 Next.js 和 Nuxt.js 双框架设计，这也是我在市面上看到的第一个 Nuxt 模版。

2 双市场策略，完全适配国内本土和出海项目，本土支持 微信登录/微信支付/阿里云短信 国际市场支持 Stripe、Creem 支付，主流 OAuth 登录 以及 Twilio 短信。

说起个人项目，现在非常多人都在鼓吹出海，目前市面上的模板也都是针对出海项目的。但我认为独立开发一定不能忽略国内市场。虽然一直都在说国内付费意愿低，在你最熟悉的市场，其实比已经竞争非常激烈的出海项目有时候更容易成功。

对于价格来说，大多数 SaaS 模板的定价都是对标国外架构，大多 100 到 200 美元。而给自己的定价策略是低价并且优质，让更多开发者有能力购买我的产品。所以价格是299人民币，早鸟价格期间 199 元，应该算是一个大多数人都能承受的价格了。

还有更多详情请看 👇

---

**Viking** @vikingmute [2025-12-10](https://x.com/vikingmute/status/1998566363972165975)

架构：

刚才所说的，工程师总是在框架选择上犯难，所以我在应用中使用了 两种最流行的全栈框架：

\- Next.js：为 React 爱好者准备

\- Nuxt.js：为 Vue 开发者设计

我本人就是 Vue 的爱好者。所以本站其实是在这个基础上使用 Nuxt 搭建的。

采用简化版的基于 PNPM 的 monorepo 架构，让两个应用可以共享基础模块：

\- 统一的认证系统

\- 共享的数据库层

\- 一致的支付接口

\- 相同的业务逻辑

![Image](https://pbs.twimg.com/media/G7xSlgVaMAAxfvI?format=jpg&name=large)

---

**Viking** @vikingmute [2025-12-10](https://x.com/vikingmute/status/1998566367482753516)

技术栈：

我想做一个充满技术品味的现代全栈项目，所以采用的是如下的最新技术：

\- TailwindCSS v4：最新的原子化 CSS 框架

\- shadcn/ui ：现代化组件库

\- TypeScript：完整的类型安全

\- Zod：运行时类型验证

\- Better-Auth：企业级认证系统

\- Drizzle ORM + PostgreSQL：类型安全的数据库操作

\- CASL：灵活的权限管理

\- Vercel AI SDK：AI 能力集成

---

**Viking** @vikingmute [2025-12-10](https://x.com/vikingmute/status/1998566371735777699)

国内外双体系支持

一套代码，双市场覆盖

国内：微信登录 & 手机号登录

国外：OAuth 登录（Google、GitHub、Apple）Twilio 手机号登录

支付：微信支付 & Stripe & Creem

国内外无缝切换

---

**Viking** @vikingmute [2025-12-10](https://x.com/vikingmute/status/1998566376110534697)

无厂商锁定的架构

采用无厂商锁定的架构，让您始终保持选择的自由，可自由选择任何云服务商、数据库、支付提供商，并且使用了 Unified API 设计

所有提供商使用一致的接口，真正做到：

\- 只需更改一个参数即可切换

\- 不需要重写代码

\- 完全解耦的服务层

![Image](https://pbs.twimg.com/media/G7xUWB2aMAAzzzp?format=jpg&name=large)

---

**Viking** @vikingmute [2025-12-10](https://x.com/vikingmute/status/1998566381634335103)

AI 以及 AI 辅助开发：

Vercel AI SDK：多 AI 提供商支持

在应用中实现了实现了一个大模型对话简单实现，可扩展设计，使用了最新的技术 ai-sdk / ai-elements / streamdown 实现非常丝滑的聊天效果，可以按需求扩展为更复杂的功能。未来也会持续推出更多更复杂实现的 Demo，让使用更加简单。

---

**Viking** @vikingmute [2025-12-10](https://x.com/vikingmute/status/1998566386759852032)

内置 Admin Panel

开箱即用的管理后台，提供轻量级的用户管理、订阅管理、订单管理等功能。基于现代化 UI 组件库构建，支持角色权限控制等功能。

让你专注于业务逻辑，而非重复的管理界面开发。

---

**Viking** @vikingmute [2025-12-10](https://x.com/vikingmute/status/1998577908672245778)

主题系统

TinyShip 基于 shadcn/ui 的现代化主题系统，内置了多种主题，完全可定制，设计力求极简，杜绝蓝紫色渐变以及 AI 味，也可以在 http://tweakcn.com 下载更多，并且支持暗黑模式。

---

**Viking** @vikingmute [2025-12-12](https://x.com/vikingmute/status/1999289221463626231)

更新了 Tinyship 的路线图：

https://docs.tinyship.cn/zh-CN/technical/roadmap…

大家可以看下这个项目下一步的发展规划：

Tinyship 的宗旨不是做大而全的应用，主打“基础完备 + 可扩展架构”，核心流程默认可用。未来可能提供快速搭建模板库，但原则不变。

大体接下来Q1-Q2的功能是：

1 构建一个基于 Fumadocs

![Image](https://pbs.twimg.com/media/G77m7ysagAEmay9?format=jpg&name=large)
