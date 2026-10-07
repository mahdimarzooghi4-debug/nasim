"""Provider Candidate registry foundation

Revision ID: 0004_provider_candidate
Revises: 0003_referral
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0004_provider_candidate"
down_revision: str | Sequence[str] | None = "0003_referral"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # Shared technical effects are allowed to represent non-Case bounded contexts.
    op.alter_column("audit_entry", "case_id", existing_type=sa.Uuid(), nullable=True)
    op.alter_column("outbox_event", "case_id", existing_type=sa.Uuid(), nullable=True)
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

    op.create_table(
        "provider_candidate_record",
        sa.Column("display_name", sa.Text(), nullable=False),
        sa.Column("registered_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("registered_by_actor_id", sa.String(length=200), nullable=False),
        sa.Column("registered_by_actor_type", sa.String(length=20), nullable=False),
        sa.Column("reason", sa.Text(), nullable=False),
        sa.Column("correlation_id", sa.String(length=200), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.CheckConstraint(
            "registered_by_actor_type IN ('HUMAN','SYSTEM','AI','AUTOMATION')",
            name="ck_provider_candidate_actor_type",
        ),
        sa.CheckConstraint(
            "display_name ~ '[^[:space:]]' AND reason ~ '[^[:space:]]' "
            "AND length(trim(registered_by_actor_id)) > 0 "
            "AND length(trim(correlation_id)) > 0",
            name="ck_provider_candidate_provenance",
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        "ix_provider_candidate_registered",
        "provider_candidate_record",
        ["registered_at", "id"],
        unique=False,
    )
    op.execute(
        "CREATE TRIGGER protect_provider_candidate_history "
        "BEFORE UPDATE OR DELETE ON provider_candidate_record "
        "FOR EACH ROW EXECUTE FUNCTION nasim_reject_history_change()"
    )

    op.execute("""
        CREATE FUNCTION nasim_provider_candidate_effects_guard()
        RETURNS trigger LANGUAGE plpgsql AS $$
        BEGIN
          IF NEW.registered_by_actor_type = 'AI' THEN
            RAISE EXCEPTION 'AI Provider Candidate registration is not admitted'
              USING ERRCODE='42501';
          END IF;
          IF NOT EXISTS (
              SELECT 1 FROM audit_entry a
              WHERE a.case_id IS NULL
                AND a.action='provider.candidate_registered.v1'
                AND a.resource_type='provider_candidate_record'
                AND a.resource_id=NEW.id
                AND a.after_reference=NEW.id
                AND a.before_reference IS NULL
                AND a.actor_id=NEW.registered_by_actor_id
                AND a.actor_type=NEW.registered_by_actor_type
                AND a.timestamp=NEW.registered_at
                AND a.reason=NEW.reason
                AND a.correlation_id=NEW.correlation_id
          ) OR NOT EXISTS (
              SELECT 1 FROM outbox_event e
              WHERE e.case_id IS NULL
                AND e.event_type='provider.candidate_registered.v1'
                AND e.occurred_at=NEW.registered_at
                AND e.payload->>'provider_candidate_id'=NEW.id::text
                AND e.payload->>'actor_id'=NEW.registered_by_actor_id
                AND e.payload->>'actor_type'=NEW.registered_by_actor_type
                AND e.payload->>'correlation_id'=NEW.correlation_id
                AND NOT (e.payload ? 'display_name')
          ) OR NOT EXISTS (
              SELECT 1 FROM idempotency_record i
              WHERE i.actor_id=NEW.registered_by_actor_id
                AND i.operation='provider.candidate.register.' || NEW.registered_by_actor_type
                AND i.target='provider-candidate'
                AND i.created_at=NEW.registered_at
                AND i.response->>'id'=NEW.id::text
          ) THEN
            RAISE EXCEPTION 'Atomic Provider Candidate effects required'
              USING ERRCODE='23514';
          END IF;
          RETURN NULL;
        END $$
    """)
    op.execute(
        "CREATE CONSTRAINT TRIGGER require_provider_candidate_effects "
        "AFTER INSERT ON provider_candidate_record "
        "DEFERRABLE INITIALLY DEFERRED FOR EACH ROW "
        "EXECUTE FUNCTION nasim_provider_candidate_effects_guard()"
    )

    registry = [
        (
            "provider_candidate.register",
            "de7eeffb-97b1-5a78-9700-adbe622fe722",
            "e1251236-fbf1-5fdd-ba8f-7e7b0c330c68",
        ),
        (
            "provider_candidate.read",
            "59006d99-4dce-55c5-9037-a780ad4dc68b",
            "50458c0e-a2d1-5bde-8ce2-a21ff8e34fb2",
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
                'SYSTEM', '0004_provider_candidate',
                'Technical Provider Candidate vocabulary only; no role mapping'
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
                'Technical Provider Candidate vocabulary only; no role mapping',
                '0004_provider_candidate', 'permission_definition', :id,
                'REGISTERED', NULL, :id
              )
            """),
            {"audit_id": audit_id, "id": identifier},
        )


def downgrade() -> None:
    connection = op.get_bind()
    used = connection.scalar(
        sa.text("""
          SELECT EXISTS(SELECT 1 FROM provider_candidate_record)
          OR EXISTS(
              SELECT 1 FROM role_permission_grant g
              JOIN permission_definition p ON p.id=g.permission_revision_id
              WHERE p.code LIKE 'provider_candidate.%'
          )
          OR EXISTS(
              SELECT 1 FROM permission_definition
              WHERE code LIKE 'provider_candidate.%' AND revision_no > 1
          )
        """)
    )
    if used:
        raise RuntimeError(
            "Provider Candidate data/authorization history requires an approved rollback data plan"
        )

    op.execute("ALTER TABLE permission_definition DISABLE TRIGGER protect_auth_history")
    op.execute("ALTER TABLE authorization_audit DISABLE TRIGGER protect_auth_history")
    for _code, identifier, audit_id in [
        (
            "provider_candidate.register",
            "de7eeffb-97b1-5a78-9700-adbe622fe722",
            "e1251236-fbf1-5fdd-ba8f-7e7b0c330c68",
        ),
        (
            "provider_candidate.read",
            "59006d99-4dce-55c5-9037-a780ad4dc68b",
            "50458c0e-a2d1-5bde-8ce2-a21ff8e34fb2",
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

    op.drop_index("ix_provider_candidate_registered", table_name="provider_candidate_record")
    op.drop_table("provider_candidate_record")
    op.execute("DROP FUNCTION nasim_provider_candidate_effects_guard()")

    op.drop_constraint(
        "ck_outbox_case_or_provider_candidate", "outbox_event", type_="check"
    )
    op.drop_constraint(
        "ck_audit_case_or_provider_candidate", "audit_entry", type_="check"
    )
    op.alter_column("outbox_event", "case_id", existing_type=sa.Uuid(), nullable=False)
    op.alter_column("audit_entry", "case_id", existing_type=sa.Uuid(), nullable=False)
