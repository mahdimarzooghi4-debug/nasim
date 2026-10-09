"""Reproducible inventory for product-owner-authorized *synthetic source candidates*.

This does NOT approve a training/evaluation dataset. No Case/outbox/Provider
access, no operational identities, no model execution, and no auto-promotion.
The original candidate file's NOT_AUTHORIZED flags are deliberately preserved
until an independent record-level reviewer and a governed use-specific
admission can validate them.
"""

import json
from hashlib import sha1, sha256
from pathlib import Path
from typing import Any

SOURCE_REF = "faf33342497ec23f7c0969930ce808787e476be6"
SOURCE_DIR = "docs/ai/initial-content"
SOURCE_SPECS: tuple[tuple[str, str, int, str], ...] = (
    (
        "nasim_synthetic_behavior_candidates_v0_1.jsonl",
        "9495f38c53eeb30db2b07824fdcb2b70a9e3ff52",
        52,
        "NSIM-SYN-",
    ),
    (
        "nasim_synthetic_grounded_positive_candidates_v0_2.jsonl",
        "3f8af141213ad111a646be3ff6a2c4fad277511c",
        32,
        "NSIM-SYN-GP-",
    ),
    (
        "nasim_fictional_grounding_fixtures_v0_2.jsonl",
        "ed7797926c674687ead88fa4dcac6f20adb9bfc3",
        8,
        "NSIM-FIX-",
    ),
    (
        "nasim_authorial_quality_corrections_v0_3.jsonl",
        "753e6fb9ae603d84e5b97c6ff8201af079b4cb19",
        2,
        "NSIM-EDIT-",
    ),
)
_CANDIDATE_FILES = frozenset(spec[0] for spec in SOURCE_SPECS[:2])


class SeedIntegrityError(ValueError):
    """Synthetic source version, boundaries or declared provenance changed."""


def _read_source(
    project_root: Path, filename: str, pinned_blob: str, count: int, prefix: str
) -> list[dict[str, Any]]:
    # Only pinned, repository-owned files. No URL, symlink-following export,
    # untrusted arbitrary file name or raw clinical/case ingestion.
    path = project_root / SOURCE_DIR / filename
    if path.is_symlink() or not path.is_file():
        raise SeedIntegrityError("SEED_SOURCE_MISSING_OR_SYMLINK")
    raw = path.read_bytes()
    blob = sha1(b"blob " + str(len(raw)).encode("ascii") + b"\\0" + raw).hexdigest()
    if blob != pinned_blob:
        raise SeedIntegrityError("SEED_GIT_BLOB_ATTESTATION_FAILED")
    try:
        lines = raw.decode("utf-8").splitlines()
        records = [json.loads(line) for line in lines]
    except (UnicodeError, ValueError) as error:
        raise SeedIntegrityError("SEED_NOT_VALID_JSONL") from error
    if len(records) != count:
        raise SeedIntegrityError("SEED_SOURCE_RECORD_COUNT_CHANGED")
    for index, row in enumerate(records, 1):
        if not isinstance(row, dict) or row.get("id", row.get("patch_id")) != (
            prefix + f"{index:03d}"
        ):
            raise SeedIntegrityError("SEED_RECORD_ID_OR_ORDER_CHANGED")
        if filename in _CANDIDATE_FILES:
            if (
                row.get("synthetic_only") is not True
                or row.get("contains_real_personal_data") is not False
                or row.get("content_status") != "AUTHOR_DRAFT_UNREVIEWED"
                or row.get("training_permission") != "NOT_AUTHORIZED"
                or row.get("evaluation_permission") != "NOT_AUTHORIZED"
                or row.get("origin") != "AUTHOR_GENERATED_NOT_FIRST_PARTY_OPERATIONAL"
                or not isinstance(row.get("question"), str)
                or not row["question"].strip()
                or not isinstance(row.get("desired_answer"), str)
                or not row["desired_answer"].strip()
            ):
                raise SeedIntegrityError("SEED_CANDIDATE_GOVERNANCE_INVARIANT_FAILED")
        elif prefix == "NSIM-FIX-":
            if (
                row.get("author_generated") is not True
                or row.get("no_real_nasim_source") is not True
                or row.get("source_state") != "FICTIONAL_SCENARIO_ONLY"
                or row.get("content_status") != "AUTHOR_DRAFT_UNREVIEWED"
                or row.get("training_permission") != "NOT_AUTHORIZED"
                or row.get("evaluation_permission") != "NOT_AUTHORIZED"
            ):
                raise SeedIntegrityError("SEED_FICTIONAL_FIXTURE_INVARIANT_FAILED")
        elif prefix == "NSIM-EDIT-":
            if (
                row.get("original_retained") is not True
                or row.get("authorization") != "NOT_AUTHORIZED"
                or row.get("human_review") != "PENDING"
            ):
                raise SeedIntegrityError("SEED_AUTHORIAL_PATCH_NOT_PENDING")
    return records


