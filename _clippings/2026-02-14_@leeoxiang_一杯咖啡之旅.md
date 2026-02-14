---
title: "一杯咖啡之旅"
source: "https://x.com/leeoxiang/status/2022318491249123404"
author:
  - "[[@leeoxiang]]"
date: "2026-02-14T15:51:06+08:00"
created: 2026-02-14
description:
tags:
  - "@leeoxiang # Remotion # Excalidraw # Claude code"
---
**Leo Xiang** @leeoxiang [2026-02-13](https://x.com/leeoxiang/status/2022318491249123404)

一杯咖啡之旅。 by Claude code + Remotion + Excalidraw

Excalidraw + Remoiton 用来教育以及数据可视化类视频效果太好了。

---

**熊布朗（deeptoai.com)** @Stephen4171127 [2026-02-13](https://x.com/Stephen4171127/status/2022322914037477630)

看起来太棒了

---

**Jing Wang** @jingwangtalk [2026-02-14](https://x.com/jingwangtalk/status/2022492137817059781)

我之前写了一个教程如何用claude code结合remotion skills制作视频：

> 2026-01-28
> 
> ![Article cover image](https://pbs.twimg.com/media/G_wW7GzbQAAMEb_?format=jpg&name=large)



### 如何通过 by Claude code + Remotion + Excalidraw 来实现的
从帖子内容和相关搜索中收集到的信息，Leo Xiang (@leeoxiang) 这条帖子展示的是一个名为"一杯咖啡之旅"的 1 分 31 秒教育/数据可视化动画视频，使用的工具链是 **Claude Code + Remotion + Excalidraw**。以下是这三者如何协作实现的：

---

**整体流程（Pipeline）**

这个工作流的核心思路是：让 Claude Code 充当"导演+编剧+程序员"，用自然语言提示它生成 Remotion 的 React 代码，而视觉风格则借助 Excalidraw 的手绘白板美学。

**1. Excalidraw — 视觉风格与素材**

Excalidraw 是一个开源的虚拟白板工具，特色是手绘风格的图形（sketchy / hand-drawn style）。从视频截图可以看到，整个视频有奶油色背景、手绘风格的文字和插图、波浪下划线等——这些都是 Excalidraw 的标志性视觉风格。

在这个流程中，Excalidraw 的角色可以是：直接在 Excalidraw 中绘制图表/场景，然后导出为 SVG 或 `.excalidraw` 文件供 Remotion 使用；或者（更可能的方式）让 Claude Code 在 Remotion 组件中直接使用 Excalidraw 的 React 组件库 (`@excalidraw/excalidraw`)，以编程方式渲染手绘风格的图形元素。社区中还有 `excalidraw-animate` 这样的工具，可以将 Excalidraw 的绘图转化为逐笔绘制的动画效果。

**2. Remotion — 编程式视频生成框架**

Remotion 是一个基于 React 的视频创作框架，核心理念是"用写 React 组件的方式写视频"。每一帧视频本质上就是一个 React 组件的渲染输出。Remotion 提供了时间轴控制、帧插值（interpolate）、序列编排（Sequence）等API，让你可以精确控制动画的每一帧。

Remotion 官方文档已经专门为 Claude Code 提供了集成指南，包括安装 Skills 文件（让 Claude 理解 Remotion 的 API 规则）、Markdown 格式的文档（方便 AI agent 直接读取）等。

**3. Claude Code — AI 编排与代码生成**

Claude Code 是整个工作流的"大脑"。用户在终端中用自然语言向 Claude 描述想要的视频内容，比如"做一个关于咖啡从种植到品饮的可视化视频，使用手绘风格"，然后 Claude Code 会：

- 自动生成 Remotion 项目的 React 组件代码
- 编排每个场景的时间线和过渡动画
- 使用 Excalidraw 风格的元素来呈现数据和图表
- 实时预览，用户可以通过反复对话（ping-pong）来迭代调整效果

**典型工作流步骤：**

1. 用 `npx create-video@latest` 创建 Remotion 项目，选择 Blank 模板 + TailwindCSS + 安装 AI Skills
2. 在一个终端运行 `npm run dev` 启动 Remotion 实时预览
3. 在另一个终端启动 `claude`，开始用自然语言描述你想要的视频
4. Claude Code 读取 Remotion 的 Skills 文件，理解框架规则，然后生成/修改 React 组件代码
5. Remotion 实时预览窗口会即时反映代码变化
6. 最终用 Remotion 的渲染命令导出为 MP4 视频

---

**为什么这个组合特别适合教育和数据可视化？**

正如 Leo Xiang 在帖子中所说的，Excalidraw 的手绘风格天然给人一种"课堂白板"的亲切感，非常适合解释概念和展示数据。而 Remotion 的编程式控制让复杂的动画时序精确可控。Claude Code 则大幅降低了门槛——你不需要精通 React 或动画编程，只需要用自然语言描述你想要的效果就行。这三者的组合让一个人就能快速产出制作精良的教育类视频。


### 能否让 claude code 直接 使用 Excalidraw 的 cli 或则 mcpserver 来自动化控制 Excalidraw 的执行，这样 使用自然语言等 就可以控制 Excalidraw 了 ？

目前有多种方式让 Claude Code 通过 MCP Server 或 CLI 来自动化控制 Excalidraw：

---

## 1. 官方 Excalidraw MCP（Excalidraw + Anthropic 联合出品）

这是最新的消息（就在几天前）——Excalidraw 官方与 Anthropic 合作发布了一个官方 MCP。你可以在 Claude AI 中搜索 "Excalidraw" 来启用它。

这个官方 MCP 的特点是"一句话生成图"的模式：你用自然语言描述，它直接在 Claude 聊天界面中渲染出 Excalidraw 图表。属于**无状态、一次性生成**的方式，适合快速出图。

---

## 2. 社区版 MCP Server（yctimlin/mcp_excalidraw）——功能更强大

这是目前功能最完整的方案，提供了 **26 个 MCP 工具**，可以实现完整的编程式控制：

**架构：** 它包含两个进程——一个 Canvas Server（Web UI + REST API + WebSocket），和一个 MCP Server（通过 stdio 与 Claude Code 通信）。Canvas Server 会在浏览器中打开一个实时的 Excalidraw 画布，AI 的每一步操作都能实时看到。

**核心能力包括：**

- 元素 CRUD：`create_element`、`get_element`、`update_element`、`delete_element`、`batch_create_elements`
- 布局工具：`align_elements`、`distribute_elements`、`group/ungroup`
- 场景感知：`describe_scene`（AI 能"看到"画布上有什么）、`get_canvas_screenshot`（截图反馈）
- 文件 I/O：`export_scene`、`import_scene`、`export_to_image`
- Mermaid 转换：`create_from_mermaid`
- 快照与回滚：`snapshot_scene`、`restore_snapshot`
- 可分享链接：`export_to_excalidraw_url`

**与官方 MCP 的关键区别：** 官方 MCP 是"提示词进、图表出"的一次性生成。而社区版实现了一个**闭环反馈循环**——AI 可以画完之后"看一看"自己画的效果（通过 `describe_scene` 和 `get_canvas_screenshot`），然后逐步迭代改进，就像一个人类设计师那样。

**在 Claude Code 中配置非常简单：**

bash

```bash
claude mcp add excalidraw --scope user \\
  -e EXPRESS_SERVER_URL=http://localhost:3000 \\
  -e ENABLE_CANVAS_SYNC=true \\
  -- node /path/to/mcp_excalidraw/dist/index.js
```

配置完成后，你就可以在 Claude Code 中用自然语言说"帮我画一个微服务架构图"或者"把这个流程图导出为 PNG"，Claude 会自动调用对应的 MCP 工具。

---

## 3. Excalidraw CLI（`excalidraw-cli`）

刚刚发布的新 CLI 工具，可以通过 `npx excalidraw-cli` 来使用，支持从 JSON 创建图表、从文件导入等。Claude Code 可以直接在终端调用它来生成 `.excalidraw` 文件或导出图片，不需要浏览器。

---

## 完整的自然语言 → Excalidraw 动画视频流水线

结合你之前看到的帖子，一个理想的全自动化流程可以是：

1. **Claude Code + Excalidraw MCP** → 用自然语言生成 Excalidraw 图表/场景（AI 可以实时看到画布并迭代）
2. **导出 `.excalidraw` JSON 文件** → 通过 MCP 的 `export_scene` 工具
3. **Remotion 读取 Excalidraw 数据** → 在 React 组件中渲染并添加动画时序（逐元素出现、镜头移动等）
4. **Remotion 渲染为视频** → 输出最终的 MP4

整个过程中，用户只需要用自然语言描述想要的内容和风格，Claude Code 作为"全栈编排者"来协调 Excalidraw MCP 和 Remotion 的代码生成。

这个领域正在快速发展——官方 MCP 才刚发布几天，社区工具也在不断迭代。用自然语言控制 Excalidraw 已经不是"可不可以"的问题，而是"选哪个方案"的问题了。