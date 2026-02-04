---
title: "Kevin Ma 分享 Droid 和 Codex 使用体验"
source: "https://x.com/kevinma_dev_zh/status/2017783866652824051"
author:
  - "[[@kevinma_dev_zh]]"
date: "2026-02-04T14:38:10+08:00"
created: 2026-02-04
description:
tags:
  - "@kevinma_dev_zh # Droid # Codex # 开源软件 # 代理工具 # 子任务 # 上下文管理 # UI 开发 # 编码模型"
---
**Kevin Ma** @kevinma\_dev\_zh [2026-02-01](https://x.com/kevinma_dev_zh/status/2017783866652824051)

分享下我现在怎么用 Droid 和 Codex。

我把工作流里的子任务拆成了独立的 subagent，用关键词触发。这些 subagent 用便宜的模型就够了，比如 Gemini 3 Flash 或 GLM，在 Droid 里很容易配置。

开启 session 后默认用 GPT-5.2 做 planning 和编码，需要时用关键词调用 subagent。subagent 除了模型便宜，还有个好处是独立上下文，不占用主上下文。Gemini 3 Flash 执行任务也比 GPT-5.2 快。

我还用了 VibeProxy 这款开源软件，登录了两个 ChatGPT Plus 账号，然后在 Droid 里配置代理。它支持 auto-failover，一个账号触发限制后会自动切到另一个，省去手动管理。

费用方面，两个 ChatGPT Plus 共 $40，Droid Pro $20。后者我因为订阅了 Lenny's Podcast 可以免费用。

把工作流迁移到 Droid 的好处很明显：减少工具切换，按需设计 subagent 和选择模型，优化 token 成本和上下文占用。

Codex CLI 现在不怎么直接用了，主要是配合 Happy Coder 在手机上远程操作。

![Image](https://pbs.twimg.com/media/HACYKFdbEAAE9Fu?format=png&name=large)

---

**云袭** @yalifesign [2026-02-01](https://x.com/yalifesign/status/2017882397212332296)

cc完全不用了吗，不选择opus做主代理的原因是什么呢

---

**Kevin Ma** @kevinma\_dev\_zh [2026-02-01](https://x.com/kevinma_dev_zh/status/2017906918812184693)

对，完全没有用 CC 了。主力的编码模型换成 GPT 之后，用 CC 的场景只有快速迭代 UI 开发，但这块的任务我换成 Amp Code 也能很好的满足。

再加上 antigravity，droid，warp 都有 opus 额度，基本上是用不完。那再订阅 Claude 就没有性价比了，Opus 贵。

也就是说 CC 能做的，其它工具也做得很好，比如 droid。

---

**云袭** @yalifesign [2026-02-01](https://x.com/yalifesign/status/2017914001095852218)

ui开发有考虑 gemini 3 pro 吗

---

**Kevin Ma** @kevinma\_dev\_zh [2026-02-01](https://x.com/kevinma_dev_zh/status/2017916372978971004)

有考虑，antigravity 中可以使用，只不过我近期 UI 相关的开发工作量不是很多，没有做深度的体验。

---

**vibecodinglover** @xiaoyu666shang [2026-02-01](https://x.com/xiaoyu666shang/status/2017790509587276098)

为什么不在opencode里用codex，还支持官方订阅，不需要代理，也有subagents，真心求教，我感觉把codex反代到droid里有时侯会不听话，尤其是工具调用时候，我用的proxypal，windows没有vibeproxy，求教

---

**Kevin Ma** @kevinma\_dev\_zh [2026-02-01](https://x.com/kevinma_dev_zh/status/2017800833333924130)

我尝试用过一段时间 OpenCode，在 tmux 中用不惯，当我向上滚动查看输出的内容时，它的输入框持续在底部让我感觉不舒服，并且我无法复制它输出的内容。

Droid 跟 Claude Code 以及 Codex CLI 的交互方式差不多，我用不惯 OpenCode 的交互和快捷键。

Droid 在上下文管理方面做得比较好，同一个问题有时我在 Codex CLI 中无法解决，但在 Droid 中可以。

我暂时还没遇到像你说的反代不听话的问题。

我记得 OpenCode 是只能登陆一个 ChatGPT Plus 账号，触发 limit 只能手动切换和重新登陆。但我用 Vibe Proxy 它会自动 failover 使用另一个账号。

---

**佐佑** @xiaozuoyou666 [2026-02-03](https://x.com/xiaozuoyou666/status/2018719651740684528)

我也很早用过droid，他能让早期的codex说人话，但是我现在依旧离不开codex cli的工具，哪怕他不是那么好用，但是似乎他内置的workflow的能力是远远大于其他第三方工具的，至少在opencode上面的能力是远不如codex cli的，droid我也听说很不错，不过不知道提升有多大

---

**李韭二** @lijiuer92 [2026-02-01](https://x.com/lijiuer92/status/2017982416741412978)

谢谢老师分享

---

**shafa ba** @shafajia [2026-02-01](https://x.com/shafajia/status/2017938693441618154)

droid的subagent太黑箱了，根本看不见传给了subagent的上下文是什么,用起来没啥安全感..还是amp做的好，启动subagent时会给出完整上下文,你能看到传给了subagent什么内容..