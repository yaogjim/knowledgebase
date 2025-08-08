---
title: "微软发布原生1-bit大语言模型bitnet-b1.58-2B-4T"
source: "https://x.com/karminski3/status/1912287572065415582"
author:
  - "[[@karminski3]]"
created: 2025-04-16
description:
tags:
  - "@karminski3 #AI #大语言模型 #低精度神经网络 #效率提升 #端侧AI"
---
**karminski-牙医** @karminski3 [2025-04-15](https://x.com/karminski3/status/1912287572065415582)

微软研究院整了个活，发布了个原生 1-bit 的大语言模型 —— bitnet-b1.58-2B-4T

有啥意义吗？有的，这个模型虽然将权重量化到超低精度（实际是1.58位，权重只有{-1, 0, +1}三个值），但它在性能上几乎能与其它2B参数规模的全精度模型相媲美。

与传统模型相比，这个1-bit模型带来了惊人的效率提升：

\- 内存占用只有0.4GB（其他同规模模型需要2-4.8GB）

\- CPU推理延迟只有29ms（其他模型为41-124ms）

最厉害的是，这个模型不是后期量化的，而是从头就用1-bit精度训练的，在4万亿token上训练后，各项测试成绩平均达到54.19分，几乎与最佳的同类模型Qwen2.5-1.5B（55.23分）相当

这证明了低精度神经网络也能达到与全精度模型相当的效果，同时大幅提升效率，为轻量级AI应用（尤其是端侧）开辟了新可能

同时，这个模型有专门配套推理框架 BitNet，这个框架原生就是为CPU推理准备的

模型地址：http://huggingface.co/microsoft/bitnet-b1.58-2B-4T…

BitNet框架地址：http://github.com/microsoft/BitNet…

![Image](https://pbs.twimg.com/media/GomgvnuXsAAOq5w?format=jpg&name=large) ![Image](https://pbs.twimg.com/media/GomgvnqWcAAmDnF?format=jpg&name=large)

---

**曾骁 そーくん Zeng Xiao** @xiaoschannel [2025-04-15](https://x.com/xiaoschannel/status/1912290607453860305)

之前就看过bitnet，好奇，有三进制硬件吗？是不是实际上还是要两个2进制位模拟，还是怎么，研发一套专门的，通过一次计算多个位来实现的方法？

我的理解现在量化一般是分部件决定多少位？所以合起来平均值可能不是一个整数？

不过量化我真的不太懂

---

**杀马特副教授** @Maxwell\_SCU [2025-04-16](https://x.com/Maxwell_SCU/status/1912319442228593104)

我一直在思考这种模型有什么用，直到发现某些离线玩具用这种性能的模型能够大大的提高可玩性。

---

**qqqqqf** @qqqqqf5 [2025-04-16](https://x.com/qqqqqf5/status/1912301177678823546)

能测一下o1pro吗，好奇openai现最强模型什么实力

---

**yibuerbu** @xybuyibuer [2025-04-15](https://x.com/xybuyibuer/status/1912290464709189793)

微软的模型… 一般都要加个？号，Phi系列就是这样

---

**熵增，复利，博弈** @chaojidigua [2025-04-15](https://x.com/chaojidigua/status/1912290251311312968)

这个是发展方向！😅