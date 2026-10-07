# The base digests and uv version were resolved from the official registries during validation.
FROM ghcr.io/astral-sh/uv:0.12.19@sha256:04d046b13e60d6bcec73cbc5e1cad25d680dea90c8573340950a0ac2d1aef424 AS uv
FROM python:3.12-slim-bookworm@sha256:34386ef0cb081344d7ec1c103ba398e6e9f64e9ab3a1509accc92a4e24a07258 AS builder
COPY --from=uv /uv /usr/local/bin/uv
ENV UV_PYTHON_DOWNLOADS=never UV_LINK_MODE=copy
WORKDIR /app
COPY backend/pyproject.toml backend/uv.lock ./
# Only locked runtime dependencies. Source is imported directly; no unlocked build backend needed.
# Optional trust bundle is a build-only mount for managed egress proxies; never disable TLS.
RUN --mount=type=secret,id=proxy_ca \
    if [ -f /run/secrets/proxy_ca ]; then \
      export SSL_CERT_FILE=/run/secrets/proxy_ca UV_SYSTEM_CERTS=true; \
    fi; \
    uv sync --locked --no-dev --no-install-project --python /usr/local/bin/python

FROM python:3.12-slim-bookworm@sha256:34386ef0cb081344d7ec1c103ba398e6e9f64e9ab3a1509accc92a4e24a07258 AS runtime
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/src PATH=/app/.venv/bin:$PATH
WORKDIR /app
RUN groupadd --gid 10001 nasim && useradd --uid 10001 --gid 10001 --no-create-home nasim
COPY --from=builder --chown=10001:10001 /app/.venv /app/.venv
COPY --chown=10001:10001 backend/src ./src
COPY --chown=10001:10001 backend/alembic.ini ./
COPY --chown=10001:10001 backend/migrations ./migrations
COPY --chmod=0555 backend/scripts/stage-migrate.sh /app/stage-migrate.sh
USER 10001:10001
EXPOSE 8000
HEALTHCHECK --interval=5s --timeout=4s --start-period=15s --retries=12 \
    CMD python -c "import urllib.request; r=urllib.request.urlopen('http://127.0.0.1:8000/health',timeout=3); assert r.status==200"
CMD ["uvicorn", "nasim.api.stage:create_stage_app", "--factory", "--host", "0.0.0.0", "--port", "8000"]
