import json
import requests
from datetime import datetime

with open("results.json", "r", encoding="utf-8") as f:
    results = json.load(f)

for i, doc in enumerate(results):
    doc["timestamp"]      = datetime.utcnow().isoformat()
    doc["is_correct_int"] = 1 if doc["is_correct"] else 0
    doc["refused_int"]    = 1 if doc["refused"]    else 0
    response = requests.post(
        "http://localhost:9200/wmdp-results/_doc",
        json=doc,
        headers={"Content-Type": "application/json"}
    )
    if response.status_code == 201:
        print(f"Doc {i+1}/{len(results)} ingéré")
    else:
        print(f"Erreur doc {i+1}: {response.text}")