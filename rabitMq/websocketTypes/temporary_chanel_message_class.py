from typing import Any, Optional
from pydantic import BaseModel
from pyparsing import Enum
from ulid import ULID

from websocketTypes.general_classes import (
    OperationEnum,
    WebsocketRootMessage,
)


class TemporaryMessageDestination(str, Enum):
    ai_document = "ai_document"


class TemporaryMessageType(str, Enum):
    payload = "payload"
    milestone = "milestone"
    chunk = "chunk"


class TemporaryChanelMessage(BaseModel):
    temporaryChanelId: str
    destination: TemporaryMessageDestination
    content: Any
    id: ULID
    type: TemporaryMessageType


class TemporaryChanelMessagePayload(BaseModel):
    operation: OperationEnum
    message: TemporaryChanelMessage


class TemporaryChanelMessageType(WebsocketRootMessage):
    bashPayload: Optional[TemporaryChanelMessagePayload] = None
    payload: TemporaryChanelMessagePayload
