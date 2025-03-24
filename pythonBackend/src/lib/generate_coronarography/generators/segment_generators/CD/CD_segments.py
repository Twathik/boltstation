from typing import List, Literal
from src.lib.generate_coronarography.utils.coronarography_classes import (
    CoronarySegmentDescription,
    CoronarySegmentation,
)
from src.lib.generate_coronarography.utils.segments_mapping import segments_mapping


def CD_segments_parser(state: CoronarySegmentation):

    CD1_ostium = state.CD1_ostium.lesion
    CD1_proximal = state.CD1_proximal.lesion
    CD1_distal = state.CD1_distal.lesion
    CD2_proximal = state.CD2_proximal.lesion
    CD2_distal = state.CD2_distal.lesion

    return [
        CD1_ostium,
        CD1_proximal,
        CD1_distal,
        CD2_proximal,
        CD2_distal,
    ]


def CD_segments_children_parser(state: CoronarySegmentation):

    MargR1 = state.MargR1.lesion
    MargR2 = state.MargR2.lesion
    IVPR_ostium = state.IVPR_ostium.lesion
    RVG_ostium = state.RVG_ostium.lesion

    return [MargR1, MargR2, IVPR_ostium, RVG_ostium]


def CD_lesions_parser(state):
    segments = CD_segments_parser(state)

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


def CD_children_parser(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):

    bifurcations: List[str] = []

    for sgt in segments:
        if (
            sgt.segment_name == "CD1_proximal"
            and not state.MargR1.lesion.stenosis == "0"
        ):
            bifurcations.append(segments_mapping("MargR1"))
        if sgt.segment_name == "CD1_distal" and not state.MargR2.lesion.stenosis == "0":
            bifurcations.append(segments_mapping("MargR2"))
        if (
            sgt.segment_name == "CD2_distal"
            and not state.IVPR_ostium.lesion.stenosis == "0"
        ):
            bifurcations.append(segments_mapping("IVPR_ostium"))
        if (
            sgt.segment_name == "CD2_distal"
            and not state.RVG_ostium.lesion.stenosis == "0"
        ):
            bifurcations.append(segments_mapping("RVG_ostium"))

    if len(bifurcations) == 0:
        return ""
    if len(bifurcations) == 1:
        return f", prenant l{bifurcations[0]}"
    else:
        return f", prenant {', '.join(bifurcations)}"
