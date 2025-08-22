---
title: "MCP：跨越AI模型与现实的桥梁"
source: "https://mp.weixin.qq.com/s/hlZnm5gu9q1nZHhzHWw0Xg"
author:
  - "[[致问]]"
published:
created: 2025-03-26
description: "本文主要围绕AI技术的进步，特别是Anthropic的Claude 3.7 Sonnet模型在逻辑推理、代码生成和复杂任务执行方面的能力提升及其应用场景。"
tags:
  - "clippings"
---
原创 致问 *2025年03月21日 08:32* *浙江*

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naKUex9wafI53I58c6TWgXFn4iaD1PoRTGTMuNmyboAkM9a2qbnxEtwibia6RHOyoYedxcG1ocfVCq5mA/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

阿里妹导读

  

本文主要围绕AI技术的进步，特别是Anthropic的Claude 3.7 Sonnet模型在逻辑推理、代码生成和复杂任务执行方面的能力提升及其应用场景。

一、引言

AI 技术近年来取得了显著进展，从最初的文本生成和简单问答工具，逐步演变为能够与现实世界互动的执行者。这种转变得益于大模型的增强能力，特别是 Anthropic 的 Claude 3.7 模型，它在逻辑推理和代码生成方面表现卓越。

早期用户对 Claude 3.7 Sonnet 的反馈：

- Cursor 报告称其在实际编码任务中“再次成为最佳”，特别是在处理复杂代码库和高级工具使用方面。
- Cognition 发现它在规划代码更改和处理全栈更新方面远超其他模型。
- Vercel 强调其在复杂代理工作流中的“卓越精度”。
- Replit 成功使用它从头构建复杂的网络应用程序和仪表板，而其他模型则停滞不前。
- Canva 报告其生成的代码“生产就绪”，错误显著减少。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naLrU7fFaF1s5cc9SMEzqmQzRibc6T5icPEJlnKFp14TUA2GTqc0ibzyPINl6LwicJWdIb61xeV1by7icuA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

Claude 3.7 Sonnet是 AI 技术的重要里程碑，它们通过深度推理、自主工作和有效协作的能力，不仅辅助人类完成任务，还扩展了人类的可能性，预示了一个 AI 与人类深度合作的未来。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naLrU7fFaF1s5cc9SMEzqmQzJKuklq3EYWp4RlAJJZv5png66RHpplCXAjRkdCLjHD0ub2h1jTK00w/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

参考：

- https://www.anthropic.com/news/claude-3-7-sonnet
- https://www.anthropic.com/claude/sonnet#customer-stories

二、Claude 3.7：技术突破与能力提升

官方研究报告地址： https://assets.anthropic.com/m/785e231869ea8b3b/original/claude-3-7-sonnet-system-card.pdf

2025 年 2 月 25 日，Anthropic 宣布推出 Claude 3.7 Sonnet，这是其迄今最智能的 AI 模型，同时推出了 Claude Code，一款用于代理编码的命令行工具。这一发布标志着 AI 技术在混合推理和实际任务执行方面的重大进步，特别是在编码和网络开发领域。

报告详细探讨系统卡的核心内容，包括模型能力、安全措施和责任扩展政策（RSP）评估。

  

**模型概述**

根据 Claude 3.7 Sonnet 系统卡 ，Claude 3.7 Sonnet 是 Claude 3 系列的混合推理模型，首次引入“扩展思考”模式。它是 Anthropic 迄今最智能的模型，特别擅长编码任务，并具有 200K 的上下文窗口。以下是关键技术亮点：

- 知识截止日期：截至 2024 年 10 月底，训练数据包括 2024 年 11 月之前的数据。
- 训练数据：使用专有混合数据，包括公共互联网、非公开第三方数据、数据标注服务和内部生成数据，不包括用户提示/输出数据，遵循 robots.txt 爬取规则，不访问密码保护或 CAPTCHA 页面。
- 训练重点：注重帮助性、无害性和诚实性，使用 Constitutional AI，并新增了从 Collective Constitutional AI 研究中得出的残疾权利原则。
- 扩展思考模式：通过令牌序列进行推理，允许用户通过系统提示指定最大思考令牌数，特别适用于数学、复杂分析和多步骤任务。

  

**各种安全评估**

