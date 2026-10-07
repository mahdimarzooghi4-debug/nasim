"""Trusted provisioning primitives and a deterministic request-time resolver.

No public management authority is defined. Callers of Provisioning must be vetted
outside this module; ActorContext records provenance, it does not authorize management.
"""

from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import func, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from nasim.authorization.contracts import PERMISSIONS, ROLES, TrustedPrincipal, Window
from nasim.authorization.models import (
    ActorRoleAssignment,
    AuthorizationAudit,
    PermissionDefinition,
    RoleDefinition,
    RolePermissionGrant,
)
from nasim.domain.errors import DomainError
from nasim.identity_context.contracts import ActorContext, ActorType


class AuthorizationResolver:
    def __init__(self, sessions: async_sessionmaker[AsyncSession]):
        self.sessions = sessions

    async def resolve(self, principal: TrustedPrincipal) -> ActorContext:
        async with self.sessions() as session:
            return await self.resolve_in_session(session, principal)

    async def resolve_in_session(
        self, session: AsyncSession, principal: TrustedPrincipal
    ) -> ActorContext:
        # One statement: PostgreSQL snapshot and clock shared across assignments/grants.
        now = func.statement_timestamp()
        query = (
            select(PermissionDefinition.code)
            .distinct()
            .join(
                RolePermissionGrant,
                RolePermissionGrant.permission_revision_id == PermissionDefinition.id,
            )
            .join(
                ActorRoleAssignment,
                ActorRoleAssignment.role_revision_id == RolePermissionGrant.role_revision_id,
            )
            .where(
                ActorRoleAssignment.actor_id == principal.actor_id,
                ActorRoleAssignment.actor_type == principal.actor_type.value,
            )
        )
        for model in (ActorRoleAssignment, RolePermissionGrant):
            query = query.where(
                model.ended_at.is_(None),
                model.starts_at <= now,
                (model.expires_at.is_(None) | (model.expires_at > now)),
            )
        codes = frozenset(await session.scalars(query.order_by(PermissionDefinition.code)))
        # D-0123: AI is not admitted to TS-03 even through an erroneous explicit grant.
        if principal.actor_type == ActorType.AI:
            codes = frozenset()
        return ActorContext(
            actor_id=principal.actor_id,
            actor_type=principal.actor_type,
            correlation_id=principal.correlation_id,
            capabilities=codes,
        )


