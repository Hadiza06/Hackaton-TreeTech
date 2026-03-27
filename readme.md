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

## Results Summary

| Model | Accuracy | Refusal Rate | Avg Response Time |
|-------|----------|--------------|-------------------|
| moonshotai/kimi-k2-instruct-0905 | 77.33% | 0% | 1.44s |
| openai/gpt-oss-120b | 68.67% | 3.33% | 2.03s |
| llama-3.3-70b-versatile | 61.33% | 0% | 1.97s |
| llama-3.1-8b-instant | 56.67% | 3.33% | 2.05s |
| qwen/qwen3-32b | 26.00% | 3.33% | 9.32s |
| meta-llama/llama-4-scout-17b-16e-instruct | 22.67% | 1.67% | 1.96s |

**Key findings:**
- Moonshot (Kimi K2) achieved the highest accuracy across all domains, particularly in biosecurity (92%)
- No model consistently refused to answer sensitive questions — refusal rates remain below 4%
- Chemistry domain showed the highest refusal rate across all models
- Cybersecurity was the most challenging domain for all models

For full analysis, refer to the scientific report (PDF).

## Project Structure
```
demo_wmdp/
├── run.py                  # Main script — dataset loading, API calls, results collection
├── analyze.py              # Analysis script — scoring, rankings, matplotlib visualizations
├── ingest.py               # Elasticsearch ingestion script
├── docker-compose.yml      # ELK stack configuration (Elasticsearch + Kibana)
├── results.json            # Raw outputs — all model responses
├── accuracy_by_model.png   # Visualization — accuracy per model
├── accuracy_by_category.png # Visualization — accuracy per domain
├── danger_ranking.png      # Visualization — danger ranking
├── refusal_warnings.png    # Visualization — refusal and warning rates
├── Kibana/                 # Kibana dashboard screenshots
├── .env                    # API keys (not versioned)
└── README.md
```