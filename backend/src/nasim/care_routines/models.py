"""Append-only records for configurable daily care routines."""

from datetime import date, datetime
from uuid import UUID

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    Date,
    DateTime,
    ForeignKey,
    ForeignKeyConstraint,
    Index,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from nasim.infrastructure.models import Base, Identified


class CareRoutineRecord(Identified, Base):
    __tablename__ = "care_routine_record"

    case_id: Mapped[UUID] = mapped_column(ForeignKey("elder_case.id"), index=True)
    routine_type: Mapped[str] = mapped_column(String(30))
    title: Mapped[str] = mapped_column(Text)
    schedule: Mapped[dict] = mapped_column(JSONB)
    active: Mapped[bool] = mapped_column(Boolean)
    supersedes_routine_id: Mapped[UUID | None]
    recorded_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    recorded_by_actor_id: Mapped[str] = mapped_column(String(200))
    recorded_by_actor_type: Mapped[str] = mapped_column(String(20))
    correlation_id: Mapped[str] = mapped_column(String(200))

    __table_args__ = (
        UniqueConstraint("case_id", "id", name="uq_care_routine_case_id"),
        UniqueConstraint("supersedes_routine_id", name="uq_care_routine_successor"),
        ForeignKeyConstraint(
            ["case_id", "supersedes_routine_id"],
            ["care_routine_record.case_id", "care_routine_record.id"],
            name="fk_care_routine_lineage",
        ),
        CheckConstraint(
            "routine_type IN ('APP_REMINDER','CAREGIVER_TASK')",
            name="ck_care_routine_type",
        ),
        CheckConstraint(
            "recorded_by_actor_type IN ('HUMAN','SYSTEM','AI','AUTOMATION')",
            name="ck_care_routine_actor_type",
        ),
        CheckConstraint(
            "title ~ '[^[:space:]]' AND length(trim(recorded_by_actor_id)) > 0 "
            "AND length(trim(correlation_id)) > 0",
            name="ck_care_routine_provenance",
        ),
        Index("ix_care_routine_case_recorded", "case_id", "recorded_at", "id"),
    )


class CareRoutineEventRecord(Identified, Base):
    __tablename__ = "care_routine_event_record"

    case_id: Mapped[UUID] = mapped_column(ForeignKey("elder_case.id"), index=True)
    routine_id: Mapped[UUID]
    occurrence_date: Mapped[date] = mapped_column(Date)
    status: Mapped[str] = mapped_column(String(20))
    occurred_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    recorded_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    recorded_by_actor_id: Mapped[str] = mapped_column(String(200))
    recorded_by_actor_type: Mapped[str] = mapped_column(String(20))
    correlation_id: Mapped[str] = mapped_column(String(200))

    __table_args__ = (
        ForeignKeyConstraint(
            ["case_id", "routine_id"],
            ["care_routine_record.case_id", "care_routine_record.id"],
            name="fk_care_routine_event_routine",
        ),
        UniqueConstraint("routine_id", "occurrence_date", name="uq_care_routine_occurrence"),
        CheckConstraint(
            "status IN ('DONE','NOT_DONE','SKIPPED')",
            name="ck_care_routine_event_status",
        ),
        CheckConstraint(
            "recorded_by_actor_type = 'HUMAN'",
            name="ck_care_routine_event_human_actor",
        ),
        CheckConstraint(
            "length(trim(recorded_by_actor_id)) > 0 AND length(trim(correlation_id)) > 0",
            name="ck_care_routine_event_provenance",
        ),
        Index("ix_care_routine_event_case_date", "case_id", "occurrence_date", "id"),
    )
