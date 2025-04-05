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


def Diag_stent_description(
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
        if Diag1_ostium.stent and Diag1.stent:
            return f"Presence d'un stent au niveau de la première diagonale à partir de son ostium"
        if Diag2_ostium.stent and Diag2.stent:
            return f"Presence d'un stent au niveau de la deuxième diagonale à partir de son ostium"

    if len(segments) == 1:

        return (
            f"Presence d'un stent au niveau de {segments_mapping(target.segment_name)}"
        )

    return f"Presence d'un stent au niveau de {",".join([segments_mapping(sgt.segment_name) for sgt in segments if sgt.stent == True])}"


def Diag_stent_No_lesion_generator(state: CoronarySegmentation):
    segments = Diag_segments_parser(state)
    stents = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.stenosis == "0"
        and x.stent == True
        and x.thrombosis == False
        and x.calcification == False,
    )

    if len(stents) == 0:
        return ""

    for stent in stents:
        report += Diag_stent_description(state, stent)
        report += " sans lesion angiographiquement significative sous-jacente"

    return report
