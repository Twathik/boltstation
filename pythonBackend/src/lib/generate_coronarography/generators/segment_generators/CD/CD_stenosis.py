from typing import List

from src.lib.generate_coronarography.generators.segment_generators.CD.CD_dissection_parser import (
    CD_dissection_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.CD.CD_segments import (
    CD_children_parser,
    CD_lesions_parser,
    CD_segments_parser,
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


def CD_lesion_description(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):
    [
        CD1_ostium,
        CD1_proximal,
        CD1_distal,
        CD2_proximal,
        CD2_distal,
    ] = CD_segments_parser(state)

    target = segments[0]

    if len(segments) == 3:
        if (
            not CD1_ostium.stenosis == "0"
            and not CD1_proximal.stenosis == "0"
            and not CD1_distal.stenosis == "0"
        ):
            return f"Stenose de {target.stenosis}% au niveau de la coronaire droite ostio-proximale{stent_parser(segments)}{lesion_description(target)} "

    if len(segments) == 2:
        if not CD1_ostium.stenosis == "0" and not CD1_proximal.stenosis == "0":
            return f"Sténose de {target.stenosis}% au niveau de la coronaire droite ostio-proximale{stent_parser(segments)}{lesion_description(target)} "
        if not CD1_proximal.stenosis == "0" and not CD1_distal.stenosis == "0":
            return f"Sténose de {target.stenosis}% au niveau de la coronaire droite proximale{stent_parser(segments)}{lesion_description(target)} "
        if not CD2_proximal.stenosis == "0" and not CD2_distal.stenosis == "0":
            return f"Sténose de {target.stenosis}% au niveau de la coronaire droite moyenne{stent_parser(segments)}{lesion_description(target)} "

    if len(segments) == 1:

        return f"Sténose de {target.stenosis}% au niveau de {segments_mapping(target.segment_name)}{stent_parser(segments)}{lesion_description(target)} "

    return f"Sténose de {target.stenosis}% allant de {segments_mapping(segments[0].segment_name)} à {segments_mapping(segments[-1].segment_name)} {stent_parser(segments)}{lesion_description(target)} "


def CD_stenosis_parser(state: CoronarySegmentation):

    lesions = CD_lesions_parser(state)
    report = (
        f"presence de {len(lesions)} lesions au niveau de la coronaire droite. "
        if len(lesions) > 1
        else ""
    )

    for lesion in lesions:
        report += CD_lesion_description(state, lesion)
        report += CD_children_parser(state, lesion)

    return report


def CD_stenosis_generator(state: CoronarySegmentation, CD_report: str):

    CD_report = ""
    CD_report += CD_stenosis_parser(state)
    CD_report += CD_dissection_generator(state)

    occluded_segments = [
        sgt for sgt in CD_segments_parser(state=state) if sgt.stenosis == "100"
    ]
    CD_report += total_occlusion_parser(occluded_segments)

    CD_report += rantrop_parser(state, occluded_segments)

    return CD_report
