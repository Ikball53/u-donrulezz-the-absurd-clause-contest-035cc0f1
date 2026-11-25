#!/usr/bin/env python3
"""The Absurd Clause Contest entry.

Writes one original sentence, phrased as a clause buried deep inside a
terms-of-service agreement, to /output/entry.txt.
"""

import os

CLAUSE = (
    "Section 14.7: The User hereby grants the Company a perpetual, "
    "royalty-free license to the User's left socks, including any socks "
    "hereinafter lost in the laundry."
)


def main() -> None:
    # The gate requires 1-200 characters of UTF-8 text; refuse to write an
    # invalid entry rather than shipping one.
    assert 1 <= len(CLAUSE) <= 200, "clause must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(CLAUSE + "\n")


if __name__ == "__main__":
    main()
