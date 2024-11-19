from typing import List, Optional
from pydantic import BaseModel, Field
from ulid import ULID

from lib.websocketTypes.general_classes import (
    OperationEnum,
    SexeEnum,
    WebsocketRootMessage,
)


class ProcessedData(BaseModel):
    last_name: Optional[str] = Field(
        description="the string most likely corresponding to the last name, can be near Nom:",
        default=None,
    )
    first_name: Optional[str] = Field(
        description="the string most likely corresponding to the first name, can be near Nom:",
        default=None,
    )
    dob: Optional[str] = Field(
        description="the date of birth converted in the format yyyy-MM-dd", default=None
    )
    blood_type: Optional[str] = Field(
        description="the string most likely corresponding to the blood type",
        default=None,
    )
    national_identifier: Optional[str] = Field(
        description="the string most likely corresponding to the national Id, containing 9 digits",
        default=None,
    )


class PatientIdentityDocument(BaseModel):
    id: Optional[str]
    identityDocumentUrls: List[str]
    processedData: Optional[ProcessedData] = None
    sexe: SexeEnum
    elapsedTime: float


class Payload(BaseModel):
    operation: OperationEnum
    PatientIdentityDocument: PatientIdentityDocument


class AddPatientIdentityDocumentMessage(WebsocketRootMessage):
    bashPayload: Optional[Payload] = None
    payload: Payload
