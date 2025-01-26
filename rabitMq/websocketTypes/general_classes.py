# Define Enum for sexe
from typing import Awaitable, Callable, List
from pydantic import BaseModel
from pyparsing import Enum
from ulid import ULID


AsyncVoidFunction = Callable[[], Awaitable[None]]


class SexeEnum(str, Enum):
    F = "F"
    M = "M"


class OperationEnum(str, Enum):
    add = "add"
    remove = "remove"
    publish = "publish"


class MessageDestination(str, Enum):
    Patient_identity_document = "Patient-identity-document"
    temporaryChanel = "temporaryChanel"


class WebsocketRootMessage(BaseModel):
    type: MessageDestination
    destination: List[MessageDestination]
    globalMessage: bool
    id: ULID  # Use ULID string
    subscriptionIds: List[str]
