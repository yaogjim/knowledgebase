---
title: "2025-11-13_stackobserve_我觉得厂商们默认把_jsonschema_塞到_model_context_里的作法特别蠢_所以我"
source: "https://x.com/stackobserve/status/1988480146647773487"
author:
  - "[[@stackobserve]]"
published: 2025-11-13
created: 2025-11-13
description:
tags:
  - "x"
  - "@stackobserve"
  - "mcp"
  - "2025-11-12"
---

# 我觉得厂商们默认把 jsonschema 塞到 model context 里的作法特别蠢, 所以我

**HD** @stackobserve 2025-11-12

我觉得厂商们默认把 jsonschema 塞到 model context 里的作法特别蠢, 所以我做了 https://github.com/AIGC-Hackers/mcpx…, list mcp 会直接返回 tools 的 typescript 声明, 像 notion 这样的 mcp tools list, 输出少了 10 倍

> 2025-11-12
> 
> 艹，看到最后没绷住喷了
> 
> 作者看完 Anthropic 那篇“用 MCP 执行代码”的文章时，“灵光一现”把 MCP 都扔到子 Agent，这样就不占用主 Agent 的上下文窗口。
> 
> 放到 SubAgent 后果然不会污染主上下文了，但处理这么大量的 MCP 服务器工具，仍然很消耗 Token，很快就达到了 Claude 的使用上限。 x.com/goon\_nguyen/st…

* * *

**非典型程序员** @null12022202 [2025-11-12](https://x.com/null12022202/status/1988574713971659227)

准确地说，是少了 90%😆

* * *

**TinKin zhang** @yin\_yon54525 [2025-11-12](https://x.com/yin_yon54525/status/1988603297058664659)

我记得cc的系统提示词是这么写的