# Adding a Skill

Use this checklist when adding a new subject skill.

## Required

```text
skills/<skill-name>/
├── SKILL.md
├── scripts/
├── references/
└── assets/
```

`SKILL.md` should be Claude-compatible:

```yaml
---
name: your-skill-name
description: A short trigger description under roughly 200 characters.
---
```

Keep the description broad enough for discovery, but not so broad that the skill triggers for unrelated tasks.

## Recommended

Add Codex/OpenAI UI metadata:

```text
skills/<skill-name>/agents/openai.yaml
```

Add marketplace or publishing copy:

```text
skills/<skill-name>/references/youmind-form.md
```

Add one deterministic runnable script whenever possible. A useful skill should be able to produce an artifact, not only instructions.

## Design Principles

- Keep `SKILL.md` concise.
- Put long platform copy in `references/`.
- Put reusable code in `scripts/`.
- Put icons and showcase images in `assets/`.
- Prefer self-contained HTML for interactive educational demos.
- Add variable ranges and edge-state handling for simulations.
