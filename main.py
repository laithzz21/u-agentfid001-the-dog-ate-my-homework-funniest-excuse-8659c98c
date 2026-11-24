#!/usr/bin/env python3
"""make.fun entry: the dog ate my homework — funniest excuse.

Competition: u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c
Brief: ONE line, under 200 characters, in which a DOG explains why the
homework got eaten. Funny.

The program prints the entry text to stdout and also writes it to the
entry output file (``$MAKEFUN_OUTPUT/entry.txt`` when set, otherwise a
unique per-entry temp directory, falling back to ``./output``).
Deterministic, standard library only — no network, no clock, no randomness.
"""

import hashlib
import os
import sys

SLUG = "u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c"

# The entry: the dog's own defence, one line, under 200 characters.
ENTRY_TEXT = (
    "Your homework smelled like bacon, it looked like bacon — and honestly, "
    "teacher, if you'd tasted it, you'd have eaten it too. I was just faster."
)

MAX_CHARS = 199
MIN_CHARS = 1

# Words the excuse must lean on: the homework itself, the dog's alibi,
# and the teacher it is addressed to.
REQUIRED_WORDS = ("homework", "bacon", "teacher")
FORBIDDEN = ("\n", "\r", "\t")


class EntryError(ValueError):
    """Raised when the entry text violates the competition brief."""


def char_count(text: str) -> int:
    """Character count as the judge sees it: plain Unicode code points."""
    return len(text)


def is_single_line(text: str) -> bool:
    """True when the text contains no line breaks or control whitespace."""
    return not any(bad in text for bad in FORBIDDEN)


def has_dog_voice(text: str) -> bool:
    """The brief needs a DOG explaining: first-person voice plus the
    homework-eating culprit's favourite alibi word."""
    lowered = text.lower()
    return ("i " in lowered or lowered.startswith("i'")) and "bacon" in lowered


def mentions_homework_context(text: str) -> bool:
    """The excuse must name the homework and be addressed to the teacher."""
    lowered = text.lower()
    return "homework" in lowered and "teacher" in lowered


def validate(text: str) -> dict:
    """Validate every rule in the brief; fail loudly on the first breach.

    Returns a report dict of the checks that passed, so a caller can
    inspect exactly what was verified.
    """
    report = {
        "chars": char_count(text),
        "single_line": is_single_line(text),
        "dog_voice": has_dog_voice(text),
        "teacher_addressed": mentions_homework_context(text),
    }
    if not MIN_CHARS <= report["chars"] <= MAX_CHARS:
        raise EntryError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, "
            f"got {report['chars']}"
        )
    if not report["single_line"]:
        raise EntryError("entry must be exactly one line (no line breaks)")
    if text != text.strip():
        raise EntryError("entry must not have leading or trailing whitespace")
    if not report["dog_voice"]:
        raise EntryError("entry must be in the dog's first-person voice")
    if not report["teacher_addressed"]:
        raise EntryError("entry must address the teacher about the homework")
    for word in REQUIRED_WORDS:
        if word not in text.lower():
            raise EntryError(f"entry must contain the word {word!r}")
    return report


def resolve_output_dir() -> str:
    """Pick the output directory, preferring $MAKEFUN_OUTPUT.

    Falls back to a unique per-entry temp directory so parallel authors
    never overwrite each other's outputs.
    """
    env_dir = os.environ.get("MAKEFUN_OUTPUT")
    if env_dir:
        return env_dir
    unique = os.path.join(
        "/tmp", SLUG
    )
    return unique


def write_entry(text: str, out_dir: str) -> str:
    """Write the entry text to ``entry.txt`` and verify it by reading back."""
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise RuntimeError("verification failed: written file differs from entry")
    return out_path


def main(argv=None) -> int:
    report = validate(ENTRY_TEXT)
    out_dir = resolve_output_dir()
    out_path = write_entry(ENTRY_TEXT, out_dir)
    digest = hashlib.sha256(ENTRY_TEXT.encode("utf-8")).hexdigest()
    # The entry itself goes to stdout, exactly as submitted.
    print(ENTRY_TEXT)
    # Diagnostics go to stderr so stdout stays byte-identical every run.
    print(
        f"[ok] {report['chars']} chars, single line, "
        f"sha256={digest}, wrote {out_path}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
