---
title: "2026-03-05_github_com_BruceLanLan_openclaw_memory_hub"
source: "https://github.com/BruceLanLan/openclaw-memory-hub"
author:
  - "[[@github.com]]"
published: 2026-03-05
created: 2026-03-05
description:
tags:
  - "github"
  - "@github.com"
  - "md"
  - "memory_hub"
---

# BruceLanLan/openclaw-memory-hub

Open in github.dev Open in a new github.dev tab Open in codespace Name Name Last commit message Last commit date Bruce Lan and Bruce Lan feat: 三层记忆/归档、create_decision、status、MEMORY_INDEX、get_context_for_age… 4cde823 · 3 Commits docs docs feat: 三层记忆/归档、create_decision、status、MEMORY_INDEX、get_context_for_age… memory_hub memory_hub feat: 三层记忆/归档、create_decision、status、MEMORY_INDEX、get_context_for_age… scripts scripts feat: OpenClaw 智能记忆中枢 - 独立开源仓库 .gitignore.gitignore feat: OpenClaw 智能记忆中枢 - 独立开源仓库 LICENSE LICENSE feat: OpenClaw 智能记忆中枢 - 独立开源仓库 PROMPT_MEMORY_HUB.md PROMPT_MEMORY_HUB.md feat: OpenClaw 智能记忆中枢 - 独立开源仓库 README.md README.md feat: 三层记忆/归档、create_decision、status、MEMORY_INDEX、get_context_for_age… pyproject.toml pyproject.toml chore: 使用 BruceLanLan 仓库地址 OpenClaw 智能记忆中枢 给 AI Agent（MiniMax / OpenClaw / Claude 等）装上「灵魂中枢」：把思考、任务、决策全部接入记忆闭环，可追溯、可反哺，数据为空时熔断不编造。 English | 中文 功能 功能 说明 对话上下文智能提取 优先用 OpenClaw Agent 抽成 JSON；未安装或超时则本地规则兜底 决策落 JSON life/decisions/*.json ，每条决策可追溯 检查点写 MEMORY 每次 checkpoint 追加一节到 MEMORY.md ，不覆盖 数据为空熔断 上下文过短或无可提取内容时不写 MEMORY，不编造 每日反哺 TASK_QUEUE 可调用 append_task_queue_today() 写明日/待办 三层记忆 MEMORY 超限自动归档到 life/archives/ ，保持精选记忆精简（可配置 MEMORY_MAX_CHARS / MEMORY_MAX_SECTIONS ） 健康检查 python -m memory_hub status 输出工作目录、MEMORY 大小、检查点数、决策条数等 省 token 上下文 MEMORY_INDEX.md 索引 + get_context_for_agent(max_chars) ：完整记忆在 MEMORY/归档，Agent 只读精简上下文 安装 Python 3.9+ ，无第三方依赖（仅标准库）。 可选：安装 OpenClaw 以使用 Agent 做智能抽取；不装则自动走本地规则兜底。 git clone https://github.com/BruceLanLan/openclaw-memory-hub.git
cd openclaw-memory-hub
# 可选：在虚拟环境中以可编辑方式安装，便于在其他项目里 import
# python3 -m venv .venv && source .venv/bin/activate # Windows: .venv\Scripts\activate
# pip install -e .不安装也可直接在本仓库根目录执行 python -m memory_hub 。 快速开始 1. 环境变量（可选） export OPENCLAW_WORKSPACE="/path/to/your/workspace" # 与 OpenClaw 共用目录
# 或
export MEMORY_HUB_WORKSPACE="/path/to/.memory_hub"
export OPENCLAW_BIN="openclaw"
export OPENCLAW_SESSION_ID="main"
# 可选：熔断与条数（默认 50 / 200 / 50）
export MEMORY_MIN_CONTEXT_LENGTH="50"
export MEMORY_MAX_RECENT_LINES="200"
export MEMORY_MAX_DECISIONS_PER_CHECKPOINT="50"
# 可选：三层记忆 - MEMORY 超限自动归档（默认 8000 字符 / 30 段）
export MEMORY_MAX_CHARS="8000"
export MEMORY_MAX_SECTIONS="30"
# 可选：省 token - 索引保留条数、Agent 上下文上限（默认 80 条 / 2500 字符）
export MEMORY_INDEX_MAX_LINES="80"
export MEMORY_CONTEXT_MAX_CHARS="2500" 不设置时，数据目录默认为 当前仓库根目录下的 .memory_hub 。 更多设计参考： ClawIntelligentMemory ，对照说明见 docs/REFERENCE_ClawIntelligentMemory.md 。 2. 执行检查点 # 在仓库根目录
python -m memory_hub # 从指定文件读取上下文
python -m memory_hub --context-file ./memory/2025-03-05.md # 不使用 OpenClaw，仅本地规则兜底
python -m memory_hub --no-openclaw # 健康检查 / 状态（可与 ClawIntelligentMemory 风格看板对接）
python -m memory_hub status
python -m memory_hub status --json # 输出省 token 的上下文（供 OpenClaw/Agent 注入，默认 2500 字符）
python -m memory_hub context
python -m memory_hub context --max-chars 2000 crontab -e
# 添加（请改路径）：
0 */6 * * * cd /path/to/openclaw-memory-hub && python -m memory_hub >> .memory_hub/checkpoint.log 2>&1 或使用脚本： chmod +x scripts/checkpoint_memory_llm.sh
# cron: 0 */6 * * * /path/to/openclaw-memory-hub/scripts/checkpoint_memory_llm.sh 目录结构（自动创建）.memory_hub/ # 或由 OPENCLAW_WORKSPACE 指定
├── MEMORY.md # 第二层：精选记忆（超限自动归档）
├── MEMORY_INDEX.md # 记忆索引（要点一条一行，省 token 回顾用）
├── TASK_QUEUE.md # 每日反哺的明日/待办
├── life/
│ ├── decisions/ # 决策 JSON（可追溯）
│ │ └── dec_20250305_120000.json
│ └── archives/ # 第三层：归档（MEMORY 超限时自动写入）
│ └── memory-archive-2025-03-05.md
└── memory/ # 第一层：按日期的原始对话/日志 └── 2025-03-05.md 验证是否生效 决策 JSON ： ls .memory_hub/life/decisions/ ，查看最新文件内容。 运行检查点 ： python -m memory_hub ，看是否追加 MEMORY.md 。 MEMORY.md ：查看最新一节「检查点 YYYY-MM-DD HH:MM:SS」。 TASK_QUEUE.md ：查看今日反哺的「明日/待办」。 见 PROMPT_MEMORY_HUB.md ，复制进 MiniMax/OpenClaw 即可要求其所有工作、思考、任务接入本记忆闭环。 API 示例 from memory_hub import ( get_config, extract_from_context, write_decision, create_decision, run_checkpoint, append_task_queue_today, mark_task_done, get_status, get_context_for_agent,
) # 从一段对话提取并跑一次检查点
ctx = "用户：明天把风控阈值调高。Agent：已记录，明日执行。"
run_checkpoint(context=ctx) # 写单条决策（简单）
write_decision({"action": "调高风控阈值", "reason": "用户要求", "due": "明日"}) # 创建可追溯决策（对齐 ClawIntelligentMemory：选项、原因、预期结果）
create_decision( title="风控阈值调整", context="用户要求明日生效", options=["维持 3%", "调高到 5%", "调高到 8%"], selected=1, reason="平衡风险与收益", expected_outcome="明日 5% 生效", tags=["risk", "config"],
) # 每日结束时反哺
append_task_queue_today( evolution_points=["今日完成策略学习 3 条"], tomorrow_tasks=["调高风控阈值", "回测新策略"],
) # 把 TASK_QUEUE 中第 1 个未完成任务勾选为已完成
mark_task_done(task_index=1) # 获取省 token 的上下文字符串（给 OpenClaw 对话前注入，默认 2500 字符）
ctx = get_context_for_agent(max_chars=2000)
# 或直接读索引 + 最近检查点 + 待办，总长不超过 max_chars 故障排查 现象 可能原因 处理 每次都是「数据为空已熔断」 未传 --context-file 且当日 memory/YYYY-MM-DD.md 不存在或过短 指定 --context-file 指向有内容的对话文件，或先往 memory/ 下按日期写入日志 OpenClaw 未安装 未装 openclaw 或不在 PATH 使用 --no-openclaw 走本地规则兜底，或安装 OpenClaw 提取内容很少 本地兜底只做关键词匹配（决策/任务） 安装并配置 OpenClaw 以获得 LLM 抽取 省 token：记住一切但少占上下文 完整记忆 仍在 MEMORY.md + life/archives/ ，不丢信息。 MEMORY_INDEX.md ：每次检查点把「决策 / 任务 / 下一步」压成一行一条，只保留最近约 80 条，供快速回顾。 get_context_for_agent(max_chars) ：生成「索引 + 最近 1～2 个检查点 + 待办」并截断到 max_chars （默认 2500），对话前注入这一段即可，无需整份 MEMORY。 使用方式： python -m memory_hub context --max-chars 2000 或代码中 get_context_for_agent(max_chars=2000) 。 更多可优化点见 docs/OPTIMIZATION.md 。 License MIT English OpenClaw Memory Hub — A minimal “soul layer” memory loop for AI agents: decisions → JSON, checkpoints → MEMORY.md, daily feedback → TASK_QUEUE.md. Empty data triggers a circuit breaker (no hallucination). Works with or without OpenClaw; fallback uses local rule-based extraction. Python 3.9+, no extra deps.Install: pip install -e . (optional). Run: python -m memory_hub from repo root. See README above for env vars and cron.Releases No releases published Packages No packages published Contributors No contributors Languages Python 97.4% Shell 2.6%