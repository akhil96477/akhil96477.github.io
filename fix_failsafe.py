js_path = "/Users/akhil/.gemini/antigravity/scratch/portfolio/script.js"
with open(js_path, "r") as f:
    js = f.read()

# Add a failsafe
failsafe = """
// FAILSAFE: If preloader gets stuck for any reason, force hide it after 4 seconds
setTimeout(() => {
  const p = document.getElementById('preloader');
  if (p && p.style.display !== 'none') {
    p.style.display = 'none';
    document.body.classList.remove('preloading');
  }
}, 4000);
"""
if "FAILSAFE" not in js:
    js = failsafe + js
    with open(js_path, "w") as f:
        f.write(js)
    print("Added failsafe")
