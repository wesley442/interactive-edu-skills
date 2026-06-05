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

function icon() {
  return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">
  <defs>
    <linearGradient id="bg" x1="100" y1="60" x2="920" y2="940" gradientUnits="userSpaceOnUse">
      <stop stop-color="#f7f2e8"/>
      <stop offset="0.52" stop-color="#e7f5f2"/>
      <stop offset="1" stop-color="#d8e2ff"/>
    </linearGradient>
    <linearGradient id="edge" x1="226" y1="162" x2="782" y2="818" gradientUnits="userSpaceOnUse">
      <stop stop-color="#1f8a70"/>
      <stop offset="0.48" stop-color="#2457c5"/>
      <stop offset="1" stop-color="#ff8b3d"/>
    </linearGradient>
    <filter id="shadow" x="-15%" y="-15%" width="130%" height="135%">
      <feDropShadow dx="0" dy="24" stdDeviation="30" flood-color="#263244" flood-opacity="0.22"/>
    </filter>
  </defs>
  <rect width="1024" height="1024" rx="210" fill="url(#bg)"/>
  <path d="M161 732L512 196l351 536H161Z" fill="#ffffff" opacity="0.78" filter="url(#shadow)"/>
  <path d="M512 196L863 732H161L512 196Z" fill="none" stroke="url(#edge)" stroke-width="42" stroke-linejoin="round"/>
  <path d="M512 196L424 732M512 196l178 536M424 732l266 0" fill="none" stroke="#2b3442" stroke-width="24" stroke-linecap="round" opacity="0.82"/>
  <circle cx="512" cy="196" r="42" fill="#2457c5"/>
  <circle cx="161" cy="732" r="38" fill="#1f8a70"/>
  <circle cx="863" cy="732" r="38" fill="#ff8b3d"/>
  <circle cx="424" cy="732" r="26" fill="#2b3442"/>
  <circle cx="690" cy="732" r="26" fill="#2b3442"/>
  <path d="M306 461c46-40 89-53 129-38 36 13 61 43 90 74 33 36 70 72 126 69 43-2 83-25 121-67" fill="none" stroke="#d63f64" stroke-width="22" stroke-linecap="round"/>
  <path d="M272 837h456" stroke="#2b3442" stroke-width="28" stroke-linecap="round" opacity="0.18"/>
</svg>`;
}

function panel({ x, y, w, h, title, subtitle, children = "" }) {
  return `
  <g>
    <rect x="${x}" y="${y}" width="${w}" height="${h}" rx="26" fill="#ffffff" stroke="#dbe3ea" stroke-width="2"/>
    <text x="${x + 30}" y="${y + 52}" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="29" font-weight="700" fill="#1d2b3a">${esc(title)}</text>
    <text x="${x + 30}" y="${y + 88}" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="18" fill="#6d7c88">${esc(subtitle)}</text>
    ${children}
  </g>`;
}

function badge(x, y, text, fill, color = "#ffffff") {
  return `<g><rect x="${x}" y="${y}" width="${text.length * 18 + 44}" height="42" rx="21" fill="${fill}"/><text x="${x + 22}" y="${y + 28}" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="18" font-weight="700" fill="${color}">${esc(text)}</text></g>`;
}

function pyramid(cx, cy, scale = 1, accent = "#2457c5") {
  const p = (x, y) => `${cx + x * scale},${cy + y * scale}`;
  return `
  <g>
    <ellipse cx="${cx + 12 * scale}" cy="${cy + 206 * scale}" rx="${300 * scale}" ry="${58 * scale}" fill="#dce8f6" opacity="0.7"/>
    <polygon points="${p(0,-210)} ${p(-240,160)} ${p(230,180)}" fill="#eaf3ff" stroke="#29394b" stroke-width="${5 * scale}"/>
    <polygon points="${p(0,-210)} ${p(230,180)} ${p(80,255)}" fill="#d7e8ff" stroke="#29394b" stroke-width="${5 * scale}"/>
    <polygon points="${p(0,-210)} ${p(80,255)} ${p(-240,160)}" fill="#f8fbff" stroke="#29394b" stroke-width="${5 * scale}"/>
    <path d="M${p(-240,160)} L${p(20,235)} L${p(230,180)}" fill="none" stroke="#29394b" stroke-width="${5 * scale}" stroke-dasharray="${12 * scale} ${10 * scale}" opacity="0.7"/>
    <path d="M${p(0,-210)} L${p(20,235)}" stroke="${accent}" stroke-width="${10 * scale}" stroke-linecap="round"/>
    <path d="M${p(-72,38)} C${p(-28,68)} ${p(8,70)} ${p(44,43)}" fill="none" stroke="#d63f64" stroke-width="${9 * scale}" stroke-linecap="round"/>
    ${["P", "A", "B", "C"].map((t, i) => {
      const pts = [[0, -232], [-268, 162], [250, 183], [20, 270]][i];
      return `<circle cx="${cx + pts[0] * scale}" cy="${cy + pts[1] * scale}" r="${15 * scale}" fill="${i === 0 ? accent : "#1f8a70"}"/><text x="${cx + (pts[0] + 24) * scale}" y="${cy + (pts[1] + 8) * scale}" font-family="Georgia,serif" font-size="${32 * scale}" font-weight="700" fill="#253244">${t}</text>`;
    }).join("")}
  </g>`;
}

function cube(cx, cy, scale = 1) {
  const p = (x, y) => `${cx + x * scale},${cy + y * scale}`;
  return `
  <g>
    <polygon points="${p(-210,-110)} ${p(70,-190)} ${p(260,-58)} ${p(-20,34)}" fill="#eef6f7" stroke="#263244" stroke-width="${5 * scale}"/>
    <polygon points="${p(-210,-110)} ${p(-20,34)} ${p(-18,252)} ${p(-210,126)}" fill="#f9fbfc" stroke="#263244" stroke-width="${5 * scale}"/>
    <polygon points="${p(-20,34)} ${p(260,-58)} ${p(260,168)} ${p(-18,252)}" fill="#deebff" stroke="#263244" stroke-width="${5 * scale}"/>
    <path d="M${p(-210,126)} L${p(70,36)} L${p(260,168)} M${p(70,-190)} L${p(70,36)}" fill="none" stroke="#263244" stroke-width="${5 * scale}" stroke-dasharray="${12 * scale} ${10 * scale}" opacity="0.65"/>
    <path d="M${p(-210,-110)} L${p(260,168)}" stroke="#d63f64" stroke-width="${10 * scale}" stroke-linecap="round"/>
    <path d="M${p(70,-190)} L${p(-18,252)}" stroke="#ff9f1c" stroke-width="${10 * scale}" stroke-linecap="round"/>
    <path d="M${p(-118,-60)} C${p(-42,-72)} ${p(12,-43)} ${p(48,4)}" fill="none" stroke="#2457c5" stroke-width="${8 * scale}" stroke-linecap="round"/>
  </g>`;
}

function base(title, kicker, accent, body) {
  return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1280" viewBox="0 0 1600 1280">
  <defs>
    <linearGradient id="paper" x1="0" y1="0" x2="1600" y2="1280" gradientUnits="userSpaceOnUse">
      <stop stop-color="#f7f2e8"/>
      <stop offset="0.42" stop-color="#f8fbfc"/>
      <stop offset="1" stop-color="#e4effa"/>
    </linearGradient>
    <pattern id="grid" width="56" height="56" patternUnits="userSpaceOnUse">
      <path d="M56 0H0V56" fill="none" stroke="#cfdbe6" stroke-width="1" opacity="0.55"/>
    </pattern>
    <filter id="soft" x="-15%" y="-15%" width="130%" height="140%">
      <feDropShadow dx="0" dy="22" stdDeviation="28" flood-color="#213043" flood-opacity="0.16"/>
    </filter>
  </defs>
  <rect width="1600" height="1280" fill="url(#paper)"/>
  <rect width="1600" height="1280" fill="url(#grid)" opacity="0.5"/>
  <circle cx="1324" cy="124" r="280" fill="#ffdca8" opacity="0.36"/>
  <circle cx="170" cy="1120" r="250" fill="#bfe6df" opacity="0.42"/>
  <g transform="translate(90 76)">
    <rect x="0" y="0" width="1420" height="1128" rx="42" fill="#fbfcfd" stroke="#dbe3ea" filter="url(#soft)"/>
    <rect x="0" y="0" width="1420" height="118" rx="42" fill="#263244"/>
    <rect x="0" y="76" width="1420" height="42" fill="#263244"/>
    <text x="52" y="72" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="38" font-weight="800" fill="#ffffff">${esc(title)}</text>
    <text x="1120" y="70" font-family="Georgia,serif" font-size="28" font-weight="700" fill="${accent}">Geo Skill</text>
    <text x="54" y="166" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="24" fill="#5c6b77">${esc(kicker)}</text>
    ${body}
  </g>
</svg>`;
}

