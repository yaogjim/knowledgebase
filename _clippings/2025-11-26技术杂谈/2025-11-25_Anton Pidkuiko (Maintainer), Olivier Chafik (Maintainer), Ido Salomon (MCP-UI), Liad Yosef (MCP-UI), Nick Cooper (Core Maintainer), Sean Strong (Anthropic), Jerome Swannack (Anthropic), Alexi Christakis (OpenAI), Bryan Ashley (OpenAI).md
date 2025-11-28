---
title: "MCP Apps: Extending servers with interactive user interfaces"
source: "https://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps/"
author:
  - "[[Anton Pidkuiko (Maintainer)]]"
  - "[[Olivier Chafik (Maintainer)]]"
  - "[[Ido Salomon (MCP-UI)]]"
  - "[[Liad Yosef (MCP-UI)]]"
  - "[[Nick Cooper (Core Maintainer)]]"
  - "[[Sean Strong (Anthropic)]]"
  - "[[Jerome Swannack (Anthropic)]]"
  - "[[Alexi Christakis (OpenAI)]]"
  - "[[Bryan Ashley (OpenAI)]]"
published: 2025-11-25
created: 2025-11-25
description: "Today we’re introducing the proposal for the MCP Apps Extension (SEP-1865) to standardize support for interactive user interfaces in the Model Context Protocol.This extension addresses one of the most requested features from the MCP community and builds on proven work from MCP-UI and OpenAI Apps SDK - the ability for MCP servers to deliver interactive user interfaces to hosts.MCP Apps Extension introduces a standardized pattern for declaring UI resources, linking them to tools, and enabling bidirectional communication between embedded interfaces and the host application."
tags:
  - "Anton Pidkuiko (Maintainer)"
  - "Olivier Chafik (Maintainer)"
  - "Ido Salomon (MCP-UI)"
  - "Liad Yosef (MCP-UI)"
  - "Nick Cooper (Core Maintainer)"
  - "Sean Strong (Anthropic)"
  - "Jerome Swannack (Anthropic)"
  - "Alexi Christakis (OpenAI)"
  - "Bryan Ashley (OpenAI)"