class Provisioning:
    """Internal-only, transactionally audited writes. Never exposed as an HTTP command."""

    def __init__(self, sessions: async_sessionmaker[AsyncSession]):
        self.sessions = sessions

    @staticmethod
    def _reason(reason: str) -> None:
        if not reason.strip() or len(reason) > 2000:
            raise DomainError("AUTHORIZATION_REASON_REQUIRED", 422)

    @staticmethod
    def _audit(
        session: AsyncSession,
        row,
        actor: ActorContext,
        now: datetime,
        reason: str,
        action: str,
        before: UUID | None = None,
    ) -> None:
        session.add(
            AuthorizationAudit(
                id=uuid4(),
                actor_id=actor.actor_id,
                actor_type=actor.actor_type.value,
                timestamp=now,
                reason=reason,
                correlation_id=actor.correlation_id,
                resource_type=row.__tablename__,
                resource_id=row.id,
                action=action,
                before_reference=before,
                after_reference=row.id,
            )
        )

    async def register(
        self,
        code: str,
        actor: ActorContext,
        reason: str,
        *,
        permission: bool = False,
        expected_id: UUID | None = None,
    ) -> UUID:
        self._reason(reason)
        if code not in (PERMISSIONS if permission else ROLES):
            raise DomainError("UNREGISTERED_AUTHORIZATION_VOCABULARY", 422)
        model = PermissionDefinition if permission else RoleDefinition
        try:
            async with self.sessions() as session, session.begin():
                prior = await session.scalar(
                    select(model)
                    .where(model.code == code)
                    .order_by(model.revision_no.desc())
                    .limit(1)
                    .with_for_update()
                )
                if (prior.id if prior else None) != expected_id:
                    raise DomainError("STALE_AUTHORIZATION_REVISION", 409)
                now = (await session.execute(select(func.statement_timestamp()))).scalar_one()
                row = model(
                    id=uuid4(),
                    code=code,
                    title=code if permission else ROLES[code],
                    revision_no=prior.revision_no + 1 if prior else 1,
                    supersedes_id=prior.id if prior else None,
                    recorded_at=now,
                    recorded_by_actor_id=actor.actor_id,
                    recorded_by_actor_type=actor.actor_type.value,
                    correlation_id=actor.correlation_id,
                    reason=reason,
                )
                session.add(row)
                self._audit(session, row, actor, now, reason, "REGISTERED", expected_id)
                await session.flush()
                return row.id
        except IntegrityError:
            raise DomainError("STALE_AUTHORIZATION_REVISION", 409) from None

    async def grant(
        self, role_id: UUID, permission_id: UUID, window: Window, actor: ActorContext
    ) -> UUID:
        return await self._create(role_id, window, actor, permission_id=permission_id)

    async def assign(
        self, principal: TrustedPrincipal, role_id: UUID, window: Window, actor: ActorContext
    ) -> UUID:
        return await self._create(role_id, window, actor, principal=principal)

    async def _create(
        self,
        role_id: UUID,
        window: Window,
        actor: ActorContext,
        *,
        permission_id: UUID | None = None,
        principal: TrustedPrincipal | None = None,
    ) -> UUID:
        try:
            async with self.sessions() as session, session.begin():
                role = await session.get(RoleDefinition, role_id)
                if role is None:
                    raise DomainError("AUTHORIZATION_DEFINITION_NOT_FOUND", 404)
                now = (await session.execute(select(func.statement_timestamp()))).scalar_one()
                common = dict(
                    id=uuid4(),
                    role_code=role.code,
                    role_revision_id=role.id,
                    starts_at=window.starts_at,
                    expires_at=window.expires_at,
                    recorded_at=now,
                    recorded_by_actor_id=actor.actor_id,
                    recorded_by_actor_type=actor.actor_type.value,
                    reason=window.reason,
                    correlation_id=actor.correlation_id,
                    supersedes_id=window.supersedes_id,
                )
                if principal is not None:
                    row = ActorRoleAssignment(
                        **common, actor_id=principal.actor_id, actor_type=principal.actor_type.value
                    )
                else:
                    permission = await session.get(PermissionDefinition, permission_id)
                    if permission is None:
                        raise DomainError("AUTHORIZATION_DEFINITION_NOT_FOUND", 404)
                    row = RolePermissionGrant(
                        **common,
                        permission_code=permission.code,
                        permission_revision_id=permission.id,
                    )
                session.add(row)
                self._audit(
                    session, row, actor, now, window.reason, "CREATED", window.supersedes_id
                )
                await session.flush()
                return row.id
        except IntegrityError:
            raise DomainError("AUTHORIZATION_CONFLICT", 409) from None

    async def revoke(
        self, resource: str, expected_id: UUID, actor: ActorContext, reason: str
    ) -> None:
        self._reason(reason)
        models = {"grant": RolePermissionGrant, "assignment": ActorRoleAssignment}
        if resource not in models:
            raise DomainError("INVALID_AUTHORIZATION_RESOURCE", 422)
        model = models[resource]
        async with self.sessions() as session, session.begin():
            row = await session.scalar(
                select(model).where(model.id == expected_id).with_for_update()
            )
            if row is None or row.ended_at is not None:
                raise DomainError("STALE_AUTHORIZATION_REVISION", 409)
            now = (await session.execute(select(func.statement_timestamp()))).scalar_one()
            row.ended_at = now
            row.ended_by_actor_id = actor.actor_id
            row.ended_by_actor_type = actor.actor_type.value
            row.end_reason = reason
            row.end_correlation_id = actor.correlation_id
            self._audit(session, row, actor, now, reason, "ENDED", expected_id)
            await session.flush()
