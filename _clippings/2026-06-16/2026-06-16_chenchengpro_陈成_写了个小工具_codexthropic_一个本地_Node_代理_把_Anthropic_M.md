---
title: "2026-06-16_chenchengpro_陈成_写了个小工具_codexthropic_一个本地_Node_代理_把_Anthropic_Me"
source: "https://x.com/chenchengpro/status/2049378400859729958"
author:
  - "[[@chenchengpro]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "x"
  - "@chenchengpro"
  - "codex"
  - "💬"
---

# 陈成: 写了个小工具 codexthropic，一个本地 Node 代理，把 Anthropic Messages API 翻译成 OpenAI Codex Respo…

**陈成**

写了个小工具 codexthropic，一个本地 Node 代理，把 Anthropic Messages API 翻译成 OpenAI Codex Responses API。实际效果：你可以用 Claude Code 直接连 OpenAI 的 GPT-5.5 后端写代码。

做这个的动机很直接——Claude Code 是目前最好的 AI coding agent 前端，但它只说 Anthropic 协议。Codex 后端（GPT-5.5）的代码能力也很强，但只有 OpenAI 自家的 Codex CLI 能用。codexthropic 在中间做协议翻译，让两边的长处接上。

技术上要处理的东西比想象中多：

1）SSE 流式事件双向映射。Anthropic 的 message\_start / content\_block\_start / content\_block\_delta / content\_block\_stop / message\_delta / message\_stop 这套事件模型，和 Codex 的 response.created / response.output\_text.delta / response.output\_item.added / response.completed 完全是两套语言，逐事件翻译，还要维护 block index 状态机。

2）Tool Use 完整映射。Anthropic 的 tools 定义转成 Codex 的 function tools，tool\_use block 转成 function\_call item，tool\_result 转成 function\_call\_output。tool\_choice 也要映射：auto→auto，any→required，none→none，指定工具名→{type:function, name}。

3）多轮推理连续性——这个最巧妙。Codex 的 reasoning.encrypted\_content 是加密的思维链状态，需要在多轮工具调用间传递才能保持推理连贯。方案是把它塞进 Anthropic thinking block 的 signature 字段，Claude Code 会原样回传 thinking blocks，下一轮请求时再从 signature 还原成 Codex 的 reasoning input item。链式思维跨轮次不断。

4）OAuth 认证。读 ~/.codex/auth.json，JWT 过期前 60s 自动刷新，并发请求用 single-flight 合并避免重复刷新。刷新失败有 30s 冷却防止锁死风暴。收到 401 会 force-refresh 重试一次。如果 Codex CLI 在后台轮换了 refresh\_token，代理会检测磁盘文件变化自动重载，不用重启。原子写入用 tmp+fsync+rename 保证不写坏 auth 文件。

5）reasoning effort 翻译。Anthropic 的 thinking.budget\_tokens 按阈值映射：<4000→low，<16000→medium，<32000→high，≥32000→xhigh。adaptive thinking 和 output\_config.effort:max 也走 xhigh。

模型映射：所有 Claude 模型名（opus/sonnet/haiku）统一映射到 gpt-5.5，因为 ChatGPT 账号的 Codex 后端目前只接受这个模型。gpt-\* 和 o\* 开头的模型名直接透传。

用法极简：npx codexthropic@latest 启动代理，另一个终端 ANTHROPIC\_BASE\_URL=http://127.0.0.1:8765 ANTHROPIC\_API\_KEY=any claude 即可。零运行时依赖，纯 node:http 实现，88 个离线测试覆盖各种边界情况。需要 Node 20+ 和 codex login 完成过的本地认证。

![图片](https://pbs.twimg.com/media/HHDask2aUAAZoD3?format=jpg&name=large)

* * *

### 热门回复

**@lencx** ♥ 187 · 💬 9

Codex Pet Skill 设计有点精妙，忍不住写了一篇长文解析。

https://

mp.weixin.qq.com/s/uH71k1yAoF6x

jsOYmVAJBg

…

Skill 的本质不是角色扮演，也不只是轻量 workflow，而是把不可控的模型能力关进可控的工程边界里。

Pet Skill：

https://

github.com/openai/skills/

tree/main/skills/.curated/hatch-pet

…

**@Serotonin** ♥ 83 · 💬 3

2025年链上信贷从2.52亿美元增长到55.6亿美元，实现了22倍的增长。这是完整图谱：每一个协议、每一个资本配置者、每一个风险层。

**@VitaminB2** ♥ 1 · 💬 2

cc switch里面本来不就可以吗

**@Jingchao** ♥ 0 · 💬 0

只能使用 Key 么？官方订阅这种模式是不是不能用？

**@Thanh Nguyen** ♥ 0 · 💬 0

已经有相当多类似的产品了。就像是一个 API 代理。