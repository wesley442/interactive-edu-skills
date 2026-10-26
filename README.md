# Interactive Edu Skills

[简体中文](README.zh-CN.md) | English

Open-source AI skills for generating interactive educational problem pages.

This repository is designed for two use cases:

1. Installable local-agent skills: each folder under `skills/` contains a standard `SKILL.md` that local models or coding agents can load and execute.
2. Runnable educational artifacts: bundled scripts generate self-contained interactive HTML pages that can be opened directly in a browser.

The long-term goal is to grow a reusable skill library for math, physics, chemistry, biology, and other subjects where a model can generate not only explanations, but also runnable interactive HTML pages.

The repository keeps skill slugs, file names, scripts, and machine-readable metadata in English for ecosystem compatibility. User-facing generated lessons and HTML pages default to Simplified Chinese unless the user requests another language.

## Included Skills

| Skill | Scope | Local executable output |
|---|---|---|
| `interactive-geometry` | Geometry problem generation, MathJax explanation, 2D/3D visualization plan | Self-contained HTML geometry explainer |
| `high-school-interactive-mechanics` | High-school mechanics, force diagrams, adjustable variables, motion animation | Self-contained HTML mechanics simulation |
| `elementary-arithmetic-animation` | Elementary column arithmetic, carrying, borrowing, and base-ten block animations | Self-contained offline HTML arithmetic lesson |

## Repository Layout

```text
interactive-edu-skills/
├── skills/
│   ├── interactive-geometry/
│   │   ├── SKILL.md
│   │   ├── assets/
│   │   └── scripts/
│   ├── high-school-interactive-mechanics/
│   │   ├── SKILL.md
│   │   ├── assets/
│   │   ├── references/
│   │   └── scripts/
│   └── elementary-arithmetic-animation/
│       ├── SKILL.md
│       ├── agents/
│       ├── assets/
│       ├── scripts/
│       └── templates/
├── docs/
│   ├── adding-a-skill.md
│   └── installation.md
└── examples/
```

## Install Locally

For Codex-style local skills, copy or symlink the skill folders into your skill directory:

```bash
mkdir -p ~/.codex/skills
ln -s "$(pwd)/skills/interactive-geometry" ~/.codex/skills/interactive-geometry
ln -s "$(pwd)/skills/high-school-interactive-mechanics" ~/.codex/skills/high-school-interactive-mechanics
ln -s "$(pwd)/skills/elementary-arithmetic-animation" ~/.codex/skills/elementary-arithmetic-animation
```

After installation, ask your local model or agent for tasks such as:

```text
Use the high-school-interactive-mechanics skill to generate a self-contained HTML page for an incline friction problem with adjustable mass, angle, and friction coefficient.
```

```text
Use the interactive-geometry skill to generate an interactive geometry explainer for a square pyramid line-plane angle problem.
```

```text
Use the elementary-arithmetic-animation skill to generate an offline lesson for 1000 minus 586, showing each borrowing step and base-ten block exchange.
```

See [docs/installation.md](docs/installation.md) for Claude-compatible packaging and direct script usage.

## Run Reference Generators

The bundled scripts are intentionally small and dependency-light. They generate self-contained reference HTML files that can be opened directly in a browser. Installed skills should use the full `SKILL.md` instructions when generating custom pages for a user request.

Available geometry templates:

| Template | Topic | Example |
|---|---|---|
| `square-pyramid` | Square pyramid line-plane angle | `examples/square-pyramid.html` |
| `cube-distance` | Cube point-to-plane distance | `examples/cube-distance.html` |
| `dihedral-angle` | Regular tetrahedron dihedral angle | `examples/dihedral-angle.html` |

Available mechanics templates:

| Template | Topic | Example |
|---|---|---|
| `incline` | Incline friction and force analysis | `examples/incline-friction.html` |
| `projectile` | Projectile motion | `examples/projectile-motion.html` |
| `circular` | Uniform circular motion | `examples/circular-motion.html` |
| `spring-energy` | Spring energy conversion | `examples/spring-energy.html` |
| `connected-bodies` | Connected bodies, tension, and friction | `examples/connected-bodies.html` |

Available elementary arithmetic templates:

