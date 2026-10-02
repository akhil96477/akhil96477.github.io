
// ── SCRAMBLE PRELOADER ──
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
});

/* ================================================
   DAVULA AKHIL — PORTFOLIO V2 JS
   Particle starfield · Scroll reveals · Tilt
   ================================================ */


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

// ── SCROLL REVEAL ──
// Add data-reveal to all revealable elements
document.querySelectorAll(
  '.section-header, .section-tag, .section-title, .bento-card, .about-text, .about-info, .stack-card, .cta-title, .cta-btn, .cta-links'
).forEach(el => el.setAttribute('data-reveal', ''));

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      // Stagger siblings
      const parent = entry.target.parentElement;
      const siblings = parent ? Array.from(parent.querySelectorAll('[data-reveal]')) : [];
      const idx = siblings.indexOf(entry.target);
      setTimeout(() => {
        entry.target.classList.add('visible');
      }, Math.max(0, idx * 80));
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -60px 0px' });

document.querySelectorAll('[data-reveal]').forEach(el => observer.observe(el));

// ── BENTO CARD TILT ──
if (window.innerWidth > 768) {
  document.querySelectorAll('.bento-card').forEach(card => {
    card.addEventListener('mousemove', e => {
      const rect = card.getBoundingClientRect();
      const x = (e.clientX - rect.left) / rect.width;
      const y = (e.clientY - rect.top) / rect.height;
      const rotateX = (0.5 - y) * 8;
      const rotateY = (x - 0.5) * 8;
      card.style.transform = `perspective(800px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-6px) scale(1.01)`;
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = '';
    });
  });
}

// ── SMOOTH SCROLL ──
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', e => {
    const t = document.querySelector(a.getAttribute('href'));
    if (t) { 
      e.preventDefault(); 
      lenis.scrollTo(t);
    }
  });
});

// ── NAV BLEND ON SCROLL ──
const nav = document.querySelector('.nav');
window.addEventListener('scroll', () => {
  if (window.scrollY > 100) {
    nav.style.mixBlendMode = 'normal';
    nav.style.background = 'rgba(10,10,10,0.8)';
    nav.style.backdropFilter = 'blur(20px)';
    nav.style.webkitBackdropFilter = 'blur(20px)';
  } else {
    nav.style.mixBlendMode = 'difference';
    nav.style.background = 'transparent';
    nav.style.backdropFilter = 'none';
  }
}, { passive: true });

// ── TEXT SCRAMBLE / DECODER EFFECT ──
const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
document.querySelectorAll('.nav-links a, .bento-card__title').forEach(el => {
  el.dataset.value = el.innerText;
  
  el.addEventListener('mouseenter', event => {
    let iterations = 0;
    const target = event.target;
    
    clearInterval(target.interval);
    
    target.interval = setInterval(() => {
      target.innerText = target.innerText.split("")
        .map((letter, index) => {
          if (index < iterations) return target.dataset.value[index];
          return letters[Math.floor(Math.random() * 26)];
        })
        .join("");
      
      if (iterations >= target.dataset.value.length) {
        clearInterval(target.interval);
        target.innerText = target.dataset.value;
      }
      
      iterations += 1 / 3;
    }, 30);
  });
});

// ── SPOTLIGHT TRACKING ──
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
});
