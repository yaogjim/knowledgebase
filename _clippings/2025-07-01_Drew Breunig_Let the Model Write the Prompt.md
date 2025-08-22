---
title: "Let the Model Write the Prompt"
source: "https://www.dbreunig.com/2025/06/10/let-the-model-write-the-prompt.html"
author:
  - "[[Drew Breunig]]"
published: 2025-06-11
created: 2025-07-01
description: "Notes from a talk I delivered at the 2025 Data + AI Summit, detailing the problem with prompts in your code and how DSPy can make everything better."
tags:
  - "clippings"
---
### 为何应用程序和管道应使用 DSPy

以下是我在 2025 年数据与人工智能峰会上发表的演讲，重点讲述如何使用 DSPy 来定义和优化你的 LLM 任务。

我们以一个简单的地理空间合并问题为例——即判断两个数据点是否指代同一个现实世界中的实体这一挑战——逐步讲解 DSPy 如何简化、改进并使你的 LLM 任务具备未来适应性。

---

![Presentation title slide "Let the Model Write the Prompts - An Intro to DSPy" by Drew Breunig](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_003.jpg)

![Quote about regular expressions creating two problems](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_004.jpg)

我敢肯定你们大多数人都听过这句话，这句老套的话是关于正则表达式如何不能完全解决你的问题……同时最终又会产生一个新的问题需要去处理。尽管我是正则表达式的粉丝（这是另一个话题了），但在过去的18个月里，我一直在反复思考这句话。

![Same quote but replacing "regular expressions" with "prompting"](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_005.jpg)

我认为你可以用“提示”替换“正则表达式”，并得到相同的结果。

现在，我所说的不是临时的聊天机器人提示。比如你可能输入到 ChatGPT 或 Claude 中的问题或任务。不，我指的是你代码中的提示，那些为你的应用程序功能或管道阶段提供动力的提示。在这些情况下，我认为提示所造成的问题和它们所解决的问题一样多。

![Comparison chart showing pros and cons of prompting with happy and sad emoji](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_006.jpg)

一方面，提示词很棒。它们能让任何人描述程序功能和任务，使非技术领域专家能够直接为你的代码做出贡献，这对人工智能驱动的功能非常有帮助。

提示词可以快速轻松地编写。有一种经典的开发模式，就是先快速让某样东西运行起来，然后再去考虑优化它。如今，我们开始看到人们通过一两个提示词迅速实现概念验证，然后将其分解为更简单的阶段——这些阶段通常不会涉及大型语言模型（LLMs）。

最后，提示词是自我记录的。无需注释，只需阅读提示词，你就能大致了解正在发生的事情。这很棒。

但另一方面：提示词糟透了。一个在某个模型上运行良好的提示词，在最新的热门模型上可能就会失效。当你修复这些问题并消除新出现的错误时，你的提示词会越来越长。突然之间，你的提示词可能可读了，但现在你需要喝杯咖啡，花30分钟来梳理清楚其中发生的一切。

而正在发生的是大量重复的模式。我在实际应用中读过很多提示词，我发现它们往往有相似的结构。我们一遍又一遍地处理相同的问题，所有这些都在一个无结构的格式化字符串中，通常夹杂在你的代码之中。

让我给你举个例子，看看这个结构是什么样的：

![Visualization showing breakdown of SWE-Bench prompt components with percentages](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_007.jpg)

在 OpenAI 的《GPT 4.1 提示指南》中，他们分享了“在 SWE-bench 验证中获得最高分所使用的”提示。这是一个很棒的提示，也是该行业中最聪明的团队之一给出的绝佳示例。

我通读了提示并开始进行标注，将段落分成不同部分，我已在此处将其可视化。

只有1%的提示定义了要完成的工作，即任务。19%是思维链指令。32%是格式化指令。对于熟悉应用程序或管道中使用的较长提示的人来说，这应该是一个熟悉的模式。提示，尤其是这样的提示，开始类似于代码。但这种代码没有结构。尽管它是自然语言，但却令人沮丧地晦涩难懂。

