#!/usr/bin/env python3
"""Say What Actually Broke -- entry program.

Writes one line of software error copy to /output/entry.txt: at most
200 characters, telling the user the brutal truth about what went
wrong and making them laugh on the way.

Python 3.13 standard library only. No network. Deterministic:
every run writes the same bytes.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

ERROR_LINE = (
    "Our last deploy broke this page — not you, not your wifi, "
    "not Mercury in retrograde. We've rolled it back; refresh and "
    "pretend we're professionals."
)


def main() -> None:
    if not 1 <= len(ERROR_LINE) <= 200 or not ERROR_LINE.strip():
        raise SystemExit("error line must be 1-200 non-blank characters")
    if "\n" in ERROR_LINE or "\r" in ERROR_LINE:
        raise SystemExit("error line must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ERROR_LINE)
    # Read back and verify the gate: UTF-8 text of 1 to 200
    # characters, not only white space, a single line, byte for
    # byte the error line. Fail loudly instead of shipping bad output.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ERROR_LINE:
        raise SystemExit("entry.txt does not match the error line")


if __name__ == "__main__":
    main()
