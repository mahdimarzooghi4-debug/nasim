"""Real PostgreSQL authorization semantics, races, provenance and trust-boundary tests."""

import asyncio
import os
from datetime import UTC, datetime, timedelta
from uuid import uuid4

import httpx
import pytest
from pydantic import PostgresDsn, ValidationError
from sqlalchemy import func, select, text
from sqlalchemy.exc import DBAPIError

from nasim.api.app import create_app
from nasim.authorization.contracts import PERMISSIONS, ROLES, TrustedPrincipal, Window
from nasim.authorization.models import (
    ActorRoleAssignment,
    AuthorizationAudit,
    PermissionDefinition,
    RoleDefinition,
    RolePermissionGrant,
)
from nasim.authorization.service import AuthorizationResolver, Provisioning
from nasim.domain.contracts import CreateCase
from nasim.domain.errors import DomainError
from nasim.identity_context.contracts import ActorContext, ActorType
from nasim.infrastructure.config import Settings
from nasim.infrastructure.database import make_sessions

pytestmark = pytest.mark.integration


@pytest.fixture
async def auth(admin_engine, manager):
    async with admin_engine.begin() as connection:
        await connection.execute(
            text("TRUNCATE actor_role_assignment, role_permission_grant, authorization_audit")
        )
    sessions = make_sessions(admin_engine)
    return Provisioning(sessions), AuthorizationResolver(sessions), sessions


async def definition(sessions, code, permission=False):
    model = PermissionDefinition if permission else RoleDefinition
    async with sessions() as session:
        result = await session.scalar(
            select(model.id).where(model.code == code, model.revision_no == 1)
        )
        assert result is not None
        return result


def principal(actor_id="worker", actor_type=ActorType.HUMAN):
    return TrustedPrincipal(actor_id=actor_id, actor_type=actor_type, correlation_id="auth-test")


def window(**changes):
    return Window(
        starts_at=datetime.now(UTC) - timedelta(seconds=10),
        reason="Approved test fixture",
        **changes,
    )


async def setup_pair(auth, manager, identity=None, code="case.read.assigned", role="caregiver"):
    provision, resolver, sessions = auth
    rid = await definition(sessions, role)
    pid = await definition(sessions, code, True)
    aid = await provision.assign(identity or principal(), rid, window(), manager)
    gid = await provision.grant(rid, pid, window(), manager)
    return aid, gid


async def test_registered_source_vocabulary_has_no_seeded_authority(auth):
    _, resolver, sessions = auth
    async with sessions() as session:
        assert set(await session.scalars(select(RoleDefinition.code))) == set(ROLES)
        assert set(await session.scalars(select(PermissionDefinition.code))) == set(PERMISSIONS)
        assert await session.scalar(select(func.count()).select_from(RolePermissionGrant)) == 0
        assert await session.scalar(select(func.count()).select_from(ActorRoleAssignment)) == 0
    assert not (await resolver.resolve(principal())).capabilities


@pytest.mark.parametrize("role", list(ROLES))
async def test_role_title_alone_never_grants(auth, manager, role):
    provision, resolver, sessions = auth
    await provision.assign(principal(), await definition(sessions, role), window(), manager)
    assert not (await resolver.resolve(principal())).capabilities


async def test_grant_without_assignment_denied(auth, manager):
    provision, resolver, sessions = auth
    await provision.grant(
        await definition(sessions, "caregiver"),
        await definition(sessions, "case.read.assigned", True),
        window(),
        manager,
    )
    assert not (await resolver.resolve(principal())).capabilities


@pytest.mark.parametrize("code", PERMISSIONS)
async def test_exact_explicit_permission_only(auth, manager, code):
    await setup_pair(auth, manager, code=code)
    assert (await auth[1].resolve(principal())).capabilities == frozenset({code})


