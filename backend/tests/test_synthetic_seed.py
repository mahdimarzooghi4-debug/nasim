"""Synthetic-only, offline evidence inventory regression; never authorizes Training."""

import json
from pathlib import Path

import pytest

from nasim.learning.synthetic_seed import (
    SOURCE_DIR,
    SOURCE_SPECS,
    SeedIntegrityError,
    build_initial_synthetic_inventory,
)


def test_initial_synthetic_seed_is_exact_and_reproducible():
    inventory = build_initial_synthetic_inventory()
    assert inventory == build_initial_synthetic_inventory()
    assert inventory["record_count"] == 84
    assert inventory["fictional_fixture_count"] == 8
    assert inventory["pending_authorial_patch_count"] == 2
    assert len(inventory["candidate_records"]) == 84
    assert inventory["dataset_status"] == "SOURCE_ATTESTED_NOT_APPROVED"
    assert inventory["source_authorization_decision"] == "D-0154"
    assert inventory["quality_review"] == "PENDING_INDEPENDENT_PER_RECORD"
    assert inventory["training_evaluation_partition"] == "UNASSIGNED"
    assert inventory["production_training_enabled"] is False
    assert len(inventory["inventory_sha256"]) == 64
    assert all(len(r["record_sha256"]) == 64 for r in inventory["candidate_records"])
    assert not any("question" in r or "desired_answer" in r for r in inventory["candidate_records"])


def test_one_byte_tamper_fails_closed(tmp_path: Path):
    src_root = Path(__file__).resolve().parents[2]
    source = src_root / SOURCE_DIR
    target = tmp_path / SOURCE_DIR
    target.mkdir(parents=True)
    for filename, _, _, _ in SOURCE_SPECS:
        (target / filename).write_bytes((source / filename).read_bytes())
    assert build_initial_synthetic_inventory(tmp_path)["record_count"] == 84
    target_file = target / SOURCE_SPECS[0][0]
    target_file.write_bytes(target_file.read_bytes() + b" ")
    with pytest.raises(SeedIntegrityError, match="SEED_GIT_BLOB_ATTESTATION_FAILED"):
        build_initial_synthetic_inventory(tmp_path)


def test_missing_fictional_source_fails_closed(tmp_path: Path):
    with pytest.raises(SeedIntegrityError, match="SEED_SOURCE_MISSING_OR_SYMLINK"):
        build_initial_synthetic_inventory(tmp_path)


def test_authorial_patch_is_not_silently_promoted():
    root = Path(__file__).resolve().parents[2] / SOURCE_DIR
    patches = [
        json.loads(line)
        for line in (root / SOURCE_SPECS[3][0]).read_text(encoding="utf-8").splitlines()
    ]
    assert {p["target_record_id"] for p in patches} == {
        "NSIM-SYN-034",
        "NSIM-SYN-GP-022",
    }
    assert all(p["authorization"] == "NOT_AUTHORIZED" for p in patches)
    assert all(p["human_review"] == "PENDING" for p in patches)
