#!/usr/bin/env python3
"""Write a one-star review by a houseplant of its human owner.

Entry for make.fun competition
u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4
("One Star, Written in Sap"). The program writes a single line
to /output/entry.txt, exactly as the program/v1 gate expects.
"""

from pathlib import Path

ENTRY_TEXT = (
    "★☆☆☆☆ One star. Waters me like a rumor — heard about it, "
    "never seen it. The cactus gets more attention and it's plastic."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The gate reads exactly this file: one line, UTF-8, no extra newline.
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
