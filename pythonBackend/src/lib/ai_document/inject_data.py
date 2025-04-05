from typing import Any, List, Callable, Dict
from src.lib.ai_document.data_injectors.generate_coronarography.prompts.initial_coronarography_report import (
    initial_coronarography_report,
)
from src.lib.ai_document.data_injectors.inject_data_from_chunk import (
    inject_data_from_chunk,
)
from src.lib.ai_document.data_injectors.kt_angioplastie_coronaire import (
    kt_angioplastie_coronaire,
)
from src.lib.ai_document.data_injectors.kt_bypass_description import (
    bypass_description,
)
from src.lib.ai_document.data_injectors.kt_context_clinique import (
    context_clinique_injector,
)
from src.lib.ai_document.data_injectors.kt_coro_atl_conclusion import (
    coro_atl_conclusion,
)
from src.lib.ai_document.data_injectors.kt_coro_general_anatomy import (
    coro_general_anatomy_injector,
)
from src.lib.ai_document.data_injectors.kt_coro_lesion_description import (
    coro_lesion_description,
)
from src.lib.ai_document.data_injectors.kt_drugs_description import drugs_description
from src.lib.ai_document.data_injectors.kt_material_injector import material_injector
from src.lib.ai_document.data_injectors.kt_operator_injector import operator_injector
from src.lib.ai_document.data_injectors.kt_procedure_details import (
    procedure_details_injector,
)
from src.lib.ai_document.data_injectors.generate_coronarography.prompts.KT_angioplasty_procedure_prompt import (
    angioplasty_procedure_prompt,
)
from src.lib.ai_document.data_injectors.generate_coronarography.prompts.KT_drug_prescription import (
    drug_prescription,
)
from src.lib.ai_document.data_injectors.generate_coronarography.prompts.KT_coro_atl_conclusion import (
    coro_atl_conclusion_prompt,
)


# Mapping widgetIds to their corresponding injectors
WIDGET_INJECTORS: Dict[str, Callable] = {
    "01JN67WHFRRKW29MDDXH5CYNGJ": operator_injector,
    "01JN8ZP7XYNEK0YRZ7H0M20GBV": material_injector,
    "01JQGZVQ5PFFQ0D2JHNSWQHXG5": procedure_details_injector,
    "01JQGZYFAZ3YRHT1J68RFAP461": context_clinique_injector,
    "01JQH0173M1Y6ERZM9H9AJ2M1S": coro_general_anatomy_injector,
    "01JQRMA26269G5K61NYVA8CGS6": coro_lesion_description,
    "01JQH05AE47JME3B887ZEEH3P8": bypass_description,
    "01JQH073H9KQYBE8HSMJ12WSRC": kt_angioplastie_coronaire,
    "01JQH09C3P4ZNS3TTXYNHG7K1F": drugs_description,
    "01JQH0CFE64JG4VD7KNF0WYY7P": coro_atl_conclusion,
}

WIDGET_PROMPTS: Dict[str, Callable] = {
    "01JQRMA26269G5K61NYVA8CGS6": initial_coronarography_report,
    "01JQH073H9KQYBE8HSMJ12WSRC": angioplasty_procedure_prompt,
    "01JQH09C3P4ZNS3TTXYNHG7K1F": drug_prescription,
    "01JQH0CFE64JG4VD7KNF0WYY7P": coro_atl_conclusion_prompt,
}


async def inject_data(
    document: List[Any], chunk: Any, clinicalEventId: str, extracted_data: List[str]
) -> None:
    widget_id = chunk.get("widgetId")

    if widget_id and widget_id in WIDGET_INJECTORS:
        await inject_data_from_chunk(
            chunk=chunk,
            clinicalEventId=clinicalEventId,
            document=document,
            widget_id=widget_id,
            injector=WIDGET_INJECTORS[widget_id],
            extracted_data=extracted_data,
        )
    else:
        document.append(chunk)