function showcase1() {
  const steps = [
    ["1", "识别题型", "正四棱锥 P-ABCD，求 BE 与平面 PAC 所成角"],
    ["2", "建立坐标", "写出 P、A、B、C、E 的坐标，所有点位可校验"],
    ["3", "向量计算", "构造方向向量与平面法向量，得到 sin θ"],
    ["4", "生成讲解", "题目、答案、分步解析、课堂提问一次生成"],
  ];
  return base("互动几何题工坊", "一句话生成可讲、可算、可视化的几何题", "#9de1d5", `
    ${panel({ x: 54, y: 210, w: 588, h: 848, title: "输入需求", subtitle: "老师只需要给出年级、知识点或题型", children: `
      <rect x="94" y="350" width="508" height="126" rx="22" fill="#f2f6f8" stroke="#d8e3eb"/>
      <text x="124" y="395" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="25" font-weight="700" fill="#253244">生成一道高中立体几何题</text>
      <text x="124" y="436" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="21" fill="#62717d">主题：线面角，难度中等，适合课堂讲解</text>
      ${badge(94, 514, "高中", "#2457c5")}
      ${badge(190, 514, "线面角", "#1f8a70")}
      ${badge(316, 514, "中等难度", "#ff8b3d")}
      ${steps.map((s, i) => `
        <g transform="translate(94 ${626 + i * 88})">
          <circle cx="24" cy="24" r="24" fill="${i === 2 ? "#d63f64" : "#263244"}"/>
          <text x="17" y="32" font-family="Georgia,serif" font-size="23" font-weight="700" fill="#fff">${s[0]}</text>
          <text x="66" y="18" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="23" font-weight="700" fill="#253244">${esc(s[1])}</text>
          <text x="66" y="49" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="18" fill="#667684">${esc(s[2])}</text>
        </g>`).join("")}
    `})}
    ${panel({ x: 692, y: 210, w: 646, h: 848, title: "生成结果预览", subtitle: "左边公式解析，右边 3D 几何体可旋转观察", children: `
      <rect x="732" y="338" width="254" height="590" rx="22" fill="#f7fafb" stroke="#dbe3ea"/>
      <text x="762" y="386" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="25" font-weight="800" fill="#253244">题目</text>
      <text x="762" y="432" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="19" fill="#51606c">正四棱锥 P-ABCD 中，</text>
      <text x="762" y="464" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="19" fill="#51606c">E 为 PC 中点，求直线</text>
      <text x="762" y="496" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="19" fill="#51606c">BE 与平面 PAC 所成角。</text>
      <rect x="762" y="548" width="196" height="64" rx="14" fill="#263244"/>
      <text x="789" y="590" font-family="Georgia,serif" font-size="28" font-weight="700" fill="#9de1d5">sin θ = 1/3</text>
      <text x="762" y="674" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="22" font-weight="800" fill="#253244">分步解析</text>
      <text x="762" y="714" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="18" fill="#62717d">建系 → 坐标 → 法向量 → 夹角</text>
      <text x="762" y="750" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="18" fill="#62717d">每一步同步高亮几何对象。</text>
      <rect x="1020" y="338" width="270" height="590" rx="22" fill="#edf5fb" stroke="#dbe3ea"/>
      ${pyramid(1155, 662, 0.56, "#2457c5")}
      <text x="1052" y="858" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="20" fill="#263244">高亮线 BE 与平面 PAC</text>
    `})}
  `);
}

