#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers (account B).

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt,
or /output/entry.txt when the variable is unset.
Gate: UTF-8 text, 1-120 characters, not only whitespace, one line.

The joke: A fortune-cookie prophecy in the engineer's world: the bug, the typo, the inevitability. Short declarative sentences like a real fortune, with the funniest word — tomorrow — sitting at the end.
"""

import os

LINE = 'You will fix the bug today. It was a typo. It was always a typo. It will be a typo again tomorrow.'


def build_line() -> str:
    """Return the line, validated as a single in-range line."""
    line = LINE.strip()
    if not line or "\n" in line or "\r" in line:
        raise SystemExit("entry must be one non-empty line")
    if not 1 <= len(line) <= 120:
        raise SystemExit(f"entry is {len(line)} chars, must be 1-120")
    return line


def write_entry(line: str) -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise SystemExit("round-trip check failed: entry.txt differs")
    return written


def main() -> None:
    written = write_entry(build_line())
    print(f"{written} ({len(written)} chars)")


if __name__ == "__main__":
    main()
