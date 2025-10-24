---
title: "The Trillion Dollar AI Software Development Stack"
source: "https://a16z.com/the-trillion-dollar-ai-software-development-stack/"
author:
  - "[[Guido Appenzeller]]"
  - "[[Yoko Li]]"
published: 2025-10-24
created: 2025-10-24
description: "Generative AI is revolutionizing software development, with AI coding assistants and agentic tools transforming how 30 million developers plan, code, review, and deploy software worldwide. From productivity gains worth trillions in global GDP to a fast-evolving startup ecosystem, the AI coding revolution is reshaping the future of programming and software creation."
tags:
  - "Guido Appenzeller"
  - "Yoko Li"
---
[![An AI image of a man sitting at a laptop with humanoid robots behind him.](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/10/250918-Trillion-Dollar-AI-Software-Dev-Stack-Social-img-1200x630-1.png)](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/10/250918-Trillion-Dollar-AI-Software-Dev-Stack-Social-img-1200x630-1.png)

聆听 Guido 和 Yoko 在 **万亿美元人工智能软件开发技术栈** 上的对谈，请通过 [Apple](https://podcasts.apple.com/us/podcast/the-trillion-dollar-ai-software-development-stack/id1740178076?i=1000731186101) 或 [Spotify](https://open.spotify.com/episode/7HmrrFtFuPUybTuvZCpJ4p) 收听。

生成式人工智能已经到来，而首个崛起的巨大市场正是软件开发领域。乍看之下，这或许令人惊讶。从历史上看，开发工具的市场规模从未跻身顶级软件品类之列。但细究起来，这一发展趋势完全合乎逻辑，原因有二：一是开发者往往最先为自己打造工具，二是其潜在市场体量异常庞大。

试想：全球约有 3000 万软件开发者，估算范围从 Evans Data 的 2700 万到 SlashData 的 4700 万不等。若假设每位开发者每年创造 10 万美元的经济价值——这个数字对美国而言或许保守，但略高于全球平均水平——那么人工智能软件开发每年创造的经济价值总额高达 3 万亿美元。根据过去 12 个月与企业和软件公司的数十次交流，我们估算目前一个简易的 AI 编程助手能使开发者的工作效率提升约 20%。

但这仅仅是个开始。根据实际案例估算，最佳实践的人工智能部署至少能将开发者的生产力提升一倍，从而每年为国内生产总值贡献 3 万亿美元。 ***这几乎相当于法国的全年国内生产总值*** 。硅谷及其他地区的少数初创企业所研发的技术，对全球 GDP 产生的影响将超越世界第七大经济体全体居民创造的生产总值总和。

巨大的价值创造带来了初创企业营收和估值的同等巨幅增长。Cursor 在 15 个月内 [实现了 5 亿美元年经常性收入，估值逼近 100 亿美元](https://cursor.com/blog/series-c) 。谷歌斥资 24 亿美元通过人才收购抢在 OpenAI 之前拿下 Windsurf。Anthropic 推出 Claude Code 并向其主要分发渠道——AI 开发工具宣战。而 OpenAI 的 GPT-5 发布更是全面聚焦编程领域。当如此规模的奖赏近在眼前，我们已然步入 AI 软件开发的战国时代。

起初，人工智能编程似乎只是一个单一领域，但如今已发展成一个生态系统，有望孕育出数十家价值数十亿美元的企业，甚至催生万亿美元巨头。过去几十年间，软件一直是人类进步和经济增长的主要驱动力。它颠覆了所有行业，而现在软件本身也正经历颠覆。借助 AI 加速开发，以及将模型作为软件新基石的“双重助推”，很可能推动软件市场在质与量上实现大规模扩张——相应的市场规模也将水涨船高（我们认为此场景下 [杰文斯悖论](https://en.wikipedia.org/wiki/Jevons_paradox) 依然成立）。

人工智能编程技术栈将呈现何种面貌？尽管尚处早期阶段，下图尝试展示我们当前的观察。橙色标注区域代表多个初创公司集群正在构建基于人工智能工具的领域，每个类别列举了一个示例。更多案例以及与开发流程正交的附加类别已在下方的市场生态图中列出。

[![A flowchart showing the AI Software Development process](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/10/250918-Trillion-Dollar-AI-ILG-1-r3.png)](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/10/250918-Trillion-Dollar-AI-ILG-1-r3.png)

## 基本循环：规划 -> 编码 -> 审查

十八个月前，早期的 AI 编程还停留在向 LLM 请求特定代码片段，再将生成代码粘贴至源码的阶段，如今看来已显陈旧。现今的工作流有时被称为 ***规划→编码→审查*** ：从需求起始就引入 LLM 参与——先详细描述新功能特性，继而明确需要决策的要点或缺失信息；代码生成通常由智能体循环完成，可能包含测试环节；最终开发者审阅 AI 产出并作必要调整。

[![A graphic with examples of the AI breaking down a high-level specification and asking questions](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/10/250918-Trillion-Dollar-AI-ILG-2-scaled.png)](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/10/250918-Trillion-Dollar-AI-ILG-2-scaled.png)

上图展示的是一个启动新项目的简单工作流程示例。该模型的任务是草拟一份高层规范——但更重要的是，它被要求返回一份所需补充信息的详尽清单。在此案例中，这份清单长达数页，涵盖了对一系列需求及架构决策的澄清说明，还包括申请 API 密钥以及获取必要工具和系统访问权限的要求，以确保顺利完成任务。

最终形成的规范具有双重作用：最初，它指导代码生成，确保设计意图与实现保持一致。但更重要的是，规范对于确保人类或 LLMs 在大型代码库中持续理解特定文件或模块的功能至关重要。人机协作是迭代式的：当人类开发者修改某段代码后，他们通常会指示语言模型同步更新项目规范——从而确保最新的代码变更得到准确反映。这种机制最终产出的高质量文档化代码，将使人类开发者和语言模型同时受益。

[![Image of Cursor Directory, a library of coding guidelines for LLMs](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/10/250918-Trillion-Dollar-AI-ILG-3.png)](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/10/250918-Trillion-Dollar-AI-ILG-3.png)

**除了项目特定需求外，大多数 AI 编程系统现已纳入全面的架构与编码规范（例如 .cursor/rules ）** 。这些规范可能涵盖公司全局、项目专属乃至模块级别的规则。我们正目睹针对特定使用场景的 AI 优化编码最佳实践在线合集（如上文示例，更多内容可参阅 [GitHub 链接](https://github.com/PatrickJS/awesome-cursorrules) 或 Claude Code [此处链接](https://github.com/brennercruvinel/CCPlugins) ），这些资源完全面向 LLMs 设计。我们正在见证首批纯粹为 AI 而非人类设计的自然语言知识库的诞生。

在这一新范式中，人工智能已超越其仅作为响应提示的代码生成器的传统角色。LLMs 如今成为真正的协作伙伴，帮助开发人员驾驭设计与实施阶段，协助制定架构决策，并识别潜在风险或限制。这些系统具备丰富的上下文理解能力，涵盖公司政策、项目特定指引、第三方最佳实践以及全面的技术文档。

用于 AI 规划的工具仍处于早期阶段。多家行业巨头和初创公司已开发出能聚合论坛、Slack、电子邮件或 Salesforce 和 Hubspot 等 CRM 系统客户反馈的应用程序（例如 [Nexoro](https://nexoro.ai/) ）。另一类公司（如 [Delty](https://www.delty.ai/) 或 [Traycer](https://traycer.ai/) ）则开发网站或 VS Code 插件，协助将需求规范拆解为详细用户故事，并优化工单流程（例如 [Linear](https://linear.app/) ）。展望未来，维基和故事跟踪器等现有记录系统显然也需要彻底改造或完全替代。  

## 生成与审查代码

一旦制定了周密的计划，我们便进入迭代循环：AI 编程助手生成代码，开发者进行审查。最佳用户界面与集成点的选择主要取决于任务长度及其是否需要异步运行。

**基于聊天的文件编辑** 允许用户通过聊天向 AI 提供提示和必要上下文。这种方法利用具备大上下文窗口的强大推理模型，可跨整个代码库工作，并经常使用基础工具进行文件创建或添加软件包。该系统可集成在集成开发环境中，或通过网页界面访问，为用户提供每次操作的实时反馈。

**后台智能体** 的运作方式有所不同，它们能在没有直接用户交互的情况下长时间持续工作。这类智能体通常采用自动化测试来确保解决方案的准确性——由于缺乏即时用户反馈，这一机制显得尤为重要。最终产出可能是经过修改的代码树，或是提交至代码仓库的拉取请求。典型代表包括 [Devin](https://app.devin.ai/) 、 [Anthropic 代码助手](https://www.anthropic.com/claude-code) 以及 [Cursor 后台智能体](https://docs.cursor.com/background-agent) 。

**AI 应用构建器与原型设计工具** ——例如 Lovable、Bolt/Stackblitz、Vercel v0 和 Replit——正成为一个快速扩张的品类。这些平台能够根据自然语言指令、线框图或视觉示例生成功能完整的应用程序，而不仅仅是用户界面。目前，它们既受到构建简单应用的氛围编码者欢迎，也被用于专业人士创建功能完备的应用原型。尽管迄今为止，由 AI 生成的用户界面很少被纳入生产代码库，但这可能仅仅反映了此类工具目前的不成熟状态。

**AI 智能体的版本控制** ：随着 AI 智能体承担更多实施工作，开发者关注的重点从代码 *如何* 变更转向 *为何* 变更以及 *是否有效* 。当整个文件被一次性生成时，传统的差异对比就失去了意义。像 [Gitbutler](https://gitbutler.com/) 这样的工具正在围绕意图而非文本来重构版本控制——记录提示历史、测试结果和智能体溯源。在这个新范式下，Git 成为后端账本，而真正的行动发生在追踪目标、决策和结果的语义层中。

**源代码管理系统集成** 使人工智能能够审查问题与拉取请求，并参与讨论。该集成充分利用了源代码管理的协作特性，围绕问题或拉取请求的讨论为 AI 提供了宝贵的实施背景。此外，人工智能还协助审查开发者的拉取请求，重点关注正确性、安全性和合规性。典型案例如 [Graphite](https://graphite.dev/) 和 [CodeRabbit](https://www.coderabbit.ai/) 提供的解决方案。

[![An image showing examples of an AI code review](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/10/250918-Trillion-Dollar-AI-ILG-6-scaled.png)](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/10/250918-Trillion-Dollar-AI-ILG-6-scaled.png)

当今编程助手的主要循环通常是代理式的（即 LLM 决定下一步行动并使用工具，如 HF 框架中的 [三星架构](https://huggingface.co/blog/smolagents) ）。目前，像文本修改、库更新或添加简单功能这类基础任务已能完全自主完成。我们曾见证过神奇时刻：GitHub 群组关于功能的讨论常以一句简短的“请实现@ai 助手”收尾，随后便能生成完美可合并的拉取请求。但对于更复杂的需求，这种自动化尚未成为常态。

**遗留代码迁移** 始终位列最成功的人工智能编程应用场景之一（例如 [参见此处](https://arxiv.org/html/2504.09691v1) ）。常见应用场景包括从 Fortran 或 COBOL 迁移至 Java、Perl 迁移至 Python，或替换陈旧的 Java 库。通用策略通常先根据遗留代码生成功能规范，待确认无误后，仅以旧代码库为参考解决歧义，再利用规范生成新实现。目前该领域已涌现多家初创企业，市场规模极为庞大。  

## QA & Documentation

代码编写完成后，需要进行集成测试并编写文档。这一阶段催生了专门的工具集。

**面向开发者和 LLMs 的文档支持** ——如今，LLMs 不仅能出色地生成面向用户的文档，还能创建供 LLMs 在运行时调用的文档。诸如 [Context7](https://context7.com/) 之类的工具可适时自动提取准确上下文——检索相关代码、注释和示例——从而确保生成的文档与实际实现保持一致。除静态页面外， [Mintlify](http://mintlify.com/) 等产品还能创建动态文档站点，开发者可直接与 [问答助手](https://www.mintlify.com/docs/ai/assistant) 互动，甚至提供 [智能体](https://www.mintlify.com/docs/ai/agent) 让用户通过简单指令按需更新或重新生成文档章节。最后值得一提的是，AI 可生成专门针对安全性与合规性的文档，这对大型企业至关重要。我们也看到该领域涌现出专业工具（例如专注合规的 [Delve](https://delve.co/) ）。

**AI 质量保证** ——开发者如今可借助 AI 代理自动生成、运行及评估跨 UI、API 和后端层的测试用例，无需再手动编写。这些系统如同自主工作的 QA 工程师，能够遍历操作流程、验证预期行为，并生成附带修复建议的缺陷报告。随着软件日益由 AI 生成，引入 AI 质量保证形成了开发闭环：极端情况下，代码正变得难以解读，开发者唯一需要关注的只剩正确性、性能与预期行为——传统流程中“编码->评审->测试->提交”的线性模式已被颠覆。  

## Tools for Agents

除了上述面向人类开发者的工具外，还涌现出一类专为智能体使用而设计的工具。

**代码搜索与索引** ——当处理大型代码库（数百万或数十亿行代码）时，将整个代码库提供给 LLM 进行每次推理操作已不再可行（更不用说成本高昂）。目前的最佳实践是为 LLM 配备搜索工具以定位相关代码片段。对于小型代码库，简单的 RAG 或 grep 搜索可能就足够了。而对于大型代码库（例如可参阅 [谷歌的这篇论文](https://arxiv.org/html/2504.09691v1) ），则需要能够解析代码并创建调用图的专用软件来确保找到所有引用。这一新兴领域包括像 [Sourcegraph](https://sourcegraph.com/?utm_source=google&utm_medium=cpc&utm_campaign=20326480795&utm_term=sourcegraph&gad_source=1&gad_campaignid=20326480795) 这样的公司，它提供分析大型代码库的工具；还有如 [Relace](https://relace.ai/) 等公司的专用模型，可帮助识别和排序相关文件。

**网络与文档搜索** ——诸如 [Mintlify](https://www.mintlify.com/) 和 [Context7](https://context7.com/) 这类工具擅长生成和维护代码感知文档，能够从实时代码库中提取最相关的代码片段、注释和使用示例，确保文档的准确性和时效性。相比之下， [Exa](https://exa.ai/) 、 [Brave](https://brave.com/search/api/) 和 [Tavily](https://www.tavily.com/) 等网络搜索工具则针对即时检索进行了优化，可帮助智能体快速按需获取外部参考信息和长尾知识。

**代码沙盒** ——测试代码并运行简单的命令行工具进行分析和调试，是智能代理的重要工具。然而，由于存在幻觉或潜在的恶意上下文，在本地开发系统上执行代码存在风险。此外，开发环境可能较为复杂，而自动化环境的优势在于能确保测试的可重复性。诸如 [E2B](https://e2b.dev/) 、 [Daytona](https://daytona.io/) 、 [Morph](https://morph.so/) 、 [Runloop](https://www.runloop.ai/) 以及 [Together 公司的代码沙盒](https://www.together.ai/code-sandbox) 等执行沙盒供应商正应对这一需求，已成为人工智能开发栈中的关键组件。  

## Market Map

以下我们尝试勾勒出更广泛的人工智能编程初创企业生态系统。该布局大致遵循先前概述的软件开发生命周期，并增加了额外类别。企业排名不分先后，偶尔也会包含现有企业的产品。

[![A Market Map of the broader AI coding start-up ecosystem](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/10/250918-Trillion-Dollar-AI-ILG-5-r8.png)](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/10/250918-Trillion-Dollar-AI-ILG-5-r8.png)

## 软件开发正在如何变革？

基于人工智能的软件开发技术已经到来，现在各组织需要将其投入实际应用。 [近期 Reddit 上有讨论提到](https://www.reddit.com/r/ClaudeAI/comments/1jer3jt/claude_code_is_super_duper_expensive_any_tips_to/) “Claude Code 成本极高，有什么优化建议吗？”。成本确实可能很高：假设你的代码库填满整个 10 万上下文窗口，我们使用推理模式的 Claude Opus 4.1 模型，并生成 1 万个输出和思考令牌。按每百万输入/输出令牌 15/75 美元计算，每次查询成本为 2.5 美元。按每小时 3 次查询、每天 7 小时、每年 200 天计算，年成本约达 1 万美元。在许多地区，这笔费用已超过初级开发人员的年薪。

最终，我们认为成本不会减缓 AI 开发工具的普及。诸如 Cursor 等许多平台通过同一接口支持多种模型，并擅长选择最合适的模型来优化成本。即便是最廉价的模型也能带来巨大效益。但讨论的焦点已从谁拥有最佳模型转向谁能以合适的价格提供价值。几十年来，软件开发成本几乎纯粹是人力成本，而如今 LLMs 增加了可观运营开支。这是否意味着向低成本国家进行 IT 外包的终结？或许未必，但这确实改变了商业逻辑。

这对全球三千万软件开发者意味着什么？在可预见的未来，人工智能会取代软件开发者吗？当然不会。这种荒谬的论调源于媒体炒作和激进营销的混合作用，它们试图将软件定价从按席位收费转变为替代人力成本的工具。历史告诉我们，虽然替代性定价在早期市场有效，但最终商品成本会趋近于边际成本，定价亦是如此。迄今为止，有限的真实数据表明，最精通人工智能的企业反而在 ***增加*** 开发者招聘，因为他们看到了大量具有短期正向投资回报率的应用场景。

**然而，软件开发者的工作本身已经改变，培训方式也必须相应调整。** 当今的大学课程将发生巨变，遗憾的是目前（包括我们在内）尚未有人真正明晰变革路径。算法、架构与人机交互依然重要，甚至编程能力仍不可或缺——毕竟开发者时常需要将 LLM 从它自己挖的坑里拽出来。但典型的大学软件开发课程，最好被视为另一个时代的遗存，对当今软件产业几乎缺乏实际指导意义。

从更长远的角度看，人工智能编程技术栈使软件能够自我扩展。例如， [Gumloop](https://www.gumloop.com/) 允许用户描述他们希望在产品中看到的附加功能，应用程序将利用 AI 编写代码来实现这些功能。这种趋势将发展到何种程度？我们能否通过让 LLMs 基于人类语言 API 规范进行晚期绑定来实现应用集成？普通的桌面应用程序是否会配备“氛围编码附加功能”菜单按钮？长远来看，应用程序若以不可变的代码形式发布且不具备任何自我扩展能力，似乎是不合情理的。

我们最终能否彻底消除代码，转而让 LLM 直接执行我们的高层意图（ [正如 Andrej 在此提出的设想](https://www.youtube.com/watch?v=LCEmiRjPEtQ) ）？在最简单的场景中，这已成为现实：ChatGPT 很乐意执行简单算法。但对于更复杂的任务，编写代码仍具有明显优势，主要源于其效率。在现代 GPU 上使用优化代码相加两个 16 位整数仅需约 10^-14 秒，而 LLM 生成输出词元至少需要 10^-3 秒。速度快一百亿倍的优势足以构成护城河，我们预计代码仍将长期存在。  

## 是时候借助人工智能来构建了

从历史上看，技术超级周期向来是创办公司的最佳时机，这次也不例外。人工智能既需要新工具，又能极大加速开发周期的双重特性，为初创企业创造了绝佳条件。以编程助手为例：微软的 GitHub Copilot 凭借先发优势、与 OpenAI 的合作关系、头号 IDE（VSCode）、头号源代码管理工具（GitHub）以及顶尖的企业销售团队，看似势不可挡。然而多家初创公司仍成功与之抗衡。在技术超级周期中，守成者往往举步维艰。

我们正处在软件开发自诞生以来最大变革的早期阶段。软件工程师们正在获得比以往任何时候都更能提升生产力和能力的工具。终端用户则可期待更丰富、更优质的软件。最后同样重要的是，当下正是史上创办软件开发公司的最佳时机。若您想参与这场变革，我们 a16z 愿与您携手同行！

- - [X](https://twitter.com/appenz)
	- [Linkedin](https://www.linkedin.com/in/appenz/)
- - [X](https://twitter.com/stuffyokodraws)
	- [Linkedin](https://www.linkedin.com/in/yokoli/)