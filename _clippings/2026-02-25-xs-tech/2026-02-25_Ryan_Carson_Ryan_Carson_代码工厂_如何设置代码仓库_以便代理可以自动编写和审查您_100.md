---
title: "2026-02-25_Ryan_Carson_Ryan_Carson_代码工厂_如何设置代码仓库_以便代理可以自动编写和审查您_100"
source: "https://x.com/ryancarson/status/2023452909883609111"
author:
  - "[[@Ryan Carson]]"
published: 2026-02-25
created: 2026-02-25
description:
tags:
  - "x"
  - "@Ryan Carson"
  - "npm"
  - "https"
---

# Ryan Carson # 代码工厂：如何设置代码仓库，以便代理可以自动编写和审查您 100

**Ryan Carson**

# 代码工厂：如何设置代码仓库，以便代理可以自动编写和审查您 100% 的代码

## 

目标

你只需要一个循环：

1.  编码代理编写代码
 
2.  该代码库在合并前会强制执行风险感知检查。
 
3.  代码审查代理验证 PR
 
4.  证据（测试+浏览器+审核）可由机器验证
 
5.  研究结果转化为可重复发生的安全带案例。
 

具体的审核代理可以是

[@greptile](https://x.com/@greptile)

，

[@coderabbitai](https://x.com/@coderabbitai)

可以是 CodeQL + 策略逻辑、自定义 LLM 审核或其他服务。控制平面模式保持不变。

我从这篇很有帮助的博客文章中获得了灵感，作者是

[@\_lopopolo](https://x.com/@_lopopolo)

[

![](https://pbs.twimg.com/profile_images/2016785876261679104/LJFhaQ17_x96.jpg)

](/ryancarson)

Ryan Carson

@ryancarson

·

[Feb 15](/ryancarson/status/2022716244361683236)

我一直在用 Codex（超高难度）搭建我们的 Harness Engineering 代码库。 目标是确保 Codex 正确无误，并审查 100% 的代码。 越来越接近目标了。

[

![](https://pbs.twimg.com/card_img/2025465725196902400/OnnMicwZ?format=jpg&name=medium)

驾驭工程：在以代理为先的世界中利用 Codex


](https://t.co/synYBpsGYA)

[

来自 openai.com](https://t.co/synYBpsGYA)

30

21

427

[

28K


](/ryancarson/status/2022716244361683236/analytics)

## 

高层流

[

![Image](https://pbs.twimg.com/media/HBS8fc6bkAAMWs8?format=png&name=4096x4096)


](/ryancarson/article/2023452909883609111/media/2023449381119430656)

## 

1）保留一份机器可读合同

您的合同应明确规定：

- 按路径划分的风险等级
 
- 各层级所需检查
 
- 控制平面变更的文档漂移规则
 
- UI/关键流量的证据要求
 

json

```json
{
  "version": "1",
  "riskTierRules": {
 "high": [
 "app/api/legal-chat/**",
 "lib/tools/**",
 "db/schema.ts"
 ],
 "low": ["**"]
  },
  "mergePolicy": {
 "high": {
 "requiredChecks": [
 "risk-policy-gate",
 "harness-smoke",
 "Browser Evidence",
 "CI Pipeline"
 ]
 },
 "low": {
 "requiredChecks": ["risk-policy-gate", "CI Pipeline"]
 }
  }
}
```

重要性：它消除了歧义，防止了脚本、工作流文件和策略文档之间出现无声的偏差。

## 

2) 登机口预检（在昂贵的 CI 之前）

可靠的模式是：

1.  首先运行 \`risk-policy-gate\`
 
2.  验证确定性策略 + 审查代理状态
 
3.  只有这样才能启动 \`test/build/security\` 扇出作业
 

这样可以避免将 CI 时间浪费在那些因政策或未解决的审查结果而受阻的 PR 负责人身上。

typescript

```typescript
const requiredChecks = computeRequiredChecks(changedFiles, riskTier);
await assertDocsDriftRules(changedFiles);
await assertRequiredChecksSuccessful(requiredChecks);

if (needsCodeReviewAgent(changedFiles, riskTier)) {
  await waitForCodeReviewCompletion({ headSha, timeoutMinutes: 20 });
  await assertNoActionableFindingsForHead(headSha);
}
```

## 

3）执行现任负责人 SHA 纪律

这是从真实的公关流程中获得的最重要的实践经验。

只有当审查状态与当前 PR 主提交匹配时，才将其视为有效：

- 等待对 \`headSha\` 进行审查检查
 
- 忽略与旧 SHA 关联的过时摘要评论
 
- 如果最近一次审核运行失败或超时，则失败。
 
- 每次同步/推送后都需要重新运行。
 
- 通过在同一节点上重新运行策略门来清除过期的门故障。
 

如果跳过此步骤，您可以使用过时的“干净”证据合并 PR。

## 

4) 使用带有 SHA 去重的单个重运行注释写入器

当多个工作流可以请求重新运行时，就会出现重复的机器人评论和竞态条件。

使用一个工作流作为规范的重新运行请求者，并按标记 + \`sha: 进行去重：<head> \`。

typescript

```typescript
const marker = '<!-- review-agent-auto-rerun -->';
const trigger = `sha:${headSha}`;
const alreadyRequested = comments.some((c) =>
  c.body.includes(marker) && c.body.includes(trigger),
);

if (!alreadyRequested) {
  postComment(`${marker}\n@review-agent please re-review\n${trigger}`);
}
```

## 

5）添加自动化修复循环（可选，效果显著）

如果审查结果可执行，则触发编码代理执行以下操作：

1.  阅读评论背景
 
2.  补丁代码
 
3.  运行重点本地验证
 
4.  将修复提交推送到同一 PR 分支
 

然后让 PR 同步触发正常的重新运行路径。保持此过程的确定性：

- 针式模型 + 可复现性工作
 
- 跳过与当前标题不符的过时评论
 
- 绝不绕过政策关卡
 

## 

6) 仅在彻底重新运行后自动解决仅限机器人发起的线程

提升生活质量的有效措施：

- 在干净的电流头重新运行后
 
- 自动解决所有评论均来自评论机器人的未解决主题帖。
 
- 永远不要自动解决人工参与的讨论串
 

然后重新运行策略门控，以便所需对话解决方案反映新的状态。

## 

7）将浏览器证据作为一流证据保存。

对于用户界面或用户流程的更改，需要在持续集成 (CI) 中提供证据清单和断言（而不仅仅是 PR 文本中的屏幕截图）：

- 所需流程存在
 
- 使用了预期的入口点
 
- 已登录流程中存在预期的帐户身份
 
- 文物新鲜有效
 

狂欢

```bash
npm run harness:ui:capture-browser-evidence
npm run harness:ui:verify-browser-evidence
```

## 

8) 利用安全带间隙环保存事故记忆

纯文本

```plaintext
production regression -> harness gap issue -> case added -> SLA tracked
```

这样可以避免修复变成一次性补丁，并提高长期覆盖率。

## 

9）我们在 PR 中运行此程序学到了什么

最重要的教训是：

1.  确定性顺序很重要：预检登机口必须在 CI 扇出之前完成。
 
2.  当前头部 SHA 匹配是不可协商的。
 
3.  重审请求需要一位权威撰稿人。
 
4.  审查摘要解析应将漏洞描述和置信度较低的摘要视为可操作内容。
 
5.  自动解决仅限机器人参与的讨论串可以减少摩擦，但前提是必须有清晰的当前讨论串证据。
 
6.  如果防护措施严格执行，补救措施可以显著缩短循环时间。
 

## 

10）通用模式与单一实现

通用模式术语：

- \`代码审查代理\`
 
- \`修复剂\`
 
- 风险策略门控
 

一个具体的实施方案（我们）：

- 代码审查代理：Greptile
 
- 补救措施：食品法典行动
 
- 规范的重新运行工作流程：\`greptile-rerun.yml\`
 
- 旧线程清理工作流程：\`greptile-auto-resolve-threads.yml\`
 
- 预检策略工作流程：\`risk-policy-gate.yml\`
 

如果使用不同的审阅者，请保持相同的控制平面语义并交换集成点。

## 

有用的命令集

狂欢

```bash
npm run typecheck
npm test
npm run build:ci
npm run harness:legal-chat:smoke
npm run harness:ui:pre-pr
npm run harness:risk-tier
npm run harness:weekly-metrics
```

## 

最终图案待复制

1.  将风险和合并政策合并到一个合同中。
 
2.  在昂贵的 CI 之前，强制执行登机前登机口检查。
 
3.  要求当前 head SHA 处于干净的代码审查代理状态。
 
4.  如果发现问题，则在分支内进行修复，然后确定性地重新运行。
 
5.  清理后重新运行，仅自动解决机器人提交的过期主题。
 
6.  要求提供浏览器端的用户界面/流程变更证明。
 
7.  将事故转化为安全带案例和跟踪回路 SLO。
 

这样就形成了一个存储库，代理商可以在其中实现、验证并按照确定性、可审计的标准进行审查。