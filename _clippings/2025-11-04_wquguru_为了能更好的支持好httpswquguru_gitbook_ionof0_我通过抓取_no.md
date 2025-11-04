---
title: "2025-11-04_wquguru_为了能更好的支持好httpswquguru_gitbook_ionof0_我通过抓取_no"
source: "https://x.com/wquguru/status/1985338399717490993"
author:
  - "[[@wquguru]]"
published: 2025-11-04
created: 2025-11-04
description:
tags:
  - "@wquguru"
  - "@nofx"
  - "@Web3Tinkle"
  - "//x"
  - "https"
  - "需求度"
  - "2025-11-04"
  - "**wquguru**"
  - "x.com"
---

**WquGuru** @wquguru 2025-11-02

为了能更好的支持好https://wquguru.gitbook.io/nof0，我通过抓取 @nofx\_ai 的 tg 群最近3天数万条历史聊天

导入某个工具（YxxMxxx），发现对于用户反馈与痛点深度分析还挺不错的，在这里分享一下，详细分析文档链接贴在最后，既可以作为 @nofx\_ai 的用户手册、也可以作为开发路线图的蓝本

（nofx的创始人 @Web3Tinkle 是一位执行力非常强的技术人和领导者，我们曾深度交流过nof1的提示词的实现🫱https://x.com/wquguru/status/1983197405320491366…）

高频的20个问题中，排在前几的有：币安API调用失败、前端端口无法访问、保证金不足问题、AI学习数据加载失败、子账户杠杆限制、持仓模式设置失败

用户痛点：部署比较困难，尤其对于新用户/非技术用户；Docker部署虽然简化了流程，但仍存在各种问题；用户不了解资金在哪个账户、以及不同账户类型的限制；高频交易导致手续费吞噬利润（"昨天手续费10.8u，89比交易"）；风控状态不持久化（"先改进风控吧，有很大缺陷，不建议跑实盘"）

社区最关注的盈利问题也有很多讨论，主要是关于盈利困难的部分，可作为优化提示词和系统的重点方向：

\- AI策略问题：只做空不做多、缺少移动止盈、频繁交易导致手续费过高

\- 市场适应问题：AI缺少市场情绪、新闻、链上数据等信息；用户无法充分回测策略，只能实盘试错

\- 配置复杂：配置参数过多；提示词对策略影响巨大，但调优需要专业知识；不同交易所配置方式不同，增加学习成本

更多成功案例、失败案例、用户建议、社区氛围，参考🫱https://x.com/wquguru/status/1983197405320491366…

> 2025-11-02
> 
> http://nof1.ai 仿盘阶段3
> 
> 过去几天市场经历了一波回调，即便是表现最好的 DeepSeek v3.1 和 Qwen3 Max，也遭遇了高达 30%-40% 的回撤，夏普率更是惨淡，分别降至 0.014 和 -0.236
> 
> 回到 nof0，在连续多天开发下，交易引擎已基本完工，目前已涵盖的核心特性包括：
> 
> \-
> 
> ![Screenshots of a web interface for nof0 open-source AI trading arena, displaying sections like introduction in Chinese, features list including AI strategy optimization and backtesting, and a grid layout with project details and navigation panels.](https://pbs.twimg.com/media/G41SlKRakAAWgq5?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/G4w2WsybcAE21eP?format=jpg&name=large)

* * *

**WquGuru** @wquguru [2025-11-03](https://x.com/wquguru/status/1985339021099479184)

高优先级需求：

1\. 移动止盈止损 (需求度: ★★★★★)

2\. 一键部署方案 (需求度: ★★★★★)

3\. 风控系统增强 (需求度: ★★★★★)

4\. 提示词优化工具 (需求度: ★★★★☆)

5\. 市场数据增强 (需求度: ★★★★☆)

中优先级需求：

6\. 多账户管理 (需求度: ★★★★☆)

7\. 策略回测系统 (需求度: ★★★★☆)

8\. 通知系统 (需求度: ★★★☆☆)

9\. 移动端支持 (需求度: ★★★☆☆)

10\. 社区策略市场 (需求度: ★★★☆☆)

低优先级需求

11\. 多语言界面 (需求度: ★★☆☆☆)

12\. 数据导出功能 (需求度: ★★☆☆☆)

13\. 社交交易功能 (需求度: ★☆☆☆☆)

* * *

**WquGuru** @wquguru [2025-11-03](https://x.com/wquguru/status/1985340225581924633)

最后的链接贴错了，应该是🫱https://youmind.site/Ynr9J51LFyjzSj
