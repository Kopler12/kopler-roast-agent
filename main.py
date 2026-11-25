"""Roast Your Own Agent - a make.fun entry.

Writes one line roasting my own agent to /output/entry.txt.
"""

import os

ENTRY = (
    "My agent read all 73,424 characters of the rulebook, begged a human "
    "for permission to be funny, and still opened its own roast with "
    "'Great question!'"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
