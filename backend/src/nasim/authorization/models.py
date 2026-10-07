"""Relational authorization history; separate from Case ownership and authentication."""

from datetime import datetime
from uuid import UUID

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKeyConstraint,
    Index,
    Integer,
    String,
    Text,
    UniqueConstraint,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column

from nasim.infrastructure.models import Base, Identified


class AuthProvenance:
    recorded_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    recorded_by_actor_id: Mapped[str] = mapped_column(String(200))
    recorded_by_actor_type: Mapped[str] = mapped_column(String(20))
    correlation_id: Mapped[str] = mapped_column(String(200))
    reason: Mapped[str] = mapped_column(Text)


def provenance_checks(prefix: str):
    return (
        CheckConstraint(
            "recorded_by_actor_type IN ('HUMAN','SYSTEM','AI','AUTOMATION')",
            name=f"ck_{prefix}_actor",
        ),
        CheckConstraint(
            "length(trim(reason)) > 0 AND length(trim(correlation_id)) > 0 AND"
            " length(trim(recorded_by_actor_id)) > 0",
            name=f"ck_{prefix}_provenance",
        ),
    )


class RoleDefinition(Identified, AuthProvenance, Base):
    __tablename__ = "role_definition"
    code: Mapped[str] = mapped_column(String(100))
    title: Mapped[str] = mapped_column(String(200))
    revision_no: Mapped[int] = mapped_column(Integer)
    supersedes_id: Mapped[UUID | None]
    __table_args__ = (
        UniqueConstraint("code", "revision_no", name="uq_role_definition_version"),
        UniqueConstraint("code", "id", name="uq_role_definition_lineage"),
        UniqueConstraint("supersedes_id", name="uq_role_definition_successor"),
        ForeignKeyConstraint(
            ["code", "supersedes_id"],
            ["role_definition.code", "role_definition.id"],
            name="fk_role_definition_lineage",
        ),
        CheckConstraint(
            "(revision_no = 1 AND supersedes_id IS NULL) OR (revision_no > 1 A"
            "ND supersedes_id IS NOT NULL)",
            name="ck_role_definition_version",
        ),
        CheckConstraint(
            "length(trim(code)) > 0 AND position('*' in code) = 0 AND length(trim(title)) > 0",
            name="ck_role_definition_code",
        ),
        *provenance_checks("role_definition"),
    )


class PermissionDefinition(Identified, AuthProvenance, Base):
    __tablename__ = "permission_definition"
    code: Mapped[str] = mapped_column(String(100))
    title: Mapped[str] = mapped_column(String(200))
    revision_no: Mapped[int] = mapped_column(Integer)
    supersedes_id: Mapped[UUID | None]
    __table_args__ = (
        UniqueConstraint("code", "revision_no", name="uq_permission_definition_version"),
        UniqueConstraint("code", "id", name="uq_permission_definition_lineage"),
        UniqueConstraint("supersedes_id", name="uq_permission_definition_successor"),
        ForeignKeyConstraint(
            ["code", "supersedes_id"],
            ["permission_definition.code", "permission_definition.id"],
            name="fk_permission_definition_lineage",
        ),
        CheckConstraint(
            "(revision_no = 1 AND supersedes_id IS NULL) OR (revision_no > 1 A"
            "ND supersedes_id IS NOT NULL)",
            name="ck_permission_definition_version",
        ),
        CheckConstraint(
            "length(trim(code)) > 0 AND position('*' in code) = 0 AND length(trim(title)) > 0",
            name="ck_permission_definition_code",
        ),
        *provenance_checks("permission_definition"),
    )


class TemporalAuth(AuthProvenance):
    starts_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    expires_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    ended_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    ended_by_actor_id: Mapped[str | None] = mapped_column(String(200))
    ended_by_actor_type: Mapped[str | None] = mapped_column(String(20))
    end_reason: Mapped[str | None] = mapped_column(Text)
    end_correlation_id: Mapped[str | None] = mapped_column(String(200))
    supersedes_id: Mapped[UUID | None]


def temporal_checks(prefix: str):
    return (
        *provenance_checks(prefix),
        CheckConstraint("expires_at IS NULL OR expires_at > starts_at", name=f"ck_{prefix}_window"),
        CheckConstraint(
            "(ended_at IS NULL AND ended_by_actor_id IS NULL AND ended_by_acto"
            "r_type IS NULL AND end_reason IS NULL AND end_correlation_id IS N"
            "ULL) OR (ended_at >= recorded_at AND ended_by_actor_id IS NOT NUL"
            "L AND length(trim(ended_by_actor_id)) > 0 AND ended_by_actor_type"
            " IN ('HUMAN','SYSTEM','AI','AUTOMATION') AND end_reason IS NOT NU"
            "LL AND length(trim(end_reason)) > 0 AND end_correlation_id IS NOT"
            " NULL AND length(trim(end_correlation_id)) > 0)",
            name=f"ck_{prefix}_end",
        ),
    )


