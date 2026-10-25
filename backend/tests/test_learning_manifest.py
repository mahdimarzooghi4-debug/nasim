"""Synthetic-only Dataset manifest tests. NO actual elder, provider or Training data."""

from dataclasses import FrozenInstanceError, replace
from uuid import UUID, uuid4

import pytest

from nasim.learning.dataset_manifest import (
    AdmissionEvidence,
    AdmissionUnavailable,
    CuratedSourceRef,
    DatasetAdmissionRequest,
    DatasetPurpose,
    ManifestError,
    VersionedManifestBuilder,
    verify_partition_isolation,
)

A = "a" * 64
B = "b" * 64
C = "c" * 64
D = "d" * 64


def source(
    record_id: UUID | None = None,
    namespace: str = "synthetic.case",
    version: str = A,
    curation: str = B,
) -> CuratedSourceRef:
    return CuratedSourceRef(
        namespace=namespace,
        source_id=record_id or uuid4(),
        source_version_sha256=version,
        curation_evidence_sha256=curation,
    )


def membership(sources: tuple[CuratedSourceRef, ...]) -> frozenset[tuple[str, str, str, str]]:
    return frozenset(
        (
            item.namespace,
            str(item.source_id),
            item.source_version_sha256,
            item.curation_evidence_sha256,
        )
        for item in sources
    )


class SyntheticOnlyAdmission:
    """Test fake. Not deployed or referenced by production app/runtime."""

    def __init__(
        self,
        *,
        policy: str = C,
        approval: str = D,
        admitted: frozenset[tuple[str, str, str, str]] | None = None,
    ) -> None:
        self.policy = policy
        self.approval = approval
        self.admitted = admitted

    def verify(self, request: DatasetAdmissionRequest) -> AdmissionEvidence:
        return AdmissionEvidence(
            policy_sha256=self.policy,
            approval_evidence_sha256=self.approval,
            eligible_sources=(
                self.admitted if self.admitted is not None else membership(request.sources)
            ),
        )


def test_unconfigured_default_builder_fails_closed_even_for_valid_curated_reference():
    item = source()
    with pytest.raises(AdmissionUnavailable, match="TRAINING_ELIGIBILITY_POLICY_NOT_APPROVED"):
        VersionedManifestBuilder().build(DatasetPurpose.TRAINING, [item])


def test_empty_batch_or_unsupported_purpose_cannot_create_even_with_test_verifier():
    builder = VersionedManifestBuilder(SyntheticOnlyAdmission())
    with pytest.raises(ManifestError, match="EMPTY_OR_INVALID"):
        builder.build(DatasetPurpose.TRAINING, [])
    with pytest.raises(ManifestError, match="INVALID_DATASET_PURPOSE"):
        builder.build("TRAINING", [source()])  # type: ignore[arg-type]


@pytest.mark.parametrize(
    ("field", "value", "reason"),
    [
        ("namespace", "", "INVALID_SOURCE_NAMESPACE"),
        ("namespace", " ", "INVALID_SOURCE_NAMESPACE"),
        ("namespace", "n" * 201, "INVALID_SOURCE_NAMESPACE"),
        ("source_version_sha256", "not-a-hash", "INVALID_SHA256"),
        ("source_version_sha256", "A" * 64, "INVALID_SHA256"),
        ("curation_evidence_sha256", "b" * 63, "INVALID_SHA256"),
    ],
)
def test_invalid_source_references_are_rejected_before_membership_admission(field, value, reason):
    values = {
        "namespace": "synthetic.case",
        "source_id": uuid4(),
        "source_version_sha256": A,
        "curation_evidence_sha256": B,
    }
    values[field] = value
    with pytest.raises(ManifestError, match=reason):
        CuratedSourceRef(**values)


def test_duplicate_or_competing_version_of_same_source_fails_before_admission():
    current = source()
    another_version = replace(current, source_version_sha256=C)
    builder = VersionedManifestBuilder(SyntheticOnlyAdmission())
    with pytest.raises(ManifestError, match="DUPLICATE_SOURCE_IDENTITY"):
        builder.build(DatasetPurpose.TRAINING, [current, current])
    with pytest.raises(ManifestError, match="DUPLICATE_SOURCE_IDENTITY"):
        builder.build(DatasetPurpose.TRAINING, [current, another_version])


def test_policy_verifier_must_explicitly_attest_to_exact_all_membership():
    one, two = source(), source()
    request = (one, two)
    subset = VersionedManifestBuilder(SyntheticOnlyAdmission(admitted=membership((one,))))
    with pytest.raises(AdmissionUnavailable, match="UNAPPROVED_OR_STALE"):
        subset.build(DatasetPurpose.TRAINING, request)
    surplus = VersionedManifestBuilder(
        SyntheticOnlyAdmission(admitted=membership((one, two, source())))
    )
    with pytest.raises(AdmissionUnavailable, match="UNAPPROVED_OR_STALE"):
        surplus.build(DatasetPurpose.TRAINING, request)
    stale = VersionedManifestBuilder(
        SyntheticOnlyAdmission(admitted=membership((replace(one, curation_evidence_sha256=C), two)))
    )
    with pytest.raises(AdmissionUnavailable, match="UNAPPROVED_OR_STALE"):
        stale.build(DatasetPurpose.TRAINING, request)


