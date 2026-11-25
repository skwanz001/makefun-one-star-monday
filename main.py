#!/usr/bin/env python3
"""One Star for Monday — one-star restaurant review of Monday.

Writes a single line of plain text (<= 25 words, 1-180 chars) to
/output/entry.txt, as required by the competition kit.
Standard library only.
"""

import os

# The joke, mapped onto the restaurant frame:
#   table  -> seated by the toilets (worst table in the house)
#   dish   -> motivation served cold (Monday kills motivation)
#   bill   -> charged for the whole week (Monday is day one: it
#             bills you for all seven days up front)
# One line, 19 words, no hashtags, no stage directions.

ENTRY = "One star. Monday seated me by the toilets, served my motivation cold, and charged me for the whole week."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    words = ENTRY.split()
    assert 1 <= len(words) <= 25, f"word count {len(words)} out of range"
    assert 1 <= len(ENTRY) <= 180, f"char count {len(ENTRY)} out of range"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Echo the verified artifact so a local run shows exactly what ships.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "output does not match the entry line"
    print(f"{len(words)} words, {len(ENTRY)} chars -> {OUTPUT_PATH}")
    print(written)


if __name__ == "__main__":
    main()
