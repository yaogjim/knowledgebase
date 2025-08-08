---
title: "Gemini 2.5 pro 阅读代码的优势"
source: "https://x.com/LinearUncle/status/1938832441818435803"
author:
  - "[[@LinearUncle]]"
created: 2025-07-01
description:
tags:
  - "@LinearUncle #代码阅读 #AI #Gemini #编程"
---
**LinearUncle** @LinearUncle 2025-06-27

很多提示词敲击师vibe coding一上来就用Claude Code一阵噼里啪啦敲键盘，但是遇到别人写的代码很多时候就束手无措了。

Gemini 2.5 pro(aistudio里）仍然是目前这个地球上阅读大规模代码的最佳模型，项目架构，细节追踪无不手拿把掐，用AI看代码看多了，我也感觉到代码越来越像汇编语言了，也许将来没人去读去写代码了。

当然这非常考验一个敲击师的抽象的能力以及技术功底。

记得有个推友专门做阅读代码的工具，感觉挺有市场潜力的，这一块目前是个空白。

> 2025-06-27
> 
> 开源的PasteMax，丐版的repoPrompt，用来打包代码构建上下文，再用gemini帮助读代码，够用了。
> 
> 用o3给我整出来一些打包代码的利器，我还是比较喜欢GUI的
> 
> ![Image](https://pbs.twimg.com/media/Gugc2L6W8AEwJEi?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/GucIJ_rXMAABS63?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/GucJ5oJXQAAT-EU?format=jpg&name=large)

---

**LinearUncle** @LinearUncle [2025-06-28](https://x.com/LinearUncle/status/1938982564473307271)

gemini 2.5 pro阅读gemini-cli核心流程的时序图

总耗时26秒，上下文38w左右，比用Claude Code吭哧吭哧去分析项目快了一个数量级。

还是gemini读代码有优势。

![Image](https://pbs.twimg.com/media/GuilmQsW8AA2aqo?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/GuimAmiXEAEMq02?format=jpg&name=large)

---

**不鍊金丹不坐禪** @zzwz [2025-06-28](https://x.com/zzwz/status/1938861759382835523)

配合半自动的 Cursor 微操 RepoPrompt 很好, 如果 AOE 全自动的 Cursor Code 还是用 Remote MCP \`context7 https://mcp.context7.com/sse\` & \`DeepWiki https://mcp.deepwiki.com/sse\` 就差不多了, 需要手动引用三方的时候其实可以直接把手动找到的文件甚至仓库或文档, 放到 codebase 临时目录里 @目录也行

---

**LinearUncle** @LinearUncle [2025-06-28](https://x.com/LinearUncle/status/1938862829060399490)

专业

---

**BRUNT Workwear** @bruntworkwear

The all-new USA Marin Welted is Built in the USA and delivers stability, comfort, and performance for the toughest job sites. Crafted with waterproof leather sourced from American cattle, global components, and assembled at our factory in Texas.  
全新的美国马林固特异 Welted 靴子在美国制造，为最艰苦的工作场所提供稳定性、舒适性和卓越性能。采用源自美国牛群的防水皮革、全球采购的部件，并在我们位于德克萨斯州的工厂组装而成。

---

**Alex Zhang** @jojogh\_007 [2025-06-29](https://x.com/jojogh_007/status/1939124460600336707)

读代码的工具也很多了，像codewiki，devvi，还有repo2markdown

---

**BadUncle** @BadUncleX [2025-06-28](https://x.com/BadUncleX/status/1938842785282691452)

早期确实gemini大窗口 + repoprompt做代码分析非常好， 一般代码库都hold得住

---

**LinearUncle** @LinearUncle [2025-06-28](https://x.com/LinearUncle/status/1938844724888211787)

现在也好用，阅读代码领域cc有些时候搞不定或者太慢了。

倒是可以让gemini给出一些架构，然后用cc给出每个模块的文档

---

**不鍊金丹不坐禪** @zzwz [2025-06-28](https://x.com/zzwz/status/1938862306747916623)

RepoPrompt 本家还有个自己的 MCP, 但越来越像 IDE ➕ Prompt 调试台了🤣

---

**你瞅啥** @moremoremeds [2025-06-28](https://x.com/moremoremeds/status/1939024163886498179)

请问 用gemini cli 自动降级到flash了 还回不去了 怎么解决啊？context 才用了10%

---

**add** @bigdatabong [2025-06-29](https://x.com/bigdatabong/status/1939271387740516534)

@readwise save thread  
@readwise 保存线程