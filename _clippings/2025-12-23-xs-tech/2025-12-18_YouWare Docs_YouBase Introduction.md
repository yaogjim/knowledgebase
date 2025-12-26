---
title: "YouBase Introduction"
source: "https://docs.youware.com/youbase/introduction"
author:
  - "[[YouWare Docs]]"
date: "2025-12-18T19:15:29+08:00"
created: 2025-12-18
description: "Learn what YouBase is and how it powers your YouWare applications with cloud backend infrastructure, authentication, database, storage, and more."
tags:
  - "YouWare Docs"
---
## Built-in Backend

完整的云基础设施

## 企业级安全

私密、加密，且始终由您掌控

## Zero Configuration

只需用自然语言描述您的需求

## What is YouBase?

YouBase 是 YouWare 内置的云后端基础设施——可将其视为驱动你的应用的后端。 如果说 YouWare 的视觉界面是应用的“脸”，那么 YouBase 就是它的“大脑”和“记忆”。没有 YouBase，你的应用就只是个华而不实的空壳：表单无法保存数据，用户无法登录，而且什么都留不住。启用 YouBase 后，你的应用就能真正“记住”用户数据，还能为每个人展示个性化内容。

---

## Overview

YouBase 是 YouWare 的云后端基础设施，为您的项目提供全面的后端能力——包括数据存储、用户认证、服务器端逻辑和文件管理。 只需用自然语言描述您的需求，YouWare 会自动生成前端和后端代码，并在云端为您运行。YouBase 提供托管的主机、计算和存储服务，这些服务可按需扩展，从您的第一个原型到数百万用户都能支持。 YouBase 运行在 YouWare 管理的云基础设施上，在您的项目域名（包括自定义域名）下，因此您无需复杂操作即可获得企业级可靠性。

---

## Why Choose YouBase

## Scales on Demand

从原型到生产，YouBase 可随您的需求无缝扩展。无论 10 名用户还是 10 万名用户访问您的网站，都能瞬间加载。

## 企业级安全

私密、加密，且始终由您掌控。包含企业级认证、细粒度的访问控制以及合规最佳实践。

## High Performance

全球快速稳定——无区域延迟、无随机停机、无“服务器过载”情况。

---

## YouBase 使用入门

![YouBase Introduction - Cloud backend infrastructure overview](https://mintcdn.com/youware-18c86901/JEHuqLUxrtQaGlaU/images/youbase-introduction.png?w=280&fit=max&auto=format&n=JEHuqLUxrtQaGlaU&q=85&s=06f773504f1f4d95638d524fde0f3450)

YouBase Introduction - Cloud backend infrastructure overview

YouBase 需要专业版或旗舰版。当您的项目需要后端功能（例如用户认证或文件存储）时，YouWare 会提示您升级并启用 YouBase。

## 现有项目的配置

对于在 YouBase beta（2025 年 12 月 16 日）之前创建的项目，是否启用 YouBase 取决于您的项目类型：

### 不含 YouWare 后端 MCP 的项目

- YouBase 选项卡上显示了“设置 YouBase”按钮
- 点击它会提示你更新项目到最新版本
- 更新后，你将能够访问：
	- YouBase 特性（数据库、用户、功能、存储）
	- 独立及自定义域名支持

如果您的项目使用 AI API (MCP)功能，这些功能在更新后将停止运行。

### 使用 YouWare 后端 MCP 的项目

- 这些项目在使用旧版数据库用户界面时，仍能继续正常运行
- 新的 Agent 与 YouWare 的后端 MCP 项目不兼容
- 在这些项目上无法启用 YouBase

使用 YouWare Backend MCP 的项目无法使用 YouBase。新的 Agent 无法与旧版后端配置协同工作。 你有两个选项：
1. 继续使用旧版后端 - 你当前的 YouWare 后端项目可保持原样继续使用，它将无限期正常运行。
2. 切换至 YouBase - 若要使用 YouBase 的功能，您需要：
	- 从遗留项目下载你的项目代码
	- 从下载的代码中删除 `backend` 目录里的所有内容
	- 将代码重新上传至新的项目，并让 Agent 使用 YouBase 重新实现后端功能
无法自动将遗留的后端项目迁移或转换到 YouBase。 如需协助，请联系 support@youware.com

## For New Projects

YouBase 测试版之后创建的项目：
- 无法启用 YouWare 后端的 MCP 或 AI API
- 使用 YouBase 实现所有后端功能

已在使用 YouWare 后端 MCP 或 AI API 的现有项目，可继续无限期使用这些功能。

---

## Pricing & Plans

YouBase 提供灵活的计划以满足您的项目从早期原型到生产应用的发展需求。

## Downgrade Policy

当你从专业版/超级版降级到免费版时，YouBase 会立即被禁用。你的数据仍会被保留 30 天，但这期间无法导出数据库。要恢复使用权限，请在 30 天保留期结束前升级订阅。

## Plan Comparison

---

在 YouBase 的 Beta 测试期间，标记为“Beta 期间无限制”的功能暂时不受限制。Beta 测试结束后，将适用标准限制。

## FAQs

No.YouBase 是模块化的。你可以根据项目需求，独立使用数据库、用户、功能或存储。

Yes.许多项目在无需编写任何后端代码的情况下，即可使用数据库、用户和存储。仅在需要高级自定义逻辑或第三方集成时，才需要相应功能。

我的订阅到期后会发生什么？

我能导出我的数据吗？

Yes.数据库数据和存储的文件可根据你的方案导出。详细信息请参阅方案对比。

YouBase 是否已准备好投入生产？

Yes.YouBase 旨在支持真实用户、真实数据以及在自定义域名下运行的生产项目。

**没有 YouWare 后端 MCP 的项目：**
- YouBase 标签页中会有一个“设置 YouBase”按钮
- 点击它会提示你更新项目到最新版本
- 更新后，您可以使用 YouBase 的功能、自定义域名和独立域名
- 请注意：您的项目中任何 AI API（MCP）功能在更新后将停止工作
**与 YouWare 后端 MCP 相关的项目：**
- 保留了旧版的数据库用户界面
- 这些项目不支持 YouBase 更新

[用户与认证](https://docs.youware.com/youbase/users-authentication)