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


def Sept_thrombus_description(segments: List[CoronarySegmentDescription]):

    return f"Presence d'un thrombus au niveau de {",".join([segments_mapping(sgt.segment_name) for sgt in segments if sgt.thrombosis == True])}"


def Sept_Thrombus_No_stenosis_generator(state: CoronarySegmentation):
    segments = Sept_segments_parser(state)
    lesions = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.stenosis == "0" and x.thrombosis == True,
    )
    if len(lesions) == 0:
        return ""

    for lesion in lesions:
        report += Sept_thrombus_description(lesion)

        stent = [sgt for sgt in lesion if sgt.stent == True]
        if len(stent) > 0:
            report += " au niveau du site d'implantation d'un stent"
        report += " sans lesion angiographiquement significative sous-jacente"

    return report
