from datetime import datetime
from typing import Any
from uuid import UUID, uuid4

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    ForeignKeyConstraint,
    Index,
    Integer,
    String,
    Text,
    UniqueConstraint,
    text,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Identified:
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)


class Provenance:
    recorded_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    recorded_by_actor_id: Mapped[str] = mapped_column(String(200))
    recorded_by_actor_type: Mapped[str] = mapped_column(String(20))


ACTOR_CHECK = "recorded_by_actor_type IN ('HUMAN', 'SYSTEM', 'AI', 'AUTOMATION')"


class ElderCase(Identified, Base):
    __tablename__ = "elder_case"
    upstream_enrollment_ref: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    created_by_actor_id: Mapped[str] = mapped_column(String(200))
    created_by_actor_type: Mapped[str] = mapped_column(String(20))
    __table_args__ = (
        CheckConstraint(
            "created_by_actor_type IN ('HUMAN', 'SYSTEM', 'AI', 'AUTOMATION')",
            name="ck_case_actor_type",
        ),
    )


class ProfileRevision(Identified, Provenance, Base):
    __tablename__ = "case_profile_revision"
    case_id: Mapped[UUID] = mapped_column(ForeignKey("elder_case.id"), index=True)
    revision_no: Mapped[int] = mapped_column(Integer)
    elder_reference: Mapped[str] = mapped_column(Text)
    supersedes_revision_id: Mapped[UUID | None]
    correction_reason: Mapped[str | None] = mapped_column(Text)
    __table_args__ = (
        UniqueConstraint("case_id", "revision_no", name="uq_profile_revision"),
        UniqueConstraint("case_id", "id", name="uq_profile_case_id"),
        UniqueConstraint("supersedes_revision_id", name="uq_profile_successor"),
        ForeignKeyConstraint(
            ["case_id", "supersedes_revision_id"],
            ["case_profile_revision.case_id", "case_profile_revision.id"],
            name="fk_profile_lineage",
        ),
        CheckConstraint("revision_no > 0", name="ck_profile_revision_positive"),
        CheckConstraint(ACTOR_CHECK, name="ck_profile_actor_type"),
        CheckConstraint(
            "(revision_no = 1 AND supersedes_revision_id IS NULL AND correction_reason IS NULL)"
            " OR (revision_no > 1 AND supersedes_revision_id IS NOT NULL"
            " AND correction_reason IS NOT NULL AND length(trim(correction_reason)) > 0)",
            name="ck_profile_correction",
        ),
    )


class ContactRevision(Identified, Provenance, Base):
    __tablename__ = "contact_point_revision"
    case_id: Mapped[UUID] = mapped_column(ForeignKey("elder_case.id"), index=True)
    logical_contact_id: Mapped[UUID]
    revision_no: Mapped[int] = mapped_column(Integer)
    contact_kind: Mapped[str] = mapped_column(String(100))
    contact_value: Mapped[str] = mapped_column(Text)
    supersedes_revision_id: Mapped[UUID | None]
    correction_reason: Mapped[str | None] = mapped_column(Text)
    __table_args__ = (
        UniqueConstraint(
            "case_id", "logical_contact_id", "revision_no", name="uq_contact_revision"
        ),
        UniqueConstraint("case_id", "logical_contact_id", "id", name="uq_contact_lineage_target"),
        UniqueConstraint("supersedes_revision_id", name="uq_contact_successor"),
        ForeignKeyConstraint(
            ["case_id", "logical_contact_id", "supersedes_revision_id"],
            [
                "contact_point_revision.case_id",
                "contact_point_revision.logical_contact_id",
                "contact_point_revision.id",
            ],
            name="fk_contact_lineage",
        ),
        CheckConstraint("revision_no > 0", name="ck_contact_revision_positive"),
        CheckConstraint(ACTOR_CHECK, name="ck_contact_actor_type"),
        CheckConstraint(
            "(revision_no = 1 AND supersedes_revision_id IS NULL AND correction_reason IS NULL)"
            " OR (revision_no > 1 AND supersedes_revision_id IS NOT NULL"
            " AND correction_reason IS NOT NULL AND length(trim(correction_reason)) > 0)",
            name="ck_contact_correction",
        ),
    )


class Assignment(Identified, Base):
    __tablename__ = "case_assignment"
    case_id: Mapped[UUID] = mapped_column(ForeignKey("elder_case.id"), index=True)
    caregiver_actor_id: Mapped[str] = mapped_column(String(200))
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    ended_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    assigned_by_actor_id: Mapped[str] = mapped_column(String(200))
    assigned_by_actor_type: Mapped[str] = mapped_column(String(20))
    reason: Mapped[str] = mapped_column(Text)
    __table_args__ = (
        Index(
            "uq_assignment_active",
            "case_id",
            unique=True,
            postgresql_where=text("ended_at IS NULL"),
        ),
        CheckConstraint("ended_at IS NULL OR ended_at >= started_at", name="ck_assignment_time"),
        CheckConstraint("length(trim(reason)) > 0", name="ck_assignment_reason"),
        CheckConstraint(
            "assigned_by_actor_type IN ('HUMAN', 'SYSTEM', 'AI', 'AUTOMATION')",
            name="ck_assignment_actor_type",
        ),
    )


