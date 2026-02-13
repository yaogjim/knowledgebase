---
title: "2026-02-13_dotey_笔记本应用_Obsidian_发布了_Obsidian_CLI_由于用户发掘出了很多_Claude"
source: "https://x.com/dotey/status/2021330725773975711"
author:
  - "[[@dotey]]"
published: 2026-02-13
created: 2026-02-13
description:
tags:
  - "x"
  - "@dotey"
  - "https"
  - "2026-02-11"
---

# 笔记本应用 Obsidian 发布了 Obsidian CLI，由于用户发掘出了很多 Claude

**宝玉** @dotey 2026-02-10

笔记本应用 Obsidian 发布了 Obsidian CLI，由于用户发掘出了很多 Claude Code 配合 Obsidian 使用的场景，所以 Obsidian 官方也发布了 CLI。

这会是个趋势，很多传统都会为 AI Agent 开发一套 CLI 接口。

日常笔记操作全部命令化了：

\- 创建、读取、编辑、删除笔记

\- 搜索 vault 内容

\- 管理任务（列出、标记完成、切换状态）

\- 操作标签、属性、书签

\- 打开每日笔记、追加内容

\- 管理模板、主题、插件

看起来似乎普通用户用不上 CLI，但是你换个角度看，这个 CLI 压根就不是给人用的，而是给 AI Agent 用的你就能理解了。

为啥不用 MCP 呢？

之前 Obsidian 社区有一些 MCP Server 方案来让 AI 访问笔记库，但 CLI 方案更轻量直接，不需要额外的 MCP 服务器，Claude Code 本身就能在终端执行命令，天然就能用。

记住，传统应用都要为 AI Agent 开发一套接口，CLI 也许不是最终形式，但是目前最佳形式。应用开发者尽早关注尽早准备。

> 2026-02-10
> 
> Anything you can do in Obsidian you can do from the command line.
> 
> Obsidian CLI is now available in 1.12 (early access).
> 
> 你在 Obsidian 中能做的任何事情，都可以通过命令行完成。
> 
> Obsidian CLI 现已在 1.12（早期访问）中可用。

* * *

