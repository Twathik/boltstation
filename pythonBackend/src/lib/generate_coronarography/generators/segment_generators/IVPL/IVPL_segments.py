from typing import List, Literal
from src.lib.generate_coronarography.utils.coronarography_classes import (
    CoronarySegmentDescription,
    CoronarySegmentation,
)
from src.lib.generate_coronarography.utils.segments_mapping import segments_mapping


def IVPL_segments_parser(state: CoronarySegmentation):

    IVPL_ostium = state.IVPL_ostium.lesion
    IVPL_proximal = state.IVPL_proximal.lesion
    IVPL_distal = state.IVPL_distal.lesion

    return [
        IVPL_ostium,
        IVPL_proximal,
        IVPL_distal,
    ]


def IVPL_lesions_parser(state):
    segments = IVPL_segments_parser(state)

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
