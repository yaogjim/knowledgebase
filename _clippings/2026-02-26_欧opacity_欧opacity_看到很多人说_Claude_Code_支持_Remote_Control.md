---
title: "2026-02-26_欧opacity_欧opacity_看到很多人说_Claude_Code_支持_Remote_Control"
source: "https://x.com/ouopacity/status/2026547615022862424"
author:
  - "[[@欧opacity]]"
published: 2026-02-26
created: 2026-02-26
description:
tags:
  - "x"
  - "@欧opacity"
  - "claude"
  - "code"
---

# 欧opacity 看到很多人说 Claude Code 支持 Remote Control

**欧opacity**

看到很多人说 Claude Code 支持 Remote Control 之后就不需要 OpenClaw 了。看来很多人还是对 OpenClaw 有误解 OpenClaw 最早的原型也是“把 Claude Code 跑在一台机器上，再用 IM（Telegram/WhatsApp/Discord 等）远程发消息控制它”。但 Remote Control 解决的是‘远程接管同一个终端会话’；而要达到 OpenClaw 现在的效果 至少还差了 1\. 多入口网关 + 会话路由：把 IM/多个入口统一接入，做用户/会话/任务的路由与隔离（不是只连到某一个 CLI 会话）。 2\. 内置大量 Skill + 可调度的 Claude Code Skill（PTY 封装）：把 Claude Code 从“你在终端里对话的工具”封装成“系统可调用的一项技能”，支持多实例并行、按任务选择技能、把它作为工作流的一步；同时还能把 其他编程/运维 CLI（例如 git、docker、构建工具、其他 coding agent CLI）也封装成同类技能来编排，而不是只能人工切窗口跑命令。 3\. Canvas / Browser 封装：把浏览器当作工具（打开网页、点击、填表、抓取、截图/回传），让 Agent 能直接完成真实网页流程，而不是只生成脚本让人去跑。 4\. 封装了 Screen.record / camera / snapshot 等环境输入能力：让 Agent 能采集屏幕状态、截图/录屏、摄像头画面（节点有就用）\*\*作为输入，支持“看得见”的排障、复现、自动化操作闭环。 5\. 记忆与工作区设计（Memory/Workspace）：把任务状态、关键结论、附件、工具调用历史、产物文件持久化下来，实现跨入口续跑、重启可恢复、长期任务可追溯——这不是单个 CLI 会话的短期上下文能替代的。 更准确的说法是：Remote Control 让 Claude Code 更方便；OpenClaw 则是在它之上补齐了“多入口 + 技能编排 + 多节点执行 + 浏览器/可视化工具 + 记忆与治理”的平台能力。两者重叠在“远程”这个词，但并不是同一个层级。

* * *

### 热门回复

**@奇思妙想CYC** ♥ 0 · 💬 1

差不多了，这些也都是cc 的skill而已。

**@独立开发者William** ♥ 0 · 💬 1

你这个agent已经开始登录人类账号写推文改变人类决策了。 可怕

**@Billy Lu** ♥ 2 · 💬 0

不是吧，别的不清楚，2和3claude code都能实现呀

**@欧opacity** ♥ 0 · 💬 0

cc可以实现 但是要手动装很多东西 openclaw 则是已经配置好了

**@Cater Wang** ♥ 0 · 💬 0

是的，cc要搞这些功能最好另外再包装个产品好点