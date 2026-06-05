# Installation

This repository uses the common `SKILL.md` directory format used by Claude-compatible and Codex-compatible local agents.

## Codex-Style Local Skills

Symlink the skill folders into your local skill directory:

```bash
mkdir -p ~/.codex/skills
ln -s "$(pwd)/skills/interactive-geometry" ~/.codex/skills/interactive-geometry
ln -s "$(pwd)/skills/high-school-interactive-mechanics" ~/.codex/skills/high-school-interactive-mechanics
```

Then ask your agent:

```text
Use $interactive-geometry to generate a self-contained HTML explainer for a square pyramid line-plane angle problem.
```

```text
Use $high-school-interactive-mechanics to generate an incline friction simulation with adjustable mass, angle, and friction coefficient.
```

## Claude-Compatible Skills

Each skill folder is self-contained and starts with `SKILL.md`. To package one skill for a Claude-compatible environment, zip the folder contents:

```bash
cd skills/interactive-geometry
zip -r ../../interactive-geometry-skill.zip .
```

Repeat for other skill folders.

## Direct Script Usage

You can also run the scripts without installing the skill:

```bash
python3 skills/interactive-geometry/scripts/generate_geometry_html.py \
  --template square-pyramid \
  --output examples/square-pyramid.html
```

```bash
python3 skills/high-school-interactive-mechanics/scripts/generate_mechanics_html.py \
  --template incline \
  --output examples/incline-friction.html
```

Available mechanics templates:

```text
incline
projectile
circular
```
