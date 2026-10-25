"""Immutable cross-manifest source purpose claim: exact identity exclusion only.

Revision ID: 0009_learning_partition_claim
Revises: 0008_learning_manifest

No household, consent, preparation, training or evaluation policy is inferred.
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0009_learning_partition_claim"
down_revision: str | Sequence[str] | None = "0008_learning_manifest"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    connection = op.get_bind()
    # Existing, conflicting proposed metadata cannot be silently grandfathered
    # into a stronger invariant. This fails closed before schema modification.
    conflict = connection.scalar(
        sa.text(
            "SELECT EXISTS("
            " SELECT 1 FROM learning_proposed_source AS s "
            " JOIN learning_proposed_manifest AS m ON m.id=s.manifest_id "
            " GROUP BY s.namespace,s.source_id "
            " HAVING COUNT(DISTINCT m.purpose)>1)"
        )
    )
    if conflict:
        raise RuntimeError(
            "Existing proposed source identities cross Training/Evaluation partitions; "
            "migration requires a separately approved reconciliation"
        )

    op.create_table(
        "learning_source_purpose_claim",
        sa.Column("namespace", sa.String(length=80), nullable=False),
        sa.Column("source_id", sa.Uuid(), nullable=False),
        sa.Column("purpose", sa.String(length=12), nullable=False),
        sa.PrimaryKeyConstraint("namespace", "source_id"),
        sa.CheckConstraint(
            "namespace ~ '^[a-z][a-z0-9_.-]{0,79}$'",
            name="ck_learning_partition_source_namespace",
        ),
        sa.CheckConstraint(
            "purpose IN ('TRAINING', 'EVALUATION')",
            name="ck_learning_partition_purpose",
        ),
    )
    op.execute(
        "INSERT INTO learning_source_purpose_claim (namespace,source_id,purpose) "
        "SELECT DISTINCT s.namespace,s.source_id,m.purpose "
        "FROM learning_proposed_source AS s "
        "JOIN learning_proposed_manifest AS m ON m.id=s.manifest_id"
    )
    op.execute(
        "CREATE TRIGGER protect_learning_partition_claim_history "
        "BEFORE UPDATE OR DELETE ON learning_source_purpose_claim "
        "FOR EACH ROW EXECUTE FUNCTION nasim_reject_history_change()"
    )
    op.execute("""
        CREATE FUNCTION nasim_learning_claim_source_purpose()
        RETURNS trigger LANGUAGE plpgsql AS $$
        DECLARE
            requested_purpose VARCHAR(12);
            claimed_purpose VARCHAR(12);
        BEGIN
            SELECT purpose INTO requested_purpose
              FROM learning_proposed_manifest WHERE id=NEW.manifest_id;
            IF requested_purpose IS NULL THEN
                RAISE EXCEPTION 'LEARNING_SOURCE_PARENT_NOT_FOUND'
                  USING ERRCODE='23503';
            END IF;
            -- UNIQUE(namespace,source_id) is a concurrent-transaction fence;
            -- no mutable/updatable claim row is required to support same-purpose
            -- replays or revised source versions.
            INSERT INTO learning_source_purpose_claim(namespace,source_id,purpose)
            VALUES (NEW.namespace,NEW.source_id,requested_purpose)
            ON CONFLICT(namespace,source_id) DO NOTHING;
            SELECT purpose INTO claimed_purpose
              FROM learning_source_purpose_claim
              WHERE namespace=NEW.namespace AND source_id=NEW.source_id;
            IF claimed_purpose IS DISTINCT FROM requested_purpose THEN
                RAISE EXCEPTION 'LEARNING_SOURCE_PARTITION_CONFLICT'
                  USING ERRCODE='23514';
            END IF;
            RETURN NEW;
        END
        $$
    """)
    op.execute(
        "CREATE TRIGGER claim_learning_source_purpose "
        "BEFORE INSERT ON learning_proposed_source "
        "FOR EACH ROW EXECUTE FUNCTION nasim_learning_claim_source_purpose()"
    )
    op.execute("REVOKE ALL ON learning_source_purpose_claim FROM PUBLIC")


def downgrade() -> None:
    connection = op.get_bind()
    if connection.scalar(sa.text("SELECT EXISTS(SELECT 1 FROM learning_source_purpose_claim)")):
        raise RuntimeError(
            "Source partition claims exist; rollback requires an approved lineage recovery plan"
        )
    op.execute("DROP TRIGGER claim_learning_source_purpose ON learning_proposed_source")
    op.execute("DROP FUNCTION nasim_learning_claim_source_purpose()")
    op.drop_table("learning_source_purpose_claim")
