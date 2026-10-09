"""Persistence of proposed manifest identity, deliberately disconnected from Runtime.

A future authorized worker must inject an independently reviewed AdmissionVerifier
and use a separately authorized database login. No verifier or writer is wired
into FastAPI, Outbox, scheduler, Training, or Production model selection.
"""

import json
from collections.abc import Iterable
from datetime import UTC, datetime
from hashlib import sha256
from uuid import UUID, uuid5

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from nasim.learning.dataset_manifest import (
    AdmissionUnavailable,
    AdmissionVerifier,
    CuratedSourceRef,
    DatasetManifest,
    DatasetPurpose,
    ManifestError,
    VersionedManifestBuilder,
)
from nasim.learning.models import ProposedDatasetManifest, ProposedDatasetSource

_NAMESPACE = UUID("7c926789-2ae3-47aa-8909-02a901c6d2d8")


def attest_stored_manifest(manifest: DatasetManifest) -> None:
    """Verify content address & deterministic ID without granting eligibility."""

    # Integrity verification is not a substitute for an admission decision.
    ordered = tuple(
        sorted(
            manifest.sources,
            key=lambda source: (
                source.namespace,
                str(source.source_id),
                source.source_version_sha256,
                source.curation_evidence_sha256,
            ),
        )
    )
    if not ordered or len({s.source_key for s in ordered}) != len(ordered):
        raise ManifestError("CORRUPT_MANIFEST_MEMBERSHIP")
    canonical = {
        "manifest_schema": "nasim.dataset-manifest.v1",
        "purpose": manifest.purpose.value,
        "policy_sha256": manifest.policy_sha256,
        "approval_evidence_sha256": manifest.approval_evidence_sha256,
        "sources": [source.serialized() for source in ordered],
    }
    packed = json.dumps(canonical, ensure_ascii=True, sort_keys=True, separators=(",", ":")).encode(
        "utf-8"
    )
    digest = sha256(packed).hexdigest()
    if (
        manifest.sources != ordered
        or manifest.manifest_sha256 != digest
        or manifest.manifest_id != uuid5(_NAMESPACE, digest)
    ):
        raise ManifestError("MANIFEST_ATTESTATION_FAILED")


class ProposedManifestRegistry:
    """Inactive technical store: requires explicit verifier + privileged writer."""

    def __init__(
        self,
        sessions: async_sessionmaker[AsyncSession],
        verifier: AdmissionVerifier | None = None,
    ) -> None:
        self._sessions = sessions
        self._builder = VersionedManifestBuilder(verifier)
        self._enabled = verifier is not None

    async def propose(
        self, purpose: DatasetPurpose, sources: Iterable[CuratedSourceRef]
    ) -> DatasetManifest:
        # Default-deny *before opening a DB transaction*.
        if not self._enabled:
            raise AdmissionUnavailable("TRAINING_ELIGIBILITY_POLICY_NOT_APPROVED")
        manifest = self._builder.build(purpose, sources)
        attest_stored_manifest(manifest)

        try:
            async with self._sessions() as session, session.begin():
                result = await session.execute(
                    pg_insert(ProposedDatasetManifest)
                    .values(
                        id=manifest.manifest_id,
                        manifest_sha256=manifest.manifest_sha256,
                        purpose=manifest.purpose.value,
                        policy_sha256=manifest.policy_sha256,
                        approval_evidence_sha256=manifest.approval_evidence_sha256,
                        source_count=len(manifest.sources),
                        recorded_at=datetime.now(UTC),
                    )
                    .on_conflict_do_nothing(index_elements=["id"])
                    .returning(ProposedDatasetManifest.id)
                )
                inserted = result.scalar_one_or_none() is not None
                if inserted:
                    session.add_all(
                        ProposedDatasetSource(
                            manifest_id=manifest.manifest_id,
                            namespace=s.namespace,
                            source_id=s.source_id,
                            source_version_sha256=s.source_version_sha256,
                            curation_evidence_sha256=s.curation_evidence_sha256,
                        )
                        for s in manifest.sources
                    )
                else:
                    # If a concurrent identical proposal already committed, verify
                    # all bytes, not just the UUID, before treating it as replay.
                    existing = await self._read(session, manifest.manifest_id)
                    if existing != manifest:
                        raise ManifestError("MANIFEST_REPLAY_CONFLICT")
        except IntegrityError as error:
            # The PostgreSQL trigger is the authoritative cross-manifest
            # partition guard, including concurrent competing proposals.
            # Never reinterpret unrelated DB failures as business eligibility.
            if (
                getattr(error.orig, "sqlstate", None) == "23514"
                and "LEARNING_SOURCE_PARTITION_CONFLICT" in str(error.orig)
            ):
                raise ManifestError("TRAINING_EVALUATION_SOURCE_OVERLAP") from error
            raise
        return manifest

    async def read(self, manifest_id: UUID) -> DatasetManifest | None:
        async with self._sessions() as session:
            return await self._read(session, manifest_id)

    @staticmethod
    async def _read(session: AsyncSession, manifest_id: UUID) -> DatasetManifest | None:
        header = await session.get(ProposedDatasetManifest, manifest_id)
        if header is None:
            return None
        rows = (
            await session.scalars(
                select(ProposedDatasetSource)
                .where(ProposedDatasetSource.manifest_id == manifest_id)
                .order_by(
                    ProposedDatasetSource.namespace,
                    ProposedDatasetSource.source_id,
                    ProposedDatasetSource.source_version_sha256,
                    ProposedDatasetSource.curation_evidence_sha256,
                )
            )
        ).all()
        if len(rows) != header.source_count:
            raise ManifestError("CORRUPT_MANIFEST_MEMBERSHIP")
        try:
            reconstructed = DatasetManifest(
                manifest_id=header.id,
                manifest_sha256=header.manifest_sha256,
                purpose=DatasetPurpose(header.purpose),
                policy_sha256=header.policy_sha256,
                approval_evidence_sha256=header.approval_evidence_sha256,
                sources=tuple(
                    CuratedSourceRef(
                        namespace=row.namespace,
                        source_id=row.source_id,
                        source_version_sha256=row.source_version_sha256,
                        curation_evidence_sha256=row.curation_evidence_sha256,
                    )
                    for row in rows
                ),
            )
            attest_stored_manifest(reconstructed)
        except (ValueError, TypeError) as error:
            raise ManifestError("STORED_MANIFEST_INVALID") from error
        return reconstructed
