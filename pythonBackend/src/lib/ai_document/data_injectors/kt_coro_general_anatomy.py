from typing import Any, List


from src.lib.ai_document.utils.ai_document_classes import (
    GeneralAnatomySchema,
)


from src.lib.ai_document.utils.plate_general_utils import (
    append_generated_text,
)
from src.lib.prismaClient import prisma_client


async def coro_general_anatomy_injector(
    document: List[Any], chunk: Any, clinicalEventId: str, extracted_data: List[str]
) -> Any:

    clinical_event = await prisma_client.clinicalevent.find_first_or_raise(
        where={"id": clinicalEventId},
    )

    procedure = GeneralAnatomySchema.model_validate(
        clinical_event.jsonData["generalAnatomy"]
    )

    if procedure.dominance is not None:
        append_generated_text(
            document,
            chunk,
            extracted_data,
            text=[
                {"text": "Dominance: ", "bold": True},
                {
                    "text": (
                        "Le réseau coronaire est codominant. "
                        if procedure.dominance == "codominance"
                        else (
                            "Le reseau coronaire présente une dominance droite. "
                            if procedure.dominance == "droite"
                            else "Le reseau coronaire présente une dominance gauche. "
                        )
                    )
                },
            ],
        )

    append_generated_text(
        document,
        chunk,
        extracted_data,
        text=[
            {"text": "Réseau coronaire: ", "bold": True},
            {
                "text": f"Le tronc commun gauche {"est de taille normale" if procedure.SizeLM=='normal' else "est tres court en cannon de fusil" if procedure.SizeLM=='cannon de fusile' else "est court" if procedure.SizeLM=='court' else "est long"}.{" Nous notons la présence d'une artère bissectrice." if procedure.presentBissec else ""}{' La coronaire droite est de taille rudimentaire.' if procedure.rudimentaryRCD else ""}"
            },
        ],
    )

    if (
        procedure.OrigineLM is not None
        or procedure.OrigineRCD is not None
        or procedure.OrigineLAD is not None
        or procedure.OrigineCx is not None
    ):
        append_generated_text(
            document,
            chunk,
            extracted_data,
            text=[
                {"text": "Anomalies de naissance: ", "bold": True},
                {
                    "text": f"{f"Le tronc commun gauche présente une anomalie de naissance {"(naissance à partir du sinus de valsalva droit). " if procedure.OrigineLM == 'sinus Valsalva droit' else "(naissance à partir de la coronaire droite). " if procedure.OrigineLM == 'CD' else ""}" if procedure.OrigineLM is not None else ". "}{f"L'interventriculaire antérieure présente une anomalie de naissance {"(naissance à partir du sinus de valsalva droit). " if procedure.OrigineLAD == 'sinus Valsalva droit' else "(naissance à partir de la coronaire droite). " if procedure.OrigineLAD == 'CD' else "(naissance à partir du sinus de valsalva gauche). " if procedure.OrigineLAD == 'sinus Valsalva gauche'else ". "}" if procedure.OrigineLAD is not None else ""}{f"L'artère circonflexe présente une anomalie de naissance {"(naissance à partir du sinus de valsalva droit). " if procedure.OrigineCx == 'sinus Valsalva droit' else "(naissance à partir de la coronaire droite). " if procedure.OrigineCx == 'CD' else "(naissance à partir du sinus de valsalva gauche). " if procedure.OrigineCx == 'sinus Valsalva gauche'else ". "}" if procedure.OrigineCx is not None else ""}{f"L'artère coronaire droite présente une anomalie de naissance {"(naissance à partir du tronc commun gauche). " if procedure.OrigineRCD == 'Tronc commun gauche' else "(naissance à partir du sinus de valsalva gauche). " if procedure.OrigineRCD == 'sinus Valsalva gauche'else ". "}" if procedure.OrigineRCD is not None else ""}"
                },
            ],
        )
    fistule: List[str] = []
    if procedure.fistuleLAD is not None:
        fistule.append("l'interventriculaire antérieure")
    if procedure.fistuleCx is not None:
        fistule.append("l'artère circonflexe")
    if procedure.fistuleRCD is not None:
        fistule.append("la coronaire droite")

    if (
        procedure.fistuleLAD is not None
        or procedure.fistuleCx is not None
        or procedure.fistuleRCD is not None
    ):
        append_generated_text(
            document,
            chunk,
            extracted_data,
            text=[
                {"text": "Fistule coronaire: ", "bold": True},
                {
                    "text": f"Nous remarquons la présence d'une fistule coronaire s'abouchant dans les cavité cardiaques au niveau de {", ".join(fistule)}."
                },
            ],
        )

    if procedure.intraMyocardiqueTrajectoryLAD:
        append_generated_text(
            document,
            chunk,
            extracted_data,
            text=[
                {
                    "text": "L'interventriculaire antérieure présente un trajet intra-myocardique."
                },
            ],
        )
