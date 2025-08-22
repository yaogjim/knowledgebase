---
title: "microsandbox：开源、可自托管部署的代码执行沙箱工具"
source: "https://x.com/ProgramerJohann/status/1941681958003802166"
author:
  - "[[@ProgramerJohann]]"
created: 2025-07-07
description:
tags:
  - "@ProgramerJohann #代码执行 #沙箱 #开源 #安全"
---
**johann.GPT** @ProgramerJohann [2025-07-06](https://x.com/ProgramerJohann/status/1941681958003802166)

microsandbox ，一个开源、可自托管部署的代码执行沙箱工具，用于安全运行不受信任的用户或AI生成代码。

采用硬件级microVM隔离，启动时间约200ms。提供Python、JavaScript、Rust等多语言SDK，支持OCI容器镜像，内置MCP协议支持。适用于AI代码执行、开发环境隔离等场景。

![Image](https://pbs.twimg.com/media/GvI9cXuWAAEJyuF?format=jpg&name=large)

---

**johann.GPT** @ProgramerJohann [2025-07-06](https://x.com/ProgramerJohann/status/1941681990824231071)

---

**wang** @wangzhr4 [2025-07-06](https://x.com/wangzhr4/status/1941803297209462990)

支持 OCI ，非常好。Kubernetes 生态可以走起来了。看了源码和文档，真的很牛，有望平替 @e2b

---

**johann.GPT** @ProgramerJohann [2025-07-06](https://x.com/ProgramerJohann/status/1941803425022550173)

是的！ 支持OCI就很好。

---

**wang** @wangzhr4 [2025-07-06](https://x.com/wangzhr4/status/1941804220027666504)

目前与 e2b 相比，主要是没做 infra 这一层。baremetal infra，可以考虑公有云的 API 接口，或者用 Terraform 来实现。在公有云上拉起 Kubernetes + baremetal 集群，就可以了。

我看这个方案用的是 libkrun，稍微小众一些，还可以考虑 firecracker-microvm.

---

**johann.GPT** @ProgramerJohann [2025-07-06](https://x.com/ProgramerJohann/status/1941804652309467494)

e2b 应该就是 firecracker

---

**wang** @wangzhr4 [2025-07-06](https://x.com/wangzhr4/status/1941805533692047839)

Firecracker 我觉得主要用过于轻量化了，为了安全和快启动，在虚拟化层精减的太厉害，原生不支持 OCI，需要 fc-containerd 一层中间层。自己的编排层 ignite 没做起来。

---

**johann.GPT** @ProgramerJohann [2025-07-06](https://x.com/ProgramerJohann/status/1941806557370667464)

专业啊哥！ 我一直在找一个完整开源的e2b，不知道有没有搞头！

---

**wang** @wangzhr4 [2025-07-06](https://x.com/wangzhr4/status/1941808227177631991)

我看上去，这个项目如果要自用，找服务器托管一下后端，前端 SDK 放本地，应该就可以了。

但是要想平替 E2B，并且要实现商业化服务，工作主要在编排层和用户接入层。包括用户账号，资源编排，与 K8s 对接。以及完整的前端。

---

**wang** @wangzhr4 [2025-07-06](https://x.com/wangzhr4/status/1941808499635417096)

\*完整的网页前端\*。

---

**axtrur** @axtrur [2025-07-06](https://x.com/axtrur/status/1941873373199646756)

看着不错啊，star了

> 2025-07-06
> 
> 年初因为ServerLess太重，所以自己实现了一整套轻量级的Nodejs（V8沙箱），python（原生服务环境），Golang（yaegi解析器），目的是动态执行一些人为生成或者AI生成的代码，但是这种方案需要内置一些常用的第三方库，甚至Yaegi还得实现一个内存文件系统做目录依赖管理。今天看了下microsandbox的实现， x.com/ProgramerJohan…
