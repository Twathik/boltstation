from typing import List

from src.lib.generate_coronarography.generators.segment_generators.IVPR.IVPR_segments import (
    IVPR_segments_parser,
)
from src.lib.generate_coronarography.utils.coronarography_classes import (
    CoronarySegmentDescription,
    CoronarySegmentation,
)
from src.lib.generate_coronarography.utils.segment_description import (
    generic_condition_parser,
    inject_dissectionType,
)
from src.lib.generate_coronarography.utils.segments_mapping import segments_mapping


def IVPR_dissection_description(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):
    [
        IVPR_ostium,
        IVPR_proximal,
        IVPR_distal,
    ] = IVPR_segments_parser(state)

    target = segments[0]

    if len(segments) == 3:
        if (
            IVPR_ostium.dissection
            and IVPR_proximal.dissection
            and IVPR_distal.dissection
        ):

            return f"Dissection diffuse {inject_dissectionType(target)} au niveau de l'interventriculaire postérieure droite"

    if len(segments) == 2:
        if IVPR_proximal.dissection and IVPR_ostium.dissection:
            return f"Dissection{inject_dissectionType(target)} au niveau de l'interventriculaire postérieure droite ostio-proximale"
        if IVPR_proximal.dissection and IVPR_distal.dissection:
            return f"Dissection{inject_dissectionType(target)} au niveau de l'interventriculaire postérieure droite"

    if len(segments) == 1:

        return f"Dissection{inject_dissectionType(target)} au niveau de {segments_mapping(target.segment_name)}"

    return f"Dissection{inject_dissectionType(target)} allant de {segments_mapping(segments[0].segment_name)} à {segments_mapping(segments[-1].segment_name)}"


def IVPR_dissection_generator(state: CoronarySegmentation):
    segments = IVPR_segments_parser(state)

    dissections = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.dissection == True,
    )

    report = (
        f"presence de {len(dissections)} lesions au niveau de l'interventriculaire postérieure droite. "
        if len(dissections) > 1
        else ""
    )

    for dissection in dissections:
        report += IVPR_dissection_description(state, dissection)

    return report
