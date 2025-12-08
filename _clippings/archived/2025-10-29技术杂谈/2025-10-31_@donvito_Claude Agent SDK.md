---
title: "Claude Agent SDK"
source: "https://x.com/donvito/status/1983851704975327473"
author:
  - "[[@donvito]]"
published: 2025-10-31
created: 2025-10-31
description: "Principal AI Scientist @ In-Parallel | ex CIO/CAIO @ Resoniks"
tags:
  - "@donvito #ClaudeAgentSDK #AI智能体 #代理 #MCP #子代理 #翻译"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-11-13"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---
**Melvin Vivas** @donvito [2025-10-30](https://x.com/donvito/status/1983851704975327473)

  
我想到为何不直接使用 Claude Agent SDK 来创建非编程工作流，而非要用其他 AI 智能体框架呢  
  
于是我用一个简单案例验证了这个想法——新闻调研智能体。虽不确定方案是否具备扩展性，但其中蕴含了几个核心概念。  
  
首要概念是采用 MCP 架构。我通过 @firecrawl\_dev 的 MCP 服务进行网络搜索获取最新资讯，随后智能体将采集的数据进行摘要处理，并生成包含结果的 markdown 文档

第二个概念是运用子代理。在此应用场景中，我需要对结果进行翻译处理。因此，我创建了一个名为 translator-agent 的子代理，并指示主代理在执行该任务时调用这一翻译子代理。

生成了两个 Markdown 文件，一份为英文原版，另一份为翻译后的版本

Claude Agent SDK 功能非常强大，因为它支持工具、MCP、技能和子代理。这些功能与其他智能体 SDK 所提供的完全一致。

我们已经见识过 Claude 代码框架的强大威力，我认为应该充分利用 @claudeai 团队构建的技术成果  
  
本次示例我采用了 GLM 4.6 模型  
  
不过它当然也能完美兼容 @claudeai 的 Haiku 和 Sonnet 模型！

![Dark-themed screenshot displays multiple open windows including code editor with Python script using claudeai library and agent definitions web search tool and translator agent configuration browser tabs showing latest news topics for October 2023 in Korean and English quarterly corporate developments page with text sections and sidebar navigation in a development environment setup](https://pbs.twimg.com/media/G4gKQDCawAAv8dm?format=jpg&name=large)