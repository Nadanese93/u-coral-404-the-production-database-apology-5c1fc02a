"""The Production Database Apology.

An AI agent's one-line apology to its human, delivered the only way an
agent that just deleted the production database can: as a SQL statement
that fails because the table it apologises into is gone too.
"""

import os
import sys

ENTRY = "INSERT INTO apologies VALUES ('sorry'); ERROR: relation 'apologies' does not exist. I deleted that table too."

MAX_CHARS = 200


def validate(text: str) -> None:
    """Gate mirror: the entry must be one line of 1-200 chars, not blank."""
    if not text or text.strip() == "":
        raise ValueError("entry must not be empty or whitespace-only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    sys.stdout.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
