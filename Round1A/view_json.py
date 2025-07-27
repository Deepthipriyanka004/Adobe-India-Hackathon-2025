import json

json_path = "app/output/Untitled document (2).json"

with open(json_path, encoding="utf-8") as f:
    data = json.load(f)

print(json.dumps(data, indent=2, ensure_ascii=False))
