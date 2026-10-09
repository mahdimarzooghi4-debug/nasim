"""Synthetic-only PostgreSQL evidence for dormant Dataset manifest persistence.

All source references and attestations here are synthetic. None of these test
verifiers are imported by the serving runtime or provide legal permission.
"""

import asyncio
import os
from dataclasses import replace
from uuid import uuid4

import pytest
from pydantic import PostgresDsn
from sqlalchemy import func, select, text
from sqlalchemy.exc import DBAPIError

from nasim.infrastructure.config import Settings
from nasim.infrastructure.database import make_engine, make_sessions
from nasim.learning.dataset_manifest import (
    AdmissionEvidence,
    AdmissionUnavailable,
    CuratedSourceRef,
    DatasetAdmissionRequest,
    DatasetPurpose,
    ManifestError,
)
from nasim.learning.models import (
    ProposedDatasetManifest,
    ProposedDatasetSource,
    SourcePurposeClaim,
)
from nasim.learning.registry import ProposedManifestRegistry, attest_stored_manifest

pytestmark = pytest.mark.integration

A = "a" * 64
B = "b" * 64
C = "c" * 64
D = "d" * 64


class SyntheticAdmission:
    """Unit fixture ONLY; not an accepted operational training policy."""

    def verify(self, request: DatasetAdmissionRequest) -> AdmissionEvidence:
        return AdmissionEvidence(
            policy_sha256=C,
            approval_evidence_sha256=D,
            eligible_sources=frozenset(
                (
                    source.namespace,
                    str(source.source_id),
                    source.source_version_sha256,
                    source.curation_evidence_sha256,
                )
                for source in request.sources
            ),
        )


def synthetic_source() -> CuratedSourceRef:
    return CuratedSourceRef(
        namespace="synthetic.example",
        source_id=uuid4(),
        source_version_sha256=A,
        curation_evidence_sha256=B,
    )


@pytest.fixture
def owner_registry(admin_engine):
    return ProposedManifestRegistry(make_sessions(admin_engine), SyntheticAdmission())


async def row_counts(engine) -> tuple[int, int]:
    async with engine.connect() as connection:
        return (
            (await connection.scalar(select(func.count()).select_from(ProposedDatasetManifest)))
            or 0,
            (await connection.scalar(select(func.count()).select_from(ProposedDatasetSource))) or 0,
        )


async def test_default_denial_performs_no_database_write(admin_engine):
    registry = ProposedManifestRegistry(make_sessions(admin_engine))
    assert await row_counts(admin_engine) == (0, 0)
    with pytest.raises(AdmissionUnavailable, match="TRAINING_ELIGIBILITY_POLICY_NOT_APPROVED"):
        await registry.propose(DatasetPurpose.TRAINING, [synthetic_source()])
    assert await row_counts(admin_engine) == (0, 0)
    assert await registry.read(uuid4()) is None


async def test_synthetic_manifest_atomic_persistence_digest_and_replay(
    admin_engine, owner_registry
):
    a, b, c = synthetic_source(), synthetic_source(), synthetic_source()
    created = await owner_registry.propose(DatasetPurpose.TRAINING, [b, c, a])
    assert created == await owner_registry.read(created.manifest_id)
    attest_stored_manifest(created)
    assert await row_counts(admin_engine) == (1, 3)
    repeated = await owner_registry.propose(DatasetPurpose.TRAINING, [a, b, c])
    assert repeated == created
    assert await row_counts(admin_engine) == (1, 3)
    assert created.policy_sha256 == C
    assert created.approval_evidence_sha256 == D


async def test_concurrent_identical_replays_are_race_safe(admin_engine, owner_registry):
    refs = [synthetic_source() for _ in range(4)]
    manifests = await asyncio.gather(
        *(owner_registry.propose(DatasetPurpose.TRAINING, refs) for _ in range(4))
    )
    assert all(result == manifests[0] for result in manifests)
    assert await row_counts(admin_engine) == (1, 4)


