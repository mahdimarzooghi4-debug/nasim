"""Immutable pre-operational Provider Candidate registry."""

from datetime import datetime
from uuid import UUID

from sqlalchemy import CheckConstraint, DateTime, ForeignKey, Index, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from nasim.infrastructure.models import Base, Identified


class ProviderCandidateRecord(Identified, Base):
    __tablename__ = "provider_candidate_record"

    display_name: Mapped[str] = mapped_column(Text)
    registered_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    registered_by_actor_id: Mapped[str] = mapped_column(String(200))
    registered_by_actor_type: Mapped[str] = mapped_column(String(20))
    reason: Mapped[str] = mapped_column(Text)
    correlation_id: Mapped[str] = mapped_column(String(200))

    __table_args__ = (
        CheckConstraint(
            "registered_by_actor_type IN ('HUMAN','SYSTEM','AI','AUTOMATION')",
            name="ck_provider_candidate_actor_type",
        ),
        CheckConstraint(
            "display_name ~ '[^[:space:]]' AND reason ~ '[^[:space:]]' "
            "AND length(trim(registered_by_actor_id)) > 0 "
            "AND length(trim(correlation_id)) > 0",
            name="ck_provider_candidate_provenance",
        ),
        Index("ix_provider_candidate_registered", "registered_at", "id"),
    )


class ProviderQualificationEvidenceRecord(Identified, Base):
    __tablename__ = "provider_qualification_evidence_record"

    provider_candidate_id: Mapped[UUID] = mapped_column(
        ForeignKey("provider_candidate_record.id"), index=True
    )
    evidence_label: Mapped[str] = mapped_column(Text)
    evidence_reference: Mapped[str] = mapped_column(Text)
    recorded_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    recorded_by_actor_id: Mapped[str] = mapped_column(String(200))
    recorded_by_actor_type: Mapped[str] = mapped_column(String(20))
    reason: Mapped[str] = mapped_column(Text)
    correlation_id: Mapped[str] = mapped_column(String(200))

    __table_args__ = (
        CheckConstraint(
            "recorded_by_actor_type IN ('HUMAN','SYSTEM','AI','AUTOMATION')",
            name="ck_provider_qualification_evidence_actor_type",
        ),
        CheckConstraint(
            "evidence_label ~ '[^[:space:]]' "
            "AND evidence_reference ~ '[^[:space:]]' "
            "AND reason ~ '[^[:space:]]' "
            "AND length(trim(recorded_by_actor_id)) > 0 "
            "AND length(trim(correlation_id)) > 0",
            name="ck_provider_qualification_evidence_provenance",
        ),
        Index(
            "ix_provider_qualification_evidence_recorded",
            "provider_candidate_id",
            "recorded_at",
            "id",
        ),
    )



class ProviderQualificationReviewRequestRecord(Identified, Base):
    __tablename__ = "provider_qualification_review_request_record"

    provider_candidate_id: Mapped[UUID] = mapped_column(
        ForeignKey("provider_candidate_record.id"), index=True
    )
    requested_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    requested_by_actor_id: Mapped[str] = mapped_column(String(200))
    requested_by_actor_type: Mapped[str] = mapped_column(String(20))
    reason: Mapped[str] = mapped_column(Text)
    correlation_id: Mapped[str] = mapped_column(String(200))

    __table_args__ = (
        CheckConstraint(
            "requested_by_actor_type IN ('HUMAN','SYSTEM','AI','AUTOMATION')",
            name="ck_provider_qualification_review_actor_type",
        ),
        CheckConstraint(
            "reason ~ '[^[:space:]]' "
            "AND length(trim(requested_by_actor_id)) > 0 "
            "AND length(trim(correlation_id)) > 0",
            name="ck_provider_qualification_review_provenance",
        ),
        Index(
            "ix_provider_qualification_review_requested",
            "provider_candidate_id",
            "requested_at",
            "id",
        ),
    )
