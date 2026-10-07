#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
export UV_CACHE_DIR="${UV_CACHE_DIR:-/tmp/nasim-uv-cache}"
export NASIM_TEST_DATABASE_URL="${NASIM_TEST_DATABASE_URL:-postgresql://nasim:nasim_dev_only@127.0.0.1:55432/nasim_test}"
export NASIM_TEST_APP_DATABASE_URL="${NASIM_TEST_APP_DATABASE_URL:-postgresql://nasim_app:nasim_app_dev_only@127.0.0.1:55432/nasim_test}"
uv run --locked pytest
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pyright
