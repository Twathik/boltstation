from typing import List

from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.Diag.Diag_segments import (
    Diag_segments_parser,
)
from src.lib.ai_document.data_injectors.generate_coronarography.utils.segment_description import (
    generic_condition_parser,
)
from src.lib.ai_document.data_injectors.generate_coronarography.utils.segments_mapping import (
    segments_mapping,
)
from src.lib.ai_document.utils.ai_document_classes import (
    CoronarySegmentDescription,
    CoronarySegmentation,
)


def Diag_calcification_description(
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
        if Diag1_ostium.calcification and Diag1.calcification:

            return f"Presence d'une calcification au niveau de la premiere diagonale à partir de son ostium"
        if Diag2_ostium.calcification and Diag2.calcification:

            return f"Presence d'une calcification au niveau de la deuxième diagonale à partir de son ostium"

    if len(segments) == 1:

        return f"Presence d'une calcification au niveau de {segments_mapping(target.segment_name)}"

    return f"Presence d'une calcification au niveau de {",".join([segments_mapping(sgt.segment_name) for sgt in segments if sgt.calcification == True])}"


def Diag_calcification_No_stenosis_generator(state: CoronarySegmentation):
    segments = Diag_segments_parser(state)
    lesions = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.stenosis == "0" and x.calcification == True,
    )
    if len(lesions) == 0:
        return ""

    for lesion in lesions:
        report += Diag_calcification_description(state, lesion)
        stent = [sgt for sgt in lesion if sgt.stent == True]
        if len(stent) > 0:
            report += " au niveau du site d'implantation d'un stent"
        report += " sans lesion angiographiquement significative sous-jacente"

    return report
