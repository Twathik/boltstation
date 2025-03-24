from typing import List
from src.lib.generate_coronarography.generators.segment_generators.LAD.LAD_segments import (
    LAD_children_parser,
    LAD_segments_parser,
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


def LAD_dissection_description(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):
    [
        LAD1_ostium,
        LAD1_proximal,
        LAD1_distal,
        LAD2_proximal,
        LAD2_distal,
        LAD3_proximal,
        LAD3_distal,
    ] = LAD_segments_parser(state)

    target = segments[0]

    if len(segments) == 3:
        if (
            LAD1_ostium.dissection
            and LAD1_proximal.dissection
            and LAD1_distal.dissection
        ):

            return f"Dissection{inject_dissectionType(target)} au niveau de l'interventriculaire antérieure ostio-proximale"

    if len(segments) == 2:
        if LAD1_proximal.dissection and LAD1_ostium.dissection:
            return f"Dissection{inject_dissectionType(target)} au niveau de l'interventriculaire antérieure ostio-proximale"
        if LAD1_proximal.dissection and LAD1_distal.dissection:
            return f"Dissection{inject_dissectionType(target)} au niveau de l'interventriculaire antérieure proximale"
        if LAD2_proximal.dissection and LAD2_distal.dissection:
            return f"Dissection{inject_dissectionType(target)} au niveau de l'interventriculaire antérieure moyenne"
        if LAD3_proximal.dissection and LAD3_distal.dissection:
            return f"Dissection{inject_dissectionType(target)} au niveau de l'interventriculaire antérieure distale"
    if len(segments) == 1:

        return f"Dissection{inject_dissectionType(target)} au niveau de {segments_mapping(target.segment_name)}"

    return f"Dissection{inject_dissectionType(target)} allant de {segments_mapping(segments[0].segment_name)} à {segments_mapping(segments[-1].segment_name)}"


def LAD_dissection_children_parser(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):

    bifurcations: List[str] = []

    for sgt in segments:
        if sgt.segment_name == "LAD1_distal" and state.Sept1.lesion.dissection:
            bifurcations.append(segments_mapping("Sept1"))
        if sgt.segment_name == "LAD2_proximal" and state.Diag1_ostium.lesion.dissection:
            bifurcations.append(segments_mapping("Diag1_ostium"))
        if sgt.segment_name == "LAD2_distal" and state.Diag2_ostium.lesion.dissection:
            bifurcations.append(segments_mapping("Diag2_ostium"))
        if sgt.segment_name == "LAD2_distal" and state.Sept2.lesion.dissection:
            bifurcations.append(segments_mapping("Sept2"))
    if len(bifurcations) == 0:
        return ""
    if len(bifurcations) == 1:
        return f", prenant l{bifurcations[0]}"
    else:
        return f", prenant {', '.join(bifurcations)}"


def LAD_dissection_generator(state: CoronarySegmentation):
    segments = LAD_segments_parser(state)

    dissections = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.dissection == True,
    )

    report = (
        f"presence de {len(dissections)} lesions au niveau de l'interventriculaire anterieur. "
        if len(dissections) > 1
        else ""
    )

    for dissection in dissections:
        report += LAD_dissection_description(state, dissection)
        report += LAD_dissection_children_parser(state, dissection)

    return report
