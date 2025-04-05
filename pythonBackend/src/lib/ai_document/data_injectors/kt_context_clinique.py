from typing import Any, List


from src.lib.ai_document.utils.ai_document_classes import (
    CoronarographyClinicalContext,
)


from src.lib.ai_document.utils.plate_general_utils import (
    append_generated_text,
    replace_none,
)
from src.lib.prismaClient import prisma_client


async def context_clinique_injector(
    document: List[Any], chunk: Any, clinicalEventId: str, extracted_data: List[str]
) -> Any:

    clinical_event = await prisma_client.clinicalevent.find_first_or_raise(
        where={"id": clinicalEventId},
    )

    procedure = CoronarographyClinicalContext.model_validate(
        clinical_event.jsonData["clinicalExamState"]
    )

    if procedure.weight is not None and not procedure.weight == 0:
        append_generated_text(
            document,
            chunk,
            extracted_data,
            text=[
                {"text": "Poids: ", "bold": True},
                {"text": f"{replace_none(procedure.BMI)} Kg"},
            ],
        )

    if procedure.length is not None and not procedure.length == 0:
        append_generated_text(
            document,
            chunk,
            extracted_data,
            text=[
                {"text": "Taille: ", "bold": True},
                {"text": f"{replace_none(procedure.length)} cm"},
            ],
        )

    if procedure.BMI is not None and not procedure.BMI == 0:
        append_generated_text(
            document,
            chunk,
            extracted_data,
            text=[
                {"text": "BMI: ", "bold": True},
                {"text": f"{replace_none(procedure.BMI)} kg/m2"},
            ],
        )

    if procedure.diagnostic is not None:
        append_generated_text(
            document,
            chunk,
            extracted_data,
            text=[
                {"text": "Diagnostic d'admission: \n", "bold": True},
                {"text": procedure.diagnostic},
            ],
        )
    if procedure.history is not None:
        append_generated_text(
            document,
            chunk,
            extracted_data,
            text=[
                {"text": "Antécédents: \n", "bold": True},
                {"text": procedure.history},
            ],
        )

    if procedure.clinical_exam is not None:
        append_generated_text(
            document,
            chunk,
            extracted_data,
            text=[
                {"text": "Examen clinique: \n", "bold": True},
                {"text": procedure.clinical_exam},
            ],
        )
    if procedure.electric is not None:
        append_generated_text(
            document,
            chunk,
            extracted_data,
            text=[
                {"text": "ECG: \n", "bold": True},
                {"text": procedure.electric},
            ],
        )
    if procedure.ischemicTest is not None:
        append_generated_text(
            document,
            chunk,
            extracted_data,
            text=[
                {"text": "Test d’ischémie: \n", "bold": True},
                {"text": procedure.ischemicTest},
            ],
        )
