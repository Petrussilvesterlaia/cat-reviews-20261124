#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one funny single-line one-star review, written by a house cat
about the human it lives with, to /output/entry.txt.

Gate: the file must be UTF-8 text of 1 to 200 characters, a single line,
not only white space.
"""

import os
import sys

REVIEW = (
    "One star. He bought me a $400 cat tree, then looked betrayed "
    "when I slept in the box it came in. I stand by my choice."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Check the review against the competition gate before writing."""
    if not text or not text.strip():
        raise ValueError("review is empty or only white space")
    if len(text) > 200:
        raise ValueError(f"review is {len(text)} characters, over the 200 limit")
    if len(text) < 1:
        raise ValueError("review must be at least 1 character")
    for sep in ("\n", "\r", "\u2028", "\u2029"):
        if sep in text:
            raise ValueError(f"review must be a single line (contains {sep!r})")
    if text != text.strip():
        raise ValueError("review has leading or trailing white space")


def validate_file_content(text: str) -> None:
    """Check exactly what landed on disk: one line, no trailing newline."""
    validate(text)
    if text.endswith("\n"):
        raise ValueError("file must not end with a trailing newline")


def main() -> int:
    validate(REVIEW)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(REVIEW)
    # Read-back verification: what landed on disk must be exactly REVIEW.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != REVIEW:
        raise ValueError("read-back mismatch: file content differs from review")
    validate_file_content(written)
    print(f"Wrote {len(written)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
