import json

MANIFEST = "manifests/repos.json"
with open(MANIFEST) as f:
    data = json.load(f)

data["repositories"] = [r for r in data["repositories"] if r["name"] != "neo-flowoff-agency"]

with open(MANIFEST, "w") as f:
    json.dump(data, f, indent=2)

print("Removed neo-flowoff-agency from repos.json")
