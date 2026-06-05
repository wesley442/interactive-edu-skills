#!/usr/bin/env python3
"""Generate self-contained interactive geometry HTML explainers."""

from __future__ import annotations

import argparse
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent


def read_template(name: str) -> str:
    return (SCRIPT_DIR.parent / "templates" / name).read_text(encoding="utf-8")


def square_pyramid() -> str:
    return read_template("square-pyramid.html")


def geometry_page(title: str, subtitle: str, body: str, script: str) -> str:
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
    :root {{ --bg:#0f1117; --panel:#1a1d27; --card:#22263a; --line:#2e3350; --blue:#4f8ef7; --green:#3ecf8e; --gold:#f5c842; --red:#f56565; --text:#e8ecf4; --muted:#8892a4; }}
    body {{ min-height: 100vh; overflow: hidden; color: var(--text); background: var(--bg); font-family: "Segoe UI", "Microsoft YaHei", sans-serif; }}
    header {{ height: 46px; display: flex; align-items: center; gap: 14px; padding: 0 22px; background: linear-gradient(90deg,#1a1d27,#22263a); border-bottom: 1px solid var(--line); }}
    .badge {{ padding: 4px 12px; border-radius: 999px; background: linear-gradient(135deg,var(--blue),#7c5cfc); color: white; font-size: 12px; font-weight: 800; }}
    h1 {{ font-size: 18px; }}
    .subtitle {{ margin-left: auto; color: var(--muted); font-size: 12px; }}
    .layout {{ display: grid; grid-template-columns: 420px 1fr; height: calc(100vh - 46px); }}
    .left {{ overflow-y: auto; border-right: 1px solid var(--line); background: var(--panel); padding: 14px; }}
    .right {{ position: relative; overflow: hidden; background: radial-gradient(circle at 55% 45%,#17233b,#0f1117 62%); }}
    .card {{ background: var(--card); border: 1px solid var(--line); border-radius: 10px; padding: 14px; margin-bottom: 12px; line-height: 1.75; font-size: 13px; }}
    .title {{ color: var(--blue); font-weight: 800; font-size: 13px; margin-bottom: 8px; }}
    .answer {{ color: white; background: linear-gradient(135deg,#1e3a2f,#1a2e40); border: 1px solid #3ecf8e55; border-radius: 8px; padding: 10px 12px; margin-top: 10px; font-size: 16px; font-weight: 800; }}
    .step {{ cursor: pointer; border-color: var(--line); transition: .2s; }}
    .step.active {{ border-color: var(--blue); box-shadow: 0 0 0 1px #4f8ef744 inset; }}
    .step.done {{ border-color: #3ecf8e55; }}
    .muted {{ color: var(--muted); }}
    .controls {{ position: absolute; left: 50%; bottom: 18px; transform: translateX(-50%); display: flex; gap: 10px; z-index: 3; }}
    button {{ border: 1px solid var(--line); background: rgba(26,29,39,.92); color: var(--text); border-radius: 8px; padding: 8px 16px; font: inherit; font-weight: 700; cursor: pointer; }}
    button.primary {{ border: 0; background: linear-gradient(135deg,var(--blue),#7c5cfc); color: white; }}
    .scene-note {{ position: absolute; right: 16px; top: 16px; min-width: 230px; background: rgba(26,29,39,.92); border: 1px solid var(--line); border-radius: 10px; padding: 12px; color: var(--muted); font-size: 12px; line-height: 1.7; z-index: 2; }}
    svg {{ width: 100%; height: 100%; display: block; }}
    .face {{ fill: #2466b3; opacity: .42; stroke: #7fb2ff; stroke-width: 3; }}
    .edge {{ stroke: #6f8edb; stroke-width: 4; fill: none; }}
    .dash {{ stroke-dasharray: 9 7; opacity: .62; }}
    .hot {{ stroke: var(--gold); stroke-width: 8; fill: none; filter: drop-shadow(0 0 7px rgba(245,200,66,.6)); }}
    .green {{ stroke: var(--green); stroke-width: 6; fill: none; }}
    .red {{ stroke: var(--red); stroke-width: 6; fill: none; }}
    text {{ font-family: "Segoe UI", "Microsoft YaHei", sans-serif; font-weight: 800; }}
    input[type=range] {{ width: 100%; accent-color: var(--blue); }}
    @media (max-width: 900px) {{ body {{ overflow: auto; }} .layout {{ display: block; height: auto; }} .right {{ height: 560px; }} }}
  </style>
</head>
<body>
  <header><span class="badge">高中数学</span><h1>{title}</h1><div class="subtitle">{subtitle}</div></header>
  <main class="layout">{body}</main>
  <script>{script}</script>
</body>
</html>
"""


def cube_distance() -> str:
    body = """<aside class="left">
      <div class="card"><div class="title">题目</div>正方体 $ABCD-A_1B_1C_1D_1$ 的棱长为 $a$。求点 $A_1$ 到平面 $B_1CD$ 的距离。
        <div class="answer">答案：$d=\\dfrac{a}{\\sqrt3}=\\dfrac{\\sqrt3}{3}a$</div>
      </div>
      <div class="card"><div class="title">参数</div><div class="muted">棱长 a：<span id="aVal">4</span></div><input id="edge" type="range" min="2" max="8" step="1" value="4"></div>
      <div class="card step active" data-step="0"><div class="title">1. 建立坐标系</div>令 $A(0,0,0)$，$B(a,0,0)$，$D(0,a,0)$，$A_1(0,0,a)$。</div>
      <div class="card step" data-step="1"><div class="title">2. 写出平面上三点</div>$B_1(a,0,a)$，$C(a,a,0)$，$D(0,a,0)$。</div>
      <div class="card step" data-step="2"><div class="title">3. 求平面法向量</div>由向量叉积可得平面 $B_1CD$ 的法向量可取 $\\vec n=(1,-1,1)$。</div>
      <div class="card step" data-step="3"><div class="title">4. 点到平面距离</div>$d=\\frac{|\\vec{DA_1}\\cdot\\vec n|}{|\\vec n|}=\\frac{a}{\\sqrt3}$。</div>
      <div class="card"><div class="title">易错点</div><div class="muted">不要把点到平面的距离误认为到平面内某条线的距离；必须使用垂线或法向量。</div></div>
    </aside>
    <section class="right">
      <div class="scene-note" id="sceneNote"></div>
      <svg viewBox="0 0 760 560" id="scene"></svg>
      <div class="controls"><button id="prev">上一步</button><button class="primary" id="next">下一步</button></div>
    </section>"""
    script = r"""
let step = 0;
const notes = [
  '先把正方体放进坐标系，顶点坐标一目了然。',
  '高亮平面 B₁CD，它是一个斜截面，不是正方体的表面。',
  '法向量垂直于整个平面，点到平面距离沿法向量方向计算。',
  '黄色线段表示点 A₁ 到平面 B₁CD 的垂直距离。'
];
document.querySelectorAll('.step').forEach(el => el.onclick = () => setStep(+el.dataset.step));
prev.onclick = () => setStep(Math.max(0, step - 1));
next.onclick = () => setStep(Math.min(3, step + 1));
edge.oninput = draw;
function setStep(n){ step=n; document.querySelectorAll('.step').forEach((el,i)=>{el.classList.toggle('active',i===step);el.classList.toggle('done',i<step)}); draw(); if(window.MathJax) MathJax.typesetPromise(); }
function p(x,y,z){ return [205 + x*92 + y*46, 410 - z*76 - y*42]; }
function line(a,b,cls='edge'){ return `<line x1="${a[0]}" y1="${a[1]}" x2="${b[0]}" y2="${b[1]}" class="${cls}"/>`; }
function dot(name, q, color='#e8ecf4'){ return `<circle cx="${q[0]}" cy="${q[1]}" r="7" fill="${color}"/><text x="${q[0]+10}" y="${q[1]-8}" fill="${color}" font-size="17">${name}</text>`; }
function draw(){
  const a = +edge.value; aVal.textContent = a;
  const A=p(0,0,0), B=p(1,0,0), C=p(1,1,0), D=p(0,1,0), A1=p(0,0,1), B1=p(1,0,1), C1=p(1,1,1), D1=p(0,1,1);
  const foot=p(.38,.62,.38);
  sceneNote.innerHTML = `<b style="color:#4f8ef7">当前步骤</b><br>${notes[step]}<br><span style="color:#f5c842">当前距离 d = ${(a/Math.sqrt(3)).toFixed(2)}</span>`;
  scene.innerHTML = `
    <rect width="760" height="560" fill="#0f1117"/>
    <g opacity=".25" stroke="#2e3350">${Array.from({length:8},(_,i)=>`<line x1="80" y1="${130+i*48}" x2="700" y2="${130+i*48}"/>`).join('')}</g>
    <polygon points="${A} ${B} ${C} ${D}" fill="#1a4a8a" opacity=".45" stroke="#4f8ef7" stroke-width="3"/>
    <polygon points="${A1} ${B1} ${C1} ${D1}" fill="#1f2b4d" opacity=".32" stroke="#6f8edb" stroke-width="3"/>
    ${line(A,A1)}${line(B,B1)}${line(C,C1)}${line(D,D1)}${line(A,B)}${line(B,C)}${line(C,D)}${line(D,A)}${line(A1,B1)}${line(B1,C1)}${line(C1,D1)}${line(D1,A1)}
    <polygon points="${B1} ${C} ${D}" class="face" opacity="${step>=1?'.72':'.25'}"/>
    ${step>=2?line(A1,foot,'green'):''}
    ${step>=3?line(A1,foot,'hot'):''}
    ${dot('A',A)}${dot('B',B)}${dot('C',C)}${dot('D',D)}${dot('A₁',A1,'#f5c842')}${dot('B₁',B1)}${dot('C₁',C1)}${dot('D₁',D1)}
    ${step>=3?`<text x="${foot[0]+10}" y="${foot[1]+26}" fill="#3ecf8e" font-size="16">垂足 H</text>`:''}
  `;
}
setStep(0);
"""
    return geometry_page("正方体点到平面距离", "空间向量 · 点面距离 · 可调棱长", body, script)


def dihedral_angle() -> str:
    body = """<aside class="left">
      <div class="card"><div class="title">题目</div>正四面体 $ABCD$ 的棱长为 $a$，求二面角 $A-BC-D$ 的余弦值。
        <div class="answer">答案：$\\cos\\theta=\\dfrac{1}{3}$</div>
      </div>
      <div class="card step active" data-step="0"><div class="title">1. 找公共棱</div>二面角 $A-BC-D$ 的棱是 $BC$。</div>
      <div class="card step" data-step="1"><div class="title">2. 作垂线截面</div>取 $BC$ 中点 $M$，连 $AM$、$DM$，它们都垂直 $BC$。</div>
      <div class="card step" data-step="2"><div class="title">3. 转化为平面角</div>二面角等于截面角 $\\angle AMD$。</div>
      <div class="card step" data-step="3"><div class="title">4. 计算</div>$AM=DM=\\frac{\\sqrt3}{2}a$，$AD=a$，由余弦定理得 $\\cos\\theta=\\frac{1}{3}$。</div>
      <div class="card"><div class="title">易错点</div><div class="muted">二面角不是两个面的视觉夹角，必须转化为垂直公共棱的截面角。</div></div>
    </aside>
    <section class="right">
      <div class="scene-note" id="sceneNote"></div>
      <svg viewBox="0 0 760 560" id="scene"></svg>
      <div class="controls"><button id="prev">上一步</button><button class="primary" id="next">下一步</button></div>
    </section>"""
    script = r"""
let step=0;
const notes=['高亮公共棱 BC。','取中点 M，作出 AM 与 DM。','二面角转化为截面角 ∠AMD。','利用等腰三角形 AMD 的余弦定理得到 1/3。'];
document.querySelectorAll('.step').forEach(el=>el.onclick=()=>setStep(+el.dataset.step));
prev.onclick=()=>setStep(Math.max(0,step-1)); next.onclick=()=>setStep(Math.min(3,step+1));
function setStep(n){step=n;document.querySelectorAll('.step').forEach((el,i)=>{el.classList.toggle('active',i===step);el.classList.toggle('done',i<step)});draw();if(window.MathJax)MathJax.typesetPromise();}
function dot(name,x,y,c='#e8ecf4'){return `<circle cx="${x}" cy="${y}" r="8" fill="${c}"/><text x="${x+12}" y="${y-8}" fill="${c}" font-size="18">${name}</text>`}
function draw(){
  const A=[370,96], B=[190,392], C=[570,384], D=[382,454], M=[380,388];
  sceneNote.innerHTML=`<b style="color:#4f8ef7">当前步骤</b><br>${notes[step]}<br><span style="color:#f5c842">目标：cos θ = 1/3</span>`;
  scene.innerHTML=`
  <rect width="760" height="560" fill="#0f1117"/>
  <g opacity=".22" stroke="#2e3350">${Array.from({length:8},(_,i)=>`<line x1="70" y1="${120+i*52}" x2="700" y2="${120+i*52}"/>`).join('')}</g>
  <polygon points="${A} ${B} ${C}" fill="#2466b3" opacity=".35" stroke="#7fb2ff" stroke-width="3"/>
  <polygon points="${D} ${B} ${C}" fill="#1a8a74" opacity=".30" stroke="#3ecf8e" stroke-width="3"/>
  <line x1="${A[0]}" y1="${A[1]}" x2="${D[0]}" y2="${D[1]}" class="edge dash"/>
  <line x1="${B[0]}" y1="${B[1]}" x2="${C[0]}" y2="${C[1]}" class="${step>=0?'hot':'edge'}"/>
  <line x1="${A[0]}" y1="${A[1]}" x2="${B[0]}" y2="${B[1]}" class="edge"/><line x1="${A[0]}" y1="${A[1]}" x2="${C[0]}" y2="${C[1]}" class="edge"/>
  <line x1="${D[0]}" y1="${D[1]}" x2="${B[0]}" y2="${B[1]}" class="edge"/><line x1="${D[0]}" y1="${D[1]}" x2="${C[0]}" y2="${C[1]}" class="edge"/>
  ${step>=1?`<line x1="${A[0]}" y1="${A[1]}" x2="${M[0]}" y2="${M[1]}" class="green"/><line x1="${D[0]}" y1="${D[1]}" x2="${M[0]}" y2="${M[1]}" class="green"/>`:''}
  ${step>=2?`<path d="M344 356 A58 58 0 0 0 420 358" fill="none" stroke="#f5c842" stroke-width="7"/><text x="397" y="346" fill="#f5c842" font-size="22">θ</text>`:''}
  ${dot('A',...A,'#f5c842')}${dot('B',...B)}${dot('C',...C)}${dot('D',...D,'#3ecf8e')}${step>=1?dot('M',...M,'#ffb74d'):''}
  `;
}
setStep(0);
"""
    return geometry_page("正四面体二面角", "二面角 · 截面角 · 余弦定理", body, script)


TEMPLATES = {"square-pyramid": square_pyramid, "cube-distance": cube_distance, "dihedral-angle": dihedral_angle}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--template", choices=sorted(TEMPLATES), default="square-pyramid")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    Path(args.output).write_text(TEMPLATES[args.template](), encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
