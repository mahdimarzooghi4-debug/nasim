#!/usr/bin/env bash
set -euo pipefail
: "${NASIM_STAGE_DB_USER:?Runtime role must be explicitly supplied}"
: "${NASIM_STAGE_DB_PASSWORD:?Runtime password must be externally supplied}"
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" \
  --set=app_user="$NASIM_STAGE_DB_USER" --set=app_password="$NASIM_STAGE_DB_PASSWORD" <<'SQL'
CREATE ROLE :"app_user" LOGIN PASSWORD :'app_password'
  NOSUPERUSER NOCREATEDB NOCREATEROLE NOREPLICATION NOBYPASSRLS;
SQL
