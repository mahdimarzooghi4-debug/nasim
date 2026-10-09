"""Inert immutable proposed Dataset manifest registry, without runtime write grants.

Revision ID: 0008_learning_manifest
Revises: 0007_referral_follow_up
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0008_learning_manifest"
down_revision: str | Sequence[str] | None = "0007_referral_follow_up"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "learning_proposed_manifest",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("manifest_sha256", sa.String(length=64), nullable=False),
        sa.Column("purpose", sa.String(length=12), nullable=False),
        sa.Column("policy_sha256", sa.String(length=64), nullable=False),
        sa.Column("approval_evidence_sha256", sa.String(length=64), nullable=False),
        sa.Column("source_count", sa.Integer(), nullable=False),
        sa.Column("recorded_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("manifest_sha256", name="uq_learning_manifest_digest"),
        sa.CheckConstraint("purpose IN ('TRAINING', 'EVALUATION')", name="ck_learning_purpose"),
        sa.CheckConstraint("source_count > 0", name="ck_learning_source_count"),
        sa.CheckConstraint(
            "manifest_sha256 ~ '^[0-9a-f]{64}$' "
            "AND policy_sha256 ~ '^[0-9a-f]{64}$' "
            "AND approval_evidence_sha256 ~ '^[0-9a-f]{64}$'",
            name="ck_learning_manifest_digests",
        ),
    )
    op.create_table(
        "learning_proposed_source",
        sa.Column("manifest_id", sa.Uuid(), nullable=False),
        sa.Column("namespace", sa.String(length=80), nullable=False),
        sa.Column("source_id", sa.Uuid(), nullable=False),
        sa.Column("source_version_sha256", sa.String(length=64), nullable=False),
        sa.Column("curation_evidence_sha256", sa.String(length=64), nullable=False),
        sa.PrimaryKeyConstraint("manifest_id", "namespace", "source_id"),
        sa.ForeignKeyConstraint(
            ["manifest_id"], ["learning_proposed_manifest.id"], ondelete="RESTRICT"
        ),
        sa.CheckConstraint(
            "namespace ~ '^[a-z][a-z0-9_.-]{0,79}$'",
            name="ck_learning_source_namespace",
        ),
        sa.CheckConstraint(
            "source_version_sha256 ~ '^[0-9a-f]{64}$' "
            "AND curation_evidence_sha256 ~ '^[0-9a-f]{64}$'",
            name="ck_learning_source_digests",
        ),
    )
    for table in ("learning_proposed_manifest", "learning_proposed_source"):
        op.execute(
            f"CREATE TRIGGER protect_{table}_history "
            f"BEFORE UPDATE OR DELETE ON {table} "
            "FOR EACH ROW EXECUTE FUNCTION nasim_reject_history_change()"
        )
    # Serving role receives neither INSERT nor UPDATE nor DELETE nor TRUNCATE.
    # A future separately approved writer must have its own restricted identity.


def downgrade() -> None:
    conn = op.get_bind()
    populated = conn.scalar(
        sa.text(
            "SELECT EXISTS (SELECT 1 FROM learning_proposed_manifest) OR "
            "EXISTS (SELECT 1 FROM learning_proposed_source)"
        )
    )
    if populated:
        raise RuntimeError(
            "Proposed Dataset lineage exists; rollback requires an approved data plan"
        )
    op.drop_table("learning_proposed_source")
    op.drop_table("learning_proposed_manifest")
