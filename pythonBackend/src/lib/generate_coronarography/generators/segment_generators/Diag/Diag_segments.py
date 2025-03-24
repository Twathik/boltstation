from typing import List, Literal
from src.lib.generate_coronarography.utils.coronarography_classes import (
    CoronarySegmentDescription,
    CoronarySegmentation,
)


def Diag_segments_parser(state: CoronarySegmentation):

    Diag1_ostium = state.Diag1_ostium.lesion
    Diag1 = state.Diag1.lesion
    Diag2_ostium = state.Diag2_ostium.lesion
    Diag2 = state.Diag2.lesion

    return [
        Diag1_ostium,
        Diag1,
        Diag2_ostium,
        Diag2,
    ]


def Diag_lesions_parser(state):
    segments = Diag_segments_parser(state)

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
