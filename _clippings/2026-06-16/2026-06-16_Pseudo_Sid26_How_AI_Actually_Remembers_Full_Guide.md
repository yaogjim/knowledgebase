---
title: "2026-06-16_Pseudo_Sid26_How_AI_Actually_Remembers_Full_Guide"
source: "https://x.com/Pseudo_Sid26/status/2049175615195242821"
author:
  - "[[@Pseudo_Sid26]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "x"
  - "@Pseudo_Sid26"
  - "memory"
  - "tokens"
---

# How AI Actually Remembers (Full Guide)

**Siddharth**

# How AI Actually Remembers (Full Guide)

## Your AI agent forgets and makes up details all the time

## So I decided to find out why, here is what I found.

## 

## 

* * *

# INTRODUCTION

Most agent memory bugs are not retrieval bugs. The memory was wrong before retrieval ever ran. It was wrong at token 4,096, when something important quietly left the cache and nothing replaced it.

But there's something happening earlier that nobody talks about as much. Every time the model processes tokens, it's running an attention mechanism.

That mechanism is quietly scoring every token in the context. Some get high attention. Some get ignored. When memory fills up and something has to go, the low scorers disappear.

That's it. That's the decision. No external system, no RAG pipeline, just the model deciding what it's going to keep paying attention to.

That's token level memory. And it shapes everything that comes after.

> I was reading through KV cache compression papers and kept noticing the same thing underneath all the math. The real question wasn't about speed. It was about what a model is actually allowed to remember. That felt like an agent design question, not an infra question

* * *

## Okay what even is the KV cache

When a transformer processes a sentence, it computes a Key vector and a Value vector for every token. These get cached. On the next generation step, the new token attends over all those stored (K, V) pairs to figure out what to output. The cache is what makes this not insanely expensive on every step.

The problem is simple and brutal:

- Every new token adds a (K, V) pair to the cache permanently
- Cache grows linearly with context length
- At 128k tokens on a large model, you're looking at gigabytes per layer per head
 
 在大型模型上处理 128k tokens 时，每层每头的显存需求为 GB 级
- Hardware doesn't care about your use case, it just runs out of memory

