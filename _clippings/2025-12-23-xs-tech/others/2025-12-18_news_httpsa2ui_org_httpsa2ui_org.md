---
title: "2025-12-18_news_ycombinator_com_httpsa2ui_org_httpsa2ui_org"
source: "https://news.ycombinator.com/item?id=46286407"
author:
  - "[[@news.ycombinator.com]]"
published: 2025-12-18
created: 2025-12-18
description:
tags:
  - "#standard"
  - "news"
  - "@news.ycombinator.com"
  - "https"
---

# [httpsa2ui.org](httpsa2ui.org)

[https://a2ui.org/](https://a2ui.org/)

* * *

## Comments

> **codethief** • [2025-12-16](https://news.ycombinator.com/item?id=46287147)
> 
> \> A2UI 允许代理发送声明式组件描述，客户端使用自己的原生小部件进行渲染。这就像让代理说一种 *通用 UI 语言* 。
> 
> (emphasis mine)
> 
> 听起来，代理突然能够做到开发者几十年来一直未能实现的事情：编写跨平台用户界面。也许这适用于简单的用例，但除此之外我持怀疑态度。
> 
> > **rockwotj** • [2025-12-16](https://news.ycombinator.com/item?id=46287213)
> > 
> > 这不是正确的看待方式。这实际上是服务器端渲染，其中 LLM 负责生成标记语言，而不是使用模板。自定义 UI 通常是更高级别的。Airbnb 已经这样做了很多年：[https://medium.com/airbnb-engineering/a-deep-dive-into-airbn...](https://medium.com/airbnb-engineering/a-deep-dive-into-airbnbs-server-driven-ui-system-842244c5f5)
> > 
> > **observationist** • [2025-12-16](https://news.ycombinator.com/item?id=46292800)
> > 
> > 不，这只是同一个问题的换汤不换药，只不过这次是通过 API 和 CLI 来解决问题，而不是为了让 AI 完成人类能做的事情而费劲周折。
> > 
> > 这是关于完成任务，而非让机器人使用与人类相同的工具和具象化语境来完成任务——这样做没有任何优势，除非机器人实际上采用人形具象化。即便如此，在几乎所有情况下，使用命令行界面（CLI）和服务 API 都比使用用户界面（UI）更优，除非你想将能力限制在类人范围内（例如游戏场景），或者想欺骗监控者，让他们误以为是人类在操作。
> > 
> > 为现有 API 或自动化接口包裹一个 JSON 的 get/push 封装层，要比将某种 GUI 交互通用化无限容易得多。因为 LLM 没有你需要的实时记忆来实时适应所有边缘情况。这对人类来说极其困难，而且为了让软件实现通用可访问性并简化以适应用户，已经投入了数千亿美元，但最终结果要么是极其有限，要么是尾部出现分形复杂度，对于任何中等复杂度的软件，没有开发者能够考虑到用户与某个功能交互的所有可能方式。
> > 
> > 直接使用现有的自动化模式。这是一个案例，其中如果 AI 在获得这项能力以及其他进展的同时，那就太棒了；但任何类型的中间件都将成为一个巨大的权宜之计，并且会被前沿模型理所当然地立即淘汰。
> > 
> > **giancarlostoro** • [2025-12-16](https://news.ycombinator.com/item?id=46292342)
> > 
> > 我思考过如何编写一个跨平台的 UI 框架，这个框架不关心你用什么语言来编写它，每次我都觉得自己在重新发明 X.org，或者至少我的直觉告诉我，我只是在重新发明一个跨平台的 X 服务器实现。
> > 
> > **hurturue** • [2025-12-16](https://news.ycombinator.com/item?id=46290238)
> > 
> > 存在跨平台的用户界面——HTML 和 Electron
> > 
> > > **kridsdale3** • [2025-12-16](https://news.ycombinator.com/item?id=46291385)
> > > 
> > > 当然。HTML 是一种标记语言（它是一个首字母缩写词）。Markdown 也是一种标记语言。LLMs 非常擅长 Markdown，现在几乎所有的聊天机器人前端都内置了渲染器。
> > > 
> > > A2UI 是一个超集，扩展到更多的元素类型。如果我们要让所有数据流的源头是字符串输出生成器，这似乎是一个不错的做法。
> > > 
> > > 我已经加入了谷歌内部的一个项目，在这个特定领域开展工作，尽管我们正在做的事情没有计划开源，其他团队也在研究类似 A2UI 的项目，并且我们与他们合作。
> > > 
> > > 我之前的职业生涯有近 20 年是从事原生平台 UI 编程，像 Flutter、React Native 这类技术一直让我很不爽。但今年我开始接受，只要服务器端的 LLMs 将是未来应用的运行所在，我们就需要像这样的客户端-操作系统无关的框架。
> 
> **mentalgear** • [2025-12-16](https://news.ycombinator.com/item?id=46287728)
> 
> 它仍然需要特定于语言的库 \[1\]（而且 SvelteKit 甚至还没有宣布呢 :( ）
> 
> \[1\] [https://a2ui.org/renderers/](https://a2ui.org/renderers/)
> 
> > **ddrdrck\_** • [2025-12-16](https://news.ycombinator.com/item?id=46289412)
> > 
> > 嗯，它是开源的，他们期望社区添加更多的渲染器。所以如果你是 SvelteKit 专家，这实际上可能是一个机会。
> > 
> > > **epec254** • [2025-12-16](https://news.ycombinator.com/item?id=46289790)
> > > 
> > > +1！我们非常欢迎社区在此贡献！

> **awei** • [2025-12-16](https://news.ycombinator.com/item?id=46290082)
> 
> 我明白跨平台通用 UI 语言的实用性，但当我看到这个协议的一些示例时，我感觉它最终会趋同于我们已有的东西——HTML。与其让所有平台支持这种新的通用标记语言，不如让它们支持 HTML，因为有些平台已经支持 HTML 了，而且 LLMs 也已经在 HTML 上训练过。
> 
> { "id": "settings-tabs", "组件": { "Tabs": { "tabItems": \[ {"title": {"literalString": "General"}, "child": "general-settings"}, {"title": {"literalString": "Privacy"}, "child": "privacy-settings"}, {"title": {"literalString": "Advanced"}, "child": "advanced-settings"} \] } } }
> 
> { "id": "email-input", "component": { "TextField": { "label": {"literalString": "电子邮箱地址"}, "text": {"path": "/user/email"}, "textFieldType": "短文本" } } } }
> 
> > **epec254** • [2025-12-16](https://news.ycombinator.com/item?id=46290249)
> > 
> > HTML 面临的一个关键挑战是客户端信任问题。如何使代理平台（例如 Gemini、Claude、OpenAI）能够渲染来自与该平台集成的不受信任的第三方代理的 UI？这在这些应用的企业版中是一个常见场景——例如，我希望使用（插入 SaaS 供应商）的代理，同时使用我公司自主开发的代理和数据。
> > 
> > 大多数 HTML 实际上是 HTML+CSS+JS——依我之见，接受这种情况就如同等待一场即将发生的代码注入攻击。通过抽象为 JSON，客户端可以安全地渲染 UI，而无需担心这个问题。
> > 
> > > **lunar\_mycroft** • [2025-12-16](https://news.ycombinator.com/item?id=46290759)
> > > 
> > > 如果所讨论的 JSON 协议支持任意行为和样式，那么即使使用 JSON，你仍然会遇到注入问题。如果它不支持这些，那么你也不需要在 HTML 协议中支持这些，并且你可以以我们已有的方式解决注入问题：清理 HTML 以移除所有/部分（取决于你的具体需求）的脚本标签、事件监听器等。
> > > 
> > > **epicurean** • [2025-12-16](https://news.ycombinator.com/item?id=46291043)
> > > 
> > > 也许这个协议就是在严格沙箱中的 HTML/CSS/JS。组件无法访问组件边界之外的任何内容（没有网络访问，没有 DOM/对象访问，没有绘图访问等）。
> > > 
> > > > **awei** • [2025-12-16](https://news.ycombinator.com/item?id=46291887)
> > > > 
> > > > 我觉得你可以用 iframe 来实现，但这总是让我感到不安
> > 
> > **awei** • [2025-12-16](https://news.ycombinator.com/item?id=46290295)
> > 
> > 对，这很有道理。我在想，将 HTML 抽象为 JSON 是否是个好主意，这样就无法在其中包含 CSS 和 JS 了
> > 
> > > **epec254** • [2025-12-16](https://news.ycombinator.com/item?id=46290372)
> > > 
> > > 想了解更多你在想什么吗？
> > > 
> > > 一个挑战是你很可能希望 JavaScript 处理/捕获数据——例如，从表单中获取数据并将其转换为 JSON 以发送回代理
> > > 
> > > **oooyay** • [2025-12-16](https://news.ycombinator.com/item?id=46290406)
> > > 
> > > 如果你使用 A2UIs 生成器，它实际上就是这么做的，只是在你描述的内容之上多了一两个抽象层。
> > > 
> > > > **awei** • [2025-12-16](https://news.ycombinator.com/item?id=46290731)
> > > > 
> > > > 我浏览文档时也有同样的想法，我觉得既然它这么做是为了避免脚本注入（这很合理），那为什么不用“json 化的”HTML 来做呢？
> > > > 
> > > > > **oooyay** • [2025-12-16](https://news.ycombinator.com/item?id=46293766)
> > > > > 
> > > > > 我在想，原始 HTML 可能太冗长了，但预制组件有签名和类型。

> **mbossie** • [2025-12-16](https://news.ycombinator.com/item?id=46286990)
> 
> 所以我知道的有 MCP-UI、OpenAI 的 ChatKit 组件以及现在 Google 的 A2UI，可能还有更多...
> 
> 为了解决同样的问题，我们还要引入多少种变体？在我看来，这似乎浪费了大量工时。
> 
> > **MrOrelliOReilly** • [2025-12-16](https://news.ycombinator.com/item?id=46287082)
> > 
> > 我同意存在相互竞争的标准很烦人，但在面对大量未知情况时，允许差异化和探索会更好。当我们尚无有意义的数据来证明任何决策的合理性时，纠结于做事的最佳方式是一种*更糟糕的*时间浪费。企业需要自由去尝试这些新 AI 应用场景的最佳方法。然后我们就能了解每种方法的优劣。随着时间推移，我们应该预期并鼓励围绕单一标准集进行整合。
> > 
> > > **pscanf** • [2025-12-16](https://news.ycombinator.com/item?id=46287183)
> > > 
> > > 面对大量未知情况时，最好允许发散和探索
> > > 
> > > 我完全同意，不过我个人不参与这些协议/框架/库中的任何一个。6个月后，其中一半将会被弃用，另一半将会演变成完全不同且不兼容的东西。
> > > 
> > > 目前，我只是从零开始构建东西——正如其他人所指出的¹，这实际上并没有那么难，它能让你了解底层的运作原理，并且不会让你受制于他人的创新节奏（无论快慢）。
> > > 
> > > ¹ [https://fly.io/blog/everyone-write-an-agent/](https://fly.io/blog/everyone-write-an-agent/)
> > > 
> > > > **kridsdale3** • [2025-12-16](https://news.ycombinator.com/item?id=46291475)
> > > > 
> > > > 我最近听说，汽车刚出现时，美国很快就形成了有80个竞争汽车制造品牌的局面。几十年内，市场弄清楚了消费者真正想要什么、什么样的款式和功能是重要的，竞争格局最终整合为5个品牌。
> > > > 
> > > > 90 年代的 GPU 领域也出现了类似的情况。当 Jensen 创立 NVIDIA 时，市场上已有 70 家其他公司在销售可插入 PCI 插槽的显卡，而现在只剩下 2 家了。
> 
> **mystifyingpoi** • [2025-12-16](https://news.ycombinator.com/item?id=46287779)
> 
> 在我看来，这似乎浪费了很多工时
> 
> 听起来很多人因为这件事拿到了报酬。这对他们来说是个胜利。这不是他们的决定，而是公司决定参与这场竞赛。反正很可能会有不止一个赢家。
> 
> > **kridsdale3** • [2025-12-16](https://news.ycombinator.com/item?id=46291513)
> > 
> > 我就是这类人之一。我们必须在竞赛方宣布其存在前好几个月就开始着手解决这个问题。所以我们在这里都只是在进行并行演进。所有人都认为，坐以待标准意味着不会浪费精力，但也不会有任何影响力。
> > 
> > 就像你提到的，现在是就业的好时机。
> 
> **shireboy** • [2025-12-16](https://news.ycombinator.com/item?id=46289283)
> 
> AGUI 听起来类似： [https://github.com/ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui)
> 
> > **meander\_water** • [2025-12-16](https://news.ycombinator.com/item?id=46292489)
> > 
> > 这提供了更多关于它们之间关系的细节
> > 
> > [https://www.copilotkit.ai/ag-ui-and-a2ui](https://www.copilotkit.ai/ag-ui-and-a2ui)
> > 
> > **epec254** • [2025-12-16](https://news.ycombinator.com/item?id=46289806)
> > 
> > 同一个团队！AGUI 在内部使用 a2UI 作为协议。
> > 
> > > **swiftlyTyped** • [2025-12-17](https://news.ycombinator.com/item?id=46301923)
> > > 
> > > 你好，我是这里的 AG-UI 作者之一。
> > > 
> > > AG-UI 是 A2UI 的首发合作伙伴，但它是 CopilotKit 独立开发的项目，而非 Google。
> > > 
> > > 我们在 AG-UI 与 A2UI 之间进行了 Day-0 握手
> 
> **adamesque** • [2025-12-16](https://news.ycombinator.com/item?id=46293344)
> 
> 与许多专注于交付人类设计的静态用户界面的方法不同，这种方法似乎是一个旨在支持生成式用户界面的工具。我个人认为这行不通，目前更倾向于更渐进式的“让代理调用一个渲染特定预制用户界面的工具”的方法，比如 MCP UI/Apps、OpenAI Apps SDK 等。
> 
> **hobofan** • [2025-12-16](https://news.ycombinator.com/item?id=46288156)
> 
> MCP-UI 和 OpenAI 应用正在融合为 MCP Apps 扩展规范：[https://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-ap...](https://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps/)
> 
> **p\_v\_doom** • [2025-12-16](https://news.ycombinator.com/item?id=46288606)
> 
> 我们应该为所有人制定一个新标准...
> 
> **askl** • [2025-12-16](https://news.ycombinator.com/item?id=46287543)
> 
> 必须的 [https://xkcd.com/927/](https://xkcd.com/927/)

> **pedrozieg** • [2025-12-16](https://news.ycombinator.com/item?id=46287538)
> 
> 多年来，我们一直有类似“JSON 描述界面，客户端渲染它”的实现方式；困难之处不在于网络传输格式，而在于组件版本管理、在特定客户端出现故障时调试状态，以及不要因为使用过于精巧的布局 DSL 而陷入困境。
> 
> 真正有意思的部分在于安全边界：代理只能通过经过审核的组件目录来表达，而客户端负责执行。如果这一点处理得当，你可以将代理替换为规则引擎或人工操作员，同时保持相同的协议。我猜想，胜出的规范不会是那些拥有最酷演示的规范，而是那些足够乏味，以至于产品团队能够接受并使用5-10年的规范。

> **wongarsu** • [2025-12-16](https://news.ycombinator.com/item?id=46287365)
> 
> 我不会希望在任何接近生产环境的地方使用这个，但对于快速原型开发来说，这似乎很棒。众所周知，人们通常要等到开始尝试使用某个东西后，才能清晰表达自己的需求。这让你可以直接跳到你意识到他们想要的东西与最初描述的完全不同的那个阶段，而不必手动构建第一个迭代。
> 
> > **turnsout** • [2025-12-16](https://news.ycombinator.com/item?id=46290688)
> > 
> > 老实说，这个的目的不是为了帮助应用开发者——而是为了完全取代对应用的需求。
> > 
> > 这里的愿景是，你可以与 Gemini 聊天，而它可以即时生成一个应用来解决你的问题。对于可视化的景观设计应用，它只需通过景观设计师的 Google 商家资料与之连接。
> > 
> > 作为一名应用开发者，我实际上甚至不反对这一点。投入到创建和维护数千个重复应用中的人力是浪费的。
> > 
> > > **verdverm** • [2025-12-16](https://news.ycombinator.com/item?id=46292809)
> > > 
> > > 这听起来像是这些创作者认为，更多没人知道如何工作、甚至不知道代码长什么样的重复应用……是个更好的主意？
> > > 
> > > 用户需要多少次启动 GPU 来创建相同的应用程序？
> > > 
> > > > **turnsout** • [2025-12-16](https://news.ycombinator.com/item?id=46294071)
> > > > 
> > > > 如果谷歌在支付 GPU 时间费用，我想他们可以自行决定如何为常用查询缓存应用。很高兴我不用支付这个费用！

> **jy14898** • [2025-12-16](https://news.ycombinator.com/item?id=46286879)
> 
> 我永远不想在不知情的情况下使用一个以这种方式驱动的应用程序。
> 
> 不过，我很高兴它正在发生，因为使用该协议不需要 LLM。

> **skybrian** • [2025-12-17](https://news.ycombinator.com/item?id=46299251)
> 
> 似乎，如果每次按下按钮都需要等待到 LLM 的服务器端往返来更新用户界面，延迟会很高？
> 
> 在与 LLM 聊天的场景中，我认为用户会期望一定程度的延迟，但这在普通应用中是不受欢迎的。
> 
> 这也意味着很多其他的 UI 性能问题都无关紧要——反正表单提交本来就会很慢，所以只需对延迟情况保持透明即可。

> **tasoeur** • [2025-12-16](https://news.ycombinator.com/item?id=46286846)
> 
> 在一个理想的世界里，人们会首先实施 UI/UX 可访问性，而很多这些问题会被首先解决。但人们也可以希望，有动力让代理在这些方面运行起来，实际上能为新应用带来很多可访问性功能。

> **qsort** • [2025-12-16](https://news.ycombinator.com/item?id=46286865)
> 
> 如果使用得当，这非常有趣。我能看到很多用例，在这些用例中我希望界面能够动态绘制（例如用于商业智能的图表）。
> 
> 让我感到害怕的是，即使没有任意代码生成，仍然存在幻觉和提示注入造成严重影响的可能性，如果类似这样的解决方案没有得到适当的沙箱化处理。就像示例中展示的那样，一个自动生成的“确认购买”按钮……我可能不会在目前就完全不加监督地生成这样的东西。

> **jadelcastillo** • [2025-12-16](https://news.ycombinator.com/item?id=46291645)
> 
> 我认为这是一种良好且务实的方法来处理 LLM 系统的使用。通过将其转换为中间语言，然后进行进一步的符号化处理。但可能如果向 LLM 暴露敏感的‘工具’，你也可能会受到提示注入攻击。

> **ceuk** • [2025-12-16](https://news.ycombinator.com/item?id=46288479)
> 
> 几天前，我向一些同事预测，围绕“server-driven UI”的理念将会复兴（这个概念从未真正流行起来），以便促进 agent 驱动的用户界面的发展。
> 
> 感觉很不错，因为我之前的判断是准确的，但我也庆幸自己没有一开始就启动一个项目，结果却被谷歌直接盯上
> 
> > **kridsdale3** • [2025-12-16](https://news.ycombinator.com/item?id=46291546)
> > 
> > 服务端驱动的 UI（SDUI）已经完全流行起来了。不包括所有的 Electron 应用，像 Instagram 的原生移动应用目前大约有一半的界面都采用了 SDUI，因为 Meta 需要能够即时更改这些界面，而不是需要 3 周的发布周期。
> > 
> > > **ceuk** • [2025-12-17](https://news.ycombinator.com/item?id=46299648)
> > > 
> > > 没想到 Instagram 用了这个，真酷

> **iristenteije** • [2025-12-16](https://news.ycombinator.com/item?id=46287886)
> 
> 我认为归根结底，GenUI 可以更无缝地集成到应用中，但即便现在它更多还是在带提示的聊天界面场景中，我认为很明显，大段文字并非总是最佳的用户体验/输出方式，而这已经是一个成功了。

> **uptownhr** • [2025-12-16](https://news.ycombinator.com/item?id=46289858)
> 
> 我的方法/原型使用 XState 和 websockets，来自一个 MCP 服务器 [https://github.com/uptownhr/mcp-agentic-ui](https://github.com/uptownhr/mcp-agentic-ui)

> **oddrationale** • [2025-12-16](https://news.ycombinator.com/item?id=46289993)
> 
> 看起来类似于 \[Adaptive Cards\](https://adaptivecards.io/)。两者都有一个基于 JSON 的 UI 构建系统。

> **barbazoo** • [2025-12-16](https://news.ycombinator.com/item?id=46289582)
> 
> 这听起来像是一种让 LLM 客户端渲染动态 UI 的方式。这是用于聊天会话期间，还是又一种构建实际应用程序的方式？
> 
> > **epec254** • [2025-12-16](https://news.ycombinator.com/item?id=46289765)
> > 
> > 这里是谷歌的产品经理。目前，它被设计用于与聊天对话内联渲染 UI 组件——这是 a2a 的一个扩展，除了聊天消息外，还允许你流式传输定义 UI 组件的 JSON 数据。
> > 
> > > **kridsdale3** • [2025-12-16](https://news.ycombinator.com/item?id=46291561)
> > > 
> > > 谷歌软件工程师在这个领域工作。在 Moma 上查找我的用户名（去掉数字），我们聊聊。我无法从你的黑客新闻用户名识别你。

> **\_pdp\_** • [2025-12-16](https://news.ycombinator.com/item?id=46287420)
> 
> 我喜欢用 Markdown 来描述用户界面。
> 
> 它简单、有效，并且对我来说比一些为非常特定的用例设计的僵化数据结构更自然，而这些用例可能不太适合你自己的问题。
> 
> 说实话，在使用 LLMs 时，我们应该考虑 Emacs，并尝试应用类似的理念。我本身并不喜欢 Emacs，但其中存在相似之处。一切都是文件，一切都是缓冲区中的文本。文本可以根据使用者以不同方式呈现。
> 
> 这也是我们在自己产品中采用的理念，并且对各类客户都非常有效。我还没有遇到任何无法用这种方式建模的情况。它简单、有效，并且在事情不如预期时能提供极大的灵活性。它在流式处理方面也表现出色（流式解析器对于简单的文本结构来说并不难实现，而且我们已经这样做了很长时间），并且 LLMs 被训练得非常好，能够生成这类输出——相比之下，任何尚未被任何人见过或采用的定制化内容都无法与之相比。
> 
> 此外，考虑到 LLMs 在编程方面越来越擅长，且浏览器可以以无缝模式渲染 iframe，一种更好且更灵活的方法是使用 HTML、CSS 和 JavaScript，而非 Slack 长期以来使用的 Block Kit API（我们知道这种方式非常僵化，使用起来很令人沮丧）。我理解你可能希望为 UI 设计一种数据结构，以便同时支持 CLI 工具，但归根结底，浏览器和 CLI 是完全不同的东西，我认为你无法有效地让它们同时工作，除非你也准备简化它，并且只针对最低公分母。

> **raybb** • [2025-12-16](https://news.ycombinator.com/item?id=46287014)
> 
> 像 Cline 这样的工具有时会给你提供可点击的多选按钮，针对这种情况是否有标准协议？或者这种方式与类似的事物相比如何？

> **evalstate** • [2025-12-16](https://news.ycombinator.com/item?id=46287157)
> 
> 我挺喜欢这个的外观——似乎介于 MCP Elicitations 的刚性结构和 MCP-UI/Skybridge 的自由形式的特性之间。

> **zwarag** • [2025-12-16](https://news.ycombinator.com/item?id=46289753)
> 
> 这可能是允许设计师在 Figma 中设计 UI 并让代理通过 A2UI 构建它的链接吗？

> **mentalgear** • [2025-12-16](https://news.ycombinator.com/item?id=46287721)
> 
> 实现这一点的方法是共同努力设计一个类似 W3C 的通用标准。

> **ChrisArchitect** • [2025-12-16](https://news.ycombinator.com/item?id=46291076)
> 
> A2UI：一种面向代理驱动接口的协议 | Hacker News

> **verdverm** • [2025-12-16](https://news.ycombinator.com/item?id=46292959)
> 
> 我对数据流的第7部分理解正确吗？
> 
> 建立 SSE 连接
> 
> ... user event
> 
> 7\. 通过源 SSE 连接发送更新
> 
> 那么客户端是否需要在整个聊天会话期间保持一个支持 SSE 的连接？如果我的网络中断或切换到另一个代理该怎么办？
> 
> 维持会话在整个生命周期内的连接似乎是一个繁重的要求，而会话的生命周期可能长达数天（正如一些人告诉我们的，他们已经对代理这样做过）

> **empath75** • [2025-12-16](https://news.ycombinator.com/item?id=46288940)
> 
> 我无法让默认模型正常工作，因为它过载了，但我尝试了 flash-lite，它至少给了我一个响应。不过，当我在演示中尝试建议的问题时，它只有三分之一的时间会显示实际的 UI，否则它会尝试向我提问，既不显示界面，甚至在应用中也不执行任何操作——我不得不查看日志才能了解它试图做什么。

> **nsonha** • [2025-12-16](https://news.ycombinator.com/item?id=46287688)
> 
> 这其中有什么代理/AI 特有的地方？看起来只是后端驱动的用户界面

> **lowsong** • [2025-12-16](https://news.ycombinator.com/item?id=46287276)
> 
> A2UI 允许代理发送声明式组件描述，客户端使用它们自己的原生组件进行渲染。这就像让代理使用一种通用的 UI 语言。
> 
> 到底为什么会有人想要这个？你究竟为什么会信任一个 LLM 来生成 UI？你这简直是在*自找*安全漏洞、UI 冒充攻击、糟糕的可用性等等。这简直是一场噩梦。
> 
> > **vidarh** • [2025-12-16](https://news.ycombinator.com/item?id=46287482)
> > 
> > 如果在聊天中进行，这只是一种与你自由交谈的替代方式。例如，考虑 Claude Code 的选择题，你可以通过让它调用合适的工具来触发这些题目。
> > 
> > > **DannyBee** • [2025-12-16](https://news.ycombinator.com/item?id=46287868)
> > > 
> > > 没有任何问题会仅仅因为是在聊天中就消失？
> > > 
> > > Freeform 看起来和表现得像文本，只是有一些经过专人审核并使其可用的特性。
> > > 
> > > 如果您现在点击的交互式图表或用户界面控制你，那么无论它是在聊天窗口内还是聊天窗口外都没关系。
> > > 
> > > 现在，在这种情况下，这不是随意的 UI，而是如果你认为这些组件的解析/验证/渲染/双向数据绑定/增量组合（该规范要求你能够增量构建 UI）：[https://a2ui.org/specification/v0.9-a2ui/#standard-component...](https://a2ui.org/specification/v0.9-a2ui/#standard-component-catalog)
> > > 
> > > 由 N×M 实现组合（目前有 4 个渲染器和大量传输方式）传输/渲染等，不会存在安全问题——我这儿有座桥要卖给你。
> > > 
> > > 在这里，我用 Gemini 向你介绍它，在你签名之前，只需帮我点击几次“完全安全的文本框”。
> > > 
> > > 我的朋友曾经把某样东西叫做 babydoggle——你知道那最终会是个 boondoggle，但它仍处于早期的形成阶段。
> > > 
> > > 这对我来说感觉像个幼稚的玩意儿。
> > > 
> > > > **vidarh** • [2025-12-16](https://news.ycombinator.com/item?id=46289498)
> > > > 
> > > > 这些问题不会仅仅因为是在聊天中就消失？
> > > > 
> > > > 我在与 Claude 的对话基础上点击 Claude 聊天中提供的按钮，和点击随机网站上的随机按钮，这两者在风险上有巨大差异。两者都可能包含恶意内容。其中一个的风险要大得多。另外，将这样构建的用户界面与代理关联，并允许第三方与之交互，对你来说比对他们来说要危险得多。
> > > > 
> > > > 如果您现在点击的交互式图表或用户界面支配了你，那么它是在聊天窗口内还是在聊天窗口外都无关紧要。
> > > > 
> > > > 在那种情况下，UI 元素是无关紧要的，除非实现存在缺陷（是的，我已经阅读了其余内容，见下文），因为你只需向用户提供一个基本链接并告诉他们点击它，就能实现同样的功能。
> > > > 
> > > > 由 N×M 种实现方式组合（目前有 4 个渲染器和多种传输方式）进行传输/渲染等操作的内容，不会存在安全问题，我这儿有座桥要卖给你。
> > > > 
> > > > 我非常怀疑我们会看到很多不会仅仅为此使用 web view 的实现，并且我非常怀疑这些问题甚至会跻身人们在使用 AI 工具时遇到的十大安全问题之列。当然，会有漏洞。你可以用这个论点来反驳任何需要对客户端软件进行修改的情况。
> > > > 
> > > > 但如果你担心客户端的安全性，mcp 和 hooks 由于其设计方式，本质上存在风险，是一个远更复杂的一团乱麻。

> **mannanj** • [2025-12-16](https://news.ycombinator.com/item?id=46290974)
> 
> 我希望不是被告诉“这是我认为你想看到的，现在看看吧”，而是被问“你想看什么？”并被展示那个。
> 
> 是的，我们确实声称用户不知道自己想要什么。我认为这在很大程度上被用作逃避重新思考如何让产品满足用户需求的借口，并且维持现状——让人们依赖系统和围墙花园（walled gardens）。这篇文章的目标是让用户界面（UIs）更好地服务于用户。那么，还有什么比让用户在界面中进行想象（或者甚至通过示例操作、按钮、点击文本来引导他们渲染特定视图）更好的方式呢！我一直想构建一个这样的东西：我只需用英语从已知的选项中提问，或者通过尝试和探索边界来发现什么是可能的，什么是不可能的。
> 
> 还有其他人也朝这个方向思考吗？或者我是不是忽略了什么明显的东西？

> **alexgotoi** • [2025-12-16](https://news.ycombinator.com/item?id=46290979)
> 
> 所以我们正在重新发明 SOAP，不过是针对 AI 代理的。这并不是说这有什么不好——有时候你需要先重新经历旧的错误，才能弄明白什么才真正有效。
> 
> 真正的问题是：UI 对智能体（agents）来说是否还有意义？毕竟 UI 的核心目的是在人类的限制条件（屏幕、鼠标、注意力）下暴露功能。智能体没有这些限制条件，它们可以读取 JSON、直接调用 API、解析文档。我们为什么要为它们构建中间件来让它们点击按钮？
> 
> 我认为在我们弄清楚 agent-native 架构是什么样子的过程中，这作为一个过渡层是合理的。但从长远来看，这可能只是辅助轮。
> 
> 我会把这个包含在我的 [https://hackernewsai.com/](https://hackernewsai.com/) 新闻通讯中。
> 
> > **kridsdale3** • [2025-12-16](https://news.ycombinator.com/item?id=46291438)
> > 
> > 这里的需求在于，代理在某个时刻必须生成一种输出，这种输出会被有视觉的人类所消费。屏幕上的像素网格向人类传递信息的带宽，远比线性文本串高得多。