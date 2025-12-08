---
title: "赵纯想关于Agent Builder和Sora2的感受"
source: "https://x.com/liseami1/status/1975776072596861307"
author:
  - "[[@liseami1]]"
published: 2025-10-09
created: 2025-10-09
description:
tags:
  - "@liseami1 #AgentBuilder #Sora2 #TTLoop #ClaudeCode #Coze #Dify"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-10-17"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---
**赵纯想** @liseami1 [2025-10-08](https://x.com/liseami1/status/1975776072596861307)

媒体对Agent Builder不兴奋，对Sora2很兴奋。原因是猴性太重，和普遍C端一样，只喜欢能刺激眼球的东西。

Agent Builder不是Coze，不是Dify。它不是工作流的编排和演绎。工作流压根儿、从来就不是Agent，因为它只有固定的流向、固定的产出物。而OpenAI的拖拉拽面板，不是让你规划工作流用的。而是对Agent装配的一种抽象。我花了三个月，探索ClaudeCode的逆向库，才用Go复刻完成的一种Agent的装配，现在所有开发者只需要动动手指就能得到。这种抽象带来的正是Agent核心封装技术的下放和普惠。

Think + ToolUse的排列组合，与固定工作流不同，它代表无穷的可能性。是LLM自身决定下一步该做什么。是真正的Agent，就像你手边的ClaudeCode 和 GeminiCLI。观察你常用的CodingCLI的工具调用链路，每一次都不是固定的。未来，结合你自身的业务设计一系列的工具，由LLM在思考后自身决定调用和调用顺序，就可以释放巨大的智能。而OpenAI，将这一切可视化了。

这还不是重点，重点是OpenAI还想吃下整个交互侧的前端实践。配合Chatkit的Widgets生成能力，我在20秒之内得到了对话流中的交互式组件。将相关组件添加到Agent的体系中，就能实现与用户的垂直场景客制化Agent。每个场景都有自身的专属UIUX，不再是简单的一次性工作后返回，而是将一切App都变身为Cursor的潜力。

图片中就是我自己在laper中设计了很久的对话式故事探讨UIUX交互的OpenAI实践，20秒，颠覆了2个月以来的复杂工作和设计。有句话说得好，"未来已经到来，只不过分布不均"。

![First image displays a white dialog box titled Create a widget in English with Chinese subtitle explaining simplified assembly of Agent using drag-and-drop panel for quick experimentation and sharing. It includes buttons for Start blank and Upload widget file. Second image shows a tool selection interface titled Tool Selection in Chinese with options listed vertically such as Weather query, Email sending, Image generation, Calendar management, File reading, Database query, Web search, Code execution, and Generate image, ending with Confirm Selection and Clear All buttons. Third image presents the Laper platform homepage with navigation menu including logo, Features, Changing, Pricing, More, and login options via Google, WeChat, or email, alongside a central illustration of a green-tinted cityscape map with streets and buildings, and a login form below.](https://pbs.twimg.com/media/G2tdccxbIAEeKjz?format=png&name=large) ![First image displays a white dialog box titled Create a widget in English with Chinese subtitle explaining simplified assembly of Agent using drag-and-drop panel for quick experimentation and sharing. It includes buttons for Start blank and Upload widget file. Second image shows a tool selection interface titled Tool Selection in Chinese with options listed vertically such as Weather query, Email sending, Image generation, Calendar management, File reading, Database query, Web search, Code execution, and Generate image, ending with Confirm Selection and Clear All buttons. Third image presents the Laper platform homepage with navigation menu including logo, Features, Changing, Pricing, More, and login options via Google, WeChat, or email, alongside a central illustration of a green-tinted cityscape map with streets and buildings, and a login form below.](https://pbs.twimg.com/media/G2tdccEa4AAbjJG?format=png&name=large) ![First image displays a white dialog box titled Create a widget in English with Chinese subtitle explaining simplified assembly of Agent using drag-and-drop panel for quick experimentation and sharing. It includes buttons for Start blank and Upload widget file. Second image shows a tool selection interface titled Tool Selection in Chinese with options listed vertically such as Weather query, Email sending, Image generation, Calendar management, File reading, Database query, Web search, Code execution, and Generate image, ending with Confirm Selection and Clear All buttons. Third image presents the Laper platform homepage with navigation menu including logo, Features, Changing, Pricing, More, and login options via Google, WeChat, or email, alongside a central illustration of a green-tinted cityscape map with streets and buildings, and a login form below.](https://pbs.twimg.com/media/G2td2xebAAA-GzH?format=jpg&name=large)

---

**赵纯想** @liseami1 [2025-10-08](https://x.com/liseami1/status/1975777072485441638)

对ClaudeCode逆向感兴趣的，可以参考 https://github.com/shareAI-lab/analysis\_claude\_code…

我用Go实现了核心的TTLoop，不代表我能以个人能力实现ClaudeCode优秀的上下文压缩器、节奏编排、消息队列、状态缓存等优秀的设计。AgentBuilder将这一切都变成拖拉拽了。