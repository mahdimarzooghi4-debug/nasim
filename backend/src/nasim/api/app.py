from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Annotated, Any
from uuid import UUID

from fastapi import Depends, FastAPI, Header, Query, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from nasim.application.casework import Casework
from nasim.authorization.contracts import TrustedPrincipal
from nasim.authorization.service import AuthorizationResolver
from nasim.domain.contracts import (
    AddContactPoint,
    AssignmentView,
    CaseProfileView,
    ContactView,
    CorrectCaseProfile,
    CorrectContactPoint,
    CorrectInteraction,
    CorrectObservation,
    CreateCase,
    ErrorResponse,
    InteractionView,
    ObservationView,
    Page,
    ProfileView,
    ReassignCaregiver,
    RecordInteraction,
    RecordObservation,
    TimelineEntry,
    WorkspaceView,
)
from nasim.domain.errors import DomainError
from nasim.identity_context.contracts import ActorContext
from nasim.infrastructure.config import Settings, load_settings
from nasim.infrastructure.database import make_engine, make_sessions
from nasim.infrastructure.schema import SCHEMA_REVISION
from nasim.provider_registry.contracts import (
    ProviderCandidateView,
    ProviderQualificationEvidenceView,
    ProviderQualificationReviewRequestView,
    ProviderQualificationReviewWorkspaceView,
    RecordProviderQualificationEvidence,
    RegisterProviderCandidate,
    RequestProviderQualificationReview,
)
from nasim.provider_registry.service import (
    ProviderCandidates,
    ProviderQualificationEvidence,
    ProviderQualificationReviewRequests,
    ProviderQualificationReviewWorkspace,
)
from nasim.referral.contracts import CreateReferral, ReferralView
from nasim.referral.service import Referrals


async def get_actor(request: Request) -> ActorContext:
    # Only trusted in-process identity middleware may populate this context.
    # There is deliberately no header/token parsing or development authentication bypass.
    principal = getattr(request.state, "trusted_principal", None)
    if principal is not None:
        if not isinstance(principal, TrustedPrincipal):
            raise DomainError("ACTOR_CONTEXT_REQUIRED", 401)
        return await request.app.state.authorization.resolve(principal)
    actor = getattr(request.state, "actor", None)
    if not isinstance(actor, ActorContext):
        raise DomainError("ACTOR_CONTEXT_REQUIRED", 401)
    return actor


def get_provider_candidates(request: Request) -> ProviderCandidates:
    return request.app.state.provider_candidates


def get_provider_qualification_evidence(request: Request) -> ProviderQualificationEvidence:
    return request.app.state.provider_qualification_evidence


def get_provider_qualification_review_requests(
    request: Request,
) -> ProviderQualificationReviewRequests:
    return request.app.state.provider_qualification_review_requests


def get_provider_qualification_review_workspace(
    request: Request,
) -> ProviderQualificationReviewWorkspace:
    return request.app.state.provider_qualification_review_workspace


def get_referrals(request: Request) -> Referrals:
    return request.app.state.referrals


def get_casework(request: Request) -> Casework:
    return request.app.state.casework


Actor = Annotated[ActorContext, Depends(get_actor)]
Service = Annotated[Casework, Depends(get_casework)]
ReferralService = Annotated[Referrals, Depends(get_referrals)]
ProviderCandidateService = Annotated[ProviderCandidates, Depends(get_provider_candidates)]
ProviderQualificationEvidenceService = Annotated[
    ProviderQualificationEvidence, Depends(get_provider_qualification_evidence)
]
ProviderQualificationReviewRequestService = Annotated[
    ProviderQualificationReviewRequests, Depends(get_provider_qualification_review_requests)
]
ProviderQualificationWorkspaceService = Annotated[
    ProviderQualificationReviewWorkspace, Depends(get_provider_qualification_review_workspace)
]
Key = Annotated[str, Header(alias="Idempotency-Key", min_length=1, max_length=200)]
Cursor = Annotated[str | None, Query(max_length=500)]
Limit = Annotated[int, Query(ge=1, le=100)]
ERRORS: dict[int | str, dict[str, Any]] = {
    422: {
        "model": ErrorResponse,
        "description": "VALIDATION_ERROR / INVALID_CURSOR / NEED_CAPTURE_REQUIRED",
    },
    401: {"model": ErrorResponse, "description": "ACTOR_CONTEXT_REQUIRED"},
    403: {
        "model": ErrorResponse,
        "description": "CAPABILITY_REQUIRED / ASSIGNED_CAREGIVER_REQUIRED",
    },
    404: {
        "model": ErrorResponse,
        "description": (
            "CASE_NOT_FOUND / RECORD_NOT_FOUND / REFERRAL_NOT_FOUND / "
            "PROVIDER_CANDIDATE_NOT_FOUND / PROVIDER_QUALIFICATION_EVIDENCE_NOT_FOUND / "
            "PROVIDER_QUALIFICATION_REVIEW_REQUEST_NOT_FOUND"
        ),
    },
    409: {
        "model": ErrorResponse,
        "description": (
            "CASE_ASSIGNMENT_CHANGED / STALE_RECORD_REVISION / "
            "IDEMPOTENCY_KEY_REUSED_WITH_DIFFERENT_PAYLOAD"
        ),
    },
}


