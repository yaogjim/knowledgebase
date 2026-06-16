---
title: "2026-06-16_Jimmy_JingLv_停止切换_冻结_Context"
source: "https://x.com/Jimmy_JingLv/status/2043946966187684297"
author:
  - "[[@Jimmy_JingLv]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "#2549"
  - "#D97757"
  - "x"
  - "@Jimmy_JingLv"
---

# 停止切换，冻结 Context

**吕立青\_JimmyLv 2𐃏26**

# 停止切换，冻结 Context

我现在同时在七八个项目里跑 Claude Code，每个项目还有好几个功能并行写。切过去的那一秒，我忘了它上次在做什么——翻历史、找 git 状态、看文件改到哪，一次切换烧掉五分钟。一天下来大脑被 context switch 磨平，真正思考的时间反而不够。

问题不在 Claude，也不在并发数。问题在切换本身。

解法只有一条：别切，冻结。让每个项目的工作状态——Claude 的对话、展开的目录、看到的 diff、shell history——原样冻结在它自己的终端会话里。需要的时候解冻回来，不用回忆，不用重建。

用 tmux session 做 context 的冰箱，一条 cc 命令帮你冻结 + 解冻。

![Image](https://pbs.twimg.com/media/HF2NG9paUAAHDLE?format=jpg&name=large)

## 诊断：并行 AI agent 的认知税是怎么收的

你以为开 8 个 Claude Code 只是"多 8 倍代码产出"。实际上你还多了 8 倍切换成本，而且成本不是线性增加，是指数级。

每个项目背后有一堆隐性状态：

- Claude 上次回答到哪、对话轨迹是什么
- 你改了哪些文件，哪些 staged 哪些没
- 文件树展开到第几层、你在看哪个模块
- shell 历史里最近敲过什么
- 你为什么选当前这个分支而不是别的

八个并行 = 这些状态 × 8 ≈ 40 个 chunk。人脑 working memory（工作记忆） 容量大概 4-7 个 chunk。超标 600%。

所以切过去那一秒必然崩。你开始 git status、翻 shell history、翻 Claude 对话、翻浏览器 tab——每次都在从零重建 context。

传统建议是多记笔记、开 checklist、写 ADR。没错，但这些是把 context 外包给你自己的大脑写作能力——前提是你有能力把复杂状态压缩成文字。Claude Code 的并行状态机太复杂，压缩必然丢信息，翻回去读笔记本身也是认知消耗。

换个思路：不压缩，不外包。让 context 原样留在它本来的位置——终端里。

## 架构：tmux session = context 的冰箱

一个 tmux session 是什么？一个完整的、持续运行的终端环境。它包含：

- 若干 pane，每个跑自己的进程
- 每个 pane 的 scrollback（你看过的所有输出）
- 每个进程的实时状态（Claude 对话不会因为你关 GUI 而消失）
- 相关环境变量、工作目录

tmux session 和 GUI 窗口解耦。关掉 cmux 窗口，session 还在系统后台活着；从任何 shell——包括手机 SSH 回来——tmux attach 就接回来了，所有状态原封不动。

这就是"冰箱"的隐喻：

- tmux detach（Ctrl+Space d）= 关冰箱门
- tmux attach = 开冰箱门
- 里面的东西不会变质，不会忘

规则很简单：一个项目 = 一个 session。八个项目 = 八个 session，彼此隔离。切过去不用回忆，因为所有 context 都在 session 里等你。

这就是"停止切换，冻结 context"的全部含义。

## 落地：一条 cc 命令

把架构变成肌肉记忆需要降低摩擦。cc 一键起一个完整工作区：

```bash
j BibiGPT
cc
```

瞬间得到一个叫 cc-bibigpt 的 tmux session，三 pane 布局自动摆好：

```bash
┌─────────────────────────┬─────────┐
│ │  broot  │ ← 折叠树 + 模糊搜索 + git 状态
│ │ │
│ Claude Code ├─────────┤
│ (75%) │ lazygit │ ← git diff / commit / stash
│ │ │
└─────────────────────────┴─────────┘
```

![Image](https://pbs.twimg.com/media/HF2PLL8a0AAw4Jh?format=jpg&name=large)

三个工具各司其职，没一件冗余：

![Image](https://pbs.twimg.com/media/HF2NlcOasAEjun1?format=jpg&name=large)

切到另一个项目时——新终端 cc 回车，建立第二个 session cc-other-project。原来那个冻结在后台，Claude 不受影响地继续等你。

回来？tmux a -t cc-bibigpt 或者 cca（下文有 fzf 模糊选的 alias）。

一个踩坑：不要用 yazi 当文件管理

我最初在右侧 pane 跑

[yazi](https://yazi-rs.github.io/)（Warp 官方赞助的 Rust TUI 文件管理器），结果发现它是 Miller columns 设计（像 macOS Finder 的列视图），不是折叠树；/ 搜索还只过滤当前目录。换到 broot 才解决——打字即全项目过滤，这才是认知负担减半的那种工具。

## 底座：为什么必须是 cmux + tmux

这个组合是踩坑换来的。核心三条约束：

1.  state 必须跟着 shell session 走，不能跟着 GUI 窗口——否则关窗就死
2.  主终端要支持真· libghostty 渲染——处理 Claude TUI 的复杂转义序列不出幺蛾子
3.  得有侧边栏——认知上要一眼分清哪个项目

Ghostty 本身做不到侧边栏

直接用 Ghostty 行不行？不行。Ghostty 的

[Vertical Tabs Discussion #2549](https://github.com/ghostty-org/ghostty/discussions/2549)，2026 年 3 月 Mitchell Hashimoto 亲手关了。原因：自定义 tab bar 违背 Ghostty "只用原生平台 UI"的哲学。纯 Ghostty 没有侧边栏，未来也不会有。

三个自称"基于 Ghostty"的东西，含金量分三档

扒完代码做了这张表：

![Image](https://pbs.twimg.com/media/HF2Ou2maQAAja57?format=jpg&name=large)

Orca 最迷惑——落地页写着 "The Worktree IDE for Claude Code, Ghostty & AI Coding Agents"，但 README 里唯一一处 Ghostty 是 "Ghostty-inspired terminals"。inspired 这个词的含金量大家自己体会。

cmux 的 CI 就诚实多了：

```bash
# .github/workflows/build-ghosttykit.yml
cd ghostty && zig build \
  -Demit-xcframework=true \
  -Dxcframework-target=universal \
  -Doptimize=ReleaseFast
```

这段在编译真正的 Ghostty 到 Apple xcframework（Apple 的二进制框架格式）。仓库里有个 ghostty/ submodule 指向他们自己 fork 的 manaflow-ai/ghostty（不是上游，因为上游 libghostty 还在 alpha），但渲染引擎是真货。另外 Resources/ghostty/ 下还打包了 100+ Ghostty 主题和 xterm-ghostty 终端描述——这不是借鉴，是真把 Ghostty 搬进来了。

cmux = 真 Ghostty 内核 + Warp-like 工作区侧边栏。这是你要的底座。

tmux 不可替代

cmux 的侧边栏是 workspace 列表，不是文件树；而且它在 GUI 层——关掉窗口 state 全死。冻结 context 的职责必须交给 tmux session。

为什么不是 Zellij？Zellij 的布局声明式更美，但：

- 手机端 SSH attach 普遍性：tmux > Zellij
- 社区生态、troubleshooting 资源：tmux > Zellij
 
 社区生态、故障排除资源：tmux 到 Zellij
- 老旧服务器 / VPS 可达性：tmux > Zellij

tmux 唯一缺点是默认状态栏丑——下文配置里会改成 Claude 橙极简版。

## 10 分钟复刻配置

1\. 装工具

```bash
# cmux（基于 Ghostty 的终端 GUI）
brew tap manaflow-ai/cmux
brew install --cask cmux

# 三件 TUI
brew install tmux broot lazygit
```

2\. Ghostty config（cmux 共用 · ~/.config/ghostty/config）

2\. Ghostty 配置（cmux 共用 · ~/.config/ghostty/config）

```bash
macos-option-as-alt = true
theme = Catppuccin Mocha
background-opacity = 0.95
```

macos-option-as-alt = true 让 tmux 的 Alt+hjkl 切 pane 能工作。cmux 直接读这份配置，不用重复写。

3\. tmux 配置（~/.tmux.conf）

```bash
# 前缀键：Ctrl+Space（默认 Ctrl+B 会被 Claude TUI 吃掉）
unbind C-b
set -g prefix C-Space
bind C-Space send-prefix

# 基础
set -g mouse on
set -g base-index 1
setw -g pane-base-index 1
set -g escape-time 10
set -g history-limit 100000

# 颜色
set -g default-terminal "tmux-256color"
set -ga terminal-overrides ",xterm-ghostty:Tc,xterm-256color:Tc,*:RGB"

# Yazi/broot 等 TUI 正确工作的前提
set -g allow-passthrough on
set -ga update-environment TERM
set -ga update-environment TERM_PROGRAM

# Popup 浮层
bind g display-popup -E -w 90% -h 90% -d "#{pane_current_path}" lazygit
bind b display-popup -E -w 85% -h 85% -d "#{pane_current_path}" broot

# Alt 切 pane
bind -n M-h select-pane -L
bind -n M-j select-pane -D
bind -n M-k select-pane -U
bind -n M-l select-pane -R

# 禁止应用偷偷改窗口名（Claude 会发 OSC 标题序列污染状态栏）
set -g allow-rename off
set -g automatic-rename off

# Status bar：极简 + Claude 橙 #D97757
set -g status-position bottom
set -g status-style 'bg=default fg=#8a8a8a'
set -g status-left-length 40
set -g status-left  '#[fg=#D97757,bold] #S #[fg=#3a3a3a]│ '
set -g status-right '#[fg=#8a8a8a]%H:%M '
setw -g window-status-format '#[fg=#3a3a3a] ○ '
setw -g window-status-current-format '#[fg=#D97757,bold] ● '
set -g message-style 'fg=#D97757 bg=default'
set -g pane-border-style 'fg=#2a2a2a'
set -g pane-active-border-style 'fg=#D97757'

bind r source-file ~/.tmux.conf \; display-message "reloaded"
```

4\. broot 默认排序（~/.config/broot/conf.hjson）

broot 首次启动会生成 ~/.config/broot/conf.hjson。找到 # default\_flags: 那行，改成：

default\_flags: "--sort-by-type-dirs-first -g"

默认标志: "--sort-by-type-dirs-first -g"

- \--sort-by-type-dirs-first：目录永远置顶
- \-g：显示每个文件的 git 状态（M 修改、A 新增、? 未追踪）

trade-off：这会把折叠树变扁平列表——但 broot 的核心交互本来就是打字过滤不是 scroll 浏览，打 src 就直达目标，排序模式怎样不重要。

5\. cc 函数 + cca alias（加进 ~/.zshrc）

```bash
cc() {
  # 已在 tmux 内就直接跑 claude
  if [[ -n "$TMUX" ]]; then
 claude --dangerously-skip-permissions "$@"
 return
  fi
  # 按项目目录命名 session，重名自动加 -2 -3 后缀
  local base="cc-${PWD##*/}"
  local session="$base"
  local i=1
  while tmux has-session -t "$session" 2>/dev/null; do
 i=$((i + 1))
 session="${base}-${i}"
  done
  tmux new-session -d -s "$session" -c "$PWD" "claude --dangerously-skip-permissions $*"
  tmux split-window -h -l 25% -t "$session" -c "$PWD" broot
  tmux split-window -v -l 50% -t "$session" -c "$PWD" lazygit
  tmux select-pane -L -t "$session"
  tmux attach -t "$session"
}

# fzf 模糊选 session 解冻
alias cca='tmux a -t "$(tmux ls -F "#S" | fzf --prompt="attach> ")"'
```

6\. 启动 + 并行多项目演示

```bash
tmux kill-server # 第一次配置保险起见
source ~/.zshrc # 加载 cc / cca

cd ~/project-a && cc  # 建 session: cc-project-a
# 再开一个 cmux workspace/pane：
cd ~/project-b && cc  # 建 session: cc-project-b
# 同一项目想开第二个 session？
cd ~/project-a && cc  # 自动建 cc-project-a-2
```

每个 session 彼此隔离——Claude 上下文、broot 位置、lazygit 状态互不干扰。

```bash
tmux ls # 看所有在跑的 session
cca # fzf 模糊选 + attach（推荐）
tmux a -t cc-project-a # 记得确切名字就直接 attach
tmux kill-session -t cc-xxx # 清掉某个
```

7\. 键位速查

![Image](https://pbs.twimg.com/media/HF2OVjlasAQfU7D?format=jpg&name=large)

broot 里：打字即过滤，↑↓ 选，Alt+Enter cd 到该目录并退出 broot，Esc 取消搜索。

lazygit 里：方向键切栏/选文件，空格暂存，c 提交，P 推送，u 撤销，q 退出。

## 手机接着干：跨设备不丢 context

tmux session 可跨设备——这是"冻结 context"最大的意外福利。

1.  Mac 上 cmux 跑 cc，建立 session
 
 在 Mac 上，cmux 运行 cc，建立会话
2.  出门前 Ctrl+Space d 冻结（session 保留在后台）
3.  手机用
 
 [Blink Shell](https://blink.sh/) SSH 回 Mac（推荐
 
 [Tailscale](https://tailscale.com/)
 
 内网穿透，不折腾端口转发）
 
4.  tmux a -t cc-项目名 解冻——Claude 对话、broot 位置、lazygit 状态全在

cmux 的 GUI 层上不了手机，但它底下的 tmux session 可以。这才是真正的"换设备不丢 context"。

## 两个反直觉的收获

第一：产品宣传"基于 X"的时候，翻 CI 和 submodule 比读 README 靠谱。

- Orca 的 README/落地页反复提 Ghostty——代码零引用，营销话术
- cmux 的 README 说 "powered by libghostty"——CI 里真在编 Ghostty
 
 cmux 的 README 说 "由 libghostty 提供支持"——CI 里真的在编译 Ghostty

Mitchell 关掉 vertical tabs 那个 discussion 的时候，没想到有人干脆把整个 Ghostty 编进 Xcode 工程。官方关了大门，社区自己开了窗。

第二：并行 AI agent 的认知负担，不在"开多少"，在"切回来能不能秒 pickup"。

传统建议是多笔记、多 checklist——但 Claude Code 并行状态机的复杂度已经超过人脑 working memory，靠记忆硬扛就是崩溃。真正的解法是不依赖大脑。

Warp 那种 GUI 侧边栏看起来酷，state 跟着 GUI 窗口走，关闭即死。tmux session 跟着 shell 走，跨设备可 attach。一个在拼 UI，一个在做架构。并行八个项目的时候，差别立刻显出来。

> 停止切换，冻结 context。不跟自己的记忆力较劲——让终端当 context 的冰箱。

## 附录：libghostty 二次开发现状

顺手扒清楚的部分，因为很多人搞混：

![Image](https://pbs.twimg.com/media/HF2Ok_wboAAlQ37?format=jpg&name=large)

Mitchell 自己的措辞："public alpha, not promising API stability"——但他补一句：核心逻辑跟 Ghostty 共享，极其稳定。不稳定的是外层 API 形状，不是终端逻辑。他目标 6 个月内发 tagged libghostty-vt。

现阶段做二次开发有两条路：

1.  等官方 libghostty 出 stable 版
2.  学 cmux，自己 fork Ghostty 编成二进制框架链接——走得通，但要自己扛维护成本

官方参考实现是

[ghostty-org/ghostling](https://github.com/ghostty-org/ghostling)：单 C 文件的最小终端 demo，用 libghostty-vt + Raylib 自己画窗口。944 stars，每周还在更新。想玩的从这里起步。

## 参考资料

- [Ghostty Vertical Tabs Discussion](https://github.com/ghostty-org/ghostty/discussions/2549) #2549（官方关闭侧边栏需求） — GitHub Discussion
 
 [Ghostty 垂直标签页讨论](https://github.com/ghostty-org/ghostty/discussions/2549)
 
 #2549（官方关闭侧边栏需求） — GitHub 讨论
 
- [manaflow-ai/cmux（真·Ghostty 内核的 Warp-like 终端）](https://github.com/manaflow-ai/cmux) — GitHub
 
 [manaflow-ai/cmux（基于真·Ghostty 内核的类似 Warp 的终端）](https://github.com/manaflow-ai/cmux)
 
 — GitHub
 
- [stablyai/orca（Ghostty-inspired 的 AI agent IDE）](https://github.com/stablyai/orca) — GitHub
 
 [stablyai/orca（受 Ghostty 启发的 AI 代理 IDE）](https://github.com/stablyai/orca)
 
 — GitHub
 
- [Mitchell Hashimoto: Libghostty Is Coming](https://mitchellh.com/writing/libghostty-is-coming) — 官方博客
 
 [Mitchell Hashimoto: Libghostty 即将到来](https://mitchellh.com/writing/libghostty-is-coming)
 
 — 官方博客
 
- [ghostty-org/ghostling（libghostty C API 参考实现）](https://github.com/ghostty-org/ghostling) — GitHub
 
- [broot 官方文档](https://dystroy.org/broot/)
 
- [lazygit](https://github.com/jesseduffield/lazygit) — GitHub