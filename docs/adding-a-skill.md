# Adding a Skill

Use this checklist when adding a new subject skill.

## Required

```text
skills/<skill-name>/
├── SKILL.md
├── assets/
└── scripts/
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

Add one deterministic runnable script whenever possible. A useful skill should be able to produce an artifact, not only instructions.

Use `references/` only when the skill needs extra domain notes, schemas, policies, or long examples that should not live in `SKILL.md`.

## Design Principles

- Keep `SKILL.md` concise.
- Put reusable code in `scripts/`.
- Put skill-local icons or reusable visual inputs in `assets/`.
- Prefer self-contained HTML for interactive educational demos.
- Add variable ranges and edge-state handling for simulations.
