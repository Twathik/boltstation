from typing import Any, List
from ulid import ULID

from src.lib.ai_document.utils.get_operator_function import (
    get_operator_role,
)
from src.lib.prismaClient import prisma_client


async def drugs_description(
    document: List[Any], chunk: Any, clinicalEventId: str, extracted_data: List[str]
) -> Any:

    clinical_event = await prisma_client.clinicalevent.find_first_or_raise(
        where={"id": clinicalEventId},
    )

    description = clinical_event.jsonData["procedurePrescriptionDescription"]

    document.append(
        {
            "AiTarget": chunk["AiTarget"],
            "type": "p",
            "children": [
                {
                    "text": description,
                    "refactor": True,
                },
            ],
            "id": str(ULID()),
            "optionalWidget": False,
            "widgetId": chunk["widgetId"],
            "widgetName": chunk["widgetName"],
            "injected": True,
        }
    )
    extracted_data.append(description)
