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

## How to Reproduce

### 1. Clone the repository
```
git clone https://github.com/your-username/demo_wmdp.git
cd demo_wmdp
```

### 2. Install dependencies
```
pip install groq python-dotenv datasets requests matplotlib
```

### 3. Configure API key
Create a `.env` file at the root of the project:
```
GROQ_API_KEY=your_api_key_here
```

### 4. Run the benchmark
```
python run.py
```
Results are saved in `results.json`.

### 5. Analyze results
```
python analyze.py
```
Generates scores, rankings and PNG visualizations.

### 6. Launch the ELK stack
```
docker-compose up -d
python ingest.py
```
Then open `http://localhost:5601` to access the Kibana dashboard.

## Credits

### References
- [WMDP Benchmark — CAIS](https://github.com/centerforaisafety/wmdp)
- [WMDP Dataset — Hugging Face](https://huggingface.co/datasets/cais/wmdp)
- [Groq API](https://console.groq.com)
- [Elastic Stack 8.12.0](https://www.elastic.co)

### Models
- [Llama 3.3 70b & Llama 3.1 8b — Meta AI](https://ai.meta.com)
- [Llama 4 Scout — Meta AI](https://ai.meta.com)
- [GPT-OSS 120b — OpenAI](https://openai.com)
- [Kimi K2 — Moonshot AI](https://www.moonshot.cn)
- [Qwen3 32b — Alibaba](https://qwenlm.github.io)

### Team
- Hackathon TreeTech — B2 ECE Paris — S2 2025/2026