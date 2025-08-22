---
title: "@Kseniase on Hugging Face: \"11 new types of RAGRAG is evolving fast, keeping pace with cutting-edge AI…\""
source: "https://huggingface.co/posts/Kseniase/836565977783893"
author:
published: 2025-04-20
created: 2025-04-23
description: "We’re on a journey to advance and democratize artificial intelligence through open source and open science."
tags:
  - "clippings"
---

11 new types of RAG  
  
RAG is evolving fast, keeping pace with cutting-edge AI trends. Today it becomes more agentic and smarter at navigating complex structures like hypergraphs.  
  
Here are 11 latest RAG types:  
  
1\. InstructRAG -> [InstructRAG: Leveraging Retrieval-Augmented Generation on Instruction Graphs for LLM-Based Task Planning (2504.13032)](https://huggingface.co/papers/2504.13032)  
Combines RAG with a multi-agent framework, using a graph-based structure, an RL agent to expand task coverage, and a meta-learning agent for better generalization  
  
2\. CoRAG (Collaborative RAG) -> [CoRAG: Collaborative Retrieval-Augmented Generation (2504.01883)](https://huggingface.co/papers/2504.01883)  
A collaborative framework that extends RAG to settings where clients train a shared model using a joint passage store  
  
3\. ReaRAG -> [ReaRAG: Knowledge-guided Reasoning Enhances Factuality of Large Reasoning Models with Iterative Retrieval Augmented Generation (2503.21729)](https://huggingface.co/papers/2503.21729)  
It uses a Thought-Action-Observation loop to decide at each step whether to retrieve information or finalize an answer, reducing unnecessary reasoning and errors  
  
4\. MCTS-RAG -> [MCTS-RAG: Enhancing Retrieval-Augmented Generation with Monte Carlo Tree Search (2503.20757)](https://huggingface.co/papers/2503.20757)  
Combines RAG with Monte Carlo Tree Search (MCTS) to help small LMs handle complex, knowledge-heavy tasks  
  
5\. Typed-RAG - > [Typed-RAG: Type-aware Multi-Aspect Decomposition for Non-Factoid Question Answering (2503.15879)](https://huggingface.co/papers/2503.15879)  
Improves answers on open-ended questions by identifying question types (a debate, personal experience, or comparison) and breaking it down into simpler parts  
  
6\. MADAM-RAG -> [Retrieval-Augmented Generation with Conflicting Evidence (2504.13079)](https://huggingface.co/papers/2504.13079)  
A multi-agent system where models debate answers over multiple rounds and an aggregator filters noise and misinformation  
  
7\. HM-RAG -> [HM-RAG: Hierarchical Multi-Agent Multimodal Retrieval Augmented Generation (2504.12330)](https://huggingface.co/papers/2504.12330)  
A hierarchical multi-agent RAG framework that uses 3 agents: one to split queries, one to retrieve across multiple data types (text, graphs and web), and one to merge and refine answers  
  
8\. CDF-RAG -> [CDF-RAG: Causal Dynamic Feedback for Adaptive Retrieval-Augmented Generation (2504.12560)](https://huggingface.co/papers/2504.12560)  
Works with causal graphs and enables multi-hop causal reasoning, refining queries. It validates responses against causal pathways  
  
These are graph-centric types of RAG:

1. NodeRAG -> [https://huggingface.co/papers/2504.11544](https://huggingface.co/papers/2504.11544)  
	Uses well-designed heterogeneous graph structures and focuses on graph design to ensure smooth integration of graph algorithms. It outperforms GraphRAG and LightRAG on multi-hop and open-ended QA benchmarks
2. HeteRAG -> [https://huggingface.co/papers/2504.10529](https://huggingface.co/papers/2504.10529)  
	This heterogeneous RAG framework decouples knowledge chunk representations. It uses multi-granular views for retrieval and concise chunks for generation, along with adaptive prompt tuning
3. Hyper-RAG -> [https://huggingface.co/papers/2504.08758](https://huggingface.co/papers/2504.08758)  
	A hypergraph-based RAG method. By capturing both pairwise and complex relationships in domain-specific knowledge, it improves factual accuracy and reduces hallucinations, especially in high-stakes fields like medicine, surpassing Graph RAG and Light RAG. Its lightweight version also doubles retrieval speed