![Image](https://pbs.twimg.com/media/HHAT0vpaIAAUvfm?format=png&name=large)

For agents this is a real daily problem. Every tool call output, every retrieved doc, every round of reasoning, every past turn in the conversation, they all eat from this budget. When it fills, something gets cut.

> The question is just what???

Think about it like your phone storage-

1.  You're on a trip, taking photos constantly.
2.  At some point your phone says storage is full.
3.  Now you have two options: stop taking photos, or delete something.
4.  Most naive systems just stop.
5.  Smart systems ask what you actually still need.

```python
# what naive KV cache looks like, no eviction, just growth
kv_cache = []

def cache_token(key, value):
 kv_cache.append((key, value))
 # no scoring, no eviction, no budget check
 # 128k tokens later, this list is just enormous

# memory usage at inference time
print(f"cache size: {len(kv_cache)} pairs")
print(f"approx memory: {len(kv_cache) * 2 * 4096 * 2 / 1e9:.2f} GB")
# at 128k tokens on a 70B model: ~64 GB. just for the cache.
```

* * *

## The first attempt: just keep recent stuff

The straightforward approach was

[StreamingLLM](https://arxiv.org/abs/2309.17453). Keep the first few tokens (called attention sinks, they matter for model stability), keep a sliding window of recent tokens, drop everything in between. Fixed budget, simple rule.

![Image](https://pbs.twimg.com/media/HHAUleabAAEHq6U?format=jpg&name=large)

Reference image from the streaming LLM paper

It worked. Models could run indefinitely without crashing. But it also meant anything that happened more than a few thousand tokens ago was just gone. If your task instruction was way up in the context and a tool call response pushed it out of the window, the model forgot its own objective.

> The assumption that recent = important is doing a lot of quiet damage in agent pipelines. An instruction from 40k tokens ago might be the most critical thing in the entire context.

> Recency and importance really are two different things.

* * *

## 

[SnapKV](https://arxiv.org/abs/2404.14469)\- the model already knows what matters

This is the one that actually changed how I think about this.

The observation is genuinely interesting. Each attention head in a transformer consistently pays attention to the same specific tokens throughout the entire generation process.

> It's not random !!!

- Head 4 in layer 7 might always care about the task instruction tokens.
- Head 2 in layer 3 might always care about entity names.
- This pattern is stable from the first output token to the last.

SnapKV asks: if the pattern is stable, why not use it to decide what to keep?

> They define an observation window, the last segment of the prompt.

> Look at what tokens get high attention inside this window.

> The tokens from earlier in the context that score high here are the heavy hitters. Keep those. Compress the rest.

![Image](https://pbs.twimg.com/media/HHAVaZ3bwAAO3RR?format=png&name=large)

There's also a clustering step. When you naively pick the top scoring tokens you get isolated pieces without the surrounding context. The words right next to an important phrase usually matter too. SnapKV uses max-pool clustering to pull in neighbors around each heavy hitter. So you keep important tokens plus enough context to actually understand them.

> Results:

- 92% compression ratio with 1024 cache slots.
- 3.6x faster generation.
- 8.2x better memory efficiency at 16k tokens.
- It can run 380k token contexts on a single A100.
- The Needle-in-a-Haystack accuracy barely drops.

```python
# simplified SnapKV per-head selection
def snapkv_select(keys, values, obs_window_size=16, budget=1024):
 obs_queries = keys[-obs_window_size:]  # observation window


 attn_scores = obs_queries @ keys[:-obs_window_size].T  # (obs, seq_len)
 token_votes  = attn_scores.sum(dim=0) # aggregate votes

 # pick top-k heavy hitters
 topk_idx = token_votes.topk(budget).indices

 # cluster
 cluster_idx = expand_with_neighbors(topk_idx, kernel_size=5)

 kept_keys = keys[cluster_idx]
 kept_values = values[cluster_idx]

 # new cache = selected prefix + full observation window
 return concat(kept_keys, keys[-obs_window_size:]), \
 concat(kept_values, values[-obs_window_size:])
```

That last test is the important one for agents. It's basically asking: if I bury one specific fact very deep in a very long context, can you still find it?

SnapKV says yes, even after compressing 92% of the cache away. That's not just faster inference, that's better working memory under constraint.

* * *

## What "Cache What Lasts" figured out

SnapKV solved the "how do we compress" question. The token retention paper goes further and asks why some tokens are always important.

The finding is that certain tokens collect high attention weight across all layers, all heads, and throughout the entire generation. Not just in one head or one layer, globally, consistently. These are the true heavy hitters.

Here's the part that stuck with me: the model is already computing this score internally. Every attention operation is implicitly ranking tokens. Token retention papers are just making that ranking explicit and actually using it for eviction decisions.

![Image](https://pbs.twimg.com/media/HHAWRWKbwAQfSJ8?format=png&name=large)

> Intuition for this:

think about the last time you read a really long document and then someone asked you about it. You don't remember every sentence. You remember the heading, the key names, the one specific stat that was surprising. Your brain ran its own retention policy on that document and kept the high signal parts. That's what the model is doing, just in a cache instead of a brain.

- Recency is not importance - a token from 60k positions back can score way higher than one from 10 positions back
 
 近期性并不重要 \- 一个 60k 个位置之前的标记可以比 10 个位置之前的标记得分高得多
- Importance is measurable -cumulative attention weight is stable and reliable
 
 重要性是可衡量的 \-累积注意力权重稳定且可靠
- Eviction should use the score - not position, not age, not random sampling
 
 驱逐应使用分数 \- 非位置，非年龄，非随机抽样
- Budget is fixed - but what fills it should be an intelligent choice
 
 预算是固定的 \- 但填充它的内容应该是一个明智的选择

```python
def compute_token_importance(attention_weights):
 # attention_weights shape: (layers, heads, seq_len, seq_len)
 
 # sum across all layers, all heads, all query positions
 cumulative = attention_weights.sum(dim=(0, 1, 2))  # shape: (seq_len,)
 
 return cumulative


scores = compute_token_importance(attn_weights)
keep = scores.topk(budget).indices
evict  = scores.topk(seq_len - budget, largest=False).indices
```

* * *

## 

[Memory Sparse Attention](https://arxiv.org/abs/2603.23516)\- a different angle

The papers above ask what to keep in the cache. MSA asks what to attend to when computing each new token.

- Full attention is O(n²). At 100M tokens that's just not possible.
- MSA combines top-k token selection with sparse attention patterns
- gets near linear complexity without losing the end to end trainability

The part that's relevant for agents is Memory Interleave. Agents don't process one big document. They process a stream of things across sessions: tool outputs, retrieved docs, user messages from last week.

MSA handles multi hop reasoning across non contiguous context segments. That's an agent memory problem being solved at the attention layer, without any external retrieval pipeline.

- Top-k selection -only attend to the most relevant tokens for each generation step
 
 Top-k 选择 -仅关注每一步生成过程中最相关的标记
- Document wise positional encoding -works across non-contiguous memory segments
 
 文档级位置编码 \-适用于非连续内存段
- 100M token throughput on 2 GPUs - this is a real system claim
 
 1 亿令牌吞吐量 在 2 个 GPU 上 - 这是一个真实的系统声明
- Beats RAG systems on long context benchmarks - retrieval from inside the model
 
 在长上下文基准测试中超越 RAG 系统 \- 从模型内部检索

## The methods compared

There are about a dozen serious papers in this space now. All share the same intuition but differ on how they score tokens and how they set the budget.

I recently compared all of them in a notebook as well.

![Image](https://pbs.twimg.com/media/HHAXLAdbEAAh8YT?format=png&name=large)

molab notebook reference

![Image](https://pbs.twimg.com/media/HHAXRQ1bwAA5-ZN?format=png&name=large)

molab notebook reference

[MOLA NOTEBOOK](https://molab.marimo.io/github/utk7arsh/SnapKV-Marimo/blob/master/notebooks/walkthrough.py/wasm)

* * *

## The connection to agent memory

Here is the thing that actually matters for people building agents.

Most agent memory discussions start at the retrieval layer. Vector database, episodic memory, summarization strategies. All of that is real and important. But it all receives inputs from a model that first had to decide what to attend to. That decision happens earlier, at the token level, and it affects everything downstream.

If a critical token gets evicted from the KV cache before it can influence generation, it's gone. No RAG pipeline retrieves it. No memory manager handles it. The model simply never processed it properly and the output reflects that. If that bad output gets written to external memory, you now have False Memory Propagation starting at the attention layer, before any external system is involved.

![Image](https://pbs.twimg.com/media/HHAXtMhbwAAxC21?format=png&name=large)

> Intuition for this:

imagine you're building a customer support agent for a SaaS product.

- User has a 2-hour troubleshooting session.
- They explain their whole setup at the start
- Then you go through 15 tool calls, logs, configs.
- By the time you're deep into the 15th issue, the original setup context from the start might have been evicted from the cache.
- Now the model starts making suggestions that ignore specific constraints the user mentioned at the beginning.
- It's not wrong because of bad retrieval. It's wrong because the right tokens were already gone before retrieval was even relevant.

## Real problems this causes

Not theoretical. These are things that happen in production:

- Lost in the middle - models reliably forget information in the middle of long contexts, because most eviction strategies favor very recent and very early tokens
 
 中间丢失 \- 模型会在长上下文中间可靠地忘记信息，因为大多数驱逐策略倾向于非常近期和非常早期的 token
- Tool output dilution - a large tool response pushes earlier task instructions out of the effective window
 
 工具输出稀释 \- 大型工具响应将之前的任务指令推出有效窗口
- RAG injection waste - you retrieve 20 chunks, but sparse attention only meaningfully processes a few of them, the rest wasted the context budget
 
 RAG 注入浪费 \- 你检索了 20 个片段，但稀疏注意力机制仅有效处理其中几个，其余的则浪费了上下文预算
- System prompt amnesia - a critical constraint from the system prompt gets evicted mid-generation, model invents a replacement
 
 系统提示失忆症 \- 系统提示中的关键约束在生成过程中被驱逐，模型编造了一个替代方案
- FMP starting at attention - a hallucinated intermediate token scores high on attention because the model is actively using it, it survives eviction, and it poisons the generation chain
 
 FMP 从注意力开始 \- 幻觉的中间 token 在注意力上得分高，因为模型正在主动使用它，它能躲过驱逐，并且它会污染生成链
- Cross session cold start - no KV state persistence across sessions means every session starts fresh, working memory rebuilt from retrieval which is always a lossy reconstruction
 
 跨会话冷启动 \- 跨会话不进行 KV 状态持久化意味着每个会话都从零开始，工作内存从检索中重建，这始终是一种有损重建

* * *

# CONCLUSION

The end state here is a transformer that manages its own memory budget dynamically and intelligently, without any of this needing to be engineered externally. That's not just a better inference system. That's a better memory substrate for every agent running on top of it.

- Per head retention - different heads care about different tokens, eviction should respect that
 
 每个头保留 - 不同的头关注不同的令牌，驱逐应该尊重这一点
- Phase aware compression -prefill and decoding have different memory profiles, treat them separately
 
 相位感知压缩 - 预填充和解码具有不同的内存配置文件，分别处理
- Recoverability - eviction doesn't have to be permanent
 
 可恢复性 \- 驱逐不一定是永久性的
- KV state persistence - save cache state at session end, reload next session, cross-episode continuity without a vector DB
 
 KV 状态持久化 \- 在会话结束时保存缓存状态，在下一次会话中重新加载，跨剧集连续性（无需向量数据库）

Agents that handle long horizon tasks well are not going to be the ones with the fanciest retrieval pipeline. They're going to be the ones where the model itself retained the right things through a long context, and the external memory layer received clean enough inputs to actually work with.

Therefore, Token-level memory is the foundation, not the ceiling. Every retrieval pipeline and memory manager receives inputs from a model that first decided what to attend to. That decision happens in the KV cache. It matters for agent design, not just inference speed.

* * *

## DISCLAIMER

This article was researched and written by the author, edited by Sonnet 4.6. The thumbnail was taken off Pinterest.

References -

\[1\] SnapKV ·

[arxiv.org/abs/2404.14469](//arxiv.org/abs/2404.14469)

\[2\] Cache What Lasts ·

[arxiv.org/abs/2512.03324](//arxiv.org/abs/2512.03324)

\[3\] MSA ·

[arxiv.org/abs/2603.23516](//arxiv.org/abs/2603.23516)

\[4\] D2O ·

[arxiv.org/abs/2406.13035](//arxiv.org/abs/2406.13035)

\[5\] H2O ·

[arxiv.org/abs/2306.14048](//arxiv.org/abs/2306.14048)

\[6\] Scissorhands ·

[arxiv.org/abs/2305.17118](//arxiv.org/abs/2305.17118)

\[7\] StreamingLLM ·

[arxiv.org/abs/2309.17453](//arxiv.org/abs/2309.17453)

\[8\] PyramidKV ·

[arxiv.org/abs/2406.02069](//arxiv.org/abs/2406.02069)

\[9\] CAKE ·

[arxiv.org/abs/2501.10107](//arxiv.org/abs/2501.10107)

\[10\] SCOPE ·

[arxiv.org/abs/2501.13981](//arxiv.org/abs/2501.13981)

* * *