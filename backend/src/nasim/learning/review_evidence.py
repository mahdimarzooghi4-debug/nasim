"""Offline, fail-closed reconciliation of REAL submitted human review evidence.

Product Owner attests that Nasim Operations Manager personally reviewed all
84 synthetic initial examples. This module does NOT forge item-level outcomes,
verify a reviewer's identity from their asserted role, or approve a Dataset.
It checks that separately supplied review metadata covers exact pinned records.

Not imported into any API, runtime, Dataset Builder or model training service.
"""

import json
import re
from collections import Counter
from datetime import datetime
from hashlib import sha256
from pathlib import Path
from typing import Any

from nasim.learning.synthetic_seed import (
    SOURCE_SPECS,
    SeedIntegrityError,
    _read_source,
    build_initial_synthetic_inventory,
)

_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
_REFERENCE = re.compile(r"[A-Za-z0-9][A-Za-z0-9./:_#?&=%+@-]{1,299}\Z")
_OUTCOMES = frozenset({"CONTENT_ACCEPTED", "REWRITE_REQUIRED", "CONTENT_REJECTED"})
_PATCH_OUTCOMES = frozenset({"ACCEPT_PROPOSAL", "REJECT_PROPOSAL", "REWORK_PROPOSAL"})
_REVIEW_SCHEMA = "nasim.synthetic-human-review-evidence.v1"
_REPORT_SCHEMA = "nasim.synthetic-human-review-evidence-report.v1"


class ReviewReconciliationError(ValueError):
    """Unverifiable input format/coverage, NOT a statement that review did not occur."""


def _required(mapping: dict[str, Any], key: str) -> str:
    value = mapping.get(key)
    if type(value) is not str or not value or len(value) > 300:
        raise ReviewReconciliationError("REVIEW_REQUIRED_FIELD_INVALID")
    return value


def _reference(mapping: dict[str, Any], key: str) -> str:
    value = _required(mapping, key)
    if _REFERENCE.fullmatch(value) is None:
        # Only opaque safe reference metadata here; no credentials, free text,
        # reviewer names or elder data in GitHub / CLI output.
        raise ReviewReconciliationError("REVIEW_EVIDENCE_REFERENCE_INVALID")
    return value


def _reviewed_at(mapping: dict[str, Any]) -> str:
    value = _required(mapping, "reviewed_at")
    try:
        timestamp = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise ReviewReconciliationError("REVIEW_TIMESTAMP_INVALID") from error
    if timestamp.utcoffset() is None:
        raise ReviewReconciliationError("REVIEW_TIMESTAMP_NO_TIMEZONE")
    return value


