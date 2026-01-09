---
title: "2026-01-09_dotey_朋友负责的团队面临的是一个真实的企业痛点_公司有完整的内部设计系统_Design_System_和私"
source: "https://x.com/dotey/status/2002230457530765621"
author:
  - "[[@dotey]]"
published: 2026-01-09
created: 2026-01-09
description:
tags:
  - "x"
  - "@dotey"
  - "https"
  - "agent"
---

# 朋友负责的团队面临的是一个真实的企业痛点：公司有完整的内部设计系统（Design System）和私

**宝玉** @dotey [2025-12-20](https://x.com/dotey/status/2002229821997478209)

朋友负责的团队面临的是一个真实的企业痛点：公司有完整的内部设计系统（Design System）和私有前端框架，但这些代码从未被 AI 训练过，通用模型根本无法直接生成符合规范的代码。

目标看起来很清晰——做一个类似 Lovable 的工具，但用的是自己的 Design System。用户上传 Figma 设计稿或截图，Agent

![Image](https://pbs.twimg.com/media/G8lZSBFWYAEvOJP?format=jpg&name=large)

* * *

**宝玉** @dotey [2025-12-20](https://x.com/dotey/status/2002230052734341608)

听起来很美好，对吧？

但挑战也很现实：

\- 要完整搭建一个 Agent 系统没想的那么容易，不仅要和模型交互，还要处理好用户交互，还有上下文工程

\- 要让模型理解和使用从未训练过的私有组件

\- 要在浏览器中实时预览生成结果

\- 出错了希望能自动修复

由于团队之前没有开发过 Agent

![Image](https://pbs.twimg.com/media/G8lZjrUXMAEe827?format=jpg&name=large)

* * *

**宝玉** @dotey [2025-12-20](https://x.com/dotey/status/2002230297396387963)

我第一个建议很现实：先跑通再优化

—— 构建 Agent 最难的不是技术，而是完整跑通流程。

![Image](https://pbs.twimg.com/media/G8lZycBXkAAVxAd?format=jpg&name=large)

* * *

**宝玉** @dotey [2025-12-20](https://x.com/dotey/status/2002230457530765621)

我推荐他们基于 Claude Agent SDK 进行二次开发，而不是从零造轮子。一些关键理由包括：

1\. Claude Code 已经验证了它是可行的

2\. 开箱即用，内置工具足够满足绝大数场景

3\. 可以自定义工具、接入 MCP、自定义 Skill

4\. 可以接入国产兼容模型

还帮着基于 Claude Agent SDK 快速搭建了一个原型系统。一些关键代码还开源在这里：https://github.com/JimLiu/claude-agent-kit…

这样很快有了个基本可用的 Agent。

![Image](https://pbs.twimg.com/media/G8lZ-vpWgAEdb-z?format=jpg&name=large)

* * *

**宝玉** @dotey [2025-12-20](https://x.com/dotey/status/2002230729795604714)

接下来就是解决代码的浏览器预览问题。

一开始我们尝试用 Sandpack（浏览器端沙盒）做代码预览，结果发现复杂组件根本跑不起来，而且无法发挥 Agent 读写文件的能力。

转向方案是给 Agent 一个本地文件系统——每个会话一个独立环境（虚拟机或目录），Agent 可以自由读取、修改、编译代码。这个决策让 Agent 的能力得到了最大化发挥。

给 Agent 一个本地文件系统才能最大化的发挥 Agent 能力

![Image](https://pbs.twimg.com/media/G8laNURWcAAbnih?format=jpg&name=large)

* * *

**宝玉** @dotey [2025-12-20](https://x.com/dotey/status/2002231160655491164)

给 Agent 一个本地文件系统才能最大化的发挥 Agent 能力

![Image](https://pbs.twimg.com/media/G8lalL4XcAE2CrL?format=jpg&name=large)

* * *

**宝玉** @dotey [2025-12-20](https://x.com/dotey/status/2002231298694246634)

另一个难题就是如何让 AI 学会使用从未训练过的私有组件？

其实就是把 Agent 当作新员工，用高质量文档和参考代码来教会它。

我们把设计系统说明、组件列表、API 文档全部 Markdown 化，让 Agent 按需检索。高质量的参考代码本身就是最好的教材。

而且完全不需要复杂的 RAG 系统，直接让 Agent

![Image](https://pbs.twimg.com/media/G8lavrZW4AAa_SM?format=jpg&name=large)

* * *

**宝玉** @dotey [2025-12-20](https://x.com/dotey/status/2002231506190962802)

还有一个难题就是如何保证生成代码的质量，让代码能跑起来？

为了保证代码质量，为 Agent 建立了一套"生成 → 验证 → 修复"的自动化闭环：Lint 静态检查、编译验证、视觉比对（借助 Chrome DevTool MCP 做截图对比）。

一个节约主 Agent 上下文的技巧：把验证工具放入 Skill 或

![Image](https://pbs.twimg.com/media/G8la51oXUAAnpfC?format=jpg&name=large)

* * *

**宝玉** @dotey [2025-12-20](https://x.com/dotey/status/2002231691385970865)

系统跑通了，Demo 很惊艳，但……

很快就没什么人用。

初期大家觉得新鲜，但很快就弃用了。开始和他们一起深度复盘，发现问题根本不在技术，而在产品逻辑与用户习惯的错位。

![Image](https://pbs.twimg.com/media/G8lbGhUWIAAXFIb?format=jpg&name=large)

* * *

**宝玉** @dotey [2025-12-20](https://x.com/dotey/status/2002232006839804178)

通过对内部员工的调查访谈，很快就找到了原因：

习惯阻力：设计师和产品经理更习惯在 Figma 里工作，而不是对着一个对话框。从舒适区（Figma）跳到陌生区（Agent 对话），这个门槛比想象中高得多。大部分甚至不知道该在聊天窗口写啥。

80/20 瓶颈：Agent 能实现 80% 的效果，但剩下 20%

![Image](https://pbs.twimg.com/media/G8lbOqVXIAAgCji?format=jpg&name=large)