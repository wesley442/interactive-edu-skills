#!/usr/bin/env python3
"""Generate self-contained interactive high-school mechanics HTML pages."""

from __future__ import annotations

import argparse
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent


def read_template(name: str) -> str:
    return (SCRIPT_DIR.parent / "templates" / name).read_text(encoding="utf-8")


def page(title: str, body: str, script: str) -> str:
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <script>
    window.MathJax = {{ tex: {{ inlineMath: [['$', '$'], ['\\\\(', '\\\\)']], displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']] }} }};
  </script>
  <script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    :root {{
      --bg: #111827;
      --panel: #1c2434;
      --card: rgba(255,255,255,0.07);
      --line: rgba(255,255,255,0.12);
      --text: #e8edf6;
      --muted: #9aa7b8;
      --blue: #64b5f6;
      --green: #66bb6a;
      --red: #ef5350;
      --orange: #ffa726;
      --purple: #ce93d8;
      --cyan: #26c6da;
      --gold: #ffd54f;
    }}
    body {{
      font-family: "Segoe UI", "Microsoft YaHei", sans-serif;
      color: var(--text);
      background: radial-gradient(circle at 15% 15%, rgba(100,181,246,.16), transparent 30%),
                  radial-gradient(circle at 90% 85%, rgba(102,187,106,.12), transparent 34%),
                  linear-gradient(135deg, #151827 0%, #17213a 54%, #0e3555 100%);
      min-height: 100vh;
      overflow-x: hidden;
    }}
    .app {{ min-height: 100vh; display: flex; flex-direction: column; }}
    .header {{
      padding: 14px 22px 12px;
      border-bottom: 1px solid var(--line);
      background: rgba(255,255,255,0.045);
      display: flex;
      align-items: center;
      gap: 16px;
      flex-wrap: wrap;
    }}
    .badge {{
      background: linear-gradient(135deg, #1565c0, #7c5cfc);
      color: white;
      font-size: 12px;
      font-weight: 800;
      padding: 4px 12px;
      border-radius: 999px;
      letter-spacing: .5px;
    }}
    h1 {{ font-size: 20px; letter-spacing: .5px; color: var(--text); }}
    .subtitle {{ color: var(--muted); font-size: 13px; margin-left: auto; }}
    .main-layout {{ flex: 1; display: flex; min-height: 0; }}
    .left-panel {{
      width: 40%;
      min-width: 390px;
      max-width: 540px;
      overflow-y: auto;
      padding: 14px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      border-right: 1px solid var(--line);
    }}
    .right-panel {{
      flex: 1;
      overflow-y: auto;
      padding: 14px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .left-panel::-webkit-scrollbar, .right-panel::-webkit-scrollbar {{ width: 5px; }}
    .left-panel::-webkit-scrollbar-thumb, .right-panel::-webkit-scrollbar-thumb {{ background: rgba(100,181,246,.4); border-radius: 4px; }}
    .card {{
      background: var(--card);
      border: 1px solid var(--line);
      border-radius: 12px;
      padding: 14px;
      box-shadow: 0 10px 30px rgba(0,0,0,.23);
      backdrop-filter: blur(10px);
    }}
    .card-title {{
      font-size: 15px;
      color: var(--blue);
      font-weight: 800;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 7px;
    }}
    .card-title::before {{
      content: "";
      width: 4px;
      height: 16px;
      background: var(--blue);
      border-radius: 2px;
      display: inline-block;
    }}
    .problem-text, .note {{ color: #cbd5e1; line-height: 1.75; font-size: 13px; }}
    .problem-text strong {{ color: white; }}
    .slider-group {{ display: flex; flex-direction: column; gap: 11px; }}
    .slider-item {{ display: flex; flex-direction: column; gap: 5px; }}
    .slider-label {{ display: flex; justify-content: space-between; color: #b8c4d6; font-size: 13px; }}
    .slider-label span:last-child {{ color: white; font-weight: 800; font-variant-numeric: tabular-nums; }}
    input[type=range] {{
      -webkit-appearance: none;
      width: 100%;
      height: 6px;
      border-radius: 3px;
      background: rgba(255,255,255,.16);
      outline: none;
      cursor: pointer;
    }}
    input[type=range]::-webkit-slider-thumb {{
      -webkit-appearance: none;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: var(--blue);
      box-shadow: 0 0 9px rgba(100,181,246,.65);
    }}
    .results-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }}
    .result-item {{
      background: rgba(255,255,255,.055);
      border-left: 3px solid var(--blue);
      border-radius: 8px;
      padding: 8px 10px;
    }}
    .result-label {{ color: var(--muted); font-size: 11px; margin-bottom: 3px; }}
    .result-value {{ color: white; font-size: 15px; font-weight: 800; font-variant-numeric: tabular-nums; }}
    .status-box {{
      border-radius: 10px;
      padding: 12px 14px;
      text-align: center;
      font-weight: 900;
      letter-spacing: .5px;
      border: 2px solid var(--green);
      color: var(--green);
      background: rgba(102,187,106,.15);
    }}
    .status-warning {{ border-color: var(--orange); color: var(--orange); background: rgba(255,167,38,.14); }}
    .tabs {{ display: flex; flex-wrap: wrap; gap: 5px; margin-bottom: 10px; }}
    .tab-btn {{
      border: 1px solid var(--line);
      border-radius: 7px;
      padding: 6px 12px;
      color: var(--muted);
      background: rgba(255,255,255,.05);
      cursor: pointer;
      font: inherit;
      font-size: 12px;
    }}
    .tab-btn.active {{ color: var(--blue); border-color: var(--blue); background: rgba(100,181,246,.18); }}
    .tab-content {{ display: none; }}
    .tab-content.active {{ display: block; }}
    .formula-steps {{ display: flex; flex-direction: column; gap: 8px; }}
    .step {{
      background: rgba(255,255,255,.045);
      border-left: 3px solid var(--blue);
      border-radius: 8px;
      padding: 9px 12px;
      color: #d9e2f1;
      line-height: 1.65;
      font-size: 13px;
    }}
    .warning-item {{
      background: rgba(255,167,38,.10);
      border: 1px solid rgba(255,167,38,.28);
      color: #ffcc80;
      border-radius: 8px;
      padding: 9px 12px;
      line-height: 1.6;
      font-size: 13px;
      margin-bottom: 8px;
    }}
    .canvas-wrapper {{
      flex: 1;
      min-height: 430px;
      border: 1px solid var(--line);
      border-radius: 12px;
      background: rgba(0,0,0,.32);
      overflow: hidden;
      position: relative;
    }}
    canvas {{ width: 100%; height: 100%; display: block; }}
    .controls {{ display: flex; flex-wrap: wrap; gap: 8px; }}
    .btn {{
      border: none;
      border-radius: 8px;
      padding: 8px 15px;
      color: white;
      font-family: inherit;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      background: linear-gradient(135deg, #1565c0, #1976d2);
      box-shadow: 0 2px 8px rgba(25,118,210,.35);
    }}
    .btn-secondary {{ background: rgba(255,255,255,.10); color: var(--text); border: 1px solid var(--line); box-shadow: none; }}
    .btn-warning {{ background: linear-gradient(135deg, #e65100, #f57c00); }}
    .variants-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }}
    .variant-item {{
      background: rgba(255,255,255,.05);
      border: 1px solid rgba(255,255,255,.08);
      border-radius: 8px;
      padding: 10px;
      color: #c8d3e0;
      font-size: 12px;
      line-height: 1.55;
    }}
    .variant-item strong {{ display: block; color: var(--blue); margin-bottom: 4px; }}
    .data-table {{ width: 100%; border-collapse: collapse; font-size: 12px; }}
    .data-table th {{ color: var(--blue); background: rgba(100,181,246,.18); padding: 6px 8px; }}
    .data-table td {{ color: #d1d9e6; padding: 5px 8px; text-align: center; border-bottom: 1px solid rgba(255,255,255,.06); }}
    @media (max-width: 900px) {{
      body {{ overflow: auto; }}
      .main-layout {{ flex-direction: column; }}
      .left-panel {{ width: 100%; max-width: none; min-width: 0; border-right: 0; border-bottom: 1px solid var(--line); }}
      .right-panel {{ min-height: 560px; }}
      .variants-grid {{ grid-template-columns: 1fr; }}
    }}
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
    return read_template("incline-friction.html")


def projectile() -> str:
    body = """<div class="header">
      <div class="badge">高中物理</div>
      <h1>平抛运动 · 互动动画</h1>
      <div class="subtitle">运动分解 · 轨迹动画 · 可调变量</div>
    </div>
    <div class="main-layout">
      <aside class="left-panel">
        <div class="card">
          <div class="card-title">题目描述</div>
          <div class="problem-text">小球以水平初速度 <strong>v₀</strong> 从高度 <strong>h</strong> 处水平抛出，忽略空气阻力。求落地时间、水平位移、落地竖直速度和合速度。</div>
        </div>
        <div class="card">
          <div class="card-title">调节参数</div>
          <div class="slider-group">
            <div class="slider-item"><div class="slider-label"><span>初速度 v₀</span><span id="vOut"></span></div><input id="v0" type="range" min="2" max="30" step="0.5" value="12"></div>
            <div class="slider-item"><div class="slider-label"><span>高度 h</span><span id="hOut"></span></div><input id="h" type="range" min="2" max="80" step="1" value="20"></div>
            <div class="slider-item"><div class="slider-label"><span>重力加速度 g</span><span id="gOut"></span></div><input id="g" type="range" min="9.0" max="10.0" step="0.01" value="9.8"></div>
          </div>
        </div>
        <div class="card">
          <div class="card-title">实时计算结果</div>
          <div class="results-grid">
            <div class="result-item"><div class="result-label">落地时间 t</div><div class="result-value" id="resT"></div></div>
            <div class="result-item"><div class="result-label">水平位移 x</div><div class="result-value" id="resX"></div></div>
            <div class="result-item"><div class="result-label">竖直速度 vy</div><div class="result-value" id="resVy"></div></div>
            <div class="result-item"><div class="result-label">合速度 v</div><div class="result-value" id="resV"></div></div>
          </div>
        </div>
        <div class="card">
          <div class="card-title">运动状态</div>
          <div class="status-box" id="statusBox"></div>
        </div>
        <div class="card">
          <div class="tabs">
            <button class="tab-btn active" onclick="switchTab('model')">物理模型</button>
            <button class="tab-btn" onclick="switchTab('formula')">公式推导</button>
            <button class="tab-btn" onclick="switchTab('warnings')">易错点</button>
          </div>
          <div class="tab-content active" id="tab-model">
            <div class="step">平抛运动可分解为两个互不影响的方向：水平方向匀速直线运动，竖直方向自由落体运动。</div>
            <div class="step">研究对象是小球；约束条件是初速度水平、空气阻力忽略、竖直初速度为 0。</div>
          </div>
          <div class="tab-content" id="tab-formula">
            <div class="formula-steps">
              <div class="step">竖直方向：$h=\\frac12gt^2 \\Rightarrow t=\\sqrt{2h/g}$</div>
              <div class="step">水平方向：$x=v_0t$，所以高度决定飞行时间，初速度决定水平位移。</div>
              <div class="step">落地时：$v_y=gt$，$v=\\sqrt{v_0^2+v_y^2}$。</div>
            </div>
          </div>
          <div class="tab-content" id="tab-warnings">
            <div class="warning-item">水平速度不变，轨迹变弯不是因为水平方向有加速度。</div>
            <div class="warning-item">落地时间只由高度和重力加速度决定，与水平初速度无关。</div>
            <div class="warning-item">合速度方向会逐渐向下偏转，不能把合速度当作水平速度。</div>
          </div>
        </div>
      </aside>
      <section class="right-panel">
        <div class="controls">
          <button class="btn" id="playPause">暂停动画</button>
          <button class="btn btn-secondary" id="resetMotion">重置运动</button>
          <button class="btn btn-warning" id="toggleTrace">隐藏轨迹</button>
        </div>
        <div class="canvas-wrapper"><canvas id="mainCanvas"></canvas></div>
        <div class="card">
          <div class="card-title">变式与课堂提问</div>
          <div class="variants-grid">
            <div class="variant-item"><strong>变式 1：高度加倍</strong>落地时间变为原来的 $\\sqrt2$ 倍，水平位移也变为 $\\sqrt2$ 倍。</div>
            <div class="variant-item"><strong>变式 2：初速度加倍</strong>落地时间不变，水平位移加倍。</div>
            <div class="variant-item"><strong>课堂提问</strong>为什么小球刚抛出时速度水平，但落地时速度斜向下？</div>
          </div>
        </div>
      </section>
    </div>"""
    script = r"""
const projectileMotion = { tau: 0, playing: true, last: 0, trace: true };
const canvas = document.getElementById('mainCanvas');
const ctx = canvas.getContext('2d');
for (const id of ['v0','h','g']) document.getElementById(id).addEventListener('input', () => resetProjectile(true));
document.getElementById('playPause').addEventListener('click', () => {
  projectileMotion.playing = !projectileMotion.playing;
  document.getElementById('playPause').textContent = projectileMotion.playing ? '暂停动画' : '播放动画';
});
document.getElementById('resetMotion').addEventListener('click', () => resetProjectile(true));
document.getElementById('toggleTrace').addEventListener('click', () => {
  projectileMotion.trace = !projectileMotion.trace;
  document.getElementById('toggleTrace').textContent = projectileMotion.trace ? '隐藏轨迹' : '显示轨迹';
});

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

function resizeCanvas() {
  const wrapper = canvas.parentElement;
  const dpr = window.devicePixelRatio || 1;
  canvas.width = Math.floor(wrapper.clientWidth * dpr);
  canvas.height = Math.floor(wrapper.clientHeight * dpr);
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
}

function drawArrow(x1, y1, x2, y2, color, label) {
  const dx = x2 - x1, dy = y2 - y1;
  const len = Math.hypot(dx, dy);
  if (len < 2) return;
  const angle = Math.atan2(dy, dx);
  ctx.save();
  ctx.strokeStyle = color;
  ctx.fillStyle = color;
  ctx.lineWidth = 3;
  ctx.shadowColor = color;
  ctx.shadowBlur = 6;
  ctx.beginPath();
  ctx.moveTo(x1, y1);
  ctx.lineTo(x2, y2);
  ctx.stroke();
  ctx.beginPath();
  ctx.moveTo(x2, y2);
  ctx.lineTo(x2 - 12 * Math.cos(angle - 0.45), y2 - 12 * Math.sin(angle - 0.45));
  ctx.lineTo(x2 - 12 * Math.cos(angle + 0.45), y2 - 12 * Math.sin(angle + 0.45));
  ctx.closePath();
  ctx.fill();
  ctx.shadowBlur = 0;
  ctx.font = 'bold 13px Segoe UI, Microsoft YaHei';
  ctx.fillText(label, x2 + 6, y2 - 6);
  ctx.restore();
}

function drawProjectile() {
  const v = projectileValues();
  document.getElementById('vOut').textContent = `${v.v0.toFixed(1)} m/s`;
  document.getElementById('hOut').textContent = `${v.h.toFixed(0)} m`;
  document.getElementById('gOut').textContent = `${v.g.toFixed(2)} m/s²`;
  document.getElementById('resT').textContent = `${v.t.toFixed(2)} s`;
  document.getElementById('resX').textContent = `${v.x.toFixed(1)} m`;
  document.getElementById('resVy').textContent = `${v.vy.toFixed(1)} m/s`;
  document.getElementById('resV').textContent = `${v.v.toFixed(1)} m/s`;
  document.getElementById('statusBox').textContent = `当前飞行进度 ${(projectileMotion.tau * 100).toFixed(0)}%，水平速度保持 ${v.v0.toFixed(1)} m/s`;
  resizeCanvas();
  const W = canvas.parentElement.clientWidth, H = canvas.parentElement.clientHeight;
  ctx.clearRect(0, 0, W, H);
  const originX = 72, originY = 80, groundY = H - 64, rightPad = 58;
  const sx = (W - originX - rightPad) / v.x;
  const sy = (groundY - originY) / v.h;
  ctx.save();
  ctx.strokeStyle = 'rgba(255,255,255,.08)';
  ctx.lineWidth = 1;
  for (let x = 0; x < W; x += 44) { ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, H); ctx.stroke(); }
  for (let y = 0; y < H; y += 44) { ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke(); }
  ctx.restore();
  ctx.fillStyle = 'rgba(100,181,246,.14)';
  ctx.fillRect(originX - 24, originY - 18, 24, groundY - originY + 18);
  ctx.fillStyle = 'rgba(255,255,255,.10)';
  ctx.fillRect(0, groundY, W, H - groundY);
  ctx.strokeStyle = 'rgba(255,255,255,.35)';
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.moveTo(35, groundY);
  ctx.lineTo(W - 28, groundY);
  ctx.stroke();
  ctx.strokeStyle = '#ef5350';
  ctx.lineWidth = 4;
  ctx.beginPath();
  for (let i = 0; i <= 90; i++) {
    const tt = v.t * i / 90;
    const px = originX + v.v0 * tt * sx;
    const py = originY + 0.5 * v.g * tt * tt * sy;
    if (i === 0) ctx.moveTo(px, py); else ctx.lineTo(px, py);
  }
  if (projectileMotion.trace) ctx.stroke();
  const currentT = v.t * projectileMotion.tau;
  const ballX = originX + v.v0 * currentT * sx;
  const ballY = originY + 0.5 * v.g * currentT * currentT * sy;
  const vyNow = v.g * currentT;
  ctx.fillStyle = '#ffb74d';
  ctx.shadowColor = '#ffb74d';
  ctx.shadowBlur = 16;
  ctx.beginPath();
  ctx.arc(ballX, ballY, 14, 0, Math.PI * 2);
  ctx.fill();
  ctx.shadowBlur = 0;
  drawArrow(ballX, ballY, ballX + 78, ballY, '#66bb6a', 'vₓ');
  drawArrow(ballX, ballY, ballX, ballY + Math.min(118, 16 + vyNow * 6), '#64b5f6', 'vᵧ');
  drawArrow(ballX, ballY, ballX + 70, ballY + Math.min(112, 16 + vyNow * 5), '#ce93d8', 'v');
  ctx.fillStyle = '#9aa7b8';
  ctx.font = '13px Segoe UI, Microsoft YaHei';
  ctx.fillText(`落地点 x = ${v.x.toFixed(1)} m`, Math.max(originX + 10, W - 210), groundY - 18);
  ctx.fillText(`h = ${v.h.toFixed(0)} m`, originX + 10, (originY + groundY) / 2);
  document.getElementById('vOut').textContent = `${v.v0.toFixed(1)} m/s`;
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

function switchTab(name) {
  document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.toggle('active', btn.getAttribute('onclick').includes("'" + name + "'")));
  document.querySelectorAll('.tab-content').forEach(c => c.classList.toggle('active', c.id === 'tab-' + name));
  if (window.MathJax) MathJax.typesetPromise();
}
"""
    return page("平抛运动互动题页", body, script)


def circular() -> str:
    body = """<div class="header">
      <div class="badge">高中物理</div>
      <h1>圆周运动 · 互动模拟</h1>
      <div class="subtitle">向心加速度 · 向心力 · 周期与角速度</div>
    </div>
    <div class="main-layout">
      <aside class="left-panel">
        <div class="card">
          <div class="card-title">题目描述</div>
          <div class="problem-text">质量为 <strong>m</strong> 的小球以速度 <strong>v</strong> 做半径为 <strong>r</strong> 的匀速圆周运动。求向心加速度、所需向心力、周期和角速度。</div>
        </div>
        <div class="card">
          <div class="card-title">调节参数</div>
          <div class="slider-group">
            <div class="slider-item"><div class="slider-label"><span>质量 m</span><span id="mOut"></span></div><input id="m" type="range" min="0.2" max="5" step="0.1" value="1.5"></div>
            <div class="slider-item"><div class="slider-label"><span>半径 r</span><span id="rOut"></span></div><input id="r" type="range" min="0.5" max="6" step="0.1" value="2"></div>
            <div class="slider-item"><div class="slider-label"><span>速度 v</span><span id="vOut"></span></div><input id="v" type="range" min="0.5" max="12" step="0.1" value="4"></div>
          </div>
        </div>
        <div class="card">
          <div class="card-title">实时计算结果</div>
          <div class="results-grid">
            <div class="result-item"><div class="result-label">向心加速度 a</div><div class="result-value" id="resA"></div></div>
            <div class="result-item"><div class="result-label">向心力 F</div><div class="result-value" id="resF"></div></div>
            <div class="result-item"><div class="result-label">周期 T</div><div class="result-value" id="resT"></div></div>
            <div class="result-item"><div class="result-label">角速度 ω</div><div class="result-value" id="resW"></div></div>
          </div>
        </div>
        <div class="card">
          <div class="card-title">关键结论</div>
          <div class="status-box" id="statusBox"></div>
        </div>
        <div class="card">
          <div class="tabs">
            <button class="tab-btn active" onclick="switchTab('model')">物理模型</button>
            <button class="tab-btn" onclick="switchTab('formula')">公式推导</button>
            <button class="tab-btn" onclick="switchTab('warnings')">易错点</button>
          </div>
          <div class="tab-content active" id="tab-model">
            <div class="step">匀速圆周运动的“匀速”指速率不变，速度方向不断改变，因此仍有加速度。</div>
            <div class="step">向心加速度始终指向圆心；所需向心力是指向圆心的合力效果。</div>
          </div>
          <div class="tab-content" id="tab-formula">
            <div class="formula-steps">
              <div class="step">向心加速度：$a=\\frac{v^2}{r}$</div>
              <div class="step">向心力：$F=ma=\\frac{mv^2}{r}$</div>
              <div class="step">周期与角速度：$T=\\frac{2\\pi r}{v}$，$\\omega=\\frac{v}{r}$。</div>
            </div>
          </div>
          <div class="tab-content" id="tab-warnings">
            <div class="warning-item">向心力不是额外一种新力，要说明由拉力、摩擦力、重力分力等具体力提供。</div>
            <div class="warning-item">速度方向沿切线，向心加速度方向指向圆心，两者互相垂直。</div>
            <div class="warning-item">速度变为 2 倍时，向心力变为 4 倍，这是常见压轴考点。</div>
          </div>
        </div>
      </aside>
      <section class="right-panel">
        <div class="controls">
          <button class="btn" id="playPause">暂停动画</button>
          <button class="btn btn-secondary" id="resetMotion">重置位置</button>
          <button class="btn btn-warning" id="toggleTrail">隐藏轨迹</button>
        </div>
        <div class="canvas-wrapper"><canvas id="mainCanvas"></canvas></div>
        <div class="card">
          <div class="card-title">变式与课堂提问</div>
          <div class="variants-grid">
            <div class="variant-item"><strong>变式 1：速度加倍</strong>$F=mv^2/r$，向心力变为原来的 4 倍。</div>
            <div class="variant-item"><strong>变式 2：半径加倍</strong>速度不变时，向心力变为原来的一半，周期变为 2 倍。</div>
            <div class="variant-item"><strong>课堂提问</strong>小球速率不变，为什么还说它有加速度？</div>
          </div>
        </div>
      </section>
    </div>"""
    script = r"""
const circleMotion = { angle: -0.8, playing: true, last: 0, trail: true, points: [] };
const canvas = document.getElementById('mainCanvas');
const ctx = canvas.getContext('2d');
for (const id of ['m','r','v']) document.getElementById(id).addEventListener('input', drawCircular);
document.getElementById('playPause').addEventListener('click', () => {
  circleMotion.playing = !circleMotion.playing;
  document.getElementById('playPause').textContent = circleMotion.playing ? '暂停动画' : '播放动画';
});
document.getElementById('resetMotion').addEventListener('click', () => { circleMotion.angle = -0.8; circleMotion.points = []; drawCircular(); });
document.getElementById('toggleTrail').addEventListener('click', () => {
  circleMotion.trail = !circleMotion.trail;
  document.getElementById('toggleTrail').textContent = circleMotion.trail ? '隐藏轨迹' : '显示轨迹';
});

function circularValues() {
  const m = +document.getElementById('m').value;
  const r = +document.getElementById('r').value;
  const v = +document.getElementById('v').value;
  const F = m * v * v / r;
  const a = v * v / r;
  const T = 2 * Math.PI * r / v;
  const omega = v / r;
  return { m, r, v, F, a, T, omega };
}

function resizeCanvas() {
  const wrapper = canvas.parentElement;
  const dpr = window.devicePixelRatio || 1;
  canvas.width = Math.floor(wrapper.clientWidth * dpr);
  canvas.height = Math.floor(wrapper.clientHeight * dpr);
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
}

function drawArrow(x1, y1, x2, y2, color, label, width = 3) {
  const dx = x2 - x1, dy = y2 - y1;
  const len = Math.hypot(dx, dy);
  if (len < 2) return;
  const angle = Math.atan2(dy, dx);
  ctx.save();
  ctx.strokeStyle = color;
  ctx.fillStyle = color;
  ctx.lineWidth = width;
  ctx.shadowColor = color;
  ctx.shadowBlur = 6;
  ctx.beginPath();
  ctx.moveTo(x1, y1);
  ctx.lineTo(x2, y2);
  ctx.stroke();
  ctx.beginPath();
  ctx.moveTo(x2, y2);
  ctx.lineTo(x2 - 12 * Math.cos(angle - 0.45), y2 - 12 * Math.sin(angle - 0.45));
  ctx.lineTo(x2 - 12 * Math.cos(angle + 0.45), y2 - 12 * Math.sin(angle + 0.45));
  ctx.closePath();
  ctx.fill();
  ctx.shadowBlur = 0;
  ctx.font = 'bold 13px Segoe UI, Microsoft YaHei';
  ctx.fillText(label, x2 + 6, y2 - 6);
  ctx.restore();
}

function drawCircular() {
  const v = circularValues();
  document.getElementById('mOut').textContent = `${v.m.toFixed(1)} kg`;
  document.getElementById('rOut').textContent = `${v.r.toFixed(1)} m`;
  document.getElementById('vOut').textContent = `${v.v.toFixed(1)} m/s`;
  document.getElementById('resA').textContent = `${v.a.toFixed(2)} m/s²`;
  document.getElementById('resF').textContent = `${v.F.toFixed(2)} N`;
  document.getElementById('resT').textContent = `${v.T.toFixed(2)} s`;
  document.getElementById('resW').textContent = `${v.omega.toFixed(2)} rad/s`;
  document.getElementById('statusBox').textContent = `当前速度 ${v.v.toFixed(1)} m/s，向心力 ${v.F.toFixed(2)} N，由指向圆心的合力提供。`;
  resizeCanvas();
  const W = canvas.parentElement.clientWidth, H = canvas.parentElement.clientHeight;
  ctx.clearRect(0, 0, W, H);
  ctx.save();
  ctx.strokeStyle = 'rgba(255,255,255,.08)';
  ctx.lineWidth = 1;
  for (let x = 0; x < W; x += 44) { ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, H); ctx.stroke(); }
  for (let y = 0; y < H; y += 44) { ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(W, y); ctx.stroke(); }
  ctx.restore();
  const cx = W / 2, cy = H / 2 + 10, rr = Math.min(W, H) * (0.18 + v.r / 40);
  const bx = cx + rr * Math.cos(circleMotion.angle);
  const by = cy + rr * Math.sin(circleMotion.angle);
  const tx = -Math.sin(circleMotion.angle), ty = Math.cos(circleMotion.angle);
  circleMotion.points.push([bx, by]);
  if (circleMotion.points.length > 80) circleMotion.points.shift();
  if (circleMotion.trail) {
    ctx.strokeStyle = 'rgba(255,213,79,.45)';
    ctx.lineWidth = 3;
    ctx.beginPath();
    circleMotion.points.forEach(([x, y], i) => { if (i === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y); });
    ctx.stroke();
  }
  ctx.strokeStyle = 'rgba(100,181,246,.55)';
  ctx.lineWidth = 4;
  ctx.beginPath();
  ctx.arc(cx, cy, rr, 0, Math.PI * 2);
  ctx.stroke();
  ctx.setLineDash([8, 6]);
  ctx.strokeStyle = 'rgba(255,255,255,.28)';
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.moveTo(cx, cy);
  ctx.lineTo(bx, by);
  ctx.stroke();
  ctx.setLineDash([]);
  ctx.fillStyle = '#e8edf6';
  ctx.beginPath();
  ctx.arc(cx, cy, 6, 0, Math.PI * 2);
  ctx.fill();
  ctx.fillStyle = '#ffb74d';
  ctx.shadowColor = '#ffb74d';
  ctx.shadowBlur = 16;
  ctx.beginPath();
  ctx.arc(bx, by, 14 + v.m * 2.2, 0, Math.PI * 2);
  ctx.fill();
  ctx.shadowBlur = 0;
  drawArrow(bx, by, bx + tx * 110, by + ty * 110, '#66bb6a', 'v');
  drawArrow(bx, by, bx + (cx - bx) * 0.52, by + (cy - by) * 0.52, '#64b5f6', 'a/F', Math.min(9, 3 + v.F / 18));
  ctx.fillStyle = '#9aa7b8';
  ctx.font = '13px Segoe UI, Microsoft YaHei';
  ctx.fillText(`r = ${v.r.toFixed(1)} m`, cx + (bx - cx) * 0.5 + 8, cy + (by - cy) * 0.5 - 8);
  ctx.fillText('速度沿切线，向心加速度指向圆心', 22, 32);
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

function switchTab(name) {
  document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.toggle('active', btn.getAttribute('onclick').includes("'" + name + "'")));
  document.querySelectorAll('.tab-content').forEach(c => c.classList.toggle('active', c.id === 'tab-' + name));
  if (window.MathJax) MathJax.typesetPromise();
}
"""
    return page("圆周运动互动题页", body, script)


def spring_energy() -> str:
    body = """<div class="header">
      <div class="badge">高中物理</div><h1>弹簧能量 · 互动模拟</h1><div class="subtitle">胡克定律 · 能量转化 · 可调变量</div>
    </div>
    <div class="main-layout">
      <aside class="left-panel">
        <div class="card"><div class="card-title">题目描述</div><div class="problem-text">质量为 <strong>m</strong> 的小物块压缩劲度系数为 <strong>k</strong> 的轻弹簧，压缩量为 <strong>x</strong>。释放后忽略摩擦，求最大速度和弹性势能。</div></div>
        <div class="card"><div class="card-title">调节参数</div><div class="slider-group">
          <div class="slider-item"><div class="slider-label"><span>劲度系数 k</span><span id="kOut"></span></div><input id="k" type="range" min="50" max="800" step="10" value="300"></div>
          <div class="slider-item"><div class="slider-label"><span>质量 m</span><span id="mOut"></span></div><input id="m" type="range" min="0.2" max="5" step="0.1" value="1.2"></div>
          <div class="slider-item"><div class="slider-label"><span>压缩量 x</span><span id="xOut"></span></div><input id="x" type="range" min="0.05" max="0.6" step="0.01" value="0.25"></div>
        </div></div>
        <div class="card"><div class="card-title">实时计算结果</div><div class="results-grid">
          <div class="result-item"><div class="result-label">弹力 F=kx</div><div class="result-value" id="resF"></div></div>
          <div class="result-item"><div class="result-label">弹性势能 Ep</div><div class="result-value" id="resEp"></div></div>
          <div class="result-item"><div class="result-label">最大速度 vmax</div><div class="result-value" id="resV"></div></div>
          <div class="result-item"><div class="result-label">角频率 ω</div><div class="result-value" id="resW"></div></div>
        </div></div>
        <div class="card"><div class="card-title">状态提示</div><div class="status-box" id="statusBox"></div></div>
        <div class="card"><div class="tabs"><button class="tab-btn active" onclick="switchTab('model')">物理模型</button><button class="tab-btn" onclick="switchTab('formula')">公式推导</button><button class="tab-btn" onclick="switchTab('warnings')">易错点</button></div>
          <div class="tab-content active" id="tab-model"><div class="step">研究对象是小物块与弹簧系统；忽略摩擦时，弹性势能可以完全转化为动能。</div></div>
          <div class="tab-content" id="tab-formula"><div class="formula-steps"><div class="step">$E_p=\\frac12kx^2$</div><div class="step">$\\frac12kx^2=\\frac12mv_{max}^2 \\Rightarrow v_{max}=x\\sqrt{k/m}$</div><div class="step">$F=kx$，压缩量越大，初始弹力越大。</div></div></div>
          <div class="tab-content" id="tab-warnings"><div class="warning-item">最大速度出现在弹簧恢复原长处，不是刚释放瞬间。</div><div class="warning-item">弹力随压缩量改变，不应把 F 当作恒力直接用 Fs。</div></div>
        </div>
      </aside>
      <section class="right-panel"><div class="controls"><button class="btn" id="playPause">暂停动画</button><button class="btn btn-secondary" id="resetMotion">重置</button></div><div class="canvas-wrapper"><canvas id="mainCanvas"></canvas></div>
        <div class="card"><div class="card-title">变式与课堂提问</div><div class="variants-grid"><div class="variant-item"><strong>变式 1：k 加倍</strong>同一压缩量下，势能加倍，最大速度变为 $\\sqrt2$ 倍。</div><div class="variant-item"><strong>变式 2：x 加倍</strong>势能变为 4 倍，最大速度变为 2 倍。</div><div class="variant-item"><strong>课堂提问</strong>为什么刚释放时速度为 0，但加速度最大？</div></div></div>
      </section>
    </div>"""
    script = r"""
const state={playing:true,last:0,t:0};
const canvas=document.getElementById('mainCanvas'),ctx=canvas.getContext('2d');
for(const id of ['k','m','x']) document.getElementById(id).addEventListener('input',()=>{state.t=0;draw();});
playPause.onclick=()=>{state.playing=!state.playing;playPause.textContent=state.playing?'暂停动画':'播放动画';};
resetMotion.onclick=()=>{state.t=0;draw();};
function values(){const k=+document.getElementById('k').value,m=+document.getElementById('m').value,x=+document.getElementById('x').value;return{ k,m,x,F:k*x,Ep:.5*k*x*x,v:x*Math.sqrt(k/m),w:Math.sqrt(k/m)}}
function resize(){const dpr=window.devicePixelRatio||1,w=canvas.parentElement.clientWidth,h=canvas.parentElement.clientHeight;canvas.width=w*dpr;canvas.height=h*dpr;ctx.setTransform(dpr,0,0,dpr,0,0);return{w,h};}
function springPath(x0,y,coils,len,amp){let d=`M${x0} ${y}`;for(let i=0;i<=coils*2;i++){const x=x0+len*(i/(coils*2));const yy=y+(i%2?amp:-amp);d+=` L${x.toFixed(1)} ${yy.toFixed(1)}`;}return d;}
function draw(){
 const v=values(); kOut.textContent=`${v.k.toFixed(0)} N/m`; mOut.textContent=`${v.m.toFixed(1)} kg`; xOut.textContent=`${v.x.toFixed(2)} m`;
 resF.textContent=`${v.F.toFixed(1)} N`; resEp.textContent=`${v.Ep.toFixed(2)} J`; resV.textContent=`${v.v.toFixed(2)} m/s`; resW.textContent=`${v.w.toFixed(2)} rad/s`; statusBox.textContent=`当前弹性势能 ${v.Ep.toFixed(2)} J，可转化为最大动能。`;
 const {w,h}=resize();ctx.clearRect(0,0,w,h);ctx.strokeStyle='rgba(255,255,255,.08)';for(let x=0;x<w;x+=44){ctx.beginPath();ctx.moveTo(x,0);ctx.lineTo(x,h);ctx.stroke()}for(let y=0;y<h;y+=44){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(w,y);ctx.stroke()}
 const baseY=h*0.62,wallX=90,eqX=w*0.55,amp=v.x*210;const pos=eqX-amp*Math.cos(state.t*v.w);const springLen=pos-wallX-58;
 ctx.fillStyle='rgba(255,255,255,.12)';ctx.fillRect(60,baseY-120,30,160);ctx.fillRect(45,baseY+42,w-90,18);
 const path=springPath(wallX,baseY,9,springLen,18);ctx.strokeStyle='#64b5f6';ctx.lineWidth=4;ctx.stroke(new Path2D(path));
 ctx.fillStyle='#ffb74d';ctx.shadowColor='#ffb74d';ctx.shadowBlur=16;ctx.fillRect(pos,baseY-34,92,68);ctx.shadowBlur=0;
 ctx.fillStyle='#9aa7b8';ctx.font='13px Segoe UI';ctx.fillText('平衡位置',eqX,baseY+80);ctx.strokeStyle='rgba(62,207,142,.7)';ctx.setLineDash([7,6]);ctx.beginPath();ctx.moveTo(eqX,baseY-95);ctx.lineTo(eqX,baseY+64);ctx.stroke();ctx.setLineDash([]);
 const epHeight=Math.max(5,Math.min(150,v.Ep*18));const ke=.5*v.m*Math.pow(amp*v.w*Math.sin(state.t*v.w)/210,2);const keHeight=Math.max(5,Math.min(150,ke*18));
 ctx.fillStyle='#4f8ef7';ctx.fillRect(w-150,baseY+50-epHeight,42,epHeight);ctx.fillStyle='#3ecf8e';ctx.fillRect(w-92,baseY+50-keHeight,42,keHeight);ctx.fillStyle='#cbd5e1';ctx.fillText('Ep',w-145,baseY+75);ctx.fillText('Ek',w-86,baseY+75);
}
function animate(now){if(!state.last)state.last=now;const dt=Math.min(.05,(now-state.last)/1000);state.last=now;if(state.playing)state.t+=dt;draw();requestAnimationFrame(animate)}
function switchTab(name){document.querySelectorAll('.tab-btn').forEach(btn=>btn.classList.toggle('active',btn.getAttribute('onclick').includes("'"+name+"'")));document.querySelectorAll('.tab-content').forEach(c=>c.classList.toggle('active',c.id==='tab-'+name));if(window.MathJax)MathJax.typesetPromise();}
draw();requestAnimationFrame(animate);
"""
    return page("弹簧能量互动模拟", body, script)


def connected_bodies() -> str:
    body = """<div class="header"><div class="badge">高中物理</div><h1>连接体 · 整体法与隔离法</h1><div class="subtitle">加速度 · 绳子拉力 · 摩擦力</div></div>
    <div class="main-layout"><aside class="left-panel">
      <div class="card"><div class="card-title">题目描述</div><div class="problem-text">水平面上两个物块 $m_1$、$m_2$ 用轻绳连接，外力 <strong>F</strong> 拉动 $m_1$，两物块与水平面间动摩擦因数均为 <strong>μ</strong>。求系统加速度和绳子拉力。</div></div>
      <div class="card"><div class="card-title">调节参数</div><div class="slider-group">
        <div class="slider-item"><div class="slider-label"><span>m₁</span><span id="m1Out"></span></div><input id="m1" type="range" min="0.5" max="6" step="0.1" value="2"></div>
        <div class="slider-item"><div class="slider-label"><span>m₂</span><span id="m2Out"></span></div><input id="m2" type="range" min="0.5" max="6" step="0.1" value="1.5"></div>
        <div class="slider-item"><div class="slider-label"><span>外力 F</span><span id="FOut"></span></div><input id="F" type="range" min="0" max="80" step="1" value="35"></div>
        <div class="slider-item"><div class="slider-label"><span>摩擦因数 μ</span><span id="muOut"></span></div><input id="mu" type="range" min="0" max="0.8" step="0.01" value="0.15"></div>
      </div></div>
      <div class="card"><div class="card-title">实时计算结果</div><div class="results-grid"><div class="result-item"><div class="result-label">系统加速度 a</div><div class="result-value" id="resA"></div></div><div class="result-item"><div class="result-label">绳子拉力 T</div><div class="result-value" id="resT"></div></div><div class="result-item"><div class="result-label">总摩擦力</div><div class="result-value" id="resFric"></div></div><div class="result-item"><div class="result-label">净外力</div><div class="result-value" id="resNet"></div></div></div></div>
      <div class="card"><div class="card-title">运动状态</div><div class="status-box" id="statusBox"></div></div>
      <div class="card"><div class="tabs"><button class="tab-btn active" onclick="switchTab('overall')">整体法</button><button class="tab-btn" onclick="switchTab('isolate')">隔离法</button><button class="tab-btn" onclick="switchTab('warnings')">易错点</button></div>
        <div class="tab-content active" id="tab-overall"><div class="step">整体看 $m_1+m_2$：$F-\\mu(m_1+m_2)g=(m_1+m_2)a$。</div></div>
        <div class="tab-content" id="tab-isolate"><div class="step">隔离 $m_2$：$T-\\mu m_2g=m_2a$，所以 $T=m_2a+\\mu m_2g$。</div></div>
        <div class="tab-content" id="tab-warnings"><div class="warning-item">绳子拉力是内力，整体法列系统方程时不出现。</div><div class="warning-item">如果外力不大于最大摩擦阈值，系统可能不动，本模板用动摩擦模型给出高中常见运动版本。</div></div>
      </div>
    </aside><section class="right-panel"><div class="controls"><button class="btn" id="playPause">暂停动画</button><button class="btn btn-secondary" id="resetMotion">重置</button></div><div class="canvas-wrapper"><canvas id="mainCanvas"></canvas></div>
      <div class="card"><div class="card-title">变式与课堂提问</div><div class="variants-grid"><div class="variant-item"><strong>变式 1：只改变 m₂</strong>观察拉力 T 如何变化。</div><div class="variant-item"><strong>变式 2：无摩擦</strong>令 μ=0，比对 $a=F/(m_1+m_2)$。</div><div class="variant-item"><strong>课堂提问</strong>为什么整体法不能直接求绳子拉力？</div></div></div>
    </section></div>"""
    script = r"""
const st={playing:true,last:0,pos:0,vel:0};const g=10,canvas=document.getElementById('mainCanvas'),ctx=canvas.getContext('2d');
for(const id of ['m1','m2','F','mu'])document.getElementById(id).addEventListener('input',()=>{st.pos=0;st.vel=0;draw();});
playPause.onclick=()=>{st.playing=!st.playing;playPause.textContent=st.playing?'暂停动画':'播放动画'};resetMotion.onclick=()=>{st.pos=0;st.vel=0;draw()};
function values(){const m1=+document.getElementById('m1').value,m2=+document.getElementById('m2').value,F=+document.getElementById('F').value,mu=+document.getElementById('mu').value;const fr=mu*(m1+m2)*g,net=F-fr,a=Math.max(0,net/(m1+m2)),T=m2*a+mu*m2*g;return{m1,m2,F,mu,fr,net,a,T}}
function resize(){const dpr=window.devicePixelRatio||1,w=canvas.parentElement.clientWidth,h=canvas.parentElement.clientHeight;canvas.width=w*dpr;canvas.height=h*dpr;ctx.setTransform(dpr,0,0,dpr,0,0);return{w,h}}
function arrow(x1,y1,x2,y2,c,l){const ang=Math.atan2(y2-y1,x2-x1);ctx.strokeStyle=c;ctx.fillStyle=c;ctx.lineWidth=4;ctx.beginPath();ctx.moveTo(x1,y1);ctx.lineTo(x2,y2);ctx.stroke();ctx.beginPath();ctx.moveTo(x2,y2);ctx.lineTo(x2-12*Math.cos(ang-.45),y2-12*Math.sin(ang-.45));ctx.lineTo(x2-12*Math.cos(ang+.45),y2-12*Math.sin(ang+.45));ctx.fill();ctx.font='bold 13px Segoe UI';ctx.fillText(l,x2+6,y2-6)}
function draw(){const v=values();m1Out.textContent=`${v.m1.toFixed(1)} kg`;m2Out.textContent=`${v.m2.toFixed(1)} kg`;FOut.textContent=`${v.F.toFixed(0)} N`;muOut.textContent=v.mu.toFixed(2);resA.textContent=`${v.a.toFixed(2)} m/s²`;resT.textContent=`${v.T.toFixed(2)} N`;resFric.textContent=`${v.fr.toFixed(1)} N`;resNet.textContent=`${v.net.toFixed(1)} N`;statusBox.textContent=v.net>0?`系统向右加速，a=${v.a.toFixed(2)} m/s²`:'外力不足，按静止/临界处理';
const {w,h}=resize();ctx.clearRect(0,0,w,h);ctx.strokeStyle='rgba(255,255,255,.08)';for(let x=0;x<w;x+=44){ctx.beginPath();ctx.moveTo(x,0);ctx.lineTo(x,h);ctx.stroke()}for(let y=0;y<h;y+=44){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(w,y);ctx.stroke()}const y=h*.58,x=100+(st.pos%(Math.max(260,w-360)));ctx.fillStyle='rgba(255,255,255,.12)';ctx.fillRect(40,y+55,w-80,18);ctx.fillStyle='#4f8ef7';ctx.fillRect(x,y,110,55);ctx.fillStyle='#3ecf8e';ctx.fillRect(x+170,y+8,92,47);ctx.strokeStyle='#f5c842';ctx.lineWidth=4;ctx.beginPath();ctx.moveTo(x+110,y+28);ctx.lineTo(x+170,y+31);ctx.stroke();ctx.fillStyle='white';ctx.font='bold 16px Segoe UI';ctx.fillText('m₁',x+44,y+34);ctx.fillText('m₂',x+204,y+38);arrow(x+110,y-20,x+110+Math.min(140,v.F*2),y-20,'#ef5350','F');arrow(x+170,y+84,x+118,y+84,'#ffa726','f₁');arrow(x+260,y+84,x+216,y+84,'#ffa726','f₂');arrow(x+145,y+8,x+180,y+8,'#f5c842','T');}
function animate(now){if(!st.last)st.last=now;const dt=Math.min(.05,(now-st.last)/1000);st.last=now;const v=values();if(st.playing&&v.a>0){st.vel+=v.a*dt*8;st.pos+=st.vel*dt}draw();requestAnimationFrame(animate)}
function switchTab(name){document.querySelectorAll('.tab-btn').forEach(btn=>btn.classList.toggle('active',btn.getAttribute('onclick').includes("'"+name+"'")));document.querySelectorAll('.tab-content').forEach(c=>c.classList.toggle('active',c.id==='tab-'+name));if(window.MathJax)MathJax.typesetPromise();}
draw();requestAnimationFrame(animate);
"""
    return page("连接体互动模拟", body, script)


TEMPLATES = {
    "incline": incline,
    "projectile": projectile,
    "circular": circular,
    "spring-energy": spring_energy,
    "connected-bodies": connected_bodies,
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--template", choices=sorted(TEMPLATES), default="incline")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    Path(args.output).write_text(TEMPLATES[args.template](), encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
