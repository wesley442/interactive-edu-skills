const fs = require("fs");
const path = require("path");
const sharp = require("sharp");

const outDir = __dirname;

function esc(s) {
  return String(s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

function write(name, svg, size = null) {
  const svgPath = path.join(outDir, `${name}.svg`);
  const pngPath = path.join(outDir, `${name}.png`);
  fs.writeFileSync(svgPath, svg);
  const job = sharp(Buffer.from(svg)).png();
  return (size ? job.resize(size.width, size.height) : job)
    .toFile(pngPath)
    .then(() => ({ svgPath, pngPath }));
}

const font = "'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif";

function icon() {
  return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">
  <defs>
    <linearGradient id="bg" x1="96" y1="48" x2="930" y2="940" gradientUnits="userSpaceOnUse">
      <stop stop-color="#fff4dc"/>
      <stop offset="0.52" stop-color="#e9f7f5"/>
      <stop offset="1" stop-color="#dbe9ff"/>
    </linearGradient>
    <linearGradient id="plane" x1="200" y1="710" x2="816" y2="414" gradientUnits="userSpaceOnUse">
      <stop stop-color="#1f8a70"/>
      <stop offset="0.52" stop-color="#2457c5"/>
      <stop offset="1" stop-color="#ff8b3d"/>
    </linearGradient>
    <filter id="shadow" x="-15%" y="-15%" width="130%" height="135%">
      <feDropShadow dx="0" dy="24" stdDeviation="30" flood-color="#263244" flood-opacity="0.22"/>
    </filter>
    <marker id="arrowBlue" markerWidth="34" markerHeight="34" refX="30" refY="17" orient="auto" markerUnits="userSpaceOnUse">
      <path d="M4 4L30 17L4 30Z" fill="#2457c5"/>
    </marker>
    <marker id="arrowRose" markerWidth="34" markerHeight="34" refX="30" refY="17" orient="auto" markerUnits="userSpaceOnUse">
      <path d="M4 4L30 17L4 30Z" fill="#d63f64"/>
    </marker>
    <marker id="arrowGreen" markerWidth="34" markerHeight="34" refX="30" refY="17" orient="auto" markerUnits="userSpaceOnUse">
      <path d="M4 4L30 17L4 30Z" fill="#1f8a70"/>
    </marker>
  </defs>
  <rect width="1024" height="1024" rx="210" fill="url(#bg)"/>
  <g filter="url(#shadow)">
    <path d="M164 742H870L870 668H318Z" fill="#ffffff" opacity="0.82"/>
    <path d="M180 734L836 420" stroke="url(#plane)" stroke-width="54" stroke-linecap="round"/>
    <path d="M198 774H866" stroke="#2b3442" stroke-width="30" stroke-linecap="round" opacity="0.22"/>
    <g transform="translate(438 471) rotate(-25)">
      <rect x="-90" y="-70" width="180" height="140" rx="28" fill="#ffffff" stroke="#2b3442" stroke-width="26"/>
      <circle cx="-46" cy="83" r="22" fill="#2b3442"/>
      <circle cx="48" cy="83" r="22" fill="#2b3442"/>
    </g>
  </g>
  <line x1="486" y1="454" x2="486" y2="276" stroke="#2457c5" stroke-width="28" stroke-linecap="round" marker-end="url(#arrowBlue)"/>
  <line x1="486" y1="454" x2="360" y2="512" stroke="#d63f64" stroke-width="28" stroke-linecap="round" marker-end="url(#arrowRose)"/>
  <line x1="486" y1="454" x2="642" y2="382" stroke="#1f8a70" stroke-width="28" stroke-linecap="round" marker-end="url(#arrowGreen)"/>
  <path d="M652 260c72 22 122 72 136 144 18 95-37 174-123 210" fill="none" stroke="#ff8b3d" stroke-width="24" stroke-linecap="round" stroke-dasharray="1 42"/>
  <circle cx="702" cy="280" r="26" fill="#ff8b3d"/>
  <rect x="272" y="826" width="480" height="42" rx="21" fill="#ffffff" opacity="0.82"/>
  <circle cx="424" cy="847" r="32" fill="#2457c5"/>
  <circle cx="624" cy="847" r="32" fill="#d63f64"/>
</svg>`;
}

function base(title, kicker, accent, body) {
  return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1280" viewBox="0 0 1600 1280">
  <defs>
    <linearGradient id="paper" x1="0" y1="0" x2="1600" y2="1280" gradientUnits="userSpaceOnUse">
      <stop stop-color="#fff4dc"/>
      <stop offset="0.4" stop-color="#f8fbfc"/>
      <stop offset="1" stop-color="#e4effa"/>
    </linearGradient>
    <pattern id="grid" width="56" height="56" patternUnits="userSpaceOnUse">
      <path d="M56 0H0V56" fill="none" stroke="#cfdae4" stroke-width="1" opacity="0.55"/>
    </pattern>
    <filter id="soft" x="-15%" y="-15%" width="130%" height="140%">
      <feDropShadow dx="0" dy="22" stdDeviation="28" flood-color="#213043" flood-opacity="0.16"/>
    </filter>
    <marker id="arrowBlue" markerWidth="28" markerHeight="28" refX="24" refY="14" orient="auto" markerUnits="userSpaceOnUse">
      <path d="M4 4L24 14L4 24Z" fill="#2457c5"/>
    </marker>
    <marker id="arrowRose" markerWidth="28" markerHeight="28" refX="24" refY="14" orient="auto" markerUnits="userSpaceOnUse">
      <path d="M4 4L24 14L4 24Z" fill="#d63f64"/>
    </marker>
    <marker id="arrowGreen" markerWidth="28" markerHeight="28" refX="24" refY="14" orient="auto" markerUnits="userSpaceOnUse">
      <path d="M4 4L24 14L4 24Z" fill="#1f8a70"/>
    </marker>
    <marker id="arrowOrange" markerWidth="28" markerHeight="28" refX="24" refY="14" orient="auto" markerUnits="userSpaceOnUse">
      <path d="M4 4L24 14L4 24Z" fill="#ff8b3d"/>
    </marker>
  </defs>
  <rect width="1600" height="1280" fill="url(#paper)"/>
  <rect width="1600" height="1280" fill="url(#grid)" opacity="0.5"/>
  <circle cx="1324" cy="124" r="280" fill="#ffdca8" opacity="0.36"/>
  <circle cx="170" cy="1120" r="250" fill="#bfe6df" opacity="0.42"/>
  <g transform="translate(90 76)">
    <rect x="0" y="0" width="1420" height="1128" rx="42" fill="#fbfcfd" stroke="#dbe3ea" filter="url(#soft)"/>
    <rect x="0" y="0" width="1420" height="118" rx="42" fill="#263244"/>
    <rect x="0" y="76" width="1420" height="42" fill="#263244"/>
    <text x="52" y="72" font-family="${font}" font-size="38" font-weight="800" fill="#ffffff">${esc(title)}</text>
    <text x="1086" y="70" font-family="Georgia,serif" font-size="28" font-weight="700" fill="${accent}">Physics Skill</text>
    <text x="54" y="166" font-family="${font}" font-size="24" fill="#5c6b77">${esc(kicker)}</text>
    ${body}
  </g>
</svg>`;
}

function panel({ x, y, w, h, title, subtitle, children = "" }) {
  return `
  <g>
    <rect x="${x}" y="${y}" width="${w}" height="${h}" rx="26" fill="#ffffff" stroke="#dbe3ea" stroke-width="2"/>
    <text x="${x + 30}" y="${y + 52}" font-family="${font}" font-size="29" font-weight="700" fill="#1d2b3a">${esc(title)}</text>
    <text x="${x + 30}" y="${y + 88}" font-family="${font}" font-size="18" fill="#6d7c88">${esc(subtitle)}</text>
    ${children}
  </g>`;
}

function badge(x, y, text, fill, color = "#ffffff") {
  return `<g><rect x="${x}" y="${y}" width="${text.length * 18 + 44}" height="42" rx="21" fill="${fill}"/><text x="${x + 22}" y="${y + 28}" font-family="${font}" font-size="18" font-weight="700" fill="${color}">${esc(text)}</text></g>`;
}

function slider(x, y, label, value, color, pos = 0.62) {
  const w = 330;
  const knob = x + w * pos;
  return `
  <g>
    <text x="${x}" y="${y}" font-family="${font}" font-size="20" font-weight="700" fill="#253244">${esc(label)}</text>
    <text x="${x + 260}" y="${y}" font-family="Georgia,serif" font-size="22" font-weight="800" fill="${color}">${esc(value)}</text>
    <path d="M${x} ${y + 38}H${x + w}" stroke="#d8e3eb" stroke-width="10" stroke-linecap="round"/>
    <path d="M${x} ${y + 38}H${knob}" stroke="${color}" stroke-width="10" stroke-linecap="round"/>
    <circle cx="${knob}" cy="${y + 38}" r="18" fill="${color}"/>
  </g>`;
}

function inclineScene(cx, cy, scale = 1) {
  const p = (x, y) => `${cx + x * scale},${cy + y * scale}`;
  return `
  <g>
    <path d="M${p(-270,190)}L${p(270,190)}L${p(270,-70)}Z" fill="#eaf3ff" stroke="#263244" stroke-width="${5 * scale}"/>
    <path d="M${p(-270,190)}L${p(270,-70)}" stroke="#263244" stroke-width="${7 * scale}" stroke-linecap="round"/>
    <g transform="translate(${cx - 10 * scale} ${cy + 16 * scale}) rotate(-25) scale(${scale})">
      <rect x="-70" y="-48" width="140" height="96" rx="18" fill="#ffffff" stroke="#263244" stroke-width="9"/>
      <circle cx="-38" cy="62" r="14" fill="#263244"/>
      <circle cx="38" cy="62" r="14" fill="#263244"/>
    </g>
    <line x1="${cx - 10 * scale}" y1="${cy + 16 * scale}" x2="${cx - 10 * scale}" y2="${cy + 158 * scale}" stroke="#2457c5" stroke-width="${9 * scale}" stroke-linecap="round" marker-end="url(#arrowBlue)"/>
    <line x1="${cx - 10 * scale}" y1="${cy + 16 * scale}" x2="${cx - 136 * scale}" y2="${cy + 74 * scale}" stroke="#d63f64" stroke-width="${9 * scale}" stroke-linecap="round" marker-end="url(#arrowRose)"/>
    <line x1="${cx - 10 * scale}" y1="${cy + 16 * scale}" x2="${cx + 116 * scale}" y2="${cy - 42 * scale}" stroke="#1f8a70" stroke-width="${9 * scale}" stroke-linecap="round" marker-end="url(#arrowGreen)"/>
    <text x="${cx + 8 * scale}" y="${cy + 152 * scale}" font-family="Georgia,serif" font-size="${28 * scale}" font-weight="800" fill="#2457c5">mg</text>
    <text x="${cx - 188 * scale}" y="${cy + 63 * scale}" font-family="Georgia,serif" font-size="${28 * scale}" font-weight="800" fill="#d63f64">f</text>
    <text x="${cx + 96 * scale}" y="${cy - 50 * scale}" font-family="Georgia,serif" font-size="${28 * scale}" font-weight="800" fill="#1f8a70">N</text>
  </g>`;
}

function projectileScene(cx, cy, scale = 1) {
  const points = [];
  for (let i = 0; i <= 11; i++) {
    const x = i * 42;
    const y = 0.04 * x * x;
    points.push(`${cx + x * scale},${cy + y * scale}`);
  }
  return `
  <g>
    <path d="M${cx - 40 * scale} ${cy + 300 * scale}H${cx + 540 * scale}" stroke="#263244" stroke-width="${5 * scale}"/>
    <path d="M${cx} ${cy} C${cx + 160 * scale} ${cy + 8 * scale}, ${cx + 320 * scale} ${cy + 88 * scale}, ${cx + 500 * scale} ${cy + 286 * scale}" fill="none" stroke="#d63f64" stroke-width="${8 * scale}" stroke-linecap="round"/>
    ${points.map((pt, i) => `<circle cx="${pt.split(",")[0]}" cy="${pt.split(",")[1]}" r="${(i === 0 || i === 11 ? 11 : 7) * scale}" fill="${i === 11 ? "#ff8b3d" : "#2457c5"}" opacity="${i < 11 ? 0.88 : 1}"/>`).join("")}
    <line x1="${cx}" y1="${cy}" x2="${cx + 130 * scale}" y2="${cy}" stroke="#1f8a70" stroke-width="${9 * scale}" marker-end="url(#arrowGreen)" stroke-linecap="round"/>
    <line x1="${cx + 270 * scale}" y1="${cy + 80 * scale}" x2="${cx + 270 * scale}" y2="${cy + 184 * scale}" stroke="#2457c5" stroke-width="${9 * scale}" marker-end="url(#arrowBlue)" stroke-linecap="round"/>
    <line x1="${cx + 330 * scale}" y1="${cy + 118 * scale}" x2="${cx + 430 * scale}" y2="${cy + 210 * scale}" stroke="#ff8b3d" stroke-width="${9 * scale}" marker-end="url(#arrowOrange)" stroke-linecap="round"/>
    <text x="${cx + 70 * scale}" y="${cy - 18 * scale}" font-family="Georgia,serif" font-size="${28 * scale}" font-weight="800" fill="#1f8a70">v₀</text>
    <text x="${cx + 286 * scale}" y="${cy + 176 * scale}" font-family="Georgia,serif" font-size="${28 * scale}" font-weight="800" fill="#2457c5">g</text>
  </g>`;
}

function circularScene(cx, cy, scale = 1) {
  return `
  <g>
    <circle cx="${cx}" cy="${cy}" r="${170 * scale}" fill="#edf5fb" stroke="#263244" stroke-width="${5 * scale}"/>
    <circle cx="${cx}" cy="${cy}" r="${8 * scale}" fill="#263244"/>
    <circle cx="${cx + 132 * scale}" cy="${cy - 106 * scale}" r="${28 * scale}" fill="#ff8b3d"/>
    <line x1="${cx + 132 * scale}" y1="${cy - 106 * scale}" x2="${cx + 38 * scale}" y2="${cy - 30 * scale}" stroke="#2457c5" stroke-width="${9 * scale}" marker-end="url(#arrowBlue)" stroke-linecap="round"/>
    <line x1="${cx + 132 * scale}" y1="${cy - 106 * scale}" x2="${cx + 232 * scale}" y2="${cy + 16 * scale}" stroke="#1f8a70" stroke-width="${9 * scale}" marker-end="url(#arrowGreen)" stroke-linecap="round"/>
    <path d="M${cx - 16 * scale} ${cy - 170 * scale}A${170 * scale} ${170 * scale} 0 0 1 ${cx + 156 * scale} ${cy - 66 * scale}" fill="none" stroke="#d63f64" stroke-width="${7 * scale}" stroke-linecap="round" stroke-dasharray="${16 * scale} ${12 * scale}"/>
    <text x="${cx + 48 * scale}" y="${cy - 54 * scale}" font-family="Georgia,serif" font-size="${28 * scale}" font-weight="800" fill="#2457c5">F</text>
    <text x="${cx + 230 * scale}" y="${cy + 30 * scale}" font-family="Georgia,serif" font-size="${28 * scale}" font-weight="800" fill="#1f8a70">v</text>
  </g>`;
}

function showcase1() {
  const steps = [
    ["1", "生成题目", "斜面摩擦力，中等难度，课堂可讲"],
    ["2", "调节变量", "m、θ、μ、g 用滑块实时变化"],
    ["3", "同步计算", "N、f、F、a 立即更新"],
    ["4", "动画演示", "箭头长度和滑块运动一起变化"],
  ];
  return base("高中互动力学题工坊", "生成可调变量的受力图、运动动画与分步解析", "#9de1d5", `
    ${panel({ x: 54, y: 210, w: 588, h: 848, title: "一句话生成互动题页", subtitle: "输入题型后自动生成题目、变量和动画", children: `
      <rect x="94" y="350" width="508" height="126" rx="22" fill="#f2f6f8" stroke="#d8e3eb"/>
      <text x="124" y="395" font-family="${font}" font-size="25" font-weight="700" fill="#253244">生成一道高中斜面摩擦力题</text>
      <text x="124" y="436" font-family="${font}" font-size="21" fill="#62717d">可调整质量、斜面角度和摩擦因数</text>
      ${badge(94, 514, "高中力学", "#2457c5")}
      ${badge(226, 514, "斜面", "#1f8a70")}
      ${badge(324, 514, "可调变量", "#ff8b3d")}
      ${steps.map((s, i) => `
        <g transform="translate(94 ${626 + i * 88})">
          <circle cx="24" cy="24" r="24" fill="${i === 2 ? "#d63f64" : "#263244"}"/>
          <text x="17" y="32" font-family="Georgia,serif" font-size="23" font-weight="700" fill="#fff">${s[0]}</text>
          <text x="66" y="18" font-family="${font}" font-size="23" font-weight="700" fill="#253244">${esc(s[1])}</text>
          <text x="66" y="49" font-family="${font}" font-size="18" fill="#667684">${esc(s[2])}</text>
        </g>`).join("")}
    `})}
    ${panel({ x: 692, y: 210, w: 646, h: 848, title: "HTML 互动页预览", subtitle: "左侧滑块控制变量，右侧实时更新受力图", children: `
      <rect x="732" y="336" width="254" height="596" rx="22" fill="#f7fafb" stroke="#dbe3ea"/>
      <text x="762" y="386" font-family="${font}" font-size="25" font-weight="800" fill="#253244">变量</text>
      ${slider(762, 438, "质量 m", "2.0kg", "#2457c5", 0.58)}
      ${slider(762, 536, "角度 θ", "30°", "#1f8a70", 0.48)}
      ${slider(762, 634, "摩擦 μ", "0.20", "#d63f64", 0.42)}
      <rect x="762" y="744" width="196" height="64" rx="14" fill="#263244"/>
      <text x="787" y="786" font-family="Georgia,serif" font-size="28" font-weight="800" fill="#9de1d5">a = 3.20</text>
      <text x="762" y="852" font-family="${font}" font-size="18" fill="#62717d">拖动滑块，结论和动画</text>
      <text x="762" y="884" font-family="${font}" font-size="18" fill="#62717d">同步变化。</text>
      <rect x="1020" y="336" width="270" height="596" rx="22" fill="#edf5fb" stroke="#dbe3ea"/>
      ${inclineScene(1155, 642, 0.5)}
      <text x="1044" y="858" font-family="${font}" font-size="20" fill="#263244">受力箭头实时更新</text>
    `})}
  `);
}

function showcase2() {
  return base("斜面滑块受力分析", "重力、支持力、摩擦力和加速度方向一屏讲清楚", "#ffd18b", `
    ${panel({ x: 54, y: 210, w: 394, h: 848, title: "题目与模型", subtitle: "先选研究对象，再列方程", children: `
      <text x="92" y="360" font-family="${font}" font-size="25" font-weight="800" fill="#253244">粗糙斜面上的滑块</text>
      <text x="92" y="404" font-family="${font}" font-size="21" fill="#62717d">求物块沿斜面下滑的加速度。</text>
      ${["研究对象：滑块", "坐标轴：沿斜面向下", "摩擦力：沿斜面向上", "方程：mg sinθ - μmg cosθ = ma"].map((t, i) => `
        <rect x="92" y="${490 + i * 82}" width="318" height="56" rx="16" fill="${i === 2 ? "#fff3de" : "#f2f6f8"}" stroke="#dbe3ea"/>
        <text x="118" y="${526 + i * 82}" font-family="${font}" font-size="20" font-weight="700" fill="#253244">${esc(t)}</text>`).join("")}
    `})}
    <g transform="translate(486 210)">
      <rect width="448" height="848" rx="26" fill="#253244"/>
      <text x="34" y="58" font-family="${font}" font-size="29" font-weight="800" fill="#fff">互动受力图</text>
      <text x="34" y="94" font-family="${font}" font-size="18" fill="#b9c6d1">箭头长度随变量变化</text>
      <rect x="36" y="136" width="376" height="562" rx="24" fill="#f5fbff"/>
      ${inclineScene(224, 420, 0.72)}
      <rect x="44" y="730" width="120" height="48" rx="24" fill="#9de1d5"/>
      <text x="74" y="761" font-family="${font}" font-size="20" font-weight="800" fill="#253244">播放</text>
      <rect x="180" y="730" width="178" height="48" rx="24" fill="#ffffff" opacity="0.16"/>
      <text x="212" y="761" font-family="${font}" font-size="20" font-weight="700" fill="#fff">重置变量</text>
    </g>
    ${panel({ x: 972, y: 210, w: 366, h: 848, title: "实时推导", subtitle: "公式、数值和状态一起更新", children: `
      <text x="1012" y="372" font-family="Georgia,serif" font-size="30" font-weight="800" fill="#253244">N = mg cosθ</text>
      <text x="1012" y="444" font-family="Georgia,serif" font-size="30" font-weight="800" fill="#253244">f = μN</text>
      <text x="1012" y="516" font-family="Georgia,serif" font-size="30" font-weight="800" fill="#253244">F = mg sinθ - f</text>
      <text x="1012" y="588" font-family="Georgia,serif" font-size="30" font-weight="800" fill="#d63f64">a = g(sinθ - μcosθ)</text>
      <path d="M1012 640H1296" stroke="#dbe3ea" stroke-width="2"/>
      ${badge(1012, 696, "状态：下滑加速", "#1f8a70")}
      ${badge(1012, 766, "临界会提示", "#ff8b3d")}
      <text x="1012" y="878" font-family="${font}" font-size="21" font-weight="800" fill="#253244">学生能看见：摩擦变大时，加速度为什么会变小。</text>
    `})}
  `);
}

function showcase3() {
  return base("平抛运动动画", "把水平匀速、竖直自由落体和合速度拆开看", "#bfe6df", `
    <g transform="translate(54 210)">
      <rect width="1330" height="430" rx="26" fill="#263244"/>
      <text x="44" y="70" font-family="${font}" font-size="34" font-weight="800" fill="#ffffff">动态调整 v₀ 和高度 h</text>
      <text x="44" y="116" font-family="${font}" font-size="23" fill="#c9d7e2">拖动滑块后，飞行时间、水平位移、竖直速度与轨迹同步变化。</text>
      <rect x="44" y="158" width="688" height="220" rx="20" fill="#f5fbff"/>
      ${projectileScene(96, 204, 1.08)}
      <rect x="792" y="162" width="222" height="82" rx="20" fill="#ffffff" opacity="0.1"/>
      <text x="820" y="196" font-family="${font}" font-size="20" fill="#c9d7e2">飞行时间</text>
      <text x="820" y="232" font-family="Georgia,serif" font-size="30" font-weight="800" fill="#9de1d5">t = √(2h/g)</text>
      <rect x="1048" y="162" width="222" height="82" rx="20" fill="#ffffff" opacity="0.1"/>
      <text x="1076" y="196" font-family="${font}" font-size="20" fill="#c9d7e2">水平位移</text>
      <text x="1076" y="232" font-family="Georgia,serif" font-size="30" font-weight="800" fill="#ffd18b">x = v₀t</text>
      <rect x="792" y="278" width="478" height="82" rx="20" fill="#ffffff" opacity="0.1"/>
      <text x="820" y="312" font-family="${font}" font-size="20" fill="#c9d7e2">合速度</text>
      <text x="820" y="348" font-family="Georgia,serif" font-size="30" font-weight="800" fill="#ffffff">v = √(v₀² + vᵧ²)</text>
    </g>
    ${panel({ x: 54, y: 690, w: 412, h: 368, title: "变量滑块", subtitle: "课堂演示时直接拖动", children: `
      ${slider(94, 830, "初速度 v₀", "12m/s", "#1f8a70", 0.56)}
      ${slider(94, 938, "高度 h", "20m", "#2457c5", 0.68)}
    `})}
    ${panel({ x: 506, y: 690, w: 412, h: 368, title: "分量分解", subtitle: "看清水平和竖直互不影响", children: `
      <text x="548" y="848" font-family="Georgia,serif" font-size="32" font-weight="800" fill="#1f8a70">vₓ = v₀</text>
      <text x="548" y="918" font-family="Georgia,serif" font-size="32" font-weight="800" fill="#2457c5">vᵧ = gt</text>
      <text x="548" y="988" font-family="${font}" font-size="22" font-weight="800" fill="#253244">轨迹弯曲，不代表水平速度在变。</text>
    `})}
    ${panel({ x: 958, y: 690, w: 380, h: 368, title: "易错点", subtitle: "把动画变成讲题节奏", children: `
      ${badge(1000, 838, "水平速度不变", "#1f8a70")}
      ${badge(1000, 908, "竖直方向自由落体", "#2457c5")}
      ${badge(1000, 978, "合速度方向在变", "#ff8b3d")}
    `})}
  `);
}

function showcase4() {
  return base("圆周运动不是一种新力", "速度沿切线，合力指向圆心，F = mv²/r 实时校验", "#ffb3a7", `
    ${panel({ x: 54, y: 210, w: 520, h: 848, title: "可调圆周运动", subtitle: "速度、半径、质量改变时，向心力实时变化", children: `
      ${slider(94, 366, "质量 m", "1.5kg", "#2457c5", 0.44)}
      ${slider(94, 484, "半径 r", "2.0m", "#1f8a70", 0.58)}
      ${slider(94, 602, "速度 v", "4.0m/s", "#d63f64", 0.72)}
      <rect x="94" y="744" width="410" height="82" rx="20" fill="#263244"/>
      <text x="126" y="796" font-family="Georgia,serif" font-size="31" font-weight="800" fill="#9de1d5">F = mv²/r = 12N</text>
      <text x="94" y="900" font-family="${font}" font-size="22" font-weight="800" fill="#253244">速度翻倍时，向心力变成 4 倍。</text>
    `})}
    <g transform="translate(626 210)">
      <rect width="376" height="848" rx="26" fill="#253244"/>
      <text x="34" y="58" font-family="${font}" font-size="29" font-weight="800" fill="#fff">动画观察</text>
      <text x="34" y="94" font-family="${font}" font-size="18" fill="#b9c6d1">切向速度与向心合力同时显示</text>
      <rect x="36" y="166" width="304" height="474" rx="24" fill="#f5fbff"/>
      ${circularScene(188, 402, 0.76)}
      <rect x="48" y="700" width="120" height="48" rx="24" fill="#ffb3a7"/>
      <text x="78" y="731" font-family="${font}" font-size="20" font-weight="800" fill="#253244">播放</text>
      <rect x="188" y="700" width="120" height="48" rx="24" fill="#ffffff" opacity="0.16"/>
      <text x="218" y="731" font-family="${font}" font-size="20" font-weight="700" fill="#fff">暂停</text>
    </g>
    ${panel({ x: 1046, y: 210, w: 292, h: 848, title: "讲解重点", subtitle: "把常见误区直接写进页面", children: `
      ${[
        ["01", "向心力不是额外的新力"],
        ["02", "速度方向沿圆的切线"],
        ["03", "加速度指向圆心"],
        ["04", "力的来源要看具体场景"],
      ].map((s, i) => `
        <g transform="translate(1086 ${366 + i * 128})">
          <text x="0" y="0" font-family="Georgia,serif" font-size="38" font-weight="800" fill="${i === 0 ? "#d63f64" : "#cad5df"}">${s[0]}</text>
          <text x="0" y="42" font-family="${font}" font-size="22" font-weight="700" fill="#253244">${esc(s[1])}</text>
          <path d="M0 72H214" stroke="#dbe3ea" stroke-width="2"/>
        </g>`).join("")}
    `})}
  `);
}

Promise.all([
  write("icon-interactive-physics", icon(), { width: 1024, height: 1024 }),
  write("showcase-1-one-prompt-to-interactive-page", showcase1()),
  write("showcase-2-incline-force-analysis", showcase2()),
  write("showcase-3-projectile-motion-animation", showcase3()),
  write("showcase-4-circular-motion-variables", showcase4()),
]).then((files) => {
  for (const file of files) console.log(file.pngPath);
}).catch((error) => {
  console.error(error);
  process.exit(1);
});