function showcase2() {
  return base("从题目到互动讲解页", "不是只给答案，而是把空间关系做成看得见的步骤", "#ffd18b", `
    ${panel({ x: 54, y: 210, w: 394, h: 848, title: "题面与条件", subtitle: "自动抽取几何对象", children: `
      <text x="92" y="360" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="25" font-weight="800" fill="#253244">正方体 ABCD-A₁B₁C₁D₁</text>
      <text x="92" y="404" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="21" fill="#62717d">求 AC₁ 与 BD 所成角。</text>
      ${["点：A, B, C, D, C₁", "线：AC₁, BD", "目标：异面直线夹角", "方法：平移 + 向量"].map((t, i) => `
        <rect x="92" y="${490 + i * 82}" width="318" height="56" rx="16" fill="${i === 2 ? "#fff3de" : "#f2f6f8"}" stroke="#dbe3ea"/>
        <text x="118" y="${526 + i * 82}" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="20" font-weight="700" fill="#253244">${esc(t)}</text>`).join("")}
    `})}
    <g transform="translate(486 210)">
      <rect width="448" height="848" rx="26" fill="#253244"/>
      <text x="34" y="58" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="29" font-weight="800" fill="#fff">3D 观察区</text>
      <text x="34" y="94" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="18" fill="#b9c6d1">旋转视角，看清异面直线</text>
      <rect x="36" y="136" width="376" height="562" rx="24" fill="#f5fbff"/>
      ${cube(224, 428, 0.82)}
      <rect x="44" y="730" width="120" height="48" rx="24" fill="#9de1d5"/>
      <text x="74" y="761" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="20" font-weight="800" fill="#253244">播放</text>
      <rect x="180" y="730" width="170" height="48" rx="24" fill="#ffffff" opacity="0.16"/>
      <text x="214" y="761" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="20" font-weight="700" fill="#fff">旋转视角</text>
    </g>
    ${panel({ x: 972, y: 210, w: 366, h: 848, title: "分步解析", subtitle: "每一步对应一个画面动作", children: `
      ${[
        ["01", "把 BD 平移到过 A 的位置"],
        ["02", "写出 AC₁ 与平移后直线的方向向量"],
        ["03", "用点积公式求夹角余弦"],
        ["04", "标注最终角度与易错点"],
      ].map((s, i) => `
        <g transform="translate(1012 ${360 + i * 128})">
          <text x="0" y="0" font-family="Georgia,serif" font-size="38" font-weight="800" fill="${i === 1 ? "#ff8b3d" : "#cad5df"}">${s[0]}</text>
          <text x="0" y="42" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="22" font-weight="700" fill="#253244">${esc(s[1])}</text>
          <path d="M0 72H284" stroke="#dbe3ea" stroke-width="2"/>
        </g>`).join("")}
    `})}
  `);
}

