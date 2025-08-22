---
title: "vidore/colqwen-omni-v0.1 · Hugging Face"
source: "https://huggingface.co/vidore/colqwen-omni-v0.1"
author:
published: 2025-07-11
created: 2025-07-18
description: "We’re on a journey to advance and democratize artificial intelligence through open source and open science."
tags:
  - "clippings"
---
[Edit model card](https://huggingface.co/vidore/colqwen-omni-v0.1/edit/main/README.md)

## ColQwen2.5-Omni: Visual+Audio Retriever based on Qwen2.5-Omni-3B-Instruct with ColBERT strategy

Check out the release [blogpost](https://huggingface.co/blog/manu/colqwen-omni-omnimodal-retrieval) for in-depth explanations and tutorials!

ColQwen-Omni is a model based on a novel model architecture and training strategy based on Omnimodal Language Models to efficiently index documents from their visual features. It is a Qwen2.5-Omni-3B extension that generates [ColBERT](https://arxiv.org/abs/2004.12832) - style multi-vector representations of text and images. It was introduced in the paper [ColPali: Efficient Document Retrieval with Vision Language Models](https://arxiv.org/abs/2407.01449) and first released in [this repository](https://github.com/ManuelFay/colpali)

![](https://github.com/illuin-tech/colpali/blob/main/assets/colpali_architecture.webp?raw=true)

## Version specificity

This model takes dynamic image resolutions in input and does not resize them, changing their aspect ratio as in ColPali. Maximal resolution is set so that 1024 image patches are created at most. Experiments show clear improvements with larger amounts of image patches, at the cost of memory requirements.

This version is trained with `colpali-engine==0.3.11`.

Data is the same as the ColPali data described in the paper.

## Model Training

### Dataset

The audio retrieval capabilities are acquired in a 0-shot capacity, as the entire training data is purely image-text matching. Yhe audio and vision tower are frozen during training.

Our training dataset of 127,460 query-page pairs is comprised of train sets of openly available academic datasets (63%) and a synthetic dataset made up of pages from web-crawled PDF documents and augmented with VLM-generated (Claude-3 Sonnet) pseudo-questions (37%). Our training set is fully English by design, enabling us to study zero-shot generalization to non-English languages. We explicitly verify no multi-page PDF document is used both [*ViDoRe*](https://huggingface.co/collections/vidore/vidore-benchmark-667173f98e70a1c0fa4db00d) and in the train set to prevent evaluation contamination. A validation set is created with 2% of the samples to tune hyperparameters.

*Note: Multilingual data is present in the pretraining corpus of the language model and most probably in the multimodal training.*

## Usage

Make sure `colpali-engine` is installed from source or with a version superior to 0.3.11.

```bash
pip install git+https://github.com/illuin-tech/colpali
```

```python
import torch
from PIL import Image
from transformers.utils.import_utils import is_flash_attn_2_available
from tqdm import tqdm
from torch.utils.data import DataLoader

from colpali_engine.models import ColQwen2_5Omni, ColQwen2_5OmniProcessor

model = ColQwen2_5Omni.from_pretrained(
    "vidore/colqwen-omni-v0.1",
    torch_dtype=torch.bfloat16,
    device_map="cuda",  # or "mps" if on Apple Silicon
    attn_implementation="flash_attention_2" # if is_flash_attn_2_available() else None,
).eval()
processor = ColQwen2_5OmniProcessor.from_pretrained("vidore/colqwen-omni-v0.1")

dataset = load_dataset("eustlb/dailytalk-conversations-grouped", split="train[:500]")
audios = [x["array"] for x in dataset["audio"]]

dataloader = DataLoader(
    dataset=audios,
    batch_size=2,
    shuffle=False,
    collate_fn=lambda x: processor.process_audios(x),
)

ds  = []
for batch_doc in tqdm(dataloader):
    with torch.no_grad():
        batch_doc = {k: v.to(model.device) for k, v in batch_doc.items()}
        embeddings_doc = model(**batch_doc)
    ds.extend(list(torch.unbind(embeddings_doc.to("cpu"))))

def get_results(query: str, k=10):
    batch_queries = processor.process_queries([query]).to(model.device)

    # Forward pass
    with torch.no_grad():
        query_embeddings = model(**batch_queries)

    scores = processor.score_multi_vector(query_embeddings, ds)
    # get top-5 scores
    return scores[0].topk(k).indices.tolist()

res = get_results("A person looking for a taxi")

# In colab
display(Audio(dataset[res[0]]["audio"]["array"], autoplay=True, rate=dataset[res[0]]["audio"]["sampling_rate"]))
```

## Contact

- Manuel Faysse: [manuel.faysse@illuin.tech](https://huggingface.co/vidore/)
- Antonio Loison: [antonio.loison@illuin.tech](https://huggingface.co/vidore/)

## Citation

If you use any datasets or models from this organization in your research, please cite the original dataset as follows:

```
@misc{faysse2024colpaliefficientdocumentretrieval,
  title={ColPali: Efficient Document Retrieval with Vision Language Models}, 
  author={Manuel Faysse and Hugues Sibille and Tony Wu and Bilel Omrani and Gautier Viaud and Céline Hudelot and Pierre Colombo},
  year={2024},
  eprint={2407.01449},
  archivePrefix={arXiv},
  primaryClass={cs.IR},
  url={https://arxiv.org/abs/2407.01449}, 
}
```

Downloads last month

125

Inference Providers [NEW](https://huggingface.co/docs/inference-providers)[Visual Document Retrieval](https://huggingface.co/tasks/visual-document-retrieval "Learn more about visual-document-retrieval")

## Model tree for vidore/colqwen-omni-v0.1

Base model

[Qwen/Qwen2.5-Omni-3B](https://huggingface.co/Qwen/Qwen2.5-Omni-3B)

Finetuned

[vidore/colqwen2.5omni-base](https://huggingface.co/vidore/colqwen2.5omni-base)

Finetuned

([1](https://huggingface.co/models?other=base_model:finetune:vidore/colqwen2.5omni-base))

this model