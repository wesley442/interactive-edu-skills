# Interactive Edu Skills

Open-source AI skills for generating interactive educational problem pages.

This repository is designed for two use cases:

1. Installable local-agent skills: each folder under `skills/` contains a standard `SKILL.md` that local models or coding agents can load and execute.
2. Marketplace publishing assets: each skill also includes YouMind-ready copy, icons, and showcase images.

The long-term goal is to grow a reusable skill library for math, physics, chemistry, biology, and other subjects where a model can generate not only explanations, but also runnable interactive HTML pages.

The repository keeps skill slugs, file names, scripts, and machine-readable metadata in English for ecosystem compatibility. User-facing generated lessons and HTML pages default to Simplified Chinese unless the user requests another language.

## Included Skills

| Skill | Scope | Local executable output |
|---|---|---|
| `interactive-geometry` | Geometry problem generation, MathJax explanation, 2D/3D visualization plan | Self-contained HTML geometry explainer |
| `high-school-interactive-mechanics` | High-school mechanics, force diagrams, adjustable variables, motion animation | Self-contained HTML mechanics simulation |

## Repository Layout

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
│   └── youmind-publishing.md
└── examples/
```

## Install Locally

For Codex-style local skills, copy or symlink the skill folders into your skill directory:

```bash
mkdir -p ~/.codex/skills
ln -s "$(pwd)/skills/interactive-geometry" ~/.codex/skills/interactive-geometry
ln -s "$(pwd)/skills/high-school-interactive-mechanics" ~/.codex/skills/high-school-interactive-mechanics
```

After installation, ask your local model or agent for tasks such as:

```text
Use the high-school-interactive-mechanics skill to generate a self-contained HTML page for an incline friction problem with adjustable mass, angle, and friction coefficient.
```

```text
Use the interactive-geometry skill to generate an interactive geometry explainer for a square pyramid line-plane angle problem.
```

See [docs/installation.md](docs/installation.md) for Claude-compatible packaging and direct script usage.

## Run Example Generators

The bundled scripts are intentionally small and dependency-light. They generate self-contained HTML files that can be opened directly in a browser.

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

## Publishing Assets

Icons and showcase images live under `assets/`. Each asset set includes PNG files for direct upload and SVG sources for editing.

See [docs/youmind-publishing.md](docs/youmind-publishing.md) for the skill form copy.

## Roadmap

- More mechanics templates: pulley systems, spring energy, collisions.
- Electromagnetism skill.
- Chemistry reaction and molecule visualization skill.
- Biology process animation skill.
- Shared schema for interactive educational scenes.

## License

MIT. See [LICENSE](LICENSE).
