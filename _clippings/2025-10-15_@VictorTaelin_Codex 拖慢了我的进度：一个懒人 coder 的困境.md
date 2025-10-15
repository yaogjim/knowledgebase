---
title: "Codex 拖慢了我的进度：一个懒人 coder 的困境 "
source: "https://x.com/VictorTaelin/status/1978040875843289485"
author:
  - "[[@VictorTaelin]]"
published: 2025-10-15
created: 2025-10-15
description:
tags:
  - "@VictorTaelin #AI编程 #Codex #GPT-5 #开发效率 #懒编程"
---
**Taelin** @VictorTaelin [2025-10-14](https://x.com/VictorTaelin/status/1978040875843289485)

  
我被 Codex 拖慢了进度。每天只能挑选两三件事来处理，因为它每项任务都要耗费很长时间。我的日常流程大致是：

\- 醒来

\- 编写提示

\- 发送给 Codex

\- 去吃点东西

\- 回来一看，还没完成

\- 洗个澡

\- 回来一看，还没完成

\- 滑动浏览一会儿

\- 终于完成了，测试一下……能运行（80%的情况下）

\- 写下下一个提示

……我现在该拿时间怎么办……那我为什么不手动编码呢？是我懒吗？嗯确实懒，多谢关心，但更重要的是亲手敲完所有代码很可能比直接让 Codex 生成更耗时……所以我大部分时间都在等待。而且感觉在实际层面，我甚至不需要下一代模型来“感受 AGI”。等哪天出现性能相当于 gpt-5-high 但速度快 50 倍的东西，我的工作效率也能提升 50 倍，因为现在完全被推理速度卡住了脖子。另外真心希望 OpenAI 能开放模型微调功能）：Codex 每次出错，几乎都是因为不熟悉我的专业领域。它总像第一次接触线性规划似的说“啊我终于明白怎么写线性程序了，您要的是这样……”，结果下次对话又忘得一干二净，这种循环我受够了。卡帕西自己做 nanogpt 时似乎也经历过这种情况……

---

**Taelin** @VictorTaelin [2025-10-14](https://x.com/VictorTaelin/status/1978042606467658086)

  
“你为何不使用 gpt-codex 或 gpt-5-medium 呢？”

我尝试了，但额外的错误所耗费的时间比缩短推理时间所节省的还要多。

“你为什么不尝试同时处理多件事情呢？”

在一个项目中实现非常困难，但我开始考虑这一点。对我来说颇具挑战。

---

**Taelin** @VictorTaelin [2025-10-14](https://x.com/VictorTaelin/status/1978042681419874804)

  
是的，这些都是方便编造的问题，根本没人问过

---

**Adam Crabtree** @SirPenguinMan [2025-10-14](https://x.com/SirPenguinMan/status/1978044871412691265)

  
尝试多会话（6 个以上）Claude 代码监管。将其视为即时战略游戏/星际争霸（需实时主动管理）。

处理那些锦上添花的事务。重构、测试、文档、独立功能、性能优化、审计等等……

---

**Taelin** @VictorTaelin [2025-10-14](https://x.com/VictorTaelin/status/1978045432707035561)

  
可惜的是，Claude 在我的代码库上表现得很糟糕

---

**Adam Crabtree** @SirPenguinMan [2025-10-14](https://x.com/SirPenguinMan/status/1978046253322944577)

  
一旦你掌握了它常犯的所有错误，就能在每个项目的 http://CLAUDE.md 文件中预先规避这些问题 （或添加预设的斜杠指令来引导其遵循项目规范）

---

**Turned Ninja** @turnedninja [2025-10-14](https://x.com/turnedninja/status/1978070602763428238)

  
没时间可浪费。照看克劳德的代码实在太累了。

现在我仅将其用于前端任务或非重要事务。任何复杂任务，默认直接使用 gpt-5-high。Claude 代码存在两大问题：过度工程化以及对具体细节关注不足。

我手头有200美元

---

**Adam Crabtree** @SirPenguinMan [2025-10-14](https://x.com/SirPenguinMan/status/1978103153032561109)

  
你不需时刻盯着。这正是即时战略游戏的精髓所在。相比使用 Codex，运用十四行诗 4.5 1m 进行即时战略操作，效率能提升十倍。

Codex 可靠，但其沙盒限制与 Claude 代码几乎无所不能的能力相比相形见绌。不妨试试让它管理你的 AWS 基础设施或 Cloudflare 等。

---

**Florian Bansac** @FlorianBansac [2025-10-14](https://x.com/FlorianBansac/status/1978088935268974947)

  
我因手动测试应用所耗费的时间而感到效率受限。

无论 Codex 还是 Cursor 或其他工具能生成多少代码，我实在没时间测试代码是否运行良好、按钮功能是否出错，或是整体界面是否美观。

我是个笨蛋吗？

---

**Taelin** @VictorTaelin [2025-10-14](https://x.com/VictorTaelin/status/1978089198243467269)

  
你的代码结构和架构可能存在问题

所以，这很可能是个技术问题

---

**Florian Bansac** @FlorianBansac [2025-10-14](https://x.com/FlorianBansac/status/1978105973727191201)

  
我当前应用的代码量已接近50万行，其架构已从最初的设计理念逐步演变而来。

我运行测试，但当测试失败时，gpt5 有时会重写测试而不是检查错误。

---

**Florian Bansac** @FlorianBansac [2025-10-14](https://x.com/FlorianBansac/status/1978111320110371321)

  
有时也会：

我：嘿，我这儿出错了

Gpt5：哦对，我在这里放了个占位符。现在让我来创建这个函数/模板吧。

---

**Anthony** @kr0der [2025-10-14](https://x.com/kr0der/status/1978043326889628133)

  
你只是在用 Codex CLI 和 Neovim 里的 GPT-5-high 来审阅吗？

---

**Taelin** @VictorTaelin [2025-10-14](https://x.com/VictorTaelin/status/1978045485400387604)

  
仅用 vim，不用 neovim

---

**The Ontic** @tautolog [2025-10-14](https://x.com/tautolog/status/1978109393863352341)

  
你怎么会被并发资源限制住呢？同时运行多个 Codex 会话不就行了。

---

**Taelin** @VictorTaelin [2025-10-14](https://x.com/VictorTaelin/status/1978112388692856833)

  
你在这方面比我强多了！
