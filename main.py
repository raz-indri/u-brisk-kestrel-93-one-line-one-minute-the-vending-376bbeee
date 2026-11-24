"""Vending machine pickup line.

The joke: the machine itself is flirting. Its coil — the spiral that
pushes snacks forward — is "stuck on you", and the punch is a wordplay
on exact change: no coins needed, only exact feelings. The button code
B7 keeps it in the machine's own world. Machine voice, short and warm.
"""

import os
from pathlib import Path

LINE = (
    "Hey, cutie — I'm the machine by the door, and my coil's been "
    "stuck on you all day. Press B7: no exact change, just exact feelings."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
