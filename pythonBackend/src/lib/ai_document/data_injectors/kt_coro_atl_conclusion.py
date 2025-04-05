from typing import Any, List
from pprintpp import pprint
from ulid import ULID

from src.lib.ai_document.utils.get_operator_function import (
    get_operator_role,
)
from src.lib.prismaClient import prisma_client


async def coro_atl_conclusion(
    document: List[Any], chunk: Any, clinicalEventId: str, extracted_data: List[str]
) -> Any:

    conclusion = """
    """.join(
        [
            doc["children"][0]["text"]
            for doc in document
            if doc.get("widgetId", "")
            in ["01JQRMA26269G5K61NYVA8CGS6", "01JQH073H9KQYBE8HSMJ12WSRC"]
            and doc.get("type", "") == "p"
        ]
    )

    pprint(conclusion, depth=4)

    document.append(
        {
            "AiTarget": chunk["AiTarget"],
            "type": "p",
            "children": [
                {
                    "text": conclusion,
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
    extracted_data.append(conclusion)
