import streamlit.components.v1 as components

from config import ENABLE_ANIMATIONS


def confetti_once(key: str = "confetti"):
    if not ENABLE_ANIMATIONS:
        return
    components.html(
        f"""
        <canvas id="{key}" style="position:fixed;inset:0;pointer-events:none;z-index:9999"></canvas>
        <script>
        const canvas = document.getElementById("{key}");
        const ctx = canvas.getContext("2d");
        let W = canvas.width = window.innerWidth;
        let H = canvas.height = window.innerHeight;
        const colors = ["#14B8A6", "#22D3EE", "#FF8A3D", "#F59E0B", "#12356B"];
        const pieces = Array.from({{length: 90}}, () => ({{
          x: Math.random() * W,
          y: -20 - Math.random() * 80,
          r: 4 + Math.random() * 6,
          c: colors[Math.floor(Math.random() * colors.length)],
          vx: -2 + Math.random() * 4,
          vy: 2 + Math.random() * 5,
          a: Math.random() * Math.PI
        }}));
        let frame = 0;
        function draw() {{
          ctx.clearRect(0, 0, W, H);
          pieces.forEach(p => {{
            p.x += p.vx; p.y += p.vy; p.a += 0.08;
            ctx.save(); ctx.translate(p.x, p.y); ctx.rotate(p.a);
            ctx.fillStyle = p.c; ctx.fillRect(-p.r/2, -p.r/2, p.r, p.r * 0.65);
            ctx.restore();
          }});
          frame++;
          if (frame < 150) requestAnimationFrame(draw);
          else canvas.remove();
        }}
        draw();
        </script>
        """,
        height=0,
    )


def countup(label: str, value: int | float, suffix: str = ""):
    components.html(
        f"""
        <div class="countup-box">
          <span data-target="{float(value)}">0</span>{suffix}
        </div>
        <script>
        const el = document.currentScript.previousElementSibling.querySelector("span");
        const target = Number(el.dataset.target);
        let start = null;
        function tick(ts) {{
          if (!start) start = ts;
          const p = Math.min((ts - start) / 900, 1);
          el.textContent = Math.round(target * p).toLocaleString("en-IN");
          if (p < 1) requestAnimationFrame(tick);
        }}
        requestAnimationFrame(tick);
        </script>
        """,
        height=30,
    )
