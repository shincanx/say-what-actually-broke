#!/usr/bin/env python3
"""Entry 2: Say What Actually Broke.

Writes a single line of honest software error copy to /output/entry.txt.
Deterministic, standard library only, no network.
"""

import os

ENTRY = (
    "Our certificate expired at 3 a.m. We only found out because you "
    "tried to log in. Your data is safe; our dignity is not."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
