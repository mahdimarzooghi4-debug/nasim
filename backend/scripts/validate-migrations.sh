#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
export UV_CACHE_DIR="${UV_CACHE_DIR:-/tmp/nasim-uv-cache}"
export NASIM_DATABASE_URL="${NASIM_TEST_DATABASE_URL:-postgresql://nasim:nasim_dev_only@127.0.0.1:55432/nasim_test}"
uv run --locked python - <<'PY'
from nasim.infrastructure.config import load_settings
settings = load_settings()
if not settings.database_url.path or not settings.database_url.path.endswith('_test'):
    raise SystemExit('Destructive migration validation requires a dedicated *_test database')
PY
uv run --locked alembic upgrade head
uv run --locked alembic downgrade base
uv run --locked alembic upgrade head
uv run --locked alembic check
# Restored tables need restored application grants for the local Compose database.
# Custom database administrators must apply equivalent least-privilege grants themselves.
if [ "$NASIM_DATABASE_URL" = 'postgresql://nasim:nasim_dev_only@127.0.0.1:55432/nasim_test' ]; then
  docker compose -f ../compose.yaml exec -T postgres psql -v ON_ERROR_STOP=1 -U nasim -d nasim_test < dev/grants.sql
fi
