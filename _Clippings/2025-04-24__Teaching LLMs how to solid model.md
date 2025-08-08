---
title: "Teaching LLMs how to solid model"
source: "https://willpatrick.xyz/technology/2025/04/23/teaching-llms-how-to-solid-model.html"
author:
published: 2025-04-24
created: 2025-04-24
description: "It turns out that LLMs can make CAD models for simple 3D mechanical parts. And, I think they’ll be extremely good at it soon."
tags:
  - "clippings"
---
事实证明，LLMs 可以为简单的 3D 机械零件制作 CAD 模型。而且，我认为他们很快就会在这方面做得非常出色。

## 一位人工智能机械工程师

代码生成是LLMs的首个突破性应用。对于机械工程而言，人工智能代理会是什么样子呢？材料选择、面向制造的设计、计算机辅助制造（CAM）以及现成零件比较都将是人工智能机械工程师的重要特征。也许，最重要的是，人工智能机械工程师将设计并改进 CAD 模型。机械工程师通常使用点击式软件（例如 Fusion 360、Solidworks 和 Onshape）来设计 CAD。那么，人工智能如何生成这些实体模型呢？

## 代码生成与计算机辅助设计相结合

一个有前景的方向是在数百万个现有 CAD 文件上训练生成模型。多个团队正在积极研究这种方法，他们正在研究扩散和 Transformer 架构。特别是，我喜欢欧特克研究公司（Autodesk Research）将参数化图元（点、曲线、形状、拉伸等）编码到 Transformer 架构中的方法。然而，据我所知，这些项目中的模型还不能接受任意输入命令并生成所需形状。

几周前，我受到近期使用LLMs驱动 Blender（一款广泛用于动画制作的开源建模工具）的启发。鉴于LLMs在生成代码方面非常出色，或许可以用类似的方式使用 CAD 建模的编程接口来生成实体模型。我立刻想到了 OpenSCAD，一款已经开发了超过 15 年的开源编程 CAD 工具。用户无需使用点击式软件来创建实体模型，而是编写一个软件脚本，然后将其渲染为实体 CAD 模型。

## LLMs 擅长编写 OpenSCAD

为了测试它，我在 Cursor 中创建了一个简单的项目，创建了一个空白的 OpenSCAD 脚本（Cursor.scad），并添加了一些 Cursor 规则：

```
# Your rule content

- We're creating files to model things in open scad. 
- All the OpenScad files you create will be in Cursor.scad. I've set up this file such that if you edit it, it will automatically be read by OpenScad (it's the open file in the program). 
- If I want to save what you've done, I'll tell you and you should create a new file and put it in the Saved folder. 
- That's it! Overtime, if needed, we could create documentation about how to use OpenScad. 
- If I'm asking you to create a new design, you should delete the current contents of cursor.scad and add the new design into it.
- When I make requests you should always first develop a step by step plan. Then tell me the step by step plan. And then I'll tell you to start modeling. 
- When you're going through the step by step plans, only execute one step at a time. 
- When you've executed a step, ask the user if its right.
```

然后，我开始使用 Cursor 创建实体模型。

这是一个例子：“创建一个 iPhone 手机壳”。

