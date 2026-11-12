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
    shutil.copyfile(src, dst)
    print(f"wrote {dst}", file=sys.stderr)


if __name__ == "__main__":
    main()
