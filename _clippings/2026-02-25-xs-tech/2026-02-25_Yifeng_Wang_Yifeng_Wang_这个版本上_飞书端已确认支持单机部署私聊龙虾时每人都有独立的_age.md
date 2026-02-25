---
title: "2026-02-25_Yifeng_Wang_Yifeng_Wang_这个版本上_飞书端已确认支持单机部署私聊龙虾时每人都有独立的_age"
source: "https://x.com/ewind_dev/status/2024099979657113657"
author:
  - "[[@Yifeng Wang]]"
published: 2026-02-25
created: 2026-02-25
description:
tags:
  - "x"
  - "@Yifeng Wang"
  - "agent"
  - "session"
---

# Yifeng Wang 这个版本上，飞书端已确认支持单机部署私聊龙虾时每人都有独立的 age

**Yifeng Wang**

这个版本上，飞书端已确认支持单机部署私聊龙虾时每人都有独立的 agent 环境，且带沙盒隔离，欢迎体验！核心是以下配置 - session.dmScope="per-account-channel-peer" 每个私聊独立会话 - agents.defaults.sandbox.mode="non-main" + scope="session" 会话级 docker 沙盒

> **@billtheinvestor**
> 
> OpenClaw v2026.2.15 更新炸裂！从实验玩具直接跃升生产级 Agent 平台，核心升级让长期跑成本暴降，市场该 FOMO 了： 1. Prompt 缓存 + 智能上下文压缩：重复系统提示/历史自动缓存，长对话 token 消耗砍 30–60%，缓存命中率 70–90% → 日常 Agent 任务输入成本几乎归零！ 2. x.com/openclaw/statu…

* * *

### 热门回复

**@鹿 𝕟𝕠𝕜𝕚𝕟𝕠𝕜𝕚 祥子——** ♥ 1 · 💬 0

私聊的话好像 per-peer 就够了？然后建个 identity link 给不同渠道的同用户