def build_initial_synthetic_inventory(project_root: Path | None = None) -> dict[str, Any]:
    """Deterministic inventory, never an approved Dataset or automatic Training Run.

    Approval of an initial synthetic *source set* is distinct from a reviewer
    accepting each of the 84 samples, deciding its purpose partition, and
    admitting an actual versioned Dataset.
    """

    root = project_root if project_root is not None else Path(__file__).resolve().parents[4]
    groups = {
        filename: _read_source(root, filename, blob, count, prefix)
        for filename, blob, count, prefix in SOURCE_SPECS
    }
    behavior, positive, fixtures, corrections = [
        groups[spec[0]] for spec in SOURCE_SPECS
    ]
    fixture_ids = {row["id"] for row in fixtures}
    if any(
        row.get("source_fixture_id") not in fixture_ids
        or row.get("no_real_nasim_official_source") is not True
        or row.get("source_state") != "FICTIONAL_SCENARIO_ONLY"
        for row in positive
    ):
        raise SeedIntegrityError("SEED_POSITIVE_FIXTURE_REFERENCE_INVALID")
    if {p.get("target_record_id") for p in corrections} != {
        "NSIM-SYN-034",
        "NSIM-SYN-GP-022",
    }:
        raise SeedIntegrityError("SEED_EDIT_TARGETS_CHANGED")

    candidate_rows: list[dict[str, str]] = []
    for file, records in ((SOURCE_SPECS[0][0], behavior), (SOURCE_SPECS[1][0], positive)):
        for row in records:
            candidate_rows.append(
                {
                    "record_id": row["id"],
                    "source_file": file,
                    "record_sha256": sha256(
                        json.dumps(row, sort_keys=True, ensure_ascii=True, separators=(",", ":"))
                        .encode("utf-8")
                    ).hexdigest(),
                }
            )
    if len(candidate_rows) != 84 or len({r["record_id"] for r in candidate_rows}) != 84:
        raise SeedIntegrityError("SEED_CANDIDATE_DUPLICATE_OR_MISSING_ID")

    inventory: dict[str, Any] = {
        "schema": "nasim.initial-synthetic-seed-inventory.v1",
        "source_commit": SOURCE_REF,
        "source_git_blobs": {filename: blob for filename, blob, _, _ in SOURCE_SPECS},
        "source_authorization_decision": "D-0154",
        "source_authorization_scope": "SYNTHETIC_ONLY",
        "record_count": len(candidate_rows),
        "fictional_fixture_count": len(fixtures),
        "pending_authorial_patch_count": len(corrections),
        "candidate_records": candidate_rows,
        "quality_review": "PENDING_INDEPENDENT_PER_RECORD",
        "training_evaluation_partition": "UNASSIGNED",
        "dataset_status": "SOURCE_ATTESTED_NOT_APPROVED",
        "production_training_enabled": False,
    }
    inventory["inventory_sha256"] = sha256(
        json.dumps(inventory, sort_keys=True, ensure_ascii=True, separators=(",", ":"))
        .encode("utf-8")
    ).hexdigest()
    return inventory
