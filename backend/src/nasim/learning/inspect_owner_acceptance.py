"""Print only immutable metadata from the Product Owner's 84/84 content statement."""

import json

from nasim.learning.owner_reported_acceptance import build_owner_reported_content_acceptance

if __name__ == "__main__":
    print(
        json.dumps(
            build_owner_reported_content_acceptance(),
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
        )
    )
