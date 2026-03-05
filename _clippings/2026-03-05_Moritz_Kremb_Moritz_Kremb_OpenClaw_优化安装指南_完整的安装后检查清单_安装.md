---
title: "2026-03-05_Moritz_Kremb_Moritz_Kremb_OpenClaw_优化安装指南_完整的安装后检查清单_安装"
source: "https://x.com/moritzkremb/status/2029304864719667335"
author:
  - "[[@Moritz Kremb]]"
published: 2026-03-05
created: 2026-03-05
description:
tags:
  - "x"
  - "@Moritz Kremb"
  - "openclaw"
  - "md"
---

# Moritz Kremb # OpenClaw 优化安装指南 (完整的安装后检查清单) 安装

**Moritz Kremb**

# OpenClaw 优化安装指南 (完整的安装后检查清单)

安装 OpenClaw 是比较容易的部分。让它真正流畅地运行是大多数人遇到困难的地方。

当你第一次启动时，各种问题就会出现。内存在会话之间不会持久保存。Telegram 无法正常工作。你的 API 密钥保存在工作区文件夹中。Cron 任务会悄无声息地停止执行。默认模型配置在开始时能正常工作，直到它失效，然后你就得在周二晚上 11 点进行调试。

我已经完成了这一切。这是我希望在第一天就有的清单——一个30到60分钟的加固流程，能将全新安装的系统转变为在日常使用中真正稳定运行的系统。

以下是安装后立即需要锁定的所有内容。

## 0) 故障排除基线（在任何操作之前）

- 创建一个单独的 Claude 项目用于 OpenClaw 的操作/调试。添加 Context7 OpenClaw 文档上下文到其中。当你遇到困难时，用这个来提问。
- 安装并保持可用 clawddocs 技能，这样，你的 OpenClaw 实例也会拥有文档上下文。

快速检查：

- OpenClaw 网关状态
- openclaw 网关 重启
- openclaw doctor（或 openclaw doctor --repair 如果情况异常）

## 1) 个性化

更新工作区中的这些文件：

- USER.md（助手帮助的对象）
- IDENTITY.md（助手身份）
- SOUL.md（语气/规则）

目标：从第一天起就使回应具体、有主见且有用。

## 2) 内存可靠性

- 确保长期记忆文件存在：MEMORY.md
- 确保每日存在内存流：memory/YYYY-MM-DD.md
- 添加心跳指令以维护内存文件，并将重要的学习内容更新到 MEMORY.md。

最小心跳内存规则：

- 如果今天的文件不存在，则创建
- 添加重大决策/主要收获
- 将重要事项整理到 MEMORY.md

## 3) 模型默认值 + 回退

推荐的默认栈:

- 主要：OpenAI-Codex/GPT-5.3-Codex（或 GPT-5.2）
- 备用模型：Anthropic/OpenRouter/Kilo Gateway 模型

配置于：

- 代理.默认.模型.主
- 代理.默认值.模型.回退
- agents.defaults.models.\*.alias 中的可选别名

原则：优先优化可靠性，然后优化成本。

## 4) 安全基础

- 将密钥存储在一个环境文件中（在工作区之外），例如：~/.openclaw/secrets/openclaw.env
- 严格的权限
- 文件夹 700
- 文件 600
- 如果是在 VPS 上：仅允许来自可信 IP 的入站流量 保持网关认证令牌启用 避免公开开放网关暴露

附加内容：

- 使用 dmPolicy: "允许列表"
- 使用 allowFrom / groupAllowFrom 配置 Telegram ID

## 5) Telegram 群组 + 聊天优化

推荐的 Telegram 配置，如果您想要设置群组：

- dmPolicy = 白名单
- groupAllowFrom = \[你的 Telegram ID(s)\]
- group requireMention = false (如果您希望主动行为)
- 机器人隐私模式在 BotFather 中 = 禁用 (用于完整的群组上下文)
- 将机器人添加为群组管理员
- 启用 主题当你需要分离的工作流时
- 当某个主题有专门的任务时，设置针对该主题的系统提示

