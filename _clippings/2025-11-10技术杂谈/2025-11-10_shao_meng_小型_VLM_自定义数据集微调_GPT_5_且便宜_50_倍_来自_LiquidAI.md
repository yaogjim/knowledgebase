---
title: "2025-11-10_shao_meng_小型_VLM_自定义数据集微调_GPT_5_且便宜_50_倍_来自_LiquidAI"
source: "https://x.com/shao__meng/status/1987681107723403448/?s=12&t=bx0WG1AGHlEB9ipAHDEpnw&rw_tt_thread=True"
author:
  - "[[@shao__meng]]"
published: 2025-11-10
created: 2025-11-10
description:
tags:
  - "x"
  - "@shao__meng"
  - "ai"
  - "csv"
---

# 小型 VLM + 自定义数据集微调 ≈ GPT-5，且便宜 50 倍！ 来自 @LiquidAI_

**meng shao** @shao\_\_meng 2025-11-09

小型 VLM + 自定义数据集微调 ≈ GPT-5，且便宜 50 倍！

来自 @LiquidAI\_ 成员 @paulabartabajo\_ 给 AI 工程师的实用建议。核心观点强调：在特定任务或领域，使用小型视觉语言模型（VLM）并基于自定义数据集进行微调，可以实现与大型通用模型（如 GPT-5）相当的准确性，同时显著降低成本（约 50 倍）。这体现了 AI 开发中的效率优先原则：小型模型在专用场景下往往更经济、更易部署，且通过微调能针对性优化性能，避免大模型的资源浪费。

开源项目

使用 Liquid AI 基础模型（LFM）和 LEAP SDK 构建的各种教程、示例和应用。演示了如何构建一个本地化的智能体工作流，用于自动解析发票文件。它强调数据隐私，因为整个过程在用户本地机器上运行，无需云服务或 API 密钥。

创建一个简单的 Python CLI，它可以监控指定文件夹中的新发票文件（通常为图像格式，如 PNG 或 JPEG），并从中提取结构化信息，例如金额和货币。然后，将提取的结果追加到 CSV 文件中，便于后续分析或记录。该工作流适用于处理日常账单或发票，展示了小型本地语言模型在实际任务中的应用潜力。根据测试，它能正确处理约 75% 的样本发票，突出模型的实用性和改进空间。

关键技术和模型

· @ollama：用于在本地运行和管理语言模型的框架，支持高效的模型推理。

· uv：一个高效的 Python 包管理器，用于处理依赖和脚本执行，提高开发效率。

· LFM2-VL-3B：Liquid AI 的视觉语言模型，负责从发票图像中提取原始文本描述，包括 OCR 功能。

· LFM2-1.2B-Extract：另一个 Liquid AI 模型，专用于将非结构化文本转换为结构化数据记录，例如 JSON 格式的金额和货币字段。

这些模型均为小型（nano 级），可在普通硬件上运行，强调成本效益和本地部署。

代码结构和工作原理

代码主要位于 src/invoice\_parser/main.py，采用模块化设计，便于扩展。工作流分为以下步骤：

1\. 文件监控：工具持续监视指定的目录（如 invoices/），检测新添加的发票文件。

2\. 文本提取：一旦检测到新文件，LFM2-VL-3B 模型会处理图像，生成原始文本描述（例如，识别出 “Total: $100 USD” 等内容）。

3\. 信息结构化：将提取的文本传递给 LFM2-1.2B-Extract 模型，它使用提示工程将文本转换为结构化数据，如 {"amount": 100, "currency": "USD"}。

4\. 数据存储：将结构化结果追加到目录中的 bills.csv 文件，确保数据持久化。

整个过程是链式的（chained），类似于智能体协作：视觉模型充当“眼睛”，提取模型充当“大脑”。如果处理现有文件，可以通过命令行参数启用。

开源地址：

https://github.com/Liquid4All/cookbook/tree/main/examples/invoice-parser…

> 2025-11-09
> 
> Advice for AI engineers 💡
> 
> A small Visual Language Model fine-tuned on your custom dataset is as accurate as GPT-5...
> 
> ... and costs 50 times less.
> 
> For example, LFM2-VL-3B by @LiquidAI\_ ↓
> 
> 给 AI 工程师的建议 💡
> 
> 一个基于您定制数据集微调的小型视觉语言模型，其准确度堪比 GPT-5...
> 
> ...且成本降低了50倍。
> 
> 例如，LFM2-VL-3B 由 @LiquidAI\_ ↓ 开发
> 
> ![Diagram split into two steps for invoice processing workflow. Step 1 shows input invoices and CSV output connected through LFM2-VL-3B model for image-to-text extraction and LFM2-1.2B for text structuring. Step 2 displays similar flow from invoices via LFM2-VL-3B to text, then LFM2-1.2B extract to record output in CSV. Purple boxes represent models, arrows indicate data flow, gray areas for inputs and outputs.](https://pbs.twimg.com/media/G5WpUz_aIAAIRI3?format=jpg&name=large)

* * *

**ihaveadream** @dreamOfTu [2025-11-10](https://x.com/dreamOfTu/status/1987710340973670550)

用qwen3 vl小参数模型是否也行？

* * *

**meng shao** @shao\_\_meng [2025-11-10](https://x.com/shao__meng/status/1987710525053280415)

我觉得行

* * *

**The Daily Signal** @DailySignal

Victor Davis Hanson: America Fought a Civil War So Trump Could Enforce Federal Law

Last month, former Democrat Speaker of the House Nancy Pelosi suggested that local and state authorities in California, a sanctuary state, could arrest federal agents for enforcing federal

维克多·戴维斯·汉森：美国曾经历内战，只为让特朗普得以执行联邦法律

上个月，前民主党众议院议长南希·佩洛西提出，作为庇护州的加利福尼亚州地方和州政府可以逮捕执行联邦任务的联邦特工