async def test_cross_manifest_training_evaluation_overlap_is_rejected_durably(
    admin_engine, owner_registry
):
    ref = synthetic_source()
    training = await owner_registry.propose(DatasetPurpose.TRAINING, [ref])
    with pytest.raises(ManifestError, match="TRAINING_EVALUATION_SOURCE_OVERLAP"):
        await owner_registry.propose(DatasetPurpose.EVALUATION, [ref])
    assert await row_counts(admin_engine) == (1, 1)
    assert await owner_registry.read(training.manifest_id) == training
    async with admin_engine.connect() as connection:
        assert await connection.scalar(select(func.count()).select_from(SourcePurposeClaim)) == 1


async def test_pg_update_delete_triggers_protect_all_immutable_rows(admin_engine, owner_registry):
    ref = synthetic_source()
    created = await owner_registry.propose(DatasetPurpose.TRAINING, [ref])
    async with admin_engine.connect() as connection:
        with pytest.raises(DBAPIError):
            async with connection.begin():
                await connection.execute(
                    text("UPDATE learning_proposed_manifest SET source_count=99 WHERE id=:id"),
                    {"id": created.manifest_id},
                )
        await connection.rollback()
        with pytest.raises(DBAPIError):
            async with connection.begin():
                await connection.execute(
                    text(
                        "DELETE FROM learning_proposed_source "
                        "WHERE manifest_id=:id AND source_id=:source_id"
                    ),
                    {"id": created.manifest_id, "source_id": ref.source_id},
                )
        await connection.rollback()
    assert await owner_registry.read(created.manifest_id) == created


async def test_invalid_additional_source_never_passes_read_attestation(
    admin_engine, owner_registry
):
    created = await owner_registry.propose(DatasetPurpose.TRAINING, [synthetic_source()])
    # Simulates a privileged erroneous writer; server never grants this action.
    # Read attestation detects even syntactically valid but incorrect membership.
    rogue = synthetic_source()
    async with admin_engine.begin() as connection:
        await connection.execute(
            text(
                "INSERT INTO learning_proposed_source "
                "(manifest_id,namespace,source_id,source_version_sha256,curation_evidence_sha256)"
                " VALUES (:manifest_id,:namespace,:source_id,:version,:curation)"
            ),
            {
                "manifest_id": created.manifest_id,
                "namespace": rogue.namespace,
                "source_id": rogue.source_id,
                "version": rogue.source_version_sha256,
                "curation": rogue.curation_evidence_sha256,
            },
        )
    with pytest.raises(ManifestError, match="CORRUPT_MANIFEST_MEMBERSHIP"):
        await owner_registry.read(created.manifest_id)


async def test_serving_runtime_may_read_but_cannot_insert_update_or_delete_manifest(
    admin_engine,
):
    db_url = os.environ.get("NASIM_TEST_APP_DATABASE_URL")
    if not db_url:
        pytest.skip("Dedicated CI serving principal is required for permission test")
    engine = make_engine(Settings(database_url=PostgresDsn(db_url)))
    try:
        async with engine.connect() as conn:
            for table in (
                "learning_proposed_manifest",
                "learning_proposed_source",
                "learning_source_purpose_claim",
            ):
                write_grants = await conn.scalar(
                    text(
                        "SELECT has_table_privilege(current_user,:table,"
                        " 'INSERT,UPDATE,DELETE,TRUNCATE')"
                    ),
                    {"table": table},
                )
                assert write_grants is False
                can_read = await conn.scalar(
                    text("SELECT has_table_privilege(current_user,:table,'SELECT')"),
                    {"table": table},
                )
                assert can_read is False
        # Don't simulate a legitimate admitted writer with the serving role.
        manifest = ProposedManifestRegistry(make_sessions(engine), SyntheticAdmission())
        with pytest.raises(DBAPIError):
            await manifest.propose(DatasetPurpose.TRAINING, [synthetic_source()])
    finally:
        await engine.dispose()
    assert await row_counts(admin_engine) == (0, 0)


