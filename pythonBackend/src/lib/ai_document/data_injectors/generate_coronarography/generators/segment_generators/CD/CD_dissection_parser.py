from typing import List

from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.CD.CD_segments import (
    CD_segments_parser,
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


def CD_dissection_description(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):
    [
        CD1_ostium,
        CD1_proximal,
        CD1_distal,
        CD2_proximal,
        CD2_distal,
    ] = CD_segments_parser(state)

    target = segments[0]

    if len(segments) == 3:
        if CD1_ostium.dissection and CD1_proximal.dissection and CD1_distal.dissection:

            return f"Dissection{inject_dissectionType(target)} au niveau de la coronaire droite ostio-proximale"

    if len(segments) == 2:
        if CD1_proximal.dissection and CD1_ostium.dissection:
            return f"Dissection{inject_dissectionType(target)} au niveau de la coronaire droite ostio-proximale"
        if CD1_proximal.dissection and CD1_distal.dissection:
            return f"Dissection{inject_dissectionType(target)} au niveau de la coronaire droite proximale"
        if CD2_proximal.dissection and CD2_distal.dissection:
            return f"Dissection{inject_dissectionType(target)} au niveau de la coronaire droite moyenne"

    if len(segments) == 1:

        return f"Dissection{inject_dissectionType(target)} au niveau de {segments_mapping(target.segment_name)}"

    return f"Dissection{inject_dissectionType(target)} allant de {segments_mapping(segments[0].segment_name)} à {segments_mapping(segments[-1].segment_name)}"


def CD_dissection_children_parser(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):

    bifurcations: List[str] = []

    for sgt in segments:
        if (
            sgt.segment_name == "CD1_proximal"
            and not state.MargR1.lesion.dissection == "0"
        ):
            bifurcations.append(segments_mapping("MargR1"))
        if (
            sgt.segment_name == "CD1_distal"
            and not state.MargR2.lesion.dissection == "0"
        ):
            bifurcations.append(segments_mapping("MargR2"))
        if (
            sgt.segment_name == "CD2_distal"
            and not state.IVPR_ostium.lesion.dissection == "0"
        ):
            bifurcations.append(segments_mapping("IVPR_ostium"))
        if (
            sgt.segment_name == "CD2_distal"
            and not state.RVG_ostium.lesion.dissection == "0"
        ):
            bifurcations.append(segments_mapping("RVG_ostium"))

    if len(bifurcations) == 0:
        return ""
    if len(bifurcations) == 1:
        return f", prenant l{bifurcations[0]}"
    else:
        return f", prenant {', '.join(bifurcations)}"


def CD_dissection_generator(state: CoronarySegmentation):
    segments = CD_segments_parser(state)

    dissections = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.dissection == True,
    )

    report = (
        f"presence de {len(dissections)} lesions au niveau de la coronaire droite. "
        if len(dissections) > 1
        else ""
    )

    for dissection in dissections:
        report += CD_dissection_description(state, dissection)
        report += CD_dissection_children_parser(state, dissection)

    return report
