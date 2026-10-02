import re

html_path = "/Users/akhil/.gemini/antigravity/scratch/portfolio/index.html"
css_path = "/Users/akhil/.gemini/antigravity/scratch/portfolio/style.css"
js_path = "/Users/akhil/.gemini/antigravity/scratch/portfolio/script.js"

# --- HTML ---
with open(html_path, "r") as f:
    html = f.read()

old_html_regex = r'<!-- SCRAMBLE PRELOADER -->.*?</div>\s*</div>'
new_html = """<!-- CINEMATIC PRELOADER -->
  <div id="preloader">
    <div class="intro-progress"></div>
    <h1 class="intro-title" data-text="DAVULA AKHIL">DAVULA AKHIL</h1>
  </div>"""

html = re.sub(old_html_regex, new_html, html, flags=re.DOTALL)
with open(html_path, "w") as f:
    f.write(html)


# --- CSS ---
with open(css_path, "r") as f:
    css = f.read()

old_css_regex = r'/\* ================================================\n   SCRAMBLE PRELOADER\n   ================================================ \*/.*?body\.preloading \{\n  overflow: hidden;\n\}'

new_css = """/* ================================================
   CINEMATIC PRELOADER
   ================================================ */
#preloader {
  position: fixed;
  top: 0; left: 0; width: 100vw; height: 100vh;
  background: #050505;
  z-index: 999999;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  transition: opacity 0.8s ease;
}

#preloader.hide {
  opacity: 0;
  pointer-events: none;
}

.intro-progress {
  position: absolute;
  top: 50%;
  left: 0;
  width: 0%;
  height: 2px;
  background: var(--primary);
  z-index: 10;
  box-shadow: 0 0 15px var(--primary);
  opacity: 1;
  transition: opacity 0.3s ease;
}

.intro-title {
  font-family: 'Space Grotesk', sans-serif;
  font-size: clamp(3rem, 10vw, 9rem);
  font-weight: 700;
  letter-spacing: 0.05em;
  margin: 0;
  color: transparent;
  -webkit-text-stroke: 1.5px rgba(255, 255, 255, 0.15);
  position: relative;
  opacity: 0;
  transform: scale(1.1);
  will-change: transform, opacity;
}

.intro-title::before {
  content: attr(data-text);
  position: absolute;
  left: 0; top: 0;
  width: 0%;
  height: 100%;
  color: var(--primary);
  -webkit-text-stroke: 0px transparent;
  overflow: hidden;
  white-space: nowrap;
  border-right: 6px solid var(--primary);
  filter: drop-shadow(0 0 20px rgba(200, 255, 0, 0.8));
  will-change: width;
}

/* Animations */
.intro-title.show {
  opacity: 1;
  transform: scale(1);
  transition: transform 1s cubic-bezier(0.16, 1, 0.3, 1), opacity 1s ease;
}

.intro-title.fill::before {
  width: 100%;
  transition: width 1s cubic-bezier(0.85, 0, 0.15, 1);
}

.intro-title.zoom {
  transform: scale(35); /* Massive fly-through */
  opacity: 0;
  transition: transform 1.2s cubic-bezier(0.7, 0, 0.3, 1), opacity 0.6s ease 0.4s;
}

body.preloading {
  overflow: hidden;
}"""

css = re.sub(old_css_regex, new_css, css, flags=re.DOTALL)
with open(css_path, "w") as f:
    f.write(css)


# --- JS ---
with open(js_path, "r") as f:
    js = f.read()

old_js_regex = r'// ── SCRAMBLE PRELOADER ──.*?\}\);'

new_js = """// ── CINEMATIC PRELOADER ──
window.addEventListener('load', () => {
  const preloader = document.getElementById('preloader');
  const progress = document.querySelector('.intro-progress');
  const title = document.querySelector('.intro-title');
  
  if (!preloader || !progress || !title) return;

  // 1. Laser scan line shoots across screen
  progress.style.transition = 'width 0.7s cubic-bezier(0.85, 0, 0.15, 1)';
  progress.style.width = '100%';

  setTimeout(() => {
    progress.style.opacity = '0'; // hide line
    title.classList.add('show'); // Fade in hollow outline text
    
    setTimeout(() => {
      title.classList.add('fill'); // Neon green liquid/laser wipe fills text
      
      setTimeout(() => {
        // Massive 3D Camera zoom-through transition
        title.classList.add('zoom');
        preloader.classList.add('hide'); // Fade out black background smoothly
        
        setTimeout(() => {
          document.body.classList.remove('preloading');
          preloader.style.display = 'none';
        }, 1200);
      }, 1400); // Wait for fill to finish + hold for maximum impact
    }, 800); // Wait for outline to settle
  }, 700); // Wait for scanline to finish
});"""

js = re.sub(old_js_regex, new_js, js, flags=re.DOTALL)
with open(js_path, "w") as f:
    f.write(js)

print("Preloader updated to cinematic fly-through sequence!")
