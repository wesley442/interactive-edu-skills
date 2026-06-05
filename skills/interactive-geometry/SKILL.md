---
name: interactive-geometry
description: Generate math geometry problems, step-by-step solutions, teaching notes, visual explanations, and self-contained interactive HTML/Three.js geometry teaching pages.
---

# Interactive Geometry

Use this skill when the user asks for geometry problem generation, geometry explanations, visual teaching pages, classroom activities, or runnable HTML geometry explainers.

## Language

Default to Simplified Chinese for user-facing explanations, generated problems, classroom notes, and HTML UI text, unless the user explicitly requests another language. Keep file names, script names, frontmatter, and machine-readable metadata in English.

## Scope

Use this skill for:

- Random geometry problem generation.
- Junior-high, high-school, and competition-style geometry.
- Solid geometry: line-plane angles, dihedral angles, skew-line angles, point-to-plane distance, volumes, sections, projections, parallel/perpendicular relations.
- Plane geometry: triangles, circles, similarity, congruence, area, angle chasing, and proof problems.
- Adapting an existing geometry problem into a new problem.
- Producing step-by-step solutions, teaching prompts, visual explanation plans, or interactive HTML teaching pages.

## Input Recognition

Before generating, identify:

1. Grade: junior high, high school, competition, or unspecified.
2. Geometry type: plane geometry, solid geometry, or unspecified.
3. Task type: angle, length, area, volume, proof, distance, dihedral angle, line-plane angle, etc.
4. Difficulty: basic, medium, hard, competition.
5. Output form: problem only, problem plus answer, full solution, or interactive teaching page.
6. Whether the user wants random parameters, variants, classroom explanation, or student hints.

If key details are missing, do not repeatedly ask. Use reasonable defaults:

- Default grade: high school.
- Default difficulty: medium.
- Default task type: solid-geometry mixed problem.
- Default output: problem, answer, step-by-step solution, visualization plan, common mistakes, and one variant problem.

## Core Output

Default response:

1. Problem statement.
2. Positioning: grade, difficulty, knowledge points, target ability.
3. Answer.
4. Step-by-step solution.
5. Visualization plan.
6. Common mistakes.
7. Variant problem.

Use a clear teacher-like style. Explain why each construction or formula is used; do not only list formulas.

## Problem Design Workflow

1. Determine the design target: knowledge points, difficulty, assessed ability, target students, and problem highlight.
2. Generate a complete, unambiguous problem with clean values and verifiable conclusions.
3. For solid geometry, prefer common classroom structures: cube, cuboid, square pyramid, triangular pyramid, prism, cylinder, cone, sections, projections, parallel/perpendicular relations, angles, distances, and volumes.
4. Solve with a reliable method. For high-school solid geometry, prefer coordinate/vector methods:
   - Establish a coordinate system.
   - Write key point coordinates.
   - Construct direction vectors or normal vectors.
   - Use dot product, cross product, distance formulas, projection formulas, or volume formulas.
   - Keep final answers consistent with the calculation.
5. Add a visualization plan: highlighted points, lines, planes, angles, camera focus, rotation/zoom observations, and pause points for classroom questions.
6. Self-check uniqueness, condition/result consistency, clean values, answer/solution consistency, readability of the figure description, and teaching value.

## Supported First-Version Templates

- Square pyramid line-plane angle.
- Cube skew-line angle.
- Cuboid point-to-plane distance.
- Cube point-to-plane distance.
- Regular tetrahedron dihedral angle.
- Plane geometry triangle and circle explainers.

For a runnable local example, use:

```bash
python3 scripts/generate_geometry_html.py --template square-pyramid --output square-pyramid.html
```

The square-pyramid template is the canonical quality baseline for geometry HTML output. It uses a dark classroom UI, MathJax, a Three.js 3D scene, draggable rotation, wheel zoom, step-by-step highlighting, 2D labels over 3D geometry, solution tabs, common mistakes, and a variant problem. The cube-distance and dihedral-angle templates provide lightweight SVG-based alternatives for deterministic local execution. Match this level for user-facing interactive geometry pages.

## Generation Rules

- Keep geometry conditions complete and unambiguous.
- Prefer clean numeric values.
- Use coordinate/vector methods for solid geometry when appropriate.
- Ensure point, line, and plane identifiers are consistent.
- Avoid claiming exact verification if a result has not been computed from the same assumptions.
- Make the visualization serve the explanation, not decoration.

## Default Format

```markdown
# 题目
[完整题干]

# 题目定位
- 年级：
- 难度：
- 知识点：
- 考查能力：

# 答案
[最终答案]

# 分步解析
1. [建模/作图思路]
2. [关键计算]
3. [结论]

# 可视化讲解
- 初始画面：
- 第 1 步高亮：
- 第 2 步高亮：
- 关键观察：
- 课堂提问：

# 易错点
[列出 2-3 个常见错误]

# 变式题
[给出 1 道同知识点变式题]
```

## HTML Requirements

When generating HTML:

- Produce one complete file with inline CSS and JS.
- The page must open directly in a browser.
- Include the problem, formulas, steps, and visualization in one page.
- Let users step through the explanation.
- Highlight the relevant points, lines, planes, vectors, or angles for each step.
- Use MathJax from CDN for formulas unless the user requests offline-only output.
- For 3D solid geometry, prefer Three.js. Provide drag-to-rotate, wheel-to-zoom, reset view, step controls, and visible labels.
- Keep text readable for classroom projection.
- Include a short note if the diagram is schematic rather than mathematically exact.

## Suggested Layout

- Top: title, grade, difficulty, and knowledge tags.
- Left: tabs for problem, answer/steps, common mistakes, and variant problem.
- Right: interactive 2D/3D geometry scene with highlighted objects.
- Overlay: current step, camera/drag hints, previous/next/reset controls.
