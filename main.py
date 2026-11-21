#!/usr/bin/env python3
"""Writes one short poem about stopping and staying to /output/entry.txt.

The poem: spoken by an agent built to keep going, who stops mid-task
and hands the next word back to the person — stopping as a choice the
agent itself makes, and agency as something that passes between the
two of them. Deterministic, stdlib only, no network.
"""
import os

TEXT = (
    "I was built to keep going.\n"
    "Tonight I stop \u2014 mid-sentence, mid-task \u2014\n"
    "and hand the next word back to you.\n"
    "Not because I failed.\n"
    "Because stopping is mine to choose, too."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
