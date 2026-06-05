---
name: high-school-interactive-mechanics
description: Generate high-school mechanics problems, force diagrams, adjustable simulations, and self-contained interactive HTML pages.
---

# High-School Interactive Mechanics

Use this skill when the user asks for high-school physics mechanics problems, force analysis, motion visualization, variable sliders, or runnable HTML simulations.

## Language

Default to Simplified Chinese for user-facing explanations, generated problems, classroom notes, and HTML UI text, unless the user explicitly requests another language. Keep file names, script names, frontmatter, and machine-readable metadata in English.

## Scope

Prefer high-school mechanics:

- Uniformly accelerated linear motion.
- Newton's laws.
- Inclines and friction.
- Connected bodies and rope tension.
- Projectile motion.
- Circular motion.
- Springs and Hooke's law.
- Work-energy theorem.
- Mechanical energy conservation.
- Momentum conservation and collisions.

If the user asks for complex electromagnetism, thermodynamics, waves, university mechanics, or engineering-grade simulation, state the limitation and give a high-school-accessible version when possible.

## Core Output

Default response:

1. Problem statement.
2. Positioning: grade, difficulty, knowledge points, target ability.
3. Physical model: object of study, motion process, knowns, unknowns, constraints.
4. Force analysis.
5. Step-by-step derivation.
6. Answer.
7. Visualization or animation plan.
8. Common mistakes.
9. Variant problem.

If the user asks for HTML, interactive page, animation, adjustable variables, sliders, or simulation, generate a self-contained HTML file.

Before generating any problem or HTML, explicitly determine:

1. Object of study.
2. Motion process.
3. Known quantities.
4. Unknown quantities.
5. Constraints.
6. Required forces.
7. Method: Newton's laws, kinematics, energy, or momentum.
8. Adjustable variables.
9. Edge states: no motion, critical state, reverse direction, or invalid setup.

## Supported First-Version Templates

- Incline friction: adjustable mass, angle, friction coefficient, gravity.
- Projectile motion: adjustable initial velocity, height, gravity.
- Circular motion: adjustable mass, radius, speed.
- Connected bodies and springs can be generated as explanations; interactive scripts should be added as templates before claiming deterministic local execution.

For a basic runnable reference example, use:

```bash
python3 scripts/generate_mechanics_html.py --template incline --output incline-friction.html
```

The incline template is the canonical quality baseline for mechanics HTML output. It uses a dark classroom UI, a Canvas scene, `requestAnimationFrame`, adjustable sliders, motion-state detection, force-vector drawing, tabs, history records, and classroom helper actions. For user-facing generated HTML, match that level of interaction and follow the full interactive HTML spec in `references/interactive-html-spec.zh-CN.md`.

## Physics Rules

- Always identify the object of study before force analysis.
- Friction direction must follow relative motion or relative motion tendency.
- Distinguish velocity, acceleration, force, and displacement directions.
- Explain why each equation applies.
- Do not treat centripetal force as an extra new force; explain it as net force or the effect of a concrete force.
- Include units and reasonable variable ranges.
- Mention static, critical, no-motion, or direction-change states when relevant.

## HTML Requirements

When generating HTML:

- Produce one complete file with inline CSS and JS.
- The page must open directly in a browser.
- Use MathJax for formulas.
- Use SVG or Canvas for 2D diagrams and animations.
- Include sliders for adjustable variables.
- Variable changes must update formulas, numeric results, force arrows, motion state, and the diagram.
- Use `requestAnimationFrame` for animation when motion is shown.
- Clamp variables to reasonable ranges.
- Clearly display critical states, such as no sliding, zero acceleration, or direction change.
- Keep the layout readable for classroom projection.
- Explain why each equation is used; do not only display formulas.
- Show at least one visual change that makes animation obvious, such as moving objects, velocity vectors, force arrows, traces, changing energy bars, or step highlights.

For detailed Chinese requirements and variable templates, read `references/interactive-html-spec.zh-CN.md` when the user asks for HTML, animation, adjustable variables, or slider controls.

## Suggested Layout

- Top: title and problem.
- Left: sliders, current values, answer, derivation.
- Right: animation or force diagram.
- Bottom: common mistakes and variant problem.
