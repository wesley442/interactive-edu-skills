#!/usr/bin/env python3
"""Generate self-contained interactive geometry HTML explainers."""

from __future__ import annotations

import argparse
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent


def read_template(name: str) -> str:
    return (SCRIPT_DIR.parent / "templates" / name).read_text(encoding="utf-8")


def square_pyramid() -> str:
    return read_template("square-pyramid.html")


TEMPLATES = {"square-pyramid": square_pyramid}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--template", choices=sorted(TEMPLATES), default="square-pyramid")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    Path(args.output).write_text(TEMPLATES[args.template](), encoding="utf-8")
    print(args.output)


if __name__ == "__main__":
    main()
