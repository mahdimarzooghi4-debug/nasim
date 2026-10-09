"""D-0162 is an owner's reported content verdict, NOT a real evidence file."""

from pathlib import Path

import pytest

from nasim.learning.owner_reported_acceptance import build_owner_reported_content_acceptance
from nasim.learning.review_evidence import (
    ReviewReconciliationError,
    reconcile_initial_review_evidence,
)
from nasim.learning.synthetic_seed import SOURCE_DIR, SOURCE_SPECS


def test_all_84_reported_accepted_preserves_original_dataset_barriers():
    report = build_owner_reported_content_acceptance()
    assert report == build_owner_reported_content_acceptance()
    assert report["all_content_accepted_owner_attestation"] == "D-0162"
    assert report["human_review_performed_owner_attestation"] == "D-0160"
    assert len(report["records"]) == 84
    assert len({row["record_id"] for row in report["records"]}) == 84
    assert all(
        row["content_outcome"] == "ACCEPTED_AS_REPORTED_BY_PRODUCT_OWNER"
        for row in report["records"]
    )
    assert report["reported_content_accepted"] == 84
    assert report["reported_content_rejected"] == 0
    assert report["reported_content_needs_rewrite"] == 0
    assert report["actual_human_review_source_version"] == "EXTERNAL_EVIDENCE_NOT_RECONCILED"
    assert report["actual_human_review_signed_evidence"] == "NOT_PROVIDED"
    assert report["authorial_patch_decisions"] == "UNRESOLVED"
    assert report["historical_original_source_flags"] == "UNCHANGED"
    assert report["dataset_status"] == "NOT_APPROVED"
    assert report["training_evaluation_partition"] == "UNASSIGNED"
    assert report["runtime_training_enabled"] is False
    assert report["production_promotion_authorized"] is False
    assert len(report["report_sha256"]) == 64


def test_owner_report_can_never_masquerade_as_authenticated_human_evidence():
    owner_report = build_owner_reported_content_acceptance()
    with pytest.raises(ReviewReconciliationError, match="REVIEW_BUNDLE_SCHEMA_INVALID"):
        reconcile_initial_review_evidence(owner_report)


def test_original_corpus_version_tamper_invalidates_owner_overlay(tmp_path: Path):
    source_root = Path(__file__).resolve().parents[2] / SOURCE_DIR
    target = tmp_path / SOURCE_DIR
    target.mkdir(parents=True)
    for filename, _, _, _ in SOURCE_SPECS:
        (target / filename).write_bytes((source_root / filename).read_bytes())
    report = build_owner_reported_content_acceptance(tmp_path)
    assert report["reported_content_accepted"] == 84
    target_file = target / SOURCE_SPECS[1][0]
    target_file.write_bytes(target_file.read_bytes() + b"X")
    with pytest.raises(ValueError, match="SEED_GIT_BLOB_ATTESTATION_FAILED"):
        build_owner_reported_content_acceptance(tmp_path)
