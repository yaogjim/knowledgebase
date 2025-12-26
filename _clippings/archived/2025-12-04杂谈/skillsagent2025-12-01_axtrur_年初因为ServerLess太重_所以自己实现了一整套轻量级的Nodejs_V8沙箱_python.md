---
title: "2025-12-01_axtrur_年初因为ServerLess太重_所以自己实现了一整套轻量级的Nodejs_V8沙箱_python"
source: "https://x.com/axtrur/status/1941873059859992633"
author:
  - "[[@axtrur]]"
published: 2025-12-01
created: 2025-12-01
description:
tags:
  - "x"
  - "@axtrur"
  - "2025-07-06"
  - "https"
status: "inbox"
importance: 2
effort: 2
review_level: 0
review_next: "2025-12-10"
review_interval: null
review_count: 0
decision: null
topics: []
links_out: []
summary: ""
pov: ""
actions: []
---

# 年初因为ServerLess太重，所以自己实现了一整套轻量级的Nodejs（V8沙箱），python

**axtrur** @axtrur 2025-07-06

年初因为ServerLess太重，所以自己实现了一整套轻量级的Nodejs（V8沙箱），python（原生服务环境），Golang（yaegi解析器），目的是动态执行一些人为生成或者AI生成的代码，但是这种方案需要内置一些常用的第三方库，甚至Yaegi还得实现一个内存文件系统做目录依赖管理。今天看了下microsandbox的实现，感觉算是介于Faas跟ServerLess的中间级别的轻量实现了，支持OCI，感觉完全可行啊，准备搞Code Use的团队可以研究一下

> 2025-07-06
> 
> microsandbox ，一个开源、可自托管部署的代码执行沙箱工具，用于安全运行不受信任的用户或AI生成代码。
> 
> 采用硬件级microVM隔离，启动时间约200ms。提供Python、JavaScript、Rust等多语言SDK，支持OCI容器镜像，内置MCP协议支持。适用于AI代码执行、开发环境隔离等场景。
> 
> ![Image](https://pbs.twimg.com/media/GvI9cXuWAAEJyuF?format=jpg&name=large)

* * *

**面包** @himself\_65 [2025-07-06](https://x.com/himself_65/status/1941988902258270467)

好像已经有很多实现了吧，比如vercel sandbox和cloudflare code sandboxes

* * *

**axtrur** @axtrur [2025-07-06](https://x.com/axtrur/status/1942010381427450367)

是的，差不多都是轻量虚拟机的实现，microsandbox，e2b开源可自托管，e2b，vercel sandbox似乎是firecracker，microsandbox是更轻量的libkrun，讲道理如果想成为沙箱服务提供商，确实可以看一下