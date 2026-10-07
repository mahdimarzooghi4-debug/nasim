#!/usr/bin/env bash
# Inside the built image, or from an already installed backend environment.
set -euo pipefail
exec python -m nasim.infrastructure.stage_migrate
