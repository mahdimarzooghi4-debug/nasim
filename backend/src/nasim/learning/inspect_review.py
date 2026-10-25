"""Offline validator of human-supplied review evidence metadata; no AI training.

Usage from backend/: uv run --locked python -m nasim.learning.inspect_review FILE
The file must originate from the external authorized reviewer evidence workflow;
this CLI itself cannot authenticate the asserted reviewer or signature.
"""

import json
import sys
from pathlib import Path

from nasim.learning.review_evidence import reconcile_initial_review_evidence

MAX_REVIEW_BYTES = 512 * 1024


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python -m nasim.learning.inspect_review FILE", file=sys.stderr)
        return 2
    source = Path(sys.argv[1])
    if source.is_symlink() or not source.is_file() or source.stat().st_size > MAX_REVIEW_BYTES:
        print("invalid or oversized review metadata file", file=sys.stderr)
        return 2
    try:
        evidence = json.loads(source.read_text(encoding="utf-8"))
        result = reconcile_initial_review_evidence(evidence)
    except (OSError, UnicodeError, ValueError) as error:
        print(f"review evidence rejected: {type(error).__name__}", file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
