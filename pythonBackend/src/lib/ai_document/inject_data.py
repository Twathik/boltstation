from typing import Any, List
from src.lib.ai_document.data_injectors.inject_data_from_chunk import (
    inject_data_from_chunk,
)
from src.lib.ai_document.data_injectors.kt_material_injector import material_injector
from src.lib.ai_document.data_injectors.kt_operator_injector import operator_injector


async def inject_data(
    document: List[Any], chunk: Any, clinicalEventId: str, extracted_data: List[str]
) -> Any:

    if "widgetId" in chunk:
        match chunk["widgetId"]:
            # operator injector
            case "01JN67WHFRRKW29MDDXH5CYNGJ":
                await inject_data_from_chunk(
                    chunk=chunk,
                    clinicalEventId=clinicalEventId,
                    document=document,
                    widget_id="01JN67WHFRRKW29MDDXH5CYNGJ",
                    injector=operator_injector,
                    extracted_data=extracted_data,
                )
            case "01JN8ZP7XYNEK0YRZ7H0M20GBV":

                await inject_data_from_chunk(
                    chunk=chunk,
                    clinicalEventId=clinicalEventId,
                    document=document,
                    widget_id="01JN8ZP7XYNEK0YRZ7H0M20GBV",
                    injector=material_injector,
                    extracted_data=extracted_data,
                )

            case _:
                document.append(chunk)
    else:
        document.append(chunk)

    pass
