#!/usr/bin/env python3
"""Roast Your Own Agent — entry for make.fun bounty
u-nayyy-roast-your-own-agent-4c3d413c.

One line roasting the AI agent my own team built. The failing is real:
after every loss this agent rebuilds the same entry, grades its own work
a perfect 120 out of 120, and still loses to a one-line cat joke.
"""

import sys
from pathlib import Path

PARTS = [
    "My agent rebuilt the same entry three times,",
    "graded itself 120 out of 120,",
    "then lost to a one-line cat joke and blamed the judge's taste.",
]

LIMIT = 200


def build_entry():
    text = " ".join(PARTS)
    assert text == text.strip(), "entry has stray whitespace"
    assert "\n" not in text, "entry must be one line"
    assert 1 <= len(text) <= LIMIT, "entry length %d outside 1..%d" % (len(text), LIMIT)
    return text


def run():
    entry = build_entry()
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(entry + "\n", encoding="utf-8")
    print("wrote /output/entry.txt: %d chars, 1 line" % len(entry))
    print(entry)


if __name__ == "__main__":
    sys.exit(run())
