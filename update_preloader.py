import re

html_path = "/Users/akhil/.gemini/antigravity/scratch/portfolio/index.html"
css_path = "/Users/akhil/.gemini/antigravity/scratch/portfolio/style.css"
js_path = "/Users/akhil/.gemini/antigravity/scratch/portfolio/script.js"

# --- HTML ---
with open(html_path, "r") as f:
    html = f.read()

# Replace the old preloader HTML
old_preloader_html_regex = r'<!-- 3D PRELOADER -->.*?</div>\s*</div>'
new_preloader_html = """<!-- SCRAMBLE PRELOADER -->
  <div id="preloader">
    <div class="preloader-content">
      <span id="scramble-intro" data-value="DAVULA AKHIL">_</span>
    </div>
  </div>"""

html = re.sub(old_preloader_html_regex, new_preloader_html, html, flags=re.DOTALL)
with open(html_path, "w") as f:
    f.write(html)


# --- CSS ---
with open(css_path, "r") as f:
    css = f.read()

old_preloader_css_regex = r'/\* ================================================\n   3D PRELOADER\n   ================================================ \*/.*?body\.preloading \{\n  overflow: hidden;\n\}'

new_preloader_css = """/* ================================================
   SCRAMBLE PRELOADER
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
  transition: transform 0.7s cubic-bezier(0.85, 0, 0.15, 1), opacity 0.7s ease;
}

#preloader.hide {
  transform: translateY(-100vh);
  opacity: 0;
  pointer-events: none;
}

.preloader-content {
  font-size: clamp(2.5rem, 6vw, 5.5rem);
  font-family: 'JetBrains Mono', monospace;
  font-weight: 700;
  color: #555;
  letter-spacing: 0.15em;
  position: relative;
}

#scramble-intro {
  position: relative;
  display: inline-block;
}

#scramble-intro.glowing {
  color: var(--primary);
  text-shadow: 0 0 25px rgba(200, 255, 0, 0.4);
  transition: color 0.1s ease, text-shadow 0.1s ease;
}

body.preloading {
  overflow: hidden;
}"""

css = re.sub(old_preloader_css_regex, new_preloader_css, css, flags=re.DOTALL)
with open(css_path, "w") as f:
    f.write(css)


# --- JS ---
with open(js_path, "r") as f:
    js = f.read()

old_preloader_js_regex = r'// ── 3D PRELOADER ──.*?\}\);'

new_preloader_js = """// ── SCRAMBLE PRELOADER ──
window.addEventListener('load', () => {
  const el = document.getElementById('scramble-intro');
  const preloader = document.getElementById('preloader');
  if (!el || !preloader) return;
  
  const finalValue = el.getAttribute('data-value');
  const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*";
  let iterations = 0;
  
  const scrambleInterval = setInterval(() => {
    el.innerText = finalValue.split("").map((char, index) => {
      if (char === " ") return " ";
      if (index < iterations) return finalValue[index];
      return chars[Math.floor(Math.random() * chars.length)];
    }).join("");
    
    if (iterations >= finalValue.length) {
      clearInterval(scrambleInterval);
      el.classList.add('glowing');
      
      // Much faster exit (minimal delay)
      setTimeout(() => {
        preloader.classList.add('hide');
        setTimeout(() => {
          document.body.classList.remove('preloading');
        }, 700);
      }, 400); 
    }
    iterations += 1.5; // Controls the speed of the scramble
  }, 40); 
});"""

js = re.sub(old_preloader_js_regex, new_preloader_js, js, flags=re.DOTALL)
with open(js_path, "w") as f:
    f.write(js)

print("Preloader updated to fast futuristic scramble!")
