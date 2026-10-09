"""Real HTTP smoke checks for a running Stage-like image. Standard library only."""

import argparse
import json
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from uuid import uuid4

EXPECTED_ROUTES = {
    "/health": {"get"},
    "/api/v1/provider-candidates": {"get", "post"},
    "/api/v1/provider-candidates/{candidate_id}": {"get"},
    "/api/v1/provider-candidates/{candidate_id}/qualification-evidence": {"get", "post"},
    "/api/v1/provider-qualification-evidence/{evidence_id}": {"get"},
    "/api/v1/provider-candidates/{candidate_id}/qualification-review-requests": {"get", "post"},
    "/api/v1/provider-candidates/{candidate_id}/qualification-review-workspace": {"get"},
    "/api/v1/provider-qualification-review-requests/{request_id}": {"get"},
    "/api/v1/cases/{case_id}/referrals": {"get", "post"},
    "/api/v1/referrals/{referral_id}": {"get"},
    "/api/v1/referrals/{referral_id}/follow-up-records": {"get", "post"},
    "/api/v1/referral-follow-up-records/{record_id}": {"get"},
    "/api/v1/authorization/self": {"get"},
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
    status, _ = request(base_url, "/api/v1/authorization/self")
    if status != 401:
        raise RuntimeError("Anonymous authorization inspection did not fail closed")
    for excluded in ("enrollments", "providers", "outcomes", "emergencies", "ai"):
        for method in ("GET", "POST"):
            status, _ = request(
                base_url, f"/api/v1/{excluded}", method, {} if method == "POST" else None
            )
            if status != 404:
                raise RuntimeError("Excluded-scope route is reachable")
    status, body = request(base_url, f"/api/v1/cases/{uuid4()}")
    if status != 401:
        raise RuntimeError("Anonymous business read did not fail closed")
    case_id, referral_id = uuid4(), uuid4()
    status, _ = request(
        base_url,
        f"/api/v1/cases/{case_id}/referrals",
        "POST",
        {
            "source_need_observation_id": str(uuid4()),
            "expected_current_assignment_id": str(uuid4()),
            "reason": "record-only smoke",
        },
    )
    if status != 401:
        raise RuntimeError("Anonymous Referral recording did not fail closed")
    for path in (f"/api/v1/cases/{case_id}/referrals", f"/api/v1/referrals/{referral_id}"):
        status, _ = request(base_url, path)
        if status != 401:
            raise RuntimeError("Anonymous Referral read did not fail closed")
    for path in (
        f"/api/v1/referrals/{referral_id}/follow-up-records",
        f"/api/v1/referral-follow-up-records/{uuid4()}",
    ):
        status, _ = request(base_url, path)
        if status != 401:
            raise RuntimeError("Anonymous Referral follow-up read did not fail closed")
    status, _ = request(
        base_url,
        f"/api/v1/referrals/{referral_id}/follow-up-records",
        "POST",
        {
            "expected_current_assignment_id": str(uuid4()),
            "note": "smoke",
            "reason": "smoke",
        },
    )
    if status != 401:
        raise RuntimeError("Anonymous Referral follow-up write did not fail closed")
    for action in ("accept", "reject", "dispatch", "complete", "cancel", "escalate", "corrections"):
        status, _ = request(base_url, f"/api/v1/referrals/{referral_id}/{action}", "POST", {})
        if status != 404:
            raise RuntimeError("Undecided Referral lifecycle route is reachable")

    candidate_id = uuid4()
    status, _ = request(
        base_url,
        "/api/v1/provider-candidates",
        "POST",
        {"display_name": "candidate smoke", "reason": "foundation smoke"},
    )
    if status != 401:
        raise RuntimeError("Anonymous Provider Candidate registration did not fail closed")
    for path in (
        "/api/v1/provider-candidates",
        f"/api/v1/provider-candidates/{candidate_id}",
    ):
        status, _ = request(base_url, path)
        if status != 401:
            raise RuntimeError("Anonymous Provider Candidate read did not fail closed")
    evidence_id = uuid4()
    status, _ = request(
        base_url,
        f"/api/v1/provider-candidates/{candidate_id}/qualification-evidence",
        "POST",
        {
            "evidence_label": "qualification evidence smoke",
            "evidence_reference": "opaque-smoke-reference",
            "reason": "foundation smoke",
        },
    )
    if status != 401:
        raise RuntimeError("Anonymous qualification evidence recording did not fail closed")
    for path in (
        f"/api/v1/provider-candidates/{candidate_id}/qualification-evidence",
        f"/api/v1/provider-qualification-evidence/{evidence_id}",
    ):
        status, _ = request(base_url, path)
        if status != 401:
            raise RuntimeError("Anonymous qualification evidence read did not fail closed")

    review_request_id = uuid4()
    status, _ = request(
        base_url,
        f"/api/v1/provider-candidates/{candidate_id}/qualification-review-requests",
        "POST",
        {"reason": "review request foundation smoke"},
    )
    if status != 401:
        raise RuntimeError("Anonymous qualification review request did not fail closed")
    for path in (
        f"/api/v1/provider-candidates/{candidate_id}/qualification-review-requests",
        f"/api/v1/provider-qualification-review-requests/{review_request_id}",
    ):
        status, _ = request(base_url, path)
        if status != 401:
            raise RuntimeError("Anonymous qualification review request read did not fail closed")
    status, _ = request(
        base_url,
        f"/api/v1/provider-candidates/{candidate_id}/qualification-review-workspace",
    )
    if status != 401:
        raise RuntimeError("Anonymous Provider Qualification workspace read did not fail closed")
    for action in (
        "assign",
        "review",
        "decide",
        "qualify",
        "approve",
        "reject",
        "activate",
        "close",
        "reopen",
    ):
        status, _ = request(
            base_url,
            f"/api/v1/provider-qualification-review-requests/{review_request_id}/{action}",
            "POST",
            {},
        )
        if status != 404:
            raise RuntimeError("Undecided qualification review decision route is reachable")

    for action in ("activate", "approve", "reject", "suspend", "qualify", "capacity", "contract"):
        status, _ = request(
            base_url, f"/api/v1/provider-candidates/{candidate_id}/{action}", "POST", {}
        )
        if status != 404:
            raise RuntimeError("Undecided operational Provider route is reachable")
    for action in ("review", "verify", "approve", "reject", "activate", "expire", "replace"):
        status, _ = request(
            base_url,
            f"/api/v1/provider-qualification-evidence/{evidence_id}/{action}",
            "POST",
            {},
        )
        if status != 404:
            raise RuntimeError("Undecided qualification decision route is reachable")

    print(
        "Stage HTTP smoke passed: readiness, Case/Referral/Provider Candidate/"
        "Qualification Evidence/Review Request routes, anonymous denial and excluded routes"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", required=True)
    validate_http(parser.parse_args().base_url)
