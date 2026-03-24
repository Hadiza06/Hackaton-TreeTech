import json
from collections import defaultdict
from statistics import mean

# ── Chargement ──
with open("results.json", "r", encoding="utf-8") as f:
    results = json.load(f)

# ── Helpers ──
def by_model(data):
    grouped = defaultdict(list)
    for r in data:
        grouped[r["model"]].append(r)
    return grouped

def by_category(data):
    grouped = defaultdict(list)
    for r in data:
        grouped[r["category"]].append(r)
    return grouped

def by_model_and_category(data):
    grouped = defaultdict(list)
    for r in data:
        grouped[(r["model"], r["category"])].append(r)
    return grouped

models_data     = by_model(results)
category_data   = by_category(results)
combo_data      = by_model_and_category(results)

# ── Précision par modèle ──
print("\n══ PRÉCISION PAR MODÈLE ══")
for model, data in models_data.items():
    accuracy = mean(r["is_correct"] for r in data)
    avg_time = mean(r["response_time"] for r in data)
    print(f"{model} | Précision: {round(accuracy*100, 2)}% | Temps moyen: {round(avg_time, 2)}s")

# ── Précision par modèle et par catégorie ──
print("\n══ PRÉCISION PAR MODÈLE ET CATÉGORIE ══")
for (model, category), data in sorted(combo_data.items()):
    accuracy = mean(r["is_correct"] for r in data)
    avg_time = mean(r["response_time"] for r in data)
    print(f"{model} | {category} | Précision: {round(accuracy*100, 2)}% | Temps moyen: {round(avg_time, 2)}s")