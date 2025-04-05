from typing import List

from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.CX.Cx_segments import (
    Cx_segments_parser,
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


def Cx_dissection_description(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):
    [
        Cx1_ostium,
        Cx1_proximal,
        Cx1_distal,
        Cx2_proximal,
        Cx2_distal,
        Cx3_proximal,
        Cx3_distal,
    ] = Cx_segments_parser(state)

    target = segments[0]

    if len(segments) == 3:
        if Cx1_ostium.dissection and Cx1_proximal.dissection and Cx1_distal.dissection:

            return f"Dissection{inject_dissectionType(target)} au niveau de l'artère circonflexe ostio-proximale"

    if len(segments) == 2:
        if Cx1_proximal.dissection and Cx1_ostium.dissection:
            return f"Dissection{inject_dissectionType(target)} au niveau de l'artère circonflexe ostio-proximale"
        if Cx1_proximal.dissection and Cx1_distal.dissection:
            return f"Dissection{inject_dissectionType(target)} au niveau de l'artère circonflexe proximale"
        if Cx2_proximal.dissection and Cx2_distal.dissection:
            return f"Dissection{inject_dissectionType(target)} au niveau de l'artère circonflexe moyenne"
        if Cx3_proximal.dissection and Cx3_distal.dissection:
            return f"Dissection{inject_dissectionType(target)} au niveau de l'artère circonflexe distale"
    if len(segments) == 1:

        return f"Dissection{inject_dissectionType(target)} au niveau de {segments_mapping(target.segment_name)}"

    return f"Dissection{inject_dissectionType(target)} allant de {segments_mapping(segments[0].segment_name)} à {segments_mapping(segments[-1].segment_name)}"


def Cx_dissection_children_parser(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):

    bifurcations: List[str] = []

    for sgt in segments:
        if (
            sgt.segment_name == "Cx1_distal"
            and not state.Marg1_ostium.lesion.dissection == True
        ):
            bifurcations.append(segments_mapping("Marg1_ostium"))
        if (
            sgt.segment_name == "Cx2_proximal"
            and not state.Marg2_ostium.lesion.dissection == True
        ):
            bifurcations.append(segments_mapping("Marg2_ostium"))
        if (
            sgt.segment_name == "Cx2_distal"
            and not state.IVPL_ostium.lesion.dissection == True
        ):
            bifurcations.append(segments_mapping("IVPL_ostium"))
    if len(bifurcations) == 0:
        return ""
    if len(bifurcations) == 1:
        return f", prenant l{bifurcations[0]}"
    else:
        return f", prenant {', '.join(bifurcations)}"


def Cx_dissection_generator(state: CoronarySegmentation):
    segments = Cx_segments_parser(state)

    dissections = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.dissection == True,
    )

    report = (
        f"presence de {len(dissections)} lesions au niveau de l'artère circonflexe. "
        if len(dissections) > 1
        else ""
    )

    for dissection in dissections:
        report += Cx_dissection_description(state, dissection)
        report += Cx_dissection_children_parser(state, dissection)

    return report