| Template | Topic | Example |
|---|---|---|
| `elementary-arithmetic` | Column addition, subtraction, multiplication, and long division with carrying and borrowing | `examples/elementary-arithmetic.html` |

Set the operands with `--a`, `--b`, and `--op`, or change them inside the page. Supports integers 0–9999, non-negative subtraction results, and quotient/remainder division. Addition and subtraction include base-ten block exchanges. The offline page supports mobile layouts, step controls, replay, and adjustable playback.

Generate any single template:

```bash
python3 skills/high-school-interactive-mechanics/scripts/generate_mechanics_html.py \
  --template spring-energy \
  --output examples/spring-energy.html
```

```bash
python3 skills/interactive-geometry/scripts/generate_geometry_html.py \
  --template cube-distance \
  --output examples/cube-distance.html
```

```bash
python3 skills/elementary-arithmetic-animation/scripts/generate_arithmetic_html.py \
  --a 1000 --b 586 --op '-' \
  --output examples/elementary-arithmetic.html
```

Regenerate all bundled examples:

```bash
python3 skills/interactive-geometry/scripts/generate_geometry_html.py --template square-pyramid --output examples/square-pyramid.html
python3 skills/interactive-geometry/scripts/generate_geometry_html.py --template cube-distance --output examples/cube-distance.html
python3 skills/interactive-geometry/scripts/generate_geometry_html.py --template dihedral-angle --output examples/dihedral-angle.html

python3 skills/high-school-interactive-mechanics/scripts/generate_mechanics_html.py --template incline --output examples/incline-friction.html
python3 skills/high-school-interactive-mechanics/scripts/generate_mechanics_html.py --template projectile --output examples/projectile-motion.html
python3 skills/high-school-interactive-mechanics/scripts/generate_mechanics_html.py --template circular --output examples/circular-motion.html
python3 skills/high-school-interactive-mechanics/scripts/generate_mechanics_html.py --template spring-energy --output examples/spring-energy.html
python3 skills/high-school-interactive-mechanics/scripts/generate_mechanics_html.py --template connected-bodies --output examples/connected-bodies.html

python3 skills/elementary-arithmetic-animation/scripts/generate_arithmetic_html.py --a 278 --b 156 --op '+' --output examples/elementary-arithmetic.html
```

Verify the elementary arithmetic solver:

```bash
node tests/arithmetic.test.cjs
```

See the [elementary arithmetic design and engine selection](docs/elementary-arithmetic-project.zh-CN.md).

Preview the reference pages:

Geometry skill (`interactive-geometry`):

- [Square pyramid geometry explainer](https://wesley442.github.io/interactive-edu-skills/examples/square-pyramid.html)
- [Cube point-to-plane distance explainer](https://wesley442.github.io/interactive-edu-skills/examples/cube-distance.html)
- [Regular tetrahedron dihedral angle explainer](https://wesley442.github.io/interactive-edu-skills/examples/dihedral-angle.html)

Mechanics skill (`high-school-interactive-mechanics`):

- [Incline friction simulation](https://wesley442.github.io/interactive-edu-skills/examples/incline-friction.html)
- [Projectile motion animation](https://wesley442.github.io/interactive-edu-skills/examples/projectile-motion.html)
- [Circular motion simulation](https://wesley442.github.io/interactive-edu-skills/examples/circular-motion.html)
- [Spring energy simulation](https://wesley442.github.io/interactive-edu-skills/examples/spring-energy.html)
- [Connected bodies simulation](https://wesley442.github.io/interactive-edu-skills/examples/connected-bodies.html)

Elementary mathematics skill (`elementary-arithmetic-animation`):

- [Elementary column arithmetic and base-ten block animations](https://wesley442.github.io/interactive-edu-skills/examples/elementary-arithmetic.html)

## Roadmap

- More mechanics templates: pulley systems, collisions, circular critical motion.
- More geometry templates: skew-line angle, sphere/cone/cylinder sections, plane-geometry proof pages.
- Electromagnetism skill.
- Chemistry reaction and molecule visualization skill.
- Biology process animation skill.
- Shared schema for interactive educational scenes.

## License

MIT. See [LICENSE](LICENSE).

GSAP used in the arithmetic animations is distributed under its own license. See the [third-party license notice](skills/elementary-arithmetic-animation/assets/THIRD_PARTY.md).
