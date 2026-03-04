---
title: "2026-03-03_李不凯正在研究_李不凯正在研究_根据最新的学习心得_给_awesome_agent_skills_repo"
source: "https://x.com/libukai/status/2028490244337914304"
author:
  - "[[@李不凯正在研究]]"
published: 2026-03-03
created: 2026-03-03
description:
tags:
  - "x"
  - "@李不凯正在研究"
  - "skill"
  - "plugin"
---

# 李不凯正在研究 根据最新的学习心得，给 awesome-agent-skills repo

**李不凯正在研究**

根据最新的学习心得，给 awesome-agent-skills repo 增加了 Marketplace 配置，把自己常用的 skills 通过 Plugin 形式共享出来了。 目前放上去的暂时只有 agent-skills-toolkit 和 vscode-extensions-toolkit 两个 Plugin。 前者是在官方 skill-creator plugin 的基础上，添加了《Claude Skill 完整构建指南》中的最佳实践形成的加强版，后续还会继续优化迭代，帮助大家更好的创建和优化自己使用的 Skill。 后者则是我在 VS Code 中几个常用扩展的配置技能，包括 API 测试用的 httpyac，进行端口管理的 port-monitor，以及通过 ssh 进行同步的 sftp。他们共同的特点都是需要根据项目实际情况进行初始化配置之后才能使用，配合这几个 Skill 效率就高多了。 至于为什么选择 Plugin 格式来做分享，主要是我想根据Anthropic 的最佳实践指南，尝试一下把 Agent/MCP/Skill/Command 这些功能都整合起来，看看是否能探索出一种可迭代且便于分发的垂直任务解决方案。 目前看起来，如果是基于 Claude Code，这应该是当下的最佳方案。

![图片](https://pbs.twimg.com/media/HCag2MsbMAABvrW?format=jpg&name=large)

> **@libukai**
> 
> 今天整完了手头的大活，终于有时间细致地把 X 上有关 Skill 的资料全部梳理了一遍，也系统性的把 awesome-agent-skills repo 更新了一轮。 这可能是全网最全面的中文 Skill 仓库了，关键是里面的内容都是我亲自验证过的，质量绝对有保障。

* * *

### 热门回复

**@Mr.Yang | 科技趋势** ♥ 0 · 💬 1

这个方向很有价值，分享类插件真正能拉开差距的是“可复用+可验证”。建议每个Skill都补两样东西：验收样例（输入/预期输出）和失败案例（常见误用），这样团队接手时能直接落地，不会停在收藏层。你会考虑给每个插件做一页ROI对比吗？

**@李不凯正在研究** ♥ 0 · 💬 1

是一个好建议，我边迭代边优化。不过我现在有一个更强烈的感受是，未来文档的意义可能真没那么大了，让 AI 读一遍原始代码再直接解读可能是更好的方案。