function showcase3() {
  return base("数值同源校验", "坐标、答案和解析必须一致，避免漂亮但算错的题", "#bfe6df", `
    <g transform="translate(54 210)">
      <rect width="1330" height="338" rx="26" fill="#263244"/>
      <text x="44" y="70" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="34" font-weight="800" fill="#ffffff">让 AI 先做数学自检</text>
      <text x="44" y="116" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="23" fill="#c9d7e2">生成题目后，检查条件、坐标、公式、答案是否互相匹配。</text>
      <rect x="44" y="170" width="382" height="92" rx="20" fill="#ffffff" opacity="0.1"/>
      <text x="72" y="206" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="20" fill="#c9d7e2">公式</text>
      <text x="72" y="246" font-family="Georgia,serif" font-size="31" font-weight="800" fill="#9de1d5">d = |n·AP| / |n|</text>
      <rect x="470" y="170" width="382" height="92" rx="20" fill="#ffffff" opacity="0.1"/>
      <text x="498" y="206" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="20" fill="#c9d7e2">校验状态</text>
      <text x="498" y="246" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="31" font-weight="800" fill="#ffd18b">passed</text>
      <rect x="896" y="170" width="278" height="92" rx="20" fill="#ffffff" opacity="0.1"/>
      <text x="924" y="206" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="20" fill="#c9d7e2">可用场景</text>
      <text x="924" y="246" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="31" font-weight="800" fill="#fff">备课 / 出题</text>
    </g>
    ${panel({ x: 54, y: 596, w: 412, h: 462, title: "条件完整", subtitle: "缺少关键条件时主动补齐默认值", children: `
      ${["底面边长 = 2", "高 = 1", "E 为 PC 中点", "目标：线面角正弦"].map((t, i) => `
        <rect x="94" y="${734 + i * 72}" width="322" height="48" rx="14" fill="#f2f6f8"/>
        <text x="120" y="${765 + i * 72}" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="21" font-weight="700" fill="#253244">${esc(t)}</text>`).join("")}
    `})}
    ${panel({ x: 506, y: 596, w: 412, h: 462, title: "步骤可追踪", subtitle: "每一步都有公式和几何对象", children: `
      <path d="M568 788H852" stroke="#dbe3ea" stroke-width="8" stroke-linecap="round"/>
      <path d="M568 788H724" stroke="#1f8a70" stroke-width="8" stroke-linecap="round"/>
      <circle cx="568" cy="788" r="18" fill="#1f8a70"/>
      <circle cx="724" cy="788" r="18" fill="#1f8a70"/>
      <circle cx="852" cy="788" r="18" fill="#cad5df"/>
      <text x="568" y="850" font-family="Georgia,serif" font-size="28" font-weight="800" fill="#253244">n = PA × PC</text>
      <text x="568" y="904" font-family="Georgia,serif" font-size="28" font-weight="800" fill="#253244">sin θ = |v · n| / |v||n|</text>
    `})}
    ${panel({ x: 958, y: 596, w: 380, h: 462, title: "课堂友好", subtitle: "附带提问、易错点和变式题", children: `
      ${badge(1000, 744, "暂停提问", "#2457c5")}
      ${badge(1000, 814, "易错点", "#d63f64")}
      ${badge(1000, 884, "变式题", "#1f8a70")}
      <text x="1000" y="988" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="22" font-weight="800" fill="#253244">老师拿到就能讲，学生看完能复盘。</text>
    `})}
  `);
}

