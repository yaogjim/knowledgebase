---
title: "2026-01-07_geekshellio_你有没有想过_有一天编程可以像回微信一样随时随地进行_一个叫_mgranda_的开发者真的做到了"
source: "https://x.com/geekshellio/status/2008335070000816283"
author:
  - "[[@geekshellio]]"
published: 2026-01-07
created: 2026-01-07
description:
tags:
  - "x"
  - "@geekshellio"
  - "https"
  - "2026-01-06"
---

# 你有没有想过，有一天编程可以像回微信一样随时随地进行？ 一个叫 mgranda 的开发者真的做到了，

**安仔** @geekshellio [2026-01-06](https://x.com/geekshellio/status/2008335070000816283)

你有没有想过，有一天编程可以像回微信一样随时随地进行？

一个叫 mgranda 的开发者真的做到了，他现在用手机同时跑六个 AI 编程助手，完全不需要电脑，就靠一台云服务器和几个巧妙的工具组合。

想想我们平时的困境，灵感来了却不在电脑前，或者在通勤路上突然想改个 bug，只能干着急。

他的方案彻底解决了这个痛点。核心思路其实很简单，就是把开发环境完全搬到云端，然后通过手机终端随时接入。

具体怎么做的呢。他租了一台 Vultr 的云服务器，配置还不错，8 核 32G 内存，关键是按小时计费，每小时两毛九美金。

不用的时候直接关机，一天满负荷跑也就七美元。他甚至写了个 iOS 快捷指令，可以直接在手机上一键启动服务器，连电脑都不用碰。

安全性他也考虑得很周到。这台服务器根本没有公网 SSH 端口，所有访问都走 Tailscale 这个私有网络。

就算有人知道服务器 IP 也连不上，因为防火墙只允许 Tailscale 的协调流量通过。这种多层防御的思路，比那些直接把 SSH 暴露在公网上的做法安全太多了。

但真正让这套方案实用的是两个细节：

第一个是 mosh 这个工具，它能让你的终端连接在网络切换时不断线。你可以从 WiFi 切到 4G，甚至手机锁屏休眠，连接都还在。

这对手机使用场景太重要了，不然每次网络波动都要重新连接，用户体验起来就很麻烦。

第二个细节就是推送通知。Claude Code 在需要你输入的时候会自动触发一个 webhook，直接给你手机发推送。

这样你就不用一直盯着屏幕了，可以把任务扔给 AI，然后该干嘛干嘛，等手机震动了再回来看。

他还用 tmux 做会话管理，配合 Git 的 worktree 功能同时开发多个特性分支。

每个分支一个独立的工作目录，每个目录跑一个 Claude 代理，互不干扰。

端口分配都是根据分支名自动计算的，完全不会冲突。六个窗口，六个功能，一部手机全搞定。

最打动我的其实是他描述的使用场景。等咖啡的时候审个 PR，坐地铁的时候让 AI 重构一段代码，窝在沙发看电视的时候顺手修个 bug。

开发不再需要专门的整块时间，而是可以见缝插针地塞进生活的碎片里。这种灵活性对很多人来说可能是革命性的。

整套系统搭建起来也不复杂，他说自己就用了一个 Claude Code 会话就配置完了。

给 AI 提供 Vultr 的 API 密钥和 GitHub 访问权限，告诉它需求，然后就自动完成了。这种用 AI 搭建 AI 开发环境的方式，其实本身就挺有意思的。

现在是 2026 年，这种移动开发的模式可能会越来越普遍。

当 AI 能处理大部分编码工作，我们需要做的更多是决策和指导，那设备的形态可能真的不再重要。

也许再过几年，抱着笔记本去星巴克写代码会变成一种复古潮流，就像现在还有人坚持听黑胶唱片一样，更多是仪式感而非刚需。

![Image](https://pbs.twimg.com/media/G98JzB2bcAAct70?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G98J_ZdbAAANwOP?format=png&name=large)

* * *

**安仔** @geekshellio [2026-01-06](https://x.com/geekshellio/status/2008335072718676009)

原文链接：

* * *

**Hans** @henieshuang [2026-01-06](https://x.com/henieshuang/status/2008559626246295576)

主要手机上不好预览，不能完全放手

* * *

**安仔** @geekshellio [2026-01-06](https://x.com/geekshellio/status/2008573839954112780)

起码做些 bugfix 和小功能开发之类的，还是挺方便的，尤其是后端开发。

* * *

**ONE FOR ISRAEL Ministry** @oneforisrael

Millions in Israel are viewing our Gospel videos! Help us reach Israel in these crucial days!

以色列有数百万观众在观看我们的福音视频！帮助我们在这些关键的日子里触达以色列！

* * *

**Soran（懒人的 AI 万能口袋）** @Soranlan [2026-01-06](https://x.com/Soranlan/status/2008341417517621449)

蛙趣，随时随地编码，并利用 AI 助手，这个想法真的是革命性的。

* * *

**安仔** @geekshellio [2026-01-06](https://x.com/geekshellio/status/2008342607928390121)

的确如此的，里面说的都是我的刚需，很多时候在外面想到新的灵感或者 bugfix 想法，我都是干等着回家改，现在用手机就可以帮我解决就很舒服。

* * *

**Alex e/acc** @alex\_metacraft [2026-01-06](https://x.com/alex_metacraft/status/2008607207160791131)

不需要这么麻烦，用https://github.com/cyhhao/vibe-remote… 就可以了

* * *

**leon7hao** @leon7hao [2026-01-06](https://x.com/leon7hao/status/2008563713033597242)

需要的话来试试 http://lody.ai

* * *

**朽木愚夫** @davis926tw [2026-01-07](https://x.com/davis926tw/status/2008690554465566868)

有想過 如果哪天我出去單幹 就會這麼做。

但現在幫老闆幹...還是回公司再說吧 哈哈

* * *

**only\_onepig** @only\_onepig [2026-01-06](https://x.com/only_onepig/status/2008589028032184499)

关机也算费用的

* * *

**Impcm** @imp\_hgf32447 [2026-01-07](https://x.com/imp_hgf32447/status/2008694265925562877)

感觉没啥意义，手机的屏幕还是太小了，操作不方便，临时有个idea，记下来，方便用电脑的时候再处理，也不是不行，毕竟电脑的效率比手机高多了。