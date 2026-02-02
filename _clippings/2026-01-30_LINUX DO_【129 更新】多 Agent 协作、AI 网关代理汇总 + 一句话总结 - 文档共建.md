---
title: "【1/29 更新】多 Agent 协作、AI 网关/代理汇总 + 一句话总结 - 文档共建"
source: "https://linux.do/t/topic/1486332"
author:
  - "[[LINUX DO]]"
date: "2026-01-30T19:11:02+08:00"
created: 2026-01-30
description: "▶ 更新日志多智能体协作项目一句话总结Claude-Code-WorkflowClaude + Codex + Gemini + Qwen，JSON 驱动的大型项目管理4级工作流系统，含有实操指南和 Dashboar…"
tags:
  - "LINUX DO"
---
## post by ageovb on Jan 19

[72](https://linux.do/u/ageovb) [ageovb](https://linux.do/u/ageovb) 文化宣导员

[11d](https://linux.do/t/topic/1486332 "Post date")

更新日志
```
2026-01-29 添加 gpt-load
2026-01-28 添加 Aether
2026-01-25 添加 oh-my-claudecode
2026-01-24 添加 happy
```

## 多智能体协作

| 项目 | 一句话总结 |
| --- | --- |
| **[Claude-Code-Workflow](https://github.com/catlog22/Claude-Code-Workflow/tree/main)** | Claude + Codex + Gemini + Qwen，JSON 驱动的大型项目管理4级工作流系统，含有实操指南和 Dashboard |
| **[Coder-Codex-Gemini](https://github.com/FredericMN/Coder-Codex-Gemini)** | Claude + Coder + Codex + Gemini， 让 **Claude/Sisyphus** 作为架构师调度 **Coder** 执行代码任务、 **Codex** 审核代码质量， **Gemini** 提供专家咨询，形成 **自动化的多方协作闭环** |
| **[ccg-workflow](https://github.com/fengshao1227/ccg-workflow)** | 基于 Claude Code，整合 Codex/Gemini 后端能力，提供智能路由、代码审查、Git 工具等 17+ 个命令 |
| **[claude-team-mcp](https://github.com/7836246/claude-team-mcp)** | Claude + Codex + Gemini，多智能体 MCP 服务器 |
| **[claude\_code\_autoflow](https://github.com/bfly123/claude_code_autoflow)** | 自动化任务分配与角色预设切换，与下面的 ccb 配合使用 |
| **[claude\_code\_bridge](https://github.com/bfly123/claude_code_bridge)** | Claude + Codex + Gemini，实时分屏显示多 AI 协作，配合上面的 cca 使用 |
| **[myclaude](https://github.com/cexll/myclaude/tree/master)** | Claude + Codex + Gemini，双智能体架构与可插拔 AI 后端 |
| **[skills](https://github.com/GuDaStudio/skills)** | Claude Code 技能扩展包，一键集成多模型协作 |
| **[oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)** | **Claude Code 的多智能体编排** |

## AI 网关/代理服务

| 项目 | 一句话总结 |
| --- | --- |
| **[Aether](https://github.com/fawney19/Aether)** | 支持 Claude / OpenAI / Gemini 及其 CLI 客户端的统一接入层 |
| **[Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager)** | 反重力账号管理与路由网关 |
| **[ccNexus](https://github.com/lich0821/ccNexus)** | Claude/Codex 智能端点轮换与 API 格式转换 |
| **[cc-switch](https://github.com/farion1231/cc-switch/blob/main/README_ZH.md)** | Claude/Codex 多账号快速切换工具 |
| **[CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI)** | CLI 转标准 API 的多账号代理服务 |
| **[claude-code-router](https://github.com/musistudio/claude-code-router/blob/main/README_zh.md)** | Claude Code 专业路由与模型映射工具 |
| **[claude-relay-service](https://github.com/Wei-Shaw/claude-relay-service)** | Claude Code 一站式镜像中转拼车服务 |
| **[gpt-load](https://github.com/tbphp/gpt-load)** | 智能密钥轮询的多渠道 AI 代理 |

## 桌面 GUI 应用

| 项目 | 一句话总结 |
| --- | --- |
| **[aio-coding-hub](https://github.com/dyndynjyxa/aio-coding-hub)** | **本地 AI CLI 统一网关** — 让 Claude Code / Codex / Gemini CLI 请求走同一个入口 |
| **[AionUi](https://github.com/iOfficeAI/AionUi/tree/main)** | 跨平台 AI 编程工具，支持 CoWork |
| **[axonhub](https://github.com/looplj/axonhub)** | 现代 AI 网关与 RBAC 权限控制系统 |
| **[hapi](https://github.com/tiann/hapi)** | 支持 Web/Telegram 的远程 AI 编程控制台 |
| **[happy](https://github.com/slopus/happy)** | 为 Claude Code 和 Codex 打造的端到端加密的跨平台（移动端及网页版）AI 编程助手客户端 |
| **[octopus](https://github.com/bestruirui/octopus)** | API 聚合与负载均衡管理平台 |

> 建议复制下面内容，让 AI 分类对比，结果更为详细

- Aether - [GitHub - fawney19/Aether](https://github.com/fawney19/Aether)
- aio-coding-hub - [GitHub - dyndynjyxa/aio-coding-hub: 一个All In One的本地AI工具, 支持Win/Mac/Linux](https://github.com/dyndynjyxa/aio-coding-hub)
- Antigravity-Manager - [GitHub - lbjlaq/Antigravity-Manager: Professional Antigravity Account Manager & Switcher. One-click seamless account switching for Antigravity Tools. Built with Tauri v2 + React (Rust).专业的 Antigravity 账号管理与切换工具。为 Antigravity 提供一键无缝账号切换功能。](https://github.com/lbjlaq/Antigravity-Manager)
- axonhub - [GitHub - looplj/axonhub: AxonHub is a modern AI gateway system that provides a unified OpenAI ( Chat Completion, Responses), Anthropic, Gemini and AI SDK compatible API](https://github.com/looplj/axonhub)
- Coder-Codex-Gemini - [GitHub - FredericMN/Coder-Codex-Gemini: CCG 多模型协作框架：Claude + Coder + Codex + Gemini | 支持 Claude Code & OpenCode 双环境 / CCG Multi-model Collaboration: Claude + Coder + Codex + Gemini | Supports Claude Code & OpenCode](https://github.com/FredericMN/Coder-Codex-Gemini)
- CLIProxyAPI - [GitHub - router-for-me/CLIProxyAPI: Wrap Gemini CLI, Antigravity, ChatGPT Codex, Claude Code, Qwen Code, iFlow as an OpenAI/Gemini/Claude/Codex compatible API service, allowing you to enjoy the free Gemini 2.5 Pro, GPT 5, Claude, Qwen model through API](https://github.com/router-for-me/CLIProxyAPI)
- ccNexus - [GitHub - lich0821/ccNexus: Intelligent API gateway for Claude Code and Codex CLI - rotate endpoints, monitor usage, and seamlessly integrate OpenAI, Gemini, and other platforms.](https://github.com/lich0821/ccNexus)
- ccg-workflow - [GitHub - fengshao1227/ccg-workflow: 多模型协作开发工具集 - 基于 Claude Code CLI，整合 Codex/Gemini 后端能力，提供智能路由、代码审查、Git 工具等 17+ 个命令](https://github.com/fengshao1227/ccg-workflow)
- cc-switch - [GitHub - farion1231/cc-switch: A cross-platform desktop All-in-One assistant tool for Claude Code, Codex, OpenCode & Gemini CLI.](https://github.com/farion1231/cc-switch)
- claude-code-autoflow - [GitHub - bfly123/claude\_code\_autoflow](https://github.com/bfly123/claude_code_autoflow)
- claude-code-bridge - [GitHub - bfly123/claude\_code\_bridge: Real-time multi-AI collaboration: Claude, Codex & Gemini with persistent context, minimal token overhead](https://github.com/bfly123/claude_code_bridge)
- claude-code-router - [GitHub - musistudio/claude-code-router: Use Claude Code as the foundation for coding infrastructure, allowing you to decide how to interact with the model while enjoying updates from Anthropic.](https://github.com/musistudio/claude-code-router)
- claude-relay-service - [GitHub - Wei-Shaw/claude-relay-service: CRS-自建Claude Code镜像，一站式开源中转服务，让 Claude、OpenAI、Gemini、Droid 订阅统一接入，支持拼车共享，更高效分摊成本，原生工具无缝使用。](https://github.com/Wei-Shaw/claude-relay-service)
- claude-team-mcp - [GitHub - 7836246/claude-team-mcp: 🤖 Multi-Agent MCP Server - Let Claude Code / Windsurf / Cursor orchestrate GPT, Claude, Gemini to work as an AI dev team](https://github.com/7836246/claude-team-mcp)
- Claude-Code-Workflow - [GitHub - catlog22/Claude-Code-Workflow: JSON-driven multi-agent development framework with intelligent CLI orchestration (Gemini/Qwen/Codex), context-first architecture, and automated workflow execution](https://github.com/catlog22/Claude-Code-Workflow)
- gpt-load - [GitHub - tbphp/gpt-load: Multi-channel AI proxy with intelligent key rotation. 智能密钥轮询的多渠道 AI 代理。](https://github.com/tbphp/gpt-load)
- hapi - [GitHub - tiann/hapi: App for Claude Code / Codex / Gemini, vibe coding anytime, anywhere](https://github.com/tiann/hapi)
- happy - [GitHub - slopus/happy: Mobile and Web client for Codex and Claude Code, with realtime voice, encryption and fully featured](https://github.com/slopus/happy)
- myclaude - [GitHub - cexll/myclaude: Multi-agent orchestration workflow (Claude Code Codex Gemini OpenCode)](https://github.com/cexll/myclaude)
- octopus - [GitHub - bestruirui/octopus: One Hub All LLMs For You | 为个人打造的 LLM API 聚合服务](https://github.com/bestruirui/octopus)
- oh-my-claudecode - [GitHub - Yeachan-Heo/oh-my-claudecode: Multi-agent orchestration for Claude Code with 5 execution modes: Autopilot (autonomous), Ultrapilot (3-5x parallel), Swarm (coordinated agents), Pipeline (sequential chains), Ecomode (token-efficient). 31+ skills, 32 specialized agents, zero learning curve.](https://github.com/Yeachan-Heo/oh-my-claudecode)
- skills - [https://github.com/GuDaStudio/skil](https://github.com/GuDaStudio/skil)

## post by sunfly on Jan 19

[sunfly](https://linux.do/u/sunfly) 不二之选

[11d](https://linux.do/t/topic/1486332/2 "Post date")

最好写点儿介绍文字