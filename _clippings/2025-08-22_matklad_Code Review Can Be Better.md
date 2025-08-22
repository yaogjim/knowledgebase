---
title: "Code Review Can Be Better"
source: "https://tigerbeetle.com/blog/2025-08-04-code-review-can-be-better/"
author:
  - "[[matklad]]"
published: 2025-08-22
created: 2025-08-22
description: "Insights, updates, and technical deep dives on building a high-performance financial transactions database."
tags:
  - "matklad"
---
![](https://tigerbeetle.com/blog/2025-08-04-code-review-can-be-better/banner.webp)

今天的类型有点不寻常：一个关于我们的 [负面结果](https://github.com/tigerbeetle/tigerbeetle/pull/3129) ，是关于我们的 [`git-review`](https://github.com/tigerbeetle/tigerbeetle/pull/2732) 用于对代码审查过程进行不同解读的工具，我们决定…… （句子不完整，翻译到这里） 暂时搁置，至少目前如此。

很多人对 GitHub 的代码审查流程不满意。主要问题之一是 GitHub 对堆叠拉取请求和 [交互式差异审查](https://gist.github.com/thoughtpolice/9c45287550a56b2047c6311fbadebed2) 的支持不佳。虽然我也认为交互式差异审查很有价值，但这并不是我决定试用 `git-review` 的原因。我对 GitHub 以及除了 [Jane Street 内部使用的工具](https://www.janestreet.com/tech-talks/janestreet-code-review/) 之外的每一个代码审查系统还有另外两个问题：

- 评审状态不作为仓库本身的一部分进行存储
- 审查通过远程优先的 Web 界面进行。

让我们从第二个开始。

打个比方，我不会用 GitHub 的网页编辑器来编写代码。我会在本地克隆一个仓库，然后在我的编辑器中进行工作，我的编辑器是：

- 完全本地，内存/非易失性内存延迟，无 HTTP 往返
- 针对我特定的古怪工作流程量身定制。

当我审查代码时，我喜欢在本地拉取源分支。然后我将代码软重置到仅基础状态，这样代码看起来就好像是我写的一样。然后我启动 magit，它让我能够有效地浏览差异和实际代码。而且我甚至使用 git 暂存区来标记我已经审查过的文件：

![code review in magit](https://tigerbeetle.com/blog/2025-08-04-code-review-can-be-better/magit-review.webp)

审查代码而非差异是如此强大：我可以运行测试，可以跳转到定义以获取上下文，可以在原地尝试我的重构建议，借助代码补全以及我功能强大的代码编辑器的其他特性。

唉，当我真的想在拉取请求（PR）上留下反馈时，我得打开浏览器，在差异（diff）中找到相关行，然后（等上几次 HTTP 往返之后）在文本框里输入我的建议。不知为何，对我来说这个文本框也经常卡顿，尤其是在差异较大的时候。

这里有两个问题。在接口方面，评审反馈是与代码相关的文本。最自然的接口是直接在代码中以行内注释的形式留下评审意见，甚至直接修复代码：

在实现层面，由于数据存储在远程数据库中，而不是本地的 git 仓库，我们会经历所有那些会导致延迟的往返过程（更不用说供应商锁定问题了）。

因此， [`git-review`](https://github.com/tigerbeetle/tigerbeetle/pull/2732) 诞生了。这个想法很简单：

- 代码审查是位于拉取请求（PR）分支之上的单个提交。
- 该提交添加了一堆带有特定标记的代码注释。
- 评审过程涉及作者和评审者双方进行修改 这个顶级提交（所以，有相当数量的……） 你提供的内容似乎不完整，请补充完整以便我能更准确地翻译 （涉及 `git push --force-with-lease` ）。
- 当所有线程都被标记为 时，审查结束 添加了 `//? 已解决 ` 并在其之上添加了一个显式的回滚提交（以便在历史记录中保留审查）。

它算不上失败，但也不是巨大的成功。说到编写工具，我非常喜欢快速致富的方案，比如编写 500 行针对特定用例的、有些粗糙的代码，它在那个特定用例中比\[一些正经的东西\]更管用。一个将你的 `.md` 文件转换为……的简单脚本 \``.html` \` [相比于通用解决方案，维护成本可能更低](https://tigerbeetle.com/blog/2025-02-27-why-we-designed-tigerbeetles-docs-from-scratch/) 。

我曾希望“代码审查就只是一次提交”会是保持实现复杂度较低的秘诀。遗憾的是，在这种特殊情况下，细节决定成败。

基本理念是，审查就是在代码中留下评论，其效果正如我所期望的那样好（也就是说，真的非常棒）。但事实证明，在审查过程中修改代码很棘手。如果审查者要求进行更改，而你将其应用到某个深层提交中，甚至在其之上添加一个新提交，那么你现在就必须解决与审查评论本身的冲突，因为这些评论通常是在 [代码块](https://git-scm.com/book/en/v2/Git-Tools-Interactive-Staging) 处添加的。 边界。然后，虽然 `--force-with-lease` 可行，但它也增加了摩擦。这里存在阻抗不匹配的情况，对于代码，我们需要非常强大的、基于哈希链的有意状态转换序列，而对于评审，我们更希望有更宽松的无冲突合并规则。这 *也许* 可以通过更多工具来解决，以便在纯净的评审分支之上“推送”和“弹出”评审评论，但这似乎远远超出了我的 500 行限制。

然后，还有第二个变化。看起来 [上游 git 可能会引入一个类似 Gerrit 的 Change-Id](https://lore.kernel.org/git/CAESOdVAspxUJKGAA58i0tvks4ZOfoGf1Aa5gPr0FXzdcywqUUw@mail.gmail.com/T/#u) 来跟踪单个提交在变基操作中的修订。如果真的发生这种情况，我们实际上可能会得到对每次提交的增量差异审查的一流支持！但这在某种程度上会与 `git-review` 方法不兼容，后者添加了 对该分支的一个完全独立的提交。但是，也许，在…… `Change-Id` 世界，我们可以向其添加评审注释 提交本身，而且，不是在最后添加一个撤销操作 在审查过程中，指示 Git 存储特定内容的所有修订版本 变更标识

不管怎样，目前我们无奈地又回到了基于网页界面的代码审查方式。希望有朝一日能有人受到足够的启发，将其妥善解决！

如果你也有类似的想法，以下链接值得一看：

- [Fossil](https://fossil-scm.org/home/doc/trunk/www/index.wiki) 是一个将所有内容存储在仓库中的软件配置管理（SCM）系统。
- [NoteDb](https://gerrit-review.googlesource.com/Documentation/note-db.html) Gerrit 的后端。Gerrit 最初是在一个……中跟踪评审状态 单独的数据库，但后来将存储转移到了 Git 中。
- [git-bug](https://github.com/git-bug/git-bug) 使用 Git 来存储有关问题的信息。
- [git-评估](https://github.com/google/git-appraise) （注：这里“git-appraise”直译为“git 评估”，如果它是一个特定的工具名称，可能需要根据实际情况进行更准确的意译，比如“git 评审工具”之类的，但仅从给定文本看，这样翻译基本符合要求） 使用 Git 来存储有关评审的信息。
- 在 GitHub 的 Web API 之上实现编辑器内审查界面的 [prr](https://doc.dxuuu.xyz/prr/index.html)
- 《简街资本的代码审查之道》表明，一个更美好的世界是有可能实现的，而且它已经存在，只是并非处处皆是。
- [git-pr](https://pr.pico.sh/) 是一个在理念上与之类似的项目，它利用 Git 原生特性来取代整个拉取请求工作流程。