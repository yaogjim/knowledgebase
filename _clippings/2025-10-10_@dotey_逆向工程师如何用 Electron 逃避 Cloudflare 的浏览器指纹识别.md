---
title: "逆向工程师如何用 Electron 逃避 Cloudflare 的浏览器指纹识别"
source: "https://x.com/dotey/status/1976308424381001927"
author:
  - "[[@dotey]]"
published: 2025-10-10
created: 2025-10-10
description:
tags:
  - "@dotey #逆向工程 #浏览器指纹识别 #Electron #Cloudflare"
---
**宝玉** @dotey 2025-10-06

这篇《我在为逆向工程师打造一款专属浏览器》的文章极其精彩，如果你对逆向工程有兴趣非常推荐。  
  
背景知识是现在很多大网站都会借助一种 fingerprinting 的技术来唯一识别一个用户，不管你怎么换匿名模式或者换浏览器，都知道你是同一台电脑使用。  
  
原理是基于浏览器画布Canvas API，在你看不见的位置在一个 <canvas> 画一张图，然后调用 toDataURL()（或读取像素数据），利用不同 GPU 之间微小的渲染差异生成的哈希值来给你打上指纹。通过将 Canvas 哈希与其他信号（如用户代理、安装的字体等）关联起来，追踪器可以构建一个相当稳健的指纹。  
  
对于逆向工作来说，监视并选择性地伪造这类调用非常有用。作者就是介绍了怎么一步步去监控和伪造 Canvas API 中的 toDataURL 函数。  
  
JavaScript 本身是很容易修改系统原生 API 的，比如我之前介绍过的跟踪 Claude Code 数据传送的 Claude Trace，就是修改了 JavaScript 的 fetch 函数，直接拿到了所有 Claude Code 的请求。  
  
作者第一个想到的办法是通过浏览器扩展，在网页加载时就加载它的注入脚本，但是没有成功（虽然后来评论有人指出是可以做到的）  
  
然后作者想到另一个办法就是用 Electron 打造一个浏览器，由于 Electron 可以比扩展程序有更高的对网页操作的优先级和权限，所以它的方法被验证是可行的，并且有一个 electron-browser-shell 开源程序可以直接实现一个浏览器套壳应用，省了很多额外的基于 Electron 开发浏览器套壳的工作。  
  
这个方法在Tiktok等各个网站都成功了，不过最终在Cloudflare上栽了跟头，不得不说Cloudflare在反逆向方面是真的牛，各种手段，我其实以前也尝试过，早放弃了。  
  
不过作者显然不是一般人，他首先发现Cloudflare 在一个沙盒化的 iframe 里渲染 Canvas，而这个 iframe 又藏在一个封闭的 Shadow DOM (一种将 DOM 封装起来，与主文档隔离的技术) 中。这个 iframe 是一个 OOPIF (out-of-process iframe)，也就是跨进程 iframe。它运行在一个不同的渲染进程里，所以页面级的脚本（以及我们注入的钩子）根本无法在那里运行，因此，也就没有日志了。  
  
找到原因后，作者通过一个底层 API，成功在 iframe 中注入了它的逆向脚本。  
  
但这还没完，Cloudflare 早就预判了会有人通过篡改系统 API 来逆向，在 JavaScript 中，函数包含一个 toString 方法，如果你篡改了系统函数，返回的结果是不一样的。  
  
作者没有放弃，又找到个办法，就是连 toString 都一起篡改了，但由于需要打补丁的 toString 方法是在太多（基本上每个系统函数都可能会被检测），而且还可能由于补丁太多还导致了其他问题。  
  
最后作者来了终极大招，重新编译 Electron 源码，魔改 Chromium！  
  
在浏览器内部调用 Canvas 的 方法时，触发一个自定义的 toDataURLCalled 方法，在 Electron 中直接获取，就不需要通过 JS 去注入了，既然 JS 系统代码没有被篡改，那么 Cloudflare 也不会认为代码有问题。所以也成功搞定了 Cloudflare。  
  
整个过程还是很精彩，推荐看看！

> 2025-10-06
> 
> i'm building a web browser for reverse engineers!
> 
> \* identify calls to common fingerprinting APIs
> 
> \* decode/decrypt known data collector payloads
> 
> \* override / hook things without leaving a trace
> 
> \* detect obfuscated scripts & deobfuscate
> 
> \+ more

---

**宝玉** @dotey [2025-10-09](https://x.com/dotey/status/1976311298515497078)

用来识别浏览器指纹画的图

图1：Tiktok

图2: Cloudflare

还挺抽象的

![Image](https://pbs.twimg.com/media/G21EW0aWEAAY_Nl?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G21EiQYWAAALMRA?format=png&name=large)

---

**宝玉** @dotey [2025-10-09](https://x.com/dotey/status/1976313184920404470)

Claude Trace

> 2025-06-04
> 
> 如果你使用 ClaudeCode，推荐试试claude-trace，它可以记录所有 claudecode 的请求日志，包括 prompt，所有内容会保存在一个 html 文件中，方便查看。它的原理很巧妙，就是自己先启动过，然后注入修改 nodejs 的 global.fetch API，然后再通过它启动 ClaudeCode，这样后续 ClaudeCode x.com/badlogicgames/…