**yan5xu** @yan5xu [2026-02-10](https://x.com/yan5xu/status/2021334338923790799)

😂 function call->mcp->skill->cli 最终归宿了

😂 函数调用->mcp->skill->cli 最终归宿了

* * *

**宝玉** @dotey [2026-02-10](https://x.com/dotey/status/2021342110956519912)

cli 其实配合 skill 最好

* * *

**Jackywine** @Jackywine [2026-02-11](https://x.com/Jackywine/status/2021379465050456525)

解惑了，我去研究一下 CLI 工具以及基本命令

* * *

**王乔治** @Naaaarukaru [2026-02-11](https://x.com/Naaaarukaru/status/2021410020207030778)

为什么需要obsidian cli？而不是直接用 bash 脚本操作呢，甚至不依赖 obsidian。

* * *

**宝玉** @dotey [2026-02-11](https://x.com/dotey/status/2021410429717844142)

节约token，不需要每次都去学习怎么使用

* * *

**JinchenMa金尘马** @jinchenma94 [2026-02-11](https://x.com/jinchenma94/status/2021384847995109608)

昨天半夜刷到了，感觉这个路子一下通了。最近一直在用Claude code去处理我的obsidian文档。给自己打造一套知识管理+流程化内容创作工作流。思路跟don哥的思路差不多。

但Claude

* * *

**Stephen Ni** @nisiyong [2026-02-11](https://x.com/nisiyong/status/2021461607021412696)

Apple Notes 用户，等苹果的开放性真是等麻了🥹 很多苹果的操作都是 AppleScript，得自己封装下

* * *

**Jason Wang** @jasonw\_nz [2026-02-10](https://x.com/jasonw_nz/status/2021331536025682358)

CLI 最大的问题是普通人没发安装，MCP就不一样了，7千万chatGPT 用户都可以一键安装

* * *

**蜗牛** @bewaterya [2026-02-11](https://x.com/bewaterya/status/2021441509183332622)

是不是vim也得重新用起来了，需要人工介入的时候直接在终端进行快速修改

* * *

**vewin** @lawgpts [2026-02-10](https://x.com/lawgpts/status/2021355079572521283)

Obsidian 创始人还自己写了个 Obsidian skill，就是简单的的写了笔记画板数据等三个核心对象的 md 文件结构规范，llm 就懂如何编辑。如果有 cli 了那 skill 更简单了，节省大量 token 去记忆规则

* * *

**YiChu** @Go7hic [2026-02-11](https://x.com/Go7hic/status/2021403100662345897)

同意。前段时间做了一个自用的批量转 avif 的工具，cli , api 全给他加上了

* * *

**赖叔 | LaiShu.ai** @hiheimu [2026-02-11](https://x.com/hiheimu/status/2021409426671010273)

很多项目的开发观念可能要从 用户使用转变成 agent使用了

但是这种转变能对开发者带来收益吗？

* * *

**Art Lab** @daemonzhang6 [2026-02-11](https://x.com/daemonzhang6/status/2021474059712901330)

Are they back to emacs

他们回到 Emacs 了吗？

* * *

**松鼠 AI** @manonglianai [2026-02-11](https://x.com/manonglianai/status/2021402548041888207)

目前cli确实是一个比较好的方案，配合bun，也不需要写特别复杂的skill

* * *

**JOJO** @zouyanjian [2026-02-11](https://x.com/zouyanjian/status/2021482636557074660)

软件的界面是服务于人的，AI 更喜欢cli

* * *

**jojo1984** @jojo1984 [2026-02-11](https://x.com/jojo1984/status/2021388998892204336)

@grok 这个怎么用

* * *

**Scofieldfee** @scofieldfee [2026-02-10](https://x.com/scofieldfee/status/2021373525626585185)

CLI确实方便调用，以后会不会就是Agent调用各种CLI

* * *

**magnus li** @MontB2000 [2026-02-11](https://x.com/MontB2000/status/2021575580525740311)

开发个脚本驱动接口就行，没必要暴露给普通用户用

* * *

**MakerCan** @candg30024511 [2026-02-11](https://x.com/candg30024511/status/2021623445038264374)

盲猜是基于Claude agent sdk开发的

* * *

**marumaki** @marumaki911 [2026-02-11](https://x.com/marumaki911/status/2021422882317078596)

Mcp好还是skill好？为什么agent要用cli? @grok

* * *

**lora** @loraShowmylife [2026-02-11](https://x.com/loraShowmylife/status/2021439211887526033)

cli对开发群体比较有用，像我这种拿obsidian当知识库的，还是claudian好用

* * *

**Leexiaopa** @Leexiaopa [2026-02-11](https://x.com/Leexiaopa/status/2021421542492848610)

其实很多古早的桌面软件就是构建调用自己的cli的

* * *

**Jiang Chang** @cj1124q [2026-02-11](https://x.com/cj1124q/status/2021498703597777024)

我用 GEMINI CLI。

我使用 Gemini 命令行界面。

* * *

**XiaoAn** @Xiaoan\_XA [2026-02-10](https://x.com/Xiaoan_XA/status/2021373073245733008)

CLI 不是给人点的，是给 Agent 调的，这一下逻辑就全通了。

* * *

**重粒子 baryon** @lilong [2026-02-11](https://x.com/lilong/status/2021408679300600079)

一直没理解大家喜欢 Obsidian 的理由？为什么不直接用 vscode，里面有终端可以用 claude code/codex 写文章，只需要个 markdown preview 插件，比如 https://github.com/baryon/markdown-live-preview… 就能实现交互式文档

> 2026-02-11
> 
> 一直没理解大家喜欢 Obsidian 的理由？为什么不直接用 vscode，里面有终端可以用 claude code/codex 写文章，只需要个 markdown preview 插件，比如 https://github.com/baryon/markdown-live-preview… 就能实现交互式文档