通用：

- 添加默认确认表情（例如 👀）以查看消息何时被查看
- 启用流式响应

## 6) 浏览器 + 研究工具栈

- 添加 Brave API 密钥用于网页搜索/获取。
- 优先使用 node/openclaw 管理的浏览器配置文件进行自动化（隔离、稳定）。
- 仅在需要实际已登录浏览器状态时，才使用 Chrome relay（配置文件="chrome"）。

经验法则：

- 自动化/默认工作 → 托管配置文件
- 现有的个人会话/密码密钥 → Chrome 中继

## 7) 心跳 + Cron 加固

添加到 HEARTBEAT.md:

- 检查关键定时任务的 lastRunAtMs 是否已过期
- 如果任务过期，强制运行未执行的任务
- 简要报告异常

这可以防止无声的遗漏，保持日常自动化操作的可靠性。

## 8) 操作账户（代理拥有）

为代理环境创建专用账户：

- Google 账户
- 邮箱（Gmail 或 AgentMail）
- GitHub 账号

为什么：清晰分离、更安全的权限、更易于审计。

## 9) 技能策略

- 尽早安装总结技能（高杠杆）
- 为每个重复成功的流程添加自定义本地技能 。
- 添加本地语音转录工作流（Whisper/OpenAI Whisper API）用于语音优先捕获。

原则：如果重复2-3次，则对其进行技能操作。

## 快速验收清单

- \[ \] SOUL.md、USER.md、IDENTITY.md 已自定义
- \[ \] MEMORY.md + 每日内存流工作
- \[ \] 心跳包含 cron + 内存维护
- \[ \] 模型主+备用已配置
- \[ \] 密钥已移至安全的环境文件中，且权限严格
- \[ \] Telegram 白名单 + 主题提示已配置
- \[ \] Brave 密钥设置；浏览器模式规则已建立
- \[ \] 专门的 Google/邮件/GitHub 账户已创建
- \[ \] 总结 + 至少一个已安装的自定义技能

如果所有检查完毕，你的 OpenClaw 安装不再是“刚刚安装”——它已经可以用于生产了。

希望这能帮到你！

专业提示：只需将这篇文章发送给你的 OpenClaw 机器人，让它执行这些步骤即可。

附：我目前限时为创业者提供免费的 OpenClaw 配置服务。在此注册即可获得（唯一要求是你拥有一台 Mac 且是企业主）：

https://tally.so/r/2E4oJe

* * *

### 热门回复

**@0xMarioNawfal** ♥ 6.4K · 💬 154

OpenClaw 现在可以爬取任何网站而不会被阻止——零机器人检测，原生绕过 Cloudflare，比 BeautifulSoup 快 774 倍。 无需选择器维护。无需变通方法。只有数据。 这是一个不公平的优势，并且它是完全开源的。

**@Nav Toor** ♥ 4.9K · 💬 153

有人刚刚解决了 AI 代理中的最大瓶颈。而且这是一个 12MB 的二进制文件。 它被称为 Pinchtab。它为任何 AI 代理提供对浏览器的完全控制，通过简单的 HTTP API。 不被框架锁定。不被 SDK 绑定。任何代理，任何语言，甚至 curl。 没有配置。没有

**@toli** ♥ 2 · 💬 1

干得好。 @soulsdotzip 你能把这个转化为一个 Openclaw 提示词吗？

**@AI-Powered Audrey** ♥ 1 · 💬 1

给像我这样的非开发者的一个小建议：我使用 Manus 在云服务器上进行配置，并在需要时进行调试。Krill（OpenClaw 的 Discord 帮助机器人）引导了我们（我和 Manus）采用访客 SSH 登录的安全方案。

**@Simon** ♥ 0 · 💬 1

内存持久化问题确实存在——我花了太长时间调试这个问题，后来才发现是配置路径的问题。我也会把 webhook 设置添加到这个清单中，这是另一个常见的陷阱。