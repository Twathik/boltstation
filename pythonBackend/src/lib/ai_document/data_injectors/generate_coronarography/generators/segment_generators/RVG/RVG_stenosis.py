from typing import List

from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.RVG.RVG_dissection_parser import (
    RVG_dissection_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.RVG.RVG_segments import (
    RVG_lesions_parser,
    RVG_segments_parser,
)

from src.lib.ai_document.data_injectors.generate_coronarography.utils.Lesion_stent import (
    stent_parser,
)
from src.lib.ai_document.data_injectors.generate_coronarography.utils.find_rantrop_location import (
    rantrop_parser,
    total_occlusion_parser,
)
from src.lib.ai_document.data_injectors.generate_coronarography.utils.segment_description import (
    lesion_description,
)
from src.lib.ai_document.data_injectors.generate_coronarography.utils.segments_mapping import (
    segments_mapping,
)
from src.lib.ai_document.utils.ai_document_classes import (
    CoronarySegmentDescription,
    CoronarySegmentation,
)


def RVG_lesion_description(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):
    [
        RVG_ostium,
        RVG_proximal,
        RVG_distal,
    ] = RVG_segments_parser(state)

    target = segments[0]

    if len(segments) == 3:
        if (
            not RVG_ostium.stenosis == "0"
            and not RVG_proximal.stenosis == "0"
            and not RVG_distal.stenosis == "0"
        ):
            return f"Sténose longue de {target.stenosis}% au niveau de la rétro ventriculaire gauche dès son ostium{stent_parser(segments)}{lesion_description(target)} "

    if len(segments) == 2:
        if not RVG_ostium.stenosis == "0" and not RVG_proximal.stenosis == "0":
            return f"Sténose de {target.stenosis}% au niveau de la rétro ventriculaire gauche ostio-marginale{stent_parser(segments)}{lesion_description(target)} "
        if not RVG_proximal.stenosis == "0" and not RVG_distal.stenosis == "0":
            return f"Sténose de {target.stenosis}% au niveau de la rétro ventriculaire gauche{stent_parser(segments)}{lesion_description(target)} "

    if len(segments) == 1:
        return f"Sténose de {target.stenosis}% au niveau de {segments_mapping(target.segment_name)}{stent_parser(segments)}{lesion_description(target)} "

    return f"Sténose de {target.stenosis}% allant de {segments_mapping(segments[0].segment_name)} à {segments_mapping(segments[-1].segment_name)} {stent_parser(segments)}{lesion_description(target)} "


def RVG_stenosis_parser(state: CoronarySegmentation):

    lesions = RVG_lesions_parser(state)
    report = (
        f"presence de {len(lesions)} lesions au niveau de la rétro ventriculaire gauche. "
        if len(lesions) > 1
        else ""
    )

    for lesion in lesions:
        report += RVG_lesion_description(state, lesion)

    return report


def RVG_stenosis_generator(state: CoronarySegmentation, RVG_report: str):

    RVG_report = ""
    RVG_report += RVG_stenosis_parser(state)
    RVG_report += RVG_dissection_generator(state)

    occluded_segments = [
        sgt for sgt in RVG_segments_parser(state=state) if sgt.stenosis == "100"
    ]
    RVG_report += total_occlusion_parser(occluded_segments)

    RVG_report += rantrop_parser(state, occluded_segments)

    return RVG_report
