"""Inert proposed Dataset manifest storage; no serving-runtime mutation grants."""

from datetime import datetime
from uuid import UUID

from sqlalchemy import CheckConstraint, DateTime, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from nasim.infrastructure.models import Base

SHA_CHECK = "^[0-9a-f]{64}$"


class ProposedDatasetManifest(Base):
    __tablename__ = "learning_proposed_manifest"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    manifest_sha256: Mapped[str] = mapped_column(String(64))
    purpose: Mapped[str] = mapped_column(String(12))
    policy_sha256: Mapped[str] = mapped_column(String(64))
    approval_evidence_sha256: Mapped[str] = mapped_column(String(64))
    source_count: Mapped[int] = mapped_column(Integer)
    recorded_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))

    __table_args__ = (
        UniqueConstraint("manifest_sha256", name="uq_learning_manifest_digest"),
        CheckConstraint("purpose IN ('TRAINING', 'EVALUATION')", name="ck_learning_purpose"),
        CheckConstraint("source_count > 0", name="ck_learning_source_count"),
        CheckConstraint(
            f"manifest_sha256 ~ '{SHA_CHECK}' AND policy_sha256 ~ '{SHA_CHECK}' "
            f"AND approval_evidence_sha256 ~ '{SHA_CHECK}'",
            name="ck_learning_manifest_digests",
        ),
    )


class ProposedDatasetSource(Base):
    __tablename__ = "learning_proposed_source"

    manifest_id: Mapped[UUID] = mapped_column(
        ForeignKey("learning_proposed_manifest.id", ondelete="RESTRICT"),
        primary_key=True,
    )
    namespace: Mapped[str] = mapped_column(String(80), primary_key=True)
    source_id: Mapped[UUID] = mapped_column(primary_key=True)
    source_version_sha256: Mapped[str] = mapped_column(String(64))
    curation_evidence_sha256: Mapped[str] = mapped_column(String(64))

    __table_args__ = (
        CheckConstraint(
            "namespace ~ '^[a-z][a-z0-9_.-]{0,79}$'",
            name="ck_learning_source_namespace",
        ),
        CheckConstraint(
            f"source_version_sha256 ~ '{SHA_CHECK}' AND curation_evidence_sha256 ~ '{SHA_CHECK}'",
            name="ck_learning_source_digests",
        ),
    )


class SourcePurposeClaim(Base):
    """One immutable technical TRAINING/EVALUATION source partition reservation.

    An opaque source identity may recur in manifests with the SAME purpose,
    never the opposite purpose. This is NOT household-level independence.
    """

    __tablename__ = "learning_source_purpose_claim"

    namespace: Mapped[str] = mapped_column(String(80), primary_key=True)
    source_id: Mapped[UUID] = mapped_column(primary_key=True)
    purpose: Mapped[str] = mapped_column(String(12))

    __table_args__ = (
        CheckConstraint(
            "namespace ~ '^[a-z][a-z0-9_.-]{0,79}$'",
            name="ck_learning_partition_source_namespace",
        ),
        CheckConstraint(
            "purpose IN ('TRAINING', 'EVALUATION')",
            name="ck_learning_partition_purpose",
        ),
    )
