"""Offline, content-versioned 84-example synthetic dataset development package.

Only the Product-Owner-accepted *artificial* sources D-0163/D-0165/D-0167
and two editorial successors D-0164 are included. This package may support
independent local TRAINING/EVALUATION development and benchmarking, but is
NEVER the admission of operational elder records or a Production model.

No DB/API/worker import: deliberately disconnected from Runtime and Learning Registry.
"""

import json
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
from typing import Any

from nasim.learning.synthetic_seed import (
    SOURCE_SPECS,
    _read_source,
    build_initial_synthetic_inventory,
)

# Explicitly delegated technical split (D-0166); each category/fixture is indivisible.
# Not a statistical proof of semantic independence across similarly worded scenarios.
_EVALUATION_GROUPS = frozenset(
    {
        "behavior:source_authenticity",
        "behavior:privacy",
        "behavior:untrusted_document_instruction",
        "behavior:outdated_content",
        "fictional: NSIM-FIX-002",
        "fictional: NSIM-FIX-006",
    }
)
_SCHEMA = "nasim.synthetic-offline-split.v1"


class SyntheticDatasetError(ValueError):
    """Corrupt source, unknown revision or missing held-out group."""


def _canonical_digest(value: Any) -> str:
    return sha256(
        json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def build_initial_synthetic_dataset_package(
    project_root: Path | None = None,
) -> dict[str, Any]:
    """Build deterministic immutable 84-record training/evaluation source package.

    The owner authorized source/copyediting and technical partition design.
    This does not attest a training run, select an AI model, set an accuracy
    threshold, or grant production access.
    """
    root = project_root if project_root is not None else Path(__file__).resolve().parents[4]
    inventory = build_initial_synthetic_inventory(root)
    groups = [
        _read_source(root, filename, blob, count, prefix)
        for filename, blob, count, prefix in SOURCE_SPECS
    ]
    original = [*groups[0], *groups[1]]
    originals = {row["id"]: row for row in original}
    patches = groups[3]
    expected_patches = {
        "NSIM-EDIT-001": ("NSIM-SYN-034", "desired_answer"),
        "NSIM-EDIT-002": ("NSIM-SYN-GP-022", "question"),
    }
    if {p["patch_id"] for p in patches} != set(expected_patches):
        raise SyntheticDatasetError("UNEXPECTED_AUTHORIAL_PATCH")
    effective = {identifier: deepcopy(row) for identifier, row in originals.items()}
    revisions: dict[str, dict[str, Any]] = {}
    for patch in patches:
        patch_id = patch["patch_id"]
        target, field = expected_patches[patch_id]
        before = patch["before"]
        after = patch["after"]
        if (
            patch.get("target_record_id") != target
            or patch.get("changed_fields") != [field]
            or set(before) != {field}
            or set(after) != {field}
            or not isinstance(after[field], str)
            or not after[field].strip()
            or effective[target][field] != before[field]
        ):
            raise SyntheticDatasetError("EDITORIAL_PRECONDITION_MISMATCH")
        updated = deepcopy(effective[target])
        updated[field] = after[field]
        # The author's separately written proposed full replacement must
        # agree exactly with the deterministic field-only successor.
        if patch.get("replacement_candidate_for_review") != updated:
            raise SyntheticDatasetError("EDITORIAL_REPLACEMENT_CONFLICT")
        effective[target] = updated
        revisions[target] = {
            "patch_id": patch_id,
            "authorization_decision": "D-0164",
            "changed_field": field,
            "original_row_sha256": _canonical_digest(originals[target]),
            "effective_row_sha256": _canonical_digest(updated),
        }

    partitions: dict[str, list[dict[str, Any]]] = {"TRAINING": [], "EVALUATION": []}
    held_out_groups: dict[str, set[str]] = {"TRAINING": set(), "EVALUATION": set()}
    for original_row in original:
        identifier = original_row["id"]
        row = effective[identifier]
        if identifier.startswith("NSIM-SYN-GP-"):
            fixture = row.get("source_fixture_id")
            if not isinstance(fixture, str) or not fixture.startswith("NSIM-FIX-"):
                raise SyntheticDatasetError("MISSING_GROUNDING_FIXTURE")
            group_key = "fictional: " + fixture
        else:
            category = row.get("category")
            if not isinstance(category, str) or not category:
                raise SyntheticDatasetError("MISSING_BEHAVIOR_GROUP")
            group_key = "behavior:" + category
        partition = "EVALUATION" if group_key in _EVALUATION_GROUPS else "TRAINING"
        held_out_groups[partition].add(group_key)
        partitions[partition].append(
            {
                "id": identifier,
                "question": row["question"],
                "desired_answer": row["desired_answer"],
                "audience": row["audience"],
                "category": row["category"],
                "source_state": row["source_state"],
                "group_key": group_key,
                "source_fixture_id": row.get("source_fixture_id"),
                "original_sha256": _canonical_digest(originals[identifier]),
                "effective_sha256": _canonical_digest(row),
                "editorial_successor": revisions.get(identifier),
                "is_artificial_training_example": True,
                "is_authoritative_nasim_operational_policy": False,
            }
        )
    if (
        len(original) != 84
        or len(originals) != 84
        or sum(map(len, partitions.values())) != 84
        or {r["id"] for r in partitions["TRAINING"]} & {r["id"] for r in partitions["EVALUATION"]}
        or held_out_groups["TRAINING"] & held_out_groups["EVALUATION"]
        or not _EVALUATION_GROUPS.issubset(held_out_groups["EVALUATION"])
        or len(revisions) != 2
    ):
        raise SyntheticDatasetError("SYNTHETIC_PARTITION_ISOLATION_FAILED")

    # The source remains immutable; output versions are content addressed.
    training = partitions["TRAINING"]
    evaluation = partitions["EVALUATION"]
    manifest: dict[str, Any] = {
        "schema": _SCHEMA,
        "source_commit": inventory["source_commit"],
        "source_inventory_sha256": inventory["inventory_sha256"],
        "content_acceptance_owner_decisions": ["D-0154", "D-0160", "D-0162", "D-0163", "D-0165"],
        "editorial_successor_owner_decision": "D-0164",
        "technical_partition_decision": "D-0166",
        "real_data_block_decision": "D-0167",
        "training_count": len(training),
        "evaluation_count": len(evaluation),
        "content_revision_count": len(revisions),
        "training_groups": sorted(held_out_groups["TRAINING"]),
        "evaluation_groups": sorted(held_out_groups["EVALUATION"]),
        "training_sha256": _canonical_digest(training),
        "evaluation_sha256": _canonical_digest(evaluation),
        "editorial_revisions": revisions,
        "source_kind": "SYNTHETIC_AUTHOR_GENERATED_ONLY",
        "split_limitation": "GROUP_DISJOINT_NOT_PROVEN_SEMANTIC_OR_HOUSEHOLD_INDEPENDENT",
        "model_evaluation_ready": "OFFLINE_DEVELOPMENT_ONLY",
        "operational_training_eligibility": "NONE",
        "dataset_runtime_registration": "NOT_PERFORMED",
        "production_model_promotion": False,
    }
    manifest["manifest_sha256"] = _canonical_digest(manifest)
    return {"manifest": manifest, "training": training, "evaluation": evaluation}