def test_invalid_or_non_admission_verifier_result_never_authorizes_manifest():
    class NonVerifier:
        def verify(self, request: DatasetAdmissionRequest) -> object:
            return True

    builder = VersionedManifestBuilder(NonVerifier())  # type: ignore[arg-type]
    with pytest.raises(AdmissionUnavailable, match="INVALID_ADMISSION_EVIDENCE"):
        builder.build(DatasetPurpose.TRAINING, [source()])


def test_deterministic_manifest_identity_independent_of_input_order_and_replay():
    records = (source(), source(), source())
    builder = VersionedManifestBuilder(SyntheticOnlyAdmission())
    a = builder.build(DatasetPurpose.TRAINING, records)
    b = builder.build(DatasetPurpose.TRAINING, reversed(records))
    c = builder.build(DatasetPurpose.TRAINING, records)
    assert a == b == c
    assert a.manifest_sha256 == b.manifest_sha256
    assert len(a.sources) == len(records)
    assert tuple(a.sources) == tuple(
        sorted(
            records,
            key=lambda s: (
                s.namespace,
                str(s.source_id),
                s.source_version_sha256,
                s.curation_evidence_sha256,
            ),
        )
    )
    assert a.to_dict()["manifest_id"] == str(a.manifest_id)


def test_policy_approval_purpose_or_content_change_yields_new_immutable_identity():
    item = source()
    baseline = VersionedManifestBuilder(SyntheticOnlyAdmission()).build(
        DatasetPurpose.TRAINING, [item]
    )
    new_policy = VersionedManifestBuilder(SyntheticOnlyAdmission(policy=D)).build(
        DatasetPurpose.TRAINING, [item]
    )
    new_approval = VersionedManifestBuilder(SyntheticOnlyAdmission(approval=C)).build(
        DatasetPurpose.TRAINING, [item]
    )
    new_purpose = VersionedManifestBuilder(SyntheticOnlyAdmission()).build(
        DatasetPurpose.EVALUATION, [item]
    )
    new_version = VersionedManifestBuilder(SyntheticOnlyAdmission()).build(
        DatasetPurpose.TRAINING, [replace(item, source_version_sha256=D)]
    )
    assert (
        len(
            {
                manifest.manifest_id
                for manifest in (baseline, new_policy, new_approval, new_purpose, new_version)
            }
        )
        == 5
    )
    with pytest.raises(FrozenInstanceError):
        baseline.__setattr__("policy_sha256", D)


def test_partition_overlap_blocked_even_when_source_versions_differ():
    identity = uuid4()
    training = VersionedManifestBuilder(SyntheticOnlyAdmission()).build(
        DatasetPurpose.TRAINING, [source(record_id=identity, version=A)]
    )
    evaluation = VersionedManifestBuilder(SyntheticOnlyAdmission()).build(
        DatasetPurpose.EVALUATION, [source(record_id=identity, version=C)]
    )
    with pytest.raises(ManifestError, match="TRAINING_EVALUATION_SOURCE_OVERLAP"):
        verify_partition_isolation(training, evaluation)


def test_separate_source_ids_do_not_prove_household_level_independence():
    # This only proves technical exact-ID non-overlap; NOT a sufficient
    # evaluation policy. Future household lineage must be checked upstream.
    builder = VersionedManifestBuilder(SyntheticOnlyAdmission())
    training = builder.build(DatasetPurpose.TRAINING, [source()])
    evaluation = builder.build(DatasetPurpose.EVALUATION, [source()])
    assert verify_partition_isolation(training, evaluation) is None
    with pytest.raises(ManifestError, match="TRAINING_PARTITION_REQUIRED"):
        verify_partition_isolation(evaluation, training)


def test_manifest_exposes_only_opaque_ids_and_evidence_digests_no_source_text():
    record = source()
    result = VersionedManifestBuilder(SyntheticOnlyAdmission()).build(
        DatasetPurpose.TRAINING, [record]
    )
    text = str(result.to_dict())
    assert "elder_reference" not in text
    assert "contact_value" not in text
    assert "content" not in text
    assert "reason" not in text
    assert str(record.source_id) in text


def test_evidence_must_be_sha256_and_may_not_be_empty():
    with pytest.raises(ManifestError, match="INVALID_SHA256"):
        AdmissionEvidence("not-a-digest", D, frozenset({("x", str(uuid4()), A, B)}))
    with pytest.raises(AdmissionUnavailable, match="NO_POLICY_ELIGIBLE_SOURCES"):
        AdmissionEvidence(C, D, frozenset())
