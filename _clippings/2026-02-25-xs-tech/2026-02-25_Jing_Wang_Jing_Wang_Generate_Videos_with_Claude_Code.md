---
title: "2026-02-25_Jing_Wang_Jing_Wang_Generate_Videos_with_Claude_Code"
source: "https://x.com/jingwangtalk/status/2016513231251210610"
author:
  - "[[@Jing Wang]]"
published: 2026-02-25
created: 2026-02-25
description:
tags:
  - "x"
  - "@Jing Wang"
  - "remotion"
  - "code"
---

# Jing Wang # Generate Videos with Claude Code

**Jing Wang**

# Generate Videos with Claude Code: A Practical Remotion Guide 使用 Claude Code 生成视频：实用移除指南

Article is from

[my newsletter](https://zerofuturetech.substack.com/p/generate-videos-with-claude-code)

. Claude Code writes code. Can it generate videos? With Remotion, yes.

文章来自

[我的简讯](https://zerofuturetech.substack.com/p/generate-videos-with-claude-code)

。 克劳德·科德会编写代码。代码能生成视频吗？有了 Remotion，答案是肯定的。

[Youtube Video (if you are a video learner)

YouTube 视频（如果您是视频学习者）](https:// https://youtu.be/19ALwZPZhuQ)

Remotion is a frontend framework built on a simple idea: video as code. It renders web pages frame by frame, then stitches those frames into video. This means you can build videos using React components and control every frame with code. This isn’t a universal solution. Remotion produces videos that feel more like animated presentations—ideal for data visualizations, mathematical concept explanations, and UI demonstrations. It’s not built for traditional editing or special effects. But for technical content creators, that’s exactly the point: reproducible, customizable, and programmable.

Remotion 是一个基于简单理念的前端框架：视频即代码。它逐帧渲染网页，然后将这些帧拼接成视频。这意味着你可以使用 React 组件构建视频，并通过代码控制每一帧。 这并非万能解决方案。Remotion 制作的视频更像是动画演示，非常适合数据可视化、数学概念讲解和用户界面演示。它并非为传统剪辑或特效而设计。但对于技术内容创作者而言，这恰恰是它的优势所在：可复现、可定制且可编程。

[

![Image](https://pbs.twimg.com/media/G_wWuTuakAAOHme?format=jpg&name=medium)


](/jingwangtalk/article/2016513231251210610/media/2016511717979885568)

## 

Part 1: Installation and Setup

第一部分：安装和设置

Installing Remotion Agent Skills

安装 Remotion Agent 技能

Remotion now supports

[AI agent skills](https://www.remotion.dev/docs/ai/skills)

. Prerequisites:

[Node.js](https://nodejs.org/en/download/)

installed on your system, and run npx installation.

Remotion 现在支持

[人工智能代理技能](https://www.remotion.dev/docs/ai/skills)

先决条件：

[Node.js](https://nodejs.org/en/download/)

已安装在您的系统上，并运行 npx 安装程序。

Run this in your terminal:

在终端中运行以下命令：

npx skills add remotion-dev/skills

npx skills 添加 remotion-dev/skills

Testing with Official Examples

使用官方示例进行测试

After installation, test with official examples. If you don’t have Bun, install it first:

安装完成后，请使用官方示例进行测试。如果您尚未安装 Bun，请先安装它：

plaintext

纯文本

```plaintext
# macOS/Linux
curl -fsSL https://bun.sh/install | bash

# Or visit https://bun.com/docs/installation
```

Create a test video:

制作测试视频：

bun create video

bun 创建视频

This displays a list of official examples. Select one to preview and verify your environment is configured correctly.

这里会显示官方示例列表。选择一个示例进行预览，并验证您的环境配置是否正确。

## 

Part 2: Planning Video Content

第二部分：视频内容规划

Creating Your Project Structure

创建项目结构

Before generating videos with Claude Code, plan the structure. Create a project folder:

在使用 Claude Code 生成视频之前，请先规划好结构。创建一个项目文件夹：

plaintext

纯文本

```plaintext
mkdir my-video
cd my-video
```

Writing an Effective Planning Prompt

撰写有效的规划提示

Enable Claude Code’s plan mode and input a detailed requirements prompt. This is the critical step—good planning directly determines the final output.

启用 Claude Code 的规划模式，并输入详细的需求提示。这是关键步骤——良好的规划直接决定最终的输出结果。

For a Claude Code introduction video, your prompt should include:

制作 Claude Code 介绍视频时，您的提示信息应包含以下内容：

- Video Goal: Help developers understand what Claude Code is in 60 seconds
 
 视频目标 ：帮助开发者在 60 秒内理解 Claude Code 是什么
 
- Target Audience: Developers with programming experience but no Claude Code experience
 
 目标受众 ：有编程经验但没有 Claude Code 经验的开发者
 
- Duration Specs: 60 seconds (30fps = 1800 frames)
 
 时长规格 ：60 秒（30fps = 1800 帧）
 
- Available Assets: Logo, simple graphics, and text animations
 
 可用素材 ：Logo、简单图形和文字动画
 
- Style Preferences: Clean modern, dark background, high contrast
 
 风格偏好 ：简洁现代，深色背景，高对比度
 

Request Claude to provide:

请克劳德提供：

1.  Storyboard script (content, duration, visual elements for each scene)
 
 分镜头脚本（每个场景的内容、时长、视觉元素）
 
2.  Copy (voiceover or subtitles)
 
 文案（旁白或字幕）
 
3.  Technical implementation hints (Remotion components and animation effects needed)
 
 技术实现提示（需要移除组件和动画效果）
 

Prompt Example:

提示示例：

plaintext

纯文本

```plaintext
I want to create a tutorial video introducing Claude Code. Please help me plan the content:

**Video Objectives**:

- Help developers who know nothing about Claude Code understand what it is and what it can do within 60 seconds

- Inspire them to think “I want to try this”

**Target Audience**:

- Developers with basic programming experience

- May have heard about AI-assisted programming but haven’t used Claude Code

**Video Duration**: 60 seconds (30fps = 1800 frames)

**Available Assets**:

- @claudecode.png (Claude Code logo/screenshot)

- Can generate simple graphics and text animations

- Do not use live-action footage

**Style Preferences**:

- Clean and modern, similar to Apple keynote style

- Color scheme: dark background + bright text (high contrast)

- Fast-paced animations, high information density

Please provide:

1. Storyboard script (content, duration, and visual elements for each scene)

2. Copy (voiceover or subtitle text)

3. Technical implementation hints (which Remotion components and animation effects are needed)
```

Reviewing the Initial Plan

审查初始计划

Review the plan before proceeding to the next phase. Make sure the pacing makes sense and the technical approach is feasible.

在进入下一阶段之前，请仔细审查计划。确保进度安排合理，技术方案切实可行。

## 

Part 3: Technical Requirements Document

第三部分：技术要求文档

Converting Storyboard to Technical Specs

将故事板转换为技术规格

Have Claude convert the storyboard into a technical document:

请克劳德将故事板转换成技术文档：

plaintext

纯文本

```plaintext
Great! Now convert this storyboard into a Remotion project 
technical requirements document, saved as video_prompt.md. Include:

1. Project Structure: Which React components to create
2. Timeline Planning: Start frame and duration for each scene
3. Animation Specs: Entry/exit animations, easing functions for each element
4. Asset Checklist: Images, fonts, color variables
5. Copy Text: All text to display (for easy modification)

Format requirements:
- Use Markdown tables for timeline
- Use code blocks for key animation logic examples
- Extract all hardcoded values (colors, sizes, copy) as constants
```

Understanding the Technical Document

理解技术文档

This step transforms creativity into executable technical specifications. Claude generates detailed documentation with frame counts, component structure, and animation parameters.

这一步骤将创意转化为可执行的技术规范。克劳德生成了包含帧数、组件结构和动画参数的详细文档。

The document serves as a blueprint that eliminates ambiguity in the implementation phase.

该文件作为蓝图，可以消除实施阶段的歧义。

## 

Part 4: Generating the Video Project

第四部分：生成视频项目

Implementing with Claude Code

使用 Claude Code 实现

With the technical document ready, have Claude Code implement it:

技术文档准备就绪后，请 Claude Code 执行它：

plaintext

纯文本

```plaintext
Create this video project using Remotion based on @video_prompt.md.
Tell me how to preview it when you're done.
```

What Claude Code Does

克劳德·科德做什么

Claude will:

克劳德将：

1.  Create the Remotion project structure
 
 创建 Remotion 项目结构
 
2.  Write React components
 
 编写 React 组件
 
3.  Configure timeline and animations
 
 配置时间轴和动画
 
4.  Set up preview and render commands
 
 设置预览和渲染命令
 

Previewing Your Video

视频预览

Preview typically uses:

预览通常使用：

plaintext

纯文本

```plaintext
npm run dev
# or
bun run dev
```

Your browser opens Remotion Studio, where you can view the video in real-time, adjust the timeline, and modify parameters.

您的浏览器将打开 Remotion Studio，您可以在其中实时查看视频、调整时间线和修改参数。

## 

The Real-World Difference

现实世界的差异

Traditional Video Production

传统视频制作

Traditional workflows involve:

传统工作流程包括：

- Opening video editing software
 
 打开视频编辑软件
 
- Manually adjusting timelines
 
 手动调整时间线
 
- Re-exporting after every change
 
 每次更改后重新导出
 
- Difficulty generating similar videos at scale
 
 大规模生成类似视频的难度
 

With Claude Code + Remotion

使用 Claude Code + 移除

The code-based approach provides:

基于代码的方法具有以下优势：

- Code defines video structure
 
 代码定义了视频结构
 
- Modifying code modifies the video
 
 修改代码会修改视频。
 
- Parameterized batch generation
 
 参数化批处理生成
 
- Version control and reusability become simple
 
 版本控制和可重用性变得简单
 

Ideal Use Cases

理想应用案例

- Data Visualization Videos: Use D3.js or Recharts to dynamically display data
 
 数据可视化视频 ：使用 D3.js 或 Recharts 动态显示数据
 
- Mathematical Concept Explanations: Use Manim.js or custom animations to demonstrate formulas
 
 数学概念讲解 ：使用 Manim.js 或自定义动画来演示公式。
 
- Product Feature Demonstrations: Use actual UI components to showcase interaction flows
 
 产品功能演示 ：使用实际的 UI 组件来展示交互流程
 
- Tutorial Videos: Code highlighting, terminal recordings, step-by-step walkthroughs
 
 教程视频 ：代码高亮显示、终端录制、分步讲解
 

## 

What’s Next

接下来会发生什么？

Understanding the Limitations

了解局限性

Remotion’s limitations are obvious—it’s not a replacement for Final Cut Pro or Premiere. But for scenarios requiring programmatic generation, batch production, or precise timeline control, it offers unique value.

Remotion 的局限性显而易见——它无法替代 Final Cut Pro 或 Premiere。但对于需要程序化生成、批量制作或精确时间线控制的场景，它却能提供独特的价值。

How Claude Code Changes the Game

克劳德·科德如何改变游戏

Claude Code lowers the barrier to entry. You don’t need to deeply learn the Remotion API—just describe the effects you want and let AI handle the implementation.

Claude Code 降低了入门门槛。您无需深入学习 Remotion API，只需描述您想要的效果，剩下的实现工作就交给 AI 来完成。

Getting Started

入门

Try making your next technical demonstration video with it. Start with simple scenes and gradually explore more complex animations and interactions. The video-as-code approach might change how you think about content creation.

不妨尝试用它制作你的下一个技术演示视频。从简单的场景入手，逐步探索更复杂的动画和交互。这种视频即代码的方法或许会改变你对内容创作的固有思维。

Reference Resources:

参考资料：

- Node.js:
 
 [https://nodejs.org/en/download/](https://nodejs.org/en/download/)
 
 Node.js：
 
 [https://nodejs.org/en/download/](https://nodejs.org/en/download/)
 
- Bun:
 
 [https://bun.com/docs/installation](https://bun.com/docs/installation)
 
 包子：
 
 [https://bun.com/docs/installation](https://bun.com/docs/installation)
 
- Remotion AI Skills:
 
 [https://www.remotion.dev/docs/ai/skills](https://www.remotion.dev/docs/ai/skills)
 
 Remotion AI 技能：
 
 [https://www.remotion.dev/docs/ai/skills](https://www.remotion.dev/docs/ai/skills)
 
- Remotion + Claude Code:
 
 [https://www.remotion.dev/docs/ai/claude-code](https://www.remotion.dev/docs/ai/claude-code)
 
 Remotion + Claude Code：
 
 [https://www.remotion.dev/docs/ai/claude-code](https://www.remotion.dev/docs/ai/claude-code)