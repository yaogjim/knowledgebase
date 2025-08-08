---
title: "如何在半天内完成两天需求"
source: "https://x.com/xiaokedada/status/1953120436063223956"
author:
  - "[[@xiaokedada]]"
created: 2025-08-07
description:
tags:
  - "@xiaokedada #AI #编程 #自动化 #效率 #前端开发"
---
**nazha** @xiaokedada [2025-08-06](https://x.com/xiaokedada/status/1953120436063223956)

#分享 新鲜的 AI Coding 案例：我是如何用半天写完了两天的需求

这两天去支持一个 B 端需求(所谓的 B 端需求，主要以列表、表单的构成的 CRUD 页面)。排期两天，昨天忙别的事情去了，今天下午才开始动手。

这一次，我没有仓皇出手。我在项目根目录创建了一个 requirements/task-2025-08-06，计划分两次任务来执行，分别是 table (列表) 和 edit (新建和编辑)。

重点来了，在每个任务中(以 table 举例)，我详细梳理了：

\- 任务需求：是要干一件什么事情

\- 列举每个列表项：包括取接口什么字段，如何展示，以及其他要求

\- 列出这个页面所需的接口：接口名，入参和返回

然后，我让 Cursor Follow 我的这个文档来进行实现。

\> 任务需求 @table.md，请参考 @index.tsx ，实现 List 页面

最后的实现效果确实非常好，没有功能缺失的问题存在。在这种 CURD 的场景下，需求和功能都非常明确，AI 确实很好发挥(我们内部也在做类似的事情)。在 C 端场景下，需求和功能会相对更难表述清楚，也不能渴望 AI 能理解你。

![Image](https://pbs.twimg.com/media/GxrdHXQawAUzAbw?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/GxrfIyrawAAIFZG?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/GxrfNNIbIAAreHs?format=jpg&name=large)

---

**William Zhang** @WZDBM [2025-08-07](https://x.com/WZDBM/status/1953277734651871530)

学到了，一个连续的任务需求用一个带有时间戳的文件夹来表示，里面存放实现该需求需要的文档（需求文档、架构设计文档等）