from typing import List

from src.lib.generate_coronarography.generators.segment_generators.Sept.Sept_dissection_parser import (
    Sept_dissection_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.Sept.Sept_segments import (
    Sept_lesions_parser,
    Sept_segments_parser,
)
from src.lib.generate_coronarography.utils.coronarography_classes import (
    CoronarySegmentDescription,
    CoronarySegmentation,
)
from src.lib.generate_coronarography.utils.Lesion_stent import (
    stent_parser,
)
from src.lib.generate_coronarography.utils.find_rantrop_location import (
    rantrop_parser,
    total_occlusion_parser,
)
from src.lib.generate_coronarography.utils.segment_description import (
    lesion_description,
)
from src.lib.generate_coronarography.utils.segments_mapping import segments_mapping


def Sept_lesion_description(segments: List[CoronarySegmentDescription]):

    target = segments[0]

    return f"Sténose de {target.stenosis}% au niveau de {",".join([segments_mapping(sgt.segment_name) + stent_parser(segments)+lesion_description(target) for sgt in segments if not sgt.stenosis == '0'])}"


def Sept_stenosis_parser(state: CoronarySegmentation):

    lesions = Sept_lesions_parser(state)
    report = (
        f"presence de {len(lesions)} lesions au niveau des septales. "
        if len(lesions) > 1
        else ""
    )

    for lesion in lesions:
        report += Sept_lesion_description(lesion)

    return report


def Sept_stenosis_generator(state: CoronarySegmentation, Sept_report: str):

    Sept_report = ""
    Sept_report += Sept_stenosis_parser(state)
    Sept_report += Sept_dissection_generator(state)

    occluded_segments = [
        sgt for sgt in Sept_segments_parser(state=state) if sgt.stenosis == "100"
    ]
    Sept_report += total_occlusion_parser(occluded_segments)

    Sept_report += rantrop_parser(state, occluded_segments)

    return Sept_report
