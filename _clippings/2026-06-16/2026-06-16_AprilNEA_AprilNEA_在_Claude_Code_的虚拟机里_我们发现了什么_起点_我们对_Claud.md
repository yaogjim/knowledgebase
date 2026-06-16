---
title: "2026-06-16_AprilNEA_AprilNEA_在_Claude_Code_的虚拟机里_我们发现了什么_起点_我们对_Claude"
source: "https://x.com/AprilNEA/status/2034216942924624054"
author:
  - "[[@AprilNEA]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "#ReverseEngineering"
  - "#Anthropic"
  - "x"
  - "@AprilNEA"
---

# AprilNEA: 在 Claude Code 的虚拟机里，我们发现了什么 起点 我们对 Claude Code 运行环境做了一次完整的逆向工程

**AprilNEA**

在 Claude Code 的虚拟机里，我们发现了什么

起点

我们对 Claude Code 运行环境做了一次完整的逆向工程。起点很简单：用 strace 追踪 PID 1，然后顺藤摸瓜。

运行环境

Claude Code 跑在 Firecracker MicroVM 里——这是 AWS 开源的轻量虚拟机，Lambda 和 Fargate 底层用的就是它。证据是 ACPI 表里写死的 OEM ID FIRECK\`。整个虚拟机极其精简：4核 CPU、16GB 内存、252GB 磁盘，没有 systemd，没有 sshd，没有 cron，PID 1 是一个自研的 \`/process\_api \` 二进制，同时充当 init 进程和 WebSocket API 网关。

关键发现：environment-runner

虚拟机里有一个 27MB 的 Go 二进制 \`/usr/local/bin/environment-runner\`，没有做 strip，保留了完整的调试信息和符号表。源码路径指向 github\[.\]com/anthropics/anthropic/api-go/environment-manager/——这是 Anthropic 内部的私有仓库。

通过 go tool objdump\`、\`strings\`、\`objdump \`等工具，我们从中提取出了完整的包结构、所有函数签名、嵌入资源和关键字符串。

三个重大发现

1\. Antspace —— Anthropic 自建的 PaaS 平台

在部署模块中，我们发现了两个部署目标：公开的 Vercel 和完全未公开的 Antspace。Antspace 拥有完整的部署协议（创建部署 → 上传 tar.gz → 流式状态推送），有独立的控制面 URL 和认证体系。互联网上关于它的公开信息为零。

命名来源推测："Ant"是 Anthropic 员工的内部昵称（他们拥有域名 ant\[.\]dev)。

2\. Baku —— Claude 网页版应用构建器的内部代号

当你在 claude\[.\]ai 上让 Claude "帮我做一个网页应用"时，后台启动的就是 Baku 环境。它预装了 Vite + React + TypeScript 模板，自动配置 Supabase 数据库（含 6 个 MCP 工具：查询、迁移、类型生成、Edge Function 部署等），构建完成后默认部署到 Antspace。

3\. BYOC —— 自带容器的企业部署模式

environment-runner 支持两种环境类型：\`anthropic\`（Anthropic 托管）和 \`byoc\`（Bring Your Own Cloud，客户自己的基础设施）。这意味着企业客户可以在自己的 Kubernetes 集群里运行 Claude Code 的完整环境，而会话编排仍由 Anthropic API 控制。

战略含义：Anthropic 正在构建一个从 AI 模型到应用托管的完整闭环：

用户用自然语言描述需求

→ Claude 在 Baku 环境中生成应用代码

→ 自动配置 Supabase 数据库

→ 一键部署到 Antspace

→ 应用上线，用户全程不离开 Anthropic 生态

这不只是一个 AI 编程助手，而是一个 AI 原生的 PaaS 平台的雏形。它的竞争对手不仅是 Cursor 和 GitHub Copilot，更是 Vercel、Netlify、Replit、Lovable 和 Bolt。而 Anthropic 的独特优势在于：他们拥有从大模型到运行时到部署平台的完整垂直整合，这是目前任何竞品都不具备的。

方法论：全部发现来自对一个未 strip 的 Go 二进制的静态分析和运行时追踪。没有任何网络攻击、权限提升或越权操作——这个二进制就在虚拟机里，带着完整的符号表，等着被读取。

[#ReverseEngineering](/hashtag/ReverseEngineering?src=hashtag_click) [#Anthropic](/hashtag/Anthropic?src=hashtag_click) [#ClaudeCode](/hashtag/ClaudeCode?src=hashtag_click) [#Firecracker](/hashtag/Firecracker?src=hashtag_click) [#PaaS](/hashtag/PaaS?src=hashtag_click) [#AI](/hashtag/AI?src=hashtag_click)

[https://fixupx.com/AprilNEA/status/2034209454389158048…](https://fixupx.com/AprilNEA/status/2034209454389158048)

* * *

### 热门回复

**@Kem Chen** ♥ 531 · 💬 73

新来的 Leader 想用 Claude Code 把项目用了十年的 php/Laravel 版本升级到最新版

关键是这个 Leader 几乎不懂 php，团队里其它人有微词，评论区都不看好

今天发了事情后续，升级平稳落地，AI 真强...

**@面包** ♥ 427 · 💬 46

说实话，我觉得王自如评价openclaw其实蛮准确的，这就是一个资本+爆点最终造成的结果。

**@HOFA Gallery (House of Fine Art)** ♥ 261 · 💬 36

Digital Art Awards 2026 | In partnership with PhillipsX

Proudly backed by Lightyear

We are pleased to announce the 32 finalists for the Second Edition of the Digital Art Awards.

This year’s selection reflects an exceptional range of practice in digital and generative art and

**@#endif** ♥ 141 · 💬 20

解除了锁推，因为从Google辞职了不用再害怕吐槽同事被发现了

现在创业中求求大家关注

@\_\_endif

吧，起号好难

正式的~吹牛~是：

\- 我从23年开始做LLM coding，领导了内部最初的coding agent，并在24年I/O成为了Google第一个正式发布的coding agent

\- LLM方面我从Palm开始贡献，一直到Gemini

**@Menci** ♥ 172 · 💬 10

HydraDB 是我最近看到过的所有跟 agent 相关的东西里唯一一个第一反应觉得它靠谱的

knowledge graph + log structure

一看就是既懂算法又了解计算机系统的人设计出来的东西