![iPhone GIF](https://willpatrick.xyz/assets/images/blog/iphone.gif)

它第一次尝试时没有成功，但经过几次迭代（包括给它提供截图），我们创建了一个基本案例。

你也可以利用 OpenSCAD 库（有许多公共库）。在这里，我使用一个库为法兰制作一个螺纹。

![Flange GIF](https://willpatrick.xyz/assets/images/blog/flange.gif)

有一件相当巧妙的事情是，LLM 可以运用其机械工程方面的常识。例如，在上文提到的内容中，Cursor 在管道上为 M6 螺栓钻出了孔，并且它正确地将直径做得略大于 6 毫米，这样螺栓就能穿过。

```
bolt_hole_d = 6.5; // Diameter for M6 bolts
```

当然，这种方法真正的优点之一是文件是可编辑的，并且 Cursor 默认对设计的所有关键元素进行参数化。在上面的示例中，我要求它添加安装螺栓的孔，它照做了，然后我手动将孔的数量从 4 个编辑为 3 个。

```
// Flange parameter
flange_OD = 50; // Outer diameter of the flange in mm 
flange_thickness = 10; // Thickness of the flange in mm
pipe_size = 1/2; // NPT Pipe Size

// Bolt hole parameters
num_bolts = 3;
bolt_hold_d = 6.5; // Diameter for M6 bolts
bold_hole_circle = 35; // Diameter for the bolt circle
```

## 为LLM构建一个评估 -> OpenSCAD -> STL

这些初步结果给我留下了深刻印象，但我想了解更多。例如，模型的推理能力是否有助于它思考创建一个零件的步骤？所以，我决定开发一项评估，以测试各种LLMs通过 OpenSCAD 生成实体模型的性能。

创建用于计算机辅助设计（CAD）评估的一个挑战在于，大多数任务有多个正确答案。例如，像“制作一个长度为 10 毫米的 M3 螺丝”这样的任务可能有多个正确答案，因为任务中未定义头部的长度、直径和样式。为了解决这个问题，我决定在我的评估中编写任务，以便对几何形状只有一种正确的解释。

例如，以下是评估中的任务之一：

> 这是一块厚度为 3 毫米的长方形板，上面有两个孔。
> 
> 1. 该板材尺寸为 18 毫米×32 毫米。
> 2. 当俯视这块板时，它有两个贯穿的孔。在板的左下角，有一个孔，其中心点距离短边（18 毫米）3 毫米，距离长边（32 毫米）3 毫米。这个孔的直径为 2 毫米。
> 3. 在板的大致左上角，有一个直径为 3 毫米的孔。其中心点距离短边（18 毫米边）8 毫米，距离长边（32 毫米边）6 毫米。

这种方法的好处是，我们可以将每个任务评定为通过或失败，并且能够以自动化方式进行。我总共编写了 25 个 CAD 任务，难度从单个操作（“一根 50 毫米长、外径 10 毫米、壁厚 2 毫米的管道”）到 5 个连续操作不等。对于每个任务，我使用 Autodesk Fusion 360 设计了一个参考 CAD 模型，然后导出了一个 STL 网格文件。

然后，我开始着手编写自动化评估管道的程序（当然，我实际上没写多少代码）。

以下是评估管道的工作方式：

1. 对于每个任务和模型，评估器通过 API 将文本提示（以及系统提示）发送到LLM。
2. LLM返回 OpenSCAD 代码。
3. OpenSCAD 代码被渲染成 STL 格式
4. 生成的 STL 会自动与参考 STL 进行对比检查
5. 如果任务通过了一些几何检查，则该任务“通过”。
6. 然后结果会在仪表板中输出。
<svg aria-roledescription="flowchart-v2" role="graphics-document document" viewBox="0 0 1798.9375 294" style="max-width: 1798.9375px;" class="flowchart" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" width="100%" id="mermaid-1745458785440"><g><marker orient="auto" markerHeight="8" markerWidth="8" markerUnits="userSpaceOnUse" refY="5" refX="5" viewBox="0 0 10 10" class="marker flowchart-v2" id="mermaid-1745458785440_flowchart-v2-pointEnd"><path style="stroke-width: 1; stroke-dasharray: 1, 0;" class="arrowMarkerPath" d="M 0 0 L 10 5 L 0 10 z"></path></marker><marker orient="auto" markerHeight="8" markerWidth="8" markerUnits="userSpaceOnUse" refY="5" refX="4.5" viewBox="0 0 10 10" class="marker flowchart-v2" id="mermaid-1745458785440_flowchart-v2-pointStart"><path style="stroke-width: 1; stroke-dasharray: 1, 0;" class="arrowMarkerPath" d="M 0 5 L 10 10 L 10 0 z"></path></marker><marker orient="auto" markerHeight="11" markerWidth="11" markerUnits="userSpaceOnUse" refY="5" refX="11" viewBox="0 0 10 10" class="marker flowchart-v2" id="mermaid-1745458785440_flowchart-v2-circleEnd"><circle style="stroke-width: 1; stroke-dasharray: 1, 0;" class="arrowMarkerPath" r="5" cy="5" cx="5"></circle></marker><marker orient="auto" markerHeight="11" markerWidth="11" markerUnits="userSpaceOnUse" refY="5" refX="-1" viewBox="0 0 10 10" class="marker flowchart-v2" id="mermaid-1745458785440_flowchart-v2-circleStart"><circle style="stroke-width: 1; stroke-dasharray: 1, 0;" class="arrowMarkerPath" r="5" cy="5" cx="5"></circle></marker><marker orient="auto" markerHeight="11" markerWidth="11" markerUnits="userSpaceOnUse" refY="5.2" refX="12" viewBox="0 0 11 11" class="marker cross flowchart-v2" id="mermaid-1745458785440_flowchart-v2-crossEnd"><path style="stroke-width: 2; stroke-dasharray: 1, 0;" class="arrowMarkerPath" d="M 1,1 l 9,9 M 10,1 l -9,9"></path></marker><marker orient="auto" markerHeight="11" markerWidth="11" markerUnits="userSpaceOnUse" refY="5.2" refX="-1" viewBox="0 0 11 11" class="marker cross flowchart-v2" id="mermaid-1745458785440_flowchart-v2-crossStart"><path style="stroke-width: 2; stroke-dasharray: 1, 0;" class="arrowMarkerPath" d="M 1,1 l 9,9 M 10,1 l -9,9"></path></marker><g class="root"><g class="clusters"></g><g class="edgePaths"><path marker-end="url(#mermaid-1745458785440_flowchart-v2-pointEnd)" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_A_B_0" d="M268,147L272.167,147C276.333,147,284.667,147,292.417,147.07C300.167,147.141,307.334,147.281,310.917,147.351L314.501,147.422"></path><path marker-end="url(#mermaid-1745458785440_flowchart-v2-pointEnd)" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_B_C_0" d="M596.5,147.5L600.583,147.417C604.667,147.333,612.833,147.167,620.417,147.083C628,147,635,147,638.5,147L642,147"></path><path marker-end="url(#mermaid-1745458785440_flowchart-v2-pointEnd)" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_C_D_0" d="M870.789,147L874.956,147C879.122,147,887.456,147,895.206,147.07C902.956,147.141,910.123,147.281,913.706,147.351L917.29,147.422"></path><path marker-end="url(#mermaid-1745458785440_flowchart-v2-pointEnd)" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_D_E_0" d="M1153.438,147.5L1157.521,147.417C1161.604,147.333,1169.771,147.167,1177.438,147.154C1185.104,147.141,1192.271,147.281,1195.855,147.351L1199.438,147.422"></path><path marker-end="url(#mermaid-1745458785440_flowchart-v2-pointEnd)" style="" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" id="L_E_I_0" d="M1481.438,147.5L1485.521,147.417C1489.604,147.333,1497.771,147.167,1505.354,147.083C1512.938,147,1519.938,147,1523.438,147L1526.938,147"></path></g><g class="edgeLabels"><g class="edgeLabel"><g transform="translate(0, 0)" class="label"></g></g><g class="edgeLabel"><g transform="translate(0, 0)" class="label"></g></g><g class="edgeLabel"><g transform="translate(0, 0)" class="label"></g></g><g class="edgeLabel"><g transform="translate(0, 0)" class="label"></g></g><g class="edgeLabel"><g transform="translate(0, 0)" class="label"></g></g></g><g class="nodes"><g transform="translate(138, 147)" id="flowchart-A-0" class="node default"><rect height="78" width="260" y="-39" x="-130" style="" class="basic label-container"></rect><g transform="translate(-100, -24)" style="" class="label"><rect></rect><foreignObject height="48" width="200"><p><span></span></p><p>Start Eval For each Task &amp; Model</p><p></p></foreignObject></g></g><g transform="translate(457, 147)" id="flowchart-B-1" class="node default"><polygon transform="translate(-139,139)" class="label-container" points="139,0 278,-139 139,-278 0,-139"></polygon><g transform="translate(-100, -24)" style="" class="label"><rect></rect><foreignObject height="48" width="200"><p><span></span></p><p>Send System + Task Prompt to LLM</p><p></p></foreignObject></g></g><g transform="translate(758.39453125, 147)" id="flowchart-C-3" class="node default"><rect height="54" width="224.7890625" y="-27" x="-112.39453125" style="" class="basic label-container"></rect><g transform="translate(-82.39453125, -12)" style="" class="label"><rect></rect><foreignObject height="24" width="164.7890625"><p><span></span></p><p>LLM Returns OpenSCAD</p><p></p></foreignObject></g></g><g transform="translate(1036.86328125, 147)" id="flowchart-D-5" class="node default"><polygon transform="translate(-116.07421875,116.07421875)" class="label-container" points="116.07421875,0 232.1484375,-116.07421875 116.07421875,-232.1484375 0,-116.07421875"></polygon><g transform="translate(-89.07421875, -12)" style="" class="label"><rect></rect><foreignObject height="24" width="178.1484375"><p><span></span></p><p>Render OpenSCAD to STL</p><p></p></foreignObject></g></g><g transform="translate(1341.9375, 147)" id="flowchart-E-7" class="node default"><polygon transform="translate(-139,139)" class="label-container" points="139,0 278,-139 139,-278 0,-139"></polygon><g transform="translate(-100, -24)" style="" class="label"><rect></rect><foreignObject height="48" width="200"><p><span></span></p><p>Compare Generated STL to Reference STL</p><p></p></foreignObject></g></g><g transform="translate(1660.9375, 147)" id="flowchart-I-9" class="node default"><rect height="78" width="260" y="-39" x="-130" style="" class="basic label-container"></rect><g transform="translate(-100, -24)" style="" class="label"><rect></rect><foreignObject height="48" width="200"><p><span></span></p><p>Output Eval Results to Dashboard</p><p></p></foreignObject></g></g></g></g></g></svg>

\[注意：评估针对每个任务 x 模型组合运行多个重复项。并且评估是并行执行的，因为在运行完整评估时可能有 1000 多个任务。\]

几何检查的工作原理如下：

- 生成的 STL 和参考 STL 使用迭代最近点（ICP）算法进行对齐。
- 然后通过以下方式比较对齐的网格：
	- 它们的体积（通过 = <2% 差异）
	- 它们的边界框（通过 = <1 毫米）
	- 零件之间的平均倒角距离（合格 = <1 毫米）
	- 豪斯多夫距离（第 95 百分位数）（通过标准 = <1 毫米）
- 要“通过”评估，所有几何检查都必须通过。

评估管道在几个方面可以改进。特别是，误报很常见（估计约为 5%）。我还注意到，偶尔一些不正确的小特征（如小半径圆角）不会被自动几何检查检测到。尽管如此，评估管道仍然足以看到有趣的结果并比较各种LLMs的性能。

如果你想了解更多关于 eval 的信息，使用它，或者查看任务，请查看 GitHub 仓库。

最后，有多种方法可以改进评估。以下是我接下来想做的几件事：

- 更多覆盖范围更广的任务
- 优化系统提示，特别是通过添加 OpenSCAD 文档和代码片段
- 创建一个使用草图和绘图作为输入的评估变体
- 添加另一个变体，用于测试LLM向现有 OpenSCAD 脚本和 STL 添加操作的能力
- 评估LLM修复现有 STL/OpenSCAD 代码中错误的能力

## 前沿模型的快速改进

以下是在 2025 年 4 月 22 日执行的一次评估运行的结果。在该评估运行中，对 15 个不同的模型在 25 个任务上进行了测试，每个任务有 2 次重复。该运行的所有结果和配置细节都可在此处获取。

结果表明，LLMs 只是最近才擅长 OpenSCAD 实体建模。

![Results from CadEval](https://willpatrick.xyz/assets/images/blog/overall_result2.png)

CadEval 的结果。在本次运行中，每个模型尝试完成 25 项任务（每项任务 2 次重复）。“成功”意味着它们通过了一些与参考几何形状进行比较的几何检查。

排名前三的模型都是在我参与该项目期间推出的，排名前七的模型都是推理模型。与它们的前身非推理模型相比，这些模型的性能有了大幅提升。十四行诗 3.5 是最好的非推理模型，十四行诗 3.7 在评估中的表现仅略好一些（对于十四行诗 3.7，使用了 2500 个标记的预算进行思考）。

深入研究结果能提供一些有趣的见解。首先，LLMs 在生成能正确编译并可渲染为 STL 的 OpenSCAD 代码方面表现相当出色。换句话说，只有一小部分失败是由 OpenSCAD 语法错误之类的问题导致的。Anthropic 的十四行诗模型在这方面表现最佳。

![Rendering Success Rate](https://willpatrick.xyz/assets/images/blog/stl_render_success.png)

对于与上述相同的评估运行，每个模型中渲染了 STL（并检查了几何形状）的任务百分比。

此外，我们可以查看渲染了 STL 的任务的成功率。o3-mini 相当强大，成功率与全尺寸 o3 模型几乎相同，而 Sonnet 3.7 似乎落后于领先的 Gemini 2.5 Pro 以及 o1、o3、o4-mini 和 o3-mini 模型一步。

![Success Rate if STL Rendered](https://willpatrick.xyz/assets/images/blog/success_rate_for_only_tasks_with_rendered_stl.png)

在生成了 STL 的任务中，成功通过所有几何检查的任务百分比。

最后，可以预料的是，Gemini 2.5 和 o4-mini 比完整的 o3 和 o1 型号便宜得多，运行速度也稍快一些。

![Average cost per task for various models](https://willpatrick.xyz/assets/images/blog/average_estimated_cost.png)

每个模型每项任务的估计成本。

![Average time per task for various models](https://willpatrick.xyz/assets/images/blog/average_estimated_time.png)

每个任务生成 OpenSCAD 并渲染 STL 的平均总时间。进行 API 调用并接收 OpenSCAD 的时间比渲染 STL 的时间长得多，渲染 STL 的时间不到 1 秒。

不出所料，有些任务很容易完成，有些任务则很难完成。

![Pass rate for each of the 25 tasks](https://willpatrick.xyz/assets/images/blog/task_success_rate.png)

逐个任务的总体成功率。

一般来说，操作更多的任务更具挑战性。

![Pass rate by part complexity](https://willpatrick.xyz/assets/images/blog/part_complexity.png)

在 Fusion360 中，每个任务需要 1 到 5 次手动操作才能完成。在评估过程中，有 5 个任务需要单次操作，5 个任务需要两次操作，依此类推。

任务 2、任务 3 和任务 6 是最简单的任务，所有模型的正确率都超过 80%。以下是这些任务成功示例的样子。

只有 2 个任务成功率为 0%，即任务 11 和任务 15。以下是这两个任务的提示及典型失败情况。

这些失败案例既有趣又有很大不同。任务 11 是空间推理能力差的一个典型例子。在图像中突出显示的特定失败案例中，模型将吊环螺栓的杆部垂直于圆环面挤出（而不是在同一平面内）。任务 15 是另一种失败模式。在附带的图像中很难看出，但如果你仔细放大，就会清楚地看到生成的形状比参考形状略大（这是有道理的，因为生成的 STL 文件未通过体积检查）。从查看此示例的 OpenSCAD 代码来看，失败似乎是由于使用了 OpenSCAD 的 hull 操作，该操作与放样操作并不完全相同。OpenSCAD 没有内置的放样操作。

任务 20 - 24 都需要 5 个连续操作，这些任务的平均成功率在 3.3%至 30%之间。以下是这 5 个任务中具有代表性的成功和失败提示。

这些故障可能很难发现。失败图像的绿色区域在生成的 STL 中应该有几何形状，但实际上却没有（参考点云以绿色绘制）。同样，红色区域在生成的 STL 中有几何形状，但它们不应该有。

## 初创企业

在过去几个月里，两家不同的初创公司推出了文本转 CAD 产品，AdamCad 和 Zoo.dev。Zoo.dev 提供了一个 API 来使用他们的文本转 CAD 模型。Zoo 对其 API 和文本转 CAD 产品的演示非常酷，看起来与我上面的 Cursor -> OpenSCAD 演示非常相似。

我将 Zoo 添加到评估流程中，以便与LLM -> OpenSCAD -> STL 进行比较。Zoo.dev API 没有生成 OpenSCAD，而是直接返回了一个 STL。Zoo 表示他们使用了专有数据集和机器学习模型。令我惊讶的是，与通过创建 OpenSCAD 生成 STL 的LLMs相比，Zoo 的 API 表现并不特别出色。尽管如此，我很高兴看到 Zoo.dev 的发展，并且期待看到 Zoo.dev 未来推出的模型与通过创建 OpenSCAD 的LLMs相比会如何。

## 接下来是什么？

我认为这些初步结果很有前景。Cursor（或其他编码代理）+OpenSCAD 提供了一种以自动化方式生成实体模型的解决方案。

然而，我认为这种方法不会迅速流行并在 CAD 设计生态系统中广泛传播。当前的设置非常笨拙，我认为需要对产品进行大幅改进才能使其更好地发挥作用。类似于 Cursor、Windsurf 和其他工具为代码生成开发了特定的用户体验和工作流程，我想开发适用于 CAD 生成的工作流程和用户体验将需要大量工作。以下是一些我认为在这个方向上值得探索的想法：

- 从 OpenSCAD 引入控制台日志和视口图像到 Cursor 以进行迭代改进和调试的工具。
- 一个用于突出显示（并测量）零件的某些面、线或方面的用户界面，这些信息会被输入到LLM以获取更多背景信息。
- 绘图或草图输入，以便用户能够快速直观地传达他们的想法。
- 一个带有滑块的用户界面，用于调整参数而非编辑代码。

此外，我预计模型的进一步发展将继续解锁此应用。特别是，改进空间推理是一个活跃的研究领域。我设想，改进的空间推理可以极大地提高模型逐步设计零件的能力。

那么文本到 CAD 何时会成为机械工程师常用的工具呢？随着初创企业积极开发产品以及前沿模型的快速改进，我猜大概是 6 到 24 个月之后。

## 这个要放到哪里？

从中长期（2 至 10 年）来看，我设想大多数部件将通过某种形式的通用 CAD（GenCAD）来创建。请允许我做一些推测。

- 最初，GenCAD 将用于创建适合现有装配体的零件。例如，你可能会说：“我需要一个适合这里的支架。” 然后，GenCAD 工具将创建一个能与现有装配体组件完美接合的支架。想通过有限元分析（FEA）来分析三种变体吗？提出需求即可。我预计主流 CAD 套件（欧特克、Solidworks、Onshape）会将这些功能直接添加到它们的产品套件中。
- 从长远来看，我设想 GenCAD 将涵盖 CAD 套件的各个方面：草图、配合、装配体、爆炸视图、CAM 刀具路径、渲染可视化以及 CAE。想象一下这样一个设计评审场景：你突出显示一个子装配体并说“用 M6 沉头螺钉替换这些铆钉并重新生成 BOM”。模型、图纸和采购电子表格会在几秒钟内全部更新。

我们正在见证计算机辅助设计（CAD）开始走出手动输入时代。就我个人而言，对此感到非常兴奋。