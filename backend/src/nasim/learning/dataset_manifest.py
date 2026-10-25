"""Policy-neutral Dataset manifest mechanics, deliberately NOT a learning pipeline.

BC-007 has no accepted training eligibility, consent/legal basis, approval
authority, curation rule or de-identification policy. Nothing in this module
queries Case/Provider tables or Outbox, extracts raw records, trains a model,
or activates a runtime. An unconfigured verifier always denies generation.

A later Business/Technical gate must supply an independently reviewed verifier
that checks legal-purpose eligibility and curation evidence against authoritative
sources before constructing any dataset from real records.
"""

import json
import re
from collections.abc import Iterable
from dataclasses import dataclass
from enum import StrEnum
from hashlib import sha256
from typing import Protocol
from uuid import UUID, uuid5

_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
_NAMESPACE = UUID("7c926789-2ae3-47aa-8909-02a901c6d2d8")
_SOURCE_NAMESPACE = re.compile(r"[a-z][a-z0-9_.-]{0,79}\Z")


class ManifestError(ValueError):
    """An invalid technical manifest request, never an eligibility decision."""


class AdmissionUnavailable(PermissionError):
    """Dataset creation is unauthorized or the required admission is absent."""


class DatasetPurpose(StrEnum):
    TRAINING = "TRAINING"
    EVALUATION = "EVALUATION"


def _digest(value: str) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise ManifestError("INVALID_SHA256")
    return value


def _nonblank(value: str) -> str:
    if not isinstance(value, str) or _SOURCE_NAMESPACE.fullmatch(value) is None:
        raise ManifestError("INVALID_SOURCE_NAMESPACE")
    return value


@dataclass(frozen=True, slots=True)
class CuratedSourceRef:
    """Opaque immutable source/version locator and attested curation reference.

    No raw note, contact value, health label or provider free text may be
    represented here. A digest's presence is NOT evidence of legal permission.
    """

    namespace: str
    source_id: UUID
    source_version_sha256: str
    curation_evidence_sha256: str

    def __post_init__(self) -> None:
        _nonblank(self.namespace)
        if not isinstance(self.source_id, UUID):
            raise ManifestError("INVALID_SOURCE_ID")
        _digest(self.source_version_sha256)
        _digest(self.curation_evidence_sha256)

    @property
    def source_key(self) -> tuple[str, str]:
        return self.namespace, str(self.source_id)

    def serialized(self) -> dict[str, str]:
        return {
            "namespace": self.namespace,
            "source_id": str(self.source_id),
            "source_version_sha256": self.source_version_sha256,
            "curation_evidence_sha256": self.curation_evidence_sha256,
        }


@dataclass(frozen=True, slots=True)
class AdmissionEvidence:
    """The result of an EXTERNAL, approved, independently verified policy.

    This is not itself the policy evaluator, a bearer credential, a human
    approval record or a way to infer eligibility from a Casework event.
    """

    policy_sha256: str
    approval_evidence_sha256: str
    eligible_sources: frozenset[tuple[str, str, str, str]]

    def __post_init__(self) -> None:
        _digest(self.policy_sha256)
        _digest(self.approval_evidence_sha256)
        if not self.eligible_sources:
            raise AdmissionUnavailable("NO_POLICY_ELIGIBLE_SOURCES")


@dataclass(frozen=True, slots=True)
class DatasetAdmissionRequest:
    purpose: DatasetPurpose
    sources: tuple[CuratedSourceRef, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.purpose, DatasetPurpose):
            raise ManifestError("INVALID_DATASET_PURPOSE")
        if not self.sources or not all(isinstance(s, CuratedSourceRef) for s in self.sources):
            raise ManifestError("EMPTY_OR_INVALID_DATASET_SOURCES")


class AdmissionVerifier(Protocol):
    """Future authorized policy engine; intentionally NO Production implementation."""

    def verify(self, request: DatasetAdmissionRequest) -> AdmissionEvidence: ...


