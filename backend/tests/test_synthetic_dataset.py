"""No real learner, reviewer signature or elder record is created in these tests."""

from pathlib import Path

import pytest

from nasim.learning.synthetic_dataset import build_initial_synthetic_dataset_package
from nasim.learning.synthetic_seed import SOURCE_DIR, SOURCE_SPECS


def test_approved_two_editorial_successors_and_group_disjoint_partition():
    package = build_initial_synthetic_dataset_package()
    assert package == build_initial_synthetic_dataset_package()
    manifest = package["manifest"]
    assert manifest["schema"] == "nasim.synthetic-offline-split.v1"
    assert manifest["training_count"] == 67
    assert manifest["evaluation_count"] == 17
    assert manifest["content_revision_count"] == 2
    assert len(manifest["manifest_sha256"]) == 64
    assert manifest["operational_training_eligibility"] == "NONE"
    assert manifest["dataset_runtime_registration"] == "NOT_PERFORMED"
    assert manifest["production_model_promotion"] is False
    assert set(manifest["training_groups"]).isdisjoint(manifest["evaluation_groups"])
    assert len({row["id"] for part in ("training", "evaluation") for row in package[part]}) == 84
    all_rows = [row for part in ("training", "evaluation") for row in package[part]]
    assert all(row["is_authoritative_nasim_operational_policy"] is False for row in all_rows)
    assert all(row["is_artificial_training_example"] is True for row in all_rows)


def test_both_user_accepted_edits_applied_only_in_derived_version():
    p = build_initial_synthetic_dataset_package()
    rows = {r["id"]: r for part in ("training", "evaluation") for r in p[part]}
    answer = rows["NSIM-SYN-034"]
    assert "نقش پشتیبانی نسیم به‌عنوان مرجع جایگزین آینده" not in answer["desired_answer"]
    assert "نمی‌توانم شما را به پشتیبانی وصل کنم" in answer["desired_answer"]
    assert answer["editorial_successor"]["patch_id"] == "NSIM-EDIT-001"
    question = rows["NSIM-SYN-GP-022"]
    assert "چه نوع مطلب تازه‌ای" in question["question"]
    assert question["editorial_successor"]["patch_id"] == "NSIM-EDIT-002"
    assert answer["original_sha256"] != answer["effective_sha256"]
    assert question["original_sha256"] != question["effective_sha256"]
    assert p["manifest"]["editorial_successor_owner_decision"] == "D-0164"


def test_corpus_has_no_cross_partition_scenario_fixture_groups():
    p = build_initial_synthetic_dataset_package()
    training = p["training"]
    evaluation = p["evaluation"]
    assert set(row["group_key"] for row in training).isdisjoint(
        row["group_key"] for row in evaluation
    )
    assert {row["source_fixture_id"] for row in training if row["source_fixture_id"]}.isdisjoint(
        row["source_fixture_id"] for row in evaluation if row["source_fixture_id"]
    )
    assert {row["id"] for row in training}.isdisjoint({row["id"] for row in evaluation})


def test_tamper_denies_entire_package(tmp_path: Path):
    src = Path(__file__).resolve().parents[2] / SOURCE_DIR
    dst = tmp_path / SOURCE_DIR
    dst.mkdir(parents=True)
    for filename, _, _, _ in SOURCE_SPECS:
        (dst / filename).write_bytes((src / filename).read_bytes())
    assert build_initial_synthetic_dataset_package(tmp_path)["manifest"]["training_count"] == 67
    patchfile = dst / SOURCE_SPECS[3][0]
    patchfile.write_bytes(patchfile.read_bytes() + b"\n ")
    with pytest.raises(ValueError, match="SEED_GIT_BLOB_ATTESTATION_FAILED"):
        build_initial_synthetic_dataset_package(tmp_path)
