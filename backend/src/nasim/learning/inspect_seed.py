"""Offline diagnostic only. Prints source-ID/digest inventory; never accesses a database."""

import json

from nasim.learning.synthetic_seed import build_initial_synthetic_inventory

if __name__ == "__main__":
    print(json.dumps(build_initial_synthetic_inventory(), ensure_ascii=False, indent=2))
