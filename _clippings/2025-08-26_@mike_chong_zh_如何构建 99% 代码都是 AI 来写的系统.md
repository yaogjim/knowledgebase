---
title: "如何构建 99% 代码都是 AI 来写的系统"
source: "https://x.com/mike_chong_zh/status/1960176017135546687"
author:
  - "[[@mike_chong_zh]]"
published: 2025-08-26
created: 2025-08-26
description: "AI 加速主义。前 Outlook Mobile 开发者，软件3.0架构师。 努力让一起用 AI 创造属于我们自己的产品与企业。一起学习，共同成功。文科生，也是理科生？？"
tags:
  - "@mike_chong_zh #人工智能 #代码生成 #DevOps #GitHub #自动化 #效率"
---
**迈克 Mike Chong** @mike\_chong\_zh [2025-08-26](https://x.com/mike_chong_zh/status/1960176017135546687)

LinkedIn 上有人分享了如何构建 99% 代码都是 AI 来写的系统。系统性思维很棒，翻译了一下：

到现在我已经用 Claude Code 和 Copilot 来写代码差不多一个月了，基本就是我自己几乎不写——99.9% 的代码都是 AI agent 写的。下面是我能靠 AI 干成的事情，以及大概的花费：

Claude Code：大约 12.5 亿 Tokens，花了 ~640 美元

Copilot：1375 次高级请求，企业版（39 美元/月）

Claude Chat：几百次对话，同样是企业版（应该和 Copilot 一样）

代码库的变化：

\* 新增 197K 行代码

\* 删除 208K 行代码

\* 主分支上有 355 次提交

\* 合并了 180 个 PR

\* 解决了 98 个 GitHub issue

我是怎么做到的？

1) 所有代码都必须过一套非常严格的 CI/CD 流程：静态检查、格式化、代码安全工具，还有完整的测试集

2) 代码库已经模块化了，每个组件都通过清晰的接口来调用

3) 接口和实现完全分开

4) 每个组件都有自己的文档

5) 每个组件的测试、文档、头文件、实现都放在一起

6) 每个组件保持在 5k 行代码以下（包括文档）

7) 每个 GitHub issue 都写得很详细，带代码引用和问题描述

8) 搭建了一个 7 层的提示体系，记录各种规范：工具层（Copilot vs Claude）、语言层（C++ vs Python）、项目层（按仓库）、角色层（开发 vs 测试 vs 架构 vs 审查）、组件层（按目录）、任务层（对应 GitHub issue）、执行层（具体操作）

这样，我只需要分配任务，15-30 分钟就能拿到第一版，然后我再迭代、审查、验证，最后一小时内就能提交——几乎不用我亲手敲代码。

现在真正的瓶颈是我自己，因为我审查代码的速度跟不上。

而且 Claude Code 现在已经包含在企业计划里了。是时候继续玩一玩，让我的“Agent 军团”来帮我缓解这个瓶颈。

![Image](https://pbs.twimg.com/media/GzPxbLRbIAAV6Ug?format=jpg&name=large)

---

**迈克 Mike Chong** @mike\_chong\_zh [2025-08-26](https://x.com/mike_chong_zh/status/1960176221498839441)

我也基本是如此做的。所以很感谢他的系统化分享。