@pytest.mark.parametrize("kind", ["assignment", "grant"])
@pytest.mark.parametrize("state", ["expired", "future", "revoked"])
async def test_inactive_authorization_denied(auth, manager, kind, state):
    provision, resolver, sessions = auth
    rid = await definition(sessions, "caregiver")
    pid = await definition(sessions, "case.read.assigned", True)
    now = datetime.now(UTC)
    inactive = (
        Window(
            starts_at=now - timedelta(days=2), expires_at=now - timedelta(days=1), reason="expired"
        )
        if state == "expired"
        else Window(starts_at=now + timedelta(days=1), reason="future")
        if state == "future"
        else window()
    )
    aid = await provision.assign(
        principal(), rid, inactive if kind == "assignment" else window(), manager
    )
    gid = await provision.grant(rid, pid, inactive if kind == "grant" else window(), manager)
    if state == "revoked":
        await provision.revoke(kind, aid if kind == "assignment" else gid, manager, "Revoked")
    assert not (await resolver.resolve(principal())).capabilities


async def test_multiple_roles_union_only_explicit(auth, manager):
    await setup_pair(auth, manager)
    await setup_pair(auth, manager, role="senior_caregiver", code="case.monitor.assigned")
    assert (await auth[1].resolve(principal())).capabilities == frozenset(
        {"case.read.assigned", "case.monitor.assigned"}
    )


@pytest.mark.parametrize("actor_type", list(ActorType))
async def test_actor_type_is_not_authority_and_has_audit_provenance(auth, manager, actor_type):
    identity = principal(actor_type=actor_type)
    assert not (await auth[1].resolve(identity)).capabilities
    recorder = ActorContext(
        actor_id="recording-test",
        actor_type=actor_type,
        capabilities=frozenset(),
        correlation_id="type-test",
    )
    await setup_pair(auth, recorder, identity)
    expected = frozenset() if actor_type == ActorType.AI else frozenset({"case.read.assigned"})
    assert (await auth[1].resolve(identity)).capabilities == expected
    async with auth[2]() as session:
        audits = list(await session.scalars(select(AuthorizationAudit)))
        assert len(audits) == 2
        assert all(
            a.actor_type == actor_type.value
            and a.reason
            and a.timestamp
            and a.correlation_id == "type-test"
            for a in audits
        )
    # Reusing same ID with another actor type is not the same principal.
    if actor_type != ActorType.HUMAN:
        assert not (await auth[1].resolve(principal())).capabilities


@pytest.mark.parametrize("code", ["*", "case.*", "authorization.admin", "made_up_role"])
async def test_no_wildcard_or_unregistered_business_vocabulary(auth, manager, code):
    with pytest.raises(DomainError) as exc:
        await auth[0].register(code, manager, "test", permission=True)
    assert exc.value.code == "UNREGISTERED_AUTHORIZATION_VOCABULARY"


@pytest.mark.parametrize("kind", ["assignment", "grant"])
async def test_revocation_preserves_history_and_stale_fails(auth, manager, kind):
    aid, gid = await setup_pair(auth, manager)
    identifier = aid if kind == "assignment" else gid
    await auth[0].revoke(kind, identifier, manager, "Explicit revoke")
    with pytest.raises(DomainError) as exc:
        await auth[0].revoke(kind, identifier, manager, "Stale revoke")
    assert exc.value.code == "STALE_AUTHORIZATION_REVISION"
    model = ActorRoleAssignment if kind == "assignment" else RolePermissionGrant
    async with auth[2]() as session:
        row = await session.get(model, identifier)
        assert row and row.reason == "Approved test fixture" and row.end_reason == "Explicit revoke"
        entries = list(
            await session.scalars(
                select(AuthorizationAudit).where(AuthorizationAudit.resource_id == identifier)
            )
        )
        assert {a.action for a in entries} == {"CREATED", "ENDED"}
        end = next(a for a in entries if a.action == "ENDED")
        assert end.before_reference == identifier == end.after_reference


@pytest.mark.parametrize("kind", ["assignment", "grant"])
async def test_real_duplicate_creation_race_one_winner(auth, manager, kind):
    provision, _, sessions = auth
    rid = await definition(sessions, "caregiver")
    pid = await definition(sessions, "case.read.assigned", True)

    async def write():
        if kind == "assignment":
            return await provision.assign(principal(), rid, window(), manager)
        return await provision.grant(rid, pid, window(), manager)

    results = await asyncio.gather(write(), write(), return_exceptions=True)
    assert (
        sum(isinstance(r, DomainError) and r.code == "AUTHORIZATION_CONFLICT" for r in results) == 1
    )
    assert sum(not isinstance(r, Exception) for r in results) == 1
    async with sessions() as session:
        assert await session.scalar(select(func.count()).select_from(AuthorizationAudit)) == 1


