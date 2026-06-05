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
      font: 700 26px Georgia, serif;
      margin: 18px 0;
    }}
    .status {{
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
    button {{ border: 0; border-radius: 999px; padding: 10px 16px; background: var(--ink); color: white; font-weight: 800; cursor: pointer; }}
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
      <div class="subtitle">调节质量、斜面角度和摩擦因数，实时观察受力图与加速度。</div>
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
        <div class="status" id="status"></div>
        <div class="formula">$$N=mg\\cos\\theta$$ $$f=\\mu N$$ $$a=g(\\sin\\theta-\\mu\\cos\\theta)$$</div>
      </aside>
      <section class="panel">
        <svg id="scene" viewBox="0 0 720 560" role="img" aria-label="Incline force diagram">
          <defs>
            <marker id="arrowB" markerWidth="16" markerHeight="16" refX="14" refY="8" orient="auto"><path d="M2 2L14 8L2 14Z" fill="#2457c5"/></marker>
            <marker id="arrowG" markerWidth="16" markerHeight="16" refX="14" refY="8" orient="auto"><path d="M2 2L14 8L2 14Z" fill="#1f8a70"/></marker>
            <marker id="arrowR" markerWidth="16" markerHeight="16" refX="14" refY="8" orient="auto"><path d="M2 2L14 8L2 14Z" fill="#d63f64"/></marker>
            <marker id="arrowO" markerWidth="16" markerHeight="16" refX="14" refY="8" orient="auto"><path d="M2 2L14 8L2 14Z" fill="#ff8b3d"/></marker>
          </defs>
          <g id="drawing"></g>
        </svg>
        <p class="note">蓝色是重力，绿色是支持力，红色是摩擦力，橙色是沿斜面合力方向。</p>
      </section>
    </section>"""
    script = r"""
const ids = ['m','theta','mu','g'];
for (const id of ids) document.getElementById(id).addEventListener('input', update);
function line(x1,y1,x2,y2,color,marker,label){
  return `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${color}" stroke-width="7" stroke-linecap="round" marker-end="url(#${marker})"/><text x="${x2+8}" y="${y2+4}" font-size="22" font-weight="800" fill="${color}">${label}</text>`;
}
function update(){
  const m = +document.getElementById('m').value;
  const theta = +document.getElementById('theta').value;
  const mu = +document.getElementById('mu').value;
  const g = +document.getElementById('g').value;
  const rad = theta * Math.PI / 180;
  const N = m*g*Math.cos(rad);
  const f = mu*N;
  const a = g*(Math.sin(rad)-mu*Math.cos(rad));
  mOut.textContent = `${m.toFixed(1)} kg`;
  thetaOut.textContent = `${theta.toFixed(0)}°`;
  muOut.textContent = mu.toFixed(2);
  gOut.textContent = `${g.toFixed(2)} m/s²`;
  answer.textContent = `a = ${a.toFixed(2)} m/s²`;
  status.textContent = Math.abs(a) < 0.05 ? '临界状态：加速度约为 0' : (a > 0 ? '沿斜面向下加速' : '合力沿斜面向上');
  status.style.background = Math.abs(a) < 0.05 ? '#ff8b3d' : (a > 0 ? '#1f8a70' : '#d63f64');
  const baseX=110, baseY=440, len=500, height=Math.tan(rad)*len;
  const topX=baseX+len, topY=baseY-height;
  const t = Math.max(0.15, Math.min(0.85, 0.5 + a/18));
  const bx=baseX+len*t, by=baseY-height*t;
  const block = `<g transform="translate(${bx} ${by}) rotate(${-theta})"><rect x="-42" y="-34" width="84" height="68" rx="12" fill="#fff" stroke="#213043" stroke-width="6"/><circle cx="-24" cy="45" r="8" fill="#213043"/><circle cx="24" cy="45" r="8" fill="#213043"/></g>`;
  const forceScale = 7;
  const nx = Math.sin(rad), ny = -Math.cos(rad);
  const downX = 0, downY = 1;
  const upSlopeX = -Math.cos(rad), upSlopeY = -Math.sin(rad);
  const alongX = Math.cos(rad) * Math.sign(a || 1), alongY = -Math.sin(rad) * Math.sign(a || 1);
  drawing.innerHTML = `<polygon points="${baseX},${baseY} ${topX},${topY} ${topX},${baseY}" fill="#deebff" stroke="#213043" stroke-width="4"/>
    <line x1="${baseX}" y1="${baseY}" x2="${topX}" y2="${topY}" stroke="#213043" stroke-width="5"/>
    ${block}
    ${line(bx,by,bx+downX*95,by+downY*95,'#2457c5','arrowB','mg')}
    ${line(bx,by,bx+nx*Math.min(150,N*forceScale),by+ny*Math.min(150,N*forceScale),'#1f8a70','arrowG','N')}
    ${line(bx,by,bx+upSlopeX*Math.min(120,f*forceScale),by+upSlopeY*Math.min(120,f*forceScale),'#d63f64','arrowR','f')}
    ${line(bx,by,bx+alongX*Math.min(130,Math.abs(a)*22+24),by+alongY*Math.min(130,Math.abs(a)*22+24),'#ff8b3d','arrowO','F')}`;
}
update();
"""
    return page("斜面摩擦力互动题页", body, script)


def projectile() -> str:
    body = """<header><h1>平抛运动互动题页</h1><div class="subtitle">调节初速度和高度，观察轨迹、时间、位移和速度分量。</div></header>
    <section class="grid"><aside class="panel">
      <h2>题目</h2><p class="note">小球以水平初速度 $v_0$ 从高度 $h$ 处抛出，忽略空气阻力，求落地时间、水平位移和落地速度。</p>
      <label><span class="row"><span>初速度 v₀</span><output id="vOut"></output></span><input id="v0" type="range" min="2" max="30" step="0.5" value="12"></label>
      <label><span class="row"><span>高度 h</span><output id="hOut"></output></span><input id="h" type="range" min="2" max="80" step="1" value="20"></label>
      <label><span class="row"><span>重力加速度 g</span><output id="gOut"></output></span><input id="g" type="range" min="9.0" max="10.0" step="0.01" value="9.8"></label>
      <div class="result" id="answer"></div>
      <div class="formula">$$t=\\sqrt{2h/g}$$ $$x=v_0t$$ $$v_y=gt$$</div>
      <p class="note">易错点：轨迹弯曲不代表水平速度变化。</p>
    </aside><section class="panel"><svg viewBox="0 0 720 560"><g id="drawing"></g></svg></section></section>"""
    script = r"""
for (const id of ['v0','h','g']) document.getElementById(id).addEventListener('input', update);
function update(){
 const v0=+document.getElementById('v0').value, h=+document.getElementById('h').value, g=+document.getElementById('g').value;
 const t=Math.sqrt(2*h/g), x=v0*t, vy=g*t, v=Math.sqrt(v0*v0+vy*vy);
 vOut.textContent=`${v0.toFixed(1)} m/s`; hOut.textContent=`${h.toFixed(0)} m`; gOut.textContent=`${g.toFixed(2)} m/s²`;
 answer.textContent=`t=${t.toFixed(2)}s, x=${x.toFixed(1)}m, v=${v.toFixed(1)}m/s`;
 const sx=600/x, sy=360/h; let path='';
 for(let i=0;i<=36;i++){ const tt=t*i/36, px=70+v0*tt*sx, py=80+0.5*g*tt*tt*sy; path += `${i?'L':'M'}${px.toFixed(1)} ${py.toFixed(1)} `; }
 drawing.innerHTML=`<rect x="60" y="70" width="20" height="380" fill="#d9e3eb"/><line x1="50" y1="450" x2="680" y2="450" stroke="#213043" stroke-width="4"/>
 <path d="${path}" fill="none" stroke="#d63f64" stroke-width="6"/>
 <circle cx="70" cy="80" r="12" fill="#2457c5"/><circle cx="${70+x*sx}" cy="450" r="12" fill="#ff8b3d"/>
 <line x1="70" y1="80" x2="160" y2="80" stroke="#1f8a70" stroke-width="7"/><text x="165" y="86" fill="#1f8a70" font-size="22" font-weight="800">v₀</text>
 <line x1="360" y1="210" x2="360" y2="310" stroke="#2457c5" stroke-width="7"/><text x="372" y="304" fill="#2457c5" font-size="22" font-weight="800">g</text>`;
}
update();
"""
    return page("平抛运动互动题页", body, script)


def circular() -> str:
    body = """<header><h1>圆周运动互动题页</h1><div class="subtitle">调节质量、半径和速度，观察向心力如何变化。</div></header>
    <section class="grid"><aside class="panel">
      <h2>题目</h2><p class="note">质量为 $m$ 的小球以速度 $v$ 做半径为 $r$ 的匀速圆周运动，求所需向心力大小。</p>
      <label><span class="row"><span>质量 m</span><output id="mOut"></output></span><input id="m" type="range" min="0.2" max="5" step="0.1" value="1.5"></label>
      <label><span class="row"><span>半径 r</span><output id="rOut"></output></span><input id="r" type="range" min="0.5" max="6" step="0.1" value="2"></label>
      <label><span class="row"><span>速度 v</span><output id="vOut"></output></span><input id="v" type="range" min="0.5" max="12" step="0.1" value="4"></label>
      <div class="result" id="answer"></div>
      <div class="formula">$$F=mv^2/r$$ $$a=v^2/r$$</div>
      <p class="note">向心力不是额外的新力，它是指向圆心的合力效果。</p>
    </aside><section class="panel"><svg viewBox="0 0 720 560"><g id="drawing"></g></svg></section></section>"""
    script = r"""
for (const id of ['m','r','v']) document.getElementById(id).addEventListener('input', update);
function update(){
 const m=+document.getElementById('m').value, r=+document.getElementById('r').value, v=+document.getElementById('v').value;
 const F=m*v*v/r, a=v*v/r; mOut.textContent=`${m.toFixed(1)} kg`; rOut.textContent=`${r.toFixed(1)} m`; vOut.textContent=`${v.toFixed(1)} m/s`; answer.textContent=`F=${F.toFixed(2)}N, a=${a.toFixed(2)}m/s²`;
 const cx=360, cy=280, rr=80+r*35, angle=-0.75, bx=cx+rr*Math.cos(angle), by=cy+rr*Math.sin(angle);
 drawing.innerHTML=`<circle cx="${cx}" cy="${cy}" r="${rr}" fill="#eef6fb" stroke="#213043" stroke-width="5"/><circle cx="${cx}" cy="${cy}" r="6" fill="#213043"/>
 <circle cx="${bx}" cy="${by}" r="${14+m*4}" fill="#ff8b3d"/>
 <line x1="${bx}" y1="${by}" x2="${cx+(bx-cx)*0.38}" y2="${cy+(by-cy)*0.38}" stroke="#2457c5" stroke-width="${Math.min(14,4+F/8)}"/>
 <text x="${cx+(bx-cx)*0.5}" y="${cy+(by-cy)*0.5}" fill="#2457c5" font-size="24" font-weight="800">F</text>
 <line x1="${bx}" y1="${by}" x2="${bx+90}" y2="${by+80}" stroke="#1f8a70" stroke-width="7"/><text x="${bx+94}" y="${by+86}" fill="#1f8a70" font-size="24" font-weight="800">v</text>`;
}
update();
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