class Interaction(Identified, Provenance, Base):
    __tablename__ = "case_interaction"
    case_id: Mapped[UUID] = mapped_column(ForeignKey("elder_case.id"), index=True)
    interaction_type: Mapped[str] = mapped_column(String(20))
    occurred_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    content: Mapped[str] = mapped_column(Text)
    supersedes_interaction_id: Mapped[UUID | None]
    correction_reason: Mapped[str | None] = mapped_column(Text)
    __table_args__ = (
        UniqueConstraint("case_id", "id", name="uq_interaction_case_id"),
        UniqueConstraint("supersedes_interaction_id", name="uq_interaction_successor"),
        ForeignKeyConstraint(
            ["case_id", "supersedes_interaction_id"],
            ["case_interaction.case_id", "case_interaction.id"],
            name="fk_interaction_lineage",
        ),
        CheckConstraint(
            "interaction_type IN ('CONTACT', 'MONITORING')", name="ck_interaction_type"
        ),
        CheckConstraint(ACTOR_CHECK, name="ck_interaction_actor_type"),
        CheckConstraint(
            "(supersedes_interaction_id IS NULL AND correction_reason IS NULL) OR"
            "(supersedes_interaction_id IS NOT NULL AND correction_reason IS NOT "
            "NULL AND length(trim(correction_reason)) > 0)",
            name="ck_interaction_correction",
        ),
    )


class Observation(Identified, Provenance, Base):
    __tablename__ = "case_observation"
    case_id: Mapped[UUID] = mapped_column(ForeignKey("elder_case.id"), index=True)
    record_type: Mapped[str] = mapped_column(String(20))
    occurred_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    content: Mapped[str] = mapped_column(Text)
    supersedes_observation_id: Mapped[UUID | None]
    correction_reason: Mapped[str | None] = mapped_column(Text)
    __table_args__ = (
        UniqueConstraint("case_id", "id", name="uq_observation_case_id"),
        UniqueConstraint("supersedes_observation_id", name="uq_observation_successor"),
        ForeignKeyConstraint(
            ["case_id", "supersedes_observation_id"],
            ["case_observation.case_id", "case_observation.id"],
            name="fk_observation_lineage",
        ),
        CheckConstraint(
            "record_type IN ('OBSERVATION', 'NEED_CAPTURE')", name="ck_observation_type"
        ),
        CheckConstraint(ACTOR_CHECK, name="ck_observation_actor_type"),
        CheckConstraint(
            "(supersedes_observation_id IS NULL AND correction_reason IS NULL) OR"
            "(supersedes_observation_id IS NOT NULL AND correction_reason IS NOT "
            "NULL AND length(trim(correction_reason)) > 0)",
            name="ck_observation_correction",
        ),
    )


class AuditEntry(Identified, Base):
    __tablename__ = "audit_entry"
    case_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("elder_case.id"), index=True, nullable=True
    )
    actor_id: Mapped[str] = mapped_column(String(200))
    actor_type: Mapped[str] = mapped_column(String(20))
    action: Mapped[str] = mapped_column(String(100))
    resource_type: Mapped[str] = mapped_column(String(100))
    resource_id: Mapped[UUID]
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    correlation_id: Mapped[str] = mapped_column(String(200))
    before_reference: Mapped[UUID | None]
    after_reference: Mapped[UUID]
    reason: Mapped[str | None] = mapped_column(Text)
    __table_args__ = (
        CheckConstraint(
            "actor_type IN ('HUMAN', 'SYSTEM', 'AI', 'AUTOMATION')", name="ck_audit_actor_type"
        ),
        CheckConstraint(
            "case_id IS NOT NULL OR "
            "(action = 'provider.candidate_registered.v1' "
            "AND resource_type = 'provider_candidate_record')",
            name="ck_audit_case_or_provider_candidate",
        ),
        Index("ix_audit_timeline", "case_id", "timestamp", "id"),
    )


class OutboxEvent(Identified, Base):
    __tablename__ = "outbox_event"
    case_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("elder_case.id"), index=True, nullable=True
    )
    event_type: Mapped[str] = mapped_column(String(100))
    occurred_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    payload: Mapped[dict[str, Any]] = mapped_column(JSONB)
    __table_args__ = (
        CheckConstraint(
            "case_id IS NOT NULL OR event_type = 'provider.candidate_registered.v1'",
            name="ck_outbox_case_or_provider_candidate",
        ),
    )


class IdempotencyRecord(Identified, Base):
    __tablename__ = "idempotency_record"
    actor_id: Mapped[str] = mapped_column(String(200))
    operation: Mapped[str] = mapped_column(String(100))
    target: Mapped[str] = mapped_column(String(36))
    key: Mapped[str] = mapped_column(String(200))
    payload_hash: Mapped[str] = mapped_column(String(64))
    response: Mapped[dict[str, Any]] = mapped_column(JSONB)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    __table_args__ = (
        UniqueConstraint("actor_id", "operation", "target", "key", name="uq_idempotency_scope"),
    )
