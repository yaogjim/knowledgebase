---
title: "2026-02-27_卡颂_卡颂_最近有两个有意思的新闻_1_Cloudflare_用_Claude_在一周内基于"
source: "https://x.com/kasong2048/status/2027062837043232833"
author:
  - "[[@卡颂]]"
published: 2026-02-27
created: 2026-02-27
description:
tags:
  - "x"
  - "@卡颂"
  - "ai"
  - "agentic"
---

# 卡颂 最近有两个有意思的新闻： 1. Cloudflare 用 Claude 在一周内基于

**卡颂**

最近有两个有意思的新闻： 1. Cloudflare 用 Claude 在一周内基于 Vite 重写了 Next.js 2. tldraw 考虑将开源项目中的所有测试用例移到闭源仓库中 他们都指向一个越来越清晰的趋势 —— “设计 Agentic Loops（代理循环）”将成为程序员的必备技能。 解释下，古法编程的思维是「人类想解法 → 人类写代码」，Agentic 思维则是「人类设计验证机制 → AI 暴力搜索解法」。 可以认为，人类的工作重心从"解决问题"转移到"设计一个让 AI 能自己解决问题的环境"。 其中的关键在于“为 Agent 设计一个循环，只要不满足验收条件他就会一直循环下去，暴力搜索解法”。 比如，SDD 的工作模式通常是： 1. 编写 Spec 2. 基于 Spec 拆解 Task 3. 基于 Task 编写测试用例 4. AI 基于测试用例编码，直到通过用例 这里的 Agentic Loops 就是： AI Coding -> 跑用例 -> 失败后重新Coding尝试 -> 跑用例 上面提到的2个新闻的重点都是“基于测试用例的 Agentic Loops”： - vinext 包含 1,700 Vitest tests 和 380 Playwright E2E tests，覆盖 Next.js 16 94% 的 API - tldraw 不希望竞对通过他们的测试用例构建 Agentic Loops，再用 AI 轻松的重写一个出来

* * *

### 热门回复

**@NerdC** ♥ 221 · 💬 10

Cursor 创始人自述ai编程正在走向第三时代： 1. 三个时代演进 - 第一时代：Tab 自动补全（逐键输入 → 智能补全），持续近两年，极大提升低熵重复工作效率。 - 第二时代：同步 Agent（实时提示-回应循环），开发者仍深度参与每步，持续时间很短（可能不到一年）。 - 第三时代：自主云端

**@Lex Tang** ♥ 208 · 💬 11

Google Jules 对于开发者来说，比小龙虾实在多了，开箱即用，每天起床一堆 PR 给你 review

**@艾略特** ♥ 134 · 💬 31

招人贴 盛大的 @EverMindAI 招各种技术， 算法，全栈和实习生 食堂很赞，不油不腻，不是外包 按时下班，我每天 7 点走 CC 不限量，随便用， 盛大公寓 5 折，小孩子国际学校 5 折

**@absolute labs** ♥ 172 · 💬 7

Web3 Commerce Panel at NFT Paris Side Event – Key Takeaways The Web3 Commerce panel brought together leaders from luxury, retail, and Web3 technology to discuss how blockchain and digital assets are reshaping online shopping, customer engagement, and brand loyalty. Key Insights

**@老鬼** ♥ 110 · 💬 2

知名 Agent 框架 Mastra 也出了个 CLI 编码工具 Mastra Code，最大的特色是“永不丢失上下文”。 在使用传统编码 Agent 进行长对话时，开发者经常需要面对“上下文窗口耗尽”的问题，Agent 会被迫压缩（Compact）历史对话，导致 AI “遗忘”之前的关键设定。 Mastra Code