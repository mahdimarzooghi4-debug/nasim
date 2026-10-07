#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
export UV_CACHE_DIR="${UV_CACHE_DIR:-/tmp/nasim-uv-cache}"
uv sync --locked
cd ..
docker compose up -d --wait
# init.sql runs only for fresh volumes. Recover safely if initial startup was interrupted.
if [ "$(docker compose exec -T postgres psql -U nasim -d postgres -tAc "SELECT 1 FROM pg_database WHERE datname='nasim_test'")" != 1 ]; then
  docker compose exec -T postgres psql -v ON_ERROR_STOP=1 -U nasim -d postgres -c 'CREATE DATABASE nasim_test OWNER nasim'
fi
docker compose exec -T postgres psql -v ON_ERROR_STOP=1 -U nasim -d postgres <<'SQL'
DO $$ BEGIN
  IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname='nasim_app') THEN
    CREATE ROLE nasim_app LOGIN PASSWORD 'nasim_app_dev_only' NOSUPERUSER NOCREATEDB NOCREATEROLE;
  END IF;
END $$;
SQL
cd backend
for database in nasim_dev nasim_test; do
  NASIM_DATABASE_URL="postgresql://nasim:nasim_dev_only@127.0.0.1:55432/$database" uv run --locked alembic upgrade head
  docker compose -f ../compose.yaml exec -T postgres psql -v ON_ERROR_STOP=1 -U nasim -d "$database" < dev/grants.sql
done
