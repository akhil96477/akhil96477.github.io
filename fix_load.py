import re

js_path = "/Users/akhil/.gemini/antigravity/scratch/portfolio/script.js"
with open(js_path, "r") as f:
    js = f.read()

# Replace window.addEventListener('load' with a self-executing init block
old_block = r"window\.addEventListener\('load', \(\) => \{"
new_block = """// Fire immediately when DOM is parsed, don't wait for slow network resources
document.addEventListener('DOMContentLoaded', () => {"""

if "window.addEventListener('load'" in js:
    js = re.sub(old_block, new_block, js)
    with open(js_path, "w") as f:
        f.write(js)
    print("Fixed listener")
else:
    print("Could not find load listener")
