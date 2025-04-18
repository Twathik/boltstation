from typing import List, Literal

from src.lib.ai_document.utils.ai_document_classes import (
    CoronaryLesionDescription,
    CoronarySegmentDescription,
    CoronarySegmentation,
)


def Sept_segments_parser(state: CoronarySegmentation):

    Sept1 = state.Sept1.lesion
    Sept2 = state.Sept2.lesion

    return [
        Sept1,
        Sept2,
    ]


def Sept_lesions_parser(state) -> List[CoronaryLesionDescription]:
    segments = Sept_segments_parser(state)

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
