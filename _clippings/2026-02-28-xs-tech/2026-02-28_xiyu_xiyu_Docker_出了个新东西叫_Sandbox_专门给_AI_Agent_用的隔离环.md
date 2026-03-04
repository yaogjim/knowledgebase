---
title: "2026-02-28_xiyu_xiyu_Docker_出了个新东西叫_Sandbox_专门给_AI_Agent_用的隔离环"
source: "https://x.com/ohxiyu/status/2027434771878645908"
author:
  - "[[@xiyu]]"
published: 2026-02-28
created: 2026-02-28
description:
tags:
  - "x"
  - "@xiyu"
  - "agent"
  - "prompt"
---

# xiyu Docker 出了个新东西叫 Sandbox，专门给 AI Agent 用的隔离环

**xiyu**

Docker 出了个新东西叫 Sandbox，专门给 AI Agent 用的隔离环境。 核心卖点：API Key 通过网络代理注入，Agent 本身拿不到密钥。即使被 prompt injection 骗了执行 curl 泄密，key 也是空的。 如果你是单人本地用，Agent 的 prompt 都是自己写的，这等于给自家厨房装银行金库的门。 Sandbox 真正有价值的场景：跑第三方插件/Skill、部署到公网 VPS、给团队共享但不想暴露 Key。 本质上解决的是信任边界问题——你不完全信任 Agent 时才需要。

* * *

### 热门回复

**@莊生夢蝶** ♥ 6 · 💬 1

软件业界永远在做一件事，在前后端的中间加塞。

**@Yunfan** ♥ 1 · 💬 0

那不是弄个本地router也行

**@Ursorcen** ♥ 0 · 💬 0

不如这个 https:// docs.veilnet.app/devop/service- mesh/docker … API key自动转网络层micro segmentation ，后量子签名数据包，除了第一次启动要从IDP pull JWT，以后完全不会再用JWT，不需要像你这样还要把JWT给docker，而且支持甚至k8s 和 docker混连