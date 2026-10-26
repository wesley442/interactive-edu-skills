---
name: elementary-arithmetic-animation
description: Generate offline interactive Chinese elementary arithmetic lessons with animated column addition, subtraction, multiplication, and long division from two integers and an operator.
---

# Elementary Arithmetic Animation

Generate a runnable teaching artifact from two integers and an operator. Default to Simplified Chinese, 278 + 156, and interactive HTML when values or format are unspecified.

## Generate

Run from this skill directory:

```bash
python3 scripts/generate_arithmetic_html.py --a 1000 --b 586 --op '-' --output /absolute/path/subtraction.html
```

Supported operators: `+`, `-`, `*`, `/`. Quote shell operators. Inputs must be integers from 0 through 9999. Subtraction requires a non-negative result. Division requires a nonzero divisor and produces quotient and remainder; never imply decimal division is supported.

Open the generated HTML in a browser and return a clickable artifact. The page supports changing inputs, presets, previous/next steps, replay, automatic playback and speed. GSAP, solver and styles are embedded, with no network requirement.

## Teaching invariants

- Use `scripts/arithmetic.js` for deterministic steps; do not invent calculation steps with model arithmetic.
- Addition/subtraction start at the units place; division starts from the highest available place.
- Show individual carry operations and each stage of borrowing across zeros.
- Multiplication includes digit products, carry, shifted partial products and column-by-column partial-sum addition. Pale trailing zeros explain place value.
- Division shows taking/bringing down digits, trial quotient, product, subtraction and zero quotient placeholders. Preserve intermediate rows.
- Addition/subtraction snapshots include base-ten block metadata (`blocks`); `scripts/blocks.js` animates ten lower-place cubes merging into a rod, or a higher-place rod splitting into ten cubes. Labels state relative place values, including hundreds/thousands. Subtraction also shows cubes being removed. Multiplication/division retain their vertical lesson without a block demo.
- Every step stores a complete snapshot. Keep backwards navigation and replay consistent with forward playback.
- Below 600px, keep the fixed playback bar and safe-area padding, crop the vertical SVG to its occupied columns, and stack the block places vertically. Keep long division scrollable inside the board. Validate 320px width and long products when changing the layout.
- Distinguish answers from carry/borrow annotations by labels as well as color. Respect reduced-motion preferences.

For changes to the solver, run `node tests/arithmetic.test.cjs` from repository root, regenerate the example, and check all four operations in a browser. Check rendered digits, not only the numeric answer. Current renderer does not provide spoken narration or MP4 export.
