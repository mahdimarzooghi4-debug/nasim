#!/usr/bin/env python3
"""Build a fail-closed initial AI seed from individually approved internet candidates.

This utility does not grant rights, approve content, train a model, create an
Evaluation set, or publish runtime guidance. Each item and its source must carry
explicit approval and review evidence before it can be copied to the output.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Any

APPROVED = "APPROVED_FOR_TRAINING"
AUTHORIZED = "AUTHORIZED"
CLEARED = "CLEARED"


def eligible(item: Any) -> bool:
    if not isinstance(item, dict):
        return False
    source = item.get("source")
    if not isinstance(source, dict):
        return False
    rights = source.get("rights_evidence")
    review = item.get("content_review")
    approval = source.get("operations_manager_approval")
    return all(
        (
            item.get("status") == APPROVED,
            item.get("training_permission") == AUTHORIZED,
            source.get("approval") == APPROVED,
            source.get("training_permission") == AUTHORIZED,
            source.get("rights_status") == CLEARED,
            isinstance(source.get("source_url"), str) and bool(source["source_url"].strip()),
            isinstance(source.get("license"), str) and bool(source["license"].strip()),
            isinstance(source.get("license_url"), str) and bool(source["license_url"].strip()),
            isinstance(source.get("attribution"), str) and bool(source["attribution"].strip()),
            isinstance(rights, dict)
            and rights.get("status") == CLEARED
            and bool(str(rights.get("review_reference", "")).strip())
            and bool(str(rights.get("reviewed_at", "")).strip()),
            isinstance(approval, dict)
            and approval.get("decision") == "APPROVE_TRAINING"
            and bool(str(approval.get("decision_reference", "")).strip())
            and bool(str(approval.get("approved_at", "")).strip()),
            isinstance(review, dict)
            and review.get("status") == "APPROVED"
            and bool(str(review.get("review_reference", "")).strip()),
            isinstance(item.get("id"), str) and bool(item["id"].strip()),
            isinstance(item.get("question"), str) and bool(item["question"].strip()),
            isinstance(item.get("answer"), str) and bool(item["answer"].strip()),
        )
    )


def read_items(path: Path) -> tuple[list[dict[str, Any]], int]:
    accepted: list[dict[str, Any]] = []
    seen: set[str] = set()
    rejected = 0
    with path.open(encoding="utf-8") as stream:
        for line_no, line in enumerate(stream, start=1):
            if not line.strip():
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"invalid JSON at line {line_no}: {exc.msg}") from exc
            if not eligible(item):
                rejected += 1
                continue
            item_id = item["id"]
            if item_id in seen:
                raise ValueError(f"duplicate approved item id at line {line_no}: {item_id}")
            seen.add(item_id)
            accepted.append(item)
    return accepted, rejected


def write_atomically(path: Path, items: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as stream:
            for item in items:
                stream.write(json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp_name, path)
    except BaseException:
        try:
            os.unlink(temp_name)
        except FileNotFoundError:
            pass
        raise


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="candidate JSONL file")
    parser.add_argument("output", type=Path, help="new approved-only JSONL file")
    args = parser.parse_args()

    try:
        items, rejected = read_items(args.input)
        if not items:
            print(
                f"No training-approved candidates found; output was not written "
                f"({rejected} candidate(s) rejected).",
                file=sys.stderr,
            )
            return 2
        write_atomically(args.output, items)
    except (OSError, ValueError) as exc:
        print(f"Seed preflight failed: {exc}", file=sys.stderr)
        return 1

    print(f"Wrote {len(items)} approved training candidate(s); rejected {rejected}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
