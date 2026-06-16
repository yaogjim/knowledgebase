---
title: "2026-06-16_TheAhmadOsman_LLM_的推理引擎及本地_AI_硬件_2026_年版"
source: "https://x.com/TheAhmadOsman/status/2057183854444843202"
author:
  - "[[@TheAhmadOsman]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "x"
  - "@TheAhmadOsman"
  - "memory"
  - "serving"
---

# LLM 的推理引擎及本地 AI 硬件（2026 年版）

**Ahmad**

# LLM 的推理引擎及本地 AI 硬件（2026 年版）

> You don't pick an inference engine first. You pick a hardware strategy, a workload shape, and a serving model. The engine follows.

That is the most useful way to think about LLM inference engines.

Series note: This is Part 3 in my series teaching Self-hosted LLMs / Local AI.

- Part 1:
 
 [GPU Memory Math for LLMs (2026 Edition)](https://x.com/TheAhmadOsman/status/2040103488714068245).
 
- Part 2:
 
 [Memory Bandwidth for Local AI Hardware (2026 Edition)](https://x.com/TheAhmadOsman/status/2041331757329285589).
 

Those two pieces explain the hardware capacity and bandwidth math.

This one explains the software layer that turns that hardware into usable inference.

## Engines

These tools serve different purposes / occupy different layers

- Local portability
- Consumer CUDA
- Apple unified-memory workflows
- Quantized inference
- Production serving
- Distributed orchestration
- Vendor-optimized datacenter execution

A useful mental model:

![Image](https://pbs.twimg.com/media/HIySrnUW8AAlRr5?format=jpg&name=large)

The inference engine is not "the model." It is the traffic cop, memory manager, kernel dispatcher, scheduler, cache accountant, parallelism planner, API surface, and sometimes the deployment framework.

最佳引擎匹配您的内存层次结构、互联、量化格式、延迟和吞吐量目标、模型架构以及操作成熟度。

## The one-page decision guide

![Image](https://pbs.twimg.com/media/HIySt_uXkAAL3dt?format=jpg&name=large)

- Laptop / edge / odd hardware → llama.cpp
- Mac-first workflows → MLX / MLX-LM
- 单 RTX 本地推理 → ExLlamaV2
- 2-4+ NVIDIA / CUDA GPUs → ExLlamaV3
- General production serving → vLLM
- Long-context / MoE / routing → SGLang
- NVIDIA max performance → TensorRT-LLM
- Cluster orchestration → NVIDIA Dynamo

The rest of this guide explains why.

## What an inference engine actually does

An inference engine loads weights, tokenizes input, runs the forward pass, samples tokens, maintains the KV cache, and streams results. Serious engines also handle batching, scheduling, prefix caching, quantization, parallel execution, API serving, metrics, and distributed execution.

The workload has two phases:

Prefill reads the prompt and builds the initial KV cache. It is compute-intensive.

Decode generates one token at a time, repeatedly reading weights and KV cache. It is memory-bandwidth-bound. Decode speed tracks memory bandwidth more than peak compute.

That distinction explains almost everything:

- Short prompt, long answer: decode dominates → memory bandwidth and batching matter.
- Long prompt, short answer: prefill dominates → attention kernels and chunked prefill matter.
- 许多用户：调度器质量很重要 → 连续批处理，缓存分页，公平性。
- Long context: KV cache dominates → paged attention, KV quantization, offload.
- MoE: 专家路由主导 → 专家并行、互联、分组 GEMMs
- 多节点: 互联主导 → NVLink、RDMA、流水线并行、解耦。

PagedAttention 解决了 KV 缓存碎片化问题。FlashAttention 使用 IO 感知分块来减少 HBM（高带宽内存）流量。推测解码生成廉价 token 并并行验证它们。反复出现的主题：推理性能是内存移动加上调度。

## The real bottlenecks

![Image](https://pbs.twimg.com/media/HIySwctXUAAWvdU?format=jpg&name=large)

1\. Memory bandwidth, not just VRAM size. VRAM determines fit. Bandwidth determines decode speed. Apple's M3 Ultra offers up to 819 GB/s unified-memory bandwidth. NVIDIA's H100 SXM lists 3.35 TB/s GPU memory bandwidth. Unified memory lets you fit models that would not fit in consumer VRAM. HBM lets you serve them faster when the model fits. Fit is not speed. Capacity is not bandwidth.

2\. KV 缓存增长 KV 缓存的大小会随着批次大小和上下文长度而增长。即使权重能够适配，长上下文工作负载也可能耗尽内存。PagedAttention 将 KV 缓存划分为块，提高利用率并支持更大的批次。

3\. Interconnect. The moment a model crosses GPU boundaries (multi-GPUs), you pay communication cost. Tensor parallelism needs frequent all-reduce collectives. Pipeline parallelism communicates at stage boundaries. Expert parallelism needs all-to-all traffic for MoE. vLLM's docs note that without NVLink, pipeline parallelism can outperform tensor parallelism.

4\. Scheduler quality. A good scheduler decides which requests enter the batch, how prefill and decode share the accelerator, whether long prompts block short decodes, and how to avoid starvation. Supporting batching is not the same as behaving like a production-ready scheduler.

5\. 运行时开销。CUDA 图、内核融合、采样开销、分词器开销、HTTP 开销、LoRA 切换以及结构化解码都很重要。在大规模场景下，这些恼人的 2% 开销会形成合力，需要引起重视（并无双关之意）。

## The engine families

![Image](https://pbs.twimg.com/media/HIySychWYAA9HOd?format=jpg&name=large)

There are four broad families:

Portable local runtimes: llama.cpp, MLC LLM, ONNX Runtime GenAI, OpenVINO, Ollama-style tools. These care about "make it run here."

Apple/unified-memory runtimes: MLX and MLX-LM. These care about "use big shared memory and Apple's stack well."

Consumer CUDA quant engines: ExLlamaV2 and ExLlamaV3. These care about "make my 3090/4090/5090 box scream with low-bit weights."

Production serving engines: vLLM, SGLang, TensorRT-LLM, TGI, LMDeploy. These care about concurrent users, KV cache, batching, parallelism, observability, and cost per token.

Then there are orchestration layers like Dynamo that sit above engines and coordinate fleets, disaggregated prefill/decode, routing, and autoscaling.

## llama.cpp: the portability king

llama.cpp is the answer when the hardware is weird, constrained, offline, CPU-heavy, edge-oriented, or not a tidy NVIDIA datacenter node.

It supports Apple Silicon via ARM NEON, Accelerate, and Metal; x86 via AVX/AVX2/AVX512/AMX; RISC-V; low-bit quantization; CUDA; AMD via HIP; MUSA; Vulkan; SYCL; and CPU+GPU hybrid offload. That is why llama.cpp owns the "just make it run" lane.

The HTTP server is more capable than a "toy local runner". llama-server provides OpenAI-compatible routes, Anthropic Messages API compatibility, reranking, continuous batching, multimodal support, JSON schema constraints, function calling, speculative decoding, and a web UI.

The critical limitation: llama.cpp is not for serious multi-node production serving. Its RPC backend is explicitly documented as proof-of-concept, fragile, and insecure.

Verdict: Use llama.cpp when portability, offline operation, GGUF, or hybrid offload matter more than fleet-scale serving.

DO NOT use with

[Multi-GPUs](https://www.ahmadosman.com/blog/do-not-use-llama-cpp-or-ollama-on-multi-gpus-setups-use-vllm-or-exllamav2/)

## MLX and MLX-LM: the Apple Silicon weapon

MLX is Apple's array framework for Apple Silicon, and MLX-LM is the LLM package built on it. It is a Mac-first ML stack.

The key hardware fact is unified memory. Apple Silicon gives the CPU and GPU direct access to the same memory pool. MLX arrays live in unified memory, and you choose the device when running the operation rather than moving arrays between separate memory spaces.

This changes the local inference tradeoff. On a discrete GPU system, the question is "does it fit in VRAM?" On an M-series Mac with large unified memory, the question becomes "does it fit in memory, and can the memory system feed the GPU fast enough?" Large quantized models can fit on machines where the same model would be impossible on a 24 GB consumer GPU.

However, it is also slower.

MLX-LM adds Hugging Face Hub integration, quantization, LoRA and full fine-tuning, distributed inference, and a large MLX Community model ecosystem. MLX is no longer Mac-only: it offers CUDA and CPU-only packages for Linux. Distributed communication supports MPI, Ring over TCP, JACCL for RDMA over Thunderbolt, and NCCL for CUDA.

MLX-LM's server itself warns that it is not recommended for production because it only implements basic security checks.

Verdict: Use MLX for Mac-first ML and LLM workflows. For high-concurrency public serving, start with a real serving stack.

## ExLlamaV2 and V3: consumer CUDA, tuned and fast

ExLlamaV2 是一个本地 CUDA 量化引擎，旨在让消费级 NVIDIA GPU 发挥超出其性能水平的作用。它支持分页注意力、动态批处理、提示词缓存、KV 缓存去重、批生成、流式处理和推测解码。要记住的关键词是“本地”。它能让量化模型在现代 CUDA GPU 上运行得更快，尤其是消费级显卡。

Best fits: one RTX 3090/4090/5090 box, local coding assistant, local chat, EXL2 quantized models, and prosumer workstation use.

ExLlamaV3 延续了面向多 GPU 和 MoE 本地推理的理念。它新增了基于 QTIP 的 EXL3 量化格式，为消费级硬件提供灵活的张量并行和专家并行推理，通过 TabbyAPI 提供一个 OpenAI 兼容的服务器，支持持续动态批处理和多模态功能。

V3 is compelling when you have 2-4+ consumer NVIDIA GPUs or want local MoE. Expect caveats: some models do not support tensor or expert parallelism in ExLlamaV3.

Verdict: ExLlamaV2 is the enthusiast's local CUDA engine. ExLlamaV3 is the frontier for multi-GPU (2-4) local setups. Expect rougher edges for better capability.

## vLLM: the default open-source production server

vLLM is the first engine most teams should evaluate for serious opensource LLM serving.

It offers PagedAttention-based KV memory management, continuous batching, chunked prefill, prefix caching, CUDA/HIP graphs, extensive quantization (FP8, MXFP8/MXFP4, NVFP4, INT8, INT4, GPTQ, AWQ, GGUF), optimized attention and GEMM/MoE kernels, speculative decoding, torch.compile, and disaggregated prefill/decode/encode.

It is also flexible: tensor/pipeline/data/expert/context parallelism, streaming, structured outputs, tool calling, OpenAI-compatible and Anthropic Messages APIs, gRPC, multi-LoRA, and support for NVIDIA, AMD, x86/ARM/PowerPC CPUs, plus plugins for TPUs, Gaudi, Ascend, Apple Silicon, and more.

vLLM's docs note that multi-node deployments typically use Ray, and without NVLink, pipeline parallelism may beat tensor parallelism. The trap is assuming vLLM removes the need for systems thinking. You still need to tune batching, context length, GPU memory utilization, parallelism layout, and routing. vLLM gives you a very good engine; it still requires good System Design.

Verdict: If someone says "we need to serve open models in production," vLLM is the default starting point.

## SGLang: vLLM's systems-brained cousin

SGLang is what you reach for when the serving workload is ugly: structured outputs, long context, MoE, disaggregation, and routing.

It offers RadixAttention prefix caching, prefill-decode disaggregation, speculative decoding, continuous batching, paged attention, tensor/pipeline/expert/data parallelism, structured outputs, chunked prefill, and multi-LoRA batching. It supports NVIDIA, AMD, Intel Xeon, Google TPUs, Ascend NPUs, and more.

SGLang's differentiator is serving architecture. Its prefill-decode disaggregation separates compute-intensive prefill from memory-intensive decode into specialized instances, transferring KV cache between them. This prevents long prefill batches from interrupting decode and spiking token latency.

Verdict: SGLang is for teams whose bottleneck is no longer "can we run the model?" but "can we run it under hostile traffic without torching latency, memory, and cost?"

## TensorRT-LLM: maximum NVIDIA performance

TensorRT-LLM is the NVIDIA-max-performance stack. It is optimized, specialized, powerful, and not pretending to be portable.

It provides Python APIs to build TensorRT engines with state-of-the-art optimizations, plus Python and C++ runtimes. It includes custom kernels for attention, GEMMs, and MoE; prefill-decode disaggregation, Wide Expert Parallelism, speculative decoding; and a high-level Python API integrated with NVIDIA Dynamo and Triton Inference Server.

B200 GPUs can load FP4 weights with optimized kernels. H100 and later support FP8 quantization that can double performance and halve memory consumption versus 16-bit with minimal accuracy loss.

Where it shines: H100/H200/B200/GB200/GB300-class fleets, NVIDIA-only datacenters, FP8/FP4 deployment, multi-node serving, and MoE at scale. Where it is awkward: AMD, Apple, or Intel portability; fast-changing experimental models; small local setups; and teams that need "works on everything."

Verdict: If you are committed to NVIDIA and care about absolute performance, TensorRT-LLM belongs in the bake-off. You trade portability for performance. Tuned specialization but less features.

## The rest of the field

TGI 是 Hugging Face 的生产服务器，具备跟踪、指标、张量并行和连续批处理功能。当需要 HF 集成和简洁性时使用它。

MLC LLM is the compiler-first universal deployment engine with OpenAI-compatible APIs across REST, Python, JavaScript, iOS, and Android. Best for "ship LLMs everywhere," especially browser, mobile, and native apps.

ONNX Runtime GenAI implements the full generative loop over ONNX Runtime and powers Foundry Local, Windows ML, and the VS Code AI Toolkit. It supports CPU, CUDA, DirectML, TensorRT-RTX, OpenVINO, QNN, WebGPU, and AMD GPU. Best for app deployment and ONNX workflows.

OpenVINO GenAI is the Intel-optimized story for Xeon CPUs, Arc GPUs, Core Ultra, and NPUs. It offers OpenAI-compatible serving with continuous batching and paged attention. Best for Intel hardware.

LMDeploy is a CUDA-focused toolkit with TurboMind for performance and PyTorch for accessibility. Most interesting for CUDA users who want an alternative to vLLM/SGLang/TensorRT-LLM.

NVIDIA Dynamo 是一个分布式编排层，位于 vLLM、SGLang 和 TensorRT-LLM 等引擎之上，支持解聚合、智能路由和多层 KV 缓存。当单引擎服务不再足够时使用它。

Note: DO NOT USE Ollama.

## Hardware strategy recipes

![Image](https://pbs.twimg.com/media/HIyS3rPWoAAICxo?format=jpg&name=large)

仅 CPU 服务器: llama.cpp 优先。适用于 Intel Xeon 的 OpenVINO。适用于应用/ONNX 部署的 ONNX Runtime GenAI。

MacBook / Mac Studio：MLX / MLX-LM 用于 Mac 原生工作流。llama.cpp 用于 GGUF 可移植性。

单 RTX 3090 / 4090 / 5090: ExLlamaV2 用于 EXL2 本地推理。llama.cpp 用于 GGUF 或可移植性。若服务多用户则使用 vLLM。

双或四消费级 RTX 设备：ExLlamaV3 用于多 GPU 量化推理或混合专家模型（MoE）。如果服务行为很重要则使用 vLLM。如果测试路由或长上下文模式则使用 SGLang。

8×H100 / H200 node: Start with vLLM or SGLang. Benchmark TensorRT-LLM if NVIDIA-only and performance justifies tuning. Use Dynamo when multi-node orchestration becomes necessary.

B200 / GB200 / GB300-class infrastructure: Benchmark TensorRT-LLM, SGLang, and vLLM. Add Dynamo for fleet-level orchestration, KV-aware routing, and autoscaling.

AMD MI300 / MI325 / MI350 / MI355: Start with vLLM or SGLang on ROCm. Avoid assuming NVIDIA benchmarks transfer cleanly.

Intel Xeon / Core Ultra / Arc: OpenVINO 生成式 AI 或 OpenVINO Model Server。如果应用嵌入很重要，则使用 ONNX Runtime 生成式 AI。

Browser, mobile, app-native: MLC LLM / WebLLM or ONNX Runtime GenAI.

## Benchmarking: what to measure

Bad benchmark: "I got 180 tok/s."

![Image](https://pbs.twimg.com/media/HIyS6ZyXoAA6C-8?format=jpg&name=large)

Good benchmark includes:

Model: exact model, architecture, parameter count, active MoE params.

Weights: dtype, quant format, group size, calibration.

引擎：版本，提交，后端，标志。

Hardware: GPU SKU, memory capacity, bandwidth, interconnect, CPU, RAM.

Workload: input/output length distributions, concurrency, streaming, shared prefixes, structured output.

Metrics: TTFT, TPOT, end-to-end latency, p50/p95/p99, tokens per second, requests per second, GPU memory usage, KV cache hit rate, prefill throughput, decode throughput, cost per 1M tokens.

Benchmarking Rules:

1.  Never compare engines using only single-user tokens per second.
2.  Test your actual prompt and output distribution.
3.  Test with realistic concurrency.
4.  Separate prefill from decode.
5.  Track p95 and p99, not only averages.
6.  Measure memory headroom at target context length.
7.  Test cache reuse if your app has repeated prefixes.
8.  Benchmark structured output separately; grammar adds overhead.
9.  Benchmark LoRA and multi-LoRA separately.
10.  Re-test after driver, CUDA, ROCm, model, or engine upgrades.

## Common mistakes

Choosing by VRAM capacity alone. VRAM determines fit. Bandwidth and scheduler determine speed. A large unified-memory machine can fit huge models, but an H100 decodes faster when the model fits due to much higher HBM bandwidth.

Using tensor parallelism on weak interconnect. Without NVLink or NVSwitch, test pipeline parallelism. vLLM's docs call this out for L40S-like setups.

忽略 KV 缓存。长上下文和并发可能使 KV 缓存成为限制因素。PagedAttention、前缀缓存、KV 量化和解聚合在规模化时不是可选的。

Treating local engines as production servers. llama.cpp server is capable. MLX-LM server is convenient. Ollama is pleasant yet SHOULD NOT BE USED.

However, production means security, observability, backpressure, routing, autoscaling, and SLA behavior. MLX-LM itself warns that its server is not recommended for production.

假设每种量化格式都是可移植的。GGUF、EXL2、EXL3、AWQ、GPTQ、FP8、FP4、MLX 格式以及 ONNX 格式并不互通。正确的格式是你的引擎已针对其优化核心的那种格式。

忽略模型架构。密集模型、MoE、混合注意力、多模态模型以及长上下文变体影响引擎的不同部分。广泛支持并不意味着每种优化的效果都相同。

Trusting benchmark charts without workload shape. A chart for Llama 3.1 8B at 1K input / 128 output says little about a coding agent with 80K context running on Qwen 3.6 27B / Gemma 4 26B-A4B, or a RAG service with 500 concurrent users.

## The opinionated final map

Local AI user: LM Studio or

[Harbor](https://github.com/av/harbor) for convenience. llama.cpp for control. MLX on Mac. ExLlamaV2/V3 for CUDA local performance.

Building a local agent: Any should work, but given what most people use; llama.cpp for portability. MLX if users are on Apple Silicon. vLLM if simulating production serving locally.

Serving an internal team: Start with vLLM. Use SGLang if structured outputs, long context, multi-LoRA, MoE, or routing matter.

Serving customers at scale: Benchmark vLLM, SGLang, and TensorRT-LLM. If routing and disaggregation matter, SGLang and Dynamo deserve attention.

NVIDIA datacenter: TensorRT-LLM for max performance. vLLM for flexibility. SGLang for complex serving. Dynamo for fleet orchestration.

Apple Silicon: MLX for native development. llama.cpp for GGUF. Unified memory is a capacity superpower with bandwidth tradeoffs, not HBM.

Edge, app, browser, or Windows-native: llama.cpp, MLC LLM, ONNX Runtime GenAI, or OpenVINO, depending on stack.

## Final principle

Inference Engines have consequences.

Pick the engine after answering these:

1.  What hardware do I actually have?
2.  Does the model fit in fast memory, or only in system/unified memory?
3.  Is decode or prefill the bottleneck?
4.  What context length and concurrency matter?
5.  Are prompts shared enough for prefix caching?
6.  Is the model dense, MoE, multimodal, or hybrid?
7.  Do I need local convenience, production serving, or fleet orchestration?
8.  What quantization format has optimized kernels on my target engine?
9.  Is my interconnect PCIe, NVLink, NVSwitch, Ethernet, RDMA, or Thunderbolt?
10.  Am I optimizing latency, throughput, cost, privacy, portability, or developer speed?

The engine follows the answers.

Until next time.

\-Ahmad