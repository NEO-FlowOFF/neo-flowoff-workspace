import json, os, glob

MANIFEST = "manifests/repos.json"
with open(MANIFEST) as f:
    data = json.load(f)

existing_repos = {repo["name"] for repo in data["repositories"]}
all_git_dirs = [d.replace("/.git", "") for d in glob.glob("*/.git")]

new_repos = sorted(set(all_git_dirs) - existing_repos)

for repo_name in new_repos:
    print(f"Adding {repo_name}...")
    pkg_path = f"{repo_name}/package.json"
    desc = ""
    if os.path.exists(pkg_path):
        try:
            with open(pkg_path) as pf:
                pkg = json.load(pf)
                desc = pkg.get("description", "")
        except Exception as e:
            print(f"Error reading {pkg_path}: {e}")
                
    new_entry = {
        "name": repo_name,
        "localPath": f"./{repo_name}",
        "remote": f"https://github.com/NEO-FlowOFF/{repo_name}.git",
        "role": desc if desc else "TODO: describe role",
        "runtime": {
            "category": "unknown",
            "framework": "unknown",
            "node": "18+"
        },
        "localDevelopment": {
            "primaryCommand": "pnpm dev",
            "ports": [],
            "notes": []
        },
        "deployment": {
            "primaryPlatform": "unknown",
            "configFiles": []
        },
        "publicSurface": {
            "domains": [],
            "webhookEndpoints": [],
            "serviceApis": []
        },
        "dependencies": {
            "internal": [],
            "external": []
        },
        "evidence": [f"./{repo_name}/package.json"]
    }
    data["repositories"].append(new_entry)

with open(MANIFEST, "w") as f:
    json.dump(data, f, indent=2)

print("repos.json updated!")
