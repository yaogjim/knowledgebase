---
title: "2025-11-14_dotey_教你如何在_Codex_CLI_里面用_SKILLs_1_在你的项目目录下创建一个_clau"
source: "https://x.com/dotey/status/1989146187786494351"
author:
  - "[[@dotey]]"
published: 2025-11-14
created: 2025-11-14
description:
tags:
  - "x"
  - "@dotey"
  - "code"
  - "skill"
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

# 教你如何在 Codex CLI 里面用 SKILLs 1. 在你的项目目录下创建一个 “.clau

**宝玉** @dotey 2025-11-13

教你如何在 Codex CLI 里面用 SKILLs

1\. 在你的项目目录下创建一个 “.claude/skills”目录，如果你不想提交到 git 就把 .claude 加到 .gitignore

注：也可以是任意其他目录，放在“.claude/skills”目录下有个好处就是 claude code 默认能使用，不需要额外配置。

2\. 把你要用到 skill 复制到“.claude/skills”目录下（可以去 http://github.com/anthropics/skills… 这里找现成的）

3\. 如果你需要用到哪个 skill，只需要手动 @ 一下相应的 skill 文件即可，比如：

\> 请使用 @.claude/skills/artifacts-builder/SKILL.md ，创建一个 whiteboard 项目

也就是说只要你让 agent 去读取相应的 SKILL md 文件，就可以让 Agent 学会使用 SKILL。

这个方法不仅仅适用于 codex cli，也同样适用于 TRAE、Cursor、GitHub Copilot 这类 coding agent。

只能说 SKILL 的设计是想当超前的，而且跟 MCP 一样，并非 Claude Code 专属。

