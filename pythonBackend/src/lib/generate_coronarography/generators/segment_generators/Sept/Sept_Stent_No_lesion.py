from typing import List


from src.lib.generate_coronarography.generators.segment_generators.Sept.Sept_segments import (
    Sept_segments_parser,
)
from src.lib.generate_coronarography.utils.coronarography_classes import (
    CoronarySegmentDescription,
    CoronarySegmentation,
)
from src.lib.generate_coronarography.utils.segment_description import (
    generic_condition_parser,
)
from src.lib.generate_coronarography.utils.segments_mapping import segments_mapping


def Sept_stent_description(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):

    return f"Presence d'un stent au niveau de {",".join([segments_mapping(sgt.segment_name) for sgt in segments if sgt.stent == True])}"


def Sept_stent_No_lesion_generator(state: CoronarySegmentation):
    segments = Sept_segments_parser(state)
    stents = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.stenosis == "0"
        and x.stent == True
        and x.thrombosis == False
        and x.calcification == False,
    )

    if len(stents) == 0:
        return ""

    for stent in stents:
        report += Sept_stent_description(stent)
        report += " sans lesion angiographiquement significative sous-jacente"

    return report
