---
title: "Claude Code 写代码的爽点"
source: "https://x.com/hylarucoder/status/1931383154134401131"
author:
  - "[[@hylarucoder]]"
created: 2025-07-01
description:
tags:
  - "@hylarucoder"
---
**海拉鲁编程客** @hylarucoder [2025-06-07](https://x.com/hylarucoder/status/1931383154134401131)

最近用 Claude Code 写代码很上瘾, 开个长帖记录 Vibe Coding 的爽点.

先说结论: 强烈建议开 claude max, 比 cursor 值, 比 cursor 爽.

---

**海拉鲁编程客** @hylarucoder [2025-06-07](https://x.com/hylarucoder/status/1931384611629842472)

1) Claude Code 最爽的就是执行任务贼丝滑 —— 自动拆解任务 → 逐步执行 → lint/compile → 出错就自己修复，整个流程行云流水

那种简单但超繁琐的批量任务，手动搞估计得两三小时，现在下达指令就完了!

![Image](https://pbs.twimg.com/media/Gs2nU1zbkAAH0sR?format=jpg&name=large)

---

**海拉鲁编程客** @hylarucoder [2025-06-07](https://x.com/hylarucoder/status/1931385265085657108)

2) TypeScript 又名 AnyScript

遇到类型错误时，程序员的经典操作：

❌ 认真修类型

✅ 直接 @ts-ignore / as any

Claude Code：一行 prompt 解决你不想碰的类型地狱

---

**海拉鲁编程客** @hylarucoder [2025-06-07](https://x.com/hylarucoder/status/1931388836820766798)

3) 下达命令要分两步走

1️⃣ 先问它的建议和理解

2️⃣ 确认无误后再让它执行

千万别觉得你的能把很多任务表达清楚

模糊指令直接执行 = 踩坑预定

---

**海拉鲁编程客** @hylarucoder [2025-06-07](https://x.com/hylarucoder/status/1931390949521072368)

4) Claude Code 技巧 CC喜欢扫描文件前15行 想要效率最大化？

把重要文档/说明写在文件开头15行内可以节约很多扫文件时间.

---

**海拉鲁编程客** @hylarucoder [2025-06-07](https://x.com/hylarucoder/status/1931393271408017578)

5) Cursor 最蛋疼的是按次数计费，Claude Code 按 token 限额就友好多了

我写不那么重要的模块时会先确保「模块间保持清晰，模块内先快速完成任务」。

任务完成后再批量优化 —— 加文档、检查 interface 命名规范等等.

这种后期批量处理的场景，Claude Code 的计费模式明显更划算 💰

---

**海拉鲁编程客** @hylarucoder [2025-06-07](https://x.com/hylarucoder/status/1931394772226482547)

6) 计算机世界最难的两件事：命名和缓存 👨‍💻

良好的命名 = 成功的一半 很多时候糊出来的代码，需要更清晰的命名才能让程序员真正理解模块边界

策略：非 critical 系统可以先糊代码，再让 AI 批量死磕命名

---

**海拉鲁编程客** @hylarucoder [2025-06-07](https://x.com/hylarucoder/status/1931395763508334593)

7) 在 prompt 中直接敲 commit 就可以完成代码提交.

写得比我好多了......

![Image](https://pbs.twimg.com/media/Gs2yGt1acAAAJfd?format=jpg&name=large)

---

**海拉鲁编程客** @hylarucoder [2025-06-07](https://x.com/hylarucoder/status/1931398807012663500)

8) 和 Claude Code 协作有个磨合期

实用技巧：

1️⃣ 项目中直接 /init 让它生成 claudemd 规范

2️⃣ 遇到不听话的时候：「请把这条规则加到你的规范中」 3️⃣ 慢慢调教出专属你的工作流

---

**海拉鲁编程客** @hylarucoder [2025-06-07](https://x.com/hylarucoder/status/1931399764844916779)

9) Claude Code 自己也会"言出法随"

明明可以直接修改文件，但有的时候他会选择： 生成 Python 脚本 → 执行脚本 → 修改源码

这种"绕一圈"但结果正确的感觉真的妙不可言

---

**海拉鲁编程客** @hylarucoder [2025-06-07](https://x.com/hylarucoder/status/1931404574214250727)

10) 有人说 Vibe Coding 的这不行那不行，完全搞错重点了.

算笔账：原来繁琐但简单的任务需要3小时，现在5分钟做到80分 —— 为什么不选后者？

你只需要动脑 5分钟，就省下了半天脑力, 这点脑力可以去攻坚更难的问题.

既然驴能拉磨，人类为什么要和驴比谁更能拉磨？

人应该去做人更值得做的事情.

---

**海拉鲁编程客** @hylarucoder [2025-06-07](https://x.com/hylarucoder/status/1931405115254358334)

11) Claude Code 有的时候也会出 BUG 比如将 here document 语法写到文件里

不过概率比较低.

![Image](https://pbs.twimg.com/media/Gs26kiPbgAAzuJs?format=png&name=large)

---

**海拉鲁编程客** @hylarucoder [2025-06-07](https://x.com/hylarucoder/status/1931406203013443905)

12) 缺点2: 只有一个终端，无法像 Cursor 那样直接选中代码

依赖语言描述定位代码，虽然大多数时候很准确，但偶尔会定位错误，需要来回澄清 🎯

---

**海拉鲁编程客** @hylarucoder [2025-06-07](https://x.com/hylarucoder/status/1931411945984553281)

13) 缺点3: 不能像 Jetbrain 家移动目录/重命名这么干净无污染.

如果你有一个工具函数被10来个模块依赖. 你想重命名. 相信我, 这方面JB家还是你大爷.

LLM 的局限性这个时候就暴露出来了.

---

**海拉鲁编程客** @hylarucoder [2025-06-07](https://x.com/hylarucoder/status/1931413214367191532)

14) 缺点4: 搜索比较依赖 grep/ag , 有点是快, 缺点是还是依据文本局限性很明显, 不够懂程序.

不过话说回来, 如果海老师的 ast-grep 能勾搭上 rust 版本的openai codex 的话是不是可以雄起一波

cc @hd\_nvim

---

**海拉鲁编程客** @hylarucoder [2025-06-07](https://x.com/hylarucoder/status/1931430985981415626)

15) 缺点5: 复杂度比较高的时候不是100%稳定

当你的操作比较复杂的时候, 尽量只做"加法"，少做“变动”“减法”, 比如, 尽量减少超多的文件移动/重命名, 这些是不稳定操作，如果你这么做后面肯定要二次调整. 更好的做法：让 Claude Code 按固定格式填充注释，然后在 JetBrains 里检索+手动微调, 重构,

---

**海拉鲁编程客** @hylarucoder [2025-06-07](https://x.com/hylarucoder/status/1931440154360877315)

16) git commit 和注释 有的时候是中文, 有的时候是英文.......

建议把对 commit 和 注释的语言要求写到 claudemd 里面.

---

**海拉鲁编程客** @hylarucoder [2025-06-07](https://x.com/hylarucoder/status/1931441728508273079)

17) Claude Code + WebStorm 的组合意外称手

用 CC 的第一天我想的是：WebStorm 要完了

用 CC 的第四天我回过味来: WebStorm 不会完，Cursor 反而危险了.

逻辑很简单：Claude Code 解决了编辑器智能的问题，这时 Cursor 要解决的问题. 剩下来的编辑体验只能从工程上下手, 而这是 JB 家的强项.

如果 Cursor 不能收购 JetBrains 或被 Claude 收购，处境会很尴尬.

至少, 这几天我发现我很少打开 Cursor