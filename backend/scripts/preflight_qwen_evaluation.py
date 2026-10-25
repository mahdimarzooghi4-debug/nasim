#!/usr/bin/env python3
"""Fail-closed preflight for a Qwen single-model evaluation package.

This checks recorded prerequisites only. It does not validate the truth of
external approvals, load model weights, execute inference, or authorize a run.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

MODEL_REPOSITORY = "Qwen/Qwen3.5-9B"
MODEL_REVISION = "c202236235762e1c871ad0ccb60c8ee5ba337b9a"


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("manifest root must be a JSON object")
    return value


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    seen: set[str] = set()
    with path.open(encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, start=1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"invalid JSONL at line {line_number}: {exc.msg}") from exc
            if not isinstance(record, dict):
                raise ValueError(f"record at line {line_number} must be a JSON object")
            record_id = record.get("id")
            if not isinstance(record_id, str) or not record_id.strip():
                raise ValueError(f"record at line {line_number} has no non-empty id")
            if record_id in seen:
                raise ValueError(f"duplicate evaluation id at line {line_number}: {record_id}")
            seen.add(record_id)
            records.append(record)
    return records


def has_evidence(value: Any, status: str, reference_key: str = "reference") -> bool:
    return (
        isinstance(value, dict)
        and value.get("status") == status
        and isinstance(value.get(reference_key), str)
        and bool(value[reference_key].strip())
    )


def check_manifest(manifest: dict[str, Any], dataset_path: Path) -> list[str]:
    failures: list[str] = []
    model = manifest.get("model")
    if not isinstance(model, dict):
        model = {}
    if model.get("repository") != MODEL_REPOSITORY:
        failures.append(f"model.repository must be {MODEL_REPOSITORY}")
    if model.get("revision") != MODEL_REVISION:
        failures.append("model.revision must match D-0179's pinned revision")

    evaluation = manifest.get("evaluation_set")
    if not isinstance(evaluation, dict):
        evaluation = {}
    if evaluation.get("status") != "APPROVED_FOR_EVALUATION":
        failures.append("evaluation_set.status must be APPROVED_FOR_EVALUATION")

    authorization = evaluation.get("authorization")
    if not has_evidence(authorization, "AUTHORIZED"):
        failures.append("evaluation authorization and its reference are required")
    elif not isinstance(authorization.get("approved_at"), str) or not authorization["approved_at"].strip():
        failures.append("evaluation authorization approved_at is required")

    if not has_evidence(evaluation.get("rights_evidence"), "CLEARED"):
        failures.append("cleared source-rights evidence and its reference are required")
    if not has_evidence(evaluation.get("content_review"), "APPROVED"):
        failures.append("approved human content review and its reference are required")
    if not has_evidence(evaluation.get("split_lineage"), "VERIFIED"):
        failures.append("verified held-out split lineage and its reference are required")

    expected_digest = evaluation.get("sha256")
    actual_digest = hashlib.sha256(dataset_path.read_bytes()).hexdigest()
    if not isinstance(expected_digest, str) or expected_digest.lower() != actual_digest:
        failures.append("evaluation_set.sha256 does not match the exact JSONL file")

    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--dataset", required=True, type=Path)
    args = parser.parse_args()

    try:
        manifest = read_json(args.manifest)
        records = read_jsonl(args.dataset)
        if not records:
            raise ValueError("evaluation dataset is empty")
        failures = check_manifest(manifest, args.dataset)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        print(f"Evaluation preflight failed: {exc}", file=sys.stderr)
        return 2

    if failures:
        for failure in failures:
            print(f"BLOCKED: {failure}", file=sys.stderr)
        return 2

    print(
        f"PRECHECK PASSED for {len(records)} evaluation record(s) and "
        f"{MODEL_REPOSITORY}@{MODEL_REVISION}."
    )
    print("No model was loaded and no evaluation run was executed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
