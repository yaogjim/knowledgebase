---
title: "Building a web search engine from scratch in two months with 3 billion neural embeddings"
source: "https://blog.wilsonl.in/search-engine/"
author: ""
created: 2025-08-18 14:32:36
published: 2025-08-18 14:32:36
description: ""
tags: ""
---
## 在两个月内利用30亿个神经嵌入从头构建一个网络搜索引擎

Published August 10, 202534 min read

[![Screenshot of SERP.](https://blog.wilsonl.in/search-engine/serp-rocksdb.png)](https://blog.wilsonl.in/search-engine/serp-rocksdb.png)

不久前，我决定开展一个项目来挑战自己：从零开始构建一个网络搜索引擎。除了有深入钻研的有趣机会外，还有两个动机：

-   搜索引擎似乎变得越来越糟糕，充斥着更多的 SEO 垃圾信息，而相关的优质内容却越来越少。
-   基于 Transformer 的文本嵌入模型开始兴起，并展现出惊人的自然语言理解能力。

我曾有一个简单的问题：为什么搜索引擎不能总是给出高质量的内容呢？这样的内容可能很稀少，但互联网的长尾很长，质量更高的结果应该比你如今看到的大量无实质内容和吸引眼球的东西排名更靠前。

另一个痛点是，搜索引擎常常显得功能不足，更接近关键词匹配而非人类水平的智能。一个相当复杂或微妙的查询根本无法被大多数搜索引擎回答，但具备这种能力将会很强大：

[![SERP result of paragraph-length query.](https://blog.wilsonl.in/search-engine/serp-paragraph-cropped.png)](https://blog.wilsonl.in/search-engine/serp-paragraph-cropped.png)

搜索引擎涵盖了计算机科学、语言学、本体论、自然语言处理、机器学习、分布式系统、性能工程等广泛领域。我想看看自己在短时间内能够学到多少知识并涵盖多少领域，这会很有趣。另外，拥有自己的搜索引擎也很酷。鉴于这些原因，我直接投入其中。

在这篇文章中，我将从头到尾讲述这两个月的历程，一开始没有任何基础设施、初始数据，也没有任何构建网络搜索引擎的经验。一些亮点如下：

-   一组 200 个 GPU 生成了总计 30 亿个 [SBERT](https://huggingface.co/sentence-transformers/multi-qa-mpnet-base-dot-v1) 嵌入向量。
-   在高峰期，数百个爬虫每秒摄取5万个页面，最终形成了一个包含2.8亿个页面的索引。
-   端到端查询延迟稳定在500毫秒左右。
-   RocksDB 和 HNSW 被[分片](https://blog.wilsonl.in/corenn/)到 200 个核心、4TB 内存和 82TB 固态硬盘上。

你可以将此搜索引擎的已部署实例作为 [实时演示](https://blog.wilsonl.in/search-engine/#live-demo) 来试用一下。以下是本文将介绍的系统的高层架构图：

-   [Proving ground](https://blog.wilsonl.in/search-engine/#proving-ground)
-   [Normalization](https://blog.wilsonl.in/search-engine/#normalization)
-   [Chunking](https://blog.wilsonl.in/search-engine/#chunking)
    -   [Semantic context](https://blog.wilsonl.in/search-engine/#semantic-context)
    -   [Statement chaining](https://blog.wilsonl.in/search-engine/#statement-chaining)
-   [Initial results](https://blog.wilsonl.in/search-engine/#initial-results)
-   [Crawler](https://blog.wilsonl.in/search-engine/#crawler)
-   [Pipeline](https://blog.wilsonl.in/search-engine/#pipeline)
-   [Storage](https://blog.wilsonl.in/search-engine/#storage)
-   [Service mesh](https://blog.wilsonl.in/search-engine/#service-mesh)
-   [GPU buildout](https://blog.wilsonl.in/search-engine/#gpu-buildout)
-   [Sharded HNSW](https://blog.wilsonl.in/search-engine/#sharded-hnsw)
-   [Optimizing latency](https://blog.wilsonl.in/search-engine/#optimizing-latency)
-   [Knowledge graph](https://blog.wilsonl.in/search-engine/#knowledge-graph)
-   [SERP](https://blog.wilsonl.in/search-engine/#serp)
    -   [AI assistant](https://blog.wilsonl.in/search-engine/#ai-assistant)
    -   [State tracking](https://blog.wilsonl.in/search-engine/#state-tracking)
-   [Search quality](https://blog.wilsonl.in/search-engine/#search-quality)
-   [Live demo](https://blog.wilsonl.in/search-engine/#live-demo)
-   [Costs](https://blog.wilsonl.in/search-engine/#costs)
-   [结论与下一步计划](https://blog.wilsonl.in/search-engine/#conclusion-and-what's-next)

## Proving ground

我首先创建了一个最小化的实验平台，来验证 [神经嵌入](https://huggingface.co/spaces/mteb/leaderboard) 在搜索方面是否更具优势：选取一些网页，将其进行分块，然后看看我能否精确地回答复杂的间接自然语言查询。

举个例子，假设我正在查看 S3 文档。以下是当前系统对一些查询的回答方式，以及我设想它们应该如何被回答：

| Query | Traditional search | Neural search |
| --- | --- | --- |
| 我想用 S3 代替 PostgreSQL，但对于数据库，我可以在另一列中用某个文件为一些人工注释添加标签 | *关于 Postgres、S3 和文件的随机结果* | 你还可以在存储对象时指定自定义元数据。 |
| 为什么在允许所有来源后，跨域资源共享（CORS）仍然不起作用？ | *关于跨域资源共享（CORS）、“S3 无法正常工作”、对象权限的随机片段* | 存储桶配置具有最终一致性模型…… |
| 文件会丢失或损坏吗？ | *(No result shown)* | 如果 PUT 请求成功，您的数据将被安全存储。 |
| 我可以从 Lua 使用 S3 吗？ | *(No result shown)* | 亚马逊 S3 的架构设计为与编程语言无关，……通过 REST API，你可以使用标准 HTTP 请求来创建、获取和删除存储桶及对象。 |

基本上，搜索引擎应该理解*意图* ，而不是*关键词* ：

-   查询被视为一个整体，而不是分解为关键词和短语。
-   无需查询工程：运算符、格式、要用的恰当词汇。
-   “舌尖现象”、隐含查询和概念性查询都能被正确映射到正确答案。
-   你可以提出多概念、复杂、有细微差别的查询，并揭示不明显的关系。
-   它应该远不容易受到关键词垃圾信息和搜索引擎优化策略的影响。

这对于一般的搜索来说已经很棒了。但它对于发现见解、未被注意到的联系和隐藏的瑰宝也会很有帮助。你可以提出一些非常复杂的特定查询，搜索引擎会在一篇晦涩的高质量文章中找出一句简短的话。你可以写下一段自己的想法和观点，然后找到其他有类似观点的作者和领域。你可以用表示质量和深度的短语进行查询，以找到具有相似价值观的内容和群体。

这是我最初创建用于验证概念的沙盒飞轮：

1.  增加收集到的多样化原始网页集。
2.  解析、规范化、扩充它们，并将其嵌入到一个可查询的 HNSW 索引中。
3.  在我进行爬取、调试、实验和评估时，构建并扩展查询的测试数据集。
4.  创建一个用户界面，以便在每个阶段内省数据、查看故障点并进行调整。

## Normalization

HTML 使用具有各种意图的标签来表示内容：布局、文本、媒体、交互性、元数据和应用程序编程。由于搜索引擎专注于文本内容，任何处理流程的第一步都是清理和规范化从爬取页面中获取的嘈杂标记，并提取语义文本。[WHATWG](https://html.spec.whatwg.org/multipage/) 已经定义了大量语义元素和规则，我从中提取出了以下迷你规范：

-   结构应保持一致： `table > (thead, tbody, tfoot) > tr > (th, td)` ; `(无序列表、有序列表) > 列表项`
-   仅应保留语义文本元素： `p, table, pre, blockquote, ul, ol, dl` 。
-   文本被修剪和折叠；在 `<p>` 之外没有松散或意外的文本节点。
-   将文本树扁平化，以便在检索和修改文本跨度（这种情况经常发生）时，无需遍历和协调树结构。
-   尽可能多地移除或展开节点：脚本、属性、空元素、`<head>`、注释节点、外部/布局元素。
-   如果存在 `main > article`，则使用它而不是整个页面。

一个目标是去除页面上所有的 [修饰部分](https://www.nngroup.com/articles/browser-and-gui-chrome/) ，因为它们不属于内容，会污染上下文并歪曲含义：

-   菜单栏、导航链接、横幅、页脚、网站信息。
-   评论区、旁白、指向其他文章的链接。
-   界面元素、表单、控件、社交媒体按钮。

这些可能会与主要内容混淆，削弱搜索引擎对页面实际内容和意图的理解，导致查询结果不佳。

如果页面使用诸如\`

\`之类的语义元素或 ARIA 角色，那么移除这些内容很简单，但否则就会陷入启发式方法和自然语言处理中。像对类和 ID 进行模式匹配这样的方法充满问题，意外删除内容比保留噪声更糟糕。如果有更多时间和资源，像对 DOM 结构进行视觉分类或训练统计文本模型这样更高级的方法是可行的。

鉴于 HTML 的宽松性，许多网站并未严格遵循这些规则，因此会出现覆盖不足和覆盖过度的情况。不幸的是，这甚至适用于一些不容忽视的大型网站，所以我不得不为它们硬编码一些特殊规则（就像某个知名浏览器那样）。

en.wikipedia.org 的示例特殊规则

```
if re.match(r"^en\.wikipedia\.org/wiki/", url):
    if tag_name not in HEADING_ELEMS:
        last_heading = find_prev_sibling(child, lambda e: e.tagName in HEADING_ELEMS)
        if (
            last_heading
            and last_heading.tagName == "h2"
            and get_text_content(last_heading).replace("[edit]", "").strip()
            in ("Sources", "Further reading", "External links", "See also")
        ):
            # This is in a section we don't want to keep.
            continue

    classes = set(child.getAttribute("class").split(" "))
    if "hatnote" in classes: continue # Remove "meta" information about the Wikipedia article itself. See https://en.wikipedia.org/wiki/Wikipedia:Hatnote.
    if tag_name == "ol" and "references" in classes: continue # Remove section containing list of references.
    if tag_name == "table" and "sidebar" in classes: continue # Remove sidebar, which sometimes contains useful facts but often just contains "adjacent" information and links, and is hard to parse due to use of table for formatting (not semantics).
    if "thumb" in classes: continue # Remove figures.
    if "navbox" in classes: continue # Remove the navigation boxes at the bottom of the page.
    if "printfooter" in classes: continue # Remove the message "Retrieved from $url".
    if child.getAttribute("id") == "siteSub": continue # Remove the message "From Wikipedia, the free encyclopedia".

    if c.tagName == "sup" and "reference" in classes: continue # Remove numbered references around square brackets within body text.
    if "mw-jump-link" in classes: continue # Remove "Jump to content" link.
    if "mw-editsection" in classes: continue # Remove "[edit]" links.
    if "mw-ui-button" in classes: continue # Remove UI buttons.
    if "wb-langlinks-edit" in classes: continue # Remove "Edit links" link.
    if "mwe-math-fallback-image-display" in classes or "mwe-math-fallback-image-inline" in classes: continue # This is a fallback, we can remove it as we handle <math> elements.
```

许多网页上都有大量丰富的结构化数据。像 OpenGraph 这样的 `<meta>` 标签广为人知。还有一整套规范用于在网页中表示几乎任何内容，以供机器人使用。搜索引擎利用这些来提供增强的丰富结果并构建它们的知识图谱。这就是它们如何知道某个内容是在提及一部电影而不是一本书或一个人，从而提高相关性、发现世界上新出现的事物，并展示精美的购物、评分、轮播和“附近”结果。

## Chunking

文本准备好之后，下一步是进行[分块](https://www.pinecone.io/learn/chunking-strategies/) 。大多数嵌入模型无法接受整页的输入，而且在这种长度下往往会[失去表征能力](https://jina.ai/news/long-context-embedding-models-are-blind-beyond-4k-tokens/) 。在页面级别进行嵌入也过于粗糙，不利于精准定位。

一种常见的方法是简单地每隔 *n* 个字符或单词进行分割。但这可能会粗暴地切断单词、语法和结构，从而破坏语义。我的方法是使用经过训练的 [句子分割器](https://spacy.io/api/sentencizer) 将文本分割成句子，句子是自然连贯的边界。这些模型在大量文本语料库上进行训练，对语法和句法有很好的理解，以实现高精度。我发现 spaCy 的模型在这里效果最佳，它能处理诸如缩写、小数、网址和非正式风格语法等细微之处。

在我看来，将文本拆分成句子是一个很好的细节原子单元：足以精确指出查询的准确相关部分或答案，对特色直接片段或结果亮点很有用。这也将允许构建更大的嵌入单元（例如段落大小），在对长度有更多控制的同时仍保持语义连贯。

### Semantic context

但分块的一个大问题是上下文。一个句子建立在先前的句子、包含的段落、当前的章节、正在积极讨论的概念等之上。如果分块脱离了上下文的建立，间接引用（“它”、“这个”、“然后”等）就会失去意义。

第一步是利用规范化的语义文档树。例如：

-   标题表示嵌套或拆分的章节；\``<h2>`\` 标签下的内容与该标题的文本相关联。
-   表格标题表示每行单元格的标签；段落表示语义文本断点；`<dd>` 与其 `<dt>` 相关联；依此类推。
-   在列表之前的像*以下是建议的值：* 这样的“引导性”句子解释了该列表的内容，因此会与该列表相关联。

因此，像这样的一个页面：

> ## PostgreSQL 性能调优指南
> 
> …
> 
> ## Connection Settings
> 
> …
> 
> ### Maximum connections
> 
> 每个连接都使用一个新进程。这与大多数其他数据库系统不同。因此，该设置可能会对性能产生意想不到的影响。由于这种设计，连接比基于线程的系统使用更多资源，因此需要格外注意。以下是一些推荐值：
> 
> -   如果您正在使用16或更高版本：
>     
>     | Environment | Recommended Setting | … |
>     | --- | --- | --- |
>     | Development | 100 | … |
>     | Web Application | 200-400 | … |
>     | Data Warehouse | 50-100 | … |
>     | Microservices | 20-50 per service | … |
>     
> -   如果您正在使用版本15：
>     
>     | Environment | Recommended Setting | … |
>     | --- | --- | --- |
>     | Development | 100 | … |
>     | Web Application | 200-400 | … |
>     | Data Warehouse | 50-100 | … |
>     | Microservices | 20-50 per service | … |
>     
> 
> …

将把第一个“开发”表格行表示为

```
[
  "PostgreSQL Performance Tuning Guide", // (heading 1)
  "Connection Settings", // (heading 2)
  "Maximum connections", // (heading 3)
  "Here are some recommended values:", // (leading statement before list)
  "If you are using version 16 or greater:", // (leading statement before table)
  "Environment: Development | Recommended Setting: 100 | …", // denormalized row to provide column headings as context
].join("\n")
```

rather than

```
"Development | 100 | …"
```

由于缺乏上下文，其含义丧失。

此上下文还提供了消除歧义及相关性。在上述示例中，两个表格仅通过每个表格之前提及的版本来区分。

### Statement chaining

这并没有解决附近局部上下文的问题：后续句子、指代等。为了进一步解决这个问题，我训练了一个 [DistilBERT](https://huggingface.co/distilbert/distilbert-base-uncased) 分类器模型，该模型会接收一个句子和前面的句子，并标记它为了保留语义而依赖于哪一个（如果有的话）。因此，在嵌入一个语句时，我会向后追溯“链条”，以确保所有相关内容也都在上下文中提供。

这还有一个好处，即标记那些永远不应被匹配的句子，因为它们本身不是“叶”句子。

[![Screenshot of the statement labeller UX.](https://blog.wilsonl.in/search-engine/statement-labeller.png)](https://blog.wilsonl.in/search-engine/statement-labeller.png)

构建了内部语句标注器用户体验，以便根据说明进行快速标注。

[![Screenshot of the statement debug view.](https://blog.wilsonl.in/search-engine/admin-statement-chain-debug.png)](https://blog.wilsonl.in/search-engine/admin-statement-chain-debug.png)

一个带有其语义上下文以及由人工智能标注的先行依赖语句的陈述。

使用上一个网页，这里有一个例子：

```
[
  "PostgreSQL Performance Tuning Guide", // heading 1
  "Connection Settings", // heading 2
  "Maximum connections", // heading 3,
  "Each connection uses a new process.", // necessary to understand the sentence
  // ...skipped unnecessary sentences
  "Due to this design, connections use more resources than in a thread-based system, and so require extra consideration.", // the target sentence
].join("\n")
```

另一个具有多个跳转的示例：

```
[
  "PostgreSQL Performance Tuning Guide", // heading 1
  "Connection Settings", // heading 2
  "Maximum connections", // heading 3
  "Each connection uses a new process.", // to understand the next line
  "This is different to most other database systems.", // to understand the next line
  "Therefore, the setting may have surprising performance impact.", // the target sentence
].join("\n")
```

在保留上下文的同时进行分块是个难题。Anthropic 有一个有趣的分析，并在[此处](https://www.anthropic.com/news/contextual-retrieval)给出了他们自己的方法。我想尝试的另一种方法是[延迟分块](https://jina.ai/news/late-chunking-in-long-context-embedding-models/) 。

## Initial results

我构建了一个用户体验（UX）界面，用于在我的沙盒环境中可视化页面并与之交互，以及测试查询。结果看起来相当不错。

例如，在 [此 S3 文档页面](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html) 上，使用自然语言问题能从不同的代码片段中得到多个相关的直接答案，而不仅仅是关键词匹配，这些代码片段并不只是简单地位于与查询直接相关的部分：

[![Prototype search results for "when should i use multipart uploads?" over S3 documentation.](https://blog.wilsonl.in/search-engine/poc-when-should-i-use-multipart-uploads.png)](https://blog.wilsonl.in/search-engine/poc-when-should-i-use-multipart-uploads.png)

这是另一个例子，查询 [此网页](https://www.psychologytoday.com/us/blog/understanding-the-anxious-mind/202303/are-you-a-life-optimizer-what-to-do-about-perfectionism) ，搜索引擎匹配到了 “这不值得”，可以说这是最相关且直接的回应，但没有上下文的话就没有意义，因此不会被匹配到。其他匹配结果也为该查询提供了更相关的观点。

[![Prototype search results for "is perfectionism worth it?" over a blog post on perfectionism.](https://blog.wilsonl.in/search-engine/poc-is-perfectionism-worth-it.png)](https://blog.wilsonl.in/search-engine/poc-is-perfectionism-worth-it.png)

以下是更多示例，其中查询的关键词与答案有很大不同，且没有直接提及答案，但却是很好的匹配：

[![](https://blog.wilsonl.in/search-engine/poc-im-charged-for-invisible-space.png)](https://blog.wilsonl.in/search-engine/poc-im-charged-for-invisible-space.png)

我在试图弄清楚为什么我的计费使用量高于实际使用量。搜索引擎在不使用我不了解的答案中的词汇的情况下为我找到了相关答案。

[![](https://blog.wilsonl.in/search-engine/poc-race-conditions.png)](https://blog.wilsonl.in/search-engine/poc-race-conditions.png)

尽管文章未提及“竞态条件”，但该搜索引擎仍能够提取与竞态条件*概念相关*的信息。

[![](https://blog.wilsonl.in/search-engine/poc-can-i-use-lua.png)](https://blog.wilsonl.in/search-engine/poc-can-i-use-lua.png)

亚马逊网络服务（AWS）没有针对 Lua 的软件开发工具包（SDK）。它并没有直接给出否定或无意义的结果，而是指出我可以使用对所有语言都可用的 REST API。

[![](https://blog.wilsonl.in/search-engine/poc-what-do-i-pay-for.png)](https://blog.wilsonl.in/search-engine/poc-what-do-i-pay-for.png)

我需要支付什么费用？在不了解围绕 S3 多部分上传收费的相关词汇和概念，且没有名为“你需要支付的费用”的文章章节的情况下，搜索引擎却知道该呈现什么内容。

[![](https://blog.wilsonl.in/search-engine/poc-how-can-i-attach-some-human-english-comment-to-a-file.png)](https://blog.wilsonl.in/search-engine/poc-how-can-i-attach-some-human-english-comment-to-a-file.png)

搜索引擎解释了 S3 中的文件是什么，以及我如何实现我的目标。请注意，查询中的关键词与结果基本上没有重叠。

那些有直接（但并非精确关键词匹配）答案的更直接的查询也能得到很好的匹配：

[![Screenshot of first result of query "can i know upload without knowing size ahead of time".](https://blog.wilsonl.in/search-engine/poc-can-i-upload-without-knowing-size-ahead-of-time.png)](https://blog.wilsonl.in/search-engine/poc-can-i-upload-without-knowing-size-ahead-of-time.png) [![Screenshot of first result of query "can uploads be interrupted".](https://blog.wilsonl.in/search-engine/poc-can-uploads-be-interrupted.png)](https://blog.wilsonl.in/search-engine/poc-can-uploads-be-interrupted.png)

许多重要的代码片段和语句都包含在丰富的标记中，如嵌套的表格行、列表和定义：

[![Screenshot of query for "what permissions do i need to upload".](https://blog.wilsonl.in/search-engine/poc-what-permissions-do-i-need-to-upload.png)](https://blog.wilsonl.in/search-engine/poc-what-permissions-do-i-need-to-upload.png)

## Crawler

我确信这个流程和生成的嵌入向量能带来不错的结果，于是我开始着手构建实际的搜索引擎，首先从一个 Node.js 爬虫程序开始。一些要求如下：

-   由于请求所需的时间差异很大，可能需要一种用于分配任务的工作窃取形式。
-   不要轻信任何东西：控制并验证 DNS 解析、URL、重定向、头部信息以及定时器。
-   源站点通常会根据 IP 进行速率限制，因此任务应分布在多个爬虫上，并处理特定于源站点的速率限制。
-   大量请求 = 大量潜在的内存泄漏。严格管理资源（套接字、长连接、池），并尽可能使用流来使内存保持为 O(1)。

最终采用的方法是：

-   每个源最多 N 个并发 Promise，由于主要工作负载是异步 I/O，这些 Promise 本质上就是轻量级线程
-   自我设定的滑动窗口以及针对每个源的并发速率限制，请求之间存在抖动延迟，失败时采用指数退避策略
-   使用 Node.js 流来获取、解压缩并以固定大小的缓冲区进行摄取，以确保内存使用的稳定性

每个节点从数据库中跨域抓取一组多样化的 URL，然后在绿色线程之间随机进行工作窃取。与简单地从全局爬取队列中按顺序轮询相比，这种多级随机队列设置减少了因需要全局协调、由于高吞吐量特性导致的频繁轮询以及对任何单个源的过度访问而产生的争用。

在轮询获取更多 URL 时，被限制速率的源会被排除，并且现有的轮询任务会被放回全局队列。

[![Diagram of multi-level crawl queues.](https://blog.wilsonl.in/search-engine/multi-level-crawl-queues.png)](https://blog.wilsonl.in/search-engine/multi-level-crawl-queues.png)

一个令人惊讶的故障点是 DNS。EAI\_AGAIN 和 SERVFAIL 导致了相当数量的故障。每次爬网的 DNS 解析都是手动完成的，以验证解析出的 IP 不是私有 IP，避免泄露内部数据。

通常我会忽略大量令人惊讶的细节。例如，URL 看似简单直接，但实际上处理起来可能很微妙。在进入系统之前，所有 URL 都经过了严格处理，因为它们对于许多系统和记录都至关重要：

-   它们必须具有 `https:` 协议，而不是 `ftp:`、`data:`、`javascript:` 等。
-   它们必须有有效的[有效顶级域名（eTLD）](https://publicsuffix.org/list/) 和[主机名](https://en.wikipedia.org/wiki/Hostname#Syntax) ，并且不能有端口、用户名或密码。
-   规范化用于去重。所有组件都先进行百分号解码，然后使用最小一致字符集重新编码。查询参数会被丢弃或排序。源地址会被转换为小写。
-   有些网址极其长，而且你可能会遇到诸如 HTTP 标头和数据库索引页面大小等罕见的限制。
-   有些 URL 还包含一些你可能想不到会出现在 URL 中的[奇怪字符](https://en.wikipedia.org/wiki/C0_and_C1_control_codes) ，但下游的系统（如 [PostgreSQL](https://www.postgresql.org/docs/current/datatype-character.html#:~:text=the%20character%20with%20code%20zero%20\(sometimes%20called%20NUL\)%20cannot%20be%20stored) 和 [SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html)）会拒绝这些 URL。

## Pipeline

[![Search engine pipeline state and data flow diagram.](https://blog.wilsonl.in/search-engine/pipeline.png)](https://blog.wilsonl.in/search-engine/pipeline.png)

每个网页都存储在 PostgreSQL 中，其状态如上图所示。工作进程会直接使用 `SELECT ... FOR UPDATE SKIP LOCKED` 事务从 PostgreSQL 进行轮询，一旦完成就转换状态。然而，大量的长事务以及来自许多远程连接的单行列锁定→读取→更新查询在 PostgreSQL 中效率不高，因此引入了一个 Rust 协调器服务：

-   将整个队列状态保存在内存中，并高效地跟踪心跳和过期情况。
-   通过更快的内存状态来处理锁定、状态转换和完整性。
-   通过复用 HTTP/2 与客户端使用高效的远程过程调用（RPC），并且与数据库建立的 PostgreSQL 连接很少，采用排队批量插入更新。

这个内存队列专为高吞吐量而设计：

-   一个 `Arc<Mutex<Task>>` 在三个数据结构之间共享：
    -   用于获取和变更任务的哈希映射`任务 ID -> 任务` 。
    -   基于可见性超时进行键控的任务二进制堆，用于使过期的轮询任务再次可用。
    -   按来源分组（`origin` -> `该来源中的任务列表` ），以便在各来源间进行公平调度，并设有单独跟踪的可用来源列表。
    -   在原始列表中进行随机轮询，对自索引位置进行 O(1) [`swap_remove`](https://doc.rust-lang.org/std/vec/struct.Vec.html#method.swap_remove) 操作（这也意味着只需更新另一个自索引位置，无需大量逐个下移）。
-   采用了优雅的漂移处理而非全局锁定：
    -   通过每个任务的锁来维护原子性。
    -   超时（例如心跳）的变化不会改变堆；相反，当后台循环遍历超时期望堆时，会重新检查最新的过期时间。
    -   一个变为空的可用源在下次访问（轮询器）之前不会从可用源列表中移除，从而分摊成本。
    -   \`Arc>\` 是真相的来源；数据结构仅仅是可能过时的索引（例如堆中已完成的任务、列表中为空的源、虚拟轮询的任务）。

结果是所有操作都具有高效的亚线性复杂度：

| Operation | Time complexity | Process |
| --- | --- | --- |
| **Push task** | O(1) | 哈希映射插入 + 向量追加到原始列表 + 更新任务的存储索引 |
| **Pop random** | O(k) average  
  *k = 排除的来源* | 从原点列表的 O(1)随机索引 → 从原点任务的 O(1)随机索引  
→ 使用存储索引实现 O(1)的交换删除 → O(log n)的堆推送 |
| **Complete task** | O(1) | 哈希映射查找 → 锁定任务 → 状态转换  
→ 使用存储的索引从原始列表中进行 O(1)的交换删除操作 |
| **Heartbeat** | O(1) | 哈希映射查找 → 就地更新超时（无需重建堆） |
| **Release timeouts** | O(log n) per task | 堆弹出 → 检查是否过期  
→ 如果是：以 O(1) 的时间复杂度将其推送到源列表；如果否：以 O(log n) 的时间复杂度重新推送到堆中 |
| **Find task** | O(1) |   直接哈希映射查找 |

每个任务仅占用大约 100 字节的内存，因此尽管理论上受内存限制，但实际上在一台典型的 128GB 内存服务器上，它可以扩展到 10 亿个活跃任务。

这也有助于实现前面描述的多级随机队列设置。数千个爬虫频繁轮询一组随机的 URL，这些 URL 会避开任意一组源，同时还要回传速率受限的源 URL，这是一个难以优化的数据库查询，但如果通过中央协调器将全局状态保存在内存中，就会更加直接。

一个有趣的优化方法是尝试减少在内存中缓冲如此多 URL 对内存的影响：

-   [实习](https://en.wikipedia.org/wiki/String_interning) ：避免了复制，这很有帮助。
-   [Zstd](https://en.wikipedia.org/wiki/Zstd)：即使使用自定义训练的字典，在小字符串上的效果也不佳。
-   [前缀树（Trie）](https://en.wikipedia.org/wiki/Trie)：在实际应用中，由于指针宽度、 usize 偏移量、稀疏性和节点分配等因素，会占用大量内存。
-   自定义压缩算法，该算法尝试在 URL 组件中查找模式：UUID、枚举、Base64 等。这在 CPU 方面开销很大。

最终，这个内存系统被淘汰，转而采用了队列服务。SQS 的并发速率限制很低，无法跟上整个流程中数千个工作线程的吞吐量。SQS 的成本也很高， [按每条消息收费](https://aws.amazon.com/sqs/pricing/) 。我决定编写一个[基于 RocksDB 的开源队列](https://github.com/wilsonzlin/queued) ，它和 SQS 一样简单，同时能够在单个节点上每秒执行 30 万次操作。

为了坚持多级随机/公平调度，我为爬取任务附加了一个随机初始 [可见性超时](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html) ，以近似洗牌，从而在任何轮询任务序列中实现来源多样化。爬虫节点轮询一个非常大的批次，而不是逐个轮询，通过多级队列方法继续避免过度的全局轮询。

## Storage

由于甲骨文云每月有 10TB 的免费流量，其出口成本极低，我最初选择它来满足基础设施需求。因为我要存储数 TB 的数据，这让我很放心，如果我需要迁移或导出数据（例如进行处理、备份），我的钱包不会瘪瘪。而且它的计算成本也比其他云便宜得多，同时它仍然是一家可靠的大型供应商。

他们的对象存储服务是存储原始页面和派生数据的初始场所，其功能和性能与 S3 类似。然而，由于大尺寸写入的频率，它很快就遇到了扩展问题，这是意料之中的，因为像 S3 这样的服务具有相当低的速率限制——存在 [硬限制](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance.html) ，但也有动态的 per-account/bucket 配额，并且在内部自动扩展期间会出现大量 500 错误。由于它是一个托管的共享服务，我无法手动扩展或调整这些。

在那之后的一段时间里，我将二进制大对象（blob）与常规行数据一起存储在 PostgreSQL 中，因为它可以手动扩展，而且我已经设置好了。通常情况下你不会这么做，因为胖列可能会导致一些瓶颈问题，比如在日志记录方面的写放大、缓存膨胀以及超出磁盘页面大小。不过，PostgreSQL 确实有一种叫做 [TOAST](https://www.postgresql.org/docs/current/storage-toast.html) 的机制，它会将这些大的二进制大对象进行分块，并存储在一个单独的表中“另行处理”，从而缓解其中的一些问题。

这种方法在一段时间内有效，但最终也遇到了限制。PostgreSQL 已经难以跟上管道高处理速率下仅插入元数据行的操作，而以这些速率写入大二进制对象的额外工作量使其不堪重负——我看到爬取数据的摄取过程需要几分钟，并且频繁进行清理以减少膨胀，这导致数据库完全停滞。为了避免迁移，人们进行了一系列尝试来扩展 PostgreSQL：

-   避免使用任何索引、事务、外键/约束、连接、序列、复杂查询、宽列或大表。
-   将所有插入操作转移到 Rust 协调器 RPC 服务，该服务会集中连接并对其进行排队和 [批处理](https://www.tigerdata.com/blog/boosting-postgres-insert-performance) 。
-   迁移到配备低延迟 NVMe 固态硬盘和[原子写入](https://www.sqlite.org/atomiccommit.html)的裸机。
-   使用 [Citus](https://www.citusdata.com/)，它保留了 PostgreSQL 的设计约束，但会拆分为水平分片以扩展写入并分散开销。

但从根本上来说，这种工作负载并不适合 PostgreSQL 的设计方式：

-   更新会创建新的元组而不是就地更新，这会导致数据膨胀，需要进行清理操作，而清理操作会竞争 I/O，但通过[多版本并发控制（MVCC）](https://www.postgresql.org/docs/current/mvcc.html) 实现具有 ACID 保证的非阻塞并发时这是必要的。
-   每次插入更新操作都是对一个可能随机的页面进行树查找（鉴于爬取的 URL 没有可预测性），会访问许多随机页面（导致缓存颠簸），并且只为一个条目重写整个页面（写入放大）。
-   每次插入或更新操作还需要检查约束条件并修改单独的索引树（例如主键、唯一性索引）。
-   由于预写日志（WAL），这些更改会被写入两次，预写日志在更大的页面（而非记录）级别提供[损坏写入保护](https://wiki.postgresql.org/wiki/Full_page_writes) ，从而增加了写入放大。
-   连接是资源密集型过程，有大量状态跟踪，且按顺序执行，不适用于数千个少量行写入器的优化。
-   SQL 查询非常通用且功能强大，所以诸如网络协议、查询规划和事务隔离等方面，对于简单的 INSERT 操作会增加大量开销。

使用 Citus 对于减轻这些开销并没有太大帮助，因为与原始磁盘 I/O 相比，它们导致写入速度慢了几个数量级。它还增加了一个协调器、分布式查询规划器和集群内连接，而我对这些并不太能控制或理解。PostgreSQL 为关系型和 ACID 功能做了很多工作，但我需要的是一个具有快速写入性能的精简键值存储。所以我转向了 [RocksDB](https://rocksdb.org/) 来存储记录/元数据和二进制大对象。

RocksDB 直接解决了上述许多限制：

-   写入操作按顺序写入 WAL（记录的，而非页面的），并在[内存](https://github.com/facebook/rocksdb/wiki/Memtable)中保持排序。只有在很久之后，它们才会在后台按顺序作为 SST 写入磁盘。这避免了大量的随机 I/O 和写入放大。
-   快速简单的插入路径，直接进入内存表，跳过许多关系型数据库管理系统的机制。
-   直接进行 [可嵌入库](https://docs.rs/rocksdb/latest/rocksdb/) 函数调用，而不是通过有线协议和连接。我可以选择一种更高效、更简单的多路复用协议，如 HTTP/2，它可以扩展到数千个插入器。
-   它仍然具有诸如即时可见写入、原子批处理更新以及[快照一致性](https://github.com/facebook/rocksdb/wiki/Iterator#consistent-view)等特性。

由于之前因写入速度慢而有过相关经历和迁移的困扰，我从一开始就对 RocksDB 进行配置，以优化写入操作，并充分利用 NVMe 固态硬盘。

我使用的 RocksDB 配置

```
fn rocksdb_opts() -> rocksdb::Options {
  let mut opt = rocksdb::Options::default();
  // Maximize disk I/O utilization.
  opt.set_max_background_jobs(num_cpus::get() as i32 * 2);
  opt.set_bytes_per_sync(1024 * 1024 * 4);

  // Enable BlobDB.
  opt.set_enable_blob_files(true);
  opt.set_min_blob_size(1024);
  opt.set_enable_blob_gc(true);

  // Use more RAM for better performance.
  // https://github.com/facebook/rocksdb/wiki/Block-Cache.
  let block_cache = Cache::new_lru_cache(1024 * 1024 * 1024 * 32);
  let mut bbt_opt = BlockBasedOptions::default();
  opt.set_write_buffer_size(1024 * 1024 * 256);

  // Enable partitioned index filters: https://github.com/facebook/rocksdb/wiki/Partitioned-Index-Filters
  // NOTE: We cannot use HashSearch as that requires a prefix extractor.
  bbt_opt.set_index_type(BlockBasedIndexType::TwoLevelIndexSearch);
  bbt_opt.set_bloom_filter(10.0, false);
  bbt_opt.set_partition_filters(true);
  bbt_opt.set_metadata_block_size(4096);
  bbt_opt.set_cache_index_and_filter_blocks(true);
  bbt_opt.set_pin_top_level_index_and_filter(true);
  bbt_opt.set_pin_l0_filter_and_index_blocks_in_cache(true);

  // Optimize for point lookups.
  // Don't use `optimize_for_point_lookup()`, which just sets a custom BlockBasedOptions; we'll use our own custom options instead.
  // NOTE: We don't enable memtable_whole_key_filtering as that uses a lot more memory for an unknown performance benefit (key lookups in memory should already be fast, and memtables should not be that large).
  // https://github.com/facebook/rocksdb/wiki/BlobDB#performance-tuning
  bbt_opt.set_block_size(1024 * 64);
  bbt_opt.set_block_cache(&block_cache);
  bbt_opt.set_format_version(5);
  // https://github.com/facebook/rocksdb/blob/25b08eb4386768b05a0748bfdb505ab58921281a/options/options.cc#L615.
  bbt_opt.set_data_block_index_type(DataBlockIndexType::BinaryAndHash);
  bbt_opt.set_data_block_hash_ratio(0.5);
  // https://github.com/facebook/rocksdb/wiki/RocksDB-Bloom-Filter#ribbon-filter.
  // Don't set this too high, as benefits drop off exponentially while memory increases linearly.
  bbt_opt.set_ribbon_filter(10.0);
  opt.set_block_based_table_factory(&bbt_opt);
  opt
}
```

我针对点查找（主要的访问模式）对其进行了优化：布隆过滤器、哈希索引、分区索引和大型块缓存。对于写入操作，使用了大型写入缓冲区和线程池来充分利用磁盘 I/O。

RocksDB 最有趣的特性是 [BlobDB](https://github.com/facebook/rocksdb/wiki/BlobDB)。由于会加剧写放大，大值可能会对[压缩](https://github.com/facebook/rocksdb/wiki/Compaction)性能产生过大影响。BlobDB 通过将大对象存储在普通 SST 之外的单独文件中来缓解这一问题，在那里只留下小指针。由于我有大量的大对象，这一点非常重要，并且使得可以将 RocksDB 用于元数据/记录和大对象。

最终我遇到了磁盘 I/O 限制，所以我决定通过分片来进行扩展。一种常见的方法是[一致性哈希](https://en.wikipedia.org/wiki/Consistent_hashing) ，它允许分片和节点根据未来的增长或节点丢失进行扩展和收缩。然而，它的实现并不简单，因此很难通过简单性来保证正确性，尤其是在插入和重新平衡操作方面。相反，我选择了固定的 64 个 RocksDB 分片，这简化了操作和客户端路由，同时为可预见的未来提供了足够的分布容量。

读写操作通过键的 [xxHash](https://xxhash.com/) 进行路由。由于节点集几乎从不改变，分片映射只是一个随代码分发的静态文件，无需元数据或发现服务。在进行这种分片之后，协调器服务很快成为瓶颈，因为 64 个分片的 I/O 流量和请求量都要经过一台机器，所以后来它被弃用，客户端直接对 RocksDB 分片节点进行读写操作。

为了表示行，我使用了由 Serde 定义的类型以及自定义紧凑键，以减少反序列化/序列化时间和存储空间。我使用了 [MessagePack](https://msgpack.org/index.html)，而不是[一种更快、更紧凑的](https://github.com/djkoloski/rust_serialization_benchmark)格式，因为那些格式通常与 Rust 绑定，并且对字段顺序敏感，而我选择了额外的保障措施来应对这两个问题。

```
#[skip_serializing_none]
#[derive(Serialize, Deserialize, Debug)]
pub struct Resource {
  #[serde(rename = "1")]
  pub state: ResourceState,
  #[serde(rename = "2")]
  pub http_status: Option<u16>,
  #[serde(rename = "3")]
  pub original_content_encoding: Option<String>,
  ..
}
```

在其峰值时，该系统每秒可处理来自数千个客户端（爬虫、解析器、矢量化器）的 20 万次写入。每个网页不仅包含原始的 HTML 源代码，还包括规范化数据、上下文相关的块、数百个高维嵌入以及大量元数据。

## Service mesh

随着系统复杂度的增加，我需要一种方法来发现服务实例，而不是硬编码 IP 地址，并在互联网上进行安全通信（因为我开始利用其他地方更便宜的资源）。

我使用相互传输层安全协议（mTLS）作为提供加密和认证的通用方式，这比为每个服务单独处理大量协议和认证方法要简单。生成了一个自定义根证书颁发机构（CA），然后在操作系统层面为每个节点生成证书和密钥。

采用了 HTTP/2 作为协议，以及 MessagePack 作为序列化机制：二进制、自描述，并且支持时间戳和映射。这种框架使得通过一个经过优化的通用内部客户端软件开发工具包（SDK）能够轻松地设置和使用新服务。HTTP/2 是一个不错的协议，因为我在跨越节点的公共互联网上有许多长而粗的管道，虽然不像私有数据中心网络那样具有低延迟或高可靠性。它提供了多路复用以及简单的请求和重试语义，这是相对于许多其他协议（例如 PostgreSQL）的一个优势。基于 mTLS + HTTP/2 的远程过程调用（RPC）使得安全的私有服务调用变得简单，无论我的基础设施位于何处。

还实现了一个内部 DNS 服务：一个用于查看和编辑内部 DNS 条目的控制平面，以及在所有节点上运行的一个 [CoreDNS](https://coredns.io/) 守护进程，用于处理 DNS 请求，拦截对内部 DNS 名称的请求并代理其余请求。我最初尝试在内部基础设施中简单地使用公共 DNS 名称，但这太不可靠了，许多内部请求仅仅因为短暂的 DNS 解析超时或失败而失败。

我也试过 ZeroTier 和 Tailscale，它们提供了一个用于加密和认证通信、DNS、路由及发现的单一软件包。但它们在大规模应用时经常出现问题（加入、传播和发现变化时出现延迟和瞬时错误），并且存在流量限制和开销——当时，它们无法轻松使 10 Gbps 连接达到饱和，还消耗大量 CPU 资源。由于涉及更低的网络堆栈层，它们在 Docker 容器中也更难使用。最终，HTTP + mTLS 要直接得多，不需要特殊的网络配置，几乎没有开销就能使连接达到饱和。它也更安全，类似于零信任，因为服务可以公开暴露，不依赖通过路由、防火墙或密钥的安全机制，而这些机制很容易配置错误或泄露。

systemd 服务用于设置定义（例如环境变量、限制）、计费（通过 cgroups）以及管理工具和日志（通过 journald）。这似乎是一个不错的权衡：

-   简单却全面，无需自定义脚本和工作流程。易于在任何开箱即用的 Linux 机器上进行调试。
-   轻量级框架：声明式、结构化，但不涉及构建镜像、仓库、部署意见等内容。
-   无性能开销且具有多层抽象。

## GPU buildout

我的初始原型使用了通过 API 获取的 OpenAI 嵌入。随着规模扩大，这在经济上变得不可行，所以我开始自己进行推理。

为了寻找最具成本效益的可扩展解决方案，我发现了 [Runpod](https://www.runpod.io/)，他们提供性价比高的 GPU，比如 RTX 4090，每小时的价格比 AWS 和 Lambda 便宜得多。这些 GPU 在三级数据中心运行，网络稳定快速，且有大量可靠的计算能力。

一个关键问题是 GPU 效率：它们很昂贵，所以我想确保它们得到充分利用。从本质上讲，这意味着推理前后的操作不应阻塞 GPU：

-   轮询未决任务并获取输入数据
-   解析和分词输入数据
-   处理和存储输出嵌入

这些 Runpod 工作节点离我的主要基础设施很远，所以长距离的胖管道是个问题。延迟意味着 GPU 在输入和输出传输完成之前就能完成推理。因此，我实现了一个围绕 Python 核心推理的 Rust 管道，它可以：

-   异步操作每个阶段，而不阻塞上游步骤
-   信号反压以暂停上游阶段，避免系统资源不堪重负

这些特性带来了动态调优的好处——我无需基于特定硬件和数据进行手动调优或限制；管道会在任何子系统能够处理的速度下尽快填满，然后发出反压信号以防止溢出，从而自动实现最高效率，同时还能应对任何突发情况和减速（例如网络中断）。每个阶段使用不同的硬件（CPU、网络、内存、GPU），因此简单的串行执行会不必要地阻塞和闲置资源。

一个小特性是使用跨命名管道的进程间通信（IPC）来与 Python 进程进行交互，而不是反复生成子进程、读写文件或启动本地 HTTP/RPC 服务器。如今，我可能会使用 [PyO3](https://github.com/PyO3/pyo3) 或 [candle-rs](https://github.com/huggingface/candle)。

使用任务队列还意味着在工作进程死亡时能自动恢复。这使得使用更便宜的可抢占式工作进程并随时进行扩展和缩减变得轻而易举。结果是，该服务在峰值时能通过 250 个 GPU 每秒生成 10 万个嵌入，平均 GPU 利用率达到 90%。

## Sharded HNSW

我使用 [分层可导航小世界网络（HNSW）](https://github.com/nmslib/hnswlib) 作为低延迟向量搜索的算法和索引。它是一种内存优化的图数据结构，支持亚线性 [近似最近邻（ANN）](https://en.wikipedia.org/wiki/Nearest_neighbor_search) 查询。 [在这篇文章中](https://blog.wilsonl.in/graph-vector-search/) 我将详细介绍 ANN、图算法和 HNSW。

随着 HNSW 索引开始超出单台机器的可用内存，我研究了对其进行扩展的方法。现有的向量数据库在操作上过于复杂，并且由于要满足更广泛的需求，在数据摄取和查询方面速度较慢。它们还需要精细的调优以及对各种索引方法和权衡因素的了解，而这些因素会影响召回率。

我决定继续使用经过验证的 HNSW，并将其均匀分片到 64 个节点，这足以满足可预见未来的扩展需求。由于每个分片是并行查询的，并且仍然是高质量（未量化或降级）的完整 HNSW 索引，所以这保持了相同的低延迟和高精度，同时现在能够扩展到更大的组合索引大小。

然而，这样做的缺点是它需要大量昂贵的随机存取存储器（RAM），并且存在 HNSW 缺乏可更新性的局限性。每当我需要更新索引时，都需要将巨大的 HNSW 索引加载到构建器节点的随机存取存储器中，插入新的嵌入，并进行完整转储。我决定深入研究这个问题，并构建了一个向量数据库，它使用更便宜的磁盘并且可以执行实时图更新，将整个集群缩减到只有一台 128GB 随机存取存储器的机器，并且不需要复杂的更新管道，同时在超过 30 亿个嵌入上仍保持高召回率。它是一个名为 **CoreNN** 的开源向量数据库，我将在 [这篇博客文章](https://blog.wilsonl.in/corenn/) 中详细介绍。

## Optimizing latency

搜索引擎的用户体验很有意思，因为它特别强调响应速度，而非华而不实或复杂的设计。许多搜索引擎给人的感觉与典型的现代应用程序不同：它们没有加载指示器和动画，设计简洁，交互性不强，就像“传统”网页一样流式加载。因此，即时结果是用户对搜索引擎的基本期望。为了优化响应能力，我试图在堆栈的各个层面减少延迟。

我使用了 [Cloudflare Argo](https://www.cloudflare.com/en-au/application-services/products/argo-smart-routing/)，以便用户能够连接到距离更近的边缘 PoP 服务器，这些服务器随后通过 Cloudflare 内部的 [专用网络](https://en.wikipedia.org/wiki/Wide_area_network) 而非互联网进行路由，这意味着跳数、 [丢包](https://en.wikipedia.org/wiki/Packet_loss) 和拥塞更少。Cloudflare 在这些边缘 PoP 点还使用了 HTTP/3，这减少了握手开销和队头阻塞。在全球范围内设置读副本成本太高。

应用服务器不是进行多次客户端-服务器往返 API 请求，而是获取所有必要的数据，并在服务器端准备好整个响应页面，进行了压缩和精简。一个端点处理程序使用 Promise（在后台立即开始执行）在需要获取数据的子树上定义渲染树，一个自定义的服务器端渲染框架在遍历过程中急切地流式输出 HTML，仅在到达时等待每个 Promise，以免阻塞就绪内容。这样做是为了减少首次内容绘制时间（TTFB），并通过流式输入使页面感觉响应迅速，而不是在长时间延迟后一次性全部显示。

```
class Element {
  // Core rendering loop.
  private async streamInner(out: Writable) {
    // Write eagerly.
    out.write(`<${this.tagName}`);
    for (const [n, v] of Object.entries(this.attrs)) {
      out.write(` ${htmlEscape(n)}="${htmlEscape(v)}"`);
    }
    out.write(">");
    for (const cRaw of this.children) {
      // Lazily await.
      const c = await cRaw;
      if (typeof c == "string") {
        out.write(htmlEscape(c));
      } else {
        await c.streamInner(out);
      }
    }
    if (!VOID_ELEMS.has(this.tagName)) {
      out.write(`</${this.tagName}>`);
    }
  }
}

// Example endpoint definition.
const endpoint = () => (
  h(".page",
    // Subtrees can be Promises.
    (async () => {
      const results = await fetchResults();
      return h(".results", ...results.map(r => (
        h(".result", ...)
      )));
    })(),
    // All Promises begin executing concurrently without delay.
    (async () => {
      const profile = await fetchProfile();
      ...
    })(),
  ),
);
```

JSX 可能会更优雅一些，但那样就需要做一些工作来定制转译过程和运行时（以处理 Promise）。

在内部服务的吞吐量方面，RocksDB 和 HNSW 分片已经提供了充足的读取能力。针对查询所做的唯一扩展是引入了一个用于为查询生成嵌入的矢量化服务。该服务运行在 CPU 上，因为远程 GPU 的有限批处理和延迟抵消了通过快速浮点运算带来的任何收益。

## Knowledge graph

我想要重现显示在搜索结果右侧的 [知识面板](https://support.google.com/knowledgepanel/answer/9163198?hl=en) 。维基百科和维基数据似乎是填充此面板的良好数据源，但它们的 API 速度慢且有速率限制。幸运的是，它们会定期提供所有数据的 [完整导出](https://dumps.wikimedia.org/) ，我利用这些导出数据构建了本地优化索引和查询服务。

维基百科为文章（例如 [澳大利亚](https://en.wikipedia.org/api/rest_v1/page/summary/Australia) ）提供了很好的结构化数据，其中包含相关图片、摘要以及对维基数据 [条目](https://www.wikidata.org/wiki/Help:Items) 的引用。这些数据具有相关属性，描述了它们与其他实体的关系，有助于在知识面板中填充 “快速事实”（例如出生日期）。综合起来，它们构成了一个用于知识面板的良好初始系统：

-   文章构成了知识面板的基础数据集。
-   标题和摘要相结合，生成嵌入向量，用于检索相关知识面板，以便在查询时显示。
-   图像、标题、描述和摘要显示在面板的上半部分。
-   如果存在链接的维基数据项，则会在知识库中查找该实体，并检索特定的关联属性。

并非所有维基百科文章都应显示为知识面板（例如列表），并且嵌入检索可能无法给出最相关的结果（例如显示特定的相邻文章而不是基础/更广泛的主题）。同样，并非所有维基数据属性都值得展示。还有许多其他数据源可供纳入。因此仍有很多改进空间，但作为一个良好的起点，它运行得很好。

## SERP

最终生成的搜索引擎结果页面（ [搜索结果页面](https://en.wikipedia.org/wiki/Search_engine_results_page) ）如下所示：

[![Screenshot of final SERP without AI features.](https://blog.wilsonl.in/search-engine/serp-rocksdb.png)](https://blog.wilsonl.in/search-engine/serp-rocksdb.png)

我追求简洁简约的外观，以营造“重实质而非形式”的美感。具体的语句片段会出现在诸如文档和维基百科等“事实”页面下，以便为查询提供快速参考和答案。另一个例子：

[![Screenshot of SERP with statement snippets.](https://blog.wilsonl.in/search-engine/serp-protein-in-chicken.png)](https://blog.wilsonl.in/search-engine/serp-protein-in-chicken.png)

很棒的是，这里几乎没有搜索引擎优化垃圾信息。例如，我在一个知名搜索引擎上查询了“最佳编程博客”，并将其与我的搜索结果进行了比较：

[![](https://blog.wilsonl.in/search-engine/serp-blogs-theirs.png)](https://blog.wilsonl.in/search-engine/serp-blogs-theirs.png)

来自一个主流搜索引擎的结果。

[![](https://blog.wilsonl.in/search-engine/serp-blogs-mine.png)](https://blog.wilsonl.in/search-engine/serp-blogs-mine.png)

我的搜索引擎的结果。

以下是一个围绕某个查询找到一些有趣的文章和见解的示例：

[![Screenshot of SERP for "the case for/against crypto" query.](https://blog.wilsonl.in/search-engine/serp-crypto.png)](https://blog.wilsonl.in/search-engine/serp-crypto.png)

如开篇所述，该搜索引擎能够理解非常复杂的查询，包括关于各种想法的完整段落。例如，我输入了一段来自大语言模型（LLM）讨论的完整段落，然后找到了一些围绕该段落及相关主题的有趣的高质量文章：

[![Screenshot of SERP for a paragraph about self-worth and high achievers.](https://blog.wilsonl.in/search-engine/serp-paragraph.png)](https://blog.wilsonl.in/search-engine/serp-paragraph.png)

上述用户界面来自现代化的 [实时演示](https://blog.wilsonl.in/search-engine/#live-demo) 。

### AI assistant

由于大语言模型（LLMs）在那个时候开始兴起（此后一直在发展），我决定看看是否可以添加一些微妙但有用的人工智能功能。我认为它们可以在三个方面有所帮助：

-   针对无需调研的直接问题提供非常快速简洁的答案。
-   与人工智能助手进行对话。
-   总结与查询相关的结果。

它带来了有益的扩充，同时又没有破坏搜索体验

[![](https://blog.wilsonl.in/search-engine/serp-ai-s3.png)](https://blog.wilsonl.in/search-engine/serp-ai-s3.png)

人工智能功能提供快速答案、相关问题以及更具针对性的摘要，同时仍保持主要体验不变。

[![](https://blog.wilsonl.in/search-engine/serp-guarantee-clause.png)](https://blog.wilsonl.in/search-engine/serp-guarantee-clause.png)

我发现语句片段对官方参考很有帮助，而人工智能能提供快速直接的答案。

我发现它对编程查询特别有用，在编程查询中，我常常知道正确的做法，只需要快速复习一下。人工智能快速回答非常简洁且切中要点，这符合我的需求。

[![](https://blog.wilsonl.in/search-engine/serp-ai-go-init-map.png)](https://blog.wilsonl.in/search-engine/serp-ai-go-init-map.png)

即使对于更复杂的查询，它也能保持清晰，而如果你想深入了解，高质量的结果仍会排在首位：

[![](https://blog.wilsonl.in/search-engine/serp-parted.png)](https://blog.wilsonl.in/search-engine/serp-parted.png)

### State tracking

跟踪点击对于提高搜索质量以及发现“盲区”、垃圾邮件结果和排名不佳的情况很有用。为防止滥用，所有结果都通过一个带有 AES-256-GCM 加密数据字符串的 `/act`URL，该字符串包含重要的结果数据，用于跟踪重要指标，然后重定向到结果 URL。

由于该应用完全是服务器端渲染（SSR）的，所以它使用了 [PRG](https://en.wikipedia.org/wiki/Post/Redirect/Get) 来处理客户端操作。通常，在操作后重定向时需要显示或更改一些用户体验，以向用户表明结果。这意味着需要在从 POST 到 GET 的过程中持久化某些状态，我决定使用一次性 cookies 来传递状态，从而无需任何服务器端状态。这也使得该应用无需使用 JavaScript。

## Search quality

关于搜索引擎质量，我学到的两件大事：

1.  数量就是质量。如果一个搜索引擎找不到东西，那它就没有用。
2.  爬取和筛选是最困难也是最重要的方面。

事后看来，第一点很明显。这是我的搜索引擎的一个局限性；由于时间和资源的限制，我无法爬取整个网络。鉴于网络和信息空间如此庞大，这意味着搜索结果存在巨大的不均衡差距。

第二点颇具挑战性。互联网的搜索空间如此庞大，以至于确定方向和进行筛选基本上是必不可少的，这样才能避免收集到大量垃圾信息，不至于在网络中越来越偏僻的角落徘徊，或者在某个领域钻研过深而在其他领域留下空白。然而，这是一个难以解决的问题，因为没有明确的起始点或明显的方向/实现方法。它必须处理大量的非结构化数据，这通常意味着要在网络规模上进行复杂的语言和网络分析。自动确定真实性、可信度、原创性、准确性和质量并非易事。

我对如何解决这个问题有一些想法，如果重新开始，我会首先更加重视这方面的研究和开发。众所周知，搜索引擎在对页面进行排名和筛选时会使用 [数千个信号](https://www.google.com/intl/en_us/search/howsearchworks/how-search-works/ranking-results/) ，但我认为基于更新的 Transformer 的内容评估和链接分析方法应该更简单、更具成本效益且更准确。我还相信智能搜索在不久的将来会发挥重要作用，它能够理解、过滤、排名和进行波束搜索，而不仅仅是简单的检索。

在查询时，会应用一些基本的质量过滤器：

-   Non-English.
-   标题或内容为空的页面。
-   Matches [blocklists](https://github.com/hagezi/dns-blocklists).
-   使用[三元组](https://en.wikipedia.org/wiki/Jaccard_index)的[杰卡德相似度](https://en.wikipedia.org/wiki/Trigram)测量的重复项。

## Live demo

[![Screenshot of demo SERP.](https://blog.wilsonl.in/search-engine/serp-demo.png)](https://blog.wilsonl.in/search-engine/serp-demo.png)

我已将搜索引擎重新部署为一个可用的演示，它带有一个更现代的极简应用程序，该应用程序仅专注于搜索结果。

我添加了基于大语言模型（LLM）的重排和过滤功能，由那两个最后的滑块表示。我正在进行实验，看看使用最新的通用智能大语言模型（LLMs）是否能在无需定制模型和训练数据的情况下实现更好的重排和过滤。[Groq](https://groq.com/) 是推理后端，以确保低延迟响应——亚秒级延迟的通用智能似乎是一个强大但被低估的工具。

由于这是一个演示环境，其延迟不像常规生产设置那么低。如在 [搜索质量](https://blog.wilsonl.in/search-engine/#search-quality) 中所述，由于索引不完整和质量过滤，对于各种查询，搜索结果质量会存在明显差距。索引截止时间约为 2023 年 8 月。

在 [search.wilsonl.in](https://search.wilsonl.in/) 体验实时演示。

## Costs

由于这是一个副业项目，我寻找了一些方法来利用鲜为人知的数量级成本效益：

| Component | Typical | Optimized | Comparison |
| --- | --- | --- | --- |
| 向量数据库，768维、数十亿条插入数据 | TurboPuffer 写入 + 存储 — 3578.88 美元 | 赫茨纳拍卖上的 CoreNN（编号 0）——150 美元 |   TurboPuffer 是 23.86 倍 |
| 内存占用大的服务器，每月 TB 级随机存取存储器 | 亚马逊云科技弹性计算云（AWS EC2）r7a 型实例 — 7011.53 美元 | 赫茨纳拍卖 —— 164.00美元 |   亚马逊云服务（AWS）是 42.75 倍 |
| 存储服务器，NVMe 固态硬盘，每月 TB 级 |   亚马逊云科技 i4g —— 243.30 美元 |   赫茨纳拍卖 —— 6.63美元 |   亚马逊网络服务（AWS）是 36.70 倍 |
| 互联网出口，每月 TB 级 |   亚马逊网络服务（AWS）——92.16 美元 |   甲骨文云 —— 8.70美元 |   亚马逊网络服务（AWS）是 10.59 倍 |
|   英伟达 GPU（半精度浮点数），小时 | 亚马逊云科技 g6e（362 万亿次浮点运算）——1.86 美元 | Runpod RTX 4090（660 万亿次浮点运算）——0.79 美元 | 亚马逊云服务（AWS）是 4.28 倍（标准化后） |
| 写入密集型键值存储，每秒十亿次 1KB 写入 | AWS DynamoDB 按需付费 — 5000 美元 | Hetzner 拍卖上的 RocksDB —— 125 美元 |   亚马逊云服务（AWS）是 40 倍 |
| Blob 存储，每秒 10 亿次 100KB 写入 | 亚马逊云科技简单存储服务（AWS S3）的 PUT 操作及存储——5000 美元 + 2300 美元 | Hetzner 拍卖上的 BlobDB —— 250 美元 |   亚马逊云服务（AWS）是 29.2 倍 |
|   队列，十亿条消息 | 亚马逊云科技简单队列服务（推送+轮询+删除）——1200美元 |   [已排队](https://github.com/wilsonzlin/queued) — 约 0 美元 |   亚马逊云服务（AWS）是~∞× |
| 按需使用的 CPU，核心月 | 亚马逊云科技弹性计算云 m7a — 83.52 美元 | 甲骨文云 E4 —— 18.00 美元 |   亚马逊云服务（AWS）是 4.63 倍 |

这些唾手可得的成本节省措施，不仅累计起来节省了大量资金，还降低了项目的门槛，使其在有限的普通资源上也能可行且可扩展。考虑到基础设施和数据的规模，涉及数百个 GPU 和数 TB 的数据，实际成本比我预期的要低，这让我感到惊讶。

然而，由于这是一个自费的单人项目，我不得不停止索引工作。我估计，这个搜索引擎项目大约需要 10000 个每月 5 美元的订阅才能维持下去，对于在世界上现有的少数几个本土搜索索引中再增加一个来说，这个数字不算高，尤其是一个注重质量而非广告的索引。我认为，优化建立一个高质量而非高数量的索引，对于训练 LLMs 也很有用。

当我重新审视成本时，有一个意外发现：OpenAI 对其最新嵌入模型进行批量推理的收费异常低，仅为 [每 100 万个令牌 0.0001 美元](https://platform.openai.com/docs/pricing#embeddings) 。即使保守估计我有 10 亿个爬取的页面，每个页面有 1000 个令牌（长得异常），为所有这些页面生成嵌入也只需花费 **100 美元** 。相比之下，即使使用便宜的 Runpod 按需 GPU 运行我自己的推理，成本也要高出大约 100 倍，更不用说 [其他](https://cohere.com/pricing) [API](https://jina.ai/embeddings/) 了。当时这个服务不可用，所以我无法利用它，但我会在未来的项目中记住这一点。

## 结论与下一步计划

我发现神经嵌入的最大价值之一在于能够找到优质的内容、见解和参考文献。这些内容通常存在于论文和文档中，属于类似文章的内容。那些只是“书签”的查询（例如 `python download windows`）或精确短语匹配不仅需要非常宽泛的索引（包括非常晦涩的页面），而且无法利用智能或理解能力；书签仅可通过 `<title>` 关键字和 URL 子字符串进行索引。鉴于此，我想要探索的一个方向是建立一个更具针对性的索引，专门从网络的长尾中筛选出高质量的有趣内容。一般来说，探索如何拥有针对不同领域和意图的子引擎以获得更准确、定制化、相关且高效的结果是很有价值的。

嵌入似乎远比传统搜索强大得多，看到（当索引有足够数据时）更高质量的结果让我对搜索和检索的未来感到兴奋。对于典型的搜索引擎，你搜索得越具体，结果就越差。能够通过非常具体的查询进行缩小和聚焦，通过模糊的见解和关系找到你确切想要的东西（质量、氛围、观点、想法、主意等），这非常强大且尚未得到充分探索。

尽管大语言模型（LLMs）兴起，但我认为搜索仍将始终发挥作用：大语言模型无法也不应记住所有知识，因为这些参数可用于实现更高的智能和能力。相反，大语言模型可以通过这些高效的密集索引将其卸载到知识表示中，这也意味着更少的幻觉和更及时的信息。也许我们会在开源本地模型之外，拥有社区维护的开源本地搜索索引。

除了 [系统的数据质量保证](https://blog.wilsonl.in/search-engine/#search-quality) 之外，还有其他一些易于实现的优化可供探索：

-   是否有可能利用像 [Common Crawl](https://commoncrawl.org/) 这样现有的爬虫基础设施？
-   能否使用推理速度快 400 倍的静态嵌入（ [静态嵌入](https://huggingface.co/blog/static-embeddings) ）？
-   嵌入模型： [后期分块](https://jina.ai/news/late-chunking-in-long-context-embedding-models/) 、量化、长上下文（以避免分块）、在不重新生成所有嵌入的情况下融入新知识，以及利用 [ONNX](https://onnx.ai/)。
-   利用数据应用程序编程接口、转储文件和协议，而非进行爬取。
-   用 Rust 重写爬虫和解析器以实现数量级的速度提升。

我计划发布关于这个项目的更多详细文章，包括：

-   对抓取的索引进行更深入的分析，包括大规模的视觉和文本内容评估以及语义地图。
-   从爬取的数据构建数据集，以测试搜索引擎的召回率，并将其与 LLMs 记住的知识量进行比较。
-   一个基于 [io\_uring](https://man7.org/linux/man-pages/man7/io_uring.7.html) 从头开始编写但未投入生产的键值存储。
-   一项关于智能体搜索、 [超快速](https://groq.com/)[大语言模型](https://www.cerebras.ai/)重排与过滤，以及生成式用户体验如何改变搜索体验的调查。

你可以订阅我的 [电子邮件时事通讯](https://wilsonzlin.kit.com/) 或 [RSS 源](https://blog.wilsonl.in/rss.xml) ，或者在 [X](https://x.com/wilsonzlin) 上关注我，以便及时了解这些新文章以及我正在进行的其他项目的最新情况。

如果你觉得这篇文章有趣，你可能也会对 [黑客世界](https://blog.wilsonl.in/hackerverse/) 感兴趣，在那里我在一个较小的规模上做了类似的事情（在黑客新闻上），还有 [核心神经网络](https://blog.wilsonl.in/corenn/) ，这是一个在本项目中为应对现有解决方案缺乏可扩展性而开发的十亿级向量数据库。