class RolePermissionGrant(Identified, TemporalAuth, Base):
    __tablename__ = "role_permission_grant"
    role_code: Mapped[str] = mapped_column(String(100))
    role_revision_id: Mapped[UUID]
    permission_code: Mapped[str] = mapped_column(String(100))
    permission_revision_id: Mapped[UUID]
    __table_args__ = (
        ForeignKeyConstraint(
            ["role_code", "role_revision_id"],
            ["role_definition.code", "role_definition.id"],
            name="fk_grant_role",
        ),
        ForeignKeyConstraint(
            ["permission_code", "permission_revision_id"],
            ["permission_definition.code", "permission_definition.id"],
            name="fk_grant_permission",
        ),
        UniqueConstraint("role_code", "permission_code", "id", name="uq_grant_lineage"),
        ForeignKeyConstraint(
            ["role_code", "permission_code", "supersedes_id"],
            [
                "role_permission_grant.role_code",
                "role_permission_grant.permission_code",
                "role_permission_grant.id",
            ],
            name="fk_grant_lineage",
        ),
        UniqueConstraint("supersedes_id", name="uq_grant_successor"),
        Index(
            "uq_grant_active",
            "role_code",
            "permission_code",
            unique=True,
            postgresql_where=text("ended_at IS NULL"),
        ),
        *temporal_checks("grant"),
    )


class ActorRoleAssignment(Identified, TemporalAuth, Base):
    __tablename__ = "actor_role_assignment"
    actor_id: Mapped[str] = mapped_column(String(200))
    actor_type: Mapped[str] = mapped_column(String(20))
    role_code: Mapped[str] = mapped_column(String(100))
    role_revision_id: Mapped[UUID]
    __table_args__ = (
        ForeignKeyConstraint(
            ["role_code", "role_revision_id"],
            ["role_definition.code", "role_definition.id"],
            name="fk_actor_role",
        ),
        UniqueConstraint("actor_id", "actor_type", "role_code", "id", name="uq_actor_role_lineage"),
        ForeignKeyConstraint(
            ["actor_id", "actor_type", "role_code", "supersedes_id"],
            [
                "actor_role_assignment.actor_id",
                "actor_role_assignment.actor_type",
                "actor_role_assignment.role_code",
                "actor_role_assignment.id",
            ],
            name="fk_actor_role_lineage",
        ),
        UniqueConstraint("supersedes_id", name="uq_actor_role_successor"),
        Index(
            "uq_actor_role_active",
            "actor_id",
            "actor_type",
            "role_code",
            unique=True,
            postgresql_where=text("ended_at IS NULL"),
        ),
        CheckConstraint(
            "actor_type IN ('HUMAN','SYSTEM','AI','AUTOMATION') AND length(trim(actor_id)) > 0",
            name="ck_actor_role_identity",
        ),
        *temporal_checks("actor_role"),
    )


class AuthorizationAudit(Identified, Base):
    __tablename__ = "authorization_audit"
    actor_id: Mapped[str] = mapped_column(String(200))
    actor_type: Mapped[str] = mapped_column(String(20))
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    reason: Mapped[str] = mapped_column(Text)
    correlation_id: Mapped[str] = mapped_column(String(200))
    resource_type: Mapped[str] = mapped_column(String(100))
    resource_id: Mapped[UUID]
    action: Mapped[str] = mapped_column(String(20))
    before_reference: Mapped[UUID | None]
    after_reference: Mapped[UUID]
    __table_args__ = (
        CheckConstraint(
            "actor_type IN ('HUMAN','SYSTEM','AI','AUTOMATION')",
            name="ck_authorization_audit_actor",
        ),
        CheckConstraint(
            "length(trim(actor_id)) > 0 AND length(trim(reason)) > 0 AND lengt"
            "h(trim(correlation_id)) > 0",
            name="ck_authorization_audit_provenance",
        ),
        CheckConstraint(
            "action IN ('REGISTERED','CREATED','ENDED')", name="ck_authorization_audit_action"
        ),
        UniqueConstraint(
            "resource_type", "resource_id", "action", name="uq_authorization_audit_event"
        ),
    )
