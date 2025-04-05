from typing import List

from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.Diag.Diag_dissection_parser import (
    Diag_dissection_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.Diag.Diag_segments import (
    Diag_lesions_parser,
    Diag_segments_parser,
)
from src.lib.ai_document.data_injectors.generate_coronarography.utils.Lesion_stent import (
    stent_parser,
)
from src.lib.ai_document.data_injectors.generate_coronarography.utils.find_rantrop_location import (
    rantrop_parser,
    total_occlusion_parser,
)
from src.lib.ai_document.data_injectors.generate_coronarography.utils.segment_description import (
    lesion_description,
)
from src.lib.ai_document.data_injectors.generate_coronarography.utils.segments_mapping import (
    segments_mapping,
)
from src.lib.ai_document.utils.ai_document_classes import (
    CoronarySegmentDescription,
    CoronarySegmentation,
)


def Diag_lesion_description(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):
    [
        Diag1_ostium,
        Diag1,
        Diag2_ostium,
        Diag2,
    ] = Diag_segments_parser(state)

    target = segments[0]

    if len(segments) == 2:
        if not Diag1_ostium.stenosis == "0" and not Diag1.stenosis == "0":
            return f"Sténose de {Diag1.stenosis}% au niveau de la première diagonale à partir de son ostium{stent_parser(segments)}{lesion_description(Diag1)} "
        if not Diag2_ostium.stenosis == "0" and not Diag2.stenosis == "0":
            return f"Sténose de {Diag2.stenosis}% au niveau de la deuxième diagonale à partir de son ostium{stent_parser(segments)}{lesion_description(Diag2)} "

        f""
    if len(segments) == 1:

        return f"Sténose de {target.stenosis}% au niveau de {segments_mapping(target.segment_name)}{stent_parser(segments)}{lesion_description(target)} "

    return f"Sténose de {target.stenosis}% au niveau de {",".join([segments_mapping(sgt.segment_name) + stent_parser(segments)+lesion_description(target) for sgt in segments if not sgt.stenosis == '0'])}"


def Diag_stenosis_parser(state: CoronarySegmentation):

    lesions = Diag_lesions_parser(state)
    report = (
        f"presence de {len(lesions)} lesions au niveau des diagonales. "
        if len(lesions) > 1
        else ""
    )

    for lesion in lesions:
        report += Diag_lesion_description(state, lesion)

    return report


def Diag_stenosis_generator(state: CoronarySegmentation, Diag_report: str):

    Diag_report = ""
    Diag_report += Diag_stenosis_parser(state)
    Diag_report += Diag_dissection_generator(state)

    occluded_segments = [
        sgt for sgt in Diag_segments_parser(state=state) if sgt.stenosis == "100"
    ]
    Diag_report += total_occlusion_parser(occluded_segments)

    Diag_report += rantrop_parser(state, occluded_segments)

    return Diag_report
