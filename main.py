"""news-summary-01 entry (Python 3.13, standard library only).

Writes the summary in summary.txt (beside this file) to
/output/entry.txt, or $MAKEFUN_OUTPUT_DIR/entry.txt when set.
Deterministic: the same bytes every run.
"""

import os
import shutil
import sys


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "summary.txt")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    # Validate the summary against the kit's gate before writing:
    # 1-2000 characters, valid UTF-8, and at least one non-whitespace
    # character. Fail loudly instead of shipping an invalid entry.
    with open(src, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    if not (1 <= len(text) <= 2000):
        raise SystemExit(f"summary is {len(text)} chars, must be 1-2000")
    if not text.strip():
        raise SystemExit("summary is blank")
    shutil.copyfile(src, dst)
    # Confirm the output is exactly what was validated.
    with open(dst, "rb") as f:
        if f.read() != raw:
            raise SystemExit("output does not match validated summary")
    print(f"wrote {dst} ({len(text)} chars)", file=sys.stderr)


if __name__ == "__main__":
    main()