def create_app(settings: Settings | None = None) -> FastAPI:
    config = settings or load_settings()
    engine = make_engine(config)

    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncIterator[None]:
        yield
        await engine.dispose()

    app = FastAPI(title="Nasim TS-03", version="0.1.0", lifespan=lifespan)
    app.state.engine = engine
    app.state.casework = Casework(make_sessions(engine))
    app.state.authorization = AuthorizationResolver(make_sessions(engine))
    app.state.referrals = Referrals(make_sessions(engine))
    app.state.provider_candidates = ProviderCandidates(make_sessions(engine))
    app.state.provider_qualification_evidence = ProviderQualificationEvidence(make_sessions(engine))
    app.state.provider_qualification_review_requests = ProviderQualificationReviewRequests(
        make_sessions(engine)
    )
    app.state.provider_qualification_review_workspace = ProviderQualificationReviewWorkspace(
        make_sessions(engine)
    )

    @app.post(
        "/api/v1/provider-candidates",
        response_model=ProviderCandidateView,
        responses=ERRORS,
        status_code=201,
    )
    async def register_provider_candidate(
        body: RegisterProviderCandidate,
        actor: Actor,
        service: ProviderCandidateService,
        key: Key,
    ) -> Any:
        return await service.register(body, actor, key)

    @app.get(
        "/api/v1/provider-candidates",
        response_model=Page[ProviderCandidateView],
        responses=ERRORS,
    )
    async def list_provider_candidates(
        actor: Actor,
        service: ProviderCandidateService,
        cursor: Cursor = None,
        limit: Limit = 50,
    ) -> Any:
        return await service.list(actor, cursor, limit)

    @app.get(
        "/api/v1/provider-candidates/{candidate_id}",
        response_model=ProviderCandidateView,
        responses=ERRORS,
    )
    async def get_provider_candidate(
        candidate_id: UUID, actor: Actor, service: ProviderCandidateService
    ) -> Any:
        return await service.get(candidate_id, actor)

    @app.post(
        "/api/v1/provider-candidates/{candidate_id}/qualification-evidence",
        response_model=ProviderQualificationEvidenceView,
        responses=ERRORS,
        status_code=201,
    )
    async def record_provider_qualification_evidence(
        candidate_id: UUID,
        body: RecordProviderQualificationEvidence,
        actor: Actor,
        service: ProviderQualificationEvidenceService,
        key: Key,
    ) -> Any:
        return await service.record(candidate_id, body, actor, key)

    @app.get(
        "/api/v1/provider-candidates/{candidate_id}/qualification-evidence",
        response_model=Page[ProviderQualificationEvidenceView],
        responses=ERRORS,
    )
    async def list_provider_qualification_evidence(
        candidate_id: UUID,
        actor: Actor,
        service: ProviderQualificationEvidenceService,
        cursor: Cursor = None,
        limit: Limit = 50,
    ) -> Any:
        return await service.list(candidate_id, actor, cursor, limit)

    @app.get(
        "/api/v1/provider-qualification-evidence/{evidence_id}",
        response_model=ProviderQualificationEvidenceView,
        responses=ERRORS,
    )
    async def get_provider_qualification_evidence_record(
        evidence_id: UUID,
        actor: Actor,
        service: ProviderQualificationEvidenceService,
    ) -> Any:
        return await service.get(evidence_id, actor)

    @app.post(
        "/api/v1/provider-candidates/{candidate_id}/qualification-review-requests",
        response_model=ProviderQualificationReviewRequestView,
        responses=ERRORS,
        status_code=201,
    )
    async def request_provider_qualification_review(
        candidate_id: UUID,
        body: RequestProviderQualificationReview,
        actor: Actor,
        service: ProviderQualificationReviewRequestService,
        key: Key,
    ) -> Any:
        return await service.request(candidate_id, body, actor, key)

    @app.get(
        "/api/v1/provider-candidates/{candidate_id}/qualification-review-requests",
        response_model=Page[ProviderQualificationReviewRequestView],
        responses=ERRORS,
    )
    async def list_provider_qualification_review_requests(
        candidate_id: UUID,
        actor: Actor,
        service: ProviderQualificationReviewRequestService,
        cursor: Cursor = None,
        limit: Limit = 50,
    ) -> Any:
        return await service.list(candidate_id, actor, cursor, limit)

    @app.get(
        "/api/v1/provider-qualification-review-requests/{request_id}",
        response_model=ProviderQualificationReviewRequestView,
        responses=ERRORS,
    )
    async def get_provider_qualification_review_request(
        request_id: UUID,
        actor: Actor,
        service: ProviderQualificationReviewRequestService,
    ) -> Any:
        return await service.get(request_id, actor)

    @app.get(
        "/api/v1/provider-candidates/{candidate_id}/qualification-review-workspace",
        response_model=ProviderQualificationReviewWorkspaceView,
        responses=ERRORS,
    )
    async def get_provider_qualification_review_workspace_view(
        candidate_id: UUID,
        actor: Actor,
        service: ProviderQualificationWorkspaceService,
        evidence_cursor: Annotated[str | None, Query(max_length=500)] = None,
        request_cursor: Annotated[str | None, Query(max_length=500)] = None,
        limit: Limit = 50,
    ) -> Any:
        return await service.read(candidate_id, actor, evidence_cursor, request_cursor, limit)

    @app.post(
        "/api/v1/cases/{case_id}/referrals",
        response_model=ReferralView,
        responses=ERRORS,
        status_code=201,
    )
    async def record_referral(
        case_id: UUID, body: CreateReferral, actor: Actor, service: ReferralService, key: Key
    ) -> Any:
        return await service.create(case_id, body, actor, key)

    @app.get(
        "/api/v1/cases/{case_id}/referrals", response_model=Page[ReferralView], responses=ERRORS
    )
    async def list_referrals(
        case_id: UUID,
        actor: Actor,
        service: ReferralService,
        cursor: Cursor = None,
        limit: Limit = 50,
    ) -> Any:
        return await service.list(case_id, actor, cursor, limit)

    @app.get("/api/v1/referrals/{referral_id}", response_model=ReferralView, responses=ERRORS)
    async def get_referral(referral_id: UUID, actor: Actor, service: ReferralService) -> Any:
        return await service.get(referral_id, actor)

    @app.get("/api/v1/authorization/self", response_model=ActorContext, responses=ERRORS)
    async def authorization_self(actor: Actor) -> ActorContext:
        return actor

    @app.exception_handler(DomainError)
    async def domain_error_handler(request: Request, error: DomainError) -> JSONResponse:
        return JSONResponse(
            status_code=error.status,
            content={"error": {"code": error.code, "message": error.message}},
        )

    @app.exception_handler(RequestValidationError)
    async def validation_error_handler(
        request: Request, error: RequestValidationError
    ) -> JSONResponse:
        # Do not reflect submitted personal data or headers into error messages/logs.
        return JSONResponse(
            status_code=422,
            content={"error": {"code": "VALIDATION_ERROR", "message": "Request validation failed"}},
        )

    @app.get(
        "/health", response_model=dict[str, str], responses={503: {"description": "DB not ready"}}
    )
    async def health() -> Any:
        try:
            async with engine.connect() as connection:
                revision = await connection.scalar(text("SELECT version_num FROM alembic_version"))
            if revision != SCHEMA_REVISION:
                return JSONResponse(status_code=503, content={"status": "not_ready"})
        except (SQLAlchemyError, OSError):
            return JSONResponse(status_code=503, content={"status": "not_ready"})
        return {"status": "ok"}

    @app.post("/api/v1/cases", response_model=CaseProfileView, responses=ERRORS, status_code=201)
    async def create(body: CreateCase, actor: Actor, service: Service, key: Key) -> Any:
        return await service.mutate("create", body, actor, key)

    @app.post(
        "/api/v1/cases/{case_id}/profile/corrections",
        response_model=ProfileView,
        responses=ERRORS,
        status_code=201,
    )
    async def correct_profile(
        case_id: UUID, body: CorrectCaseProfile, actor: Actor, service: Service, key: Key
    ) -> Any:
        return await service.mutate("profile_correct", body, actor, key, case_id)

    @app.post(
        "/api/v1/cases/{case_id}/reassignments",
        response_model=AssignmentView,
        responses=ERRORS,
        status_code=201,
    )
    async def reassign(
        case_id: UUID, body: ReassignCaregiver, actor: Actor, service: Service, key: Key
    ) -> Any:
        return await service.mutate("reassign", body, actor, key, case_id)

    @app.post(
        "/api/v1/cases/{case_id}/contacts",
        response_model=ContactView,
        responses=ERRORS,
        status_code=201,
    )
    async def contact(
        case_id: UUID, body: AddContactPoint, actor: Actor, service: Service, key: Key
    ) -> Any:
        return await service.mutate("contact_add", body, actor, key, case_id)

    @app.post(
        "/api/v1/cases/{case_id}/contacts/{logical_contact_id}/corrections",
        response_model=ContactView,
        responses=ERRORS,
        status_code=201,
    )
    async def correct_contact(
        case_id: UUID,
        logical_contact_id: UUID,
        body: CorrectContactPoint,
        actor: Actor,
        service: Service,
        key: Key,
    ) -> Any:
        return await service.mutate(
            "contact_correct", body, actor, key, case_id, logical_contact_id
        )

    @app.post(
        "/api/v1/cases/{case_id}/interactions",
        response_model=InteractionView,
        responses=ERRORS,
        status_code=201,
    )
    async def interaction(
        case_id: UUID, body: RecordInteraction, actor: Actor, service: Service, key: Key
    ) -> Any:
        return await service.mutate("interaction_add", body, actor, key, case_id)

    @app.post(
        "/api/v1/cases/{case_id}/interactions/{interaction_id}/corrections",
        response_model=InteractionView,
        responses=ERRORS,
        status_code=201,
    )
    async def correct_interaction(
        case_id: UUID,
        interaction_id: UUID,
        body: CorrectInteraction,
        actor: Actor,
        service: Service,
        key: Key,
    ) -> Any:
        return await service.mutate(
            "interaction_correct", body, actor, key, case_id, interaction_id
        )

    @app.post(
        "/api/v1/cases/{case_id}/observations",
        response_model=ObservationView,
        responses=ERRORS,
        status_code=201,
    )
    async def observation(
        case_id: UUID, body: RecordObservation, actor: Actor, service: Service, key: Key
    ) -> Any:
        return await service.mutate("observation_add", body, actor, key, case_id)

    @app.post(
        "/api/v1/cases/{case_id}/observations/{observation_id}/corrections",
        response_model=ObservationView,
        responses=ERRORS,
        status_code=201,
    )
    async def correct_observation(
        case_id: UUID,
        observation_id: UUID,
        body: CorrectObservation,
        actor: Actor,
        service: Service,
        key: Key,
    ) -> Any:
        return await service.mutate(
            "observation_correct", body, actor, key, case_id, observation_id
        )

    @app.get("/api/v1/cases/{case_id}", response_model=CaseProfileView, responses=ERRORS)
    async def profile(case_id: UUID, actor: Actor, service: Service) -> Any:
        return await service.read("profile", case_id, actor)

    @app.get("/api/v1/cases/{case_id}/workspace", response_model=WorkspaceView, responses=ERRORS)
    async def workspace(case_id: UUID, actor: Actor, service: Service) -> Any:
        return await service.read("workspace", case_id, actor)

    @app.get(
        "/api/v1/cases/{case_id}/assignments", response_model=list[AssignmentView], responses=ERRORS
    )
    async def assignments(case_id: UUID, actor: Actor, service: Service) -> Any:
        return await service.read("assignments", case_id, actor)

    @app.get("/api/v1/cases/{case_id}/contacts", response_model=list[ContactView], responses=ERRORS)
    async def contacts(case_id: UUID, actor: Actor, service: Service) -> Any:
        return await service.read("contacts", case_id, actor)

    @app.get(
        "/api/v1/cases/{case_id}/interactions",
        response_model=Page[InteractionView],
        responses=ERRORS,
    )
    async def interactions(
        case_id: UUID, actor: Actor, service: Service, cursor: Cursor = None, limit: Limit = 50
    ) -> Any:
        return await service.read("interactions", case_id, actor, cursor, limit)

    @app.get(
        "/api/v1/cases/{case_id}/observations",
        response_model=Page[ObservationView],
        responses=ERRORS,
    )
    async def observations(
        case_id: UUID, actor: Actor, service: Service, cursor: Cursor = None, limit: Limit = 50
    ) -> Any:
        return await service.read("observations", case_id, actor, cursor, limit)

    @app.get(
        "/api/v1/cases/{case_id}/timeline", response_model=Page[TimelineEntry], responses=ERRORS
    )
    async def timeline(
        case_id: UUID, actor: Actor, service: Service, cursor: Cursor = None, limit: Limit = 50
    ) -> Any:
        return await service.read("timeline", case_id, actor, cursor, limit)

    return app