![Code editor screenshot showing Python prompting instructions](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_008.jpg)

这就是提示词在实际应用中的样子。它长达数页。

对于致力于开发由大语言模型（LLM）驱动的应用程序的团队，我们可以做得更好。我们可以让其更清晰易读，便于团队协作，更具可问责性，并面向未来。我们只需要让大语言模型来编写提示词。

![Speaker introduction slide for Drew Breunig with professional background](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_009.jpg)

大家好，我是德鲁·布罗伊尼格。我领导数据科学和产品团队，曾助力打造位置智能公司 PlaceIQ（该公司于 2022 年被 Precisely 收购），我还帮助各组织用简单、高效的叙述方式来阐释其技术。目前，我大量的时间都花在了与开放数据项目“序曲地图基金会”的合作上。

今天我们将讲解一个类似于我们在 Overture 处理的示例数据管道问题。

![Map visualization showing San Francisco with Overture Maps Foundation description](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_010.jpg)

但首先，简单介绍一下序曲地图基金会（Overture Maps Foundation）。序曲制作了一个令人惊叹的数据产品：一个免费、易于访问的高质量地理空间数据集。我们每月都会更新 [我们的 6 个主题](https://docs.overturemaps.org/schema/reference/) （地点、交通、建筑、行政区划、地址和基础数据），提高其质量和覆盖范围。我们的数据以地缘镶嵌格式（geoparquet）在亚马逊云服务（AWS）和微软 Azure 上提供（只需 [使用 DuckDB 进行查询](https://docs.overturemaps.org/getting-data/duckdb/) 或 [浏览地图并提取数据](https://explore.overturemaps.org/#15/38.90678/-77.03649) ）。

而且，特别是对于这个群体， [CARTO](https://www.carto.com/) 使 [我们的数据能够在 DataBricks 市场上获取](https://docs.overturemaps.org/getting-data/data-mirrors/databricks/) 。再说一次，这是免费的！去看看吧！

![Grid of company logos showing Overture Maps Foundation members](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_011.jpg)

Overture 由亚马逊、Meta、微软和 TomTom 创立。此后，包括 Esri、优步、Niantic、Mazar 等在内的近 40 家组织也加入进来。这些公司不仅帮助构建我们的数据集，还在其产品中使用这些数据集。仅在 Meta、微软和 TomTom 的地图中，就有数十亿用户受益于 Overture 数据。

![Map showing Databricks location with places data description](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_012.jpg)

今天，我们要讨论一下地点，或者说是兴趣点。这些数据点详细说明了企业、学校、医院、公园、餐馆以及你可能在地图上搜索的任何其他事物。为了构建我们的 Overture Places 数据集，我们采用了多个数据集——来自 Facebook 页面、微软必应地图位置等等——并将它们合并成一个单一的组合集。

![Three icons representing data entry, regional names, and geocoding challenges](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_013.jpg)

*合并* ，即将指代同一现实世界实体的数据点进行合并的行为，是一个难题。兴趣点数据由人类创建，存在不一致性，通常有相似的区域名称，并且可能在地理上放置错误。合并多个数据集是一个永远无法完美解决的难题，但比较地名的任务似乎特别适合由大语言模型（LLM）来完成。

![Pipeline diagram showing progression from spatial clustering to LLM comparison](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_014.jpg)

但是，在很多情况下，我们并不想把整个问题都抛给一个语言模型（LLM）。这里我们要处理数亿次比较，而且需要定期执行这项任务。对于简单的比较，即名称几乎完全匹配且地理空间信息正确的情况，我们可以依靠空间聚类和字符串相似度。但当匹配情况不太确定时，语言模型是我们合并流程中的一个很好的备用步骤。

于是，挑战就变成了如何在序曲团队之间管理这个工作流程。将一个冗长、无结构的提示作为格式化字符串放入我们的代码中，对于来自许多不同公司的众多开发人员来说，可能很难管理。此外，如果没有结构，我们管道中的大语言模型（LLM）阶段可能会变得相当难以控制。

![Title slide introducing DSPy as solution for turning prompting into programming](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_015.jpg)

这时我们可以借助 DSPy。DSPy 让我们能够以编程方式来表达任务，而不是通过提示，从而实现更易于管理的代码库。但它的作用远不止于此……

DSPy 不仅降低了我们代码库的复杂性，还通过将我们的任务与大语言模型（LLMs）解耦，降低了使用大语言模型的复杂性。我来解释一下。

![Philosophical statement about future improvements in AI strategies and models](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_016.jpg)

在我看来，DSPy 的理念可以总结为：“明天会有更好的策略、优化方法和模型。不要依赖于任何一个。”

![Three-pillar diagram showing DSPy's approach to decoupling tasks from LLMs](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_017.jpg)

DSPy 将你的任务与特定的 LLM 以及任何特定的提示或优化策略解耦。

通过将 *任务* 定义为代码而非提示词，我们可以让代码专注于目标，而非最新的提示词技巧。

通过使用 DSPy 中不断增加的优化函数库，我们可以利用已有的评估数据，提高提示 LLM 完成任务的效率。

最后，每当我们想要尝试一个新模型时，我们都可以轻松地重新运行这些优化。我们无需担心由 DSPy 定义的最终提示；我们只关心我们的提示的性能。

![Visual breakdown of prompt components using colored blocks](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_018.jpg)

让我们回到 OpenAI SWE-Bench 提示。我们将以此作为我们的目录。对于我们的合并任务来说，一个好的提示可能包含许多相同的组件。那么，让我们逐步浏览这些部分，看看 DSPy 是如何处理每一部分的。

我们将从任务和提示策略开始。

![Explanation of DSPy signatures and modules with icons](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_019.jpg)

DSPy 根据<强 id=0>签名和<强 id=1>模块创建提示。

签名通过指定输入和期望的输出来定义任务。它可以是一个字符串，比如， `  问题 -> 答案  ` 。你可以写任何内容，例如， `  棒球运动员 -> 是否是投手  ` 。甚至可以输入你的参数， `baseball_player -> is_pitcher: bool` 。我们也可以将这些定义为类，稍后会讲到。

模块是将你的签名转换为提示的策略。它们可以非常简单（ `Predict` 模块），也可以要求大语言模型（LLM）逐步思考（ `ChainOfThought` 模块）。最终，它们会管理你提示中的任何示例或其他可学习参数。

用一个签名定义你的任务，然后将其交给一个模块。如下所示：

![Code example showing basic DSPy implementation](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_020.jpg)

这是 DSPy 中的“你好，世界”。

我们连接到一个大语言模型（LLM）并将其设置为我们的模型。DSPy 为此使用了 [LiteLLM](https://www.litellm.ai/) ，它使我们能够连接到无数平台、我们自己的服务器（可能运行 SGLang 或 vLLM），甚至是使用 [Ollama](https://ollama.com/) 运行的本地模型。

在第 8 行，我们定义了我们的签名（ `  问题 -> 答案  ` ）并将其交给一个模块（ `Predict` ）。这为我们提供了一个程序（ `qa` ），我们可以用一个问题（在这种情况下是“为什么天空是蓝色的？”）来调用它。

我们无需处理任何提示或输出解析。所有这些都在幕后进行……

![System prompt example showing how signatures become prompts](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_021.jpg)

DSPy 会根据指定模块，从你的签名中创建一个提示。

这是由我们的“你好，世界”代码生成的系统提示。它定义了我们的任务，指定了输入和输出字段，详细说明了我们期望的格式，并再次强调了我们的任务。

这不是我们写的，我们不必看它（除非我们真的想看），也不必触碰它。

![User prompt example showing input formatting](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_022.jpg)

这是我们生成的用户提示，其中包含一个我们可能交给它的问题（“法国的首都是什么？”）。这些提示会被发送到我们提供的大语言模型（LLM）。

（现在我敢肯定，读到这篇文章的你们很多人都在心里给这些提示词做标记，加上自己最喜欢的技巧——比如提出给大语言模型（LLM）小费或者威胁它的“母亲”。别担心，我会向你们展示如何改进这个提示词。先记住这个想法。）

![ChainOfThought module example with reasoning field](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_023.jpg)

现在模块是 *模块化的* （因此得名！），并且我们可以轻松地将它们换进换出。通过使用 `ChainOfThought` 而不是 `Predict` ，DSPy 会生成这个系统提示。

![Grid showing various DSPy module types available](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_024.jpg)

有许多不同的模块。你甚至可以自己编写。

![Code example defining Place and PlaceMatcher signature classes](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_025.jpg)

对于我们的合并任务，我们将选择使用类而不是字符串来定义我们的签名。

我们在这里的第一个类是一个 Pydantic `BaseModel` ，它构建了我们的地点对象：它有一个地址和一个名称。

我们的第二个类是我们的特色。我们将两个位置定义为输入，并指定我们想要返回的内容：一个布尔值 `match` 和一个 `match_confidence` ，其可以是低、中或高。

注意两条突出显示的行。你可以将描述性文本传递给 DSPy，以便在生成提示时使用。这是一个很好的地方来存储从你的变量名中看不出来的领域知识（DSPy 也会使用这些变量名，所以要好好命名！） `match` 输出相当不言自明，但为了提供一些背景信息，我将在这里添加一个非常简短的描述。

第一个亮点，即文档字符串，也会被传递过去。旁注，希望这是我幻灯片中唯一的一处错误——文档字符串 *应该* 写成“确定这两个地点是否指的是同一个地点”，这样我的输出字段描述也会变得多余。

最后，我们将其传递给一个 `Predict` 模块来创建我们的程序。

![Code showing how to call the PlaceMatcher with example results](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_026.jpg)

调用我们的程序很简单：我们创建两个位置并将它们传递给匹配器。

这是一个棘手的合并可能呈现出的样子的好例子：顶部记录来自阿拉米达县餐厅卫生检查数据集，底部记录来自 Overture。经过标准化处理后，地址匹配。但名称却大不相同，不过鉴于地址相同，人类很容易就能识别出它们是同一个。

我们得到一个 `Prediction` 对象，其中包含我们的两个输出。我们的模型—— [文心一言 3.0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) ——答对了，返回 `True` 。

![Another prompt component breakdown visualization](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_027.jpg)

看看我们从目录中完成了多少内容。定义我们的签名和模型就完成了我们的任务、提示指令以及 *格式化* 。我们不必使用任何特定于 LLM 的结构化输出调用，也不必编写任何字符串处理来提取我们的输出。它就是 *能正常运行* 。

甚至在进行任何优化之前，DSPy 就能让我们更快地启动并运行起来，同时生成更易于维护且能与我们共同成长的代码。

![Code example showing ReAct module with tool definitions](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_028.jpg)

在我们的合并任务中，我们没有使用任何工具，但下面是我们可以使用的方法。 `ReAct` 模块允许我们在创建程序时提供命名良好的 Python 函数，如下所示……

![Prompt component breakdown highlighting tool definitions](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_029.jpg)

剩下的提示组件是最大的一个：详细的上下文和说明。对大多数人来说，这是最独特的部分，它会随着你收集错误案例和经验教训而不断扩充。它包含你的示例、零散的指导、紧急修复等等。

DSPy 会为你创建这部分内容，但你需要 *评估数据* 。

你们都有评估数据，对吧？这是你们最有价值的人工智能资产。然而，我惊讶地发现，我经常遇到没有评估数据的团队！他们没有在应用程序中建立反馈循环，也没有从管道中收集失败案例。而且他们没有与领域专家合作来标记示例，更不用说自己标记数据了。

别像他们那样！这是另一场演讲、 [帖子](https://hamel.dev/blog/posts/evals/) 、 [课程](https://maven.com/parlance-labs/evals) 或书籍的主题。但不要犹豫，马上开始：手动标注几百个示例。这总比什么都不做好。

对于我们的合并任务，我是这样做的：

1. 我编写了一个非常简单的 DuckDB 查询，以便从我的两个数据集中生成候选示例。我找到了地址和名称具有 [足够相似字符串](https://duckdb.org/docs/stable/sql/functions/text.html#text-similarity-functions) 的附近位置。我的查询从每个候选记录中选择地址和名称，并将这些行写入 CSV 文件。
2. 然后我通过直观编码创建了一个超小的 HTML（使用 Claude Code，但对于这样一个简单的网站，你也可以使用 Cursor、Cline，甚至 ChatGPT），它会加载 CSV 文件，展示比较结果，并让我将它们标记为匹配或不匹配。我甚至添加了键盘命令，这样我在喝咖啡的时候就可以按下 `T` 或 `F` 。该网站将我的工作输出到一个新的 CSV 文件中。

总体而言，整个练习耗时约一小时，其中包括为1000多对进行标注。

![Code showing DSPy optimization process with MIPROv2](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_030.jpg)

有了我们的评估集，我们唯一需要的另一件事就是一个用于评估结果的指标函数。这个函数在我们代码的顶部，接受我们的 `  示例  ` （来自我们带标签训练集的一条记录）和一个 `  预测  ` （根据我们训练集的输入生成的新响应）。我们的指标非常简单，如果响应匹配就返回 `True` 。但在这里我们可以做得更复杂，比如分解字符串，甚至使用 [一个大语言模型作为评判](https://www.dbreunig.com/2025/01/08/evaluating-llms-as-knowledge-banks.html#evaluating-the-responses) 。

我们将我们的指标、标记数据和程序提供给一个 DSPy 优化器——这里，我们使用的是 MIPROv2（稍后会详细介绍）。我们调用 `compile` ，然后 DSPy 会持续运行，最终返回给我们一个优化后的程序。我们可以立即使用它，但这里我们只是将其保存到一个 JSON 文件中，以便稍后加载。

在公布结果之前，让我们先介绍一下我们的优化器 MIPROv2。

![Three-step MIPROv2 process diagram with icons](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_031.jpg)

MIPROv2 使用一个大语言模型（LLM）来编写最优提示。它通过三个阶段来完成这项工作。

首先，它运行我们现有的程序和带标签的数据以生成一些示例。目前，这些追踪相当简单，但如果我们将几个模块堆叠在一起，这可能会变得相当复杂。

接下来，它使用这些示例和我们的签名来提示一个语言模型（LLM）生成对我们程序的描述。然后，它使用这个描述、我们的示例以及一系列提示技巧，要求一个语言模型编写许多不同的候选提示，我们可以用这些提示来改进我们的程序。

最后，它会采用我们标记好的示例以及这些候选提示，并运行许多小批次，评估每个的性能。这就像是一场提示竞赛。然后，表现最佳的组件和示例会被组合成新的提示候选，接着对这些新候选进行评估，直到选出获胜者。

![Generated instruction text showing detailed place matching criteria](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_032.jpg)

在运行了十几分钟后，DSPy 返回了一个大幅改进的提示。我原来的提示“确定两个兴趣点是否指的是同一个地方”变成了：

> 给定两条表示地点或企业的记录——每条记录至少包含名称和地址——分析这些信息并确定它们是否指代同一个现实世界中的实体。如果名称和地址在其他方面非常相似，那么像大小写、变音符号、音译、缩写或格式等细微差异可视为潜在匹配。只有当两个字段都非常匹配时才输出“True”；如果名称或地址存在显著差异，即使其中一个字段完全匹配，也输出“False”。你的判断应能适应常见的变化和错误，并且适用于多种语言和文字。

差别可真大！

DSPy 还识别出了几个理想的示例匹配项，以便插入到我们的提示中。

![Prompt breakdown emphasizing detailed context and instructions](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_033.jpg)

运行一次优化就完成了我们的提示组件列表。但它起作用了吗？

![Results showing performance improvement from 60.7% to 82.0% with code snippet](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_034.jpg)

是的，成功了。刚开始时，文心一言 3 0.6B 在我们的评估集上的得分是 60.7%。经过优化后，我们的程序得分 *82%* 。

我们仅用14行代码就实现了这一点，它管理着一个约700个标记的提示。代码易于阅读，并且随着新的评估数据的获取，我们可以持续运行优化。新优化的程序可以保存、版本控制、跟踪和加载。

![Comparison of model performance across Qwen, Llama, and Phi models](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_035.jpg)

我们展示了 DSPy 如何让你将任务与提示解耦……但模型呢？

我喜欢 DSPy 的一点是，我们可以轻松地针对出现的任何新模型重新运行优化和评估，而且我们优化后的提示通常会有所不同！不同的模型是不同的，认为一个手工调整的提示可以自然地从一个模型转换到最新的热门模型是错误的。使用 DSPy，我们只需提供一个新模型并运行我们的优化。

这对任何团队来说都是一项优势，对 Overture 尤其如此。亚马逊、Meta 和微软都有自己的模型，可能希望我们用他们的最新成果来运行我们的流程。有了 DSPy，这很容易做到。不到一个小时，我就针对 Llama 3.2 1B（性能达到 91%）和 Phi-4-Mini 3.8B（性能达到 95%）对我们的合并程序进行了优化。

明天总会有更快、更便宜、更好的模型出现。通过使用 DSPy 将你的任务与模型解耦，你就能随时准备迎接下一个最佳选择。

![Takeaways slide with four key points about using DSPy](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_036.jpg)

使用 DSPy 能让一切变得更轻松，让你的程序更出色。它能让你更快地启动并运行起来，随着你获取评估数据并与团队协作而不断发展，优化你的提示词，并让你紧跟快速发展的 LLMs 领域的步伐。

![Repeat of three-pillar DSPy framework diagram](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_037.jpg)

将你的任务与大语言模型（LLM）解耦。编写任务，而非提示词。定期优化你的程序，并让它们负责。采用模型可移植性。

**不要编写你的提示词。编写你的程序。**

![Future improvements list including new optimizers and fine-tuning](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_038.jpg)

而我们只是触及了皮毛而已！（记住：DSPy 会与你共同成长。）

还有更多的优化器，其中有几种会微调你的模型权重，而不仅仅是你的提示词。你的管道或功能可能会演变成多阶段模块。或者你可能会选择合并一些工具。

对于我们的合并任务，我很想尝试一下 DSPy 新的 [辛巴优化器](https://dspy.ai/api/optimizers/SIMBA/) 。我还认为我们可以从一个多阶段模块中受益，该模块首先检查数据破坏情况（一些可自由编辑的数据源经常会被垃圾信息或恶作剧破坏）。

![Three QR codes with action items for getting started](https://www.dbreunig.com/img/dais/dais_2025_dbreunig_039.jpg)

感谢今天收听（或阅读！）。我鼓励大家从小事做起，今天就试着写一个签名。你会惊讶于自己能如此迅速地开始。

如果你想尝试进行合并，或者只是想为你的应用程序或工作流程添加一些地理空间数据，访问 [序曲地图（Overture Maps）](https://overturemaps.org/) 并获取一些数据。它质量很高且 *免费* ，对于 [地点数据集有特别友好的许可协议](https://docs.overturemaps.org/attribution/) 。

最后，看看我的网站。上面有很多关于使用人工智能进行构建以及对人工智能的思考的文章（还有一些地理空间方面的内容）。注册获取定期更新或 [联系我](https://www.dbreunig.com/contact.html) 。我很想听听你是如何使用 DSPy 或以其他方式利用人工智能进行构建的。

---