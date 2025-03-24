from typing import List

from src.lib.generate_coronarography.generators.segment_generators.IVPL.IVPL_dissection_parser import (
    IVPL_dissection_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.IVPL.IVPL_segments import (
    IVPL_lesions_parser,
    IVPL_segments_parser,
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


def IVPL_lesion_description(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):
    [
        IVPL_ostium,
        IVPL_proximal,
        IVPL_distal,
    ] = IVPL_segments_parser(state)

    target = segments[0]

    if len(segments) == 3:
        if (
            not IVPL_ostium.stenosis == "0"
            and not IVPL_proximal.stenosis == "0"
            and not IVPL_distal.stenosis == "0"
        ):
            return f"Sténose longue de {target.stenosis}% au niveau de l'interventriculaire postérieure gauche dès son ostium{stent_parser(segments)}{lesion_description(target)} "

    if len(segments) == 2:
        if not IVPL_ostium.stenosis == "0" and not IVPL_proximal.stenosis == "0":
            return f"Sténose de {target.stenosis}% au niveau de l'interventriculaire postérieure gauche ostio-marginale{stent_parser(segments)}{lesion_description(target)} "
        if not IVPL_proximal.stenosis == "0" and not IVPL_distal.stenosis == "0":
            return f"Sténose de {target.stenosis}% au niveau de l'interventriculaire postérieure gauche{stent_parser(segments)}{lesion_description(target)} "

    if len(segments) == 1:
        return f"Sténose de {target.stenosis}% au niveau de {segments_mapping(target.segment_name)}{stent_parser(segments)}{lesion_description(target)} "

    return f"Sténose de {target.stenosis}% allant de {segments_mapping(segments[0].segment_name)} à {segments_mapping(segments[-1].segment_name)} {stent_parser(segments)}{lesion_description(target)} "


def IVPL_stenosis_parser(state: CoronarySegmentation):

    lesions = IVPL_lesions_parser(state)
    report = (
        f"presence de {len(lesions)} lesions au niveau de l'interventriculaire postérieure gauche. "
        if len(lesions) > 1
        else ""
    )

    for lesion in lesions:
        report += IVPL_lesion_description(state, lesion)

    return report


def IVPL_stenosis_generator(state: CoronarySegmentation, IVPL_report: str):

    IVPL_report = ""
    IVPL_report += IVPL_stenosis_parser(state)
    IVPL_report += IVPL_dissection_generator(state)

    occluded_segments = [
        sgt for sgt in IVPL_segments_parser(state=state) if sgt.stenosis == "100"
    ]
    IVPL_report += total_occlusion_parser(occluded_segments)

    IVPL_report += rantrop_parser(state, occluded_segments)

    return IVPL_report
