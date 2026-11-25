"""Your Computer Just Needs to Agree: one-line tech support reply.

The entry is a single line from a hopeless tech support agent to a
desperate customer. The setup is cheerful agent speak, good news and a
ticket closed as resolved, and the punchline is that the computer still
has to agree before the deadline. The program writes exactly that one
line, and nothing else, to /output/entry.txt.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

LINE = (
    "Good news, I have closed your ticket as resolved, now we just "
    "need your computer to agree with me before your deadline."
)


def main():
    if LINE.strip() != LINE:
        raise ValueError("line has stray leading or trailing whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    if not 1 <= len(LINE) <= 199:
        raise ValueError("line must be 1 to 199 characters, got %d" % len(LINE))
    if len(LINE.encode("utf-8")) != len(LINE):
        raise ValueError("line must be plain ASCII text")
    if "  " in LINE:
        raise ValueError("line has a double space")
    if "\t" in LINE:
        raise ValueError("line has a tab")
    if not LINE.endswith(".") or LINE.count(".") != 1:
        raise ValueError("line must be exactly one sentence")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("entry.txt mismatch, got %r" % written)
    if written.count("\n") != 0 or written.count("\r") != 0:
        raise ValueError("entry.txt must not contain a newline")


if __name__ == "__main__":
    main()
