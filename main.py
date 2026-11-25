#!/usr/bin/env python3
"""One line from the Moon, for the make.fun bounty 'The Moon Finally Answers Back'.

Writes the Moon's answer to /output/entry.txt, byte-exact.
"""

import os

ENTRY = "You spent centuries wishing on me and never once said please. So tonight, my answer is: no."
# The Moon has spoken; one line, no encore.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
