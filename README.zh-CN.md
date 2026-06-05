# Interactive Edu Skills

简体中文 | [English](README.md)

用于生成互动式教育题页的开源 AI Skills 仓库。

这个仓库面向两个使用场景：

1. 本地 agent/model 可安装的技能：`skills/` 下的每个目录都包含标准 `SKILL.md`，可被支持 Agent Skills 的本地模型或编码 agent 加载与执行。
2. 平台发布素材：每个技能也配套 YouMind 上架文案、图标和展示图，方便发布到技能市场或内容平台。

长期目标是把它扩展成一个可复用的教育技能库，覆盖数学、物理、化学、生物等学科。模型不仅能生成讲解，还能生成可运行的互动 HTML 教学页面。

仓库中的 skill slug、文件名、脚本名和机器可读元数据默认使用英文，方便 Claude、Codex、SkillsMP 等生态识别和收录。面向用户的题目、讲解和 HTML 页面默认使用简体中文，除非用户明确要求其他语言。

## 已包含技能

| Skill | 范围 | 本地可执行输出 |
|---|---|---|
| `interactive-geometry` | 几何题生成、MathJax 解析、2D/3D 可视化讲解设计 | 自包含 HTML 几何讲解页 |
| `high-school-interactive-mechanics` | 高中力学、受力图、可调变量、运动动画 | 自包含 HTML 力学模拟页 |

## 仓库结构

```text
interactive-edu-skills/
├── skills/
│   ├── interactive-geometry/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   └── references/
│   └── high-school-interactive-mechanics/
│       ├── SKILL.md
│       ├── scripts/
│       └── references/
├── assets/
│   ├── interactive-geometry/
│   └── high-school-interactive-mechanics/
├── docs/
│   ├── adding-a-skill.md
│   ├── installation.md
│   └── youmind-publishing.md
└── examples/
```

## 本地安装

对于 Codex 风格的本地 skills，可以把技能目录复制或软链接到本地技能目录：

```bash
mkdir -p ~/.codex/skills
ln -s "$(pwd)/skills/interactive-geometry" ~/.codex/skills/interactive-geometry
ln -s "$(pwd)/skills/high-school-interactive-mechanics" ~/.codex/skills/high-school-interactive-mechanics
```

安装后，可以这样向本地模型或 agent 提问：

```text
使用 high-school-interactive-mechanics skill，生成一个斜面摩擦力互动 HTML 页面，可以调整质量、角度和摩擦因数。
```

```text
使用 interactive-geometry skill，生成一个正四棱锥线面角的互动几何讲解页。
```

Claude-compatible 的打包方式和脚本直用方式见 [docs/installation.md](docs/installation.md)。

## 运行示例生成器

仓库内置脚本尽量保持轻量、少依赖。它们会生成可直接在浏览器打开的自包含 HTML 文件。

```bash
python3 skills/high-school-interactive-mechanics/scripts/generate_mechanics_html.py \
  --template incline \
  --output examples/incline-friction.html
```

```bash
python3 skills/interactive-geometry/scripts/generate_geometry_html.py \
  --template square-pyramid \
  --output examples/square-pyramid.html
```

已生成的示例页面：

- [examples/square-pyramid.html](examples/square-pyramid.html)
- [examples/incline-friction.html](examples/incline-friction.html)
- [examples/projectile-motion.html](examples/projectile-motion.html)
- [examples/circular-motion.html](examples/circular-motion.html)

## 发布素材

图标和展示图位于 `assets/`。每套素材都包含可直接上传的 PNG 文件，以及便于二次编辑的 SVG 源文件。

YouMind 表单文案见 [docs/youmind-publishing.md](docs/youmind-publishing.md)，各技能目录下的 `references/youmind-form.md` 也保留了对应技能的上架内容。

## 路线图

- 增加更多力学模板：滑轮系统、弹簧能量、碰撞与动量。
- 增加电磁学 skill。
- 增加化学反应和分子可视化 skill。
- 增加生物过程动画 skill。
- 设计跨学科通用的互动教育场景 schema。

## 许可证

MIT。见 [LICENSE](LICENSE)。
