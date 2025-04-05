from typing import Any, List

from src.lib.ai_document.utils.ai_document_classes import ProcedureDetails

from src.lib.ai_document.utils.plate_general_utils import (
    append_generated_text,
    replace_none,
)
from src.lib.prismaClient import prisma_client


async def procedure_details_injector(
    document: List[Any], chunk: Any, clinicalEventId: str, extracted_data: List[str]
) -> Any:

    clinical_event = await prisma_client.clinicalevent.find_first_or_raise(
        where={"id": clinicalEventId},
    )

    procedure = ProcedureDetails.model_validate(
        clinical_event.jsonData["procedureDetails"]
    )

    if procedure.startTime is not None or procedure.endTime is not None:
        append_generated_text(
            document,
            chunk,
            extracted_data,
            text=[
                {"text": "Heure de début - fin: ", "bold": True},
                {
                    "text": f"{replace_none(procedure.startTime)} min - {replace_none(procedure.endTime)} min."
                },
            ],
        )

    if procedure.procedureDuration is not None:

        append_generated_text(
            document,
            chunk,
            extracted_data,
            text=[
                {"text": "Durée: ", "bold": True},
                {"text": f"{int(replace_none(procedure.procedureDuration))} min."},
            ],
        )

    if procedure.anesthesia is not None:

        append_generated_text(
            document,
            chunk,
            extracted_data,
            text=[
                {"text": "Type d’anesthésie: ", "bold": True},
                {"text": procedure.anesthesia},
            ],
        )

    if procedure.rayDuration is not None or procedure.graphyDuration is not None:

        append_generated_text(
            document,
            chunk,
            extracted_data,
            text=[
                {"text": "Durée scopie - graphie: ", "bold": True},
                {
                    "text": f"{int(replace_none(procedure.rayDuration))} min - {int(replace_none(procedure.graphyDuration))} min"
                },
            ],
        )

    if procedure.clairance is not None:

        append_generated_text(
            document,
            chunk,
            extracted_data,
            text=[
                {"text": "Clairance de la créatinine: ", "bold": True},
                {"text": f"{int(replace_none(procedure.clairance))} ml/min/m2"},
            ],
        )

    if procedure.contrastDose is not None:

        append_generated_text(
            document,
            chunk,
            extracted_data,
            text=[
                {"text": "Dose de contraste: ", "bold": True},
                {"text": f"{int(replace_none(procedure.contrastDose))} ml"},
            ],
        )

    if procedure.primaryShift is not None:

        append_generated_text(
            document,
            chunk,
            extracted_data,
            text=[
                {"text": "Voie artérielle primaire: ", "bold": True},
                {
                    "text": f"Une voie d'abord {replace_none(procedure.primaryShift)}{f" {procedure.primaryShiftSize}" if procedure.primaryShiftSize is not None and not procedure.primaryShiftSize == 'other' else ''} {"n'a pas pu être réalisée" if procedure.primaryFailure else 'a été mise en place avec succès' }. La fermeture de la voie d'abord {"a été soldée d’échec." if procedure.primaryClosureFailure else 'a été réalisée avec succès.'}"
                },
            ],
        )

    if procedure.secondaryShift is not None:

        append_generated_text(
            document,
            chunk,
            extracted_data,
            text=[
                {"text": "Voie artérielle secondaire: ", "bold": True},
                {
                    "text": f"Une voie d'abord {replace_none(procedure.secondaryShift)}{f" {procedure.secondaryShiftSize}" if procedure.secondaryShiftSize is not None and not procedure.secondaryShiftSize == 'other' else ''} {"n'a pas pu être réalisée" if procedure.secondaryFailure else 'a été mise en place avec succès' }. La fermeture de la voie d'abord {"a été soldée d’échec." if procedure.secondaryClosureFailure else 'a été réalisée avec succès.'}"
                },
            ],
        )

    if procedure.tertiaryShift is not None:

        append_generated_text(
            document,
            chunk,
            extracted_data,
            text=[
                {"text": "Voie artérielle tertiaire: ", "bold": True},
                {
                    "text": f"Une voie d'abord {replace_none(procedure.tertiaryShift)}{f" {procedure.tertiaryShiftSize}" if procedure.tertiaryShiftSize is not None and not procedure.tertiaryShiftSize == 'other' else ''} {"n'a pas pu être réalisée" if procedure.tertiaryFailure else 'a été mise en place avec succès' }. La fermeture de la voie d'abord {"a été soldée d’échec." if procedure.tertiaryClosureFailure else 'a été réalisée avec succès.'}"
                },
            ],
        )

    if procedure.venousPrimaryShift is not None:

        append_generated_text(
            document,
            chunk,
            extracted_data,
            text=[
                {"text": "Voie veineuse primaire: ", "bold": True},
                {
                    "text": f"Une voie d'abord {replace_none(procedure.venousPrimaryShift)}{f" {procedure.venousPrimaryShiftSize}" if procedure.venousPrimaryShiftSize is not None and not procedure.venousPrimaryShiftSize == 'other' else ''} {"n'a pas pu être réalisée" if procedure.venousPrimaryFailure else 'a été mise en place avec succès' }. La fermeture de la voie d'abord {"a été soldée d’échec." if procedure.venousPrimaryClosureFailure else 'a été réalisée avec succès.'}"
                },
            ],
        )

    if procedure.venousSecondaryShift is not None:

        append_generated_text(
            document,
            chunk,
            extracted_data,
            text=[
                {"text": "Voie veineuse secondaire: ", "bold": True},
                {
                    "text": f"Une voie d'abord {replace_none(procedure.venousSecondaryShift)}{f" {procedure.venousSecondaryShiftSize}" if procedure.venousSecondaryShiftSize is not None and not procedure.venousSecondaryShiftSize == 'other' else ''} {"n'a pas pu être réalisée" if procedure.venousSecondaryFailure else 'a été mise en place avec succès' }. La fermeture de la voie d'abord {"a été soldée d’échec." if procedure.venousSecondaryClosureFailure else 'a été réalisée avec succès.'}"
                },
            ],
        )

    if procedure.venousTertiaryShift is not None:

        append_generated_text(
            document,
            chunk,
            extracted_data,
            text=[
                {"text": "Voie veineuse tertiaire: ", "bold": True},
                {
                    "text": f"Une voie d'abord {replace_none(procedure.venousTertiaryShift)}{f" {procedure.venousTertiaryShiftSize}" if procedure.venousTertiaryShiftSize is not None and not procedure.venousTertiaryShiftSize == 'other' else ''} {"n'a pas pu être réalisée" if procedure.venousTertiaryFailure else 'a été mise en place avec succès' }. La fermeture de la voie d'abord {"a été soldée d’échec." if procedure.venousTertiaryClosureFailure else 'a été réalisée avec succès.'}"
                },
            ],
        )

    if procedure.circulatorySupport is not None:

        append_generated_text(
            document,
            chunk,
            extracted_data,
            text=[
                {"text": "Assistance circulatoire: ", "bold": True},
                {
                    "text": f'Durant la procédure, Nous avons eu recours une assistance circulatoire de type "{procedure.circulatorySupport}"'
                },
            ],
        )
