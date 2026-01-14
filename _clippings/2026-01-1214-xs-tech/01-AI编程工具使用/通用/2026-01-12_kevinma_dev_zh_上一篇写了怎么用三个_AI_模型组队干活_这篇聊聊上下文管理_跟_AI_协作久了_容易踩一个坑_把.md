---
title: "2026-01-12_kevinma_dev_zh_上一篇写了怎么用三个_AI_模型组队干活_这篇聊聊上下文管理_跟_AI_协作久了_容易踩一个坑_把"
source: "https://x.com/kevinma_dev_zh/status/2006764405313470920"
author:
  - "[[@kevinma_dev_zh]]"
published: 2026-01-12
created: 2026-01-12
description:
tags:
  - "x"
  - "@kevinma_dev_zh"
  - "https"
  - "2026-01-02"
---

# 上一篇写了怎么用三个 AI 模型组队干活，这篇聊聊上下文管理。 跟 AI 协作久了，容易踩一个坑：把

**Kevin Ma** @kevinma\_dev\_zh 2025-12-30

上一篇写了怎么用三个 AI 模型组队干活，这篇聊聊上下文管理。

跟 AI 协作久了，容易踩一个坑：把聊出来的东西都往文档里塞。时间一长，过时信息一堆，AI 读了反而被干扰。

这个问题的根源在于混淆了过程性上下文和持久性文档。

我原来的习惯是，跟 AI 聊完技术方案就存到 docs 目录里，方便各个 Agent 共享。

时间一长，目录里堆满了"方案 v1"、"重构计划"、"某某设计草案"。过时了不敢删，不知道哪个还有用。更麻烦的是，AI 探索代码库的时候会把这些过时文档也读进去，基于错误信息做判断。

后来想明白了，Issues 和 PR 本来就是管理"过程"的工具，直接复用就行。

现在每个任务我都创建一个 Issue，把背景、方案、任务拆解、验收标准都放进去，相当于一张任务单。做完就关掉，过程性的东西随之归档，代码库保持干净。

PR 也一样。描述里写清楚改了什么、为什么改、怎么测试。合并后这些信息跟代码绑在一起，不再是散落的文档。

docs 目录只存放真正需要长期维护、代表项目核心知识的持久性文档，比如 PRD、UI/UX 规范、架构设计、开发规范和 API 规范等。

这个其实就是复用成熟的人类团队协作经验，把每个 Agent 当作团队成员，通过 Issue 分配任务，通过 PR Review 代码，通过共享文档同步核心知识。

这使得 AI 的协作变得更加高效、可控且可追溯。

> 2025-12-30
> 
> 分享一下我的开发工作流，我主力使用 Claude Code, Codex CLI 和 Gemini CLI，组成一个开发团队。
> 
> Claude Code 写代码快，小任务一把梭没问题。但任务一大，几乎必定有 Bug。让它自己改，改着改着容易绕进去。
> 
> 所以我让 Codex 来 Review。 x.com/xqliu/status/2…

* * *

**吕立青\_JimmyLv 2𐃏26** @Jimmy\_JingLv [2026-01-02](https://x.com/Jimmy_JingLv/status/2006909205492683162)

哈哈哈，我没叫docs/就叫notes/ ，相当于给我和它一个memory

那对了，你是通过GitHub MCP之类的让agent去读issue内容吗？

* * *

**Kevin Ma** @kevinma\_dev\_zh [2026-01-02](https://x.com/kevinma_dev_zh/status/2006917409098310038)

我使用gh命令，模型自动会去找这个命令。只需要安装授权一次，任意 agent 都能调用，比mcp优雅

* * *

**吕立青\_JimmyLv 2𐃏26** @Jimmy\_JingLv [2026-01-02](https://x.com/Jimmy_JingLv/status/2007066930172289219)

嗯嗯 那这个确实更棒，哈哈哈

* * *

**zac** @zac3fire [2026-01-11](https://x.com/zac3fire/status/2010375619486654838)

上周没有全力开发，基本上就是清理这个。之前很多项目方案和问题都保存了，但一些文档没有即使更新，导致多个ai对项目有一些错误判断。

当然，也因为我没有做好项目管理。最后清理了一番，使用github projects来做项目规划，有啥问题直接提交issues，也能同步到projects里

同时备份一个backlog在文件夹里。

另外，确实很多方案我有点忘了怎么确定的。然后ai基本都是靠提交的pr帮我回忆起来的。

当然，后面发现antigravity有个不错的功能就是我与ai的聊天记录可以导出，放在项目里。这样就不会遗忘了。

* * *

**Kevin Ma** @kevinma\_dev\_zh [2026-01-11](https://x.com/kevinma_dev_zh/status/2010457621560688819)

我觉得聊天记录还是太详细碎片化了，过程信息太多。issues 和 pr 刚刚好

* * *

**Jarvis贾维斯** @Jarvis2hang [2026-01-02](https://x.com/Jarvis2hang/status/2006960430107996236)

我也遇到这样的问题，一直没有好的方案，跟ai聊的内容，让她用md记到指定目录，时间一长，就是各种混乱的内容的。

本质上还是memory管理和上下文管理，需要换个思路来维护

* * *

**Kevin Ma** @kevinma\_dev\_zh [2026-01-02](https://x.com/kevinma_dev_zh/status/2006984155150880871)

围绕需求和任务产生的临时文档和上下文，用 issues 很好，你可以试试

* * *

**Jarvis贾维斯** @Jarvis2hang [2026-01-02](https://x.com/Jarvis2hang/status/2007018888886985172)

好的

* * *

**泊舟** @bozhou\_ai [2026-01-02](https://x.com/bozhou_ai/status/2006908689777840628)

这就跟本地切个分支一个意思是吧

* * *

**Kevin Ma** @kevinma\_dev\_zh [2026-01-02](https://x.com/kevinma_dev_zh/status/2006984449410609277)

不一样，分支是管理代码的，issues 是做任务和上下文协同的

* * *

**Himanshu Kumar** @codewithimanshu [2026-01-02](https://x.com/codewithimanshu/status/2006911293169549681)

Kevin observes document bloat from AI conversation integration.

凯文观察到 AI 对话整合导致文档膨胀。

* * *

**MJ Zou** @emjayzo [2026-01-02](https://x.com/emjayzo/status/2006914250313175117)

啊！GitHub Issues这个东西有道理呀

* * *

**奇特飞古** @laofeiguUK [2026-01-11](https://x.com/laofeiguUK/status/2010278080388964692)

成熟的团队一直是这么用issues的…

* * *

**马克** @suke2826 [2026-01-02](https://x.com/suke2826/status/2006927193943978138)

很好

* * *

**Bito** @BitoHQ

10x faster production-ready code in Cursor and Claude with Bito’s AI Architect:

1\. System intelligence

2\. Services, APIs, dependencies

3\. Grounded code generation

4\. Production-ready output

借助 Bito 的 AI 架构师，在 Cursor 和 Claude 中实现 10 倍更快的生产就绪代码：

系统智能

2\. 服务、API、依赖

3\. 基于实际的代码生成

4\. 生产就绪的输出