---
title: "2026-03-09_Leo_Leo_给_Claude_Code_接了个_X_搜索引擎_基于_Grok_搭了个本地桥接服"
source: "https://x.com/runes_leo/status/2030787396976132253"
author:
  - "[[@Leo]]"
published: 2026-03-09
created: 2026-03-09
description:
tags:
  - "x"
  - "@Leo"
  - "claude"
  - "code"
---

# Leo 给 Claude Code 接了个 X 搜索引擎。 基于 Grok 搭了个本地桥接服

**Leo**

给 Claude Code 接了个 X 搜索引擎。 基于 Grok 搭了个本地桥接服务，常驻后台，Claude Code 需要搜 X 时自动调用。终端一行命令，几秒返回摘要 + 相关用户原话。 两个关键优势：不走 X 官方 API（省掉每月 $200 的 Basic 套餐），而且能搜到实时动态——API 搜索有延迟和索引限制，Grok 直接拿最新的。（前提：可能需要 X Premium+/Premium的 Grok 权限） 最典型的场景：跟 Claude Code 干活时想知道某个话题在 X 上的最新讨论——谁在聊、什么观点、有没有坑。以前得切浏览器手动搜，现在 Claude 自己去查，带着摘要回来继续干活。 搭完之后回不去了。信息获取从"我去找"变成"它帮我找"，体感完全不一样。

![图片](https://pbs.twimg.com/media/HC5iRzqbMAAQcbT?format=jpg&name=large)

* * *

### 热门回复

**@QingYue** ♥ 10 · 💬 1

woc 咋两这个思路差不多啊 果然是英雄所见略同

**@Cryptoxiao** ♥ 3 · 💬 1

直接用6551的推特mcp 更便宜 更方便

**@sunyoung** ♥ 5 · 💬 1

我之前做别的项目时还用过一种类似但更“底层”的方式：直接让 Claude Code 启动一个模拟浏览器（headless browser），抓取网页请求里的接口和 token，然后把这些参数拿出来，后续用 curl 或 HTTP client 直接模拟请求。这样其实也能把网页能力转成脚本化调用。 本质上都是同一个思路：把 Web UI 当作

**@Leo** ♥ 0 · 💬 2

6551确实好用，不过我快没额度了所以不得不找找替代方案哈哈

**@maxtimer** ♥ 0 · 💬 2

@grok 怎么实现的