from typing import List

from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.Diag.Diag_segments import (
    Diag_segments_parser,
)
from src.lib.ai_document.data_injectors.generate_coronarography.utils.segment_description import (
    generic_condition_parser,
    inject_dissectionType,
)
from src.lib.ai_document.data_injectors.generate_coronarography.utils.segments_mapping import (
    segments_mapping,
)
from src.lib.ai_document.utils.ai_document_classes import (
    CoronarySegmentDescription,
    CoronarySegmentation,
)


def Diag_dissection_description(
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
        if Diag1_ostium.dissection and Diag1.dissection:
            return f"Dissection{inject_dissectionType(target)} au niveau de la première diagonale à partir de son ostium"
        if Diag2_ostium.dissection and Diag2.dissection:
            return f"Dissection{inject_dissectionType(target)} au niveau de la deuxième diagonale à partir de son ostium"

    if len(segments) == 1:

        return f"Dissection{inject_dissectionType(target)} au niveau de {segments_mapping(target.segment_name)}"

    return f"Dissection{inject_dissectionType(target)} au niveau de {",".join([segments_mapping(sgt.segment_name) for sgt in segments if sgt.dissection == True])}"


def Diag_dissection_generator(state: CoronarySegmentation):
    segments = Diag_segments_parser(state)
    dissections = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.dissection == True,
    )
    if len(dissections) == 0:
        return ""

    for dissection in dissections:
        report += Diag_dissection_description(state, dissection)

    return report