@pytest.mark.parametrize("kind", ["assignment", "grant"])
async def test_real_revocation_race_one_winner(auth, manager, kind):
    aid, gid = await setup_pair(auth, manager)
    identifier = aid if kind == "assignment" else gid
    results = await asyncio.gather(
        *[auth[0].revoke(kind, identifier, manager, "race") for _ in range(2)],
        return_exceptions=True,
    )
    assert sum(r is None for r in results) == 1
    assert (
        sum(
            isinstance(r, DomainError) and r.code == "STALE_AUTHORIZATION_REVISION" for r in results
        )
        == 1
    )
    assert not (await auth[1].resolve(principal())).capabilities


async def test_resolver_observes_only_committed_authority_during_revoke(auth, manager):
    _, gid = await setup_pair(auth, manager)
    _, resolver, sessions = auth
    async with sessions() as writer, writer.begin():
        row = await writer.get(RolePermissionGrant, gid, with_for_update=True)
        assert row
        now = (await writer.execute(select(func.statement_timestamp()))).scalar_one()
        row.ended_at = now
        row.ended_by_actor_id = manager.actor_id
        row.ended_by_actor_type = manager.actor_type.value
        row.end_reason = "race"
        row.end_correlation_id = manager.correlation_id
        Provisioning._audit(writer, row, manager, now, "race", "ENDED", gid)
        await writer.flush()
        result = await asyncio.wait_for(resolver.resolve(principal()), timeout=5)
        assert result.capabilities == frozenset({"case.read.assigned"})
    assert not (await resolver.resolve(principal())).capabilities


@pytest.mark.parametrize(
    "table",
    [
        "role_definition",
        "permission_definition",
        "authorization_audit",
        "actor_role_assignment",
        "role_permission_grant",
    ],
)
@pytest.mark.parametrize("operation", ["UPDATE", "DELETE"])
async def test_db_history_immutable(auth, manager, table, operation):
    await setup_pair(auth, manager)
    field = "actor_id" if table == "authorization_audit" else "reason"
    statement = (
        f"DELETE FROM {table}"
        if operation == "DELETE"
        else f"UPDATE {table} SET {field}='tampered'"
    )
    async with auth[2]() as session:
        with pytest.raises(DBAPIError):
            async with session.begin():
                await session.execute(text(statement))


async def test_end_without_audit_rolls_back(auth, manager):
    aid, _ = await setup_pair(auth, manager)
    async with auth[2]() as session:
        with pytest.raises(DBAPIError):
            async with session.begin():
                await session.execute(
                    text(
                        "UPDATE actor_role_assignment SET ended_at=statement_timestamp(), "
                        "ended_by_actor_id='x', ended_by_actor_type='HUMAN', "
                        "end_reason='x', end_correlation_id='x' WHERE id=:id"
                    ),
                    {"id": aid},
                )
    assert (await auth[1].resolve(principal())).capabilities == frozenset({"case.read.assigned"})


@pytest.mark.parametrize("kind", ["assignment", "grant"])
async def test_cross_lineage_replacement_rejected(auth, manager, kind):
    aid, gid = await setup_pair(auth, manager)
    await auth[0].revoke(kind, aid if kind == "assignment" else gid, manager, "replace")
    rid = await definition(auth[2], "caregiver")
    with pytest.raises(DomainError) as exc:
        if kind == "assignment":
            await auth[0].assign(principal("different"), rid, window(supersedes_id=aid), manager)
        else:
            await auth[0].grant(
                rid,
                await definition(auth[2], "case.monitor.assigned", True),
                window(supersedes_id=gid),
                manager,
            )
    assert exc.value.code == "AUTHORIZATION_CONFLICT"


