---
title: "Real-world engineering challenges: building Cursor"
source: "https://newsletter.pragmaticengineer.com/p/cursor?utm_campaign=post&utm_medium=web"
author:
  - "[[Gergely Orosz]]"
published: 2025-06-11
created: 2025-07-01
description: "Cursor has grown 100x in load in just a year, sees 1M+ QPS for its data layer, and serves billions of code completions, daily. A deepdive into how it’s built with cofounder, Sualeh Asif"
tags:
  - "clippings"
---
### Cursor 在短短一年内负载增长了 100 倍，其数据层的每秒查询率（QPS）超过 100 万，并且每天提供数十亿次代码补全。与联合创始人苏莱赫·阿西夫一起深入了解它是如何构建的。

Cursor 是一款由人工智能驱动的集成开发环境，似乎是工程师们最喜欢的。在 [我们去年进行的一项调查](https://blog.pragmaticengineer.com/ide-that-software-engineers-love/) 中，对于 [“你最喜欢的具有能帮助你工作的生成式人工智能功能的编辑器是什么？”](https://blog.pragmaticengineer.com/ide-that-software-engineers-love/) 这个问题，Cursor 是最常见的答案。

Anysphere 是 Cursor 背后的初创公司，成立于 2022 年，Cursor 的第一个版本于两年前，即 2023 年 3 月发布。上周，Anysphere 宣布他们已经筹集了 9 亿美元的 C 轮融资，公司估值达到 99 亿美元（！！）。该业务的年收入已超过 5 亿美元（！！），这可能是一项纪录：据我所知，没有其他开发工具公司在推出首款产品后的两年内达到这一里程碑。财富 500 强中 500 家最大的科技公司中有一半以上在使用 Cursor，这也有所帮助。

同样在上周，该公司发布了 [Cursor 1.0](https://www.cursor.com/changelog) ，这是一个重大版本：显著的新增功能包括人工智能代码审查（通过一个名为 BugBot 的工具）、后台代理以及对内存的支持（记住过去聊天的细节）。

我与 Cursor 联合创始人苏莱赫·阿西夫（Sualeh Asif）坐下来，了解 Cursor 的工作原理以及团队如何构建这个工具，他分享了其内部的新细节：

1. **技术栈** 。TypeScript 和 Rust、云服务提供商、Turbopuffer、Datadog、PagerDuty 等等。
2. **自动完成功能的工作原理。** 一个低延迟同步引擎将加密后的上下文传递给服务器，服务器在其上运行推理。
3. **聊天功能如何在不将代码存储在服务器上的情况下运行。** 巧妙运用默克尔树，避免在服务器上存储源代码，同时能够使用嵌入技术搜索源代码。
4. **Anyrun：Cursor 的编排器服务。** 一个 Rust 服务负责在云端启动代理，利用亚马逊 EC2 和 AWS Firecracker，安全地并以正确的进程隔离方式进行。
5. **工程挑战。** 使用模式决定了技术选择、扩展问题、冷启动问题、分片挑战以及难以发现的故障。
6. **因必要而进行的数据库迁移。** Cursor 如何以及为何从 Yugabyte（一个本应能无限扩展的数据库）迁移到 PostgresSQL。此外，在一次大型索引中断期间，在数小时内迁移到 Turbopuffer 的艰巨努力。
7. **工程文化与流程。** 每 2 至 4 周发布一次，异常保守的功能特性标记，有一个专门的基础设施团队，一种实验文化，以及他们所面临的一个有趣的工程挑战。

*本集是 [《现实世界工程挑战》系列](https://newsletter.pragmaticengineer.com/t/real-world-engineering-challenges) 的一部分。阅读 [其他类似的深度剖析](https://newsletter.pragmaticengineer.com/t/real-world-engineering-challenges) 。*

---

#### 按数字解读 Cursor

在深入探讨技术栈之前，让我们先从一些关于 Cursor 的数字背景开始：

- **50** ：参与 Cursor 项目的工程师人数
- 每秒100万次交易，峰值时更高
- **100 倍：** 12 个月内用户量和负载增长 100 倍，有时环比翻倍。
- **1 亿多行** ：企业客户（如英伟达、优步、条纹支付、生鲜配送平台 Instacart、电商平台 Shopify、金融科技公司 Ramp、数据监控平台 Datadog 等）每天使用 Cursor 编写的企业代码行数。Cursor 称，美国最大的 1000 家公司中有超过 50%使用其产品。
- **超过 5 亿美元** ：年度营收运行率。5 月初时为 3 亿美元 [，](https://www.lennysnewsletter.com/p/the-rise-of-cursor-michael-truell) 1 月份时为 1 亿美元 [，而一年前还为零。Cursor 会创造营收增长记录吗？](https://x.com/AnjneyMidha/status/1879306784525222193)
- **十亿：** 企业用户和非企业用户每天使用 Cursor 编写的代码行数略少于这个数字
- **数百太字节** ：Cursor 数据库中存储的索引规模。 *这可能看起来不如其他数字那么令人印象深刻，但与图像和视频相比，代码本身在存储方面占用空间相当小。此外，这不是代码本身，而是嵌入向量，因为 Cursor 不在其数据库中存储代码。*

据路透社报道，Cursor 在创收方面可能正在追赶 GitHub Copilot [报道称](https://www.reuters.com/business/ai-vibe-coding-startups-burst-onto-scene-with-sky-high-valuations-2025-06-03/) GitHub Copilot 在 2024 年可能创造了 5 亿美元的收入。目前，Cursor 有望在 2025 年实现同样的收入，如果以目前的速度持续增长，甚至可能更多。

## 1\. 技术栈

关于 Cursor 背后这个诞生还不到三年的代码库的一些数据：

- **25,000** 个文件
- **700 万** 行代码

**编辑器** 是 Visual Studio Code 的一个分支，这意味着它与 VS Code 拥有相同的技术栈：

- **TypeScript** ：大部分业务逻辑用这种语言编写
- **电子** ：Cursor 所使用的框架

在创办公司时，他们必须决定是像 [Zed](https://zed.dev/) 那样从头开始构建编辑器，还是从一个分支版本起步。苏莱解释了这个决定：

> 我们需要自主拥有编辑器，而不能“仅仅”是一个扩展程序，因为我们想要改变人们的编程方式。这意味着我们要么需要构建一个全新的集成开发环境（IDE），要么从现有的编辑器进行分支开发。
> 
> 我们决定进行复刻，因为一切从头开始的话，光是构建一个稳定的编辑器就会耗费巨大精力。我们的价值主张不是构建一个稳定的编辑器，而是改变开发者的编程方式，以渐进的方式来实现。例如，不进行复刻的话，构建神奇的“标签模型”会非常困难，而复刻之后就轻而易举了。复刻让我们能够专注于体验，而非编辑器本身。

**后端**

- **TypeScript** ：大部分业务逻辑用它编写。
- **Rust** ：所有对性能要求严苛的组件都使用这种语言。下面要讨论的编排器就是一个例子。
- **从 Node API 到 Rust：** 大部分业务逻辑用 TypeScript 编写，性能密集型部分则用 Rust 编写，因此存在一座桥梁，可通过 Node.js 从 TypeScript 调用 Rust 代码。一个例子是调用大量使用此桥梁的索引逻辑（用 Rust 编写）。
- **单体应用：** 后端服务大多是一个大型单体应用，并作为一个整体进行部署。 *这提醒我们，单体应用对于早期创业公司来说运行得相当不错，并且可以帮助团队快速行动。*

**数据库：**

- **[TurboPuffer](https://turbopuffer.com/)** ：一个多租户数据库，用于存储加密文件和工作区的默克尔树，如下所述。团队因其可扩展性而更喜欢这个数据库，并且无需像以前那样处理 [数据库分片](https://en.wikipedia.org/wiki/Shard_\(database_architecture\)) 的复杂性。我们在下面的“工程挑战”中介绍挑战。
- **[松果体（Pinecone）](https://pinecone.io/) ：** 一个向量数据库，用于存储一些文档的嵌入向量

**数据流**

- **[Warpstream](https://www.warpstream.com/)** ：一个兼容 Apache Kafka 的数据流服务

**工具：**

- **[Datadog](https://www.datadoghq.com/)** ：用于日志记录和监控。苏莱赫表示他们是重度用户，并且发现 Datadog 的开发者体验比其他竞品要好得多
- **[PagerDuty](https://www.pagerduty.com/)** ：用于值班管理，与他们的 Slack 集成
- **[Slack](https://slack.com/intl/en-gb/)** ：内部通信与聊天工具
- **[哨兵](https://sentry.io/)** ：错误监控
- **[幅度](https://amplitude.com/)** ：分析
- **[Stripe](https://stripe.com/en-nl)** ：使用 Cursor 购买计划时的计费和支付。
- **[WorkOS](https://workos.com/):** 登录 Cursor 时的身份验证，例如使用 GitHub 或 Google Workspace 登录
- **[Vercel](https://vercel.com/)** ：Cursor.com 网站所托管的平台
- **[线性的](https://linear.app/)** ：用于管理工作
- **Cursor** \- 自然而然！团队使用 Cursor 来构建 Cursor。最终，每位工程师都要对自己签入的代码负责，无论这些代码是他们亲手编写的，还是由 Cursor 生成的。

**模型训练：** Cursor 使用多个供应商来训练自己的模型并微调现有模型：

- **[电压园区](https://www.voltagepark.com/)**
- **[Databricks MosaicML](https://www.databricks.com/blog/databricks-mosaicml)**
- **[Foundry](https://mlfoundry.com/)**

#### 物理基础设施

所有基础设施都运行在云服务提供商上。苏莱赫说：

> 我们是一家非常典型的“云服务公司”。我们主要依赖亚马逊云服务（AWS），推理环节则主要依靠微软云服务（Azure）。我们也会使用其他一些较新的 GPU 云服务。

大部分 CPU 基础设施在 AWS 上运行。他们还运营着数万台英伟达 H100 GPU。相当一部分 GPU 在 Azure 中运行。

![](https://newsletter.pragmaticengineer.com/p/%7B%22src%22:%22https://substack-post-media.s3.amazonaws.com/public/images/3ab72d5b-860d-4271-be74-c64a2c7669d5_1536x847.png%22,%22srcNoWatermark%22:null,%22fullscreen%22:null,%22imageSize%22:null,%22height%22:803,%22width%22:1456,%22resizeWidth%22:null,%22bytes%22:null,%22alt%22:null,%22title%22:null,%22type%22:null,%22href%22:null,%22belowTheFold%22:true,%22topImage%22:false,%22internalRedirect%22:null,%22isProcessing%22:false,%22align%22:null,%22offset%22:false%7D)

微软 Azure 数据中心内的 20 块英伟达 H100 GPU。Cursor 的计算需求相当于数千个这样的机架。来源：英伟达

**推理** 是 Cursor 目前最大的 GPU 使用场景，这意味着生成下一个标记，无论是作为自动完成，还是完整的代码块。实际上，Azure GPU 仅用于推理，而不用于其他与大语言模型（LLM）相关的工作，如微调模型和训练模型。

**[Terraform](https://developer.hashicorp.com/terraform)** 是 Cursor 用于管理诸如 GPU 和虚拟机（如 EC2 实例）等基础设施的工具。

## 2\. Cursor 的自动完成功能是如何工作的

为了了解构建 Cursor 所面临的一些技术挑战，让我们看看首次启动编辑器时会发生什么。

![](https://newsletter.pragmaticengineer.com/p/%7B%22src%22:%22https://substack-post-media.s3.amazonaws.com/public/images/242912d9-7577-4f8d-85e6-e03fbe6f1b3a_1600x1112.png%22,%22srcNoWatermark%22:null,%22fullscreen%22:null,%22imageSize%22:null,%22height%22:1012,%22width%22:1456,%22resizeWidth%22:null,%22bytes%22:null,%22alt%22:null,%22title%22:null,%22type%22:null,%22href%22:null,%22belowTheFold%22:true,%22topImage%22:false,%22internalRedirect%22:null,%22isProcessing%22:false,%22align%22:null,%22offset%22:false%7D)

使用项目打开 Cursor

#### 低延迟同步引擎：自动完成建议

打开项目或文件夹后，你可能会直接进入文件编辑。这意味着 Cursor 需要生成自动完成建议，Cursor 团队将其称为标签建议。

**一个低延迟同步引擎为“标签模型”提供动力。** 这会生成呈灰色显示的建议，按下“Tab”键即可接受这些建议。这些建议需要在理想情况下不到一秒的时间内快速生成。以下是幕后发生的情况：

![](https://newsletter.pragmaticengineer.com/p/%7B%22src%22:%22https://substack-post-media.s3.amazonaws.com/public/images/583f8775-d894-4cb5-aa20-940b8284c864_1558x1348.png%22,%22srcNoWatermark%22:null,%22fullscreen%22:null,%22imageSize%22:null,%22height%22:1260,%22width%22:1456,%22resizeWidth%22:null,%22bytes%22:null,%22alt%22:null,%22title%22:null,%22type%22:null,%22href%22:null,%22belowTheFold%22:true,%22topImage%22:false,%22internalRedirect%22:null,%22isProcessing%22:false,%22align%22:null,%22offset%22:false%7D)

Cursor 的“标签建议”是如何工作的

它的工作原理：

1. 客户端会在本地收集当前上下文窗口（代码）的一小部分
2. 代码已加密
3. 加密代码/上下文被发送到后端
4. 后端对代码/上下文进行解密
5. 使用 Cursor 的内部 LLM 模型生成一条建议
6. 建议被退回
7. 集成开发环境（IDE）会显示该建议。按下“Tab”键可接受该建议。
8. ……该过程会对下一个建议重复进行。

这种“标签模型”必须尽可能快，数据传输要尽可能低。在要发送多少上下文以及建议的质量之间总是存在权衡：Cursor 能发送的相关上下文越多，建议就越好。然而，发送大量上下文会减慢建议的显示速度，所以把握好这一点是 Cursor 工程师面临的一项挑战。

## 3\. Cursor 的聊天功能如何在不将代码存储在服务器上的情况下运行

Cursor 支持一种聊天模式，用于询问代码库相关问题、与代码库“聊天”，或者要求 Cursor 执行一些操作，这些操作会启动一个代理来进行重构、添加某些功能、修改方法等。后端不存储任何源代码，但所有大语言模型（LLM）操作都在后端进行。它管理这些操作的方式是通过代码库的索引。其工作原理如下：

**在聊天模式下提问：** 我们以询问 createTodo()方法为例，它是代码库的一部分，在 server.js 中定义。 *为了使事情更复杂，我在 index.html 中内联定义了一个类似的方法 addTodo()。让我们看看 Cursor 如何处理这个！*

![](https://newsletter.pragmaticengineer.com/p/%7B%22src%22:%22https://substack-post-media.s3.amazonaws.com/public/images/343ce691-1072-42b0-b066-e051f767d6a5_958x194.png%22,%22srcNoWatermark%22:null,%22fullscreen%22:null,%22imageSize%22:null,%22height%22:194,%22width%22:958,%22resizeWidth%22:null,%22bytes%22:null,%22alt%22:null,%22title%22:null,%22type%22:null,%22href%22:null,%22belowTheFold%22:true,%22topImage%22:false,%22internalRedirect%22:null,%22isProcessing%22:false,%22align%22:null,%22offset%22:false%7D)

向 Cursor 提供与代码库相关的提示

该提示被发送到 Cursor 服务器，在那里它会对其进行解释，并决定需要执行一次代码库搜索：

![](https://newsletter.pragmaticengineer.com/p/%7B%22src%22:%22https://substack-post-media.s3.amazonaws.com/public/images/89b78ca0-5680-4739-8f16-190320090835_974x180.png%22,%22srcNoWatermark%22:null,%22fullscreen%22:null,%22imageSize%22:null,%22height%22:180,%22width%22:974,%22resizeWidth%22:null,%22bytes%22:null,%22alt%22:null,%22title%22:null,%22type%22:null,%22href%22:null,%22belowTheFold%22:true,%22topImage%22:false,%22internalRedirect%22:null,%22isProcessing%22:false,%22align%22:null,%22offset%22:false%7D)

搜索开始：

![](https://newsletter.pragmaticengineer.com/p/%7B%22src%22:%22https://substack-post-media.s3.amazonaws.com/public/images/c89f983a-87d8-4b88-9510-aec3db4ca8e3_966x186.png%22,%22srcNoWatermark%22:null,%22fullscreen%22:null,%22imageSize%22:null,%22height%22:186,%22width%22:966,%22resizeWidth%22:null,%22bytes%22:null,%22alt%22:null,%22title%22:null,%22type%22:null,%22href%22:null,%22belowTheFold%22:true,%22topImage%22:false,%22internalRedirect%22:null,%22isProcessing%22:false,%22align%22:null,%22offset%22:false%7D)

**搜索是使用代码库索引完成的** 。代码库索引是之前创建的嵌入。它尝试使用向量搜索来定位与上下文最匹配的嵌入。在这种情况下，向量搜索返回了两个非常接近的结果：在 server.js 和 index.html 中。

**从客户端请求代码：** 服务器不存储任何源代码，但现在要从 [server.js](http://server.js/) 和 index.html 请求源代码，以便它可以对两者进行分析并确定哪一个是相关的：

![](https://newsletter.pragmaticengineer.com/p/%7B%22src%22:%22https://substack-post-media.s3.amazonaws.com/public/images/fad62e93-ffab-4615-b5d9-56b63b7569ae_962x334.png%22,%22srcNoWatermark%22:null,%22fullscreen%22:null,%22imageSize%22:null,%22height%22:334,%22width%22:962,%22resizeWidth%22:null,%22bytes%22:null,%22alt%22:null,%22title%22:null,%22type%22:null,%22href%22:null,%22belowTheFold%22:true,%22topImage%22:false,%22internalRedirect%22:null,%22isProcessing%22:false,%22align%22:null,%22offset%22:false%7D)

最后，在进行向量搜索并向客户端请求相关源代码之后，服务器便拥有了回答问题所需的上下文：

![](https://newsletter.pragmaticengineer.com/p/%7B%22src%22:%22https://substack-post-media.s3.amazonaws.com/public/images/e263225e-bae9-42a4-a649-b17990c57a1d_950x920.png%22,%22srcNoWatermark%22:null,%22fullscreen%22:null,%22imageSize%22:null,%22height%22:920,%22width%22:950,%22resizeWidth%22:null,%22bytes%22:null,%22alt%22:null,%22title%22:null,%22type%22:null,%22href%22:null,%22belowTheFold%22:true,%22topImage%22:false,%22internalRedirect%22:null,%22isProcessing%22:false,%22align%22:null,%22offset%22:false%7D)

Cursor 在幕后做了一些事情，以使这类搜索能够正常工作。

#### 带有代码块的语义索引代码

为了像上述情况那样允许使用嵌入进行向量搜索，Cursor 首先需要将代码分解成更小的块，创建嵌入，并将这些嵌入存储在服务器上。以下是它的实现方式：

![](https://newsletter.pragmaticengineer.com/p/%7B%22src%22:%22https://substack-post-media.s3.amazonaws.com/public/images/05e037ae-80cb-48a4-873e-9ddf25de77fe_1318x1322.png%22,%22srcNoWatermark%22:null,%22fullscreen%22:null,%22imageSize%22:null,%22height%22:1322,%22width%22:1318,%22resizeWidth%22:null,%22bytes%22:null,%22alt%22:null,%22title%22:null,%22type%22:null,%22href%22:null,%22belowTheFold%22:true,%22topImage%22:false,%22internalRedirect%22:null,%22isProcessing%22:false,%22align%22:null,%22offset%22:false%7D)

1. **创建代码块。** Cursor 会将文件内容切割成更小的部分。每个部分稍后都将成为一个嵌入。
2. **创建嵌入，而不存储文件名或代码。** Cursor 甚至不想在服务器上存储文件名，因为这可能被视为机密信息。相反，它会将混淆后的文件名和加密的代码块发送到服务器。服务器对代码进行解密，使用 [OpenAI 的嵌入模型](https://platform.openai.com/docs/guides/embeddings) 或其自己的模型之一创建嵌入，并将嵌入存储在其向量数据库 Turbopuffer 中。

创建嵌入在计算上成本高昂，这也是它在 Cursor 后端使用云端 GPU 来完成的原因之一。对于中等规模的代码库，索引通常耗时不到一分钟，而对于大型代码库则可能需要几分钟甚至更长时间。你可以在 Cursor 中，通过“Cursor 设置”→“索引”来查看索引状态：

![](https://newsletter.pragmaticengineer.com/p/%7B%22src%22:%22https://substack-post-media.s3.amazonaws.com/public/images/be0b36de-c456-45d4-816b-b3784d5f3517_1326x692.png%22,%22srcNoWatermark%22:null,%22fullscreen%22:null,%22imageSize%22:null,%22height%22:692,%22width%22:1326,%22resizeWidth%22:null,%22bytes%22:null,%22alt%22:null,%22title%22:null,%22type%22:null,%22href%22:null,%22belowTheFold%22:true,%22topImage%22:false,%22internalRedirect%22:null,%22isProcessing%22:false,%22align%22:null,%22offset%22:false%7D)

#### 使用默克尔树保持索引最新

当你使用 Cursor 或其他 IDE 编辑代码库时，Cursor 的服务器端索引会过时。一个简单的解决方案是每隔几分钟运行一次重新索引操作。然而，由于索引在计算方面成本很高，并且会通过传输加密代码块消耗带宽，所以这并不理想。相反，Cursor 巧妙地利用了默克尔树和一个高延迟同步引擎（同步引擎每 3 分钟运行一次）来保持服务器端索引的最新状态。

A [默克尔树](https://en.wikipedia.org/wiki/Merkle_tree) 是一种树状结构，其每个叶子节点都是底层文件的加密哈希值（例如文件 main.js 的哈希值）。并且每个节点都是其子节点哈希值的组合。一个包含四个文件的简单项目的默克尔树如下所示：

![](https://newsletter.pragmaticengineer.com/p/%7B%22src%22:%22https://substack-post-media.s3.amazonaws.com/public/images/714edd02-f202-4cbb-a442-60c09d06ad14_1600x889.png%22,%22srcNoWatermark%22:null,%22fullscreen%22:null,%22imageSize%22:null,%22height%22:809,%22width%22:1456,%22resizeWidth%22:null,%22bytes%22:null,%22alt%22:null,%22title%22:null,%22type%22:null,%22href%22:null,%22belowTheFold%22:true,%22topImage%22:false,%22internalRedirect%22:null,%22isProcessing%22:false,%22align%22:null,%22offset%22:false%7D)

基于代码库中代码的默克尔树

这个默克尔树的工作原理如下：

- 每个文件都会根据其内容生成一个哈希值。树的叶子节点就是文件。
- 每个文件夹都会根据其子文件夹的哈希值生成一个哈希值。

Cursor 使用了一个与此非常相似的默克尔树，只是它使用了混淆后的文件名。Cursor 客户端基于本地文件创建一个默克尔树，服务器也基于其已完成索引的文件创建一个默克尔树。这意味着客户端和服务器都存储它们各自的默克尔树。

**Cursor 每 3 分钟进行一次索引同步。** 为了确定哪些文件需要重新索引，它会比较两个默克尔树；一个是客户端上作为真相来源的默克尔树，另一个是服务器上作为索引状态的默克尔树。让我们以客户端上的“index.html”发生变化为例：

![](https://newsletter.pragmaticengineer.com/p/%7B%22src%22:%22https://substack-post-media.s3.amazonaws.com/public/images/4eef44d8-4fee-436b-9bc6-d5840e2d18a2_1460x1452.png%22,%22srcNoWatermark%22:null,%22fullscreen%22:null,%22imageSize%22:null,%22height%22:1448,%22width%22:1456,%22resizeWidth%22:null,%22bytes%22:null,%22alt%22:null,%22title%22:null,%22type%22:null,%22href%22:null,%22belowTheFold%22:true,%22topImage%22:false,%22internalRedirect%22:null,%22isProcessing%22:false,%22align%22:null,%22offset%22:false%7D)

客户端和服务器端的默克尔树不同步。Cursor 使用了混淆的文件名，上面的实际文件名仅为简化起见。

**树遍历用于定位需要重新索引的位置。** 树遍历并非我们开发者经常实现的功能，但对于此用例，Cursor 工程师必须这样做。默克尔树使树遍历变得高效，因为从根节点开始，很容易判断哈希值是否匹配。在哈希值存在差异的地方，也很容易找到需要同步的文件。同样重要的是，默克尔树将同步操作最小化，仅针对已更改的文件。

这种默克尔树结构非常适合 Cursor 在实际中的使用。例如，在一天结束时关闭计算机，然后在第二天从 git 仓库获取更新来开始新的一天，这是很常见的操作。在一个团队中，到第二天早上有一堆文件发生变化也是很常见的。有了这种默克尔树，Cursor 尽可能少地进行重新索引，在客户端节省时间，并在服务器端尽可能高效地使用计算资源。

#### 安全索引

尽管 Cursor 不在服务器端存储代码，但代码库中仍有一些敏感部分，即使加密后发送也不是个好主意。敏感数据包括密钥、API 密钥和密码。

**使用.gitignore 和.cursorignore 是确保索引安全的最佳方法。** 密钥、API 密钥、密码和其他敏感信息不应上传到版本控制系统，通常存储为局部变量，或存储在添加到.gitgnore 的本地环境文件（.env 文件）中。Cursor 尊重.gitignore，不会索引其中列出的文件，也不会将这些文件的内容发送到服务器。此外，它还提供了一个.cursorignore 文件，应在其中添加要被 Cursor 忽略的文件。

在上传代码块进行索引之前，Cursor 还会扫描代码块中是否存在可能的机密信息或敏感数据，并且不会发送这些数据。

#### 索引超大型代码库

对于庞大的代码库（通常是有数千万行代码的单一仓库），对整个代码库进行索引极其耗时，会占用大量 Cursor 的计算资源，而且通常没有必要。在这种情况下，使用.cursorignore 文件是明智的做法。文档提供了更多指导。

## 4\. Anyrun：Cursor 的编排器服务

Anyrun 是 Cursor 编排器组件的名称，并且完全用 Rust 编写。 *有趣的事实：“Anyrun”是对 Cursor 的公司名称 Anysphere 的致敬。* Anyrun 负责以下事项：

## 此帖子仅限付费订阅者阅读

[已经是付费订阅用户了？ **登录**](https://substack.com/sign-in?redirect=%2Fp%2Fcursor%3Futm_campaign%3Dpost%26utm_medium%3Dweb&for_pub=pragmaticengineer&change_user=false)