---
title: "2026-01-27_idoubicc_复盘一下我vibe_coding_一周_开发WorkAny_的过程_很有意思_1_上周三在"
source: "https://x.com/idoubicc/status/2014963595554304105"
author:
  - "[[@idoubicc]]"
published: 2026-01-27
created: 2026-01-27
description:
tags:
  - "x"
  - "@idoubicc"
  - "cc"
  - "https"
---

# 复盘一下我vibe coding 一周，开发WorkAny 的过程，很有意思。😂 1. 上周三在

**idoubi** @idoubicc 2026-01-23

复盘一下我vibe coding 一周，开发WorkAny 的过程，很有意思。😂

1\. 上周三在香港办卡，临时起意想做个桌面 Agent 项目，对标 cowork，晚上回到广州开始写代码

2\. 初期目标是快速发布，没时间去研究哪个 Agent 框架好用了，看很多人在用 claude agent sdk，先用这个吧

3\. 第一时间想到用 tauri，喜欢小而美，总觉得 electron 很重，不想用

4\. 不想自己写代码了，决定让 claude code 来写。之前的 claude 账号都被封了，用不上原版 cc，装了个 cc-switch，接上 OpenRouter 的 API 开始写

5\. 截了个 chatbot 的交互截图，让 cc 参考着先把基本的对话流程跑通，用 claude agent sdk，接上 OpenRouter，cc 很快写完了第一版

6\. tauri 本质是用 rust 的壳子套了个前端界面，不熟悉 rust，让 cc 用 hono 写API，rust 只做壳子，不做业务功能。API 作为 sidecar 打包进 app

7\. 让 cc 在 API 引入 sqlite 实现本地存储，持久化任务数据，创建本地工作目录，保存任务输出文件

8\. 写了半天，看 OpenRouter 消耗了 110 刀，有点肉疼。买了个美国住宅 ip，付费上了原版 claude pro

9\. 截了个 Manus 的任务详情图，让 cc 参考写完工具调用的逻辑，中间是 chatbot 对话，右边用一个虚拟计算机的容器展示输入输出

10\. 让 cc 接入 shadcn/ui，把样式做得好看一点，支持切换皮肤

11\. 又写了一天，关键时候 claude pro 限频了，很影响心情，补差价上了 claude max 顶配版

12\. 让 cc 把自定义模型配置，mcp、skills 调用的逻辑都实现了，跑了几个生成 PPT、Excel、Doc、 网页的 case，效果不错

13\. 让 cc 把输出文件夹和中间过程的 artifacts 都在右边展示出来，写了个 artifact preview 容器，渲染各种类型的文件，可视化预览

14\. 有些任务需要跑脚本完成，考虑到用户电脑可能没装代码运行环境，让 cc 引入 sandbox 来运行代码

15\. 考虑到扩展性，需要支持不同类型的 Agent runtime 和 sandbox，让 cc 写了两个抽象类，统一接口调用。Agent runtime 支持 claude code、codex、deepagents，sandbox 支持 boxlite、codex-sandbox、claude-sandbox

16\. 觉得 cc 写的代码有点乱，让 cc 引入 eslint 和 prettier 做了下格式化，把逻辑太多的文件做模块化拆分。再参考 ShipAny 的目录结构，调整了一下项目结构

17\. 让 cc 写打包脚本，构建不同操作系统的安装包。把安装包发给一些朋友，开始内测了。根据内测用户的反馈，再让 cc 继续优化逻辑，解决问题，迭代功能

18\. 有些用户电脑没装 node，没有 claude code，安装软件后跑不起来，让 cc 在构建脚本支持 flag 参数，把 node 和 cc 作为 sidecar 打包进 app，让用户能够开箱即用

19\. Mac 用户安装 app 后提示文件损坏或有安全提示，让 cc 在构建脚本里面加上签名处理，用我的 Apple 开发者账户对打包的 Mac app 做签名

20\. node 和 cc 都打包进 app 的版本，安装包 100 多 m，有点重。让 cc 在构建脚本实现默认不打包，在用户启动 app 的时候引导安装 node 和 cc，精简版安装包才 20 多 m，小巧精致

21\. app 基本功能实现得差不多了，让 cc 在 ShipAny 模板基础上写一个 WorkAny 的官网，放上演示图，部署上线

22\. WorkAny 开源发布，MVP 版本上线，用户拉源码本地构建，配个 API 直接用