function showcase4() {
  return base("适合四类用户", "同一个 skill，覆盖备课、家教、学生自学和内容创作", "#ffb3a7", `
    ${[
      ["数学老师", "快速生成课堂例题、板书步骤和提问点", "#2457c5", "备课省时"],
      ["家教老师", "把学生错题改编成同类变式训练", "#1f8a70", "讲解清楚"],
      ["高中学生", "看懂空间关系，不再只背公式", "#d63f64", "自学复盘"],
      ["内容创作者", "产出短视频脚本和动画分镜", "#ff8b3d", "素材即用"],
    ].map((c, i) => {
      const x = 54 + (i % 2) * 684;
      const y = 232 + Math.floor(i / 2) * 420;
      return `
      <g transform="translate(${x} ${y})">
        <rect width="620" height="352" rx="30" fill="#ffffff" stroke="#dbe3ea" stroke-width="2"/>
        <circle cx="84" cy="86" r="42" fill="${c[2]}"/>
        <text x="64" y="101" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="38" font-weight="900" fill="#ffffff">${i + 1}</text>
        <text x="144" y="80" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="32" font-weight="800" fill="#253244">${esc(c[0])}</text>
        <text x="144" y="118" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="21" fill="#667684">${esc(c[3])}</text>
        <text x="64" y="202" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="27" font-weight="800" fill="#253244">${esc(c[1])}</text>
        <rect x="64" y="260" width="250" height="54" rx="27" fill="${c[2]}" opacity="0.14"/>
        <text x="92" y="295" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="21" font-weight="800" fill="${c[2]}">${esc(["生成题目", "同类变式", "分步解析", "动画分镜"][i])}</text>
      </g>`;
    }).join("")}
    <g transform="translate(350 1030)">
      <rect width="720" height="84" rx="42" fill="#263244"/>
      <text x="60" y="54" font-family="'PingFang SC','Noto Sans CJK SC','Microsoft YaHei',sans-serif" font-size="26" font-weight="800" fill="#ffffff">核心吸引力：把几何题从“文字解析”升级成“互动理解”</text>
    </g>
  `);
}

Promise.all([
  write("icon-interactive-geometry", icon(), { width: 1024, height: 1024 }),
  write("showcase-1-one-prompt-to-lesson", showcase1()),
  write("showcase-2-interactive-3d-explainer", showcase2()),
  write("showcase-3-math-verified-workflow", showcase3()),
  write("showcase-4-user-scenarios", showcase4()),
]).then((files) => {
  for (const file of files) {
    console.log(file.pngPath);
  }
}).catch((error) => {
  console.error(error);
  process.exit(1);
});
