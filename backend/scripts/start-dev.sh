#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
export UV_CACHE_DIR="${UV_CACHE_DIR:-/tmp/nasim-uv-cache}"
export NASIM_DATABASE_URL="${NASIM_DATABASE_URL:-postgresql://nasim_app:nasim_app_dev_only@127.0.0.1:55432/nasim_dev}"
exec uv run --locked uvicorn nasim.api.app:create_app --factory --host 127.0.0.1 --port 8000
