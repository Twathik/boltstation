from typing import List

from pprintpp import pprint
import pydash
from src.lib.generate_coronarography.generators.segment_generators.LM.LM_dissection_parser import (
    LM_dissection_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.LM.LM_segments import (
    LM_segments_children_parser,
    LM_segments_parser,
)
from src.lib.generate_coronarography.utils.coronary_tree import coronary_tree
from src.lib.generate_coronarography.utils.anomalies_calculator import (
    stenotic_anomalies_calculator,
    total_occlusion_calculator,
)
from src.lib.generate_coronarography.utils.coronarography_classes import (
    CoronarySegmentDescription,
    CoronarySegmentation,
)
from src.lib.generate_coronarography.utils.Lesion_stent import (
    stent_parser,
)
from src.lib.generate_coronarography.utils.find_rantrop_location import (
    find_rantrop_location,
    rantrop_parser,
)
from src.lib.generate_coronarography.utils.segment_description import (
    lesion_description,
)
from src.lib.generate_coronarography.utils.segments_mapping import segments_mapping


def LM_stenosis_parser(state: CoronarySegmentation):
    segments = LM_segments_parser(state)
    LM_proximal, LM_medium, LM_distal = segments

    stenos_count = stenotic_anomalies_calculator(segments=LM_segments_parser(state))
    LM_report = f"Sténose"

    match stenos_count:
        case 3:
            if (
                LM_proximal.stenosis == LM_medium.stenosis
                and LM_proximal.stenosis == LM_distal.stenosis
            ):
                return (
                    LM_report
                    + f" de {LM_proximal.stenosis}%, tubulaire sur l'ensemble du tronc commun gauche{stent_parser(segments)}{lesion_description(LM_proximal)} "
                )

            if LM_proximal.stenosis == LM_medium.stenosis:
                return (
                    LM_report
                    + f" de {LM_proximal.stenosis}% au niveau du tronc commun gauche ostio-proximo moyen{lesion_description(LM_proximal)}, et d'une lésion de {LM_distal.stenosis} dans son segment distal{stent_parser(segments)}{lesion_description(LM_distal)}. "
                )

            if LM_distal.stenosis == LM_medium.stenosis:
                return (
                    LM_report
                    + f" de {LM_proximal.stenosis}% au niveau du tronc commun gauche ostio-proximal{lesion_description(LM_proximal)}, de {LM_distal.stenosis} dans son segment medio-distal{stent_parser(segments)}{lesion_description(LM_distal)}. "
                )
            else:
                return (
                    LM_report
                    + f" de {LM_proximal.stenosis}% au niveau du tronc commun gauche ostio-proximal{lesion_description(LM_proximal)}, de {LM_medium.stenosis} dans son segment median{lesion_description(LM_medium)}, et de {LM_distal.stenosis} dans sa distalité{stent_parser(segments)}{lesion_description(LM_distal)}. "
                )
        case 2:
            if LM_proximal.stenosis == LM_medium.stenosis:
                return (
                    LM_report
                    + f" de {LM_proximal.stenosis}% au niveau tronc commun gauche ostio-proximo-moyen{stent_parser(segments)}{lesion_description(LM_proximal)}. "
                )
            if LM_medium.stenosis == LM_distal.stenosis:
                return (
                    LM_report
                    + f" de {LM_medium.stenosis}% au niveau tronc commun gauche medio-distal{stent_parser(segments)}{lesion_description(LM_medium)}. "
                )
            if LM_proximal.stenosis == LM_distal.stenosis:
                return (
                    LM_report
                    + f" de {LM_proximal.stenosis}% au niveau tronc commun gauche ostio-proximal{lesion_description(LM_proximal)} et distal{stent_parser(segments)}{lesion_description(LM_distal)}. "
                )

        case 1:
            if not LM_proximal.stenosis == "0":
                return (
                    LM_report
                    + f" de {LM_proximal.stenosis}% au niveau tronc commun gauche proximal{stent_parser(segments)}{lesion_description(LM_proximal)}. "
                )
            if not LM_medium.stenosis == "0":
                return (
                    LM_report
                    + f" de {LM_medium.stenosis}% au niveau tronc commun gauche moyen {stent_parser(segments)}{lesion_description(LM_medium)}. "
                )
            if not LM_distal.stenosis == "0":
                return (
                    LM_report
                    + f" de {LM_distal.stenosis}% au niveau tronc commun gauche distal{stent_parser(segments)}{lesion_description(LM_distal)}. "
                )
    return ""
    """ return f"{f"{LM_report} de {LM_proximal.stenosis}% au niveau tronc commun gauche proximal{stent_parser(segments)}{lesion_description(LM_proximal)}. "if not LM_proximal.stenosis == "0" else ''}{LM_report+ f" de {LM_medium.stenosis}% au niveau tronc commun gauche moyen(TCGm){stent_parser(segments)}{lesion_description(LM_medium)}. " if not LM_medium.stenosis == "0" else ""}{LM_report+ f" de {LM_distal.stenosis}% au niveau tronc commun gauche distal{stent_parser(segments)}{lesion_description(LM_distal)}. " if not LM_distal.stenosis == "0" else ""}" """


def LM_Total_occlusion_parser(state: CoronarySegmentation):
    LM_proximal, LM_medium, LM_distal = LM_segments_parser(state)

    total_occlusion_count = total_occlusion_calculator(
        segments=LM_segments_parser(state)
    )

    if total_occlusion_count > 0:
        occlusion_localisation = ""
        sgt: CoronarySegmentDescription = LM_proximal
        if LM_proximal.stenosis == "100":
            occlusion_localisation = "proximale"
            sgt = LM_proximal
        else:
            if LM_medium.stenosis == "100":
                occlusion_localisation = "médiane"
                sgt = LM_medium
            else:
                if LM_distal.stenosis == "100":
                    occlusion_localisation = "distale"
                    sgt = LM_distal
        rantrop = ""
        if not sgt.Rantrop_collaterality == None or not sgt.Rantrop == None:
            rantrop = f'Il existe une reprise{sgt.Rantrop}{sgt.Rantrop_collaterality + "e" if not sgt.Rantrop_collaterality == None else ''}'

        return f" Le tronc commun gauche est le siege d'une occlusion complète{ " aiguë" if pydash.some([sgt for sgt in LM_segments_parser(state) if sgt.acute_occlusion ]) else ''} dans sa partie{occlusion_localisation}.{rantrop}"
    return ""


def LM_lesion_children_parser(state: CoronarySegmentation) -> str:

    segments = LM_segments_children_parser(state=state)
    LAD, Bisec, Cx = segments
    LM_distal = state.LM_distal.lesion

    count = sum(not sgt.stenosis == "0" for sgt in segments)
    lesions = []
    if not LAD.stenosis == "0":
        lesions.append("l'interventriculaire anterieur proximale")
    if not Bisec.stenosis == "0":
        lesions.append("la bisectrice")
    if not Cx.stenosis == "0":
        lesions.append(
            f"{"ainsi que celui de" if count > 1 else ''}l'artère circonflexe"
        )
    if count > 0 and not LM_distal.stenosis == "0":
        if count == 3:
            return "Cette lesion prends les ostiums de l'interventriculaire antérieur proximale, de la bissectrice ainsi que l'artère circonflexe."
        if count == 2:
            return f"Cette lesion s’étend vers les ostiums de {','.join(lesions)}."
        if count == 1:
            return f"Cette lesion s’étend vers l'ostium de {lesions[0]}."
        pass
    return ""


def LM_stenosis_generator(state: CoronarySegmentation, LM_report: str):

    LM_report = ""
    LM_report += LM_stenosis_parser(state)
    LM_report += LM_Total_occlusion_parser(state)
    LM_report += LM_lesion_children_parser(state)
    LM_report += LM_dissection_generator(state)

    occluded_segments = [
        sgt for sgt in LM_segments_parser(state=state) if sgt.stenosis == "100"
    ]
    LM_report += rantrop_parser(state, occluded_segments)

    return LM_report
