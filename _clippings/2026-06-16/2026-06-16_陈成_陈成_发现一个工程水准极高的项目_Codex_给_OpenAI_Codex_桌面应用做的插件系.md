---
title: "2026-06-16_chenchengpro_陈成_发现一个工程水准极高的项目_Codex_给_OpenAI_Codex_桌面应用做的插件系统"
source: "https://x.com/chenchengpro/status/2050051524580303178"
author:
  - "[[@chenchengpro]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "x"
  - "@chenchengpro"
  - "codex"
  - "asar"
---

# 陈成: 发现一个工程水准极高的项目：Codex++，给 OpenAI Codex 桌面应用做的插件系统

**陈成**

发现一个工程水准极高的项目：Codex++，给 OpenAI Codex 桌面应用做的插件系统。

Codex 是闭源代码签名的 Electron 应用，没有任何扩展机制。这个项目的做法相当硬核——它需要突破四层防线才能把代码注入进去：

第一层，改 asar 包。用 @electron/asar 解包 app.asar，把 package.json 的 main 字段从原始入口改成自己的 loader.cjs，同时精确保留原始 asar 的 unpacked 文件集（否则 Electron 的模块加载会 MODULE\_NOT\_FOUND）。重打包用原子操作：先写临时文件再 rename，防止写入中断导致 app 损坏。

第二层，过完整性校验。Electron 会校验 asar header 的 SHA-256（注意不是整个文件，是 header JSON），存在 Info.plist 的 ElectronAsarIntegrity 里。改完 asar 必须同步更新这个哈希。

第三层，关 fuse。Electron 在 Framework 二进制里有一组 fuse 开关，用已知的 sentinel 字符串 "dL7pKGdnNz796PbbjQWNKmHXBZaB9tsX" 定位，后面跟 version + count header，每个 fuse 占一字节（ASCII '0'=off, '1'=on）。直接把 EnableEmbeddedAsarIntegrityValidation 从 '1' 改成 '0'。加上第二层的哈希更新，形成双保险。

第四层，重签名。上面的操作破坏了原始 Developer ID 签名，用 codesign --force --deep --sign - 做 ad-hoc 重签名，让 macOS 不拦截。

注入的 loader.cjs 只有 70 行，设计原则是"插件系统崩了绝不能带崩 Codex"。所有逻辑包在 safe() 里，异常只写日志到 loader.log，最后一行永远是 require("./" + originalMain)——无条件把控制权交还给 Codex 原始入口。

Runtime 层也有意思。它需要访问 Codex 的内部 window services 对象，但这是个 minified 的闭源 bundle，变量名是混淆过的。解法是用 fingerprint 匹配：搜索包含 buildFlavor: 的工厂函数调用，然后检查调用体里是否同时包含 allowDevtools:、preloadPath:、globalState: 等至少 5 个已知属性名，命中后回溯找到赋值的变量名，在语句结尾注入 globalThis.codexpp\_window\_services = ;。一套完整的 JS AST 级别的 source patch。

Sparkle 自动更新兼容是最精巧的部分。Sparkle 要求有效的 Developer ID 签名才能更新，但补丁后的 app 只有 ad-hoc 签名。解决方案：hook Node 的 Module.\_load，拦截 Sparkle 模块的 installUpdatesIfAvailable 方法。更新前用 ditto 把备份的原始签名 .app 复制回去让 Sparkle 正常工作，更新完后 launchd 监听到 app.asar 文件变化，自动触发 codexplusplus repair --quiet 重新走一遍补丁流程。全自动，用户零感知。

不是一个简单的 monkey-patch，是从二进制 fuse 到 JS source patch 到 Sparkle hook 的完整工程体系。

[GitHub - b-nnett/codex-plusplus: Codex++ 微调系统 for the Codex 桌面应用](https://t.co/ESzJnusGj7)

![图片](https://pbs.twimg.com/card_img/2050051524634750976/Fnd_sV2S?format=jpg&name=large)

* * *

### 热门回复

**@实践哥MinLi** ♥ 582 · 💬 7

年初的时候，我跟朋友说，今年最值得掌握的两个技术，一个是Auto research，一个是 multi agent。

这个文章把两个技术结合起来了，非常值得参考，跟自己平时用的做印证。

**@宝玉** ♥ 448 · 💬 27

OpenAI 官方推出 Ralph loop 功能了，给 Codex CLI 加了个 /goal 命令。也就是说：你定个目标，它就一直跑，跨多轮不丢，不达目的不停。

这是 0.128.0 版本里的新东西，要在 ~/.codex/config.toml 的 \[features\] 段写一句 goals = true 才能启用。

\[features\]

goals = true

目前只在终端 CLI

**@小宇玩ai** ♥ 0 · 💬 0

Sparkle 这一层最精巧但也最脆弱。fingerprint 匹配 + Module.\_load hook 都是绑死在当前 bundle 拓扑上的，OpenAI 任何一次小的内部重构都会打回 sentinel 阶段。这种成功状态的半衰期通常按 OpenAI 客户端版本号算，不是按月算。能玩，别长期依赖。

**@ZFC** ♥ 0 · 💬 0

英雄所见略同，感觉 codex 可以做出花来也，接入 symphony

**@크롱** ♥ 0 · 💬 0

最终，这是一种硬核方法，从对 asar 包进行修改开始，以突破那个封闭的生态系统。超越仅仅添加功能，通过工程手段强行撬开被提供者阻止的可扩展性的结构性阻力是