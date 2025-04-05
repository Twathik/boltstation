from typing import List


from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.Sept.Sept_segments import (
    Sept_segments_parser,
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


def Sept_dissection_description(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):

    return f"Dissection au niveau de {",".join([segments_mapping(sgt.segment_name) + f" {inject_dissectionType(sgt)}" for sgt in segments if sgt.dissection == True])}"


def Sept_dissection_generator(state: CoronarySegmentation):
    segments = Sept_segments_parser(state)
    dissections = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.dissection == True,
    )
    if len(dissections) == 0:
        return ""

    for dissection in dissections:
        report += Sept_dissection_description(state, dissection)

    return report
