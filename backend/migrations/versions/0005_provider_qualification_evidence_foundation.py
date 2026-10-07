"""Provider Qualification Evidence foundation

Revision ID: 0005_provider_qe
Revises: 0004_provider_candidate
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0005_provider_qe"
down_revision: str | Sequence[str] | None = "0004_provider_candidate"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.drop_constraint("ck_audit_case_or_provider_candidate", "audit_entry", type_="check")
    op.drop_constraint("ck_outbox_case_or_provider_candidate", "outbox_event", type_="check")
    op.create_check_constraint(
        "ck_audit_case_or_provider_candidate",
        "audit_entry",
        "case_id IS NOT NULL OR "
        "(action = 'provider.candidate_registered.v1' "
        "AND resource_type = 'provider_candidate_record') OR "
        "(action = 'provider.qualification_evidence_recorded.v1' "
        "AND resource_type = 'provider_qualification_evidence_record')",
    )
    op.create_check_constraint(
        "ck_outbox_case_or_provider_candidate",
        "outbox_event",
        "case_id IS NOT NULL OR event_type IN "
        "('provider.candidate_registered.v1', "
        "'provider.qualification_evidence_recorded.v1')",
    )

    op.create_table(
        "provider_qualification_evidence_record",
        sa.Column("provider_candidate_id", sa.Uuid(), nullable=False),
        sa.Column("evidence_label", sa.Text(), nullable=False),
        sa.Column("evidence_reference", sa.Text(), nullable=False),
        sa.Column("recorded_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("recorded_by_actor_id", sa.String(length=200), nullable=False),
        sa.Column("recorded_by_actor_type", sa.String(length=20), nullable=False),
        sa.Column("reason", sa.Text(), nullable=False),
        sa.Column("correlation_id", sa.String(length=200), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.CheckConstraint(
            "recorded_by_actor_type IN ('HUMAN','SYSTEM','AI','AUTOMATION')",
            name="ck_provider_qualification_evidence_actor_type",
        ),
        sa.CheckConstraint(
            "evidence_label ~ '[^[:space:]]' "
            "AND evidence_reference ~ '[^[:space:]]' "
            "AND reason ~ '[^[:space:]]' "
            "AND length(trim(recorded_by_actor_id)) > 0 "
            "AND length(trim(correlation_id)) > 0",
            name="ck_provider_qualification_evidence_provenance",
        ),
        sa.ForeignKeyConstraint(
            ["provider_candidate_id"],
            ["provider_candidate_record.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        "ix_provider_qualification_evidence_record_provider_candidate_id",
        "provider_qualification_evidence_record",
        ["provider_candidate_id"],
        unique=False,
    )
    op.create_index(
        "ix_provider_qualification_evidence_recorded",
        "provider_qualification_evidence_record",
        ["provider_candidate_id", "recorded_at", "id"],
        unique=False,
    )
    op.execute(
        "CREATE TRIGGER protect_provider_qualification_evidence_history "
        "BEFORE UPDATE OR DELETE ON provider_qualification_evidence_record "
        "FOR EACH ROW EXECUTE FUNCTION nasim_reject_history_change()"
    )

    op.execute("""
        CREATE FUNCTION nasim_provider_qualification_evidence_effects_guard()
        RETURNS trigger LANGUAGE plpgsql AS $$
        BEGIN
          IF NEW.recorded_by_actor_type = 'AI' THEN
            RAISE EXCEPTION 'AI Provider Qualification Evidence recording is not admitted'
              USING ERRCODE='42501';
          END IF;
          IF NOT EXISTS (
              SELECT 1 FROM audit_entry a
              WHERE a.case_id IS NULL
                AND a.action='provider.qualification_evidence_recorded.v1'
                AND a.resource_type='provider_qualification_evidence_record'
                AND a.resource_id=NEW.id
                AND a.after_reference=NEW.id
                AND a.before_reference IS NULL
                AND a.actor_id=NEW.recorded_by_actor_id
                AND a.actor_type=NEW.recorded_by_actor_type
                AND a.timestamp=NEW.recorded_at
                AND a.reason=NEW.reason
                AND a.correlation_id=NEW.correlation_id
          ) OR NOT EXISTS (
              SELECT 1 FROM outbox_event e
              WHERE e.case_id IS NULL
                AND e.event_type='provider.qualification_evidence_recorded.v1'
                AND e.occurred_at=NEW.recorded_at
                AND e.payload->>'provider_qualification_evidence_id'=NEW.id::text
                AND e.payload->>'provider_candidate_id'=NEW.provider_candidate_id::text
                AND e.payload->>'actor_id'=NEW.recorded_by_actor_id
                AND e.payload->>'actor_type'=NEW.recorded_by_actor_type
                AND e.payload->>'correlation_id'=NEW.correlation_id
                AND NOT (e.payload ? 'evidence_label')
                AND NOT (e.payload ? 'evidence_reference')
          ) OR NOT EXISTS (
              SELECT 1 FROM idempotency_record i
              WHERE i.actor_id=NEW.recorded_by_actor_id
                AND i.operation='provider.qualification_evidence.record.' ||
                    NEW.recorded_by_actor_type
                AND i.target=NEW.provider_candidate_id::text
                AND i.created_at=NEW.recorded_at
                AND i.response->>'id'=NEW.id::text
                AND i.response->>'provider_candidate_id'=NEW.provider_candidate_id::text
          ) THEN
            RAISE EXCEPTION 'Atomic Provider Qualification Evidence effects required'
              USING ERRCODE='23514';
          END IF;
          RETURN NULL;
        END $$
    """)
    op.execute(
        "CREATE CONSTRAINT TRIGGER require_provider_qualification_evidence_effects "
        "AFTER INSERT ON provider_qualification_evidence_record "
        "DEFERRABLE INITIALLY DEFERRED FOR EACH ROW "
        "EXECUTE FUNCTION nasim_provider_qualification_evidence_effects_guard()"
    )

    registry = [
        (
            "provider_qualification_evidence.record",
            "ec18a841-6a7b-5597-ba56-e7ea9f8ba892",
            "b4db3fa3-6625-5935-ad05-19373fad76af",
        ),
        (
            "provider_qualification_evidence.read",
            "fb34d52a-3e7e-50cb-9538-66af553215a8",
            "18a6b7d7-1be3-566c-b950-7986aa766313",
        ),
    ]
    connection = op.get_bind()
    for code, identifier, audit_id in registry:
        connection.execute(
            sa.text("""
              INSERT INTO permission_definition (
                id, code, title, revision_no, recorded_at, recorded_by_actor_id,
                recorded_by_actor_type, correlation_id, reason
              )
              VALUES (
                :id, :code, :code, 1, transaction_timestamp(), 'schema-migration',
                'SYSTEM', '0005_provider_qe',
                'Technical Provider Qualification Evidence vocabulary only; no role mapping'
              )
            """),
            {"id": identifier, "code": code},
        )
        connection.execute(
            sa.text("""
              INSERT INTO authorization_audit (
                id, actor_id, actor_type, timestamp, reason, correlation_id,
                resource_type, resource_id, action, before_reference, after_reference
              )
              VALUES (
                :audit_id, 'schema-migration', 'SYSTEM', transaction_timestamp(),
                'Technical Provider Qualification Evidence vocabulary only; no role mapping',
                '0005_provider_qe', 'permission_definition', :id,
                'REGISTERED', NULL, :id
              )
            """),
            {"audit_id": audit_id, "id": identifier},
        )


def downgrade() -> None:
    connection = op.get_bind()
    used = connection.scalar(
        sa.text("""
          SELECT EXISTS(SELECT 1 FROM provider_qualification_evidence_record)
          OR EXISTS(
              SELECT 1 FROM role_permission_grant g
              JOIN permission_definition p ON p.id=g.permission_revision_id
              WHERE p.code LIKE 'provider_qualification_evidence.%'
          )
          OR EXISTS(
              SELECT 1 FROM permission_definition
              WHERE code LIKE 'provider_qualification_evidence.%' AND revision_no > 1
          )
        """)
    )
    if used:
        raise RuntimeError(
            "Provider Qualification Evidence data/authorization history requires "
            "an approved rollback data plan"
        )

    op.execute("ALTER TABLE permission_definition DISABLE TRIGGER protect_auth_history")
    op.execute("ALTER TABLE authorization_audit DISABLE TRIGGER protect_auth_history")
    for _code, identifier, audit_id in [
        (
            "provider_qualification_evidence.record",
            "ec18a841-6a7b-5597-ba56-e7ea9f8ba892",
            "b4db3fa3-6625-5935-ad05-19373fad76af",
        ),
        (
            "provider_qualification_evidence.read",
            "fb34d52a-3e7e-50cb-9538-66af553215a8",
            "18a6b7d7-1be3-566c-b950-7986aa766313",
        ),
    ]:
        connection.execute(
            sa.text("DELETE FROM authorization_audit WHERE id=:id"), {"id": audit_id}
        )
        connection.execute(
            sa.text("DELETE FROM permission_definition WHERE id=:id"), {"id": identifier}
        )
    op.execute("ALTER TABLE permission_definition ENABLE TRIGGER protect_auth_history")
    op.execute("ALTER TABLE authorization_audit ENABLE TRIGGER protect_auth_history")

    op.drop_index(
        "ix_provider_qualification_evidence_recorded",
        table_name="provider_qualification_evidence_record",
    )
    op.drop_index(
        "ix_provider_qualification_evidence_record_provider_candidate_id",
        table_name="provider_qualification_evidence_record",
    )
    op.drop_table("provider_qualification_evidence_record")
    op.execute("DROP FUNCTION nasim_provider_qualification_evidence_effects_guard()")

    op.drop_constraint(
        "ck_audit_case_or_provider_candidate", "audit_entry", type_="check"
    )
    op.drop_constraint(
        "ck_outbox_case_or_provider_candidate", "outbox_event", type_="check"
    )
    op.create_check_constraint(
        "ck_audit_case_or_provider_candidate",
        "audit_entry",
        "case_id IS NOT NULL OR "
        "(action = 'provider.candidate_registered.v1' "
        "AND resource_type = 'provider_candidate_record')",
    )
    op.create_check_constraint(
        "ck_outbox_case_or_provider_candidate",
        "outbox_event",
        "case_id IS NOT NULL OR event_type = 'provider.candidate_registered.v1'",
    )
