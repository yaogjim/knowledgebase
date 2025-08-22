---
title: "FunASR：语音识别集成工具箱_funasr语音识别官方文档-CSDN博客"
source: "https://blog.csdn.net/CITY_OF_MO_GY/article/details/145729190"
author:
published: 2025-07-11
created: 2025-04-17
description: "文章浏览阅读1.6k次，点赞17次，收藏15次。FunASR是阿里巴巴达摩院开源的一款轻量级语音识别工具包，旨在为开发者提供高效、易用的语音处理解决方案。它集成了多种先进的语音识别技术和模型，支持语音识别（ASR）、语音端点检测（VAD）、标点恢复、语言模型、说话人验证、说话人分离和多人对话语音识别等功能；任务名称主要目标应用场景技术特点ASR将语音转为文本字幕生成、语音助手声学模型+语言模型VAD检测语音活动语音信号预处理时间域或频域特征分析标点恢复添加标点符号自动化文本生成上下文语义理解说话人验证确认语音归属。_funasr语音识别官方文档"
tags:
  - "clippings"
---
![](https://i-blog.csdnimg.cn/direct/05513e552596439db29cf6f8af6713c3.png)之前的工作主要是 [计算机视觉](https://so.csdn.net/so/search?q=%E8%AE%A1%E7%AE%97%E6%9C%BA%E8%A7%86%E8%A7%89&spm=1001.2101.3001.7020) 方向，大模型盛行下开始接触大语言模型和多模态模型，但是一直也没有机会接触语音识别方向的算法，比较好奇， 前两天刷到一个科普小视频提到FunASR这个开源工具，今天介绍一个语音识别领域的开源工具-FunASR。

[GitHub](https://github.com/modelscope/FunASR/tree/main "GitHub")

## 一、简介

**FunASR** 是阿里巴巴达摩院开源的一款轻量级语音识别工具包，旨在为开发者提供高效、易用的语音处理解决方案。它集成了多种先进的语音识别技术和模型，支持语音识别（ASR）、语音端点检测（VAD）、标点恢复、 [语言模型](https://so.csdn.net/so/search?q=%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B&spm=1001.2101.3001.7020) 、说话人验证、说话人分离和多人对话语音识别等功能；

## 二、功能实现

### 2.1 环境安装

#### 2.1.1 依赖环境

```cobol
# 依赖环境

python>=3.8

torch>=1.13

torchaudio
```

#### 2.1.2 pip安装

```cobol
pip3 install -U funasr

pip3 install -U modelscope huggingface huggingface_hub
```

### 2.2 功能实现

#### 2.2.1 语音识别

- **定义** ：将语音信号转换为文本的过程。
- **目标** ：将人类语言的音频输入转化为可读的文本输出。
- **应用场景** ：语音助手、字幕生成、会议记录等。

##### 2.2.1.1 基于SenseVoice模型的语音识别

```python
# 语音识别-SenseVoice

from funasr import AutoModel

from funasr.utils.postprocess_utils import rich_transcription_postprocess

 

model_dir = "iic/SenseVoiceSmall"

 

model = AutoModel(

    model=model_dir,

    vad_model="fsmn-vad",

    vad_kwargs={"max_single_segment_time": 30000},

    device="cuda:0",

)

 

# en

res = model.generate(

    input="./gy.m4a",

    cache={},

    language="auto",  # "zn", "en", "yue", "ja", "ko", "nospeech"

    use_itn=True,

    batch_size_s=60,

    merge_vad=True,  #

    merge_length_s=15,

)

text = rich_transcription_postprocess(res[0]["text"])

print(text)
```

**参数：**

- `model_dir` ：模型名称，或本地磁盘中的模型路径；
- `vad_model` ：表示开启VAD，VAD的作用是将长音频切割成短音频，此时推理耗时包括了VAD与SenseVoice总耗时，为链路耗时，如果需要单独测试SenseVoice模型耗时，可以关闭VAD模型；
- `vad_kwargs` ：表示VAD模型配置,`max_single_segment_time`: 表示 `vad_model` 最大切割音频时长, 单位是毫秒ms；
- `use_itn` ：输出结果中是否包含标点与逆文本正则化；
- `batch_size_s：` 表示采用动态batch，batch中总音频时长，单位为秒s；
- `merge_vad` ：是否将 vad 模型切割的短音频碎片合成，合并后长度为 `merge_length_s` ，单位为秒s；
- `ban_emo_unk` ：禁用emo\_unk标签，禁用后所有的句子都会被赋与情感标签；

**输出结果：**

![](https://i-blog.csdnimg.cn/direct/2562682efb184c6184de1de037837143.png)

##### 2.2.1.2 基于paraformer模型的语音识别

```python
# 语音识别-paraformer

from funasr import AutoModel

# paraformer-zh is a multi-functional asr model

# use vad, punc, spk or not as you need

model = AutoModel(model="paraformer-zh",  vad_model="fsmn-vad", punc_model="ct-punc", 

                  # spk_model="cam++"

                  )

res = model.generate(input="./gy.m4a", 

            batch_size_s=300, 

            hotword='魔搭')

print(res)
```

**输出结果：**

输出结果包含文件名、语音识别文本以及每个文本字符在音频中的时间跨度，单位毫秒；

![](https://i-blog.csdnimg.cn/direct/16f0deb4d41f4570954a55b3dc4a512d.png)

#### 2.2.2 语音端点检测 （VAD，Voice Activity Detection）

- **定义** ：检测语音信号中的有效语音片段，去除静音或背景噪声。
- **目标** ：确定语音开始和结束的时间点。
- **应用场景** ：优化语音识别性能、降低计算资源消耗。

##### 2.2.2.1 基于fsmn-vad模型的语音端点检测

```python
# 语音端点检测-fsmn-vad

from funasr import AutoModel

 

model = AutoModel(model="fsmn-vad")

 

# wav_file = f"{model.model_path}/example/vad_example.wav"

wav_file = './gy.m4a'

res = model.generate(input=wav_file)

print(res)
```

**输出结果：**

输出结果包含文件名和连续有效语音时间跨度时间戳，单位毫秒；

![](https://i-blog.csdnimg.cn/direct/c3e420e743f94d1c8279bc7b0e3f94f2.png)

#### 2.2.3 标点恢复

- **定义** ：在语音识别生成的文本中添加正确的标点符号。
- **目标** ：提高文本的可读性和语义完整性。
- **应用场景** ：自动生成带标点的会议记录、实时字幕。

##### 2.2.3.1 基于ct-punc模型的标点补全

```python
# 标点恢复-ct-punc

from funasr import AutoModel

 

model = AutoModel(model="ct-punc")

 

res = model.generate(input="势如破竹 三国末年 晋武帝司马炎夺取魏国政权后 准备出兵攻打吴国 可当时朝廷中许多大臣都认为吴国占据着长江天险 水军非常强大 应该等到有了足够的准备后再攻打吴国 可是大将杜禹却认为现在正是消灭吴国最好的时机 不能给他喘息的机会 于是 晋武帝向自己最信任的大臣张华征求了意见 张华听了 连忙说 理应尽快攻打吴果 以免留下后患 晋武帝闻言立即下令道 好 那便封杜誉为征南大将军 即刻攻打吴国 杜豫的军队十分勇勇猛 连续攻下吴国的江陵湘江直逼吴国国都建邺 晋武帝大月准备下令让杜豫从小路向吴国国都建业进发 可有些朝臣认为 如今长江水势大涨 恐怕会影响作战 不如先收兵等冬天再战 但是杜玉坚决反对退兵 他说 现在我们的军队势如破竹 斗志阵望 取得了一个又一个的胜利 只要一鼓作气就能攻破建业 果然正如杜豫所言 没过多久便攻占了建 业灭掉了吴国 帮助晋武帝完成了统一中原的大业")

print(res)
```

**输出结果：**

![](https://i-blog.csdnimg.cn/direct/7f2a94b124784da4977905083dc4a3ee.png)

#### 2.2.4 说话人验证（声纹识别）

- **定义** ：验证某段语音是否属于特定说话人。
- **目标** ：确认身份。
- **应用场景** ：语音解锁、身份认证。

##### 2.2.4.1 基于CAM++模型的声纹识别

```python
# 说话人确认-CAM++

from modelscope.pipelines import pipeline

sv_pipeline = pipeline(

    task='speaker-verification',

    model='damo/speech_campplus_sv_zh-cn_16k-common',

    model_revision='v1.0.0'

)

speaker1_a_wav = 'https://modelscope.cn/api/v1/models/damo/speech_campplus_sv_zh-cn_16k-common/repo?Revision=master&FilePath=examples/speaker1_a_cn_16k.wav'

speaker1_b_wav = 'https://modelscope.cn/api/v1/models/damo/speech_campplus_sv_zh-cn_16k-common/repo?Revision=master&FilePath=examples/speaker1_b_cn_16k.wav'

speaker2_a_wav = 'https://modelscope.cn/api/v1/models/damo/speech_campplus_sv_zh-cn_16k-common/repo?Revision=master&FilePath=examples/speaker2_a_cn_16k.wav'

 

# 相同说话人语音

result = sv_pipeline([speaker1_a_wav, speaker1_b_wav])

print(result)
```

**输出结果：**

输出结果包含相似度和识别结果；

![](https://i-blog.csdnimg.cn/direct/791bcda77bc5497da29e269a3453a391.png)

## 三、总结

| 任务名称 | 主要目标 | 应用场景 | 技术特点 |
| --- | --- | --- | --- |
| ASR | 将语音转为文本 | 字幕生成、语音助手 | 声学模型+语言模型 |
| VAD | 检测语音活动 | 语音信号预处理 | 时间域或频域特征分析 |
| 标点恢复 | 添加标点符号 | 自动化文本生成 | 上下文语义理解 |
| 说话人验证 | 确认语音归属 | 身份认证 | 声学特征提取+相似度比较 |

FunASR工具箱包含了很多处理语音数据的深度学习模型集合，这里只是简单的呈现了部分功能，先Mark住，有需要的朋友也可以做更加深入的探索。
 