根据《Claude 3.7 Sonnet System Card》（Anthropic, 2025），Claude 3.7 模型通过全面的安全性评估，确保其在复杂任务中的无害性和可靠性。报告中详细探讨了儿童安全、偏见、恶意使用和提示注入等风险，并在责任扩展政策（RSP）框架下评估了 CBRN、自主性及网络安全领域的潜在威胁。例如，模型在 SWE-bench Verified 测试中得分 70.3%，在减少不必要拒绝方面提升了 45%，同时通过扩展思考模式的优化，保持了推理的忠实性和透明度（Anthropic, 2025, p. 12-41）。这种对安全的重点关注，体现了 Anthropic 致力于负责任 AI 发展的承诺。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naLrU7fFaF1s5cc9SMEzqmQzibtFBWEicib1kCI8O5HY3Ccia9v3QxSFszYxjDK3HmwmC60E7icuJv7tleg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**安全与无害性评估**

系统卡详细描述了 Claude 3.7 Sonnet 的安全测试，涵盖多个方面：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/Z6bicxIx5naIDZOZtfiaNBvjCkqQIJ90dznbA8j1N7q7KFbibc1sbKPcPWyVw87QibCITBMdtT2SSMMwbibOnBsbT7A/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![图片](https://mmbiz.qpic.cn/mmbiz_png/Z6bicxIx5naIDZOZtfiaNBvjCkqQIJ90dzc9Sf2tdsTnNZtMRqDwcfiaIaohEoXQW8DHJBQYiat6pt4yNpSNSInZibw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![图片](https://mmbiz.qpic.cn/mmbiz_png/Z6bicxIx5naIDZOZtfiaNBvjCkqQIJ90dzia52qSmmiazYF19zJ3y4B7XX2UOyLYsCGlxcoSkl1y5skM2KdnptAxlQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**责任扩展政策（RSP）评估**

系统卡还包括 RSP 评估，涵盖 CBRN、自主性和网络安全领域：

![图片](https://mmbiz.qpic.cn/mmbiz_png/Z6bicxIx5naIDZOZtfiaNBvjCkqQIJ90dzS8FjdjsxGy4Gn7SF0vAYTbQUAFQUFL8V5JZsq6Tcu8lcTYq4LfI4kw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

网络安全与未来风险

系统卡还评估了网络操作和潜在未来风险：

- 自主网络操作：在现实评估中，Claude 3.7 Sonnet 在易任务中 1/1 成功（Pass@5），中任务 1/2 成功。
- Cybench 基准：在 40 个 CTF 挑战中，成功 15/34 次，与 3.5 Sonnet (new) 的 14/34 比较。
- 破坏能力：评估未来 AI 系统可能破坏评估或影响开发者的行为，引用相关研究。

#### 为什么这么多的安全评估？

问题：为什么Claude要这么大费周章地做安全性的评估？这说明AI真的已经开始在威胁到人类了？里面关于安全的篇幅为什么这么多？

Grok3：Claude之所以大费周章地进行安全性评估，不是因为AI已经威胁人类，而是为了预防潜在风险、满足监管和用户需求、应对技术复杂性，并体现伦理责任。安全篇幅多是因为评估的系统性、透明性和全面性，覆盖了从基础功能到高风险应用的各个方面。这种做法表明Anthropic致力于负责任的AI开发，确保Claude 3.7 Sonnet在广泛应用中安全可靠，而非AI威胁的证据。

Claude 3.7：安全评估之所以成为Claude等AI系统开发过程中的重要环节，并非因为AI已经对人类构成实际威胁，而是出于负责任的技术发展考虑。

重视安全评估主要有以下几个原因：

1.预防性原则 - 在技术发展初期就建立安全框架，比等问题出现后再解决更为明智。

2.社会责任 - 开发强大工具的企业有责任确保其产品不会造成意外伤害。

3.复杂性管理 - AI系统越来越复杂，可能出现开发者无法预见的行为。

4.建立信任 - 透明的安全评估有助于建立公众和监管机构对AI技术的信任。

5.防范错误使用 - 即使AI本身无害，也可能被错误使用或滥用。

大量关于安全的内容反映了行业对这一问题的重视，以及努力确保AI发展朝着有益于人类的方向前进的决心，而非暗示AI已经成为威胁。这更像是一种技术成熟度的体现，就像其他任何重要技术（如医药、航空、核能）都需要严格的安全标准一样。

O3 Mini：从某种角度看，Claude（以及其他类似的先进 AI 系统）在安全性评估上花费大量篇幅，其实是一种负责任研发和部署技术的表现，而不必然意味着 AI 已经在“威胁到人类”。下面几点可以解释这种现象：

**1.预防和控制风险**

高级 AI 系统拥有强大的生成能力和决策潜力，这也意味着在特定场景下可能会产生不可预见的行为或被错误地利用。通过系统化的安全评估，开发者可以提前识别和缓解潜在风险，确保系统在各种情况下都能遵循设定的伦理和安全标准。

**2.负责任的技术开发**

如今的 AI 研究环境越来越重视“对齐”问题，即如何使 AI 的目标和行为与人类的价值观保持一致。Claude 在开发过程中增加安全性评估和相关措施，正是在体现这份对技术社会影响的谨慎态度。很多机构都在提前进行大量测试和理论验证，以防止可能出现的问题。

**3.避免滥用和误解**

安全性评估不仅仅是为了防止 AI 自身出现问题，也包括防范外部恶意使用情况。通过设定详细的安全策略和限制，开发者希望能减少 AI 被错误利用或造成人为损害的可能性。

**4.前瞻性安全设计**

高度复杂的系统通常需要层层防护，就像现代工业中的其他高风险领域（比如航空、核能等），AI 技术的发展也需要稳妥而缜密的安全设计。篇幅较多的安全部分说明相关团队在项目前期就投入大量精力，确保系统在实际运行中具备足够的稳定性和安全保障。

因此，Claude 要进行如此详尽的安全性评估，并不是说明 AI 已经构成了直接威胁，而是开发者认识到随着技术不断进步，潜在风险也在增加，从而主动采取措施以确保技术“向善”发展。这样的做法反而体现了整个行业对安全和伦理问题高度重视的态度。

  

**案例**

#### 天气动画卡片

创建一个包含 CSS 和 JavaScript 的单一 HTML 文件，以生成一个动画天气卡。该卡片应通过不同的动画直观地展示以下天气条件： 风：（例如，移动的云、摇摆的树木或风线） 雨：（例如，落下的雨滴、形成的水坑） 晴：（例如，闪耀的光线、明亮的背景） 雪：（例如，落下的雪花、积雪） 所有天气卡应并排显示。卡片应具有深色背景。在这个单一文件中提供所有的 HTML、CSS 和 JavaScript 代码。JavaScript 应包含一种切换不同天气条件的方法（例如，一个函数或一组按钮），以展示每种天气的动画效果。

关注 重播 分享 赞

视频加载失败，请刷新页面再试

[刷新](https://mp.weixin.qq.com/s/)

<audio><source src="https://res.wx.qq.com/voice/getvoice?mediaid=MzA3MzA0MTAyNF8xMDAwMDI3Njk="></audio>

[视频详情](https://mp.weixin.qq.com/s/)

#### 生成SVG图

详细阅读我下面的文章内容，帮我基于文章的内容重点，绘制一张SVG图，用图说话，方便我快速获取信息；

\====

MCP相关的内容...

![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

#### 设计风格对比(内容对比)

请为我创建一个 HTML 页面，展示多种主流设计风格的视觉示例和效果，以便我能直观了解每种风格的样貌。请包含现代主义、极简主义、工业风格等，确保页面简洁易懂。

![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

#### 教学动画

这个是让模型帮我写的一个提示词，看其它地方讲可以用来做动画试一下效果。

生成一个动画，讲解如何计算由参数曲线和x轴围成的面积。参数曲线由函数 ( x(t) ) 和 ( y(t) ) 定义，( t ) 从 0 到 1。动画需逐步展开，视觉清晰，帮助学生理解计算过程。

视觉元素:

- 坐标系:
- 绘制一个笛卡尔坐标系，x轴和y轴用白色标注。
- x轴水平位于底部，标记点 0 和 1；y轴垂直位于左侧，标记点 0 和 1。
- 关键点:
- 用不同颜色的点标记并用白色文本标注以下位置：
- 点 A (0, 0)：原点，用黄色点标记。
- 点 B (0, 1)：y轴上，用红色点标记。
- 点 C (1, 1)：右上角，用紫色点标记。
- 点 D (1, 0)：x轴上，用黄色点标记。
- 矩形:
- 用浅蓝色线条连接 A、B、C、D 四点，形成一个正方形。
- 参数曲线:
- 在正方形内绘制一条黄色的半圆形曲线，向上拱起，表示参数曲线 ( x(t) ) 和 ( y(t) )。
- 阴影区域:
- 将曲线与x轴之间的区域用青色（teal）填充，表示待计算的面积。
- 公式展示:
- 在青色阴影区域内，用白色文本清晰显示面积计算公式：

\\text{Area} = \\int\_{0}^{1} y(t) \\cdot x'(t) \\, dt

动画序列: 动画需按以下步骤逐步呈现，确保观众能跟随理解：

1.从黑色背景开始，绘制并标注坐标系（x轴和y轴）。

2.逐一绘制并标注点 A、B、C、D，使用各自的颜色。

3.用浅蓝色线条连接四点，绘制矩形正方形。

4.缓慢绘制黄色半圆形曲线，强调其为参数曲线。

5.用青色填充曲线下的区域，突出显示待计算的面积。

6.在阴影区域内显示公式

\\text{Area} = \\int\_{0}^{1} y(t) \\cdot x'(t) \\, dt

风格与设计:

- 采用数学插图常见的简洁精确风格。
- 使用黑色背景，搭配白色文本和彩色元素（点、线、阴影），增强视觉对比度。
- 确保所有元素（点、曲线、阴影）清晰可辨。

额外要求:

- 动画过渡需平滑，节奏适中，避免观众感到仓促。
- 可加入细微动态效果（如曲线逐渐绘制、阴影逐步填充），增加趣味性和吸引力。

关注 重播 分享 赞

视频加载失败，请刷新页面再试

[刷新](https://mp.weixin.qq.com/s/)

<audio><source src="https://res.wx.qq.com/voice/getvoice?mediaid=MzA3MzA0MTAyNF8xMDAwMDI3Njk="></audio>

[视频详情](https://mp.weixin.qq.com/s/)

  

**小结**

- 模型能力持续提升，效果都比以往更好，准确度更高；
- 我们还没有完全发挥这些模型的潜力，主要是缺乏想象力；
- 只要善用模型配置和写代码的能力，AI就能在日常工作中带来巨大的帮助。
- 数据分析
- 生成报告
- 日常自动化任务
- 尝试让模型和自身领域结合，掘出更多实用价值；

三、MCP：模型与现实世界的连接

  

**什么是 MCP？**

MCP，全称是“模型上下文协议”（Model Context Protocol），是Anthropic开源的一个标准协议。打个比方，它就像是AI世界的“USB-C”接口。你知道USB-C吧？一根线就能连接手机、电脑、充电器，超级方便。MCP的作用也差不多，它让AI模型（比如Anthropic的Claude）可以轻松地跟外部的数据源和工具连接起来，比如数据库、文件系统、API等等。

以前，如果想让AI访问你的数据库或者调用某个工具，得专门写一堆代码，特别麻烦。现在有了MCP，就像是插上USB-C线那么简单，AI模型通过这个标准协议就能直接获取数据或执行操作，不用每次都重新开发连接方式。这样，开发AI应用就变得更快、更省事了。

![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

#### MCP怎么工作？

MCP用的是 **客户端-服务器** 的模式，简单来说：

- **MCP客户端：** 嵌在AI应用里（比如Claude Desktop），负责跟服务器“聊天”，告诉服务器“我需要什么数据”或者“帮我干点儿啥”。
- **MCP服务器：** 一个轻量级的小程序，连接到具体的数据源或工具（比如你的本地文件、GitHub仓库、Slack频道），然后按照客户端的请求提供数据或者执行任务。

它们之间用一种标准的消息格式（基于JSON-RPC）交流，AI模型可以通过这些消息：

1.**获取数据：** 比如从数据库里查东西、从文件里读内容。

2.**执行操作：** 比如调用API发个消息、管理代码仓库。

3.**理解指令：** 通过一些提示模板，AI知道怎么用这些数据和工具。

![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

#### MCP有什么好处？

MCP之所以厉害，主要有这几点：

1.**标准化：** 就像USB-C成了通用接口，MCP让AI跟外部世界的连接有了统一标准，省去了重复开发的麻烦。

2.**安全性：** 服务器管着访问权限，不用担心数据被乱用。

3.**灵活性：** 不管是数据库、文件还是API，MCP都能支持，而且还能根据需要扩展。

4.**跨平台：** 不管你用什么系统、什么编程语言（目前有Python和TypeScript的支持），都能用。

#### MCP能干啥？

举几个例子你就明白了：

- **数据分析：** AI可以直接查数据库，拿到最新数据帮你分析。
- **自动化任务：** 比如让AI调用API，在GitHub上创建issue，或者在Slack上发消息。
- **开发辅助：** AI跟你的代码编辑器（IDE）连起来，帮你写代码、找bug。

Anthropic已经开源了MCP，还提供了几个现成的示例服务器，比如连接Google Drive、Slack、GitHub等。社区也在开发更多服务器，未来能干的事会越来越多。

简单来说，MCP就是AI的“万能接口”。有了它，AI模型就能像插上USB-C线一样，轻松连接到各种外部数据源和工具，变得更聪明、更实用。不管是开发者还是普通用户，都能通过MCP让AI干更多事，而且过程简单又安全。未来随着MCP的普及，我们可能会看到更多酷炫的AI应用冒出来！

  

**如何开发MCP Server？**

- 开发一个MCP Server需要使用Anthropic的Model Context Protocol（MCP），它是一个开源标准协议，帮助AI模型与外部数据源和工具无缝连接。
- 推荐使用Python SDK，通过uv或pip安装，创建简单的服务器文件，并使用mcp dev命令本地运行。
- 该服务器可以作为HTTP服务运行，通常监听默认端口（如3000），用户可以通过HTTP请求与服务器交互。

MCP（模型上下文协议）服务器提供三种主要能力：资源、工具和提示词：

- 资源（Resources）资源是AI可以读取的数据，比如文件内容、数据库查询结果或API的响应。 例如，AI可能通过资源获取你的日历事件列表。
- 工具（Tools）工具是AI可以调用的函数，用于执行特定操作，比如添加新任务或发送邮件，使用工具时，通常需要用户先批准，以确保安全。
- 提示词（Prompts）提示词是服务器提供给AI的预写消息或模板，帮助AI理解如何使用资源和工具，例如，服务器可能告诉AI：“你可以添加任务，试试说‘添加任务：买牛奶’”，从而帮助用户更轻松地完成任务。提示词虽然直接提供给AI，但实际上是通过AI间接帮助用户，比如AI会根据提示词告诉用户如何操作。

![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

#### 安装与设置

安装MCP Python SDK，可以选择以下两种方式安装MCP Python SDK：

- 使用uv（推荐，速度更快）：运行uv add "mcp\[cli\]"。 uv是一个Rust编写的现代Python包管理器，相比传统pip更高效。

```c
curl -LsSf https://astral.sh/uv/install.sh | shuv add "mcp[cli]"
```

- 使用pip：运行pip install mcp。

#### 创建简单服务器

创建一个名为server.py的文件，内容如下：

```c
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("Simple Server")
@mcp.tool()def add(a: int, b: int) -> int:    """Add两个数字"""    return a + b
@mcp.resource("greeting://{name}")def get_greeting(name: str) -> str:    """获取个性化问候"""    return f"Hello, {name}!"
```

运行服务器，使用以下命令在开发模式下运行服务器：

```c
mcp dev server.py
```

![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

一个复杂一点的TODO MCP服务；

```c
import sqlite3from fastapi import HTTPExceptionfrom mcp.server.fastmcp import FastMCPimport atexitdb_conn = Nonedef init_db():    global db_conn    db_conn = sqlite3.connect("todo.db")    cursor = db_conn.cursor()    cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, description TEXT NOT NULL, completed INTEGER DEFAULT 0);")    db_conn.commit()init_db()def close_db():    if db_conn:        db_conn.close()atexit.register(close_db)mcp = FastMCP("To-Do List Server")@mcp.tool()def add_task(description: str) -> int:    if not description.strip():        raise ValueError("Task description cannot be empty")    cursor = db_conn.cursor()    cursor.execute("INSERT INTO tasks (description) VALUES (?);", (description,))    task_id = cursor.lastrowid    db_conn.commit()    return task_id@mcp.tool()def mark_task_completed(task_id: int) -> bool:    cursor = db_conn.cursor()    cursor.execute("UPDATE tasks SET completed=1 WHERE id=?;", (task_id,))    rows_affected = cursor.rowcount    db_conn.commit()    return rows_affected > 0@mcp.tool()def delete_task(task_id: int) -> bool:    cursor = db_conn.cursor()    cursor.execute("DELETE FROM tasks WHERE id=?;", (task_id,))    rows_affected = cursor.rowcount    db_conn.commit()    return rows_affected > 0@mcp.tool()def update_task_description(task_id: int, new_description: str) -> bool:    if not new_description.strip():        raise ValueError("Task description cannot be empty")    cursor = db_conn.cursor()    cursor.execute("UPDATE tasks SET description=? WHERE id=?;", (new_description, task_id))    rows_affected = cursor.rowcount    db_conn.commit()    return rows_affected > 0@mcp.resource("tasks://all")def get_all_tasks() -> list[dict]:    cursor = db_conn.cursor()    cursor.execute("SELECT id, description, completed FROM tasks;")    tasks = []    for row in cursor.fetchall():        tasks.append({"id": row[0], "description": row[1], "completed": bool(row[2])})    return tasks@mcp.resource("task_status://{task_id}")def get_task_status(task_id: int) -> dict:    cursor = db_conn.cursor()    cursor.execute("SELECT description, completed FROM tasks WHERE id=?;", (task_id,))    row = cursor.fetchone()    if row is None:        raise HTTPException(status_code=404, detail="Task not found")    return {"description": row[0], "completed": bool(row[1])}@mcp.resource("task_counts://{dummy}")def get_task_counts(dummy: str = "all") -> dict:    cursor = db_conn.cursor()    cursor.execute("SELECT COUNT(*) FROM tasks WHERE completed=0;")    incomplete_count = cursor.fetchone()[0]    cursor.execute("SELECT COUNT(*) FROM tasks WHERE completed=1;")    completed_count = cursor.fetchone()[0]    return {"incomplete": incomplete_count, "completed": completed_count}@mcp.prompt()def todo_list_prompt() -> str:    return """    You have access to a to-do list server. You can use the following tools and resources:    - Tool: add_task(description) -> int      - Adds a new task with the given description and returns the task ID.    - Tool: mark_task_completed(task_id) -> bool      - Marks the task with the given ID as completed and returns True if successful, False otherwise.    - Tool: delete_task(task_id) -> bool      - Deletes the task with the given ID and returns True if successful, False otherwise.    - Tool: update_task_description(task_id, new_description) -> bool      - Updates the description of the task with the given ID and returns True if successful, False otherwise.    - Resource: tasks://all      - Returns a list of all tasks, each with their ID, description, and completion status.    - Resource: task_status://{task_id}      - Returns the status of the task with the given ID, including its description and completion status.    - Resource: task_counts://{dummy}      - Returns a dictionary with the count of incomplete and completed tasks.    You can use these to manage your to-do list.    """
```

#### 调试服务器

![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

#### 部署MCP服务

- 部署MCP服务器可以选择本地运行、VPS或云平台，具体取决于使用场景。
- 确保服务器稳定、安全，并支持JSON-RPC和SSE协议。
- 使用mcp install server.py可为Claude Desktop安装服务器；对于通用部署，可用Uvicorn或Docker运行。
- 部署需配置HTTPS、限制访问，并设置监控和日志。

```c
sudo mcp install server.py
```

部署成功之后，可以看到Claude Desktop多了一个MCP的服务；

如果出现问题，可以在控制台中看到一些错误日志，然后进行修复。

![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

#### 问题与修复

1、错误与修复：uv命令找不到；

```c
2025-03-01T13:15:43.231Z [To-Do List Server] [info] Initializing server...2025-03-01T13:15:43.246Z [To-Do List Server] [error] spawn uv ENOENT {"context":"connection","stack":"Error: spawn uv ENOENT\n    at ChildProcess._handle.onexit (node:internal/child_process:285:19)\n    at onErrorNT (node:internal/child_process:483:16)\n    at process.processTicksAndRejections (node:internal/process/task_queues:82:21)"}2025-03-01T13:15:43.246Z [To-Do List Server] [error] spawn uv ENOENT {"stack":"Error: spawn uv ENOENT\n    at ChildProcess._handle.onexit (node:internal/child_process:285:19)\n    at onErrorNT (node:internal/child_process:483:16)\n    at process.processTicksAndRejections (node:internal/process/task_queues:82:21)"}2025-03-01T13:15:43.248Z [To-Do List Server] [info] Server transport closed2025-03-01T13:15:43.248Z [To-Do List Server] [info] Client transport closed
```

安装全局的uv

```c
brew install uv
```

2、依赖包没有找到

![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

方法 1：安装时指定依赖包

- 在运行 mcp install server2.py 时，使用 --with 选项指定所需的依赖包。例如：

```sql
mcp install server2.py --with fastapi
```

- 如果服务还依赖其他包（例如 uvicorn），可以用逗号分隔列出：

```sql
mcp install server2.py --with fastapi,uvicorn
```

- 运行后，MCP 会在隔离环境中自动安装这些包。

方法 2：在代码中声明依赖包

- 在你的服务代码 server2.py 中，使用 FastMCP 的 dependencies 参数指定依赖包。例如：

python

```javascript
from fastmcp import FastMCP
mcp = FastMCP("To-Do List Server", dependencies=["fastapi", "uvicorn"])
```

3、说无法打开数据库目录

![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

修改代码中可以打开的数据库目录；

db\_conn = sqlite3.connect("/Users/aihe/Desktop/Claude\_MCP\_3D\_Demo/todo.db")

  

**如何集成MCP Server？**

在这里可以看到支持MCP Server的客户端列表：

https://modelcontextprotocol.io/clients

#### Claude Desktop

```css
sudo mcp install server.py
```

然后就可以看到这个服务安装到了Claude Desktop的配置文件中；

![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

然后可以使用我们配置的MCP服务

![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

#### Cursor&Windsurf

配置在cursor和Windsurf也是可以的；

![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

#### 集成外部Mcp Server

- **mcp.so：** 社区驱动的平台，包含 1584 个服务器，适合发现和分享。
- **glama.ai/mcp/servers：** 列出 872 个开源 MCP 服务器，提供详细信息。
- **portkey.ai/mcp-servers：** 列出 42 个 MCP 服务器，专注于开源领域。
- **GitHub 仓库：** punkpeye/awesome-mcp-servers

比如我看到了一个playweight的mcp 服务；

![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

然后在本地做一下配置：

```json
{  "mcpServers": {    "playwright": {      "command": "npx",      "args": ["-y", "@executeautomation/playwright-mcp-server"]    }  }}
```

![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

然后本地可以使用这个对应的服务和工具；

![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

#### 客户端SDK集成

参考： https://github.com/modelcontextprotocol/python-sdk

```python
#!/usr/bin/env python3"""简单的 MCP 客户端示例连接到 server2.py 并演示 MCP 的基本功能"""import asyncioimport osimport jsonfrom mcp import ClientSession, StdioServerParametersfrom mcp.client.stdio import stdio_clientfrom typing import Optional, List, Dict, Any
# 创建连接到 server2.py 的参数server_params = StdioServerParameters(    command="python",     args=[os.path.join(os.path.dirname(os.path.abspath(__file__)), "server2.py")],    env=None  # 使用当前环境变量)
async def run():    """演示 MCP 客户端功能的主函数"""    print("正在连接到 MCP 服务器...")        async with stdio_client(server_params) as (read, write):        async with ClientSession(read, write) as session:            # 1. 初始化连接            await session.initialize()            print("✓ 已成功初始化连接")                        # 2. 获取可用的提示词            try:                prompts = await session.list_prompts()                print(f"可用的提示词: {prompts}")                                if prompts and prompts.prompts:                    # 3. 获取提示词内容                    try:                        prompt = await session.get_prompt(prompts.prompts[0].name)                        print(f"\n服务器提示词:\n{prompt}\n")                    except Exception as e:                        print(f"获取提示词内容时出错: {e}")            except Exception as e:                print(f"获取提示词列表时出错: {e}")                        # 4. 列出可用资源            try:                resources = await session.list_resources()                print(f"可用的资源: {resources}")            except Exception as e:                print(f"获取资源列表时出错: {e}")                resources = []                        # 5. 列出可用工具            try:                tools = await session.list_tools()                print(f"可用的工具: {tools}")            except Exception as e:                print(f"获取工具列表时出错: {e}")                tools = []                    
if __name__ == "__main__":    try:        asyncio.run(run())    except KeyboardInterrupt:        print("\n程序已被用户中断")    except Exception as e:        print(f"\n发生错误: {e}")    finally:        print("演示完成")
```

![图片](https://mp.weixin.qq.com/s/www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg%20stroke='none'%20stroke-width='1'%20fill='none'%20fill-rule='evenodd'%20fill-opacity='0'%3E%3Cg%20transform='translate(-249.000000,%20-126.000000)'%20fill='%23FFFFFF'%3E%3Crect%20x='249'%20y='126'%20width='1'%20height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

四、MCP 的未来畅想

想象一下未来的场景：

- 开发者不再需要从零开始写复杂的代码，只用几行配置就能快速搭出一个 AI 驱动的应用。比如，一个程序员想做一个“智能日程助手”，通过 MCP 直接调用日历服务和 AI 模型，半天就能上线。
- 普通用户甚至都不用会编程。就像点外卖一样，他们只需要在 Claude Desktop 上输入几行简单的指令，比如“帮我买点东西”，AI 就能通过 MCP 连接到购物服务，几分钟搞定。
- 服务商也能轻松转型。过去的老牌公司，比如物流商或银行，只需开放一个标准的 MCP 接口，AI 模型就能直接集成，用户点点鼠标就能用上服务，省去了繁琐的定制开发。

你只需轻声对 AI 说几句话，生活中的大小事务便能轻松搞定。比如：

- 购物：你说：“帮我买一箱牛奶和一些新鲜水果。” AI 通过 MCP 连接到电商平台，自动筛选最佳商品、下单、支付，甚至根据你的偏好安排次日送达。
- 健康管理：你说：“我最近睡眠不好。” AI 立刻调用健康服务，分析你的睡眠数据，推荐调整作息的建议，或者直接帮你预约睡眠专家。
- 旅行规划：你说：“我想下个月去意大利玩十天。” AI 会自动搜索最优机票、预订特色酒店、规划经典景点路线，还能根据天气预报提醒你带上雨伞。
- 美食体验：你说：“今晚我想吃中餐，但不想出门。” AI 迅速连接外卖平台，推荐附近评分最高的中餐厅，帮你点好菜送到家门口。
- 教育与工作：你说：“我需要准备明天的会议PPT。” AI 不仅能整理资料、生成幻灯片，还能根据你的风格润色内容；学生说：“我不会解二次方程。” AI 则会调用教育平台，提供步骤讲解和互动练习。

MCP 就像一个“AI 界的超级连接器”，把技术门槛拉低，让每个人都能玩转智能生活。

过去，使用软件需要复杂的下载、安装和配置，普通用户常常感到困难。

如今，MCP让这一切变得简单，只需几行配置就能完成。

这些场景的实现，只需与 AI 简单对话，MCP 就会像一个无形的桥梁，连接起各种服务，让繁琐的操作彻底消失。

AI 将成为你的“生活管家”，从日常购物到健康管理、旅行安排、美食享受，再到学习与工作，样样都能轻松应对。

五、总结

Claude 3.7 Sonnet 和 MCP，标志着 AI 从单纯的对话工具迈向了现实世界的执行者。

它不仅在编码、推理和任务执行上表现出色，还通过 MCP 这个“AI 万能接口”，让开发者快速构建应用，让普通人轻松调用服务，甚至让传统服务商无缝融入 AI 生态。

技术门槛的降低和功能的增强，正在为我们打开一个 AI 无处不在的未来...

MCP 可能不是完美的协议，但在大模型时代，它就像 AI 的“万能插头”，让模型能连上现实世界。未来，这种连接方式肯定会越来越聪明，让更多普通人轻松感受到 AI 的强大和便利。

我们平台正在积极探索面向未来的 AI 场景，想让 AI 变得更好玩、更实用，大家可以来体验下我们的平台...

- Spark AI 官网： https://aispark.alibaba-inc.com/
- AI应用搭建平台： https://appbuilder.alibaba-inc.com/

**参考资源：**

- https://www.anthropic.com/news/claude-3-7-sonnet
- https://www.anthropic.com/claude/sonnet#customer-stories
- https://assets.anthropic.com/m/785e231869ea8b3b/original/claude-3-7-sonnet-system-card.pdf
- https://modelcontextprotocol.io/clients
- https://github.com/modelcontextprotocol/python-sdk
- mcp.so：社区驱动的平台，包含 1584 个服务器，适合发现和分享。
- glama.ai/mcp/servers：列出 872 个开源 MCP 服务器，提供详细信息。
- portkey.ai/mcp-servers：列出 42 个 MCP 服务器，专注于开源领域。
- GitHub 仓库： punkpeye/awesome-mcp-servers

  

**构建高性能秒杀系统**

  

秒杀活动因其高流量和用户参与度，已成为电商平台的重要营销方式。本方案详细介绍如何利用阿里云产品构建高性能秒杀系统，以实现高并发处理，确保系统稳定和快速响应，从而为用户提供流畅的抢购体验。

  

点击阅读原文查看详情。

  

[阅读原文](https://mp.weixin.qq.com/s/) [阅读原文](https://mp.weixin.qq.com/s/) 继续滑动看下一个

向上滑动看下一个 [知道了](https://mp.weixin.qq.com/s/) ： ， ， ， ， ， ， ， ， ， ， ， ， 。 视频 小程序 赞 ，轻点两下取消赞 在看 ，轻点两下取消在看 分享 留言 收藏 听过