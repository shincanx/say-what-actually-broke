#!/usr/bin/env python3
"""Say What Actually Broke - entry 3.

Writes a single line of honest, funny error copy to /output/entry.txt.
Deterministic: same input, same output, every run.
Standard library only, no network.
"""

import os

ENTRY = (
    "Your file didn't save - the disk is full. We kept every log since 2019 "
    "and deleted nothing, so your work is the first thing we've ever thrown away."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
