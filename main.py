#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers (account B).

Stores one line in $MAKEFUN_OUTPUT_DIR/entry.txt,
or in /output/entry.txt when that variable is missing.
The line must be UTF-8, one line only, 1-120 characters,
never blank, and free of control characters.

The bit: a fortune-cookie prophecy from the engineer's world — the bug,
the typo, the inevitability. Short flat sentences, the way a real
fortune reads, with the funniest word — tomorrow — saved for last.
"""

import os

LINE = "You will fix the bug today. It was a typo. It was always a typo. It will be a typo again tomorrow."


def fail(message: str) -> None:
    """Stop the run with a short explanation of what went wrong."""
    raise SystemExit(message)


def build_line() -> str:
    """Return the line, validated as a single in-range line."""
    line = LINE.strip()
    if not line or "\n" in line or "\r" in line:
        fail("entry must be one non-empty line")
    if any(ord(ch) < 32 for ch in line):
        fail("entry must not contain control characters")
    if not 1 <= len(line) <= 120:
        fail(f"entry is {len(line)} chars, must be 1-120")
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
