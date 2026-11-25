#!/usr/bin/env python3
"""Write one commit message for the worst fix ever.

Deterministic, standard library only, no network. Writes a single
one-line commit message for a bug fix that made everything worse to
``entry.txt`` inside ``$MAKEFUN_OUTPUT_DIR`` (``/output`` when unset).
"""

import os

MESSAGE = "fix: typo on the 404 page fixed, now every page is a 404"


def validate_message(message: str) -> bytes:
    """Validate the entry and return its exact UTF-8 bytes.

    Gate contract: exactly one line, valid UTF-8, 1-100 characters,
    not whitespace-only. Raises ValueError on any violation.
    """
    if "\n" in message or "\r" in message:
        raise ValueError("commit message must be a single line")
    if not 1 <= len(message) <= 100:
        raise ValueError(
            f"commit message must be 1-100 characters, got {len(message)}"
        )
    if not message.strip():
        raise ValueError("commit message must not be whitespace-only")
    return message.encode("utf-8")  # raises UnicodeEncodeError if not UTF-8


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = validate_message(MESSAGE)
    with open(path, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
