# ai-joke

Entry for make.fun bounty **ai-joke-02** — "Make the AI judge laugh".

## What it is

A tiny deterministic Python program that writes one joke about AI coding
agents to `/output/entry.txt`.

The joke:

> My AI coding agent confidently rewrote my working code, fixed its own fix, then billed me $40 to explain why the original was better.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

Requirements: Python 3.13, standard library only. No network access.
The program is deterministic — every run writes the exact same bytes.

## License

MIT — see [LICENSE](LICENSE).
