"""Append-only care routine plans and explicit human occurrence records.

Revision ID: 0010_care_routines
Revises: 0009_learning_partition_claim

Notifications, elder self-access, and missed-response automation are not configured here.
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision: str = "0010_care_routines"
down_revision: str | Sequence[str] | None = "0009_learning_partition_claim"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "care_routine_record",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("case_id", sa.Uuid(), nullable=False),
        sa.Column("routine_type", sa.String(length=30), nullable=False),
        sa.Column("title", sa.Text(), nullable=False),
        sa.Column("schedule", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column("active", sa.Boolean(), nullable=False),
        sa.Column("supersedes_routine_id", sa.Uuid(), nullable=True),
        sa.Column("recorded_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("recorded_by_actor_id", sa.String(length=200), nullable=False),
        sa.Column("recorded_by_actor_type", sa.String(length=20), nullable=False),
        sa.Column("correlation_id", sa.String(length=200), nullable=False),
        sa.ForeignKeyConstraint(["case_id"], ["elder_case.id"]),
        sa.ForeignKeyConstraint(
            ["case_id", "supersedes_routine_id"],
            ["care_routine_record.case_id", "care_routine_record.id"],
            name="fk_care_routine_lineage",
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("case_id", "id", name="uq_care_routine_case_id"),
        sa.UniqueConstraint("supersedes_routine_id", name="uq_care_routine_successor"),
        sa.CheckConstraint(
            "routine_type IN ('APP_REMINDER','CAREGIVER_TASK')",
            name="ck_care_routine_type",
        ),
        sa.CheckConstraint(
            "recorded_by_actor_type IN ('HUMAN','SYSTEM','AI','AUTOMATION')",
            name="ck_care_routine_actor_type",
        ),
        sa.CheckConstraint(
            "title ~ '[^[:space:]]' AND length(trim(recorded_by_actor_id)) > 0 "
            "AND length(trim(correlation_id)) > 0",
            name="ck_care_routine_provenance",
        ),
    )
    op.create_index(
        "ix_care_routine_record_case_id",
        "care_routine_record",
        ["case_id"],
        unique=False,
    )
    op.create_index(
        "ix_care_routine_case_recorded",
        "care_routine_record",
        ["case_id", "recorded_at", "id"],
        unique=False,
    )
    op.create_table(
        "care_routine_event_record",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("case_id", sa.Uuid(), nullable=False),
        sa.Column("routine_id", sa.Uuid(), nullable=False),
        sa.Column("occurrence_date", sa.Date(), nullable=False),
        sa.Column("status", sa.String(length=20), nullable=False),
        sa.Column("occurred_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("recorded_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("recorded_by_actor_id", sa.String(length=200), nullable=False),
        sa.Column("recorded_by_actor_type", sa.String(length=20), nullable=False),
        sa.Column("correlation_id", sa.String(length=200), nullable=False),
        sa.ForeignKeyConstraint(["case_id"], ["elder_case.id"]),
        sa.ForeignKeyConstraint(
            ["case_id", "routine_id"],
            ["care_routine_record.case_id", "care_routine_record.id"],
            name="fk_care_routine_event_routine",
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("routine_id", "occurrence_date", name="uq_care_routine_occurrence"),
        sa.CheckConstraint(
            "status IN ('DONE','NOT_DONE','SKIPPED')",
            name="ck_care_routine_event_status",
        ),
        sa.CheckConstraint(
            "recorded_by_actor_type = 'HUMAN'",
            name="ck_care_routine_event_human_actor",
        ),
        sa.CheckConstraint(
            "length(trim(recorded_by_actor_id)) > 0 AND length(trim(correlation_id)) > 0",
            name="ck_care_routine_event_provenance",
        ),
    )
    op.create_index(
        "ix_care_routine_event_record_case_id",
        "care_routine_event_record",
        ["case_id"],
        unique=False,
    )
    op.create_index(
        "ix_care_routine_event_case_date",
        "care_routine_event_record",
        ["case_id", "occurrence_date", "id"],
        unique=False,
    )
    op.execute(
        "CREATE TRIGGER protect_care_routine_record_history "
        "BEFORE UPDATE OR DELETE ON care_routine_record "
        "FOR EACH ROW EXECUTE FUNCTION nasim_reject_history_change()"
    )
    op.execute(
        "CREATE TRIGGER protect_care_routine_event_history "
        "BEFORE UPDATE OR DELETE ON care_routine_event_record "
        "FOR EACH ROW EXECUTE FUNCTION nasim_reject_history_change()"
    )
    op.execute("REVOKE ALL ON care_routine_record, care_routine_event_record FROM PUBLIC")


def downgrade() -> None:
    connection = op.get_bind()
    occupied = connection.scalar(
        sa.text(
            "SELECT EXISTS(SELECT 1 FROM care_routine_record) OR "
            "EXISTS(SELECT 1 FROM care_routine_event_record)"
        )
    )
    if occupied:
        raise RuntimeError(
            "Care routine history exists; rollback requires an approved lineage recovery plan"
        )
    op.execute("DROP TRIGGER protect_care_routine_event_history ON care_routine_event_record")
    op.execute("DROP TRIGGER protect_care_routine_record_history ON care_routine_record")
    op.drop_table("care_routine_event_record")
    op.drop_table("care_routine_record")
