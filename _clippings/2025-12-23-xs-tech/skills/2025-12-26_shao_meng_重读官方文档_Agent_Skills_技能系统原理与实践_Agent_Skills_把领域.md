---
title: "2025-12-26_shao_meng_重读官方文档_Agent_Skills_技能系统原理与实践_Agent_Skills_把领域"
source: "https://x.com/shao__meng/status/2004162418394780041"
author:
  - "[[@shao__meng]]"
published: 2025-12-26
created: 2025-12-26
description:
tags:
  - "#wechat"
  - "x"
  - "@shao__meng"
  - "https"
---

# [重读官方文档] Agent Skills 技能系统原理与实践 Agent Skills 把领域

**meng shao** @shao\_\_meng [2025-12-25](https://x.com/shao__meng/status/2004162418394780041)

\[重读官方文档\] Agent Skills 技能系统原理与实践

Agent Skills 把领域特定知识、工作流程、最佳实践打包成可重用的“技能包”，让通用 AI Agent 转变为专精于特定任务的 Agent。不同于一次性提示，Skills 是基于文件系统的资源，按需加载，避免重复指导。

https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview…

Anthropic 已将 Agent Skills 标准正式开放：

https://agentskills.io/home

Agent Skills 核心优势包括：

· 将 AI Agent 专精化，适应特定领域任务

· 一次性创建，跨会话自动复用

· 支持技能组合，构建复杂工作流

· 通过“渐进披露”机制，仅加载相关内容，高效管理上下文窗口

核心概念与工作原理

Agent Skills 可基于 Agent 的 VM 环境运行，利用文件系统访问、bash 命令和代码执行能力。每个 Skill 是一个目录，核心文件为 SKILL. md，包含 YAML 元数据和 markdown 指令。

加载分为三个级别，实现渐进披露：

· 级别1：元数据（始终加载）：YAML 中的 name 和 description，轻量预载入系统提示，帮助 Claude 判断何时触发（几乎无 token 消耗）。

· 级别2：主要指令（触发时加载）：SKILL. md 正文，提供流程指导、示例代码等（通常 <5k tokens）。

· 级别3：资源与代码（按需加载）：额外 markdown 文件、脚本、模板或参考资料。通过 bash 读取文件或执行脚本，仅输出进入上下文（无上限限制）。

这种架构允许 Skill 包含大量内容（如完整 API 文档、大型示例），但只在需要时占用上下文。AI Agent 使用 bash 命令（如 cat SKILL. md 或 python script. py）访问内容，确保高效和确定性。

预构建 Skills

Anthropic 提供预构建 Skills，可以看这个开源项目：

https://github.com/anthropics/claude-cookbooks/tree/main/skills…

最佳实践

· 元数据描述：清晰描述“技能做什么” + “何时使用”（触发条件），帮助 Claude 准确匹配用户意图。

· 指令结构：在 SKILL. md 中提供清晰步骤、快速入门、示例；拆分复杂内容到子文件，避免单文件过长。

· 利用脚本：优先用可执行脚本处理确定性操作（如数据验证、文件处理），输出高效且不占上下文。

· 渐进设计：从评估 AI Agent 能力缺口开始，迭代测试；提供丰富示例，提升鲁棒性。

· 范围控制：技能专注单一领域，便于组合使用；从简单任务起步，逐步扩展。

· 测试迭代：观察 Claude 是否正确触发和使用，必要时让 Claude 自我反思改进。

https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices…

![Image](https://pbs.twimg.com/media/G9A3Ei4bQAAal_1?format=jpg&name=large)

* * *

**Mio** @Mio1722729 [2025-12-25](https://x.com/Mio1722729/status/2004235562161787175)

这个排版好好啊！哥有空了能出个教程吗😍😍

* * *

**meng shao** @shao\_\_meng [2025-12-25](https://x.com/shao__meng/status/2004340830207988225)

在这里哈:

> 2025-11-30
> 
> 信息卡提示词，在小红书和公众号都做了合集，会持续更新不同风格。
> 
> 小红书：
> 
> https://xiaohongshu.com/collection/item/692be4800078000000000001?xhsshare=CopyLink&appuid=6437ec66000000000e01f05f&apptime=1764484456&share\_id=0a42ba1d33ac412288c9a7c95916620b&share\_channel=copy\_link…
> 
> 公众号：
> 
> https://mp.weixin.qq.com/mp/appmsgalbum?\_\_biz=MzkwNDExODE4Nw==&action=getalbum&album\_id=4107369467909505031&scene=126#wechat\_redirect…
> 
> https://mp.weixin.qq.com/mp/appmsgalbum?\_\_biz=MzkwNDExODE4Nw==&action=getalbum&album\_id=4108352062407311366&scene=126#wechat\_redirect…
> 
> ![Image](https://pbs.twimg.com/media/G6-7NJVbkAI9Jg6?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G6-7NKFbkAIU4jS?format=jpg&name=large)