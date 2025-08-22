---
title: "In-depth guide to fine-tuning LLMs with LoRA and QLoRA"
source: "https://www.mercity.ai/blog-post/guide-to-fine-tuning-llms-with-lora-and-qlora"
author:
published: 2025-07-11
created: 2025-07-01
description: "In this blog we provide detailed explanation of how QLoRA works and how you can use it in hugging face to finetune your models. We also touch on the lastest quantization and LoRA based training methods!"
tags:
  - "clippings"
---
![](https://cdn.prod.website-files.com/61b1b0f3cfbb813f0495d1f9/61d5ae26c987d76de2556cd2_BG%2020-min.png) ![](https://cdn.prod.website-files.com/61b1b0f3cfbb813f0495d1f9/61d5ae26112cd59bc0ecef4a_BG%2021-min.png)

像 GPT-4 这样的语言模型已成为自然语言处理行业构建产品和应用程序的事实上的标准。这些模型能够执行大量任务，并且可以使用 [提示工程技术](https://www.mercity.ai/blog-post/advanced-prompt-engineering-techniques) 轻松适应新任务。但这些模型在训练方面也带来了巨大挑战。像 GPT-4 这样的大型模型训练成本高达数百万美元，因此我们在生产环境中使用较小的模型。

但另一方面，较小的模型无法泛化到多个任务，最终我们会为多个用户的多个任务准备多个模型。这就是像 LoRA 这样的 PEFT 技术发挥作用的地方，与完全微调大型模型相比，这些技术能让你更高效地训练大型模型。在本博客中，我们将详细介绍 LoRA、QLoRA 以及其他特别从 LoRA 衍生出来的流行技术。

## 什么是 PEFT 微调？

[PEFT 微调](https://www.mercity.ai/blog-post/fine-tuning-llms-using-peft-and-lora) 即参数高效微调，是一组微调技术，它能让你比常规训练更高效地对模型进行微调与训练。PEFT 技术通常通过减少神经网络中可训练参数的数量来发挥作用。最著名且常用的 PEFT 技术有前缀微调（Prefix Tuning）、P-tuning、LoRA 等。LoRA 可能是使用最广泛的一种。LoRA 也有许多变体，如 QLoRA 和 LongLoRA，它们各有其应用场景。

### 为什么要使用 PEFT 微调？

使用 PEFT 技术有很多原因，它们已成为微调 LLMs 和其他模型的首选方法。但以下是一些即使是企业和大型公司也喜欢使用这些方法的原因。

#### 节省时间

随着可训练参数数量的减少，你在训练上花费的时间也会减少。但这只是其中一方面。可训练参数减少后，你可以更快地训练模型，结果也能更快地测试模型。有了更多的时间，你可以把它花在测试不同的模型、不同的数据集、不同的技术等等上面。

此外，有了更多时间，你可以将模型训练更长的时间，从而大幅降低损失，同时随着 PEFT 技术针对内存使用进行了大量优化，批大小也会增加。

#### 节省资金

这是不言而喻的，但 PEFT 可以为你节省大量的计算成本。如前所述，由于进行了大量的内存优化，你无需租用具有大量 VRAM 的实例，因为你可以在较小的 VRAM 中容纳更大的批次。这在计算方面节省了资金，并使你能够利用更大批次大小的优势在大得多的数据集上进行训练。

#### 轻松构建多租户架构服务

如前所述，由于大语言模型（LLMs）的规模变得如此之大，服务和处理起来非常复杂，几乎不可能为每个用户训练专门的模型。如果你有多个用户，那么要么每次有新用户进来时都承担微调新模型这个复杂的任务，要么就只在新数据上为新用户微调同一个模型。这两种方法都有各自的问题，如果你为每个用户都微调一个新模型，会带来更高的准确性，但你必须处理庞大的模型，将它们加载到内存中、存储它们、处理它们等等，这简直是架构上的噩梦，而且如果犯一个小错误就可能导致大问题。为所有用户训练同一个模型要容易得多，但模型的准确性会大幅下降。

![](https://cdn.prod.website-files.com/640f56f76d313bbe39631bfd/65358e23a1841692bce3fdde_pZkMHXa1_5JDK-50qaL33QmXp3A_QHlenbmoeLOLZjeAwjV_4JMC258-7ft_nQP0SWwDiGjpdWAwzXoHdH9e24xopk6UPhjVfKqcpGpgmDDJ5KVju6bhb7i1z7qa8SO3MW2RPjQalY3yC66Yx3arBco.png)

另一方面，PEFT 微调兼收并蓄，让你能够构建小型 **适配器** ，将其与模型配对以获得定制化结果。这些适配器可以针对特定数据集或特定用户进行微调。这些适配器非常小，只有 6MB - 8MB，你只需将这些适配器应用于大型模型，在生产环境中这样做要快得多。

![](https://cdn.prod.website-files.com/640f56f76d313bbe39631bfd/65358e237ecc65ca6bff3e86_pIAt6GubybV8S1uucMNhmD6r3YgBFMH10yfupxAN--0sMvjakr6kerdmhrxFpzh4NySfz83mDUHEXQXSVRCZ9cYGUJkraPYJVxNdq63WzpO30yHRr7jNQBfh9fJ0oxD7jzVPUTHZpQY536m2xoLn_D4.png)

## LoRA 微调

LoRA 是最流行且可能是使用最广泛的参数高效微调（PEFT）技术，但它早在 2021 年就在\[这篇\](https://arxiv.org/abs/2106.09685)论文中发布了。LoRA 更像是一种适配器方法，它在模型中引入新参数，通过这些新参数来训练模型。关键在于如何引入新参数并将其合并回模型，\*\*而不\*\*增加模型中的参数总数。

### LoRA 是如何工作的？

如前所述，LoRA 是一种基于适配器的方法，但仅在训练步骤中添加新参数，这些参数并非作为模型的一部分引入。这使得模型大小完全保持不变，同时仍能提供参数高效微调的灵活性。以下是对其工作原理的更详细解释。

LoRA 的工作原理是将权重更新矩阵分解为较小的矩阵，并使用它们来训练模型。看一下下面的图，ΔW <sub>AxB </sub> 是权重更新矩阵，即反向传播中学习到的变化矩阵，其大小与我们微调模型时需要更新的参数数量相同。这个矩阵，或者任何矩阵，都可以表示为一组较小的矩阵，这里表示为 A 和 B， *r* 是它们的秩。 *r* 参数控制较小矩阵的大小。

然后，可以使用这些较小的矩阵通过常规反向传播来训练模型，但更新的是较小矩阵中的参数，而不是直接在模型中更新。我们基本上是通过较小的矩阵来学习ΔW。然后，可以将这些较小的矩阵相乘，以恢复原始矩阵。由于这些矩阵要小得多，此过程使用的参数更少，因此计算资源也少得多。这还会导致更小的检查点，因为无需存储整个模型，只需存储较小的矩阵即可。

![](https://cdn.prod.website-files.com/640f56f76d313bbe39631bfd/65358e2365a382945ff60dd2_oqMjFlY7MeAQFHy2IvqYbKYLaAHWFt2mxQXorwdv0ohg-OhpmF5X5MltxKvE6CgXW9OAyUFplEMKFxGR01DBUQEivGUX44l4tzKQoQWBniwVz5bGR8awfBBJhlOwJ-tqQXPdoAd86E2Ys-GBSCPvdmk.png)

### 使用 HuggingFace 进行 LoRA 微调

要使用 HuggingFace 实现 LoRA 微调，你需要使用 [PEFT 库](https://pypi.org/project/peft/) 将 LoRA 适配器注入模型，并将它们用作更新矩阵。

```python
from transformers import AutoModelForCausalLM
from peft import get_peft_config, get_peft_model, LoraConfig, TaskType

model = AutoModelForCausalLM.from_pretrained(model_name_or_path, device_map="auto", trust_remote_code=True) # load the model

peft_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM, inference_mode=False, r=32, lora_alpha=16, lora_dropout=0.1,
    target_modules=['query_key_value'] # optional, you can target specific layers using this
) # create LoRA config for the finetuning

model = get_peft_model(model, peft_config) # create a model ready for LoRA finetuning

model.print_trainable_parameters() 
# trainable params: 9,437,184 || all params: 6,931,162,432 || trainable%: 0.13615586263611604
```

完成此操作后，你就可以像平常一样训练模型了。但这一次，与平常相比，它所需的时间和计算资源要少得多。

## QLoRA 微调

QLoRA 是一种微调技术，它将高精度计算技术与低精度存储方法相结合。这有助于在确保模型仍具有高性能和准确性的同时，保持模型规模较小。

### QLoRA 是如何工作的？

![](https://cdn.prod.website-files.com/640f56f76d313bbe39631bfd/65358e232cf7056045158369_kAizskrUxOXNivr5h5E4TCPBYNX_J8JTGZKYgd7lVTFSGPKHrZKvQZp1faQG5KfNmIsf_G-m2QzJf6Z5wuaPpURbeXo4VioqFcL8aNHccc3Pzwzlf8QLXI9maqVYxgBnRBOiUYDxKRbUex2iXTODbMA.png)

QLoRA 通过引入 3 个有助于减少内存同时保持相同质量性能的新概念来工作。它们是 **4 位正常浮点** 、 **双量化** 和 **分页优化器** 。让我们详细谈谈这 3 个非常重要的概念。

#### 4位正常浮点数

4 位 NormalFloat 或 NF 是一种基于分位数量化技术构建的全新的 *信息理论最优* 数据类型。4 位 NF 的工作原理是在 0 到 1 的分布中估计 2 <sup>k</sup> + 1（k 为位数）个分位数，然后将其值归一化到\[-1, 1\]范围内。得到这些之后，我们还可以将神经网络权重归一化到\[-1, 1\]范围，然后量化为我们在步骤 2 中得到的分位数。

以下是分位数量化的一个示例

![](https://cdn.prod.website-files.com/640f56f76d313bbe39631bfd/65358e23515cf733600388f4_7xYu7pLVD0_QDWRkB3GtH8WC4HZIyQBrfYpeESnmcLUQltE1FpKFno3USa6R6NhgHD11UOTssJbikqIa2hSB4P_2okBSyVO8pxxmDZbJ40LKbp323ayLshQ4XE59BYV_2Q5lYycQFrnKfFWS_CmCeKQ.png)

你可以看到存在数据被量化的“桶”或“箱”。数字2和3都落入同一个分位数，即2。这种量化过程通过“四舍五入”到最接近的分位数，使你能够使用更少的数字。

#### 双重去量化

双量化是在 4 位 NF 量化的量化过程中对所使用的量化常数进行量化的过程。如论文中所述，这一点并不重要，但平均每个参数可以节省 0.5 比特。这对该过程有帮助，因为 QLoRA 使用逐块 k 比特量化，这意味着不是将所有权重一起量化，而是创建多个权重块，然后对这些块进行独立量化。

这种逐块方法会导致创建多个量化常量，然后这些常量又可以再次进行量化以节省更多空间。这是可行的，因为量化常量的数量较少，因此不需要大量的计算或存储。

#### 使用 LoRA 微调减少错误

如前所示，分位数量化会为大范围的数字创建桶或箱。此过程会导致将多个不同的数字放入同一个桶中，例如，在量化过程中，数字2和3可能会被转换为3。这会在权重反量化过程中引入1的误差。

以下是在神经网络权重的更大分布上这些误差的图形表示。

![](https://cdn.prod.website-files.com/640f56f76d313bbe39631bfd/65358e23a61fd7828ed079ca_MZdJdD5ihusfmdnu1iO-YUGQ0KaM4PZXWCFu5z4hOi6k8bCR41fMHVU-JNKu11M9t9BOrVq-cYwZysc0xwIt5LV5SGafLhggn-mvA_p3aPB9bc2Yzjpx0qALyVguZ23AEWYXnx5LYvyxIWNxwPMH4dc.png)

这个错误就是为什么 QLoRA 更像是一种微调机制，而不是一种独立的量化策略。虽然它可用于 4 位推理。当使用 QLoRA 进行微调时，我们采用了 LoRA 微调机制，即创建两个较小的权重更新矩阵，然后用它们来更新神经网络的权重。在这里，我们将 LoRA 矩阵保持在更高精度的格式，如脑浮点 16（bfloat16）或浮点 16，并且在反向传播和前向传播过程中，网络的权重也会进行反量化。所以实际的训练仍然是以更高精度的格式进行，但存储仍采用较低精度。这就导致了量化误差的出现，但模型训练本身能够弥补量化过程中的这些低效问题。

因此，使用更高精度的 LoRA 训练有助于模型了解并减少量化误差。

### QLoRA 与 LoRA 有何不同？

QLoRA 和 LoRA 都是微调技术，但 QLoRA 使用 LoRA 作为辅助手段来修复量化误差过程中引入的错误。LoRA 本身更像是一种独立的微调技术。

### 使用 HuggingFace 进行 QLoRA 微调

要使用 HuggingFace 进行 QLoRA 微调，你需要安装 [BitsandBytes 库](https://pypi.org/project/bitsandbytes/) 和 PEFT 库。BitsandBytes 库负责 4 位量化以及整个低精度存储和高精度计算部分。PEFT 库将用于 LoRA 微调部分。

```python
import torch
from peft import prepare_model_for_kbit_training, LoraConfig, get_peft_model
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

model_id = "EleutherAI/gpt-neox-20b"
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
) # setup bits and bytes config

model = AutoModelForCausalLM.from_pretrained(model_id, quantization_config=bnb_config, device_map={"":0})

model.gradient_checkpointing_enable()
model = prepare_model_for_kbit_training(model) # prepares the whole model for kbit training

config = LoraConfig(
    r=8, 
    lora_alpha=32, 
    target_modules=["query_key_value"], 
    lora_dropout=0.05, 
    bias="none", 
    task_type="CAUSAL_LM"
)

model = get_peft_model(model, config) # Now you get a model ready for QLoRA training
```

然后你可以再次使用 HF 训练器进行正常训练。查看这个 [Colab 笔记本](https://colab.research.google.com/drive/1VoYNfYDKcKRQRor98Zbf2-9VQTtGJ24k?usp=sharing#scrollTo=FCc64bfnmd3j) 作为 QLoRA 训练的指南。

## QLoRA 与标准微调对比

在论文中，研究人员对 QLoRA、LoRA 以及网络的完全微调进行了非常详细的比较。

![](https://cdn.prod.website-files.com/640f56f76d313bbe39631bfd/65358e23a61fd7828ed079d3_iFgh5dLJlkXuia76nlzEeGFJaHuZk0d27_qMY4dIPcigc3lBDNZnnyybIXrjzCFDJ4aOLC5OU5eUa3m5anHnq7F70bNGG8ql9DMFjaHT2nlgBAqqft5ojwrnILo1Q1UfdbtGqth8lFumRthtk281fvA.png)

如你在上述表格中所见，在使用 QLoRA 进行训练时，T5 模型家族的性能没有任何损失，甚至在使用双重量化时，我们也没有看到任何重大差异。一个显著的区别是所需的 LoRA 适配器数量。在论文中，作者提到与普通的 LoRA 微调相比，他们在 QLoRA 微调中需要更多的 LoRA 适配器。作者建议在所有线性变压器模块以及查询、键和值层上应用 LoRA 适配器。

即使对于大得多的语言模型，性能仍然相同：

![](https://cdn.prod.website-files.com/640f56f76d313bbe39631bfd/65358e233b0593b2e2dce709_-cLgG3H7dbGRuFqh3m0OHfHHqnXNC9qoGEk7ANjagwAiex64QT1ayNQ86Jcfa1qOjuSqSy8BzVVdsBXyKDNMGlm_X1hCnhyNnCpY_W6ycUn2UYvYT0kgvNlcmnXulLvRbyGDn64YoexaSMMYTr4-7Mk.png)

因此，作者在基础 LLaMA 模型之上训练了一个模型，即 [羊驼（Guanaco）](https://huggingface.co/timdettmers/guanaco-65b) 。这是一个拥有 330 亿参数的模型，在 OASST1 数据集上进行训练。在发布时，它成为了一个先进的模型，相对于 ChatGPT 达到了 **99.3%** 的性能。尽管其他模型如 Vicuna 13B 参数较少，但由于使用了 4 位精度，羊驼 33B（Guanaco33B）比 13B 模型使用的内存更少。

## LoRA 微调的其他变体

### QA LoRA

问答 LoRA 是基于 QLoRA 构建的另一种微调技术，在\[这篇\]论文中被提出。问答 LoRA 主要是为微调扩散模型而发布的，但和 LoRA 一样，它也可以很容易地推广到训练任何类型的模型。

QLoRA 和 QALoRA 的区别在于，QALoRA 是量化感知的，这意味着在微调过程中，LoRA 适配器的权重与模型的权重一起被量化。这有助于更高效地训练，因为在反向传播过程中无需进行转换步骤来更新模型。

![](https://cdn.prod.website-files.com/640f56f76d313bbe39631bfd/65358e23d7d446708a1eec24_mR-H3Wh2jk0zRKaY7FQCRQANOZNaQNV62RwDzf28bcUQBHHg5ei75Q0M1lHLqL-VTAjiWCHGhzzwUhFbZYso-uVZ-sTabL78mpR3eEAmLAZNEmthk8n9oDaCPKdf4r0KaZjLPs3sbxBn-fF0r7Ggfuk.png)

### 长 LoRA

![](https://cdn.prod.website-files.com/640f56f76d313bbe39631bfd/65358e2317daafaf293fb79c_wSYLsK_nzksoc9Wzl4UjQW68U8F451DuQCVh7_TzN_icR9iRnzOx0v26S0rEcMgbDgYprqBBcoU8FQhqGo9j-9w9WHr-O04EBoukXwwVXAa3GFkm4te8ElCs4nHEEh1T-xurHGQRQiVzfLjCz8b0VD8.png)

[LongLoRA](https://arxiv.org/abs/2309.12307) 是 LoRA 微调技术的又一变体，但该技术专门用于训练更长上下文模型。LongLoRA 通过使用一种称为 **SHIFT SHORT ATTENTION** 的方法来工作。此方法会创建令牌的块或组，其中注意力是独立计算的。由于工作负载分布，这种方法使 LongLoRA 能够扩展到长得多的上下文。

与此同时，作者表明，为使该方法正常工作，在归一化层和嵌入层也需要使用 LoRA。

### AdaLoRA

在传统的 LoRA 中，你为每一层固定一个秩 r。但不同的层对模型性能的贡献不同。

AdaLoRA（自适应 LoRA）所做的是在训练期间根据权重矩阵的重要性动态分配参数预算，即秩。这避免了 LoRA 的统一秩分配，对于重要性不同的层来说，这种统一分配可能不是最优的。重要的层（通常是顶层的 Transformer 层）会获得更高的秩，而不太关键的层则会被裁剪。

它通过模仿权重矩阵的奇异值分解（SVD）算法并通过其奇异值更新权重来实现这一点：

![](https://cdn.prod.website-files.com/640f56f76d313bbe39631bfd/682f9f271dfebe56a0445a06_AD_4nXf5OKq5Se4xLnekVb5kZrxEK298VQiyXn_CTw6pqd7Q31KoAq1o-8F2kwncU9jbeSC-w5_nFtCyqq_l-xPwGA1_LyMWJBXR1SbGbTvIeEbXOG2IcJsyoK3V2x88J8RXyfi8002iDw.png)

### DoRA

[可分解秩适应（DoRA）](https://arxiv.org/pdf/2402.09353) 将高秩的 LoRA 层分解为结构化的单秩组件，允许在训练期间根据它们对特定任务的重要性对参数预算进行动态剪枝，从而充分利用有限的参数预算。它引入了 r′对单秩矩阵，每对矩阵都充当一个 LoRA 组件。在训练过程中，DoRA 评估每个组件对整体性能的贡献，并剪枝贡献较小的组件。

![](https://cdn.prod.website-files.com/640f56f76d313bbe39631bfd/682f9f270f51d8769902a253_AD_4nXe557d4mk2wd2AUnZITtRY6PcjRtnLzKQyj8HX7EBHfMUIblwR4b4UTCZHa6OC9hiDUjehweOJejBytIw_KydBH2Ca3OMIda3CfHphTc56BPiDh3RdUpUsm0VUEiB5t9BqS8kyz.png)

DoRA 没有使用标准的 LoRA 层，而是将其重新解释为：

![](https://cdn.prod.website-files.com/640f56f76d313bbe39631bfd/682f9f27cc46e85b462743ad_AD_4nXc41tOO91LNa9L7XwHMl_2MzsU1-LAi4kUNx18N6Jr261oEwRVATpTTJcOgXnf_TQjj5moXLVR7BXVk5BfQYQAASi0QuTvUUs5HHOaTttwSkYZWxpdol5KIf6mU25tk4095c7Allg.png)

这里 r′表示 LoRA 组件的数量。一个 LoRA 组件是由 A、B 和 c 组成的三元组，其中 A 和 B 是单秩矩阵，形状分别为 d×1 和 1×d。c 是用于修剪该组件的标量，如果要修剪该组件，则将其设置为 0。

通过在 LoRA 配置中进行以下修改，DoRA 可以直接集成：

```python
config = LoraConfig(
    r=8, 
    lora_alpha=32, 
    target_modules=["query_key_value"], 
    lora_dropout=0.05, 
    bias="none", 
    task_type="CAUSAL_LM",
    use_dora=True # simply pass True here to use DoRA
)

model = get_peft_model(model, config) # Now you get a model ready for QLoRA training
```

![](https://cdn.prod.website-files.com/640f56f76d313bbe39631bfd/682f9f27b92cc05d5f1d923c_AD_4nXc0Fa-KzkKwd7i273CUbdvH-gO434ojJq89CJOzJK_B-1dfcunK2eeaRZKUA34mLGhOoVxa_uaItndXPy6YPNO40GryYXRn4AbvHLRJ2q7_yGzsLBxlkMwFuvxFtGLbZdr5Xresew.png)

## 现代量化策略（2025年5月）

以下是一些往往效果非常好的现代量化策略。

### AWQ（激活感知权重量化）

[AWQ](https://arxiv.org/pdf/2306.00978) 是一种训练后量化（PTQ）技术，旨在将大语言模型（LLMs）压缩为低比特格式，具体为 4 比特，同时不影响性能。与传统的均匀处理所有权重的量化方法不同，AWQ 能够智能地识别并保留一小部分对维持模型准确性至关重要的 *显著* 权重。

AWQ 的独特之处在于其方法，它不是直接分析权重，而是评估激活分布以确定哪些权重通道最为重要。这种方法无需反向传播或重构，使得该过程在不同领域和模态中既高效又具有高度通用性。

AWQ 在各种基准测试中始终能取得出色的结果，包括经过指令微调的和多模态的 LLMs。例如，它能在诸如 LLaMA-2 70B 这样的大型模型上实现高效的 4 位推理，与 FP16 实现方式相比，在桌面和移动 GPU 上都能实现超过 3 倍的加速。

### 仿射量化

[仿射量化（AffineQuant）](https://arxiv.org/html/2403.12544v1) 引入了一种全新的模型训练后量化（PTQ）方法，通过利用仿射变换来优化权重和激活值的分布。与传统的依赖简单缩放的方法不同，仿射量化使用变换矩阵来更精确地对齐量化前后的输出，有效减少量化误差。

通过应用仿射变换矩阵，它调整数据分布以更好地拟合量化函数，从而减少量化误差。为确保变换是可逆的，仿射量化（AffineQuant）采用渐进掩码优化方法，最初关注对角元素，然后逐渐扩展到其他元素（确保可逆性）。这种方法符合列维 - 德斯普朗克定理，保证了变换的可逆性。

![](https://cdn.prod.website-files.com/640f56f76d313bbe39631bfd/682f9f27e7a75d2528741bcb_AD_4nXdC0zY3zTJnXsuoNbGX8QC3a8vn1U4b1r8UJ3Zec42Lu0D5b3j2uQTwzp8krhvewwp6LYLqr6tnQ5egEdqBVWlncPbRRvoadQXzPBN3bEPj8Wn7advMgYKhbBo0FjAg-UdxqzLO.png)

仿射量化为大语言模型（LLMs）中的后训练量化（PTQ）设定了新标准。例如，在使用 W4A4 量化的 LLaMA2 - 7B 模型上，它实现了 15.76 的 C4 困惑度，超过了像 OmniQuant 这样的先前方法。在零样本任务中，它在 LLaMA - 30B 上使用 4/4 位量化达到了令人印象深刻的 58.61%的平均准确率，标志着相对于现有技术在性能上有显著飞跃。

### 动态4位量化

[动态 4 位量化](https://unsloth.ai/blog/dynamic-4bit) ，由 [Unsloth](https://huggingface.co/collections/unsloth/unsloth-4-bit-dynamic-quants-67503bb873f89e15276c44e7) 实现，为量化 LLMs 提供了一种灵活的方法。与静态量化方法不同，动态量化在运行时动态调整模型的精度级别，确保更好的性能和资源使用。

基于 BitsandBytes（BnB）4 位量化构建，与标准的 BnB 4 位实现相比，这种动态策略在使用多不到 10%的 VRAM 的情况下，显著提高了准确性

Unsloth 的动态 4 位量化已被证明能提供准确可靠的结果，常常优于标准的 4 位量化方法。例如，虽然标准量化可能会降低模型性能，但 Unsloth 的方法能保持高精度，同时显著减少内存使用。比如，将 Llama 3.2 Vision（11B）从 20GB 压缩到仅 6.5GB，同时保持其高精度。

如果你正在考虑为你的企业微调模型，那么你可能是对的。但数据成为了这个过程中的重要部分，看看我们的 [合成数据生成指南](https://www.mercity.ai/blog-post/using-chatgpt-to-build-synthetic-datasets) 。然而，微调后的模型有很多方法可以通过提供定制来提高你企业的性能。微调模型能帮助你根据特定需求和知识对模型进行定制。你可以使用 RAG 管道来定制模型，但有时知识量过于庞大，嵌入和相似性搜索还不够，这时就需要通过微调来进行定制了。

如果您的企业需要经过微调的模型， [尽管联系我们](https://www.mercity.ai/contacts) ，别不好意思。我们在微调各类模型方面经验丰富，从小型的 T5 模型到像 Falcon180B 这样的大型模型。各种情况我们都见过。