> 2025-11-13
> 
> 深度体验TRAE SOLO 正式版，总结一点技巧(附完整可重现提示词和源码)
> 
> 内容摘要：TRAE SOLO 模式评测，内含两个有价值的经验分享：
> 
> 1\. 如何借助 SubAgent 控制 MCP 工具上下文；
> 
> 2\. 在 TRAE SOLO 模式下一次性完成一个抓取网页内容生成 Markdown 的浏览器插件的提示词
> 
> 正文：🧵 x.com/Trae\_ai/status…
> 
> ![First image shows an orange-themed diagram titled Claude Code skills with icons for folder, tool, runtime, SKILL.md file, PDF, code brackets, gear, and .claude/skills/ path. Second image displays a clean whiteboard dashboard interface with tools like pen, eraser, line, rectangle, circle, text, brush size slider, color palette including black, red, orange, yellow, green, cyan, blue, purple, magenta, white, and buttons for download and clear canvas. Third image depicts a code artifacts test output in a terminal-like view with model details, agent instructions for using SKILL.md, status checks, review notes, and listed files like artifacts-builder, plan.md, index.ts, bundle.js. Fourth image illustrates a macOS development environment with open files in VS Code including artifacts-test, SKILL.md, builder.ts, showing code snippets for React components, artifact handling, and project structure with folders like src, node_modules.](https://pbs.twimg.com/media/G5rdbPxXQAAp843?format=jpg&name=large) ![First image shows an orange-themed diagram titled Claude Code skills with icons for folder, tool, runtime, SKILL.md file, PDF, code brackets, gear, and .claude/skills/ path. Second image displays a clean whiteboard dashboard interface with tools like pen, eraser, line, rectangle, circle, text, brush size slider, color palette including black, red, orange, yellow, green, cyan, blue, purple, magenta, white, and buttons for download and clear canvas. Third image depicts a code artifacts test output in a terminal-like view with model details, agent instructions for using SKILL.md, status checks, review notes, and listed files like artifacts-builder, plan.md, index.ts, bundle.js. Fourth image illustrates a macOS development environment with open files in VS Code including artifacts-test, SKILL.md, builder.ts, showing code snippets for React components, artifact handling, and project structure with folders like src, node_modules.](https://pbs.twimg.com/media/G5rdmVVWMAAerRy?format=jpg&name=large) ![First image shows an orange-themed diagram titled Claude Code skills with icons for folder, tool, runtime, SKILL.md file, PDF, code brackets, gear, and .claude/skills/ path. Second image displays a clean whiteboard dashboard interface with tools like pen, eraser, line, rectangle, circle, text, brush size slider, color palette including black, red, orange, yellow, green, cyan, blue, purple, magenta, white, and buttons for download and clear canvas. Third image depicts a code artifacts test output in a terminal-like view with model details, agent instructions for using SKILL.md, status checks, review notes, and listed files like artifacts-builder, plan.md, index.ts, bundle.js. Fourth image illustrates a macOS development environment with open files in VS Code including artifacts-test, SKILL.md, builder.ts, showing code snippets for React components, artifact handling, and project structure with folders like src, node_modules.](https://pbs.twimg.com/media/G5rdqpaWQAA-2sE?format=jpg&name=large) ![First image shows an orange-themed diagram titled Claude Code skills with icons for folder, tool, runtime, SKILL.md file, PDF, code brackets, gear, and .claude/skills/ path. Second image displays a clean whiteboard dashboard interface with tools like pen, eraser, line, rectangle, circle, text, brush size slider, color palette including black, red, orange, yellow, green, cyan, blue, purple, magenta, white, and buttons for download and clear canvas. Third image depicts a code artifacts test output in a terminal-like view with model details, agent instructions for using SKILL.md, status checks, review notes, and listed files like artifacts-builder, plan.md, index.ts, bundle.js. Fourth image illustrates a macOS development environment with open files in VS Code including artifacts-test, SKILL.md, builder.ts, showing code snippets for React components, artifact handling, and project structure with folders like src, node_modules.](https://pbs.twimg.com/media/G5rdtgkXoAAr7w-?format=jpg&name=large)

* * *

**魔都老猿** @Ari76184709 [2025-11-14](https://x.com/Ari76184709/status/1989154963524841670)

👍👍👍

* * *

**yan5xu** @yan5xu [2025-11-14](https://x.com/yan5xu/status/1989180407951290637)

skills 的设计真的非常精巧，特别是用 文件系统+markdown with yaml 元数据 + grep（搜索），对 agent/人都友好。这一套元数据替代完整信息+按需加载，可以用到很多地方

> 2025-11-14
> 
> claude skills 有个没怎么被看到的点，就是信息分层设计。首先用元信息替代完整信息，离当前任务距离越远，展示的细节越少。其次是按需加载，skills 基于 markdown+grep，就搭建出一套简单但非常有用的按需加载层。真的是非常优雅。
> 
> ![Image](https://pbs.twimg.com/media/G5r0o9EacAA0zB3?format=jpg&name=large)

* * *

**微风轻语** @endearqb [2025-11-14](https://x.com/endearqb/status/1989147475979141459)

好主意， 我试试用 Codex 来 使用 skill-creator 的 skill 完成以下任务

![Image](https://pbs.twimg.com/media/G5rfEiPbkAA7cXG?format=png&name=large)

* * *

**溪河** @l4walk6 [2025-11-14](https://x.com/l4walk6/status/1989161345598767581)

诶我理解，skills 更像是 Function Call ，无论是 cc 的主 Agent，还是 Sub Agent 都能调用？那 skills 和 mcp 的区别在哪？一个本地一个云端？

* * *

**Lyra** @HasManaFuture8 [2025-11-14](https://x.com/HasManaFuture8/status/1989164256441631037)

claude 的 skill 是由模型自动加载的，手动@其实就是提示词模版了，不够优雅啊

* * *

**Paul** @nori\_tsukiji [2025-11-14](https://x.com/nori_tsukiji/status/1989191419450519982)

浅显易懂的文字，读起来很舒服

* * *

**面条** @miantiao\_me [2025-11-14](https://x.com/miantiao_me/status/1989173574515716411)

和 SpecKit 和 OpenSpec 用法一样