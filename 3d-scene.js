
// ── THREE.JS 3D HERO ANIMATION ──
(function() {
    const container = document.getElementById('three-container');
    if (!container) return;

    // Setup scene, camera, renderer
    const scene = new THREE.Scene();
    
    // Camera
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.z = 30;

    // Renderer (transparent background)
    const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(window.devicePixelRatio);
    container.appendChild(renderer.domElement);

    // ── CREATE 3D OBJECTS ──
    
    // 1. The Core Icosahedron (Tech/AI symbol)
    const geometry = new THREE.IcosahedronGeometry(12, 1);
    const material = new THREE.MeshBasicMaterial({ 
        color: 0xc8ff00, 
        wireframe: true, 
        transparent: true, 
        opacity: 0.15 
    });
    const core = new THREE.Mesh(geometry, material);
    scene.add(core);

    // 2. Outer Ring (Torus)
    const ringGeo = new THREE.TorusGeometry(18, 0.1, 16, 100);
    const ringMat = new THREE.MeshBasicMaterial({ 
        color: 0xc8ff00, 
        transparent: true, 
        opacity: 0.3 
    });
    const ring = new THREE.Mesh(ringGeo, ringMat);
    ring.rotation.x = Math.PI / 2;
    scene.add(ring);

    // 3. Floating Particles in 3D Space
    const particlesGeo = new THREE.BufferGeometry();
    const particleCount = 400;
    const posArray = new Float32Array(particleCount * 3);
    for(let i = 0; i < particleCount * 3; i++) {
        // Spread particles around
        posArray[i] = (Math.random() - 0.5) * 60;
    }
    particlesGeo.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
    const particlesMat = new THREE.PointsMaterial({
        size: 0.15,
        color: 0xc8ff00,
        transparent: true,
        opacity: 0.8,
        blending: THREE.AdditiveBlending
    });
    const particles = new THREE.Points(particlesGeo, particlesMat);
    scene.add(particles);

    // ── INTERACTIVITY ──
    let mouseX = 0;
    let mouseY = 0;
    let targetX = 0;
    let targetY = 0;
    const windowHalfX = window.innerWidth / 2;
    const windowHalfY = window.innerHeight / 2;

    document.addEventListener('mousemove', (event) => {
        mouseX = (event.clientX - windowHalfX);
        mouseY = (event.clientY - windowHalfY);
    });

    // ── ANIMATION LOOP ──
    const clock = new THREE.Clock();

    function animate() {
        requestAnimationFrame(animate);
        const elapsedTime = clock.getElapsedTime();

        // Mouse Parallax Targets
        targetX = mouseX * 0.001;
        targetY = mouseY * 0.001;

        // Auto-rotation
        core.rotation.y += 0.002;
        core.rotation.x += 0.001;
        
        ring.rotation.x += 0.001;
        ring.rotation.y += 0.002;

        particles.rotation.y = elapsedTime * 0.05;

        // Interactive Mouse Tilting
        scene.rotation.x += 0.05 * (targetY - scene.rotation.x);
        scene.rotation.y += 0.05 * (targetX - scene.rotation.y);

        renderer.render(scene, camera);
    }
    animate();

    // ── RESIZE HANDLER ──
    window.addEventListener('resize', () => {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
    });
})();
