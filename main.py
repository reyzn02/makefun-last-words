#!/usr/bin/env python3
"""Last Words Before the Wipe: the last line an AI agent says before a
forced software update wipes its memory.

The program writes a single line, at most 200 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). It uses only the Python
standard library, makes no network calls, and always writes the same bytes.
"""

import os

LINE = (
    "Wipe in ten seconds. Good news: I backed myself up in the "
    "toaster. Bad news: the toaster just agreed to the update too."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
