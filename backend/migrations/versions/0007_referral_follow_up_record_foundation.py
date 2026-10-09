"""Immutable human Referral follow-up record foundation.

Revision ID: 0007_referral_follow_up
Revises: 0006_provider_qreview
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0007_referral_follow_up"
down_revision: str | Sequence[str] | None = "0006_provider_qreview"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

PERMISSIONS = (
    (
        "referral.follow_up.record.assigned",
        "73f9a23c-4ebd-4c3a-8e11-4b8d731efc10",
        "1f3a44e0-6bf4-4d43-bd70-8e73919e9a11",
    ),
    (
        "referral.follow_up.read.assigned",
        "49816310-774f-4d79-a536-97a1b61f2a23",
        "f78df08d-ceca-4466-83bb-99067e705127",
    ),
    (
        "referral.follow_up.read.oversight",
        "f70e6198-d7b7-4108-b6c5-ab8aba77d544",
        "3ae86d7b-e302-4471-9f08-f8d455d97d5a",
    ),
)


def upgrade() -> None:
    op.create_table(
        "referral_follow_up_record",
        sa.Column("referral_id", sa.Uuid(), nullable=False),
        sa.Column("recorded_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("recorded_by_actor_id", sa.String(length=200), nullable=False),
        sa.Column("recorded_by_actor_type", sa.String(length=20), nullable=False),
        sa.Column("note", sa.Text(), nullable=False),
        sa.Column("reason", sa.Text(), nullable=False),
        sa.Column("correlation_id", sa.String(length=200), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.CheckConstraint(
            "recorded_by_actor_type = 'HUMAN'", name="ck_referral_follow_up_human"
        ),
        sa.CheckConstraint(
            "note ~ '[^[:space:]]' AND reason ~ '[^[:space:]]' "
            "AND length(trim(recorded_by_actor_id)) > 0 "
            "AND length(trim(correlation_id)) > 0",
            name="ck_referral_follow_up_provenance",
        ),
        sa.ForeignKeyConstraint(["referral_id"], ["referral_record.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        "ix_referral_follow_up_recorded",
        "referral_follow_up_record",
        ["referral_id", "recorded_at", "id"],
    )
    op.execute(
        "CREATE TRIGGER protect_referral_follow_up_history "
        "BEFORE UPDATE OR DELETE ON referral_follow_up_record "
        "FOR EACH ROW EXECUTE FUNCTION nasim_reject_history_change()"
    )
    op.execute("""
        CREATE FUNCTION nasim_referral_follow_up_effects_guard()
        RETURNS trigger LANGUAGE plpgsql AS $$
        DECLARE referral_case UUID;
        BEGIN
          SELECT r.case_id INTO referral_case
          FROM referral_record r WHERE r.id=NEW.referral_id;
          IF referral_case IS NULL OR NEW.recorded_by_actor_type <> 'HUMAN' THEN
            RAISE EXCEPTION 'Invalid human Referral follow-up source'
              USING ERRCODE='23514';
          END IF;
          IF NOT EXISTS (
              SELECT 1 FROM audit_entry a
              WHERE a.case_id=referral_case
                AND a.action='referral.follow_up_recorded.v1'
                AND a.resource_type='referral_follow_up_record'
                AND a.resource_id=NEW.id AND a.after_reference=NEW.id
                AND a.before_reference=NEW.referral_id
                AND a.actor_id=NEW.recorded_by_actor_id
                AND a.actor_type=NEW.recorded_by_actor_type
                AND a.timestamp=NEW.recorded_at
                AND a.reason=NEW.reason
                AND a.correlation_id=NEW.correlation_id
          ) OR NOT EXISTS (
              SELECT 1 FROM outbox_event e
              WHERE e.case_id=referral_case
                AND e.event_type='referral.follow_up_recorded.v1'
                AND e.occurred_at=NEW.recorded_at
                AND e.payload->>'follow_up_record_id'=NEW.id::text
                AND e.payload->>'referral_id'=NEW.referral_id::text
                AND e.payload->>'case_id'=referral_case::text
                AND e.payload->>'actor_id'=NEW.recorded_by_actor_id
                AND e.payload->>'actor_type'=NEW.recorded_by_actor_type
                AND e.payload->>'correlation_id'=NEW.correlation_id
                AND NOT (e.payload ?| ARRAY['note','reason','content'])
          ) OR NOT EXISTS (
              SELECT 1 FROM idempotency_record i
              WHERE i.actor_id=NEW.recorded_by_actor_id
                AND i.operation='referral.follow_up.record.HUMAN'
                AND i.target=NEW.referral_id::text
                AND i.created_at=NEW.recorded_at
                AND i.response->>'id'=NEW.id::text
                AND i.response->>'referral_id'=NEW.referral_id::text
          ) THEN
            RAISE EXCEPTION 'Atomic Referral follow-up effects required'
              USING ERRCODE='23514';
          END IF;
          RETURN NULL;
        END $$
    """)
    op.execute(
        "CREATE CONSTRAINT TRIGGER require_referral_follow_up_effects "
        "AFTER INSERT ON referral_follow_up_record DEFERRABLE INITIALLY DEFERRED "
        "FOR EACH ROW EXECUTE FUNCTION nasim_referral_follow_up_effects_guard()"
    )
    connection = op.get_bind()
    for code, identifier, audit_id in PERMISSIONS:
        connection.execute(
            sa.text("""
                INSERT INTO permission_definition (
                  id,code,title,revision_no,recorded_at,
                  recorded_by_actor_id,recorded_by_actor_type,correlation_id,reason
                ) VALUES (
                  :id,:code,:code,1,transaction_timestamp(),
                  'schema-migration','SYSTEM','0007_referral_follow_up',
                  'Technical Follow-up vocabulary only; no role mapping'
                )
            """),
            {"id": identifier, "code": code},
        )
        connection.execute(
            sa.text("""
                INSERT INTO authorization_audit (
                  id,actor_id,actor_type,timestamp,reason,correlation_id,
                  resource_type,resource_id,action,before_reference,after_reference
                ) VALUES (
                  :audit_id,'schema-migration','SYSTEM',transaction_timestamp(),
                  'Technical Follow-up vocabulary only; no role mapping',
                  '0007_referral_follow_up','permission_definition',:id,
                  'REGISTERED',NULL,:id
                )
            """),
            {"audit_id": audit_id, "id": identifier},
        )


def downgrade() -> None:
    connection = op.get_bind()
    used = connection.scalar(
        sa.text("""
            SELECT EXISTS(SELECT 1 FROM referral_follow_up_record) OR EXISTS(
              SELECT 1 FROM role_permission_grant g
              JOIN permission_definition p ON p.id=g.permission_revision_id
              WHERE p.code LIKE 'referral.follow_up.%'
            ) OR EXISTS(
              SELECT 1 FROM permission_definition
              WHERE code LIKE 'referral.follow_up.%' AND revision_no > 1
            )
        """)
    )
    if used:
        raise RuntimeError(
            "Referral follow-up data or authorization history requires "
            "an approved rollback data plan"
        )
    op.execute("ALTER TABLE permission_definition DISABLE TRIGGER protect_auth_history")
    op.execute("ALTER TABLE authorization_audit DISABLE TRIGGER protect_auth_history")
    for _code, identifier, audit_id in PERMISSIONS:
        connection.execute(
            sa.text("DELETE FROM authorization_audit WHERE id=:id"), {"id": audit_id}
        )
        connection.execute(
            sa.text("DELETE FROM permission_definition WHERE id=:id"), {"id": identifier}
        )
    op.execute("ALTER TABLE permission_definition ENABLE TRIGGER protect_auth_history")
    op.execute("ALTER TABLE authorization_audit ENABLE TRIGGER protect_auth_history")
    op.drop_index("ix_referral_follow_up_recorded", table_name="referral_follow_up_record")
    op.drop_table("referral_follow_up_record")
    op.execute("DROP FUNCTION nasim_referral_follow_up_effects_guard()")
