#!/usr/bin/env python3
"""Generate self-contained interactive high-school mechanics HTML pages."""

from __future__ import annotations

import argparse
from pathlib import Path


def page(title: str, body: str, script: str) -> str:
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <script>
    window.MathJax = {{ tex: {{ inlineMath: [['$', '$'], ['\\\\(', '\\\\)']] }} }};
  </script>
  <script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
  <style>
    :root {{
      color-scheme: light;
      --ink: #213043;
      --muted: #62717d;
      --line: #d9e3eb;
      --panel: #ffffff;
      --soft: #f2f7fa;
      --blue: #2457c5;
      --green: #1f8a70;
      --rose: #d63f64;
      --orange: #ff8b3d;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", sans-serif;
      color: var(--ink);
      background: linear-gradient(135deg, #fff4dc 0%, #f8fbfc 45%, #e4effa 100%);
      min-height: 100vh;
    }}
    .app {{ max-width: 1180px; margin: 0 auto; padding: 28px; }}
    header {{ margin-bottom: 20px; }}
    h1 {{ margin: 0 0 8px; font-size: 34px; }}
    h2 {{ margin-top: 0; }}
    .subtitle {{ color: var(--muted); font-size: 18px; }}
    .grid {{ display: grid; grid-template-columns: 380px 1fr; gap: 20px; align-items: stretch; }}
    .panel {{
      background: rgba(255,255,255,.92);
      border: 1px solid var(--line);
      border-radius: 18px;
      box-shadow: 0 18px 45px rgba(33,48,67,.12);
      padding: 22px;
    }}
    label {{ display: grid; gap: 8px; margin: 18px 0; font-weight: 700; }}
    .row {{ display: flex; justify-content: space-between; gap: 12px; color: var(--muted); font-weight: 600; }}
    input[type="range"] {{ width: 100%; accent-color: var(--green); }}
    .result {{
      background: var(--ink);
      color: #b9f1e7;
      border-radius: 14px;
      padding: 16px 18px;
      font: 700 25px Georgia, serif;
      margin: 18px 0;
    }}
    .status-pill {{
      display: inline-block;
      border-radius: 999px;
      padding: 8px 14px;
      color: white;
      background: var(--green);
      font-weight: 800;
      margin: 8px 0 16px;
    }}
    .formula {{ color: var(--ink); line-height: 1.8; }}
    svg {{ width: 100%; height: 560px; background: #eef6fb; border-radius: 18px; border: 1px solid var(--line); }}
    .note {{ color: var(--muted); line-height: 1.7; }}
    .controls {{ display: flex; gap: 10px; margin: 14px 0 0; flex-wrap: wrap; }}
    button {{
      border: 0;
      border-radius: 999px;
      padding: 10px 16px;
      background: var(--ink);
      color: white;
      font-weight: 800;
      cursor: pointer;
    }}
    button.secondary {{ background: #dce6ee; color: var(--ink); }}
    @media (max-width: 860px) {{ .grid {{ grid-template-columns: 1fr; }} svg {{ height: 420px; }} }}
  </style>
</head>
<body>
  <main class="app">
    {body}
  </main>
  <script>{script}</script>
</body>
</html>
"""


def incline() -> str:
    body = """<header>
      <h1>斜面摩擦力互动题页</h1>
      <div class="subtitle">调节质量、斜面角度和摩擦因数，实时观察受力图、加速度和滑块运动。</div>
    </header>
    <section class="grid">
      <aside class="panel">
        <h2>题目</h2>
        <p class="note">质量为 $m$ 的小物块放在倾角为 $\\theta$ 的粗糙斜面上，动摩擦因数为 $\\mu$。若物块沿斜面方向运动，求沿斜面方向的加速度。</p>
        <label><span class="row"><span>质量 m</span><output id="mOut"></output></span><input id="m" type="range" min="0.5" max="5" step="0.1" value="2"></label>
        <label><span class="row"><span>角度 θ</span><output id="thetaOut"></output></span><input id="theta" type="range" min="5" max="55" step="1" value="30"></label>
        <label><span class="row"><span>摩擦因数 μ</span><output id="muOut"></output></span><input id="mu" type="range" min="0" max="0.8" step="0.01" value="0.2"></label>
        <label><span class="row"><span>重力加速度 g</span><output id="gOut"></output></span><input id="g" type="range" min="9.0" max="10.0" step="0.01" value="9.8"></label>
        <div class="result" id="answer"></div>
        <div class="status-pill" id="motionStatus"></div>
        <p class="note" id="motionReadout"></p>
        <div class="formula">$$N=mg\\cos\\theta$$ $$f=\\mu N$$ $$a=g(\\sin\\theta-\\mu\\cos\\theta)$$</div>
      </aside>
      <section class="panel">
        <svg id="scene" viewBox="0 0 720 560" role="img" aria-label="Incline force animation">
          <defs>
            <marker id="arrowB" markerWidth="18" markerHeight="18" refX="16" refY="9" orient="auto" markerUnits="userSpaceOnUse"><path d="M2 3L16 9L2 15Z" fill="#2457c5"/></marker>
            <marker id="arrowG" markerWidth="18" markerHeight="18" refX="16" refY="9" orient="auto" markerUnits="userSpaceOnUse"><path d="M2 3L16 9L2 15Z" fill="#1f8a70"/></marker>
            <marker id="arrowR" markerWidth="18" markerHeight="18" refX="16" refY="9" orient="auto" markerUnits="userSpaceOnUse"><path d="M2 3L16 9L2 15Z" fill="#d63f64"/></marker>
            <marker id="arrowO" markerWidth="18" markerHeight="18" refX="16" refY="9" orient="auto" markerUnits="userSpaceOnUse"><path d="M2 3L16 9L2 15Z" fill="#ff8b3d"/></marker>
          </defs>
          <g id="drawing"></g>
        </svg>
        <div class="controls">
          <button id="playPause">暂停</button>
          <button id="resetMotion" class="secondary">重置运动</button>
        </div>
        <p class="note">蓝色是重力，绿色是支持力，红色是摩擦力，橙色是沿斜面合力方向。滑块位置由加速度随时间更新。</p>
      </section>
    </section>"""
    script = r"""
const inputIds = ['m','theta','mu','g'];
const motion = { pos: 0.2, vel: 0, last: 0, playing: true, a: 0, direction: 1, trail: [] };
for (const id of inputIds) document.getElementById(id).addEventListener('input', () => { resetMotion(false); updateValues(); drawIncline(); });
document.getElementById('playPause').addEventListener('click', () => {
  motion.playing = !motion.playing;
  document.getElementById('playPause').textContent = motion.playing ? '暂停' : '播放';
  motion.last = performance.now();
});
document.getElementById('resetMotion').addEventListener('click', () => resetMotion(true));

function line(x1, y1, x2, y2, color, marker, label) {
  return `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${color}" stroke-width="7" stroke-linecap="round" marker-end="url(#${marker})"/><text x="${x2+8}" y="${y2+4}" font-size="22" font-weight="800" fill="${color}">${label}</text>`;
}

function values() {
  const m = +document.getElementById('m').value;
  const theta = +document.getElementById('theta').value;
  const mu = +document.getElementById('mu').value;
  const g = +document.getElementById('g').value;
  const rad = theta * Math.PI / 180;
  const N = m * g * Math.cos(rad);
  const f = mu * N;
  const a = g * (Math.sin(rad) - mu * Math.cos(rad));
  return { m, theta, mu, g, rad, N, f, a };
}

function updateValues() {
  const v = values();
  motion.a = v.a;
  motion.direction = Math.sign(v.a || 1);
  document.getElementById('mOut').textContent = `${v.m.toFixed(1)} kg`;
  document.getElementById('thetaOut').textContent = `${v.theta.toFixed(0)}°`;
  document.getElementById('muOut').textContent = v.mu.toFixed(2);
  document.getElementById('gOut').textContent = `${v.g.toFixed(2)} m/s²`;
  document.getElementById('answer').textContent = `a = ${v.a.toFixed(2)} m/s²`;
  document.getElementById('motionReadout').textContent = `动画位移进度：${(motion.pos * 100).toFixed(0)}%，速度比例：${motion.vel.toFixed(2)}`;
  const statusEl = document.getElementById('motionStatus');
  statusEl.textContent = Math.abs(v.a) < 0.05 ? '临界状态：加速度约为 0' : (v.a > 0 ? '沿斜面向下加速' : '合力沿斜面向上');
  statusEl.style.background = Math.abs(v.a) < 0.05 ? '#ff8b3d' : (v.a > 0 ? '#1f8a70' : '#d63f64');
}

function resetMotion(alsoDraw) {
  motion.pos = 0.2;
  motion.vel = 0;
  motion.last = performance.now();
  motion.trail = [];
  if (alsoDraw) drawIncline();
}

function drawIncline() {
  const v = values();
  const baseX = 100, baseY = 440, len = 520, height = Math.tan(v.rad) * len;
  const topX = baseX + len, topY = baseY - height;
  const t = Math.max(0.08, Math.min(0.92, motion.pos));
  const bx = baseX + len * t;
  const by = baseY - height * t;
  const nx = Math.sin(v.rad), ny = -Math.cos(v.rad);
  const upSlopeX = -Math.cos(v.rad), upSlopeY = -Math.sin(v.rad);
  const alongX = Math.cos(v.rad) * Math.sign(v.a || 1);
  const alongY = -Math.sin(v.rad) * Math.sign(v.a || 1);
  const block = `<g transform="translate(${bx} ${by}) rotate(${-v.theta})"><rect x="-42" y="-34" width="84" height="68" rx="12" fill="#fff" stroke="#213043" stroke-width="6"/><circle cx="-24" cy="45" r="8" fill="#213043"/><circle cx="24" cy="45" r="8" fill="#213043"/></g>`;
  const trail = motion.trail.map((q, i) => {
    const px = baseX + len * q;
    const py = baseY - height * q;
    const alpha = 0.18 + i / Math.max(1, motion.trail.length) * 0.55;
    return `<circle cx="${px}" cy="${py}" r="${5 + i * 0.4}" fill="#ff8b3d" opacity="${alpha.toFixed(2)}"/>`;
  }).join('');
  const forceScale = 6;
  document.getElementById('drawing').innerHTML = `
    <polygon points="${baseX},${baseY} ${topX},${topY} ${topX},${baseY}" fill="#deebff" stroke="#213043" stroke-width="4"/>
    <line x1="${baseX}" y1="${baseY}" x2="${topX}" y2="${topY}" stroke="#213043" stroke-width="5"/>
    <path d="M${baseX} ${baseY + 20}H${topX}" stroke="#c7d7e4" stroke-width="4"/>
    ${trail}
    ${block}
    ${line(bx, by, bx, by + 95, '#2457c5', 'arrowB', 'mg')}
    ${line(bx, by, bx + nx * Math.min(150, v.N * forceScale), by + ny * Math.min(150, v.N * forceScale), '#1f8a70', 'arrowG', 'N')}
    ${line(bx, by, bx + upSlopeX * Math.min(120, v.f * forceScale), by + upSlopeY * Math.min(120, v.f * forceScale), '#d63f64', 'arrowR', 'f')}
    ${line(bx, by, bx + alongX * Math.min(140, Math.abs(v.a) * 24 + 28), by + alongY * Math.min(140, Math.abs(v.a) * 24 + 28), '#ff8b3d', 'arrowO', 'F')}
    <text x="104" y="74" font-size="21" fill="#62717d">滑块沿斜面运动，变量改变时受力和加速度同步更新</text>`;
}

function animate(now) {
  if (!motion.last) motion.last = now;
  const dt = Math.min(0.05, (now - motion.last) / 1000);
  motion.last = now;
  if (motion.playing && Math.abs(motion.a) >= 0.05) {
    const scaledA = motion.a / 18;
    motion.vel += scaledA * dt;
    motion.pos += motion.vel * dt;
    if (motion.pos > 0.92 || motion.pos < 0.08) {
      motion.pos = motion.a >= 0 ? 0.08 : 0.92;
      motion.vel = 0;
      motion.trail = [];
    }
  }
  motion.trail.push(motion.pos);
  if (motion.trail.length > 16) motion.trail.shift();
  updateValues();
  drawIncline();
  requestAnimationFrame(animate);
}

resetMotion(false);
updateValues();
drawIncline();
requestAnimationFrame(animate);
"""
    return page("斜面摩擦力互动题页", body, script)


def projectile() -> str:
    body = """<header><h1>平抛运动互动题页</h1><div class="subtitle">调节初速度和高度，播放小球沿抛物线运动的过程。</div></header>
    <section class="grid"><aside class="panel">
      <h2>题目</h2><p class="note">小球以水平初速度 $v_0$ 从高度 $h$ 处抛出，忽略空气阻力，求落地时间、水平位移和落地速度。</p>
      <label><span class="row"><span>初速度 v₀</span><output id="vOut"></output></span><input id="v0" type="range" min="2" max="30" step="0.5" value="12"></label>
      <label><span class="row"><span>高度 h</span><output id="hOut"></output></span><input id="h" type="range" min="2" max="80" step="1" value="20"></label>
      <label><span class="row"><span>重力加速度 g</span><output id="gOut"></output></span><input id="g" type="range" min="9.0" max="10.0" step="0.01" value="9.8"></label>
      <div class="result" id="answer"></div>
      <div class="formula">$$t=\\sqrt{2h/g}$$ $$x=v_0t$$ $$v_y=gt$$</div>
      <p class="note">易错点：轨迹弯曲不代表水平速度变化。</p>
    </aside><section class="panel">
      <svg viewBox="0 0 720 560"><g id="drawing"></g></svg>
      <div class="controls"><button id="playPause">暂停</button><button id="resetMotion" class="secondary">重置运动</button></div>
    </section></section>"""
    script = r"""
const projectileMotion = { tau: 0, playing: true, last: 0 };
for (const id of ['v0','h','g']) document.getElementById(id).addEventListener('input', () => resetProjectile(true));
document.getElementById('playPause').addEventListener('click', () => {
  projectileMotion.playing = !projectileMotion.playing;
  document.getElementById('playPause').textContent = projectileMotion.playing ? '暂停' : '播放';
});
document.getElementById('resetMotion').addEventListener('click', () => resetProjectile(true));

function projectileValues() {
  const v0 = +document.getElementById('v0').value;
  const h = +document.getElementById('h').value;
  const g = +document.getElementById('g').value;
  const t = Math.sqrt(2 * h / g);
  const x = v0 * t;
  const vy = g * t;
  const v = Math.sqrt(v0 * v0 + vy * vy);
  return { v0, h, g, t, x, vy, v };
}

function resetProjectile(drawNow) {
  projectileMotion.tau = 0;
  projectileMotion.last = performance.now();
  if (drawNow) drawProjectile();
}

function drawProjectile() {
  const v = projectileValues();
  document.getElementById('vOut').textContent = `${v.v0.toFixed(1)} m/s`;
  document.getElementById('hOut').textContent = `${v.h.toFixed(0)} m`;
  document.getElementById('gOut').textContent = `${v.g.toFixed(2)} m/s²`;
  document.getElementById('answer').textContent = `t=${v.t.toFixed(2)}s, x=${v.x.toFixed(1)}m, v=${v.v.toFixed(1)}m/s`;
  const originX = 80, originY = 88, groundY = 455;
  const width = 600;
  const sx = width / v.x;
  const sy = (groundY - originY) / v.h;
  let path = '';
  for (let i = 0; i <= 48; i++) {
    const tt = v.t * i / 48;
    const px = originX + v.v0 * tt * sx;
    const py = originY + 0.5 * v.g * tt * tt * sy;
    path += `${i ? 'L' : 'M'}${px.toFixed(1)} ${py.toFixed(1)} `;
  }
  const currentT = v.t * projectileMotion.tau;
  const ballX = originX + v.v0 * currentT * sx;
  const ballY = originY + 0.5 * v.g * currentT * currentT * sy;
  const vyNow = v.g * currentT;
  document.getElementById('drawing').innerHTML = `
    <rect x="58" y="70" width="24" height="${groundY - 70}" fill="#d9e3eb"/>
    <line x1="45" y1="${groundY}" x2="690" y2="${groundY}" stroke="#213043" stroke-width="4"/>
    <path d="${path}" fill="none" stroke="#d63f64" stroke-width="6" stroke-linecap="round"/>
    <circle cx="${ballX}" cy="${ballY}" r="15" fill="#ff8b3d"/>
    <line x1="${ballX}" y1="${ballY}" x2="${ballX + 86}" y2="${ballY}" stroke="#1f8a70" stroke-width="7" stroke-linecap="round"/>
    <line x1="${ballX}" y1="${ballY}" x2="${ballX}" y2="${ballY + Math.min(120, vyNow * 9 + 18)}" stroke="#2457c5" stroke-width="7" stroke-linecap="round"/>
    <text x="${ballX + 92}" y="${ballY + 6}" fill="#1f8a70" font-size="22" font-weight="800">vₓ</text>
    <text x="${ballX + 12}" y="${ballY + Math.min(130, vyNow * 9 + 28)}" fill="#2457c5" font-size="22" font-weight="800">vᵧ</text>
    <text x="96" y="56" font-size="21" fill="#62717d">小球按平抛方程随时间运动，速度分量同步显示</text>`;
}

function animateProjectile(now) {
  if (!projectileMotion.last) projectileMotion.last = now;
  const dt = Math.min(0.05, (now - projectileMotion.last) / 1000);
  projectileMotion.last = now;
  if (projectileMotion.playing) projectileMotion.tau = (projectileMotion.tau + dt / 2.8) % 1;
  drawProjectile();
  requestAnimationFrame(animateProjectile);
}

resetProjectile(false);
drawProjectile();
requestAnimationFrame(animateProjectile);
"""
    return page("平抛运动互动题页", body, script)


def circular() -> str:
    body = """<header><h1>圆周运动互动题页</h1><div class="subtitle">调节质量、半径和速度，播放小球做圆周运动并观察向心力。</div></header>
    <section class="grid"><aside class="panel">
      <h2>题目</h2><p class="note">质量为 $m$ 的小球以速度 $v$ 做半径为 $r$ 的匀速圆周运动，求所需向心力大小。</p>
      <label><span class="row"><span>质量 m</span><output id="mOut"></output></span><input id="m" type="range" min="0.2" max="5" step="0.1" value="1.5"></label>
      <label><span class="row"><span>半径 r</span><output id="rOut"></output></span><input id="r" type="range" min="0.5" max="6" step="0.1" value="2"></label>
      <label><span class="row"><span>速度 v</span><output id="vOut"></output></span><input id="v" type="range" min="0.5" max="12" step="0.1" value="4"></label>
      <div class="result" id="answer"></div>
      <div class="formula">$$F=mv^2/r$$ $$a=v^2/r$$</div>
      <p class="note">向心力不是额外的新力，它是指向圆心的合力效果。</p>
    </aside><section class="panel">
      <svg viewBox="0 0 720 560"><g id="drawing"></g></svg>
      <div class="controls"><button id="playPause">暂停</button><button id="resetMotion" class="secondary">重置运动</button></div>
    </section></section>"""
    script = r"""
const circleMotion = { angle: -0.8, playing: true, last: 0 };
for (const id of ['m','r','v']) document.getElementById(id).addEventListener('input', drawCircular);
document.getElementById('playPause').addEventListener('click', () => {
  circleMotion.playing = !circleMotion.playing;
  document.getElementById('playPause').textContent = circleMotion.playing ? '暂停' : '播放';
});
document.getElementById('resetMotion').addEventListener('click', () => { circleMotion.angle = -0.8; drawCircular(); });

function circularValues() {
  const m = +document.getElementById('m').value;
  const r = +document.getElementById('r').value;
  const v = +document.getElementById('v').value;
  const F = m * v * v / r;
  const a = v * v / r;
  return { m, r, v, F, a };
}

function drawCircular() {
  const v = circularValues();
  document.getElementById('mOut').textContent = `${v.m.toFixed(1)} kg`;
  document.getElementById('rOut').textContent = `${v.r.toFixed(1)} m`;
  document.getElementById('vOut').textContent = `${v.v.toFixed(1)} m/s`;
  document.getElementById('answer').textContent = `F=${v.F.toFixed(2)}N, a=${v.a.toFixed(2)}m/s²`;
  const cx = 360, cy = 280, rr = 95 + v.r * 28;
  const bx = cx + rr * Math.cos(circleMotion.angle);
  const by = cy + rr * Math.sin(circleMotion.angle);
  const tx = -Math.sin(circleMotion.angle), ty = Math.cos(circleMotion.angle);
  document.getElementById('drawing').innerHTML = `
    <circle cx="${cx}" cy="${cy}" r="${rr}" fill="#eef6fb" stroke="#213043" stroke-width="5"/>
    <circle cx="${cx}" cy="${cy}" r="7" fill="#213043"/>
    <path d="M${cx} ${cy}L${bx} ${by}" stroke="#9fb5c8" stroke-width="3" stroke-dasharray="8 8"/>
    <circle cx="${bx}" cy="${by}" r="${14 + v.m * 3.2}" fill="#ff8b3d"/>
    <line x1="${bx}" y1="${by}" x2="${cx + (bx - cx) * 0.48}" y2="${cy + (by - cy) * 0.48}" stroke="#2457c5" stroke-width="${Math.min(16, 5 + v.F / 8)}" stroke-linecap="round"/>
    <line x1="${bx}" y1="${by}" x2="${bx + tx * 105}" y2="${by + ty * 105}" stroke="#1f8a70" stroke-width="7" stroke-linecap="round"/>
    <text x="${cx + (bx - cx) * 0.58}" y="${cy + (by - cy) * 0.58}" fill="#2457c5" font-size="24" font-weight="800">F</text>
    <text x="${bx + tx * 112}" y="${by + ty * 112}" fill="#1f8a70" font-size="24" font-weight="800">v</text>
    <text x="92" y="58" font-size="21" fill="#62717d">小球持续转动；速度沿切线，向心合力指向圆心</text>`;
}

function animateCircular(now) {
  if (!circleMotion.last) circleMotion.last = now;
  const dt = Math.min(0.05, (now - circleMotion.last) / 1000);
  circleMotion.last = now;
  const v = circularValues();
  if (circleMotion.playing) circleMotion.angle += dt * (0.5 + v.v / 3.5);
  drawCircular();
  requestAnimationFrame(animateCircular);
}

drawCircular();
requestAnimationFrame(animateCircular);
"""
    return page("圆周运动互动题页", body, script)


TEMPLATES = {"incline": incline, "projectile": projectile, "circular": circular}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--template", choices=sorted(TEMPLATES), default="incline")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    Path(args.output).write_text(TEMPLATES[args.template](), encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
