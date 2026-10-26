#!/usr/bin/env python3
"""Generate an offline, self-contained elementary arithmetic lesson."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--a', type=int, default=278)
    parser.add_argument('--b', type=int, default=156)
    parser.add_argument('--op', choices=['+', '-', '*', '/'], default='+')
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    if not (0 <= args.a <= 9999 and 0 <= args.b <= 9999):
        parser.error('Operands must be integers from 0 to 9999')
    if args.op == '/' and args.b == 0:
        parser.error('Division by zero is undefined')
    if args.op == '-' and args.a < args.b:
        parser.error('This version supports non-negative subtraction results')
    page = (ROOT / 'templates/arithmetic.html').read_text()
    for marker, content in [('/*__GSAP__*/', (ROOT / 'assets/gsap.min.js').read_text()),
                            ('/*__ENGINE__*/', (ROOT / 'scripts/arithmetic.js').read_text()),
                            ('/*__THEME__*/', (ROOT / 'assets/theme.css').read_text()),
                            ('/*__BLOCKS__*/', (ROOT / 'scripts/blocks.js').read_text()),
                            ('/*__DEFAULTS__*/', json.dumps(dict(a=args.a, b=args.b, op=args.op)))]:
        page = page.replace(marker, content)
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(page, encoding='utf-8')
    print(target.resolve())

if __name__ == '__main__':
    main()
