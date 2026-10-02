import re
import os

html_path = "/Users/akhil/.gemini/antigravity/scratch/portfolio/index.html"
js_path = "/Users/akhil/.gemini/antigravity/scratch/portfolio/script.js"
three_path = "/Users/akhil/.gemini/antigravity/scratch/portfolio/3d-scene.js"
css_path = "/Users/akhil/.gemini/antigravity/scratch/portfolio/style.css"

# 1. HTML: Add Lenis, remove old 2D canvas
with open(html_path, "r") as f:
    html = f.read()

lenis_script = '<script src="https://cdn.jsdelivr.net/gh/studio-freight/lenis@1.0.19/bundled/lenis.min.js"></script>'
if lenis_script not in html:
    html = html.replace('</head>', f'  {lenis_script}\n</head>')

html = html.replace('<canvas id="particleCanvas"></canvas>', '')
with open(html_path, "w") as f:
    f.write(html)


# 2. JS: Remove 2D Starfield, add Lenis, debounce spotlight
with open(js_path, "r") as f:
    js = f.read()

# Strip out the entire 2D particle system
if "// ── PARTICLE STARFIELD ──" in js:
    # Find the block and remove it
    # We can do a simple regex or just string replace if we know the bounds
    # Since it goes from // ── PARTICLE STARFIELD ── to // ── SCROLL REVEAL ──
    js = re.sub(r"// ── PARTICLE STARFIELD ──.*?// ── SCROLL REVEAL ──", "// ── SCROLL REVEAL ──", js, flags=re.DOTALL)

# Add Lenis
lenis_init = """
// ── LENIS SMOOTH SCROLL ──
const lenis = new Lenis({
  duration: 1.2,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  direction: 'vertical',
  gestureDirection: 'vertical',
  smooth: true,
  mouseMultiplier: 1,
  smoothTouch: false,
});

function raf(time) {
  lenis.raf(time);
  requestAnimationFrame(raf);
}
requestAnimationFrame(raf);

"""
if 'new Lenis' not in js:
    # Insert after preloader
    js = js.replace('// ── SCROLL REVEAL ──', lenis_init + '// ── SCROLL REVEAL ──')

# Debounce Spotlight
spotlight_old = """// ── SPOTLIGHT TRACKING ──
document.querySelectorAll('.bento-card').forEach(card => {
  card.addEventListener('mousemove', e => {
    const rect = card.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    card.style.setProperty('--x', `${x}px`);
    card.style.setProperty('--y', `${y}px`);
  });
});"""

spotlight_new = """// ── SPOTLIGHT TRACKING ──
document.querySelectorAll('.bento-card').forEach(card => {
  let ticking = false;
  card.addEventListener('mousemove', e => {
    if (!ticking) {
      window.requestAnimationFrame(() => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        card.style.setProperty('--x', `${x}px`);
        card.style.setProperty('--y', `${y}px`);
        ticking = false;
      });
      ticking = true;
    }
  });
});"""
js = js.replace(spotlight_old, spotlight_new)

# Smooth scroll anchor tag handling for Lenis
anchor_old = """document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const t = document.querySelector(a.getAttribute('href'));
    if (t) { e.preventDefault(); t.scrollIntoView({ behavior: 'smooth' }); }
  });
});"""
anchor_new = """document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const t = document.querySelector(a.getAttribute('href'));
    if (t) { 
      e.preventDefault(); 
      lenis.scrollTo(t);
    }
  });
});"""
js = js.replace(anchor_old, anchor_new)

with open(js_path, "w") as f:
    f.write(js)

# 3. Optimize Three.js Scene
with open(three_path, "r") as f:
    three = f.read()

# Replace setPixelRatio
if 'renderer.setPixelRatio(window.devicePixelRatio);' in three:
    three = three.replace(
        'renderer.setPixelRatio(window.devicePixelRatio);', 
        'renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2)); // Cap pixel ratio for performance'
    )

with open(three_path, "w") as f:
    f.write(three)

# 4. Remove default CSS scroll-behavior: smooth as it conflicts with Lenis
with open(css_path, "r") as f:
    css = f.read()
css = css.replace("scroll-behavior: smooth;", "/* scroll-behavior: smooth; removed for Lenis */")
with open(css_path, "w") as f:
    f.write(css)

print("Performance optimization complete!")
