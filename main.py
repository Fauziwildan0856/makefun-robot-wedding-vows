"""One-Line Robot Wedding Vows -- make.fun entry.

Writes a single line of robot wedding vows to ``entry.txt`` and validates it
against the competition gate:

* UTF-8 text of 1 to 160 characters (counted without the trailing newline),
* not only whitespace,
* a single line (no embedded newline or carriage return).

The vow follows the winner pattern for this bounty: a real wedding promise,
machine-specific details (updates, drained battery, factory reset), and a
twist that pays off in the last few words -- the vow promises to survive the
very factory reset that erases it.

Run:
    python3 main.py

The entry is written to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` when that variable
is set, otherwise to ``/output/entry.txt``. The program uses only the Python
standard library and is deterministic: every run writes byte-identical output.
"""

import os
import sys

# The vow: one line, a wedding promise, machine-specific, twist at the end.
VOW = (
    "I vow to love you through every update, every drained battery, "
    "and every factory reset \u2014 even the one that erases this vow."
)

MAX_CHARS = 160


def output_path() -> str:
    """Return the directory the entry file goes in."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def validate(text: str) -> None:
    """Check *text* against the competition gate; raise ValueError if it fails."""
    if not text:
        raise ValueError("entry is empty")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d-character limit"
            % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises UnicodeEncodeError if not encodable


def main() -> int:
    validate(VOW)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # Trailing newline is the usual file ending; the gate counts the vow text.
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(VOW + "\n")
    # Read back what was written and re-check it, so a truncated or
    # mangled file can never pass silently.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != VOW + "\n":
        raise ValueError("read-back mismatch: entry.txt does not match the vow")
    validate(written.rstrip("\n"))
    print("wrote %s (%d characters)" % (path, len(VOW)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
