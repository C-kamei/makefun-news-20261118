#!/usr/bin/env python3
"""news-image-20261118 entry (Python 3.13, standard library only).

The entry image is the entry.png beside this file: a newspaper front page
summing up the world news of Wednesday 18 November 2026, drawn with PIL
from wire reports of that day (lead: U.S. sinks five Iranian tankers;
summit, measles, Israel, COP31, Italy). The hero photo is AI-generated and
labelled ILLUSTRATION in the image. This program copies it byte for byte to
/output/entry.png, so both grader runs write identical bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil
from pathlib import Path

ENTRY = Path(__file__).with_name("entry.png")


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(ENTRY, dest)
    # Fail loudly rather than submit a truncated copy.
    assert dest.stat().st_size == ENTRY.stat().st_size


if __name__ == "__main__":
    main()