---
今天我们推出 [MCP 应用扩展](https://github.com/modelcontextprotocol/ext-apps) （ [SEP-1865](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1865) ）提案，旨在为模型上下文协议中的交互式用户界面提供标准化支持。

这项扩展解决了 MCP 社区最迫切需求的功能之一，并基于 [MCP-UI](https://github.com/idosal/mcp-ui) 和 [OpenAI Apps SDK](https://developers.openai.com/apps-sdk/) 的成熟成果—— **使 MCP 服务器能够向主机交付交互式用户界面** 。

MCP 应用扩展引入了一种标准化模式，用于声明 UI 资源、将其与工具链接，并实现嵌入式界面与宿主应用之间的双向通信。

![Example of an inline chat app with interactive UI for permission management](https://blog.modelcontextprotocol.io/posts/images/inline-chat-app.png)

该 SEP 由 OpenAI 和 Anthropic 的 MCP 核心维护者，与 MCP-UI 创建者及 MCP UI 社区工作组的主要维护者共同撰写。

## 交互式界面的标准化

目前，MCP 服务器仅限于与主机交换文本和结构化数据。虽然这在许多应用场景中表现良好，但当工具需要呈现可视化信息或收集复杂用户输入时，这种限制就会造成操作障碍。

例如，设想一个数据可视化 MCP 服务器，它返回 JSON 格式的图表数据。宿主应用程序必须解析这些数据并进行渲染。在这种情况下，处理各种专业数据对客户端开发者而言意味着沉重负担——他们需要构建自己的逻辑来渲染界面。随着更多界面需求的出现（比如需要从用户处收集多个相关设置），复杂度会急剧膨胀。反之，若缺乏界面支持，这些交互就会退化为笨拙的文本提示与回复的来回传递。

MCP 社区在应对这些限制方面展现了创造力，但不同实现方案采用各异的约定和架构，导致服务器难以在不同客户端间保持稳定运行。这种标准化缺失带来了生态系统碎片化的切实风险——我们正积极采取措施防范这一局面。

## Building together

由 [Ido Salomon](https://github.com/idosal) 和 [Liad Yosef](https://github.com/liady) 创建、并由热心社区维护的 [MCP-UI 项目](https://github.com/MCP-UI-Org/mcp-ui) ，率先实现了具有交互界面的智能体应用愿景。该项目开创了将丰富用户界面作为一等 MCP 资源的交付模式，证明了智能体应用能天然融入 MCP 架构。该项目拥有庞大社区支持，提供 [功能丰富的 SDK](https://mcpui.dev/guide/client/overview) ，已被 Postman、Shopify、Hugging Face、Goose 和 ElevenLabs 等领先企业与项目采用。

[OpenAI 应用软件开发工具包](https://developers.openai.com/apps-sdk/) 进一步验证了对话式人工智能界面对丰富用户体验的需求。该工具包使开发者能够以 MCP 为底层框架，在 ChatGPT 内部构建丰富交互式应用。为确保生态系统的互操作性并建立统一的安全及使用规范，Anthropic、OpenAI 与 MCP-UI 正携手开发面向交互界面的官方 MCP 扩展。

![Example of a fullscreen app with a rich data table interface](https://blog.modelcontextprotocol.io/posts/images/fullscreen-chat-app.png)

## MCP Apps 扩展规范

我们正在为 MCP 提出一套 UI 资源规范，但其意义远不止于一系列模式变更。MCP 应用扩展正逐渐显现出智能应用运行时的雏形：一个为 AI 模型、用户与应用程序之间实现创新交互奠定基础的系统。该提案有意保持精简，从核心模式起步，计划在未来逐步扩展完善。

### 关键设计决策

#### 预声明资源

UI 模板是采用 `ui://` URI 方案的资源，在工具元数据中进行引用。

这种方法使主机能够在工具执行前预取和审阅模板，从而提升性能和安全性。同时，它将静态呈现（模板）与动态数据（工具结果）分离开来，实现了更高效的缓存。

#### MCP 通信传输协议

UI 组件无需自定义消息协议，而是通过现有的 MCP JSON-RPC 基础协议，借助 `postMessage` 与宿主进行通信。这意味着：

- UI 开发者可以使用标准的 `@modelcontextprotocol/sdk` 来构建他们的应用程序
- 所有通信都经过结构化处理且可审计
- 未来的 MCP 功能将自动适配 UI 扩展

#### Starting with HTML

最初的扩展规范仅支持 `text/html` 格式内容，通过沙盒化的 [iframe](https://developer.mozilla.org/docs/Web/HTML/Reference/Elements/iframe) 进行渲染。这种设计具备以下特性：

- 通用浏览器支持
- 完善的安全模型
- 截图与预览生成功能
- 为未来扩展奠定清晰基准

其他内容类型，如外部 URL、远程 DOM 和原生小部件，已明确推迟至未来版本中实现。

#### Security-first

托管来自 MCP 服务器的交互式内容需要谨慎考虑安全性。该提案通过多层防护机制应对这一问题：

1. **iframe 沙盒隔离** ：所有 UI 内容均在权限受限的沙盒化 iframe 中运行
2. **预声明模板** ：主机可在渲染前审查 HTML 内容
3. **可审计消息** ：所有用户界面与主机间的通信均通过可记录日志的 JSON-RPC 协议进行
4. **用户同意** ：主机可要求对界面发起的工具调用进行明确授权

这些缓解措施构建了纵深防御体系，既能防范恶意服务器攻击，又保留了开发者所需的灵活性。

#### 向后兼容性

MCP Apps 是一项可选扩展。现有实现方案无需改动即可继续运行，宿主端可根据自身节奏逐步适配 UI 支持。服务端应为所有支持 UI 的工具提供纯文本回退方案，确保即便在 UI 不可用时也能返回有意义的内容，从而同时兼容支持 UI 和纯文本的宿主环境。

## 接下来是什么

[UI 社区工作组](https://github.com/modelcontextprotocol-community/working-groups/issues/35) 通过大量反馈和讨论，为这份提案的成型发挥了关键作用。我们构建了 [早期体验版 SDK](https://github.com/modelcontextprotocol/ext-apps) 来演示规范提案中描述的模式与类型。 [MCP-UI](https://mcpui.dev/) 客户端及服务端 SDK 均支持这些模式。

若您有意为此贡献力量，我们诚邀您：

- 在 [SEP-1865](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1865) 中查阅完整规范
- 在 [GitHub Issues](https://github.com/MCP-UI-Org/mcp-ui/issues) 中分享反馈和疑虑
- 加入 [MCP 贡献者 Discord](https://modelcontextprotocol.io/community/communication#discord) 的 `#ui-wg` 频道参与讨论
- 测试原型实现并分享您的体验

## Acknowledgements

没有 MCP-UI、OpenAI 和 Anthropic 维护者的工作，这项提案就不可能存在。

**伊多·所罗门** 和 **利亚德·约瑟夫** 通过 MCP-UI 项目及 `#ui-wg` 频道管理，孵化并倡导了诸多如今被 MCP 应用标准化的交互模式，他们与贡献者们共同证明了用户界面资源能够自然而然地融入 MCP 体系。

**肖恩·斯特朗** 、 **奥利维尔·查菲克** 、 **安东·皮德库伊科** 和 **杰罗姆·斯万纳克** 来自 Anthropic，他们共同引导这项倡议并推动合作。

OpenAI 的 **Nick Cooper** 、 **Alexei Christakis** 和 **Bryan Ashley** 根据他们构建 Apps SDK 的经验提供了宝贵的指导。

特别感谢 **UI 社区工作组** 成员以及所有参与讨论、共同完善此提案的贡献者。