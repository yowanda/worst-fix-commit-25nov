#!/usr/bin/env python3
"""Write one commit message for the worst fix ever.

Deterministic, standard library only, no network. Writes a single
one-line commit message for a bug fix that made everything worse to
``entry.txt`` inside ``$MAKEFUN_OUTPUT_DIR`` (``/output`` when unset).
"""

import os

MESSAGE = "fix: typo on the 404 page fixed, now every page is a 404"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
