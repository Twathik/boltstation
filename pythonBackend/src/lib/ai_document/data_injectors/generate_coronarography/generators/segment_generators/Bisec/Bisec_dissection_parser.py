from typing import List

from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.Bisec.Bisec_segments import (
    Bisec_segments_parser,
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


def Bisec_dissection_description(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):
    [
        Bisec_ostium,
        Bisec_proximal,
        Bisec_distal,
    ] = Bisec_segments_parser(state)

    target = segments[0]

    if len(segments) == 3:
        return "Dissection au niveau de la bissectrice à partir de son ostium"

    if len(segments) == 2:
        if Bisec_ostium.dissection and Bisec_proximal.dissection:
            return f"Dissection{inject_dissectionType(target)} au niveau de la bissectrice proximale à partir de son ostium"
        if Bisec_proximal.dissection and Bisec_distal.dissection:
            return (
                f"Dissection{inject_dissectionType(target)} au niveau de la bissectrice"
            )

    if len(segments) == 1:

        return f"Dissection{inject_dissectionType(target)} au niveau de {segments_mapping(target.segment_name)}"

    return f"Dissection{inject_dissectionType(target)} au niveau de {",".join([segments_mapping(sgt.segment_name) for sgt in segments if sgt.dissection == True])}"


def Bisec_dissection_generator(state: CoronarySegmentation):
    segments = Bisec_segments_parser(state)
    dissections = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.dissection == True,
    )
    if len(dissections) == 0:
        return ""
    report = ""
    for dissection in dissections:
        report += Bisec_dissection_description(state, dissection)

    return report
