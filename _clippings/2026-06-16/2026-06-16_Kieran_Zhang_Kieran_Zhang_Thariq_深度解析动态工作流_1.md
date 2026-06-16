---
title: "2026-06-16_ninthbit_ai_Kieran_Zhang_Thariq_深度解析动态工作流_1"
source: "https://x.com/ninthbit_ai/status/2061933937426039290"
author:
  - "[[@ninthbit_ai]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "x"
  - "@ninthbit_ai"
  - "\-"
  - "claude"
---

# Kieran Zhang: Thariq 深度解析动态工作流： 1

**Kieran Zhang**

Thariq 深度解析动态工作流：

1\. dynamic workflows 是什么？

Claude Code 不只是“自己干活”，而是能为当前任务写一个专用工作流：

\- 生成 JS workflow 文件

\- 调用特殊函数创建 / 协调 subagents

\- 每个 subagent 有独立上下文

\- 可以选择不同模型

\- 可以决定是否用独立 worktree

\- 中断后可以 resume 继续跑

2\. 解决的问题

单一 agent 在复杂长任务里容易出三类问题：

\- agentic laziness：做到一半就宣布完成，比如安全审查 50 项只做了 35 项

\- self-preferential bias：验证自己产物时偏向相信自己

\- goal drift：长上下文、多轮压缩后，原始目标和限制慢慢丢失

workflow 的作用是把规划、执行、验证、合并拆成结构化流程，用多个隔离上下文降低这些问题。

3\. 触发方式

可以直接让 Claude “use a workflow”，也可以用触发词“ultracode”

4\. 常见 workflow 模式

\- Classify-and-act

先分类，再把任务路由给不同 agent 或流程。

\- Fan-out-and-synthesize

拆成很多小任务并行执行，最后统一合成。适合大量相似子任务。

\- Adversarial verification

每个产出再派一个独立 agent 按 rubric 反向验证。

\- Generate-and-filter

先生成很多方案，再去重、打分、过滤。

\- Tournament

多个 agents 用不同方法竞争，同题作答，再两两比较选赢家。

\- Loop until done

不预设轮数，而是循环直到没有新发现、没有错误、满足停止条件。

5\. 适合场景

\- 大规模 migration / refactor

例如 Bun 从 Zig 重写到 Rust，据说就用了 workflows。

\- deep research

并行搜索、抓来源、验证 claims、合成带引用报告。

\- deep verification

把报告里的 factual claims 全部拆出来，每个 claim 单独验证。

\- sorting / ranking

比如 1000 条支持工单按严重程度排序；用 pairwise comparison 或 tournament 比单次全量评分更可靠。

\- memory / rule mining

从历史 session 或 code review 里挖反复出现的纠正，提炼成 CLAUDE.md 规则。

\- root-cause investigation

让不同 agents 基于日志、文件、数据分别提出假设，再由验证者和反驳者检验。

\- triage at scale

批量处理支持队列、bug 报告、待办 backlog。文章特别提到 quarantine：读不可信公开内容的 agent 不应该有高权限动作。

\- design / naming / taste-based exploration

适合发散多个方案，再按审美或 rubric 评审。

\- evals

用 workflow 评估某个 skill、prompt、模型输出质量。

\- model routing

先让 classifier agent 判断任务复杂度，再决定用 Sonnet 还是 Opus。

适合高价值、复杂、长链条、需要并行或强验证的任务。

6\. 实用技巧

\- prompt 要具体，最好说明 workflow 类型，比如 adversarial review、tournament、fan-out-and-synthesize

\- 可以要求 quick workflow，用于小范围快速验证

\- 和 /goal、/loop 配合：/goal 设硬完成条件，/loop 做持续 triage / research / verification

\- 可以指定 token budget，比如 “use 10k tokens”

\- workflow 可以按 s 保存，路径在 \`~/.claude/workflows\`

\- 也可以把 workflow JS 文件放进 skill 里分发

> **@trq212**
> 
> Thariq @trq212 · Jun 2 文章 适用于所有任务的框架：Claude Code 中的动态工作流 上周，我们在 Claude Code 中发布了动态工作流。Claude 现在可以实时编写自己的工作流框架，为手头的任务定制。 虽然默认的 Claude 代码框架是为编码而构建的,... Thariq @trq212 · Jun 2 文章 适用于所有任务的框架：Claude Code 中的动态工作流 上周，我们在 Claude Code 中发布了动态工作流。Claude 现在可以实时编写自己的工作流框架，为手头的任务定制。 虽然默认的 Claude 代码框架是为编码而构建的,...

![引用图片](https://pbs.twimg.com/media/HJ0q6o6aYAEM_ej?format=jpg&name=large)

* * *

### 热门回复

**@Phoenix Yin** ♥ 750 · 💬 52

今天来看腾讯的开发工程师的初面题。

Q1 - Q9, Q12我感觉这是整张卷子最值钱的部分。面试官非常懂行，他关注的是大模型在实际业务中的控制流和记忆管理。

先说Q1, Q2, Q5。

大模型的 Token 是要算钱且有长度限制的。怎么存用户的聊天记录？

**@响马** ♥ 178 · 💬 33

以前当一个人说，我有一个点子，只缺一个程序员。其实他缺的是：

需求经理，产品经理，设计师，架构师，前端工程师，后端工程师，数据库工程师，测试工程师，运维工程师，运营经理，内容编辑，美工，客服，和前台小妹。

现在 ai 来了，这些都有了，你会发现，其实他真正缺的是点子。

**@Jianshuo Wang** ♥ 118 · 💬 49

Claude Code 50 万行，本质是两层 while(true) 循环，加读写查三个工具。就这简单的 56 行，是大多数 Coding Agent 的骨架。