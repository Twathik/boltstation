from typing import Any, List
from ulid import ULID

from pprintpp import pprint

from src.lib.ai_document.utils.get_operator_function import (
    get_operator_function,
    get_operator_role,
)
from src.lib.prismaClient import prisma_client


async def operator_injector(
    document: List[Any], chunk: Any, clinicalEventId: str, extracted_data: List[str]
) -> Any:

    operators = await prisma_client.clinicalevent_interventionoperator.find_many(
        where={"clinicalEventId": clinicalEventId},
        include={"interventionOperator": True},
    )

    for operator in operators:

        document.append(
            {
                "AiTarget": False,
                "type": "p",
                "children": [
                    {
                        "text": f"{get_operator_role(role=operator.role)}: ",
                        "bold": True,
                    },
                    {"text": f"{operator.interventionOperator.operatorName}"},
                ],
                "id": str(ULID()),
                "optionalWidget": False,
                "indent": 1,
                "listStyleType": "disc",
                "widgetId": chunk["widgetId"],
                "widgetName": chunk["widgetName"],
                "injected": True,
            }
        )
        extracted_data.append(
            f"{get_operator_role(role=operator.role)}: {operator.interventionOperator.operatorName}"
        )
        pass
