from typing import List
from src.lib.generate_coronarography.generators.segment_generators.LAD.LAD_dissection_parser import (
    LAD_dissection_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.LAD.LAD_segments import (
    LAD_children_parser,
    LAD_lesions_parser,
    LAD_segments_parser,
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


def LAD_lesion_description(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):
    [
        LAD1_ostium,
        LAD1_proximal,
        LAD1_distal,
        LAD2_proximal,
        LAD2_distal,
        LAD3_proximal,
        LAD3_distal,
    ] = LAD_segments_parser(state)

    target = segments[0]

    if len(segments) == 3:
        if (
            not LAD1_ostium.stenosis == "0"
            and not LAD1_proximal.stenosis == "0"
            and not LAD1_distal.stenosis == "0"
        ):
            return f"Stenose de {target.stenosis}% au niveau de l'interventriculaire antérieure ostio-proximale{stent_parser(segments)}{lesion_description(target)} "

    if len(segments) == 2:
        if not LAD1_ostium.stenosis == "0" and not LAD1_proximal.stenosis == "0":
            return f"Sténose de {target.stenosis}% au niveau de l'interventriculaire antérieure ostio-proximale{stent_parser(segments)}{lesion_description(target)} "
        if not LAD1_proximal.stenosis == "0" and not LAD1_distal.stenosis == "0":
            return f"Sténose de {target.stenosis}% au niveau de l'interventriculaire antérieure proximale{stent_parser(segments)}{lesion_description(target)} "
        if not LAD2_proximal.stenosis == "0" and not LAD2_distal.stenosis == "0":
            return f"Sténose de {target.stenosis}% au niveau de l'interventriculaire antérieure moyenne{stent_parser(segments)}{lesion_description(target)} "
        if not LAD3_proximal.stenosis == "0" and not LAD3_distal.stenosis == "0":
            return f"Sténose de {target.stenosis}% au niveau de l'interventriculaire antérieure distale{stent_parser(segments)}{lesion_description(target)} "
    if len(segments) == 1:

        return f"Sténose de {target.stenosis}% au niveau de {segments_mapping(target.segment_name)}{stent_parser(segments)}{lesion_description(target)} "

    return f"Sténose de {target.stenosis}% allant de {segments_mapping(segments[0].segment_name)} à {segments_mapping(segments[-1].segment_name)} {stent_parser(segments)}{lesion_description(target)} "


def LAD_stenosis_parser(state: CoronarySegmentation):

    lesions = LAD_lesions_parser(state)
    report = (
        f"presence de {len(lesions)} lesions au niveau de l'interventriculaire anterieur. "
        if len(lesions) > 1
        else ""
    )

    for lesion in lesions:
        report += LAD_lesion_description(state, lesion)
        report += LAD_children_parser(state, lesion)

    return report


def LAD_stenosis_generator(state: CoronarySegmentation, LAD_report: str):

    LAD_report = ""
    LAD_report += LAD_stenosis_parser(state)
    LAD_report += LAD_dissection_generator(state)

    occluded_segments = [
        sgt for sgt in LAD_segments_parser(state=state) if sgt.stenosis == "100"
    ]
    LAD_report += total_occlusion_parser(occluded_segments)

    LAD_report += rantrop_parser(state, occluded_segments)

    return LAD_report
