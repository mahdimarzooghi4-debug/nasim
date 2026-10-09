"""Version-bound inventory overlay for Product Owner's reported 84/84 content acceptance.

D-0160: the Operations Manager personally reviewed all 84 synthetic examples.
D-0162: Product Owner reports that the Manager accepted ALL 84 original
samples. This overlay is NOT an authenticated human review record. The exact
Git blob versions actually viewed by the Manager have not been evidenced.

No dataset activation, real elder data collection, editing or AI inference.
"""

import json
from hashlib import sha256
from pathlib import Path
from typing import Any

from nasim.learning.synthetic_seed import build_initial_synthetic_inventory


def build_owner_reported_content_acceptance(
    project_root: Path | None = None,
) -> dict[str, Any]:
    """Report owner's 84/84 statement without fabricating signed evidence.

    This deliberately differs from synthetic-human-review-evidence.v1 so it
    cannot be substituted for an externally authenticated review batch.
    """
    inventory = build_initial_synthetic_inventory(project_root)
    records = [
        {
            "record_id": record["record_id"],
            "source_file": record["source_file"],
            "current_source_record_sha256": record["record_sha256"],
            "content_outcome": "ACCEPTED_AS_REPORTED_BY_PRODUCT_OWNER",
        }
        for record in inventory["candidate_records"]
    ]
    if len(records) != 84 or len({row["record_id"] for row in records}) != 84:
        raise ValueError("OWNER_REPORTED_SOURCE_SET_INCOMPLETE")

    payload: dict[str, Any] = {
        "schema": "nasim.owner-reported-synthetic-content-acceptance.v1",
        "source_commit": inventory["source_commit"],
        "inventory_sha256": inventory["inventory_sha256"],
        "review_owner_role": "NASIM_OPERATIONS_MANAGER",
        "human_review_performed_owner_attestation": "D-0160",
        "all_content_accepted_owner_attestation": "D-0162",
        "report_scope": "84_ORIGINAL_SYNTHETIC_RECORDS_ONLY",
        "reported_content_accepted": 84,
        "reported_content_rejected": 0,
        "reported_content_needs_rewrite": 0,
        "records": records,
        "historical_original_source_flags": "UNCHANGED",
        "actual_human_review_source_version": "EXTERNAL_EVIDENCE_NOT_RECONCILED",
        "actual_human_review_signed_evidence": "NOT_PROVIDED",
        "authorial_patch_decisions": "UNRESOLVED",
        "training_evaluation_partition": "UNASSIGNED",
        "dataset_status": "NOT_APPROVED",
        "runtime_training_enabled": False,
        "production_promotion_authorized": False,
    }
    canonical = json.dumps(
        payload, ensure_ascii=True, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    payload["report_sha256"] = sha256(canonical).hexdigest()
    return payload
