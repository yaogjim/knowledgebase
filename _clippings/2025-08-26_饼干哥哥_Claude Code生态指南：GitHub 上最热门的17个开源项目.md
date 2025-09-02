---
title: "Claude Code生态指南：GitHub 上最热门的17个开源项目"
source: "https://mp.weixin.qq.com/s/vS7PF7c0TIfPZXswfwlQdw"
author:
  - "[[饼干哥哥]]"
published: 2025-08-26
created: 2025-08-26
description:
tags:
  - "饼干哥哥"
---
原创 饼干哥哥 *2025年08月24日 18:08*

我最开始接触Claude Code——这种「代理式终端编程工具」的时候，说实话，很不习惯

于是我安装了很多第三方工具来让它变得更好用，例如安装 ccusage 查看用量、安装 Claudia 把它变回 IDE等等

慢慢的，我意识到一个蓬勃发展的生态系统正在围绕它迅速成形，未来一定会涌现出大量优秀的第三方服务来弥补它的不足、增强它的能力。

  

于是我花了 2 天时间，帮大家整理好了 这 17 个github 上Claude Code 的优秀开源项目

  

无论你是新手还是资深玩家，相信这份清单都能帮你打造出属于效率拉满的 AI 编程工作站，又或者能借鉴开发出新的优秀项目。

