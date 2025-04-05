from typing import List, Literal

from src.lib.ai_document.utils.ai_document_classes import (
    CoronaryLesionDescription,
    CoronarySegmentDescription,
    CoronarySegmentation,
)


def IVPR_segments_parser(state: CoronarySegmentation):

    IVPR_ostium = state.IVPR_ostium.lesion
    IVPR_proximal = state.IVPR_proximal.lesion
    IVPR_distal = state.IVPR_distal.lesion

    return [
        IVPR_ostium,
        IVPR_proximal,
        IVPR_distal,
    ]


def IVPR_lesions_parser(state) -> List[CoronaryLesionDescription]:
    segments = IVPR_segments_parser(state)

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
