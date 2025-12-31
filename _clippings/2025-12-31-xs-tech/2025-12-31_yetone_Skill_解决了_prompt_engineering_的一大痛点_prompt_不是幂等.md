---
title: "2025-12-31_yetone_Skill_解决了_prompt_engineering_的一大痛点_prompt_不是幂等"
source: "https://x.com/yetone/status/2005535844132897119"
author:
  - "[[@yetone]]"
published: 2025-12-31
created: 2025-12-31
description:
tags:
  - "x"
  - "@yetone"
  - "https"
  - "2025-12-29"
---

# Skill 解决了 prompt engineering 的一大痛点 —— 「prompt 不是幂等

**yetone** @yetone 2025-12-28

Skill 解决了 prompt engineering 的一大痛点 —— 「prompt 不是幂等的」，就是相同的 prompt 在相同的 model 下每一次的生成结果都可能是不同的。

Skill 就是把 prompt 中能幂等的部分单独拆出来抽象成 script/binary，这种把非幂等逻辑和幂等逻辑相互隔离的分治法类似于 Rust 一直在做的把 unsafe 和 safe 相互隔离的哲学：既然避免不了非幂等和 unsafe，不如建立厚厚的安全墙，让非幂等和 unsafe 的区域越来越小，让幂等和 safe 的区域越来越大，这样的应用才会越来越可靠。

> 2025-12-28
> 
> Skill 很好，但也没必要拔太高和神话它，Skill 只是一种技术手段，是 Agent 的重要工具，本身都没有自主性。现在 Agent 离靠谱都还早，更不要说 Skill 了。 x.com/jefferytatsuya…

* * *

**yetone** @yetone [2025-12-29](https://x.com/yetone/status/2005571069378539977)

感谢 @mranti 和 @adam8157 指正，这里「幂等」用错了，应该是用「确定性」 x.com/yetone/status/…

> 2025-12-29
> 
> 感谢 @mranti 和 @adam8157 指正，这里「幂等」用错了，应该是用「确定性」 x.com/yetone/status/…

* * *

**Yaphet** @Ajun65322052 [2025-12-29](https://x.com/Ajun65322052/status/2005580491630813577)

感觉，这并不是 skills 解决的，这个思路应该追溯到 tool calling 就是了。如果只说 skills 解决的，感觉还是范式的问题

* * *

**yetone** @yetone [2025-12-29](https://x.com/yetone/status/2005581328297931014)

LLM 不喜欢用自定义的 tool 的，LLM 只喜欢用 filesystem based tool 和 Bash tool，Skill 恰恰利用了 LLM 的这一习性

* * *

**Xu Desheng** @xudesheng [2025-12-30](https://x.com/xudesheng/status/2005904744741478890)

你这个一下子从认识上拔高了！👍

* * *

**黑眼圈** @i\_m\_m\_ [2025-12-29](https://x.com/i_m_m_/status/2005593667587936694)

透彻！

* * *

**李志** @LiZhiZhuangB123 [2025-12-29](https://x.com/LiZhiZhuangB123/status/2005570372486516851)

从LLM的角度讲，Skill本身是幂等，这个没问题，但Skill 并不能彻底解决非幂等问题，而且把不确定性往上推了一层。

好的设计下，Skill 内部执行通常是幂等的，但调用哪个 Skill、传什么参数，往往还是由 LLM 来决定，实际上也无法 100% 保证确定性，分布式推理、MoE 架构、浮点精度等因素会导致 logits

* * *

**RichChat** @richardchang [2025-12-30](https://x.com/richardchang/status/2005800365229584393)

稍微有点没看懂原文🤣 重新翻译了一下感觉yetone的这个针对skills的注解是挺透彻的：

痛点：用大语言模型的时候，一个大问题就是“prompt 不幂等”。“幂等”简单说，就是同一个操作重复做几次，结果应该一模一样。比如数学里，绝对值函数 abs(abs(x)) = abs(x)，不管算几次都一样。

* * *

**Michael Guo** @Michaelzsguo [2025-12-29](https://x.com/Michaelzsguo/status/2005684769217245482)

我同意宝玉的看法：不能把Skill看的太高了。AI的趋势应该是让AI自己去figure out这堵安全墙， 减少人为的作用。AI其实是有这个能力的， 譬如我今天创建的一个Skill就是完全是由CC自己造出来的， 我只是和它对话提供一些要求 - 他知道他需要什么（问问题），我提供要求（回答）。

* * *

**AirPoker** @undeter61646319 [2025-12-29](https://x.com/undeter61646319/status/2005583373125980443)

skills越高大全整体越幂等，不过足够高大全时为啥不手动/自动触发呢..

* * *

**Rain** @aroma10928750 [2025-12-29](https://x.com/aroma10928750/status/2005549243998892371)

Skill 里面可以幂等拆分出来的部分一般是哪些，可以怎么拆

* * *

**wang wa** @zxyu0023 [2025-12-29](https://x.com/zxyu0023/status/2005670655732359639)

把 LLM 当成不可信的 unsafe block：允许它做事，但不允许它决定“对不对”。

* * *

**ZW** @zway\_ai [2025-12-29](https://x.com/zway_ai/status/2005549355357614448)

一段话就把我一直弄不明白的 skill 讲明白了。感谢

* * *

**Nanka** @NankaCN [2025-12-29](https://x.com/NankaCN/status/2005546706742682064)

有趣的角度

* * *

**RoyalWithCheese** @eseehchtiwlayor [2025-12-29](https://x.com/eseehchtiwlayor/status/2005553913630749118)

说得好清楚，透了的感觉

* * *

**Hanchin Hsieh** @\_yuchanns\_ [2025-12-29](https://x.com/_yuchanns_/status/2005536384745111917)

这个说法赞👍

* * *

**web3nomad.eth | atypica.ai** @web3nomad [2025-12-29](https://x.com/web3nomad/status/2005559675207696418)

通透

* * *

**xu** @xu6009594887919 [2025-12-29](https://x.com/xu6009594887919/status/2005558173084917986)

厉害