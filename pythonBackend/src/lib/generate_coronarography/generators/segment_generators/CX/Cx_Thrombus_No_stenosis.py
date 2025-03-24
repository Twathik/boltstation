from typing import List

from src.lib.generate_coronarography.generators.segment_generators.CX.Cx_segments import (
    Cx_segments_parser,
)
from src.lib.generate_coronarography.utils.coronarography_classes import (
    CoronarySegmentDescription,
    CoronarySegmentation,
)
from src.lib.generate_coronarography.utils.segment_description import (
    generic_condition_parser,
)
from src.lib.generate_coronarography.utils.segments_mapping import segments_mapping


def Cx_thrombus_description(
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
        if Cx1_ostium.thrombosis and Cx1_proximal.thrombosis and Cx1_distal.thrombosis:

            return f"Presence d'un thrombus au niveau de l'artère circonflexe ostio-proximale"

    if len(segments) == 2:
        if Cx1_proximal.thrombosis and Cx1_ostium.thrombosis:
            return f"Presence d'un thrombus au niveau de l'artère circonflexe ostio-proximale"
        if Cx1_proximal.thrombosis and Cx1_distal.thrombosis:
            return f"Presence d'un thrombus au niveau de l'artère circonflexe proximale"
        if Cx2_proximal.thrombosis and Cx2_distal.thrombosis:
            return f"Presence d'un thrombus au niveau de l'artère circonflexe moyenne"
        if Cx3_proximal.thrombosis and Cx3_distal.thrombosis:
            return f"Presence d'un thrombus au niveau de l'artère circonflexe distale"
    if len(segments) == 1:

        return f"Presence d'un thrombus au niveau de {segments_mapping(target.segment_name)}"

    return f"Presence d'un thrombus allant de {segments_mapping(segments[0].segment_name)} à {segments_mapping(segments[-1].segment_name)}"


def Cx_thrombus_children_parser(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):

    bifurcations: List[str] = []

    for sgt in segments:
        if (
            sgt.segment_name == "Cx1_distal"
            and not state.Marg1_ostium.lesion.thrombosis == True
        ):
            bifurcations.append(segments_mapping("Marg1_ostium"))
        if (
            sgt.segment_name == "Cx2_proximal"
            and not state.Marg2_ostium.lesion.thrombosis == True
        ):
            bifurcations.append(segments_mapping("Marg2_ostium"))
        if (
            sgt.segment_name == "Cx2_distal"
            and not state.IVPL_ostium.lesion.thrombosis == True
        ):
            bifurcations.append(segments_mapping("IVPL_ostium"))

    if len(bifurcations) == 0:
        return ""
    if len(bifurcations) == 1:
        return f", prenant l{bifurcations[0]}"
    else:
        return f", prenant {', '.join(bifurcations)}"


def Cx_Thrombus_No_stenosis_generator(state: CoronarySegmentation):
    segments = Cx_segments_parser(state)
    lesions = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.stenosis == "0" and x.thrombosis == True,
    )
    print(lesions)
    report = (
        f"presence de {len(lesions)} thrombus au niveau de l'artère circonflexe. "
        if len(lesions) > 1
        else ""
    )

    for lesion in lesions:
        report += Cx_thrombus_description(state, lesion)
        report += Cx_thrombus_children_parser(state, lesion)
        stent = [sgt for sgt in lesion if sgt.stent == True]
        if len(stent) > 0:
            report += " au niveau du site d'implantation d'un stent"
        report += " sans lesion angiographiquement significative sous-jacente"

    return report
