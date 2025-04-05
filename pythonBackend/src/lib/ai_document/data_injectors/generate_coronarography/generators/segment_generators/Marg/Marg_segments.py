from typing import List, Literal

from src.lib.ai_document.data_injectors.generate_coronarography.utils.segments_mapping import (
    segments_mapping,
)
from src.lib.ai_document.utils.ai_document_classes import (
    CoronaryLesionDescription,
    CoronarySegmentDescription,
    CoronarySegmentation,
)


def Marg_segments_parser(state: CoronarySegmentation):

    Marg1_ostium = state.Marg1_ostium.lesion
    Marg1_proximal = state.Marg1_proximal.lesion
    Marg1_distal = state.Marg1_distal.lesion
    Marg2_ostium = state.Marg2_ostium.lesion
    Marg2_proximal = state.Marg2_proximal.lesion
    Marg2_distal = state.Marg2_distal.lesion

    return [
        Marg1_ostium,
        Marg1_proximal,
        Marg1_distal,
        Marg2_ostium,
        Marg2_proximal,
        Marg2_distal,
    ]


def Marg_lesions_parser(state) -> List[CoronaryLesionDescription]:
    segments = Marg_segments_parser(state)

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
