---
title: "2026-06-16_verysmallwoods_substack_com_腾讯开源_TencentDB_Agent_Memory_给_OpenClaw_和_Hermes_Ag"
source: "https://verysmallwoods.substack.com/p/tencentdb-agent-memory-openclaw-hermes?r=1vcnoc&utm_campaign=post&utm_medium=web&triedRedirect=true"
author:
  - "[[@tencentdb]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "verysmallwoods"
  - "@tencentdb"
  - "null"
  - "https"
---

# 腾讯开源 TencentDB Agent Memory：给 OpenClaw 和 Hermes Agent 接上 4 层本地长期记忆，PersonaMem 准确率 48% → 76%

### 腾讯 4 月初放出 TencentDB Agent Memory，7 周攒下 4.1K stars。它的思路有点反潮流 - 不再把对话历史塞进扁平向量库，而是建一座 L0 Conversation → L1 Atom → L2 Scenario → L3 Persona 的语义金字塔；短期任务状态再用 Mermaid 符号图替代工具日志。已经支持 OpenClaw 插件和 Hermes Agent

每个用 agent 久一点的人都会有一个共同的疲劳点 - 同一个项目背景，同一套 SOP，同一种输出格式，你跟它解释了一百遍，它还是每次重开都问你「你想要什么风格」「这个项目的技术栈是什么」。

把历史扔进上下文，token 爆掉； **把历史扔进向量库，召回出一堆相关但不连续的片段** 。两个方向都不解决「让 agent 自己记住什么该问、什么不该问」这件事。

腾讯 4 月初开源的 `Tencent/TencentDB-Agent-Memory` （以下简称 TDAI）就在试着回答这个问题。7 周拿到 4.1K stars，5 月 23 日被 MarkTechPost 写了一篇深度介绍，5 月 25 日还在持续提交。和大多数 agent memory 方案比，它最不一样的一点是 - **拒绝扁平向量存储** 。

## 一个反传统的姿态：记忆不是向量堆，是金字塔

TDAI 的 README 一开头就把这条立场摆出来：

> Traditional memory systems shred data into fragments and dump them into a flat vector store. Recall degenerates into a blind search across disconnected fragments, with no macro-level guidance.

翻译过来 - 传统记忆方案把数据剁成碎片扔进扁平向量库，召回变成在断片之间瞎找，没有宏观指引。

它的替代方案有两根支柱：

- **记忆分层（Memory Layering）** \- 长期记忆做成自下而上的语义金字塔，下层保留证据，上层保留结构
 
- **符号化记忆（Symbolic Memory）** \- 短期任务状态压成 Mermaid 图，工具日志原文卸载到外部文件
 

下层证据 + 上层结构这套思路本身不新，但 TDAI 把它彻底落到代码里，并且坚持「白盒可调试」- 每一层的中间产物都是人类可读的 Markdown 或 JSONL，不是黑箱向量。

## 长期记忆的 4 层金字塔：L0 → L3

这是 TDAI 最容易被抄走、也最值得理解的设计。一条对话进来之后，它会逐层往上蒸馏：

