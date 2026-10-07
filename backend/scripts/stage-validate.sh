#!/usr/bin/env bash
# Validate an isolated Stage-like stack with externally supplied environment values.
set -euo pipefail
cd "$(dirname "$0")/../.."
: "${NASIM_STAGE_PROJECT:?Supply a dedicated Stage validation project}"
: "${NASIM_STAGE_SMOKE_URL:?Supply an HTTP address reaching the validation backend}"
compose=(docker compose -f compose.stage.yaml)
if [ -n "${NASIM_STAGE_COMPOSE_OVERRIDE:-}" ]; then
  compose+=(-f "$NASIM_STAGE_COMPOSE_OVERRIDE")
fi
"${compose[@]}" config --quiet
artifacts="${NASIM_STAGE_ARTIFACT_DIR:-/tmp/${NASIM_STAGE_PROJECT}-stage-validation}"
mkdir -p "$artifacts"
chmod 700 "$artifacts"
cleanup() {
  status=$?
  trap - EXIT
  "${compose[@]}" logs --no-color --tail 200 > "$artifacts/compose.log" 2>&1 || true
  if ! "${compose[@]}" down --remove-orphans; then
    if [ "$status" -eq 0 ]; then status=1; fi
  fi
  if [ "$status" -ne 0 ]; then
    echo "Stage validation failed; logs retained in $artifacts/compose.log and data volume preserved" >&2
  fi
  exit "$status"
}
trap cleanup EXIT
"${compose[@]}" build
"${compose[@]}" up -d --wait --wait-timeout 90
# Verify container/runtime invariants directly in the built image; no development packages.
"${compose[@]}" exec -T backend python - <<'PY'
import importlib.util
import os
if os.getuid() == 0:
    raise SystemExit('Stage runtime must not run as root')
for module in ('pytest', 'ruff', 'pyright', 'httpx'):
    if importlib.util.find_spec(module) is not None:
        raise SystemExit(f'Development package unexpectedly installed: {module}')
from nasim.infrastructure.stage_config import load_stage_settings
settings = load_stage_settings()
import asyncio
from sqlalchemy import text
from nasim.infrastructure.database import make_engine
async def check_db():
    engine = make_engine(settings)
    try:
        async with engine.connect() as conn:
            revision = await conn.scalar(text('SELECT version_num FROM alembic_version'))
            if revision != '0003_referral':
                raise SystemExit('Unexpected Stage migration revision')
            if await conn.scalar(text('SELECT rolsuper FROM pg_roles WHERE rolname=current_user')):
                raise SystemExit('Stage runtime DB role must not be a superuser')
            for privilege in ('UPDATE', 'DELETE', 'TRUNCATE'):
                if await conn.scalar(text(
                    "SELECT has_table_privilege(current_user, 'audit_entry', :privilege)"
                ), {'privilege': privilege}):
                    raise SystemExit('Stage runtime DB role can alter audit history')
    finally:
        await engine.dispose()
asyncio.run(check_db())
print('Non-root runtime and locked production dependency checks passed')
PY
"${compose[@]}" exec -T postgres sh -c 'pg_dump --schema-only --no-owner --no-privileges -U "$POSTGRES_USER" -d "$POSTGRES_DB"' > "$artifacts/schema-before.sql"
UV_CACHE_DIR="${UV_CACHE_DIR:-/tmp/nasim-uv-cache}" uv run --project backend --locked python -m nasim.stage_validation --base-url "$NASIM_STAGE_SMOKE_URL"
"${compose[@]}" restart backend
# Repeat the explicit migration command too: no new revision or DDL should be produced.
"${compose[@]}" run --rm --no-deps migrate
"${compose[@]}" up -d --wait --wait-timeout 90 backend
"${compose[@]}" exec -T postgres sh -c 'pg_dump --schema-only --no-owner --no-privileges -U "$POSTGRES_USER" -d "$POSTGRES_DB"' > "$artifacts/schema-after.sql"
# PostgreSQL dump randomizes \restrict tokens, which are not schema changes.
sed '/^\\restrict /d; /^\\unrestrict /d' "$artifacts/schema-before.sql" > "$artifacts/schema-before.normalized.sql"
sed '/^\\restrict /d; /^\\unrestrict /d' "$artifacts/schema-after.sql" > "$artifacts/schema-after.normalized.sql"
diff -u "$artifacts/schema-before.normalized.sql" "$artifacts/schema-after.normalized.sql"
UV_CACHE_DIR="${UV_CACHE_DIR:-/tmp/nasim-uv-cache}" uv run --project backend --locked python -m nasim.stage_validation --base-url "$NASIM_STAGE_SMOKE_URL"
echo 'Stage-like boot, migration, HTTP smoke, restart and zero schema drift passed'