23\. 让 cc 写了个 github 构建脚本，在代码推送到 main 分支时，自动触发 github action 构建，一次性打包 Windows、Linux、Mac 三大平台的安装包，自动发布到 release，用户无需自行构建了

24\. 根据用户的反馈，问题丢给 cc 去修，想到什么新功能也告诉 cc 加上，自己只做测试，不写代码，看都不看一眼。🌚

\------

几点感悟：

1\. 第一次尝试全自动驾驶 vibe coding 做项目，爽感非常强烈，WorkAny 的代码 100% 由 cc 老弟完成，我只负责指挥，日常开三个窗口，让三个 cc 老弟同时干活，效率拉满

2\. AI 时代技术平权，人人都是建筑师，理解用户需求、好的产品 sense 和审美是做出好产品的关键

3\. 技术广度和全局视野是最大的优势，可以精准提需求，指哪打哪，遇到问题能快速定位，防止 AI 走偏失控

4\. 以前总觉得手洗的衣服比洗衣机洗的干净，现在可以放心交给洗衣机了，又干净又快，能穿就行

5\. 优秀的程序员不会被 AI 淘汰，法拉利老了还是法拉利。🌝

> 2026-01-23
> 
> 我的桌面 Agent 产品 WorkAny 开源了。
> 
> 主要特性：
> 
> 1\. 以 Claude Code 为 Agent 运行时，可以完成各类任务
> 
> 2\. 以 Codex 为运行沙盒，可以在隔离环境执行脚本
> 
> 3\. 支持整理文件、生成网站、生成 PPT / Excel / Word 等日常办公任务
> 
> 4\. 支持 MCP / Agent Skills，可玩性高
> 
> 5\. 支持自定义模型，可以接入
> 
> ![Image](https://pbs.twimg.com/media/G_aWoB0bAAEXBoz?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G_VnLGmbAAI0Ap7?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G_VnNc3aQAAwDw6?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G_VnQQ6bwAAx83m?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G_VnVAVWQAAJGDs?format=jpg&name=large)

* * *

**aries\_warrior\_flamenco** @Aries\_warrior\_f [2026-01-24](https://x.com/Aries_warrior_f/status/2014970075561001186)

很赞，你真的很棒！另外想请教一下，就是虽然告诉AI让他有一个参考对象，但是其实这款产品相对而言的复杂度也是比较高的了，怎么把控它在开发中不跑偏呢？虽然网上有很多的Skills教程，但是实际使用应该又是另外一码事

* * *

**idoubi** @idoubicc [2026-01-24](https://x.com/idoubicc/status/2014986409619419444)

不要想着一步到位，模块化实现，一步步来。

* * *

**ZeroNode** @y45871296 [2026-01-25](https://x.com/y45871296/status/2015267079289733315)

感觉技术广度的价值被重新定义了

现在最值钱的是能精准描述问题、防止AI跑偏的能力

懂得提需求比会写代码重要太多了

* * *

**Versun** @VersunPan [2026-01-24](https://x.com/VersunPan/status/2014966960120078562)

羡慕用openrouter接cc的人，好奇账单多少，应该有上千吧🤤

* * *

**Eternalfate** @Eternalfate\_\_ [2026-01-24](https://x.com/Eternalfate__/status/2015045512156807565)

日常开三个窗口，让三个 cc 老弟同时干活。

不会串吗？期待能分享一下多窗口的工作流程

* * *

**toprrr** @toprrr69087 [2026-01-25](https://x.com/toprrr69087/status/2015218625536577661)

美国住宅IP用的哪个渠道购买的

* * *

**小鳄鱼** @jeff\_run\_faster [2026-01-24](https://x.com/jeff_run_faster/status/2014973980785180988)

@grok 这个apo是做什么用的？实现原理？

* * *

**GlowJames 追光** @jameszz343698 [2026-01-24](https://x.com/jameszz343698/status/2015007622697734408)

现在砸点小钱就可以快速出可用产品，我愿意给他起名：产品工程师

* * *

**Zephyr** @Zephyr0715 [2026-01-25](https://x.com/Zephyr0715/status/2015265204767236365)

我做了四个月 底层用的langgraph，现在四不像，感觉智能体能力吧 L2 水平，加了A2A,MCP,MEMORY, 反正干活的效果就是感觉很次🙃

* * *

**王归鸿Vince** @wangvince666 [2026-01-24](https://x.com/wangvince666/status/2014970290464555057)

牛的 boxlite都能被你发现 不愧是法拉利