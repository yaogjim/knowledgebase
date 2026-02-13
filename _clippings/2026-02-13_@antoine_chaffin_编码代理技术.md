---
title: "编码代理技术"
source: "https://x.com/antoine_chaffin/status/2021977663716380800"
author:
  - "[[@antoine_chaffin]]"
date: "2026-02-13T17:06:46+08:00"
created: 2026-02-13
description:
tags:
  - "@antoine_chaffin # 代理 # 搜索 # 语义 # 代理技术 # AI # 软件开发 # 代码检索"
---
**Antoine Chaffin** @antoine\_chaffin [2026-02-12](https://x.com/antoine_chaffin/status/2021977672197582921)

代理浪费数千个 token 进行试错式的 grep 操作。它们猜测标识符、优化模式、再次执行 grep、读取错误的文件并进行回溯

当查询是'where is the caching logic?'且函数名为\`\_build\_lru\_store\`时，grep 在第一次尝试时就派不上用场了

![Image](https://pbs.twimg.com/media/HA-BB4RbAAAjTLS?format=jpg&name=large)

---

**Antoine Chaffin** @antoine\_chaffin [2026-02-12](https://x.com/antoine_chaffin/status/2021977674898714797)

ColBERT 风格的模型保留每个词元的表示，而不是将所有内容压缩成一个向量

嵌入的软匹配能力 + 词汇搜索的细粒度匹配

非常适合代码，在代码中结构严格，但意图和语法很少使用相同的词汇

---

**Antoine Chaffin** @antoine\_chaffin [2026-02-12](https://x.com/antoine_chaffin/status/2021977678270935125)

  
我们在 CoRNStack 数据上预训练了模型，然后使用 nv-retriever 的负样本在 CoIR 训练集上进一步优化了这些模型

这个较小的模型基于 1700 万参数的 ColBERT 模型，其性能超过了 14900 万参数的模型（后者规模是前者的 9 倍），仅略逊于 EmbeddingGemma-300M 模型

![Image](https://pbs.twimg.com/media/HA-BJ6IWIAAm-Js?format=jpg&name=large)

---

**Antoine Chaffin** @antoine\_chaffin [2026-02-12](https://x.com/antoine_chaffin/status/2021977682049949916)

较大的模型基于我们即将发布的内部 LateOn 模型，其表现远超 EmbeddingGemma-300M，并且在仅 149M 参数的情况下，能够与 500-600M 参数规模的 LLMs 竞争

这两个模型都表现远超其体量，并且足够小巧，可以在本地运行

---

**Antoine Chaffin** @antoine\_chaffin [2026-02-12](https://x.com/antoine_chaffin/status/2021977684318785906)

不错的基准测试。它在实际中能正常工作吗？

AI 代理了解 grep，因此 ColGrep 保留了界面并在其基础上添加了语义排序功能

正则表达式能发现典型的重试模式，而语义排序则能揭示关于退避逻辑的意图

grep 的精确性 + 嵌入的理解

---

**Antoine Chaffin** @antoine\_chaffin [2026-02-12](https://x.com/antoine_chaffin/status/2021977686319468716)

代理们对此狂热不已，并且毫不费力地利用其有效性

我们在7个仓库中运行了135个问题（难度可变）

使用 ColGrep 生成的答案在 70%的情况下更受青睐，同时平均节省了 15.7%的 token，搜索操作减少了 56%。

---

**Antoine Chaffin** @antoine\_chaffin [2026-02-12](https://x.com/antoine_chaffin/status/2021977689138073890)

标记不是免费的

在我们的135个问题测试集上，我们节省了大约32美元

作为一个经验法则，这意味着每1000个问题243美元

它开始相当快地累积起来，尤其是考虑到大型团队的使用情况

![Image](https://pbs.twimg.com/media/HA-BftHXIAAuGLn?format=jpg&name=large)

---

**Antoine Chaffin** @antoine\_chaffin [2026-02-12](https://x.com/antoine_chaffin/status/2021977693261050304)

最令人满意的结果是，最大的提升出现在最难的问题上——这些问题描述的是行为，而非函数名，在这方面，嵌入技术表现得尤为出色

然而，对于函数名位于查询中的非常简单的查询，grep 仍然更胜一筹

这就是为什么 ColGrep 包含

![Image](https://pbs.twimg.com/media/HA-BjstbsAQovBX?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/HA-BklIWcAAmExU?format=jpg&name=large)

---

**Antoine Chaffin** @antoine\_chaffin [2026-02-12](https://x.com/antoine_chaffin/status/2021977696113213527)

ColGrep 在底层使用了 NextPlaid，这意味着尽管它是一个多向量模型，但索引和搜索过程快速且便捷

结合强大的轻量级模型，这意味着你仅用你的笔记本电脑就能从这些结果中受益

> 2026-02-10
> 
> 发布 NextPlaid 今天在 @LightOnIO。它是一个可用于生产环境的多向量数据库 🎉
> 
> NextPlaid 让你可以在几秒钟内使用我们的预构建容器部署 API。它嵌入了一个多向量数据库和一个基于 ONNX 的用于延迟交互模型的推理引擎。

---

**Antoine Chaffin** @antoine\_chaffin [2026-02-12](https://x.com/antoine_chaffin/status/2021977699804475571)

一如既往，所有内容都可供你使用并可扩展

训练代码: https://github.com/lightonai/pylate/tree/main/examples/train/lateon\_code…

模型与数据的集合: https://huggingface.co/collections/lightonai/lateon-code…

但最重要的是，不妨在 ColGrep 中试一试： https://github.com/lightonai/next-plaid/tree/main/colgrep…

这不仅仅是免费的，它还为你省钱

---

**Antoine Chaffin** @antoine\_chaffin [2026-02-12](https://x.com/antoine_chaffin/status/2021977702425645268)

尝试使用，尽情测试，我们非常感谢任何有助于改进的反馈！

作为结束语，尽管它是为代码检索而构建的，我们知道代理被用于其他任务

由于 ColGrep 支持任何 PyLate 模型，你可以用我们的其他模型扩展代理，例如

---

**Antoine Chaffin** @antoine\_chaffin [2026-02-12](https://x.com/antoine_chaffin/status/2021977704904429707)

现在是抄送和致谢的时候了！

显然要感谢我出色的联合维护者兼 ColGrep 的创建者 @raphaelsrty，他在这个项目上确实下了很大功夫

感谢 @mixedbreadai（@rikiyatakehi @aaxsh18 @bclavie @drexalt）为基于 Ettin 构建这个很酷的小型模型，以及构建 mgrep，

---

**Antoine Chaffin** @antoine\_chaffin [2026-02-12](https://x.com/antoine_chaffin/status/2021978038490026047)

  
也抄送我的老伙计们，那些喜欢深夜互动的同好们。我们最新的模型发布以来已经有一段时间了，但我们回来了，接下来几周会有很多新动作

行业正朝着一个有趣的方向发展，出现了替代 grep 的语义搜索工具，用于编码代理。有 mixedbread 开发的 mgrep，有 llamaindex 开发的 semtools，现在还有 lighton 开发的 (multi-vec) colgrep。看到这些进展非常酷。恭喜 https://t.co/HfI4mzweIf

行业正朝着一个有趣的方向发展，出现了用于编码代理的语义搜索替代 grep 的工具。有 mixedbread 开发的 mgrep，有 llamaindex 开发的 semtools，现在还有 lighton 开发的（多向量）colgrep。看到这些进展非常酷。恭喜 https://t.co/HfI4mzweIf

---

**Gregor** @bygregorr [2026-02-12](https://x.com/bygregorr/status/2022019210994737245)

你在利用轻量级模型进行代码检索方面走在正确的道路上，但在处理大型代码库时，你是否考虑过缓存对性能的影响？

---

**Antoine Chaffin** @antoine\_chaffin [2026-02-12](https://x.com/antoine_chaffin/status/2022020484892930203)

你指的是哪种缓存和哪种性能？

---

**Eddie Kollar** @eddiekollar [2026-02-12](https://x.com/eddiekollar/status/2022001532812898452)

看到这篇及时的帖子，因为我一直在研究这个方向。我已经很接近着手开发类似工具的原型了。迫不及待想用它了！

---

**Antoine Chaffin** @antoine\_chaffin [2026-02-12](https://x.com/antoine_chaffin/status/2022004098435051545)

希望它符合你的想法！

请随时告诉我们，如果有任何我们可以为你修复的小问题！

---

**Ryan D’Onofrio** @rsdgpt [2026-02-12](https://x.com/rsdgpt/status/2022066190714384648)

你们有没有停止过做饭？

---

**Antoine Chaffin** @antoine\_chaffin [2026-02-12](https://x.com/antoine_chaffin/status/2022093760717537761)

从不

---

**catid** @MrCatid [2026-02-12](https://x.com/MrCatid/status/2022011760245715169)

如果它能和大模型配合使用，会显著更受欢迎

---

**Antoine Chaffin** @antoine\_chaffin [2026-02-12](https://x.com/antoine_chaffin/status/2022012344193176031)

你是什么意思？

它与任何 PyLate 模型兼容

如果你指的是大型密集模型，那么如图所示，这些模型并没有好多少

拥有轻量级工具能够轻松在本地运行，从而轻松拥有本地最新索引

我确定

---

**ruban** @suseendran [2026-02-12](https://x.com/suseendran/status/2022071907160666301)

干得漂亮，兄弟

---

**Antoine Chaffin** @antoine\_chaffin [2026-02-12](https://x.com/antoine_chaffin/status/2022076016358043896)

谢谢兄弟！

---

**Project Atlantis e/acc** @atlantis2point0 [2026-02-12](https://x.com/atlantis2point0/status/2022040950248526289)

grep 和 awk 是垃圾，然而整个围绕它们建立的自动化编码行业却存在

---

**Antoine Chaffin** @antoine\_chaffin [2026-02-12](https://x.com/antoine_chaffin/status/2022041377287418206)

嗯，代理通过探索成功得到了答案

不过，给出更好的信号非常有帮助！

---

**dinos** @din0s\_ [2026-02-12](https://x.com/din0s_/status/2021988148230885681)

但是它能击败 BM25 吗？

---

**Antoine Chaffin** @antoine\_chaffin [2026-02-12](https://x.com/antoine_chaffin/status/2021988566520541395)

先生，请查看图表底部特意放置的那条线，不要越过它

---

**Anton** @Anton\_Kuzmen [2026-02-13](https://x.com/Anton_Kuzmen/status/2022156992358621297)

请 🙏

\`brew install colgrep\` 或者类似的命令

---

**Antoine Chaffin** @antoine\_chaffin [2026-02-13](https://x.com/antoine_chaffin/status/2022209193969934616)

@raphaelsrty ，看来 @tonywu\_71 是对的 😏

---

**RSMC全球亚洲** @RSMCGlobalAsian

尋找美國可靠的生育機構嗎？我們專注於為中國準父母提供一站式解決方案。擁有超過2000名卵子捐贈者和500多名代母隨時可供選擇，我們隨時準備支持您的生育旅程.

直接透過微信ID: RSMCIVF05 與我們經驗豐富的生育醫生聯繫，

或撥打 +1 858-314-9656 獲得個性化協助

---

**Antaripa Saha** @doesdatmaksense [2026-02-12](https://x.com/doesdatmaksense/status/2021979705172545911)

super cool man, both my fav topics (late-interaction + grep search for coding agent). can't wait to try! 

---

**Antoine Chaffin** @antoine\_chaffin [2026-02-12](https://x.com/antoine_chaffin/status/2021979964485390768)

Do not hesitate to give us feedback!!

We really believe it can be helpful for people, so we want to make it the best we can! 

---

**aditya** @adiaddxyz [2026-02-12](https://x.com/adiaddxyz/status/2021999556909834583)

whoa really really cool stuff! excited to check it out 👀 

---

**Antoine Chaffin** @antoine\_chaffin [2026-02-12](https://x.com/antoine_chaffin/status/2021999935382860017)

Please do and give us feedback!! 

---

**Celagos** @clagosarias [2026-02-13](https://x.com/clagosarias/status/2022222576190468215)

Definitely an inexplicable under explored topic.

We should definitely focus the same amount of energy on preparing better tools for AI as we are doing on preparing better harnesses.

Curious to see if this is one of those subjects @karpathy thinks is underexplored as well. 

---

**Antoine Chaffin** @antoine\_chaffin [2026-02-13](https://x.com/antoine_chaffin/status/2022226843894428119)

It is actually a large debate in the community for some time

Essentially, @bcherny said back then (and is still emphasizing it) that they tried to use embeddings-based RAG back then for Claude Code and that essentially it was wasteful because agents were finding the things 

---

**Cyrus** @cyrusnewday [2026-02-12](https://x.com/cyrusnewday/status/2022038155596378544)

Woah, super cool! 

---

**Antoine Chaffin** @antoine\_chaffin [2026-02-12](https://x.com/antoine_chaffin/status/2022039899885719718)

Thank you!! 

---

**yucel** @17Ahmetyucel [2026-02-12](https://x.com/17Ahmetyucel/status/2022001223852077547)

congratulations on the release! 

---

**Antoine Chaffin** @antoine\_chaffin [2026-02-12](https://x.com/antoine_chaffin/status/2022004139203743858)

Thank you!! 

---

**Pau** @hugemensa [2026-02-12](https://x.com/hugemensa/status/2021989133162516535)

man, you guys are on fire lately! I wonder if I should start enforcing a token limit in the functions I write 

---

**Antoine Chaffin** @antoine\_chaffin [2026-02-12](https://x.com/antoine_chaffin/status/2021989745513934864)

That's actually only the beginning :)

We have a few other releases planned in the next days (weeks if I need to sleep at some point)

Re: token limit, are you saying this because of model lengths limitation? ColBERT models have been shown to generalize very well to larger context 

---

**Omer Faruk Oruc** @orcsrise [2026-02-12](https://x.com/orcsrise/status/2022085910615998768)

Installed ColGrep on my AI coding agent. Asked "error toast notification user-facing error message"

→ Found PMInputArea.tsx, ChatInput.tsx (score 6.46)

Neither file contains "notification"

ColGrep understood intent. grep never would. 2-3 colgrep calls replaced 5-6 grep 

![Image](https://pbs.twimg.com/media/HA_kad-bsAA7DAC?format=png&name=large)