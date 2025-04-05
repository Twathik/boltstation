from typing import List

from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.RVG.RVG_segments import (
    RVG_segments_parser,
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


def RVG_dissection_description(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):
    [
        RVG_ostium,
        RVG_proximal,
        RVG_distal,
    ] = RVG_segments_parser(state)

    target = segments[0]

    if len(segments) == 3:
        if RVG_ostium.dissection and RVG_proximal.dissection and RVG_distal.dissection:

            return f"Dissection diffuse {inject_dissectionType(target)} au niveau de la rétro ventriculaire gauche"

    if len(segments) == 2:
        if RVG_proximal.dissection and RVG_ostium.dissection:
            return f"Dissection{inject_dissectionType(target)} au niveau de la rétro ventriculaire gauche ostio-proximale"
        if RVG_proximal.dissection and RVG_distal.dissection:
            return f"Dissection{inject_dissectionType(target)} au niveau de la rétro ventriculaire gauche"

    if len(segments) == 1:

        return f"Dissection{inject_dissectionType(target)} au niveau de {segments_mapping(target.segment_name)}"

    return f"Dissection{inject_dissectionType(target)} allant de {segments_mapping(segments[0].segment_name)} à {segments_mapping(segments[-1].segment_name)}"


def RVG_dissection_generator(state: CoronarySegmentation):
    segments = RVG_segments_parser(state)

    dissections = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.dissection == True,
    )

    report = (
        f"presence de {len(dissections)} lesions au niveau de la rétro ventriculaire gauche. "
        if len(dissections) > 1
        else ""
    )

    for dissection in dissections:
        report += RVG_dissection_description(state, dissection)

    return report