async def test_registry_revision_preserves_pinned_grants_and_stale_fails(auth, manager):
    await setup_pair(auth, manager)
    original = await definition(auth[2], "caregiver")
    # A previous test run may have registered revisions; use the actual current head.
    async with auth[2]() as session:
        current = await session.scalar(
            select(RoleDefinition.id)
            .where(RoleDefinition.code == "caregiver")
            .order_by(RoleDefinition.revision_no.desc())
        )
    revised = await auth[0].register(
        "caregiver", manager, "Versioned evidence", expected_id=current
    )
    assert revised != original
    with pytest.raises(DomainError) as exc:
        await auth[0].register("caregiver", manager, "stale", expected_id=current)
    assert exc.value.code == "STALE_AUTHORIZATION_REVISION"
    assert (await auth[1].resolve(principal())).capabilities == frozenset({"case.read.assigned"})


async def test_case_create_reserved_registry_permission_does_not_redefine_ts03(
    auth, service, manager
):
    await setup_pair(auth, manager, code="case.create")
    actor = await auth[1].resolve(principal())
    with pytest.raises(DomainError) as exc:
        await service.mutate(
            "create",
            CreateCase(
                upstream_enrollment_ref="upstream",
                elder_reference="elder",
                initial_caregiver_actor_id="worker",
            ),
            actor,
            "test",
        )
    assert exc.value.code == "CAPABILITY_REQUIRED"


async def test_trusted_principal_http_resolution_and_anonymous_denial(auth, manager):
    await setup_pair(auth, manager)
    app = create_app(Settings(database_url=PostgresDsn(os.environ["NASIM_TEST_APP_DATABASE_URL"])))
    identity = None

    @app.middleware("http")
    async def trusted_test_adapter(request, call_next):
        if identity is not None:
            request.state.trusted_principal = identity
        return await call_next(request)

    try:
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app), base_url="http://test"
        ) as client:
            assert (
                await client.get(
                    "/api/v1/authorization/self",
                    headers={
                        "X-Actor-ID": "worker",
                        "X-Role": "caregiver",
                        "Authorization": "Bearer fake",
                    },
                )
            ).status_code == 401
            identity = principal()
            response = await client.get("/api/v1/authorization/self")
            assert response.status_code == 200
            assert response.json()["capabilities"] == ["case.read.assigned"]
            identity = {"actor_id": "worker"}
            assert (await client.get("/api/v1/authorization/self")).status_code == 401
    finally:
        await app.state.engine.dispose()


@pytest.mark.parametrize(
    "change",
    [
        {"reason": " "},
        {"starts_at": datetime.now()},
        {"expires_at": datetime.now(UTC) - timedelta(days=2)},
    ],
)
def test_window_contract_fails_closed(change):
    with pytest.raises(ValidationError):
        Window(**({"starts_at": datetime.now(UTC), "reason": "test"} | change))


@pytest.mark.parametrize("kind", ["assignment", "grant"])
async def test_valid_replacement_preserves_predecessor(auth, manager, kind):
    aid, gid = await setup_pair(auth, manager)
    old = aid if kind == "assignment" else gid
    await auth[0].revoke(kind, old, manager, "Replacement evidence")
    rid = await definition(auth[2], "caregiver")
    if kind == "assignment":
        new = await auth[0].assign(principal(), rid, window(supersedes_id=old), manager)
    else:
        pid = await definition(auth[2], "case.read.assigned", True)
        new = await auth[0].grant(rid, pid, window(supersedes_id=old), manager)
    assert new != old
    model = ActorRoleAssignment if kind == "assignment" else RolePermissionGrant
    async with auth[2]() as session:
        prior = await session.get(model, old)
        successor = await session.get(model, new)
        assert prior and prior.ended_at and successor and successor.supersedes_id == old
    assert (await auth[1].resolve(principal())).capabilities == frozenset({"case.read.assigned"})


@pytest.mark.parametrize("permission", [False, True])
async def test_definition_cross_code_lineage_rejected(auth, manager, permission):
    model = PermissionDefinition if permission else RoleDefinition
    code, other = ("case.create", "case.read.oversight") if permission else ("employer", "family")
    previous = await definition(auth[2], other, permission)
    async with auth[2]() as session:
        with pytest.raises(DBAPIError):
            async with session.begin():
                now = (await session.execute(select(func.statement_timestamp()))).scalar_one()
                row = model(
                    id=uuid4(),
                    code=code,
                    title=code,
                    revision_no=2,
                    supersedes_id=previous,
                    recorded_at=now,
                    recorded_by_actor_id=manager.actor_id,
                    recorded_by_actor_type=manager.actor_type.value,
                    correlation_id=manager.correlation_id,
                    reason="cross lineage",
                )
                session.add(row)
                Provisioning._audit(
                    session, row, manager, now, "cross lineage", "REGISTERED", previous
                )
                await session.flush()


