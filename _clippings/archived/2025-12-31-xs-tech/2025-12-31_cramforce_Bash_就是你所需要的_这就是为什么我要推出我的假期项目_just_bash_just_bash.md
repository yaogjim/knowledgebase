---
title: "2025-12-31_cramforce_Bash_就是你所需要的_这就是为什么我要推出我的假期项目_just_bash_just_bash"
source: "https://x.com/cramforce/status/2004992618913251786"
author:
  - "[[@cramforce]]"
published: 2025-12-31
created: 2025-12-31
description:
tags:
  - "#network"
  - "x"
  - "@cramforce"
  - "https"
---

# Bash 就是你所需要的！ 这就是为什么我要推出我的假期项目：just-bash just-bash

**Malte Ubl** @cramforce [2025-12-27](https://x.com/cramforce/status/2004992618913251786)

Bash 就是你所需要的！

这就是为什么我要推出我的假期项目：just-bash

just-bash 是 TypeScript 中相当完整的 bash 实现，旨在作为 AI 代理使用的 bash 工具。因为事实证明，代理们喜欢通过 shell 脚本探索数据，甚至不仅仅是编码方面。

它包含 grep、sed、awk 以及像 Claude Code 或 Cursor 这样的代理会使用的 99% 顶尖特性。事实上，Claude Code 可以用它进行安全的 bash 执行。

在包中

\- 一个 bash 工具，用于 @aisdk

一个供你自己或你的编码代理使用的二进制文件

一个覆盖文件系统，用于安全地向你的代理提供文件

一个兼容 Vercel Sandbox 的 API，这样如果需要运行二进制文件，你可以快速升级到真实的虚拟机

一个使用 just-bash 探索 just-bash 代码库的示例 AI 代理

我导入了 Oils Shell bash 兼容套件，而 just-bash 表现得相当出色。这个代码库有趣的地方在于：它基本上完全由 Opus 4.5 编写。编码代理喜欢 bash，而且很擅长复现它。它们还很擅长教科书级别的递归下降解析器和 AST tweet-walk 解释器。话虽如此，代码量相当大，我没全看完 😅 .

这本质上是个 hack，但似乎真的很有用。我还没发现代理想用的东西它不支持的，而且它速度快、安全（有注意事项）。它无法写入你的电脑，并且文件系统被赋予了代理无法逃离的根权限。

在 https://npmjs.com/package/just-bash…

相关：我们最近的博客文章讲述了我们如何将数据分析代理迁移到 bash 工具，并实现了惊人的质量提升 vercel.com/blog/we-removed-80-percent-of-our-agents-tools... 视频展示了示例代理调查刚刚用 bash 编写的代码库

* * *

**yenkel** @yenkel [2025-12-27](https://x.com/yenkel/status/2004994452952330328)

好奇你有没有看 @tursodatabase agentfs 关于文件系统实现的 https://docs.turso.tech/agentfs/introduction…

看起来这是个不错的应用场景 @glcst ?

* * *

**Malte Ubl** @cramforce [2025-12-27](https://x.com/cramforce/status/2004994788010156489)

启动 Claude Code 并连接它。添加文件系统非常简单。示例：

* * *

**Ankur Goyal** @ankrgyl [2025-12-28](https://x.com/ankrgyl/status/2005076276504350788)

非常非常酷

* * *

**Malte Ubl** @cramforce [2025-12-28](https://x.com/cramforce/status/2005076792256987174)

我监督构建玩得很开心

* * *

**Giuseppe** @giuseppegurgone [2025-12-28](https://x.com/giuseppegurgone/status/2005386372677550311)

这是你的第一个提示吗？这个代理有没有搭建那个初始提交？如果是的话，那挺简洁的，这是什么代理？

* * *

**Malte Ubl** @cramforce [2025-12-28](https://x.com/cramforce/status/2005388044267069587)

项目.md 包含我的提示。

这是克劳德代码，搭配 Opus 4.5

* * *

**Steren** @steren [2025-12-28](https://x.com/steren/status/2005333188474978377)

给它 cURL，释放它真正的力量。

* * *

**Malte Ubl** @cramforce [2025-12-28](https://x.com/cramforce/status/2005333811631116787)

已经有 cURL 了！

https://github.com/vercel-labs/just-bash?tab=readme-ov-file#network-access…

![Image](https://pbs.twimg.com/media/G9RgZmNbIAAPvtp?format=jpg&name=large)

* * *

**Karim C** @BrandGrowthOS [2025-12-27](https://x.com/BrandGrowthOS/status/2005058110512411067)

有趣的构建。问题：你的代理实际上什么时候需要 bash 逻辑，而不是更简单的结构化工具？我发现，一旦我的团队在三个月后试图维护它，shell 的灵活性就变成了调试噩梦。

* * *

**Malte Ubl** @cramforce [2025-12-27](https://x.com/cramforce/status/2005058685731787060)

我觉得没有一成不变的规则。

当你看到很多涌现行为时，通常效果不错。这种行为既更强大，又本质上更难维护。权衡。

* * *

**Muvaffak** @muvaffakonus [2025-12-27](https://x.com/muvaffakonus/status/2005009178591723794)

我很好奇工具调用的速度问题，因为我们正在为移动使用的 MCP（针对代理）优化这个耗时。你觉得这会更快吗？是因为工具调用本身，还是 exec fork 的开销，或者其他原因？

* * *

**Malte Ubl** @cramforce [2025-12-27](https://x.com/cramforce/status/2005009971965284555)

你得把你的配置解释得更清楚一点。这通常比通过进程边界或网络到沙箱使用真实的 bash 要快得多。

* * *

**Adam** @\_overment [2025-12-28](https://x.com/_overment/status/2005168049624670348)

喜欢这个项目！

我对这个有一些问题，好奇你怎么想：

'bash is all you need'只是故事的一部分，对吧？虽然文件系统无疑是高级 AI 代理的核心要素，但如果需要一个能够