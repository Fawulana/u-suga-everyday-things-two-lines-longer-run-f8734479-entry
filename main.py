# SPDX-License-Identifier: MIT
"""Everyday Things, Two Lines — entry program.

Writes exactly two lines to /output/entry.txt (UTF-8, deterministic,
no network, stdlib only): a two-line explanation of a toaster for a
10-year-old, built on one concrete analogy, with an honest second line
about what the analogy maps and what it leaves out.

Why this analogy: a lift is something a 10-year-old has stood in, and
the toaster's real motion really is down, wait, up — so the picture
carries the mechanism, not just the look.
"""

import os

LINE_1 = (
    "A toaster is a tiny elevator for bread: it carries your slice down "
    "into a little box of glowing red wires and lifts it back up brown "
    "and crisp."
)

LINE_2 = (
    "It maps the ride down, the wait in the heat, and the pop back up, "
    "but it leaves out that the heat comes from electric wires glowing "
    "red-hot and that the bread never travels anywhere — it just sits "
    "still while the heat browns it."
)


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    text = LINE_1 + "\n" + LINE_2 + "\n"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
