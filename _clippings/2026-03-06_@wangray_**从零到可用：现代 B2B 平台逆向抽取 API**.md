---
title: "**从零到可用：现代 B2B 平台逆向抽取 API**"
source: "https://x.com/wangray/status/2029587037029064778"
author:
  - "[[@wangray]]"
date: "2026-03-06T10:08:42+08:00"
created: 2026-03-06
description:
tags:
  - "@wangray # B2B 平台逆向抽取# Web GUI 自动化# API 抽取# Chromium DevTools Protocol# 无头浏览器# 逆向工程"
---
**Ray Wang** @wangray [2026-03-05](https://x.com/wangray/status/2029587037029064778)

🧵 今天在客户公司，3 小时把一个没有公开 API 的 B2B 平台变成了全自动化工具。

从零到可用，方法论分享👇

---

**Ray Wang** @wangray [2026-03-05](https://x.com/wangray/status/2029587039390413046)

1/ 核心思路：不要模拟点击，要拦截请求。

大多数人想到"自动化 Web 操作"，第一反应是 Selenium、Playwright，模拟人点按钮。

问题是：现代前端框架（React/Vue/Ant Design）的虚拟事件系统会拦住你。Upload 组件点不动，SPA 切页后 DOM 引用失效，模拟链条越长越脆。

换个思路：让人操作，让机器拦截。

---

**Ray Wang** @wangray [2026-03-05](https://x.com/wangray/status/2029587041403744282)

2/ 具体做法：

① 用无头浏览器打开目标页面

② 注入一段 JS，hook 住 XMLHttpRequest 的 open/send

③ 人手动完成一次完整操作（创建、配置、发布）

④ 机器在后台记录所有请求——URL、headers、body 全拿到

一轮操作下来，8 个内部 API 端点全部逆向完成。1.5 小时。

---

**Ray Wang** @wangray [2026-03-05](https://x.com/wangray/status/2029587044138352888)

3/ 最大的坑：httpOnly cookies。

浏览器里 fetch 能正常发请求，脚本里死活 401。排查了近 1 小时。

原因：document.cookie 拿不到 httpOnly 标记的 cookie。浏览器自动带上了，但你在外部脚本里手动拼 cookie header 时少了关键字段。

解法：用 CDP (Chrome DevTools Protocol) 拿完整 cookie 列表，包括 httpOnly 的。一行命令搞定。

---

**Ray Wang** @wangray [2026-03-05](https://x.com/wangray/status/2029587046222962886)

4/ 另一个隐藏坑：cookie domain 污染。

同一个浏览器里 http://auth.xxx.com 和 http://platform.xxx.com 的 cookie 混在一起。全部发过去，服务端反而 CSRF 校验失败。

必须按 domain 过滤，只保留目标域名的 cookie。

---

**Ray Wang** @wangray [2026-03-05](https://x.com/wangray/status/2029587048332726585)

5/ 拿到 API 之后，封装成一个零依赖的 Python CLI（只用 urllib，任何环境都能跑）。

支持单条命令，也支持 JSON 配置批量执行。

结果：之前手动操作 10 分钟/个的流程，现在 5 秒。30 个实例从 5 小时 → 2 分钟。

---

**Ray Wang** @wangray [2026-03-05](https://x.com/wangray/status/2029587050459287750)

6/ 这套方法论可以复制到任何有 Web GUI 但没有 API 的 B2B 平台。

核心公式：

人操作 + 机器拦截 > 模拟点击

CDP cookies > document.cookie

逆向是冷启动手段，不是终点

Plaid 早期做的事情本质上一样——银行没有好 API，Plaid 自己用 screen scraping 造了一个，后来做成了 $60 亿的公司。

逆向不丢人，关键是逆向完了之后往哪走。

---

**招财牛猫 | AI情报** @LuckyBullCat [2026-03-05](https://x.com/LuckyBullCat/status/2029588531727769708)

同类场景先录制关键流程 再补重试和幂等键 失败率能从两成压到个位数

---

**Ray Wang** @wangray [2026-03-05](https://x.com/wangray/status/2029590230978924883)

👍学习了

---

**Simon@Twillot** @mytwillot [2026-03-05](https://x.com/mytwillot/status/2029698994038046955)

碰上推特这种容易封号，有前端加密的也不行