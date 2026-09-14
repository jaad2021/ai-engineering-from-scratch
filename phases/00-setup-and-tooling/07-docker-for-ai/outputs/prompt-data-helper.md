# Prompt Data Helper

## Dataset Loading

Use Hugging Face Datasets to load datasets.

```python
from datasets import load_dataset

dataset = load_dataset("stanfordnlp/imdb", split="train")
```

## Streaming Large Datasets

Use streaming=True for datasets that are too large to load into memory.

## Dataset Formats

- CSV — simple tabular data
- JSON — structured data and APIs
- Parquet — efficient storage for AI/ML datasets

## Data Splitting

A common split is 80% training, 10% validation, and 10% testing.

Use a fixed random seed such as 42 for reproducible splits.

## Hugging Face Cache

Downloaded Hugging Face models are cached locally under ~/.cache/huggingface/hub/.
