import json
import csv

for nom in ['results', 'contextual_results']:
    with open(f'{nom}.json') as f:
        data = json.load(f)
    with open(f'{nom}.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)