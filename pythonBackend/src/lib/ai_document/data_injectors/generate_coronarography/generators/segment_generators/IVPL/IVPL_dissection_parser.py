from typing import List

from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.IVPL.IVPL_segments import (
    IVPL_segments_parser,
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


def IVPL_dissection_description(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):
    [
        IVPL_ostium,
        IVPL_proximal,
        IVPL_distal,
    ] = IVPL_segments_parser(state)

    target = segments[0]

    if len(segments) == 3:
        if (
            IVPL_ostium.dissection
            and IVPL_proximal.dissection
            and IVPL_distal.dissection
        ):

            return f"Dissection diffuse {inject_dissectionType(target)} au niveau de l'interventriculaire postérieure gauche"

    if len(segments) == 2:
        if IVPL_proximal.dissection and IVPL_ostium.dissection:
            return f"Dissection{inject_dissectionType(target)} au niveau de l'interventriculaire postérieure gauche ostio-proximale"
        if IVPL_proximal.dissection and IVPL_distal.dissection:
            return f"Dissection{inject_dissectionType(target)} au niveau de l'interventriculaire postérieure gauche"

    if len(segments) == 1:

        return f"Dissection{inject_dissectionType(target)} au niveau de {segments_mapping(target.segment_name)}"

    return f"Dissection{inject_dissectionType(target)} allant de {segments_mapping(segments[0].segment_name)} à {segments_mapping(segments[-1].segment_name)}"


def IVPL_dissection_generator(state: CoronarySegmentation):
    segments = IVPL_segments_parser(state)

    dissections = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.dissection == True,
    )

    report = (
        f"presence de {len(dissections)} lesions au niveau de l'interventriculaire postérieure gauche. "
        if len(dissections) > 1
        else ""
    )

    for dissection in dissections:
        report += IVPL_dissection_description(state, dissection)

    return report
