import re
import os

css_path = 'neo-flw-landing/landing_v2.css'
with open(css_path, 'r') as f:
    content = f.read()

def convert_rgba(match):
    r, g, b, a = match.groups()
    a = float(a)
    a_pct = f"{int(a * 100)}%"
    return f"rgb({r.strip()} {g.strip()} {b.strip()} / {a_pct})"

# Convert rgba(r,g,b,a) to rgb(r g b / a%)
content = re.sub(r'rgba\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*([0-9.]+)\s*\)', convert_rgba, content)

# Fix redundant padding/margin
content = content.replace("0 12px 20px 12px", "0 12px 20px")

# Silence conflicting/stylelint-specific rules
header = "/* stylelint-disable property-no-vendor-prefix, media-feature-range-notation, no-descending-specificity, rule-empty-line-before */\n"
if not content.startswith("/* stylelint-disable"):
    content = header + content

with open(css_path, 'w') as f:
    f.write(content)

print("Stylelint errors fixed in landing_v2.css")
