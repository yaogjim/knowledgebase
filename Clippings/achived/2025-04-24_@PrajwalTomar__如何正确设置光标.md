---
title: "提取中文标题"
source: "https://x.com/PrajwalTomar_/status/1912513810575097900/?rw_tt_thread=True"
author:
  - "[[@PrajwalTomar_]]"
created: 2025-04-24
description:
tags:
  - "@PrajwalTomar_ 提取带有 # 的中文标签"
---
**Prajwal Tomar** @PrajwalTomar\_ [2025-04-16](https://x.com/PrajwalTomar_/status/1912513810575097900)

  
如何正确设置光标

游标规则已过时。项目规则才是目前的正确方式。

以下是它为何重要以及如何正确设置它的原因：

![Image](https://pbs.twimg.com/media/GoqYJH2XwAA9YmP?format=jpg&name=large)

---

**Prajwal Tomar** @PrajwalTomar\_ [2025-04-16](https://x.com/PrajwalTomar_/status/1912513814207295655)

  
1\. 为什么.cursorrules 还不够

游标最初在项目根目录使用单个.cursorrules 文件，但这种方法存在严重问题：

有限控制

→ 一个规则文件应用于整个项目，即使不相关时也是如此。

上下文过载

→ 光标必须

---

**Prajwal Tomar** @PrajwalTomar\_ [2025-04-16](https://x.com/PrajwalTomar_/status/1912513817394966616)

  
2\. 介绍 Cursor 的项目规则（.mdc 文件）

通过引入项目规则，Cursor 解决了所有这些问题，这些规则以模块化的.mdc 文件形式存储在.cursor/rules/目录中。

这使您能够针对每个文件类型、模块或功能应用规则，而不是针对一个大文件。

为什么项目规则更好：

---

**Prajwal Tomar** @PrajwalTomar\_ [2025-04-16](https://x.com/PrajwalTomar_/status/1912513820511105231)

  
3\. 逐步设置

以下是正确设置项目规则的方法：

---

**Prajwal Tomar** @PrajwalTomar\_ [2025-04-16](https://x.com/PrajwalTomar_/status/1912513826555326773)

  
步骤 1：一般规则（general.mdc）

此规则适用于整个项目中的所有文件。

范围：\*（所有文件）

内容：

\- 所有开发都使用 TypeScript。

\- 优先考虑可读性和可维护性。

\- 使用清晰、具描述性的名称。

\- 为复杂内容添加有意义的注释

![Image](https://pbs.twimg.com/media/GoqYOvdWkAAxZcE?format=png&name=large)

---

**Prajwal Tomar** @PrajwalTomar\_ [2025-04-16](https://x.com/PrajwalTomar_/status/1912513832607707370)

  
步骤 2：前端规则（frontend.mdc）

这些规则仅适用于前端文件（.tsx）。

范围：\*.tsx（React 组件）

内容：

\- 使用函数式 React 组件。

\- 应用 Tailwind CSS；避免内联样式。

\- 组件应该是模块化且可复用的。

\- 保持一致

![Image](https://pbs.twimg.com/media/GoqYSkEWgAAWOaH?format=png&name=large)

---

**Prajwal Tomar** @PrajwalTomar\_ [2025-04-16](https://x.com/PrajwalTomar_/status/1912513836458078289)

  
步骤 3：后端规则（backend.mdc）

这些规则仅适用于后端逻辑（.ts API 和数据库文件）。

范围：api/\*\*/\*.ts（所有后端 API 文件）

内容：

\- 始终验证 API 输入。

\- 始终一致地使用 async/await。

\- 遵循 RESTful 约定。

\- 针对……优化查询

---

**Prajwal Tomar** @PrajwalTomar\_ [2025-04-16](https://x.com/PrajwalTomar_/status/1912513839213765105)

  
4\. 我所在机构发生了什么变化

切换到项目规则产生了实际影响：

更少的人工智能错误

→ 光标更精确地遵循作用域规则。

不再有重复的修正

→ 人工智能会记住你的标准并自动应用它们。

更简洁、更一致的代码

→ 每个人

---

**Prajwal Tomar** @PrajwalTomar\_ [2025-04-16](https://x.com/PrajwalTomar_/status/1912513842619560085)

  
5\. 项目规则的最佳实践

要充分利用.mdc：

保持规则模块化：

\- 分离前端、后端和数据库逻辑。

使用精确的范围：

\- .tsx → React 组件

\- api/\*\*/\*.ts → 后端应用程序编程接口

\- \*/\*.sql → SQL 查询

定期完善规则：

\- 如果一条规则是

---

**Prajwal Tomar** @PrajwalTomar\_ [2025-04-16](https://x.com/PrajwalTomar_/status/1912513845597507632)

  
6\. 最终要点：项目规则是一个改变游戏规则的因素

光标项目规则比.cursorrules 有了巨大改进：

\- 人工智能生成的代码更准确且遵循最佳实践。

\- 规则更易于管理、更新，并在各个项目中进行扩展。

\- 减少修复所花费的时间

---

**Prajwal Tomar** @PrajwalTomar\_ [2025-04-16](https://x.com/PrajwalTomar_/status/1912513848965484982)

  
Cursor 不仅仅是一个由人工智能驱动的集成开发环境，它是一个在正确设置时能适应您的编码标准的工具。

如果你仍在使用.cursorrules，那你就在限制 Cursor 的潜力。

立即开始使用项目规则，全面掌控人工智能生成的代码。

有什么问题吗？让我们
