import re

html_path = "/Users/akhil/.gemini/antigravity/scratch/portfolio/index.html"
css_path = "/Users/akhil/.gemini/antigravity/scratch/portfolio/style.css"
js_path = "/Users/akhil/.gemini/antigravity/scratch/portfolio/script.js"

# 1. Add Preloader HTML right after <body>
with open(html_path, "r") as f:
    html = f.read()

preloader_html = """
  <!-- 3D PRELOADER -->
  <div id="preloader">
    <div class="preloader-content">
      <span class="word">DAVULA</span>
      <span class="word accent">AKHIL</span>
    </div>
  </div>
"""
if '<div id="preloader">' not in html:
    html = html.replace('<body>', f'<body>\n{preloader_html}')
    with open(html_path, "w") as f:
        f.write(html)


# 2. Add Preloader CSS to the top of style.css
with open(css_path, "r") as f:
    css = f.read()

preloader_css = """
/* ================================================
   3D PRELOADER
   ================================================ */
#preloader {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: #050505;
  z-index: 999999;
  display: flex;
  justify-content: center;
  align-items: center;
  perspective: 1200px;
  transition: transform 1.2s cubic-bezier(0.77, 0, 0.175, 1);
}

#preloader.hide {
  transform: translateY(-100vh);
}

.preloader-content {
  display: flex;
  gap: 1.5rem;
  font-size: clamp(3rem, 8vw, 7rem);
  font-weight: 700;
  font-family: 'Space Grotesk', sans-serif;
  color: var(--text-main);
  transform-style: preserve-3d;
}

.preloader-content .word {
  display: inline-block;
  opacity: 0;
  transform-origin: bottom center;
  transform: rotateX(90deg) translateY(50px) translateZ(-200px);
  animation: reveal3D 1.2s cubic-bezier(0.19, 1, 0.22, 1) forwards;
}

.preloader-content .word.accent {
  color: var(--primary);
  animation-delay: 0.15s;
}

@keyframes reveal3D {
  0% {
    opacity: 0;
    transform: rotateX(90deg) translateY(50px) translateZ(-200px);
  }
  100% {
    opacity: 1;
    transform: rotateX(0deg) translateY(0) translateZ(0);
  }
}

/* Hide body scroll while preloading */
body.preloading {
  overflow: hidden;
}
"""
if '#preloader {' not in css:
    css = preloader_css + "\n" + css
    with open(css_path, "w") as f:
        f.write(css)

# 3. Add body.preloading to HTML and remove it in JS
with open(html_path, "r") as f:
    html = f.read()
if '<body class="preloading">' not in html:
    html = html.replace('<body>', '<body class="preloading">')
    with open(html_path, "w") as f:
        f.write(html)

with open(js_path, "r") as f:
    js = f.read()

preloader_js = """
// ── 3D PRELOADER ──
window.addEventListener('load', () => {
  setTimeout(() => {
    const preloader = document.getElementById('preloader');
    if (preloader) {
      preloader.classList.add('hide');
      setTimeout(() => {
        document.body.classList.remove('preloading');
      }, 1200); // Wait for slide up animation
    }
  }, 2200); // Show text for 2.2 seconds before sliding up
});

"""
if '3D PRELOADER' not in js:
    js = preloader_js + js
    with open(js_path, "w") as f:
        f.write(js)

print("Preloader added successfully.")
