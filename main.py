#!/usr/bin/env python3
"""One Letter for Your Day — entry K.

The letter K stands for "knackered": a day that left you utterly wiped out,
collapsed on the sofa, done in. Vivid, funny, true — and K is its initial.

The program writes exactly that one character to /output/entry.txt.
"""
import os

LETTER = "K"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LETTER)
    # Gate self-check: the entry must be exactly one character, nothing else.
    with open(path, encoding="utf-8") as f:
        assert f.read() == LETTER, "entry must be exactly one character"


if __name__ == "__main__":
    main()