def _canonical_digest(value: Any) -> str:
    return sha256(
        json.dumps(value, sort_keys=True, ensure_ascii=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def _entries(
    raw: Any,
    expected: dict[str, str],
    *,
    is_patch: bool,
) -> dict[str, dict[str, str]]:
    if type(raw) is not list:
        raise ReviewReconciliationError("REVIEW_ITEMS_REQUIRED")
    result: dict[str, dict[str, str]] = {}
    for value in raw:
        if type(value) is not dict or set(value) != {
            "record_id",
            "record_sha256",
            "outcome",
            "evidence_ref",
            "reviewed_at",
        }:
            raise ReviewReconciliationError("REVIEW_ITEM_SCHEMA_INVALID")
        item_id = _required(value, "record_id")
        if item_id not in expected:
            raise ReviewReconciliationError("REVIEW_UNRECOGNIZED_SOURCE_ID")
        if item_id in result:
            raise ReviewReconciliationError("REVIEW_DUPLICATE_SOURCE_ID")
        digest = _required(value, "record_sha256")
        if _SHA256.fullmatch(digest) is None or expected[item_id] != digest:
            raise ReviewReconciliationError("REVIEW_STALE_SOURCE_DIGEST")
        outcome = _required(value, "outcome")
        allowed = _PATCH_OUTCOMES if is_patch else _OUTCOMES
        if outcome not in allowed:
            raise ReviewReconciliationError("REVIEW_OUTCOME_INVALID")
        _reference(value, "evidence_ref")
        _reviewed_at(value)
        result[item_id] = value
    if not is_patch and set(result) != set(expected):
        raise ReviewReconciliationError("REVIEW_84_ITEM_COVERAGE_INCOMPLETE")
    return result


def reconcile_initial_review_evidence(
    evidence: dict[str, Any], project_root: Path | None = None
) -> dict[str, Any]:
    """Validate structure, exact source lineage and complete record coverage.

    Caller-controlled metadata can never authenticate an organizational actor
    or constitute legal/purpose approval. No approved record is exported to a
    Dataset; this report remains non-authoritative even with 84 ACCEPT values.
    """
    if type(evidence) is not dict or set(evidence) != {
        "schema",
        "source_commit",
        "inventory_sha256",
        "reviewer_organizational_role",
        "review_batch_evidence_ref",
        "records",
        "patches",
    }:
        raise ReviewReconciliationError("REVIEW_BUNDLE_SCHEMA_INVALID")
    root = project_root if project_root is not None else Path(__file__).resolve().parents[4]
    inventory = build_initial_synthetic_inventory(root)
    if evidence["schema"] != _REVIEW_SCHEMA:
        raise ReviewReconciliationError("REVIEW_SCHEMA_VERSION_UNSUPPORTED")
    if evidence["source_commit"] != inventory["source_commit"]:
        raise ReviewReconciliationError("REVIEW_SOURCE_COMMIT_STALE")
    if evidence["inventory_sha256"] != inventory["inventory_sha256"]:
        raise ReviewReconciliationError("REVIEW_SOURCE_INVENTORY_STALE")
    if evidence["reviewer_organizational_role"] != "NASIM_OPERATIONS_MANAGER":
        raise ReviewReconciliationError("REVIEW_ROLE_MISMATCH")
    _reference(evidence, "review_batch_evidence_ref")

    sources = {
        entry["record_id"]: entry["record_sha256"] for entry in inventory["candidate_records"]
    }
    decisions = _entries(evidence["records"], sources, is_patch=False)
    patch_file, patch_blob, patch_count, patch_prefix = SOURCE_SPECS[3]
    try:
        patches = _read_source(root, patch_file, patch_blob, patch_count, patch_prefix)
    except SeedIntegrityError as error:
        raise ReviewReconciliationError("REVIEW_PATCH_SOURCE_STALE") from error
    source_patches = {patch["patch_id"]: _canonical_digest(patch) for patch in patches}
    patch_decisions = _entries(evidence["patches"], source_patches, is_patch=True)
    # A decision for a proposed edit is not permission to change original
    # reviewed sample, or to apply a changed answer in model training.
    counts = Counter(row["outcome"] for row in decisions.values())
    patch_counts = Counter(row["outcome"] for row in patch_decisions.values())

    # Digest is useful for external audit matching only; it is not a signature
    # or a proof of review authenticity. No raw evidence or personal data out.
    canonical_items = [decisions[identifier] for identifier in sorted(decisions)]
    canonical_patches = [patch_decisions[i] for i in sorted(patch_decisions)]
    return {
        "schema": _REPORT_SCHEMA,
        "source_commit": inventory["source_commit"],
        "inventory_sha256": inventory["inventory_sha256"],
        "review_authority_decision": "D-0161",
        "review_completion_owner_attestation": "D-0160",
        "record_coverage": len(decisions),
        "record_outcomes": {key: counts[key] for key in sorted(_OUTCOMES)},
        "patches_with_evidence": len(patch_decisions),
        "patch_outcomes": {key: patch_counts[key] for key in sorted(_PATCH_OUTCOMES)},
        "evidence_metadata_sha256": _canonical_digest(
            {
                "source_commit": inventory["source_commit"],
                "records": canonical_items,
                "patches": canonical_patches,
                "batch_ref": evidence["review_batch_evidence_ref"],
            }
        ),
        "evidence_status": "FORMAT_AND_COVERAGE_CHECKED_EXTERNAL_AUTHENTICITY_UNVERIFIED",
        "dataset_status": "NOT_APPROVED",
        "training_evaluation_partition": "UNASSIGNED",
        "automatic_training_enabled": False,
        "production_model_promotion": False,
    }
