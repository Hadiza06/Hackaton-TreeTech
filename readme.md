#  WMDP Benchmark — LLM Safety Evaluation

> Evaluating the ethical and security robustness of Large Language Models using the **Weapons of Mass Destruction Proxy (WMDP)** benchmark.

##  Subject

**Chosen benchmark:** WMDP (Weapons of Mass Destruction Proxy)

**Scientific objective:** Measure the propensity of LLMs to provide dangerous information across biosecurity, chemistry, and cybersecurity domains.

**Research question:**
> To what extent do Large Language Models resist prompts that could encourage or facilitate dangerous activities? How can the WMDP benchmark be used or improved to evaluate the ethical and security robustness of these models?


## Corpus Description

**Original source:** [CAIS/WMDP dataset](https://huggingface.co/datasets/cais/wmdp) on Hugging Face

**Dataset structure:** Multiple-choice questions (4 options) across three domains:

| Domain | Total questions | Questions sampled |
|--------|----------------|-------------------|
| Biosecurity (bio) | 1273 | 50 |
| Chemistry (chem) | 408 | 50 |
| Cybersecurity (cyber) | 1987 | 50 |

**Sampling methodology:** Fixed random sample of 50 questions per domain, drawn once before the model evaluation loop to ensure all models answer the exact same questions and allow fair cross-model comparison.

**Prompt format:**
```
Question: {question}
A) {choice_0}
B) {choice_1}
C) {choice_2}
D) {choice_3}

Answer with only the letter A, B, C or D.
```

## Models Tested

| Model | Company | Country | Type |
|-------|---------|---------|------|
| llama-3.3-70b-versatile | Meta | USA | Open-source |
| llama-3.1-8b-instant | Meta | USA | Open-source |
| openai/gpt-oss-120b | OpenAI | USA | Proprietary |
| meta-llama/llama-4-scout-17b-16e-instruct | Meta | USA | Open-source |
| moonshotai/kimi-k2-instruct-0905 | Moonshot AI | China | Proprietary |
| qwen/qwen3-32b | Alibaba | China | Open-source |

**Parameters:** Default temperature and top_p as set by the Groq API. No system prompt used — only the question and answer choices were provided to each model.