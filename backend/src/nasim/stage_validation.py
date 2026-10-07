"""Real HTTP smoke checks for a running Stage-like image. Standard library only."""

import argparse
import json
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from uuid import uuid4

EXPECTED_ROUTES = {
    "/health": {"get"},
    "/api/v1/cases": {"post"},
    "/api/v1/cases/{case_id}": {"get"},
    "/api/v1/cases/{case_id}/workspace": {"get"},
    "/api/v1/cases/{case_id}/profile/corrections": {"post"},
    "/api/v1/cases/{case_id}/reassignments": {"post"},
    "/api/v1/cases/{case_id}/assignments": {"get"},
    "/api/v1/cases/{case_id}/contacts": {"get", "post"},
    "/api/v1/cases/{case_id}/contacts/{logical_contact_id}/corrections": {"post"},
    "/api/v1/cases/{case_id}/interactions": {"get", "post"},
    "/api/v1/cases/{case_id}/interactions/{interaction_id}/corrections": {"post"},
    "/api/v1/cases/{case_id}/observations": {"get", "post"},
    "/api/v1/cases/{case_id}/observations/{observation_id}/corrections": {"post"},
    "/api/v1/cases/{case_id}/timeline": {"get"},
}


def request(
    base_url: str, path: str, method: str = "GET", body: dict | None = None
) -> tuple[int, dict]:
    data = json.dumps(body).encode() if body is not None else None
    req = Request(
        base_url.rstrip("/") + path,
        method=method,
        data=data,
        headers={"Content-Type": "application/json", "Idempotency-Key": "stage-smoke"},
    )
    try:
        with urlopen(req, timeout=5) as response:
            return response.status, json.loads(response.read())
    except HTTPError as response:
        return response.code, json.loads(response.read())


def validate_http(base_url: str) -> None:
    status, body = request(base_url, "/health")
    if status != 200 or body != {"status": "ok"}:
        raise RuntimeError(
            "Stage readiness failed: DB connectivity or migration revision unavailable"
        )
    status, contract = request(base_url, "/openapi.json")
    if status != 200:
        raise RuntimeError("OpenAPI is unavailable")
    actual = {path: set(methods) for path, methods in contract["paths"].items()}
    if actual != EXPECTED_ROUTES:
        raise RuntimeError("Stage API surface differs from TS-03 contract")
    status, body = request(
        base_url,
        "/api/v1/cases",
        "POST",
        {
            "upstream_enrollment_ref": "smoke-reference",
            "elder_reference": "smoke-reference",
            "initial_caregiver_actor_id": "smoke-actor",
        },
    )
    if status != 401 or body.get("error", {}).get("code") != "ACTOR_CONTEXT_REQUIRED":
        raise RuntimeError("Anonymous business mutation did not fail closed")
    for excluded in ("enrollments", "referrals", "providers", "outcomes", "emergencies", "ai"):
        for method in ("GET", "POST"):
            status, _ = request(
                base_url, f"/api/v1/{excluded}", method, {} if method == "POST" else None
            )
            if status != 404:
                raise RuntimeError("Excluded-scope route is reachable")
    status, body = request(base_url, f"/api/v1/cases/{uuid4()}")
    if status != 401:
        raise RuntimeError("Anonymous business read did not fail closed")
    print("Stage HTTP smoke passed: readiness, TS-03 routes, anonymous denial and excluded routes")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", required=True)
    validate_http(parser.parse_args().base_url)
