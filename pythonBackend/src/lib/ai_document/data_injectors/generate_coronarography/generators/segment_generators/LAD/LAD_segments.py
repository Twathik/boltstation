from typing import List, Literal

from src.lib.ai_document.data_injectors.generate_coronarography.utils.segments_mapping import (
    segments_mapping,
)
from src.lib.ai_document.utils.ai_document_classes import (
    CoronaryLesionDescription,
    CoronarySegmentDescription,
    CoronarySegmentation,
)


def LAD_segments_parser(state: CoronarySegmentation) -> List[CoronaryLesionDescription]:

    LAD1_ostium = state.LAD1_ostium.lesion
    LAD1_proximal = state.LAD1_proximal.lesion
    LAD1_distal = state.LAD1_distal.lesion
    LAD2_proximal = state.LAD2_proximal.lesion
    LAD2_distal = state.LAD2_distal.lesion
    LAD3_proximal = state.LAD3_proximal.lesion
    LAD3_distal = state.LAD3_distal.lesion

    return [
        LAD1_ostium,
        LAD1_proximal,
        LAD1_distal,
        LAD2_proximal,
        LAD2_distal,
        LAD3_proximal,
        LAD3_distal,
    ]


def LAD_segments_children_parser(state: CoronarySegmentation):

    Sept1 = state.Sept1.lesion
    Diag1_ostium = state.Diag1_ostium.lesion
    Diag1 = state.Diag1.lesion
    Diag2_ostium = state.Diag2_ostium.lesion
    Diag2 = state.Diag2.lesion
    Sept2 = state.Sept2.lesion

    return [
        Sept1,
        Diag1_ostium,
        Diag1,
        Diag2_ostium,
        Diag2,
        Sept2,
    ]


def LAD_lesions_parser(state) -> List[CoronaryLesionDescription]:
    segments = LAD_segments_parser(state)

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


def LAD_children_parser(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
) -> List[CoronaryLesionDescription]:

    bifurcations: List[str] = []

    for sgt in segments:
        if sgt.segment_name == "LAD1_distal" and not state.Sept1.lesion.stenosis == "0":
            bifurcations.append(segments_mapping("Sept1"))
        if (
            sgt.segment_name == "LAD2_proximal"
            and not state.Diag1_ostium.lesion.stenosis == "0"
        ):
            bifurcations.append(segments_mapping("Diag1_ostium"))
        if (
            sgt.segment_name == "LAD2_distal"
            and not state.Diag2_ostium.lesion.stenosis == "0"
        ):
            bifurcations.append(segments_mapping("Diag2_ostium"))
        if sgt.segment_name == "LAD2_distal" and not state.Sept2.lesion.stenosis == "0":
            bifurcations.append(segments_mapping("Sept2"))
    if len(bifurcations) == 0:
        return ""
    if len(bifurcations) == 1:
        return f", prenant l{bifurcations[0]}"
    else:
        return f", prenant {', '.join(bifurcations)}"
