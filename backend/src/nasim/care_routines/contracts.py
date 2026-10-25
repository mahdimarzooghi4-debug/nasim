"""Configurable recurring elder-care routines and explicit human acknowledgements."""

from datetime import date, time
from typing import Literal
from uuid import UUID
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from pydantic import AwareDatetime, Field, field_validator, model_validator

from nasim.domain.contracts import AssignedCommand, Contract, Text
from nasim.identity_context.contracts import ActorType

CARE_ROUTINE_PERMISSIONS = (
    "care_routine.manage.assigned",
    "care_routine.read.assigned",
    "care_routine.event.record.assigned",
    "care_routine.event.read.assigned",
)


class RoutineSchedule(Contract):
    timezone: str = Field(min_length=1, max_length=100)
    local_time: time
    cadence: Literal["DAILY", "WEEKLY"]
    weekdays: list[int] = Field(default_factory=list, max_length=7)

    @field_validator("timezone")
    @classmethod
    def valid_timezone(cls, value: str) -> str:
        try:
            ZoneInfo(value)
        except (ZoneInfoNotFoundError, ValueError) as exc:
            raise ValueError("A valid IANA time zone is required") from exc
        return value

    @field_validator("local_time")
    @classmethod
    def local_time_has_no_offset(cls, value: time) -> time:
        if value.tzinfo is not None:
            raise ValueError("Use local_time with the separately declared IANA time zone")
        return value

    @field_validator("weekdays")
    @classmethod
    def unique_weekdays(cls, value: list[int]) -> list[int]:
        if len(set(value)) != len(value) or any(day < 0 or day > 6 for day in value):
            raise ValueError("weekdays must contain unique values from 0 to 6")
        return sorted(value)

    @model_validator(mode="after")
    def cadence_days(self) -> "RoutineSchedule":
        if self.cadence == "DAILY" and self.weekdays:
            raise ValueError("DAILY schedules must not specify weekdays")
        if self.cadence == "WEEKLY" and not self.weekdays:
            raise ValueError("WEEKLY schedules must specify at least one weekday")
        return self


class CreateCareRoutine(AssignedCommand):
    routine_type: Literal["APP_REMINDER", "CAREGIVER_TASK"]
    title: Text
    schedule: RoutineSchedule
    active: bool = True
    supersedes_routine_id: UUID | None = None


class CareRoutineView(Contract):
    id: UUID
    case_id: UUID
    routine_type: Literal["APP_REMINDER", "CAREGIVER_TASK"]
    title: str
    schedule: RoutineSchedule
    active: bool
    supersedes_routine_id: UUID | None
    recorded_at: AwareDatetime
    recorded_by_actor_id: str
    recorded_by_actor_type: ActorType
    correlation_id: str


class RecordCareRoutineEvent(AssignedCommand):
    occurrence_date: date
    status: Literal["DONE", "NOT_DONE", "SKIPPED"]
    occurred_at: AwareDatetime


class CareRoutineEventView(Contract):
    id: UUID
    case_id: UUID
    routine_id: UUID
    occurrence_date: date
    status: Literal["DONE", "NOT_DONE", "SKIPPED"]
    occurred_at: AwareDatetime
    recorded_at: AwareDatetime
    recorded_by_actor_id: str
    recorded_by_actor_type: ActorType
    correlation_id: str