@dataclass(frozen=True, slots=True)
class DatasetManifest:
    """Deterministic *proposed* version, not an APPROVED Dataset or TrainingRun."""

    manifest_id: UUID
    manifest_sha256: str
    purpose: DatasetPurpose
    policy_sha256: str
    approval_evidence_sha256: str
    sources: tuple[CuratedSourceRef, ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "manifest_id": str(self.manifest_id),
            "manifest_sha256": self.manifest_sha256,
            "purpose": self.purpose.value,
            "policy_sha256": self.policy_sha256,
            "approval_evidence_sha256": self.approval_evidence_sha256,
            "sources": [source.serialized() for source in self.sources],
        }


def _source_attestation(source: CuratedSourceRef) -> tuple[str, str, str, str]:
    return (
        source.namespace,
        str(source.source_id),
        source.source_version_sha256,
        source.curation_evidence_sha256,
    )


class VersionedManifestBuilder:
    """No verifier is installed by default; runtime cannot create a manifest."""

    def __init__(self, verifier: AdmissionVerifier | None = None) -> None:
        self._verifier = verifier

    def build(
        self,
        purpose: DatasetPurpose,
        sources: Iterable[CuratedSourceRef],
    ) -> DatasetManifest:
        # Read the input once. No streaming of operational free text or DB rows.
        requested = DatasetAdmissionRequest(purpose=purpose, sources=tuple(sources))
        self._validate_identity(requested.sources)

        if self._verifier is None:
            raise AdmissionUnavailable("TRAINING_ELIGIBILITY_POLICY_NOT_APPROVED")

        # Every source/version and curation evidence must be individually
        # covered by an external approval. Reject any extra or omitted entries.
        admission = self._verifier.verify(requested)
        if not isinstance(admission, AdmissionEvidence):
            raise AdmissionUnavailable("INVALID_ADMISSION_EVIDENCE")
        membership = frozenset(_source_attestation(s) for s in requested.sources)
        if admission.eligible_sources != membership:
            raise AdmissionUnavailable("UNAPPROVED_OR_STALE_SOURCE_MEMBERSHIP")

        ordered = tuple(sorted(requested.sources, key=_source_attestation))
        canonical = {
            "manifest_schema": "nasim.dataset-manifest.v1",
            "purpose": requested.purpose.value,
            "policy_sha256": admission.policy_sha256,
            "approval_evidence_sha256": admission.approval_evidence_sha256,
            "sources": [s.serialized() for s in ordered],
        }
        packed = json.dumps(
            canonical, ensure_ascii=True, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")
        digest = sha256(packed).hexdigest()
        return DatasetManifest(
            manifest_id=uuid5(_NAMESPACE, digest),
            manifest_sha256=digest,
            purpose=requested.purpose,
            policy_sha256=admission.policy_sha256,
            approval_evidence_sha256=admission.approval_evidence_sha256,
            sources=ordered,
        )

    @staticmethod
    def _validate_identity(sources: tuple[CuratedSourceRef, ...]) -> None:
        seen: set[tuple[str, str]] = set()
        for source in sources:
            identity = source.source_key
            if identity in seen:
                raise ManifestError("DUPLICATE_SOURCE_IDENTITY")
            seen.add(identity)


def verify_partition_isolation(training: DatasetManifest, evaluation: DatasetManifest) -> None:
    """Check exact source identity overlap, NOT household-level independence."""

    if training.purpose is not DatasetPurpose.TRAINING:
        raise ManifestError("TRAINING_PARTITION_REQUIRED")
    if evaluation.purpose is not DatasetPurpose.EVALUATION:
        raise ManifestError("EVALUATION_PARTITION_REQUIRED")
    if {s.source_key for s in training.sources} & {s.source_key for s in evaluation.sources}:
        raise ManifestError("TRAINING_EVALUATION_SOURCE_OVERLAP")
