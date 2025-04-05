from typing import Any, List
from ulid import ULID

from src.lib.ai_document.utils.ai_document_classes import (
    AngioplastyBalloon,
    AngioplastyDEB,
    AngioplastyGeneric,
    AngioplastyGuideWire,
    AngioplastyKT,
    AngioplastyMicroKT,
    AngioplastyProcedureStep,
    AngioplastyResult,
    AngioplastyRotationalAtherectomy,
    AngioplastyStent,
)
from src.lib.ai_document.utils.get_operator_function import (
    get_operator_role,
)
from src.lib.ai_document.utils.plate_general_utils import (
    append_generated_text,
    get_PCI_material_name,
    get_PCI_step_main_artery,
    get_PCI_step_main_segment,
    get_lesion_localisation,
    get_segment_title,
)
from src.lib.prismaClient import prisma_client


async def kt_angioplastie_coronaire(
    document: List[Any], chunk: Any, clinicalEventId: str, extracted_data: List[str]
) -> Any:

    clinical_event = await prisma_client.clinicalevent.find_first_or_raise(
        where={"id": clinicalEventId},
    )

    procedure = [
        AngioplastyProcedureStep.model_validate(step).root
        for step in clinical_event.jsonData["angioplastieProcedure"]
    ]

    for step in procedure:
        complication_remark = f"{step.complication} {step.remark}"

        specific_material = (
            await prisma_client.usedspecificmaterial.find_many(
                where={
                    "id": {
                        "in": (
                            step.usedSpecificMaterialId
                            if isinstance(step.usedSpecificMaterialId, list)
                            else [step.usedSpecificMaterialId]
                        )
                    }
                }
            )
            if not step.usedSpecificMaterialId == None
            and len(step.usedSpecificMaterialId) > 0
            else []
        )
        match step:
            case AngioplastyKT():

                append_generated_text(
                    document,
                    chunk,
                    extracted_data,
                    text=[
                        {
                            "text": f"{f"{"échec de " if not step.success else ""}mise en place{"avec succès " if not step.success else ""} d'une sonde porteuse de type {get_PCI_material_name(specific_material[0])}" if len(specific_material) == 1 else f"{"échec de " if not step.success else "succès apres "}plusieurs tentative de mise en place une sonde porteuse en utilisant les sondes suivantes {", ".join([get_PCI_material_name(material) for material in specific_material])}"}{" avec difficulté " if step.difficultPassthrough else ""} {f" au de niveau de {get_PCI_step_main_artery(step.segment)}. {complication_remark}"}",
                            "refactor": True,
                        }
                    ],
                )

            case AngioplastyBalloon():

                description = get_lesion_localisation(step.segments)

                append_generated_text(
                    document,
                    chunk,
                    extracted_data,
                    text=[
                        {
                            "text": f"{'échec de ' if not step.success else ''}{step.inflationType}{f'{' avec difficulté' if step.success else "suite au non franchissement de la lesion"}' if step.difficultPassthrough else ''}{' avec succès' if step.success else ''} au niveau de {description} par l’intermédiaire {f" d'un ballon {get_PCI_material_name(specific_material[0])}" if len(specific_material) == 1 else f" par l’intermédiaire de plusieurs ballons : {", ".join([get_PCI_material_name(material) for material in specific_material])}"} {f"porté{'s' if len(specific_material)>0 else ''} à {step.inflation_pressure} ATM" if not step.inflation_pressure == None and not step.inflation_pressure ==0 else ''}. {complication_remark}",
                            "refactor": True,
                        }
                    ],
                )
            case AngioplastyStent():

                description = get_lesion_localisation(step.segments)

                append_generated_text(
                    document,
                    chunk,
                    extracted_data,
                    text=[
                        {
                            "text": f"{'échec d\'une ' if not step.success else 'succès d\'une '}angioplastie{f'{' difficile' if step.success else "suite au non franchissement de la lesion"}' if step.difficultPassthrough else ''} avec mise en place de stent au niveau de {description} par l’intermédiaire {f" d'un stent {get_PCI_material_name(specific_material[0])}" if len(specific_material) == 1 else f" par l’intermédiaire de plusieurs stent : {", ".join([get_PCI_material_name(material) for material in specific_material])}"}{f"porté{'s' if len(specific_material)>0 else ''} à {step.inflation_pressure} ATM" if not step.inflation_pressure == None and not step.inflation_pressure ==0 else ''}{f"{f'nous avons eu recours a la technique {step.specificTechnic[0]} durant la procédure' if len(step.specificTechnic) == 1 else f". Nous avons eu recours à plusieurs technique durant la procédure: {", ".join(step.specificTechnic)}"}" if not step.specificTechnic == None else ""}. {complication_remark}",
                            "refactor": True,
                        }
                    ],
                )
            case AngioplastyGuideWire():

                description = get_PCI_step_main_segment(step.segment)
                append_generated_text(
                    document,
                    chunk,
                    extracted_data,
                    text=[
                        {
                            "text": f"{"succès de " if step.success else "échec de "}mise en place {f'd\' un guide d\'angioplastie' if len(specific_material) <=1 else f"de {len(specific_material)} guide d'angioplastie"} en distalité de {description}{', le franchissement de la lésion a été difficile.' if step.difficultPassthrough else ""}. {complication_remark}",
                            "refactor": True,
                        }
                    ],
                )
            case AngioplastyRotationalAtherectomy():

                description = get_lesion_localisation(step.segments)

                append_generated_text(
                    document,
                    chunk,
                    extracted_data,
                    text=[
                        {
                            "text": f"{'échec d\'une ' if not step.success else 'succès d\'une'} athéréctomie rotatoire {f'{' avec difficulté' if step.success else "suite au non franchissement de la lesion"}' if step.difficultPassthrough else ''} au niveau de {description} par l’intermédiaire {f" d'un fraise {get_PCI_material_name(specific_material[0])}" if len(specific_material) == 1 else f" de plusieurs fraises : {", ".join([get_PCI_material_name(material) for material in specific_material])}"}. {complication_remark}",
                            "refactor": True,
                        }
                    ],
                )
            case AngioplastyMicroKT():

                description = get_PCI_step_main_segment(step.segment)
                append_generated_text(
                    document,
                    chunk,
                    extracted_data,
                    text=[
                        {
                            "text": f"{"succès de " if step.success else "échec de "}mise en place {f'd\' un microcathèter' if len(specific_material) <=1 else f"de {len(specific_material)} microcathèters"} en distalité de {description}{', le franchissement de la lésion a été difficile.' if step.difficultPassthrough else ""}. {complication_remark}",
                            "refactor": True,
                        }
                    ],
                )
            case AngioplastyDEB():
                description = get_lesion_localisation(step.segments)

                append_generated_text(
                    document,
                    chunk,
                    extracted_data,
                    text=[
                        {
                            "text": f"{'échec d\'une ' if not step.success else 'succès d\'une '}angioplastie au ballon actif{' sous contrainte d\'un passage difficile' if step.difficultPassthrough else ""} au niveau de {description} par l’intermédiaire {f" d'un ballon {get_PCI_material_name(specific_material[0])}" if len(specific_material) == 1 else f" de plusieurs ballons : {", ".join([get_PCI_material_name(material) for material in specific_material])}"}{f"porté{'s' if len(specific_material)>0 else ''} à {step.inflation_pressure} ATM" if not step.inflation_pressure == None and not step.inflation_pressure ==0 else ''}. {complication_remark}",
                            "refactor": True,
                        }
                    ],
                )
            case AngioplastyResult():

                description = get_lesion_localisation(step.segments)

                append_generated_text(
                    document,
                    chunk,
                    extracted_data,
                    text=[
                        {
                            "text": f"{'échec d\'' if step.result == 'failure' else f'succès {'intermédiaire' if step.result == 'intermediary' else ''} d\''}angioplastie au niveau de {description}, {f"l'artère est restée occluse, siège d'un flux {step.TIMI_Flow} " if step.residualStenosis == '100' else f"il n'existe pas de sténose résiduelle avec un flux {step.TIMI_Flow}" if step.residualStenosis == '0' else f"il existe une sténose résiduelle évaluée à {step.residualStenosis}"}.{step.failureOrigin}. {complication_remark}",
                            "refactor": True,
                        }
                    ],
                )

            case AngioplastyGeneric():

                description = get_lesion_localisation(step.segments)
                append_generated_text(
                    document,
                    chunk,
                    extracted_data,
                    text=[
                        {
                            "text": f"{"succès de " if step.success else "échec de "}{step.description} {f'd\' un' if len(specific_material) <=1 else f"de {len(specific_material)}"} au niveau de {description}. {complication_remark}",
                            "refactor": True,
                        }
                    ],
                )
            case _:
                print("Unknown step type", step)