![Image](https://mmbiz.qpic.cn/sz_mmbiz_png/RVqfiaDPokvuOSibBkjRRveibfrT0hZ14PMfFwXw8ay7jqPcsmmgwppV8unVJXdGic3QN1YJqw8MWdZev5GpVhfyyQ/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1)

## (文末附使用案例）

## 类型一：工作流编排 / 多代理协作（规范化推进与并行协作）

这类工具专注于管理和协调一个或多个 AI 代理，将复杂的开发任务分解、结构化，并实现自动化流程。

  

### 1\. Claude Taskmaster (推测式开发助理) (★ 20.9k)

https://github.com/eyaltoledano/claude-task-master

最近更新: 2025-08-22

AI 驱动的任务管理 CLI，可将产品规格 (PRD) 转化为可执行的开发任务。它充当 Claude Code 内部的项目“经理”，接收高级目标，然后将需求分解为具体任务，并协调 Claude Code 逐步完成实施。

快速开始:

```
npx task-master-ai --help
```

  

### 2\. Claude-Flow (★ 6.7k)

https://github.com/ruvnet/claude-flow

最近更新: 2025-08-21

这是一个先进的 AI 编排框架，它协调多个 Claude Code 代理以“蜂群”形式处理复杂任务。它引入了蜂巢思维的群体智能和递归工作流，使 Claude 能够派生子代理，让它们协作和批判，并以最少的人工干预迭代地编写、测试和优化代码。

快速开始:

```
npx claude-flow@alpha init --force
npx claude-flow@alpha swarm "Build a REST API" --claude
```

  

### 3\. Claude Squad (★ 4.3k)

https://github.com/smtg-ai/claude-squad

最近更新: 2025-08-09

一个终端应用程序，允许您通过文本用户界面（TUI）并行管理多个 AI 编码代理。它使用 tmux 在独立的窗格中为每个代理创建隔离的会话，让您可以同时监督和协调多个实例处理不同任务，实现“AI 结对编程团队”的方法。

快速开始:

```
brew install claude-squad
cs
```

  

### 4\. Claude Code Spec-Workflow (Spec-Driven Dev) (★ 1.7k)

https://github.com/Pimzino/claude-code-spec-workflow

最近更新: 2025-08

一个为 Claude Code 设计的自动化、规范驱动的开发工作流。它引入了结构化流程，使新功能开发经历“需求 -> 设计 -> 任务 -> 实现”等阶段，而错误修复则遵循“报告 -> 分析 -> 修复 -> 验证”的流程。

快速开始:

```
npm i -g @pimzino/claude-code-spec-workflow
claude-code-spec-workflow
```

  

### 5\. SuperClaude Framework (★ 13.7k)

https://github.com/SuperClaude-Org/SuperClaude\_Framework

最近更新: 2025-08-22

一个配置框架，通过内置的专业命令、认知角色和开发方法来增强 Claude Code。它附带约 19 个额外的斜杠命令和 9 个预定义的“角色”模式（如架构师、测试人员等），您可以激活这些模式来指导 Claude 的辅助风格。

快速开始:

```
pip install --user SuperClaude
superclaude init
```

  

## 类型二：后端路由与模型替换（解耦前端与多模型支持）

这类工具通过代理层拦截和重定向 API 请求，实现 Claude Code 前端与不同 AI 模型后端（如 OpenAI、Gemini）的解耦，提供了灵活的模型选择方案。

  

### 6\. Claude Code Router (★ 14.8k)

https://github.com/musistudio/claude-code-router

最近更新: 2025-08-20

此代理工具可让您将 Claude Code 与不同的模型后端（如 OpenAI、Gemini 等）和自定义工作流结合使用。它拦截 Claude Code 的请求并将其路由到各种提供商，允许 Claude Code 作为前端，而由您决定哪个大语言模型实际处理任务。

快速开始:

```
npm install -g @musistudio/claude-code-router
claude-code-router init
claude-code-router start
```

  

### 7\. Claude Code Proxy (OpenAI/Gemini Router) (★ 2.0k)

https://github.com/1rgs/claude-code-proxy

最近更新: 2025-08-22

一个 Anthropic API 代理，允许 Claude Code 与非 Anthropic 模型后端（如 OpenAI 的 GPT 或 Google 的 Gemini）一起使用。此代理将 Claude 的模型名称映射到指定的 OpenAI/Gemini 模型，因此您可以在这些模型的响应上运行 Claude Code 界面。

快速开始:

```
git clone https://github.com/lrgs/claude-code-proxy
cd claude-code-proxy
uvicorn server:app --port 8082
```

  

## 类型三：交互界面与编辑器集成（GUI 与 IDE 深度融合）

这类工具将 Claude Code 的核心功能从命令行界面中解放出来，通过提供桌面 GUI、Web 客户端或深度集成到 IDE中，优化开发者的交互体验。

  

### 8\. Claudia - Claude Code GUI & Toolkit (★ 13.9k)

https://github.com/getAsterisk/claudia

最近更新: 2025-08-15

这是一款功能强大的 Claude Code 桌面 GUI 应用程序和工具包。它提供了一个用户友好的界面来创建自定义子代理、通过点击操作管理交互式会话，以及可视化项目上下文，从而无需直接使用 CLI 即可轻松协调 AI 辅助开发。

快速开始:

```
git clone https://github.com/getAsterisk/claudia.git
cd claudia && npm install
cp .env.example .env
npm run dev
```

  

### 9\. Claude Code UI (Web/Mobile) (★ 3.3k)

https://github.com/siteboon/claudecodeui

最近更新: 2025-08-15

一个基于 Web 且适合移动设备的 Claude Code 客户端。它在浏览器中提供了一个响应式的聊天界面，连接到您在服务器上运行的 Claude Code CLI，让您可以通过图形界面而不是终端远程管理会话和审查输出。

快速开始:

```
git clone https://github.com/siteboon/claudecodeui.git
cd claudecodeui && npm install
npm run dev
```

  

### 10\. Claude Code Neovim Extension (★ 0.9k)

https://github.com/coder/claudecode.nvim

最近更新: 2025-07-02

一个 Neovim 插件，将 Anthropic 的 Claude Code 助手集成到 Neovim 中，完全用 Lua 实现。它为 Neovim 用户提供了完整的 Claude Code 体验，包括 AI 聊天、内联差异审查和代码生成等，有效地将 Neovim 转变为一个由 AI 驱动的 IDE。

快速开始:

```
{
  "coder/claudecode.nvim",
  dependencies = { "folke/snacks.nvim"},
  config = true
}
```

## 类型四：生态扩展与能力增强（插件、模板与社区资源）

这类工具通过提供预设模板、专用子代理、自动化插件（斜杠命令）以及连接外部工具的 MCP 服务器，共同构成了丰富的生态系统，极大地扩展了 Claude Code 的原生能力。

### 11\. Awesome Claude Code (★ 12.1k)

https://github.com/hesreallyhim/awesome-claude-code

最近更新: 2025-08-19

这是一个精心策划的列表，包含各种斜杠命令、 CLAUDE.md 模板、CLI 工具和其他资源，用于增强您的 Claude Code 工作流程。该存储库是社区知识库，可帮助开发人员充分利用 Anthropic 的 CLI AI 编码助手。

快速开始:

```
git clone https://github.com/hesreallyhim/awesome-claude-code.git
cd awesome-claude-code
open README.md
```

  

### 12\. Claude Code Subagents Collection (★ 9.9k)

https://github.com/wshobson/agents

最近更新: 2025-08-20

提供超过 75 个专业子代理的全面集合，每个子代理都充当领域专家以扩展 Claude 的能力。这些子代理（例如“Python Pro”或“DevOps 疑难解答员”）通过自定义的系统提示和工具来处理特定的编程领域，从而增强开发工作流程。

快速开始:

```
git clone https://github.com/wshobson/agents.git
cp agents/*.md ~/.claude/agents/
```

  

### 13\. Claude Code Templates (★ 4.7k)

https://github.com/davila7/claude-code-templates

最近更新: 2025-08-23

一个 CLI 工具，为 Claude Code 提供快速启动配置模板和监控功能。它提供针对特定框架的预设命令和“项目模板”，让您可以通过一个步骤为新项目搭建好 Claude Code 的设置，同时还包含实时跟踪使用情况的实用程序。

快速开始:

```
npm install -g claude-code-templates
claude-code-templates init my-react-app
```

  

### 14\. Awesome Claude Code MCP Servers (★ 3.6k)

https://github.com/appcypher/awesome-mcp-servers

最近更新: 2025-08

这是一个精选的模型上下文协议 (MCP) 服务器列表，可以扩展 Claude Code 的能力。MCP 服务器允许 AI 模型安全地与文件系统、数据库、Web API 等工具进行交互。

快速开始:

```
pip install mcp-file-server
claude --connect file-server
```

  

### 15\. CCPlugins - Claude Code Plugins (★ 2.0k)

https://github.com/brennercruvinel/CCPlugins

最近更新: 2025-08-02

这是一个包含 24 个预定义斜杠命令的包，用于增强 Claude Code CLI 的自动化能力。它为常见任务（如清理、格式化、构建和测试等）提供了一键式命令，让您不必持续输入冗长的指令。

快速开始:

```
git clone https://github.com/brennercruvinel/CCPlugins.git
cd CCPlugins && python install.py
```

  

## 类型五：监控与度量（用量与成本可视化/统计）

这类工具专注于追踪和分析 Claude Code 的 API 调用消耗，通过实时仪表盘或离线日志分析，帮助开发者可视化 Token 用量与预估成本，以优化开销。

### 16\. Claude Code Usage Monitor (★ 4.5k)

https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor

最近更新: 2025-08-18

一个用于在当前会话中监控 Claude Code 的 token 使用量和成本的实时终端仪表板。此监控器会显示实时的 token 消耗情况，并能预估您何时会达到 token 限制，在您接近计划配额时发出警告。

快速开始:

```
claude-monitor --live
```

  

### 17\. CC Usage (Claude Code Usage Analyzer) (★ 7.2k)

https://github.com/ryoppippi/ccusage

最近更新: 2025-08

这是一个用于从本地日志文件分析您的 Claude Code token 使用量和成本消耗的命令行工具。它读取 Claude Code 的 .jsonl 对话日志，并生成关于您使用了多少 token 及其成本的详细报告。

快速开始:

```
npx ccusage@latest daily
```

  

  

这些工具，当然没必要全都装，分享一下我自己的方案。

我最近打算开发一个功能复杂的全栈 Web 应用，于是：

1. 1\. 第一步：搭建监控与交互环境
- 安装 Claude Code Usage Monitor ，实时监控 Token 消耗
	- 安装 Claudia ，恢复 GUI 操作体验
3. 2\. 第二步：增强核心能力
- 在 Claudia 环境中，集成 Claude Code Subagents Collection ，这样就拥有了“前端专家”、“数据库专家”等超多领域的 Sub-Agents
	- 同时，安装 CCPlugins ，将常用的代码清理、格式化等操作封装成一键命令
5. 3\. 第三步：引入自动化工作流
- 项目启动时，使用 Claude Taskmaster ，直接将产品需求文档（PRD）喂给它，自动分解为一系列清晰、可执行的开发任务，并交由Agents 逐步完成。

  

你的 Claude Code 用了哪些工具呢？

还有什么工具很好用但没在这清单里的？

欢迎评论分享

---

以上，

## 既然看到这里了，如果觉得不错，随手点个赞、推荐、转发三连吧，你的支持是我持续创作的动力。我们下期见。

为了帮助大家减少AI信息差，饼干哥哥拉了个AI交流群，围绕着 AI数据分析、AI编程、AI工作流、AI Agent 等进行讨论。

感兴趣的可以关注公众号「饼干哥哥AGI」， 后台回复「AI交流群」

  

补充阅读：

[我从X和Reddit扒了这12 个高级玩法，把 Claude Code 变成可交付系统](https://mp.weixin.qq.com/s?__biz=MjM5NDI4MTY3NA==&mid=2257494118&idx=1&sn=dc09dc3daee2cc1b5f3521f854153ff8&scene=21#wechat_redirect)

[Claude Code 太烧钱？你 80% 的成本可能都被浪费了！附省钱攻略](https://mp.weixin.qq.com/s?__biz=MjM5NDI4MTY3NA==&mid=2257494095&idx=1&sn=01a2daad14d59da67d18c0adc49a8820&scene=21#wechat_redirect)

[用Claude Code，24小时把网站SEO干到谷歌第一，并赚3000美金](https://mp.weixin.qq.com/s?__biz=MjM5NDI4MTY3NA==&mid=2257494005&idx=1&sn=dcf74c56af01bdce9cf2f461535b0821&scene=21#wechat_redirect)

[30 个进阶技巧彻底榨干Claude Code价值：工作流、上下文交互、拓展与自动化、架构与重构、性能与协作......](https://mp.weixin.qq.com/s?__biz=MjM5NDI4MTY3NA==&mid=2257493862&idx=1&sn=09003be42ca7a5403951926e25d574ae&scene=21#wechat_redirect)

[发现个用 Claude Code 的高效...](https://mp.weixin.qq.com/s?__biz=MjM5NDI4MTY3NA==&mid=2257493787&idx=1&sn=60c3b2346fefbbad513eafb61350205d&scene=21#wechat_redirect)

[两句话，让Claude Code+Kimi K2 跑了3小时爬完17个竞品网站、做了一份深度市场数据分析报告](https://mp.weixin.qq.com/s?__biz=MjM5NDI4MTY3NA==&mid=2257493673&idx=1&sn=43b968ba894b62c86ba961e7e005963f&scene=21#wechat_redirect)

继续滑动看下一个

饼干哥哥AGI

向上滑动看下一个

Clip to Feishu Docs