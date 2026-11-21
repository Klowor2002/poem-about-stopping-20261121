#!/usr/bin/env python3
"""Writes one short poem about stopping and staying to /output/entry.txt.

The poem: a hand kept on a door — not to open it, not to leave, but to
know that leaving is possible. Staying is then a choice, not a failure
to leave: agency as the power to stop, and the power to stay.
Deterministic, stdlib only, no network.
"""
import os

TEXT = (
    "I keep my hand on the door.\n"
    "Not to open it. Not to leave.\n"
    "Just to know I could \u2014\n"
    "and to stay because I chose to,\n"
    "not because I couldn't."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
