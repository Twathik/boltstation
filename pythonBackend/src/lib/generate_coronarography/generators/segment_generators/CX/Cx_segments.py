from typing import List, Literal
from src.lib.generate_coronarography.utils.coronarography_classes import (
    CoronarySegmentDescription,
    CoronarySegmentation,
)
from src.lib.generate_coronarography.utils.segments_mapping import segments_mapping


def Cx_segments_parser(state: CoronarySegmentation):

    Cx1_ostium = state.CX1_ostium.lesion
    Cx1_proximal = state.CX1_proximal.lesion
    Cx1_distal = state.CX1_distal.lesion
    Cx2_proximal = state.CX2_proximal.lesion
    Cx2_distal = state.CX2_distal.lesion
    Cx3_proximal = state.CX3_proximal.lesion
    Cx3_distal = state.CX3_distal.lesion

    return [
        Cx1_ostium,
        Cx1_proximal,
        Cx1_distal,
        Cx2_proximal,
        Cx2_distal,
        Cx3_proximal,
        Cx3_distal,
    ]


def Cx_segments_children_parser(state: CoronarySegmentation):

    Marg1_ostium = state.Marg1_ostium.lesion
    Marg2_ostium = state.Marg2_ostium.lesion
    IVPL_ostium = state.IVPL_ostium.lesion

    return [
        Marg1_ostium,
        Marg2_ostium,
        IVPL_ostium,
    ]


def Cx_lesions_parser(state):
    segments = Cx_segments_parser(state)

    sequence: List[List[CoronarySegmentDescription]] = []
    index = -1
    current_stenosis_level: Literal[
        "0", "<30", "30-50", "50", "50-70", "70-90", "90-99", "100"
    ] = "0"

    for sgt in segments:
        if not sgt.stenosis == "0" and not sgt.stenosis == "100":
            if not sgt.stenosis == current_stenosis_level:
                index += 1
                current_stenosis_level = sgt.stenosis
                sequence.append([])
            sequence[index].append(sgt)
        else:
            if len(sequence) > 0:
                index += 1
                current_stenosis_level = "0"
                sequence.append([])

    return [arr for arr in sequence if arr]


def Cx_children_parser(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):

    bifurcations: List[str] = []

    for sgt in segments:
        if (
            sgt.segment_name == "Cx1_distal"
            and not state.Marg1_ostium.lesion.stenosis == "0"
        ):
            bifurcations.append(segments_mapping("Marg1_ostium"))
        if (
            sgt.segment_name == "Cx2_proximal"
            and not state.Marg2_ostium.lesion.stenosis == "0"
        ):
            bifurcations.append(segments_mapping("Marg2_ostium"))
        if (
            sgt.segment_name == "Cx2_distal"
            and not state.IVPL_ostium.lesion.stenosis == "0"
        ):
            bifurcations.append(segments_mapping("IVPL_ostium"))
    if len(bifurcations) == 0:
        return ""
    if len(bifurcations) == 1:
        return f", prenant l{bifurcations[0]}"
    else:
        return f", prenant {', '.join(bifurcations)}"
