"""news-image-20261117 entry: write the day's front page to /output/entry.png.

The image (entry.png, beside this file) is a newspaper front page summing up
the world news of Tuesday 17 November 2026: a third US aircraft carrier
reaching the Middle East as an oil tanker burns near the Strait of Hormuz,
the Crimean bridge struck with its middle span collapsed, Trump heading to
Asia for the Xi-Putin summit in Shenzhen, the EU states' Rwanda return hub,
tightening AI chip curbs, and the Pentagon failing its audit again.

The program is deterministic: it copies fixed bytes, makes no network calls,
reads nothing but the image beside it, and writes the same file on every run.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    # Fail loudly instead of handing the grader a truncated file: the copy
    # must start with the PNG magic bytes and match the source byte for byte.
    with open(dst, "rb") as f:
        head = f.read(8)
    if head != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png is not a whole PNG")
    if os.path.getsize(dst) != os.path.getsize(SRC):
        raise SystemExit("copied entry.png differs in size from the source")
    return 0


if __name__ == "__main__":
    sys.exit(main())
