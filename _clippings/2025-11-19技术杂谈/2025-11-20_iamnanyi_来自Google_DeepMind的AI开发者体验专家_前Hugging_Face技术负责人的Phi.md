---
title: "2025-11-20_iamnanyi_来自Google_DeepMind的AI开发者体验专家_前Hugging_Face技术负责人的Phi"
source: "https://x.com/iamnanyi/status/1991153807074734170"
author:
  - "[[@iamnanyi]]"
published: 2025-11-20
created: 2025-11-20
description:
tags:
  - "x"
  - "@iamnanyi"
  - "2025-11-19"
  - "xml"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-12-10"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---

# 来自Google DeepMind的AI开发者体验专家，前Hugging Face技术负责人的Phi

**NanYi** @iamnanyi 2025-11-19

来自Google DeepMind的AI开发者体验专家，前Hugging Face技术负责人的Philipp Schmid分享的Gemini 3 Pro提示通用使用最佳实践。以下是他认为提升Gemini 3 Pro性能的提示词建议：

Gemini 3 更倾向于直接性而非说服力，更注重逻辑而非冗长。核心原则包括：

1）精确指令：在输入提示中保持简洁。Gemini 3 对直接、清晰的指令反应最佳。明确陈述你的目标，避免冗余。

2）一致性及定义参数：在整个提示中保持统一的结构（例如，标准化的 XML 标签），并明确定义模糊的术语。

3）输出冗长性：默认情况下，Gemini 3 较少冗长，倾向于提供直接、高效的答案。如果你需要更对话式或"健谈"的角色，你必须明确要求它。

4）多模态连贯性：文本、图像、音频或视频都应被视为同等类别的输入。指令应明确引用特定模态，以确保模型跨模态综合而非孤立分析。

5）约束位置：将行为约束和角色定义放在系统指令中或提示的最顶部，以确保它们锚定模型的推理过程。

6）长上下文结构：在处理大型上下文（书籍、代码库、长视频）时，将你的具体指令放在提示的末尾（数据上下文之后）。

7）上下文锚定：当从大块数据过渡到你的查询时，明确地连接两者。在问题前使用类似“基于以上信息…”的框架短语。

> 2025-11-19
> 
> 我使用 Gemini 3 Pro 已有一段时间，以下是我总结的通用最佳实践。包含目前对我最有效的原则和架构模式。
> 
> 这并非要奉为金科玉律，而是作为助你精进的起点
> 
> ![Image](https://pbs.twimg.com/media/G6HrzKUWUAEYdAX?format=jpg&name=large)

* * *

**NanYi** @iamnanyi [2025-11-19](https://x.com/iamnanyi/status/1991156750293287224)

在推理与规划阶段，可以让Gemini 3将目标分解为子任务，并检查信息是否完整；使用TODO列表来追踪任务进度；在输出结果之前进行自我批评与检查，确保输出符合用户意图和预期。

使用 XML 风格的标签或 Markdown 来结构化Prompt，提供了明确的边界，帮助模型区分指令和数据。不要混合 XML 或