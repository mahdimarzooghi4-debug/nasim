import base64
import json
from datetime import datetime
from uuid import UUID

from nasim.domain.errors import DomainError


def encode_cursor(time: datetime, identifier: UUID) -> str:
    return base64.urlsafe_b64encode(
        json.dumps([time.isoformat(), str(identifier)]).encode()
    ).decode()


def decode_cursor(cursor: str) -> tuple[datetime, UUID]:
    try:
        values = json.loads(base64.b64decode(cursor, altchars=b"-_", validate=True))
        if not isinstance(values, list) or len(values) != 2:
            raise ValueError
        time = datetime.fromisoformat(values[0])
        if time.tzinfo is None:
            raise ValueError
        return time, UUID(values[1])
    except (ValueError, TypeError, KeyError, UnicodeDecodeError) as error:
        raise DomainError("INVALID_CURSOR", 422) from error
