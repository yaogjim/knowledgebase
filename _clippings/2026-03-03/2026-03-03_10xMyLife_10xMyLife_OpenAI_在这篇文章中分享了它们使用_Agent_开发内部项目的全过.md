---
title: "2026-03-03_10xMyLife_10xMyLife_OpenAI_在这篇文章中分享了它们使用_Agent_开发内部项目的全过"
source: "https://x.com/hhmy27/status/2028345786527080682"
author:
  - "[[@10xMyLife]]"
published: 2026-03-03
created: 2026-03-03
description:
tags:
  - "x"
  - "@10xMyLife"
  - "agent"
  - "https"
---

# 10xMyLife OpenAI 在这篇文章中分享了它们使用 Agent 开发内部项目的全过

**10xMyLife**

OpenAI 在这篇文章中分享了它们使用 Agent 开发内部项目的全过程——百万行代码，数千次PR merge，没有一行代码是人类手写的 [https://openai.com/index/harness-engineering/…](https://openai.com/index/harness-engineering/) 几个有意思的地方： 1️⃣ 他们（工程师）完全相信 Codex（使用 GPT5 模型）的编码能力，没有手写任何代码，全部都由 Codex 生成 2️⃣ 人力资源不再使用在编码上，而是致力于拆解目标，分解任务，构造一个有明确反馈的编码环境，让 Agent 可以从小任务做起，逐渐完成大目标，并且在出错的时候，不会通过“再试一次”这种方法去重新生成代码，而是通过人力介入，思考这次出错是缺少哪些 Context/工具/反馈？通过调整编码环境，让 Agent 拥有更明确的 Context 补充说明： 我非常赞同这种工作方式，类似Ralph Wiggum Loop的工作理念，即让 AI 在循环中尝试完成任务，将这一轮的错误作为下一轮的输出，反复迭代，最终达成目标。和依赖 prompt 的工作方式相比，这种方式更加科学，建立了明确的反馈环境，有着清楚的错误日志，开发者从"人在环中"（Human-in-the-loop）转变为"人在环上"（Human-on-the-loop），只需设定目标和质量标准，让 AI 自主迭代直至收敛 3️⃣ 当 Agent 完成编码工作后，会有多个 Agent 负责 review 代码，只有当所有 Agent 都对代码满意之后，才会允许 PR 合并，而在这一步中并不强制要求人类 review 4️⃣ 对于 Context 管理，一个庞大的操作手册效果并不好，应该给 Agent 地图，而不是操作手册。工程师们提供的是一个简短的概述文件，告诉 AI 项目架构，去哪里查看模块代码，模块的设计理念，待完成和已经完成的工作有哪些。 5️⃣ 给 Agent 更多信息 在开发过程中，工程师们追求暴露更多的信息给 Agent，比如说会议记录，一致性规范等，目标是让 Agent 接手代码的时候，能够在规范下开展工作 这里有一个很重要的结论：将更多系统以代理能够直接检查、验证和修改的形式纳入，能够带来更大的杠杆效应——这不仅针对 Codex，也适用于其他正在处理该代码库的代理（例如 Aardvark）。 前段时间 Krapathy 的推文也有类似的理念 [https://x.com/karpathy/status/2024583544157458452?s=46…](/karpathy/status/2024583544157458452?s=46) 将来的系统应该尽可能的提供给 Agent 用的 API/CLI，让 Agent 能够轻松的读取上下文信息，而不是通过视觉方案/HTML 解析来获取 6️⃣ 当一个开发工程的吞吐量瓶颈是人类注意力而非 Token 产出速度的时候，人类在开发过程中的定位需要从传统的编写代码，运行测试等工作，切换到设计开发环境、调整反馈机制和编码规范，来帮助Agent用更可靠的方式开发

![图片](https://pbs.twimg.com/media/HCYhthPaYAIRHau?format=jpg&name=large)

* * *

### 热门回复

**@karminski-牙医** ♥ 956 · 💬 26

Apple ANE 被成功逆向! 38TOPS 算力其实是数字游戏? 刚刷到博主 maderix 开源了个硬核项目: 逆向 Apple 的私有 API, 绕过 CoreML, 直接在 Apple Neural Engine (ANE) 上实现了神经网络训练! 等会? 啥是 ANE? ANE是苹果芯片内部的神经网络加速单元, M4 上目前已经是 16 核的运算单元了,

**@plantegg** ♥ 386 · 💬 19

最近几个月大家为之疯狂的各个大模型 Agent 基本都来自于 2022 年的这篇论文: https:// arxiv.org/abs/2210.03629 将这篇论文工程上实现就得到了 Claude code/Cline 这样的 Agent 从 2022 年到 2025 年，大家都在干什么？

**@Orange AI** ♥ 268 · 💬 30

今天 HackerNews 上有一篇很有趣的文章 《MCP 已死，CLI 永生》 它断言 MCP 已经在走向衰亡。 理由是：大模型并不需要特殊的协议 最好的工具总是既能为人所用，又能被机器高效处理的。 而 CLI 就是那一个很好的工具。 如果现在的轮子就很好用，我们并不需要再次发明轮子 https:// ejholmes.github.io/2026/02/28/mcp -is-dead-long-live-the-cli.html …

**@meng shao** ♥ 181 · 💬 4

CLI Is All You Need，为什么 CLI 完胜 MCP？ Anthropic 推出 MCP 标准后，大量开发者开始为每一种工具、API、数据库构建专用的 MCP Server，但最顶尖的“10x 开发者”却并不采用这种方式。他们直接将终端的标准输入/输出暴露给 Agent，让 Agent 像人类开发者一样，在 Shell 中自由执行

**@Ian Maurer** ♥ 17 · 💬 3

BioMCP has been expanded to 12 entities and 29 trusted sources. ChatBots and Coding Agents can use BioMCP tool either as a command line interface (CLI) or model context protocol (MCP) server.