async def test_definition_revision_does_not_inherit_grants(auth, manager):
    _, _, sessions = auth
    async with sessions() as session:
        latest = await session.scalar(
            select(RoleDefinition.id)
            .where(RoleDefinition.code == "senior_caregiver")
            .order_by(RoleDefinition.revision_no.desc())
        )
    new = await auth[0].register(
        "senior_caregiver", manager, "Version evidence", expected_id=latest
    )
    old = await definition(sessions, "senior_caregiver")
    pid = await definition(sessions, "case.read.oversight", True)
    await auth[0].grant(old, pid, window(), manager)
    await auth[0].assign(principal(), new, window(), manager)
    assert not (await auth[1].resolve(principal())).capabilities


async def test_creation_without_matching_audit_rolls_back(auth, manager):
    rid = await definition(auth[2], "caregiver")
    async with auth[2]() as session:
        with pytest.raises(DBAPIError):
            async with session.begin():
                now = (await session.execute(select(func.statement_timestamp()))).scalar_one()
                session.add(
                    ActorRoleAssignment(
                        id=uuid4(),
                        actor_id="unlogged",
                        actor_type="HUMAN",
                        role_code="caregiver",
                        role_revision_id=rid,
                        starts_at=now,
                        recorded_at=now,
                        recorded_by_actor_id=manager.actor_id,
                        recorded_by_actor_type="HUMAN",
                        correlation_id=manager.correlation_id,
                        reason="no audit",
                    )
                )
    assert not (await auth[1].resolve(principal("unlogged"))).capabilities


async def test_runtime_role_can_resolve_but_not_manage_authorization(auth, manager):
    await setup_pair(auth, manager)
    app = create_app(Settings(database_url=PostgresDsn(os.environ["NASIM_TEST_APP_DATABASE_URL"])))
    try:
        assert (await app.state.authorization.resolve(principal())).capabilities == frozenset(
            {"case.read.assigned"}
        )
        async with app.state.engine.begin() as connection:
            for table in [
                "role_definition",
                "permission_definition",
                "role_permission_grant",
                "actor_role_assignment",
                "authorization_audit",
            ]:
                assert not await connection.scalar(
                    text(
                        "SELECT has_table_privilege(current_user,:table,"
                        "'INSERT,UPDATE,DELETE,TRUNCATE')"
                    ),
                    {"table": table},
                )
    finally:
        await app.state.engine.dispose()


async def test_resolved_context_integrates_ts03_without_ownership_bypass(auth, manager, service):
    provision, resolver, sessions = auth
    creator = principal("fixture-creator")
    await setup_pair(auth, manager, creator, code="case.assignment.manage", role="nasim_operator")
    result = await service.mutate(
        "create",
        CreateCase(
            upstream_enrollment_ref="enrolled",
            elder_reference="elder",
            initial_caregiver_actor_id="worker",
        ),
        await resolver.resolve(creator),
        "resolved-create",
    )
    from uuid import UUID

    case_id = UUID(result["case"]["id"])
    rid = await definition(sessions, "caregiver")
    await provision.assign(principal(), rid, window(), manager)
    with pytest.raises(DomainError) as missing:
        await service.read("profile", case_id, await resolver.resolve(principal()))
    assert missing.value.code == "CAPABILITY_REQUIRED"
    await provision.grant(
        rid, await definition(sessions, "case.read.assigned", True), window(), manager
    )
    assert await service.read("profile", case_id, await resolver.resolve(principal()))
    intruder = principal("not-assigned")
    await provision.assign(intruder, rid, window(), manager)
    with pytest.raises(DomainError) as not_assigned:
        await service.read("profile", case_id, await resolver.resolve(intruder))
    assert not_assigned.value.code == "ASSIGNED_CAREGIVER_REQUIRED"
