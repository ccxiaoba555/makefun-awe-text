"""Write a short text to /output/entry.txt.

Deterministic, offline, standard library only. Running the program
twice produces byte-identical output.
"""

import os

TEXT = (
    "The light touching your skin left its star before the first "
    "cities were built. It crossed the dark without hurrying, and "
    "it will keep travelling long after we are gone \u2014 yet for "
    "one quiet moment it rests here, warm as a held hand."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
