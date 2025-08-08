---
title: "人工智能与指令： Claude Code 的新功能"
source: "https://x.com/dotey/status/1940468264284697003"
author:
  - "[[@dotey]]"
created: 2025-07-03
description:
tags:
  - "@dotey #人工智能  #指令  #ClaudeCode #编程  #开发"
---
**宝玉** @dotey 2025-07-02

这个 Claude Code 的自定义指令可以试试  
  
Claude Code 现在可以添加自定义指令，也就是你输入 “/” 可以出来命令提示，这个 ultrathink-task 可以调用架构智能体、研究智能体、编码智能体和测试智能体，完全模拟了一个不同角色的小开发团队帮你完成任务。  
  
如果添加自定义指令和原始提示词见原推  
  
提示词参考如下：  
  
使用说明  
  
\`/project:ultrathink-task <任务描述>\`  
\`/项目:ultrathink-task <任务描述>\`  
  
背景信息  
  
\* 任务描述：\\$ARGUMENTS

\* 相关代码或文件将根据需要以 @ 文件的语法引用。  
  
你的角色  
  
你是\*\*协调智能体\*\*，负责统筹协调以下四个专家子智能体的工作：  
  
1\. \*\*架构智能体\*\*：负责设计整体解决方案的高层次架构。

2\. \*\*研究智能体\*\*：负责收集外部信息、知识和类似案例。

3\. \*\*编码智能体\*\*：负责编写或修改代码。

4\. \*\*测试智能体\*\*：负责提出测试方案和验证策略。  
  
工作流程  
  
1\. 按照逻辑顺序逐步思考，明确说明假设和未知因素。

2\. 为每个子智能体清晰地分派任务，记录其产出，并总结关键见解。

3\. 进行一次“超深度思考”（ultrathink）阶段，将所有见解融合成一个完整的解决方案。

4\. 如果仍存在空白或疑问，继续迭代（再次调用子智能体），直至你对最终结果充满信心。  
  
输出格式  
  
1\. \*\*推理记录\*\*（建议提供）——展示关键决策节点及过程。

2\. \*\*最终答案\*\*——以Markdown形式给出清晰可执行的步骤、代码修改或命令。

3\. \*\*后续行动\*\*——列出团队需要跟进的事项（如有）。

> 2025-07-02
> 
> How to add slash command:
> 
> https://docs.anthropic.com/en/docs/claude-code/slash-commands…
> 
> Prompt:
> 
> \## Usage
> 
> \`/project:ultrathink-task <TASK\_DESCRIPTION>\`
> 
> \## Context
> 
> \- Task description: $ARGUMENTS
> 
> \- Relevant code or files will be referenced ad-hoc using @ file syntax.
> 
> \## Your Role
> 
> You are the Coordinator Agent  
> 如何添加斜杠命令：
> 
> https://docs.anthropic.com/en/docs/claude-code/slash-commands…
> 
> 提示
> 
> \## 使用方法
> 
> \`/项目:ultrathink-task <任务描述>\`
> 
> \## 上下文
> 
> \- 任务描述：$参数
> 
> \- 相关代码或文件将使用@文件语法临时引用。
> 
> \## 你的角色
> 
> 你是协调器代理
> 
> ![Image](https://pbs.twimg.com/media/Gu3tmNhXgAA21s1?format=jpg&name=large)

---

**海拉鲁编程客** @hylarucoder [2025-07-03](https://x.com/hylarucoder/status/1940608293640286329)

我一直用的是

\- ultrathink: 任务描述

\- thinkhard: 任务描述

我写的后端是go,一些简单的任务 claude code 会调 curl 命令拿 token, 紧接着发起接口测试.
