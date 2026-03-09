---
title: "2026-03-09_Jason_Zuo_Jason_Zuo_elvissun_elvissun_的_agent_swarm"
source: "https://x.com/xxx111god/status/2028687759867531561"
author:
  - "[[@Jason Zuo]]"
published: 2026-03-09
created: 2026-03-09
description:
tags:
  - "x"
  - "@Jason Zuo"
  - "agent"
  - "llm"
---

# Jason Zuo [@elvissun](elvissun) 的 agent swarm

**Jason Zuo**

对比

[@elvissun](/elvissun)

的 agent swarm 和我的实践分享几个tips： 1. 监控别用 LLM 轮询，用 bash/python 脚本做 pre-flight 检查，有异常才触发 AI。零 token 开销。 2. Agent 管理用 ACP 比 tmux 省心，原生调 Codex/Claude Code/Gemini，session lifecycle 自动管理。 3. Claude Code 可以走 Max 订阅，不用花 API 钱。 4. Task tracking 建议上 issue 系统，状态机 + priority + blocked + 自动 dispatch。任务多了以后一个 JSON 管不住。 5. Code review 搞交叉验证 — Codex 抓逻辑、Gemini 抓安全、Claude 兜底。多模型互查比单个 reviewer 靠谱。 6. Git worktree 隔离每个 agent 的工作区，并行不打架。

![图片](https://pbs.twimg.com/media/HCdJ1IZagAAqBWe?format=png&name=large)

> **@elvissun**
> 
> zoe 每天消耗超过 2400 万 opus 令牌，以监控未运行的代理。 用一个两层系统替换了她的 cron： bash 预检查，空闲时零令牌 webhook 触发 Opus 仅在需要时。 约 95%的 token 减少和更可靠的输出。详情见下文。 (设置一个 cron 任务来 x.com/16836399296732…

![引用图片](https://pbs.twimg.com/media/HCdJ1IZagAAqBWe?format=png&name=large)

* * *

### 热门回复

**@Dan Lincoln Harris** ♥ 24 · 💬 0

来自北大西洋的更多作品。《Bloodlands》。我现在明白了为什么乔恩·舒勒在这片海岸建立了绘画工作室。谢谢，乔恩。

**@Elvis** ♥ 1 · 💬 1

是的，我们现在正在把 JSON 导入 SQLite 呢，哈哈 你对 ACP 的设置是什么？

**@Jun** ♥ 0 · 💬 0

没有项目和产品谈ai方法论都是耍流氓

**@49 Agents - IDE for Humans** ♥ 0 · 💬 0

LLM 轮询用于监控是计算资源的浪费。仅在实际出现问题时触发 AI 的 bash 预检是正确的模式。对于代理管理，ACP 增加了另一层维护——你已经了解的 tmux 会话可能没那么光鲜，但它们