"""Write a short text to /output/entry.txt.

Deterministic, standard library only, offline. The text is meant to
slow the reader down: a small shore scene under old starlight, an
image that keeps growing after the last line.
"""

import os

TEXT = (
    "The tide was still coming in while the stars were out, and a small "
    "crab crossed the wet sand, leaving a line of prints the water took "
    "back one by one. That starlight left before the first cities "
    "were built, and it is still on its way down."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