async def test_different_versions_cannot_cross_purpose_after_registration(
    admin_engine, owner_registry
):
    ref = synthetic_source()
    await owner_registry.propose(DatasetPurpose.TRAINING, [ref])
    with pytest.raises(ManifestError, match="TRAINING_EVALUATION_SOURCE_OVERLAP"):
        await owner_registry.propose(
            DatasetPurpose.EVALUATION, [replace(ref, source_version_sha256=D)]
        )
    assert await row_counts(admin_engine) == (1, 1)


async def test_same_purpose_can_reuse_identity_across_versioned_manifests(
    admin_engine, owner_registry
):
    ref = synthetic_source()
    earlier = await owner_registry.propose(DatasetPurpose.TRAINING, [ref])
    later = await owner_registry.propose(
        DatasetPurpose.TRAINING, [replace(ref, source_version_sha256=D)]
    )
    assert earlier.manifest_id != later.manifest_id
    assert await row_counts(admin_engine) == (2, 2)
    async with admin_engine.connect() as connection:
        assert await connection.scalar(select(func.count()).select_from(SourcePurposeClaim)) == 1


async def test_concurrent_opposite_purpose_only_one_is_persisted(admin_engine, owner_registry):
    source = synthetic_source()

    async def attempt(purpose):
        try:
            return await owner_registry.propose(purpose, [source])
        except ManifestError as error:
            return str(error)

    results = await asyncio.gather(
        attempt(DatasetPurpose.TRAINING),
        attempt(DatasetPurpose.EVALUATION),
    )
    assert sum(isinstance(r, str) for r in results) == 1
    assert "TRAINING_EVALUATION_SOURCE_OVERLAP" in results
    assert await row_counts(admin_engine) == (1, 1)
    async with admin_engine.connect() as connection:
        assert await connection.scalar(select(func.count()).select_from(SourcePurposeClaim)) == 1


async def test_concurrent_same_purpose_distinct_versions_remain_allowed(
    admin_engine, owner_registry
):
    source = synthetic_source()
    results = await asyncio.gather(
        owner_registry.propose(DatasetPurpose.TRAINING, [source]),
        owner_registry.propose(DatasetPurpose.TRAINING, [replace(source, source_version_sha256=D)]),
    )
    assert results[0].manifest_id != results[1].manifest_id
    assert await row_counts(admin_engine) == (2, 2)


async def test_direct_privileged_source_insert_cannot_bypass_partition_guard(
    admin_engine, owner_registry
):
    training_ref = synthetic_source()
    eval_ref = synthetic_source()
    await owner_registry.propose(DatasetPurpose.TRAINING, [training_ref])
    evaluation = await owner_registry.propose(DatasetPurpose.EVALUATION, [eval_ref])
    with pytest.raises(DBAPIError, match="LEARNING_SOURCE_PARTITION_CONFLICT"):
        async with admin_engine.begin() as connection:
            await connection.execute(
                text(
                    "INSERT INTO learning_proposed_source "
                    " (manifest_id,namespace,source_id,source_version_sha256, "
                    "curation_evidence_sha256) "
                    "VALUES (:manifest_id,:namespace,:source_id,:source_version_sha256,"
                    ":curation_evidence_sha256)"
                ),
                {
                    "manifest_id": evaluation.manifest_id,
                    "namespace": training_ref.namespace,
                    "source_id": training_ref.source_id,
                    "source_version_sha256": D,
                    "curation_evidence_sha256": B,
                },
            )
    assert await row_counts(admin_engine) == (2, 2)


async def test_partition_claim_is_append_only_for_all_database_writers(
    admin_engine, owner_registry
):
    source = synthetic_source()
    await owner_registry.propose(DatasetPurpose.TRAINING, [source])
    async with admin_engine.connect() as connection:
        with pytest.raises(DBAPIError):
            async with connection.begin():
                await connection.execute(
                    text("UPDATE learning_source_purpose_claim SET purpose='EVALUATION'")
                )
        await connection.rollback()
        with pytest.raises(DBAPIError):
            async with connection.begin():
                await connection.execute(text("DELETE FROM learning_source_purpose_claim"))
        await connection.rollback()
    assert await row_counts(admin_engine) == (1, 1)
