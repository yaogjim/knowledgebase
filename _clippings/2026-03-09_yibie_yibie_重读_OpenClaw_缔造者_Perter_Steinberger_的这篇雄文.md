---
title: "2026-03-09_yibie_yibie_重读_OpenClaw_缔造者_Perter_Steinberger_的这篇雄文"
source: "https://x.com/yibie/status/2028650995153314299"
author:
  - "[[@yibie]]"
published: 2026-03-09
created: 2026-03-09
description:
tags:
  - "x"
  - "@yibie"
  - "ai"
  - "md"
---

# yibie 重读 OpenClaw 缔造者 Perter Steinberger 的这篇雄文

**yibie**

重读 OpenClaw 缔造者 Perter Steinberger 的这篇雄文《Shipping at Inference-Speed》，还有很深的启发，这篇文章是 Perter 说明自己 AI 辅助编程时，他自己工作流、方法、工具选择的转变，而这个转变让他打开与 AI 协作新的大门。

Perter 在 AI 辅助编程的范式转变，是来自他亲自开发的项目 VibeTunnel。年初他花了两个月时间，尝试用Rust、Go 甚至 Zig 重写核心模块，但旧模型一直失败，最终没完成。隔了一段时间，他重新打开这个项目，只给了 codex 两句提示让它把整个转发系统转成 Zig，模型自己跑了五个小时，经过多轮代码压缩，一次就交付了可用的转换。这种事在去年是不可想象的。

之后，他就彻底地改变了与 AI 协作的范式：

一、关键工作流转变

1\. 从"阅读代码"到"观看代码流"

\- 不再逐行阅读 AI 生成的代码 - 只看代码流的关键部分 - 通过长期经验积累，能凭直觉判断"这个任务应该多久完成" - 如果 codex 一次没解决，立即警觉可能有问题

2\. 项目并行化（3-8 个同时进行）

通常结构：1 个核心大项目，多个卫星项目（CLI 工具、小功能等）

当大项目在推理时，切换到其他项目 "软件开发就像爬山——不是直线上升，而是绕着山转圈"

3\. 默认从 CLI 开始

\- 所有项目默认先做成命令行工具、 - AI 可以直接调用和验证输出 - 快速闭环（closing the loop） - UI 和 Web 是后续添加的

二、具体工作流技巧

1\. 极简提示词（Prompts）

旧方式：长篇大论的语音口述提示 新方式： - "build" 或 "write plan to docs/\*.md and build this" - 拖拽 UI 截图 + "fix padding" - "look at ../vibetunnel and do the same for Sparkle changelogs"

2\. 无计划模式（No Plan Mode）

\- 不搞复杂的"计划模式" - 直接开始对话 → 让模型探索 → 共同制定计划 → "build" - 认为计划模式是旧模型的产物（那时模型不擅长遵循提示）

3\. 直接提交到 main

\- 不使用 worktree（工作树） - 不使用复杂的分支策略 - 如果代码乱了，让 AI 重构而不是回退 - 大任务留在分心时做（如写文章时同时跑 4 个重构任务）

4\. 知识管理：docs/ 文件夹

不使用：复杂的会话历史系统、issue 追踪器

使用： - 每个项目的 docs/ 文件夹 - 全局 [http://AGENTS.MD](http://AGENTS.MD) 文件 - 脚本强制模型读取相关文档 - 用 "write docs to docs/\*.md" 让模型自己命名文件

5\. 跨项目复用

提示词示例： "find all my recent go projects and implement this change there too + update changelog" "look at ../project-folder and do the same here"

三、反直觉的工具选择❌ 线性/问题追踪器（Linear/issue trackers） ❌ Slash 命令（/commit 不如直接打 "commit/push"） ❌ 多智能体编排系统（multi-agent orchestration） ❌ 异步代理（Cursor Web/codex remote）→ 缺少可控性 ❌ 检查点/回滚（让 AI 改而不是 revert）

四、金句摘录

1\. "大多数软件不需要深度思考" — 数据从一个表单传到另一个表单 2. "与模型对抗通常是浪费时间和 token" — 设计符合模型训练数据习惯的代码结构 3. "我设计代码库不是为了让我容易导航，而是让 agents 能高效工作" 4. 上下文管理 > 上下文大小 — Codex 虽然窗口大，但内部思考更紧凑，能比 Claude 在相同 token 下完成 5 倍工作 5. 长提示词已死 — 在 GPT 5.2 时代，短提示 + 图片/示例足够[https://steipete.me/posts/2025/shipping-at-inference-speed…](https://steipete.me/posts/2025/shipping-at-inference-speed)

[AGENTS.md](https://t.co/5EIzIfm3UI)

* * *

### 热门回复

**@Leo** ♥ 378 · 💬 30

给 Claude Code 接了个 X 搜索引擎。 基于 Grok 搭了个本地桥接服务，常驻后台，Claude Code 需要搜 X 时自动调用。终端一行命令，几秒返回摘要 + 相关用户原话。 两个关键优势：不走 X 官方 API（省掉每月 $200 的 Basic 套餐），而且能搜到实时动态——API 搜索有延迟和索引限制，Grok

**@Geek** ♥ 195 · 💬 25

我今天把 CLI Proxy API 换成 Sub2API 了，好用~

**@刘飞** ♥ 178 · 💬 19

调研了一阵子 OpenClaw 的使用案例（身边朋友，微信群，社交媒体等等），也体验了一下，感受跟之前的很类似： 对于本来就有自己业务的，尤其是商业闭环的，才用得更好，也更愿意充值，因为真的能省事儿，带来生产力，很快就能正向循环。以开发者、自媒体、投资人和小企业老板为主。

**@YC (Yucheng Liu)** ♥ 180 · 💬 0

Linear Thinking Is a Bug（线性思维是个 Bug） "最应该改掉的习惯：每次思考都要"整理清楚再继续"。这是在强迫非线性机器按线性节拍运转。" Overview 线性思维——一件事导向下一件事，思考必须"在轨道上走"——是被学校、语言和社会结构训练进我们大脑的