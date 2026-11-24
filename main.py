"""One Word for Your Wi-Fi entry (Python 3.13, standard library only).

The entry is a single word: "Houdini".

Why this word: home Wi-Fi does its best escape-artist impression —
there for the video call, gone the second the call matters, back again
like nothing happened. It is funny at once, instantly understood with
no context, true to how home Wi-Fi actually behaves, and a fresh angle
on the most familiar annoyance (the signal vanishing) rather than the
words everyone reaches for.

The program writes the word to the output directory as entry.txt and
verifies the written bytes afterwards: UTF-8 text, 1 to 20 characters,
not only white space, and a single word with no spaces.
"""

import os
from pathlib import Path

WORD = "Houdini"
MAX_CHARS = 20


def output_path() -> Path:
    """Where the grader reads the entry: MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    return out_dir / "entry.txt"


def check_word(word: str) -> None:
    """Raise ValueError unless the word passes the competition gate."""
    if not word or word != word.strip():
        raise ValueError("entry must be non-empty text with no padding")
    if len(word) > MAX_CHARS:
        raise ValueError(f"entry is {len(word)} chars, over the 20-char cap")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word with no spaces")
    if not word.isalpha():
        raise ValueError("entry must be letters only, no digits or punctuation")


def write_entry(word: str) -> Path:
    """Write the word, then read it back and verify it in full."""
    check_word(word)
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    data = word.encode("utf-8")
    target.write_bytes(data)
    written = target.read_bytes()
    if written != data:
        raise IOError("read-back bytes differ from the entry")
    if written.decode("utf-8") != word:
        raise ValueError("read-back text differs from the entry")
    return target


def main() -> None:
    target = write_entry(WORD)
    print(f"wrote {target} ({target.stat().st_size} bytes): {WORD}")


if __name__ == "__main__":
    main()
