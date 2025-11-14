---
title: "2025-11-14_shao_meng_开源推荐_Multi_Agent_Research_System_Anthropic_开源"
source: "https://x.com/shao__meng/status/1988873500745175233"
author:
  - "[[@shao__meng]]"
published: 2025-11-14
created: 2025-11-14
description:
tags:
  - "x"
  - "@shao__meng"
  - "research"
  - "claude"
---

# [开源推荐] Multi-Agent Research System Anthropic 开源

**meng shao** @shao\_\_meng 2025-11-12

\[开源推荐\] Multi-Agent Research System: Anthropic 开源的基于 Claude Agent SDK 的演示项目，模拟“深度研究”流程：通过多个 AI 智能体协作，高效处理复杂主题的研究和报告生成。

系统核心组件

系统定义了两种主要子智能体，均使用 Claude Haiku 模型驱动：

· 研究智能体（Researcher）：负责分解主题并搜索信息。工具包括 WebSearch（网页搜索）和 Write（写入笔记）。它将研究结果保存到 files/research\_notes 文件夹中，支持并行执行多个实例。

· 报告撰写智能体（Report-Writer）：负责整合研究笔记，生成最终输出。工具包括 Read（读取文件）和 Write to Glob（全局写入报告）。它从 files/reports 文件夹中读取并合成内容。

工作流程

1\. 主题分解：用户输入研究查询，主智能体自动拆分为 2-4 个子主题（例如，“AI 伦理”可拆为“历史发展”“当前挑战”“未来趋势”）。

2\. 并行研究：为每个子主题启动一个 Researcher 智能体，同时进行网页搜索并记录关键发现到独立文件，避免信息丢失。

3\. 信息整合：主智能体扫描研究笔记，确保覆盖完整性。

4\. 报告生成：启动 Report-Writer 智能体，读取所有笔记，合成结构化报告（如 Markdown 或扩展为 PPT/网页），保存到 files/reports。

5\. 输出：用户获得一份综合报告，支持迭代修改。

优势与扩展性

· 高效性：并行智能体加速研究，适用于学术、商业或内容创作场景。

· 客观性：依赖事实搜索和合成，减少主观偏差。

· 自定义潜力：可扩展工具（如添加 PowerPoint 生成或数据可视化），或集成其他 Claude 功能。

开源地址

https://github.com/anthropics/claude-agent-sdk-demos/tree/main/research-agent…

> 2025-11-12
> 
> We built a Deep Research demo for the Claude Agent SDK!
> 
> It's one our most requested use cases: spawn multiple AI agents to research a topic in parallel, then synthesize their findings into a report.
> 
> 🧵 on how it works:
> 
> 我们为 Claude 智能体 SDK 打造了一款深度研究演示！
> 
> 这是我们最常被要求实现的应用场景之一：同时启动多个 AI 代理并行研究某个主题，然后将它们的研究结果整合成一份报告。
> 
> 🧵 关于其工作原理：
> 
> ![Screenshot of the Multi-Agent Research System interface in Chinese, featuring title Multi-Agent Research System with Anthropic logo. Sections include system overview describing Anthropic open-source project based on Claude Agent SDK for simulating deep research via multiple AI agents. Core components detail Researcher agent using Claude Haiku model with tools WebSearch and Write for information gathering and note saving. Report-Writer agent with Read and Write to Glob for synthesizing reports. Workflow steps numbered 1 to 5: theme decomposition, parallel research, information integration, report generation, and output. Evaluation section with icons for evaluation criteria.](https://pbs.twimg.com/media/G5nlz6ObQAAGDFn?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G5k6nWxacAkTfe8?format=jpg&name=large)

* * *

**索骥** @JasonLee66659 [2025-11-13](https://x.com/JasonLee66659/status/1989117506527916278)

烧不起token啊

* * *

**Realtor.com** @realtordotcom

Only 3 in 10 Veterans know about 0% down home loans.

Join our mission to help veterans find their way home.

只有十分之三的退伍军人了解零首付住房贷款。

加入我们的使命，帮助退伍军人找到回家的路。