"""Synthetic-only simulated review evidence; NEVER human attestation test fixtures."""

from copy import deepcopy
from pathlib import Path

import pytest

from nasim.learning.review_evidence import (
    ReviewReconciliationError,
    reconcile_initial_review_evidence,
)
from nasim.learning.synthetic_seed import (
    SOURCE_DIR,
    SOURCE_SPECS,
    build_initial_synthetic_inventory,
)


def synthetic_evidence_for_tests() -> dict:
    inventory = build_initial_synthetic_inventory()
    return {
        "schema": "nasim.synthetic-human-review-evidence.v1",
        "source_commit": inventory["source_commit"],
        "inventory_sha256": inventory["inventory_sha256"],
        "reviewer_organizational_role": "NASIM_OPERATIONS_MANAGER",
        "review_batch_evidence_ref": "TEST-ONLY-SYNTHETIC-REF",
        "records": [
            {
                "record_id": row["record_id"],
                "record_sha256": row["record_sha256"],
                "outcome": "CONTENT_ACCEPTED",
                "evidence_ref": "TEST-ONLY-EVIDENCE",
                "reviewed_at": "2026-10-09T10:00:00+04:00",
            }
            for row in inventory["candidate_records"]
        ],
        "patches": [],
    }


def test_reconciliation_is_only_metadata_not_an_approval():
    evidence = synthetic_evidence_for_tests()
    report = reconcile_initial_review_evidence(evidence)
    assert report == reconcile_initial_review_evidence(deepcopy(evidence))
    assert report["record_coverage"] == 84
    assert report["record_outcomes"]["CONTENT_ACCEPTED"] == 84
    assert report["patches_with_evidence"] == 0
    assert report["evidence_status"] == (
        "FORMAT_AND_COVERAGE_CHECKED_EXTERNAL_AUTHENTICITY_UNVERIFIED"
    )
    assert report["dataset_status"] == "NOT_APPROVED"
    assert report["automatic_training_enabled"] is False
    assert report["training_evaluation_partition"] == "UNASSIGNED"
    assert report["production_model_promotion"] is False
    assert "TEST-ONLY-EVIDENCE" not in str(report)
    assert len(report["evidence_metadata_sha256"]) == 64


@pytest.mark.parametrize(
    ("change", "error"),
    [
        (lambda e: e["records"].pop(), "REVIEW_84_ITEM_COVERAGE_INCOMPLETE"),
        (
            lambda e: e["records"].append(deepcopy(e["records"][0])),
            "REVIEW_DUPLICATE_SOURCE_ID",
        ),
        (
            lambda e: e["records"][0].update(record_id="UNKNOWN"),
            "REVIEW_UNRECOGNIZED_SOURCE_ID",
        ),
        (
            lambda e: e["records"][0].update(record_sha256="a" * 64),
            "REVIEW_STALE_SOURCE_DIGEST",
        ),
        (
            lambda e: e["records"][0].update(outcome="APPROVED_FOR_TRAINING"),
            "REVIEW_OUTCOME_INVALID",
        ),
        (
            lambda e: e["records"][0].update(reviewed_at="2026-10-09T10:00:00"),
            "REVIEW_TIMESTAMP_NO_TIMEZONE",
        ),
        (
            lambda e: e.update(reviewer_organizational_role="SYSTEM"),
            "REVIEW_ROLE_MISMATCH",
        ),
        (
            lambda e: e.update(inventory_sha256="a" * 64),
            "REVIEW_SOURCE_INVENTORY_STALE",
        ),
        (
            lambda e: e.update(source_commit="different"),
            "REVIEW_SOURCE_COMMIT_STALE",
        ),
        (
            lambda e: e["records"][0].update(evidence_ref="SECRET please no"),
            "REVIEW_EVIDENCE_REFERENCE_INVALID",
        ),
        (
            lambda e: e["records"][0].update(training_approved=True),
            "REVIEW_ITEM_SCHEMA_INVALID",
        ),
        (
            lambda e: e.update(extra_permission=True),
            "REVIEW_BUNDLE_SCHEMA_INVALID",
        ),
    ],
)
def test_fails_closed_on_partial_stale_forged_or_illegal_scope(change, error):
    payload = synthetic_evidence_for_tests()
    change(payload)
    with pytest.raises(ReviewReconciliationError, match=error):
        reconcile_initial_review_evidence(payload)


def test_rewrite_and_reject_are_never_silently_accepted():
    payload = synthetic_evidence_for_tests()
    payload["records"][0]["outcome"] = "REWRITE_REQUIRED"
    payload["records"][1]["outcome"] = "CONTENT_REJECTED"
    result = reconcile_initial_review_evidence(payload)
    assert result["record_outcomes"] == {
        "CONTENT_ACCEPTED": 82,
        "CONTENT_REJECTED": 1,
        "REWRITE_REQUIRED": 1,
    }
    assert result["dataset_status"] == "NOT_APPROVED"


def test_missing_or_tampered_original_seed_never_admits_review(tmp_path: Path):
    original = Path(__file__).resolve().parents[2] / SOURCE_DIR
    target = tmp_path / SOURCE_DIR
    target.mkdir(parents=True)
    for filename, _, _, _ in SOURCE_SPECS:
        (target / filename).write_bytes((original / filename).read_bytes())
    payload = synthetic_evidence_for_tests()
    assert reconcile_initial_review_evidence(payload, tmp_path)["record_coverage"] == 84
    fname = SOURCE_SPECS[0][0]
    (target / fname).write_bytes((target / fname).read_bytes() + b"X")
    with pytest.raises(ValueError, match="SEED_GIT_BLOB_ATTESTATION_FAILED"):
        reconcile_initial_review_evidence(payload, tmp_path)


def test_unreviewed_original_authorial_patch_is_not_applied():
    report = reconcile_initial_review_evidence(synthetic_evidence_for_tests())
    assert report["patches_with_evidence"] == 0
    assert report["automatic_training_enabled"] is False
