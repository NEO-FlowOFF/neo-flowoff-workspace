import os
import glob

# Search in the neo-flw-landing directory
search_dir = '/Users/nettomello/neomello/NEO-FlowOFF/neo-flw-landing'
extensions = ['*.html', '*.md', '*.json', '*.js', '*.webmanifest', '.env.example']

old_str = "NEØ.FLOWOFF"
new_str = "neoflowoff.agency"

files_to_check = []
for ext in extensions:
    files_to_check.extend(glob.glob(os.path.join(search_dir, '**', ext), recursive=True))

for file_path in files_to_check:
    if "node_modules" in file_path or ".git" in file_path:
        continue
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if old_str in content:
            new_content = content.replace(old_str, new_str)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated: {file_path}")
    except Exception as e:
        print(f"Skipping {file_path} due to error: {e}")

print("Replacement complete.")