[

![]({"src":"https://substack-post-media.s3.amazonaws.com/public/images/faacfe05-07a7-46cc-bf25-f3c2dc76eac3_1400x400.png","srcNoWatermark":null,"fullscreen":null,"imageSize":null,"height":400,"width":1400,"resizeWidth":null,"bytes":59475,"alt":null,"title":null,"type":"image/png","href":null,"belowTheFold":true,"topImage":false,"internalRedirect":"https://verysmallwoods.substack.com/i/199236089?img=https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffaacfe05-07a7-46cc-bf25-f3c2dc76eac3_1400x400.png","isProcessing":false,"align":null,"offset":false})

](https://substackcdn.com/image/fetch/$s_!AuGC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffaacfe05-07a7-46cc-bf25-f3c2dc76eac3_1400x400.png)

实际生效路径是反向的 - **答问题先看上层，缺细节再向下钻** ：

[

![]({"src":"https://substack-post-media.s3.amazonaws.com/public/images/8caa1266-b19a-4eac-9bf2-219805ac160c_1400x400.png","srcNoWatermark":null,"fullscreen":null,"imageSize":null,"height":400,"width":1400,"resizeWidth":null,"bytes":49630,"alt":null,"title":null,"type":"image/png","href":null,"belowTheFold":true,"topImage":false,"internalRedirect":"https://verysmallwoods.substack.com/i/199236089?img=https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8caa1266-b19a-4eac-9bf2-219805ac160c_1400x400.png","isProcessing":false,"align":null,"offset":false})

](https://substackcdn.com/image/fetch/$s_!KWxh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8caa1266-b19a-4eac-9bf2-219805ac160c_1400x400.png)

整条钻取链 README 里有一个清晰的说法 - **「顶层符号（Persona / canvas）→ 中层索引（Scenario / jsonl）→ 底层原文（L0 Conversation / refs）」** 。这意味着：当你看到一句 “用户偏好写 Python 而不是 Go”，你能顺着 persona → 触发这条结论的几个 scenario → scenario 里抽出的 atom → atom 引用的原始对话，一层层验证。

对比之下，单纯的向量库召回出 3 条相关 chunk，然后让 LLM “summarize”，错了你不知道错在哪 - 这是 TDAI 强调白盒的原因。

Pipeline 的触发节奏在 `openclaw.plugin.json` 里：

```markup
{
  "pipeline": {
 "everyNConversations": 5, // 每 5 轮对话触发 L1 提取
 "enableWarmup": true, // 新 session: 1 轮 → 2 → 4 → ... → N
 "l1IdleTimeoutSeconds": 600, // 用户停 10 分钟也触发 L1
 "l2MinIntervalSeconds": 900 // 同 session 两次 L2 至少间隔 15 分钟
  },
  "persona": {
 "triggerEveryN": 50 // 累计 50 条新记忆生成一次 persona
  }
}
```

Warmup 这个细节挺贴心 - 新会话头几轮就触发提取，不用等攒够 5 条；之后翻倍退避到稳态。

## 短期记忆：Mermaid 图把 50 万 token 压成几百 token

长期记忆解决「跨 session 记得用户」，短期记忆解决「同一个长任务里别被工具日志撑爆 context」。

TDAI 给出的方案是把工具调用记录拆三层处理：

[

![]({"src":"https://substack-post-media.s3.amazonaws.com/public/images/c52c2ed9-a7d6-4a87-9b50-a3320562a9a0_2067x346.png","srcNoWatermark":null,"fullscreen":null,"imageSize":null,"height":244,"width":1456,"resizeWidth":null,"bytes":91357,"alt":null,"title":null,"type":"image/png","href":null,"belowTheFold":true,"topImage":false,"internalRedirect":"https://verysmallwoods.substack.com/i/199236089?img=https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc52c2ed9-a7d6-4a87-9b50-a3320562a9a0_2067x346.png","isProcessing":false,"align":null,"offset":false})

](https://substackcdn.com/image/fetch/$s_!gt6Y!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc52c2ed9-a7d6-4a87-9b50-a3320562a9a0_2067x346.png)

- 工具原始输出全量落盘（ `refs/*.md` ）- agent 看不到
 
- 中间提取出每一步的关系，编码成 Mermaid 节点图 - 每个节点带 `node_id`
 
- 只有 Mermaid canvas 注入到 context - LLM 既能解析、人也能读
 
- 哪个节点要看细节，grep `node_id` 把对应的原始文本拉回来
 

为什么是 Mermaid 而不是 JSON？官方说法是 - LLM 解析够准、人类读够省力，token 密度比 prose 和 flat JSON 都高。这点我们 0523 的 AI 早读里也提过 Claude Code 的 Thariq Shihipar 在做类似的事（用 HTML 而不是 Markdown 当输出格式）- 都是同一个方向： **给 LLM 用的中间表示，要比给人用的更紧凑** 。

短期压缩的触发阈值：

```markup
{
  "offload": {
 "enabled": true,
 "mildOffloadRatio": 0.5, // 上下文用到 50% 开始温和压缩
 "aggressiveCompressRatio": 0.85, // 用到 85% 进入激进模式
 "mmdMaxTokenRatio": 0.2 // Mermaid canvas 最多占 20% 预算
  }
}
```

## OpenClaw 集成：两行命令，零配置

[OpenClaw](https://github.com/openclaw/openclaw) 是 TDAI 的一等公民集成路径。安装就两行：

```markup
openclaw plugins install @tencentdb-agent-memory/memory-tencentdb
openclaw gateway restart
```

启用更简单：

```markup
// ~/.openclaw/openclaw.json
{
  "memory-tencentdb": {
 "enabled": true
  }
}
```

之后所有事都是 TDAI 自己做 - 对话捕获、L1 提取、L2 场景聚合、L3 画像生成、下一轮对话开始前的召回注入。默认后端是 SQLite + sqlite-vec，数据落在 `~/.openclaw/memory-tdai/` ，可以直接打开看每一层长什么样。

要开启短期 Mermaid 压缩多加一行 `offload.enabled: true` ，再跑一次 `openclaw-after-tool-call-messages.patch.sh` 把 OpenClaw 的 `after-tool-call` hook 接上即可。

## Hermes Agent 集成：Docker 一键起，Python 包 Node.js

第二条集成路径走的是 [NousResearch 的 Hermes Agent](https://github.com/NousResearch/hermes-agent) 。这条路径架构上更有意思 - TDAI 核心是 Node.js 写的，但 Hermes 是 Python 框架。怎么接？官方的答案是 **Python 进程里跑一个 Node.js sidecar** ：

[

![]({"src":"https://substack-post-media.s3.amazonaws.com/public/images/e3b75b67-ce1e-4bcf-9586-86da20175756_2135x1620.png","srcNoWatermark":null,"fullscreen":null,"imageSize":null,"height":1105,"width":1456,"resizeWidth":null,"bytes":237481,"alt":null,"title":null,"type":"image/png","href":null,"belowTheFold":true,"topImage":false,"internalRedirect":"https://verysmallwoods.substack.com/i/199236089?img=https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe3b75b67-ce1e-4bcf-9586-86da20175756_2135x1620.png","isProcessing":false,"align":null,"offset":false})

](https://substackcdn.com/image/fetch/$s_!UMH2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe3b75b67-ce1e-4bcf-9586-86da20175756_2135x1620.png)

Hermes 的生命周期 hook 映射到 Gateway endpoint：

[

![]({"src":"https://substack-post-media.s3.amazonaws.com/public/images/ce9d8b89-47e5-4155-9fca-cc1a464cff80_1400x400.png","srcNoWatermark":null,"fullscreen":null,"imageSize":null,"height":400,"width":1400,"resizeWidth":null,"bytes":47288,"alt":null,"title":null,"type":"image/png","href":null,"belowTheFold":true,"topImage":false,"internalRedirect":"https://verysmallwoods.substack.com/i/199236089?img=https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fce9d8b89-47e5-4155-9fca-cc1a464cff80_1400x400.png","isProcessing":false,"align":null,"offset":false})

](https://substackcdn.com/image/fetch/$s_!TrmD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fce9d8b89-47e5-4155-9fca-cc1a464cff80_1400x400.png)

Python provider 那一层做了几件值得抄的可靠性工程：

- **熔断器** \- 连续 5 次 Gateway 失败 → 暂停所有调用 60 秒
 
- **capture 背压** \- 最多 4 个并发 `sync_turn` 线程；第 5 个等最老的最多 5 秒再起，防止 sidecar 卡死时线程无限堆积
 
- **进程监督** \- 起 sidecar 后轮询 `/health` 30 秒；崩了自动 tail `gateway.stderr.log` 给 diagnostics
 
- **零配置自动发现** \- 在 `~/.memory-tencentdb/` 、 `~/.hermes/plugins/` 几个标准路径自动找 `server.ts`
 

落到使用上，一条 docker run 起整套：

```markup
docker run -d \
  --name hermes-memory \
  --restart unless-stopped \
  -p 8420:8420 \
  -e MODEL_API_KEY="your-api-key" \
  -e MODEL_BASE_URL="https://api.lkeap.cloud.tencent.com/v1" \
  -e MODEL_NAME="deepseek-v3.2" \
  -e MODEL_PROVIDER="custom" \
  -v hermes_data:/opt/data \
  hermes-memory
```

默认模型是腾讯云 LKE 跑的 DeepSeek-V3.2 - 近日 The Decoder 报道 DeepSeek 把 75% 折扣永久化、输出 token 比 GPT-5.5 便宜至少 34 倍。便宜模型 + 本地记忆，这套组合的运行成本可以压得很低。

## 检索引擎：BM25 + 向量 + RRF 三个一起上

agent 调 `tdai_memory_search` 的时候，TDAI 同时跑两条召回路径，然后用 RRF 融合：

```markup
// src/core/tools/memory-search.ts
const RRF_K = 60;  // 经典 RRF 论文的常数

function rrfMergeL1(...lists: MemorySearchResultItem[][]) {
  const map = new Map<string, { item: MemorySearchResultItem; rrfScore: number }>();

  for (const list of lists) {
 for (let rank = 0; rank < list.length; rank++) {
 const item = list[rank];
 const score = 1 / (RRF_K + rank + 1);
 const existing = map.get(item.id);
 if (existing) existing.rrfScore += score;
 else map.set(item.id, { item, rrfScore: score });
 }
  }
  return [...map.values()]
 .sort((a, b) => b.rrfScore - a.rrfScore)
 .map(({ item, rrfScore }) => ({ ...item, score: rrfScore }));
}
```

代码很短，三件事值得注意：

- `RRF_K = 60` 是 RRF 原论文（Cormack et al., 2009）的标准常数，不是拍脑袋
 
- 关键词检索走的是 SQLite FTS5（ `buildFtsQuery` ），向量走 sqlite-vec - **完全本地，零外部 API 依赖**
 
- 自动降级 - 没配 embedding service 时直接退回纯 FTS5；没 FTS5 退回纯向量；两个都没就空召回
 

BM25 那边支持 `zh` （jieba）和 `en` 两种分词，中英文场景都能用。

## Benchmark：长会话场景下的真实增益

README 给的数字看起来很漂亮，但有个关键约束需要先说清楚 - **这些是连续长会话的成绩，不是单轮对话** 。比如 SWE-bench 每个 session 跑 50 个连续任务，模拟真实长任务下 context 累积压力。

[

![]({"src":"https://substack-post-media.s3.amazonaws.com/public/images/f7c0279a-2bb6-4283-bee8-940d70dfdc30_1400x400.png","srcNoWatermark":null,"fullscreen":null,"imageSize":null,"height":400,"width":1400,"resizeWidth":null,"bytes":46226,"alt":null,"title":null,"type":"image/png","href":null,"belowTheFold":true,"topImage":false,"internalRedirect":"https://verysmallwoods.substack.com/i/199236089?img=https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7c0279a-2bb6-4283-bee8-940d70dfdc30_1400x400.png","isProcessing":false,"align":null,"offset":false})

](https://substackcdn.com/image/fetch/$s_!pPHf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7c0279a-2bb6-4283-bee8-940d70dfdc30_1400x400.png)

PersonaMem 上 48% → 76% 这个跳跃最值得关注 - 因为它直接测的就是 “agent 是否记得你”。WideSearch 的 token 砍 61% 也很硬 - 短期记忆这套 Mermaid 卸载方案在搜索类长任务上对成本影响最大。

SWE-bench 上 +9.93% 看起来小，但考虑到这是个高度工程化的代码 benchmark，能在 50 任务的连续 session 里把 pass rate 又往上推 6 个百分点（同时 token 砍掉 1/3），增量并不小。

## 几个 tradeoff 和适用场景

- **短会话用不上** \- 几轮就结束的 chat，pipeline 都没触发完，分层没意义
 
- **冷启动需要时间** \- 新用户没 persona，需要积累 50 条 L1 atom 才能出第一版 persona；warmup 缓解了这点但不能消除
 
- **依赖一个 LLM 做提取** \- L1 / L2 / L3 都靠 LLM 蒸馏，本地存储但 LLM 调用仍要计入成本（默认走 OpenClaw 的模型，或单独配 `llm.*` ）
 
- **目前只对接两个宿主** \- OpenClaw 和 Hermes。LangChain / LangGraph / AutoGen / Claude Code 没有官方插件，要自己写 host adapter（ `TdaiCore + HostAdapter` 解耦设计，理论上能接）
 
- **和 mem0 / Letta 不完全重叠** \- mem0（56K stars，Apache 2.0）和 Letta（23K stars，Apache 2.0）也都是开源的 agent memory 项目，但它们设计上偏 SDK / 框架，托管层（mem0 Cloud / Letta Cloud）是主要变现路径；TDAI 默认本地优先，没有官方托管服务，定位更接近「OpenClaw 生态里的开箱即用插件」
 

适用场景比较明确：

- 你有一个 **长期、多 session 跟同一个用户打交道** 的 agent（编程助手、研究伴侣、知识 worker）
 
- 你不想把对话历史交给第三方 SaaS - 本地 SQLite 起步够用
 
- 你接受用 OpenClaw 或 Hermes 当 host，或者愿意自己写 adapter
 

## 怎么开始

最低成本的路径是装 OpenClaw + 这个插件 - 两行命令 + 一段配置，跑起来之后打开 `~/.openclaw/memory-tdai/` 看每一层产出。三天之后再回头看 `persona.md` 里它给你画出了什么 - 这是最直接的体感测试。

判据很简单：

- 你不需要在新会话里重新解释项目背景了
 
- agent 主动援引你三周前说过的偏好
 
- 长任务里它没被工具日志撑爆 context
 

这三件事变成常态，TDAI 就在干活儿了。

往大了说，agent memory 还远没收敛 - mem0、Letta、Zep、Hippo、Claude Code 的 `CLAUDE.md` ，每一家在解决同一个问题的不同切面。TDAI 的贡献在于 - 它把「分层 + 符号化 + 白盒可调试」这三件事一起做了，并且把代码全开源出来，让你能看到每一层的产物。这种透明度本身就是稀缺品。

4129 stars 不是终点，但确实说明社区在等一个本地优先、能 debug、能审计的 agent memory 方案。

* * *

- 仓库： [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory)