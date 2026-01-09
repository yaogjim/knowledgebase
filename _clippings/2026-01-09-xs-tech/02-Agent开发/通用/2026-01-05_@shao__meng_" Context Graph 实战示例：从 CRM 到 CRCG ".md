---
title: "\" Context Graph 实战示例：从 CRM 到 CRCG \""
source: "https://x.com/shao__meng/status/2006169366916915531"
author:
  - "[[@shao__meng]]"
date: "2026-01-05T15:34:02+08:00"
created: 2026-01-05
description:
tags:
  - "@shao__meng # AI # Context Graph # CRM # CRCG # Agentic AI"
---
**meng shao** @shao\_\_meng 2025-12-30

Context Graph 实战示例：从 CRM 到 CRCG

@ishan\_chhabra 这篇文章是对「AI’s trillion-dollar opportunity: Context graphs」提出「Context Graph」的进一步阐释和实用化说明。

核心观点是：传统的 CRM 系统是“记录系统”，只存储静态数据和最终状态；而新兴的 Agentic AI 需要一种全新的“上下文图”，它不仅是记录数据，更是记录决策过程、推理逻辑和动态上下文，从而变成“推理系统”。

为什么“Context Graph”容易被误解？

· “Graph”一词容易让人联想到图数据库或知识图谱，但作者强调：Context Graphs 与这些技术无关。

· 它本质上是两种思路的结合：

1\. 上下文工程：为 AI 模型提供精确、相关的任务信息，避免幻觉或遗忘。

2\. 决策图：AI Agent 在执行任务时动态构建的图结构，记录它收集了哪些上下文、为什么做出某个决策。

文章用一个销售场景的实用例子来说明差异

作者以销售团队的 POC 失败问题为例，对比三种方法：

1\. 传统 CRM 方式：

· 在 CRM 中新增字段（如 POC 开始/结束日期、成功标准）。

· 销售人员填写，但“成功标准”往往简陋（如“需要邮件集成”）。

· 结果：领导无法深入了解真正的成功定义、关键人物或与组织目标的匹配。

2\. 朴素 AI 方式：

· 用 AI 自动从会议录音中提取总结，填充或更新 CRM 字段。

· 问题：多次更新会导致上下文丢失，只剩最终状态，没有决策痕迹（为什么这个标准被优先？）。

3\. Context Graph 方式（推荐的新架构）：

· 以销售一家新一代 CRM 给客户 “Dunder Mifflin” 为例，涉及两场会议：

· 第一场：与普通员工 Jim 聊天，他抱怨“每周花5小时找线索”和“CRM 更新太慢”。

· 第二场：与经理 Michael 聊天，他强调“为 IPO 准备，需要将预测准确率从73%提升到90%”。

· 系统不只是简单记录痛点，而是动态构建图结构：

· 先有基础节点：自家产品的核心能力（擅长预测和管道可见性，不擅长线索生成）。

· 与 Jim 的痛点匹配：线索生成不匹配（标记为无法解决）；CRM 更新匹配，并拉取类似客户案例。

· 与 Michael 的痛点匹配：预测准确率高度匹配，创建“成功指标”节点（从73%到90%），并因 Michael 是决策者而优先级更高。

· 结果：询问“成功定义是什么？”时，Context Graph 能给出层次化、带理由的答案：

· 首要：决策者 Michael 的预测需求，与公司 IPO 目标对齐，且匹配产品核心能力。

· 次要：员工 Jim 的 CRM 更新需求（影响力较低）。

· 不相关：Jim 的线索生成需求（产品不支持）。

为什么这很重要？未来的潜力

· 传统 CRM 只存储“什么”（最终事实），Context Graph 存储“为什么”（决策痕迹、来源权重、优先级逻辑）。

· 当积累成千上万笔交易的 Context Graph 后，AI 能分析图结构，发现人类忽略的模式，例如：“当经理提到 IPO 时，早引入预测功能可使成交速度提升40%”。

· 这标志着从被动记录数据，向主动数字化业务逻辑的转变。Agentic AI 系统将以此为基础，构建更智能、可解释的决策流程。

> 2025-12-30
> 
> ![Image](https://pbs.twimg.com/media/G9dYY_PaYAEVSxd?format=jpg&name=large) ![Article cover image](https://pbs.twimg.com/media/G9cO1DTXoAAS5tV?format=jpg&name=large)

---

**S Li** @YanyuRensheng [2026-01-02](https://x.com/YanyuRensheng/status/2006911618404462903)

原文的整体思路似乎跟AI没什么关系，只是试图借助AI实现增强型的传统CRM？

---

**ElevenLabs** @elevenlabsio

See why over 1 million creators use ElevenLabs for voiceovers, instant translations, and more to grow their following. Try for free today.