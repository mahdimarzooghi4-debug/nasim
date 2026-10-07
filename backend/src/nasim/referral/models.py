"""Referral owns only its immutable recording evidence."""

from datetime import datetime
from uuid import UUID

from sqlalchemy import CheckConstraint, DateTime, ForeignKeyConstraint, Index, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from nasim.infrastructure.models import Base, Identified


class ReferralRecord(Identified, Base):
    __tablename__ = "referral_record"
    case_id: Mapped[UUID]
    source_need_observation_id: Mapped[UUID]
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    created_by_actor_id: Mapped[str] = mapped_column(String(200))
    created_by_actor_type: Mapped[str] = mapped_column(String(20))
    reason: Mapped[str] = mapped_column(Text)
    correlation_id: Mapped[str] = mapped_column(String(200))
    __table_args__ = (
        ForeignKeyConstraint(
            ["case_id", "source_need_observation_id"],
            ["case_observation.case_id", "case_observation.id"],
            name="fk_referral_same_case_need",
        ),
        CheckConstraint(
            "created_by_actor_type IN ('HUMAN','SYSTEM','AI','AUTOMATION')",
            name="ck_referral_actor_type",
        ),
        CheckConstraint(
            "reason ~ '[^[:space:]]' AND length(trim(correlation_id)) > 0 "
            "AND length(trim(created_by_actor_id)) > 0",
            name="ck_referral_provenance",
        ),
        Index("ix_referral_case_created", "case_id", "created_at", "id"),
    )
