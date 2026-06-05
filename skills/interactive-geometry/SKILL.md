---
name: interactive-geometry
description: Generate geometry problems, visual explanations, and self-contained interactive HTML explainers with formulas and diagrams.
---

# Interactive Geometry

Use this skill when the user asks for geometry problem generation, geometry explanations, visual teaching pages, or runnable HTML geometry explainers.

## Language

Default to Simplified Chinese for user-facing explanations, generated problems, classroom notes, and HTML UI text, unless the user explicitly requests another language. Keep file names, script names, frontmatter, and machine-readable metadata in English.

## Core Output

Default response:

1. Problem statement.
2. Positioning: grade, difficulty, knowledge points, target ability.
3. Model: key points, lines, planes, coordinates or auxiliary construction.
4. Answer.
5. Step-by-step solution.
6. Visualization plan.
7. Common mistakes.
8. Variant problem.

If the user asks for HTML, interaction, animation, visual page, or runnable output, generate a self-contained HTML file. Prefer MathJax for formulas and SVG for deterministic diagrams. Use Three.js only when true 3D interaction is needed and the runtime can load it.

## Supported First-Version Templates

- Square pyramid line-plane angle.
- Cube skew-line angle.
- Cuboid point-to-plane distance.
- Plane geometry triangle and circle explainers.

For a runnable local example, use:

```bash
python3 scripts/generate_geometry_html.py --template square-pyramid --output square-pyramid.html
```

## Generation Rules

- Keep geometry conditions complete and unambiguous.
- Prefer clean numeric values.
- Use coordinate/vector methods for solid geometry when appropriate.
- Ensure point, line, and plane identifiers are consistent.
- Avoid claiming exact verification if a result has not been computed from the same assumptions.
- Make the visualization serve the explanation, not decoration.

## HTML Requirements

When generating HTML:

- Produce one complete file with inline CSS and JS.
- The page must open directly in a browser.
- Include the problem, formulas, steps, and visualization in one page.
- Let users step through the explanation.
- Highlight the relevant points, lines, planes, vectors, or angles for each step.
- Use MathJax from CDN for formulas unless the user requests offline-only output.
- Keep text readable for classroom projection.
- Include a short note if the diagram is schematic rather than mathematically exact.

## Suggested Layout

- Top: title and problem summary.
- Left: problem, answer, derivation, step controls.
- Right: geometry diagram with highlighted objects.
- Bottom: common mistakes and variant problem.

## YouMind Publishing Copy

See `references/youmind-form.md`.
