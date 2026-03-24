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