#!/usr/bin/env python3
"""ai-joke-02 entry: writes one joke about AI coding agents to /output/entry.txt.

The joke is 133 UTF-8 characters, inside the competition's 1-280 range.
Deterministic: the joke is hardcoded, no randomness, no network, no time,
no environment input. Both runs write the exact same bytes.
"""

from pathlib import Path

JOKE = "My AI coding agent confidently rewrote my working code, fixed its own fix, then billed me $40 to explain why the original was better."
# 133 UTF-8 chars: inside the competition's 1-280 char range for the joke.

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
