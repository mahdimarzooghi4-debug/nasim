"""Print only offline synthetic dataset content-addressed metadata, no Q/A prose."""

import json

from nasim.learning.synthetic_dataset import build_initial_synthetic_dataset_package

if __name__ == "__main__":
    print(
        json.dumps(
            build_initial_synthetic_dataset_package()["manifest"],
            ensure_ascii=False,
            indent=2,
        )
    )
