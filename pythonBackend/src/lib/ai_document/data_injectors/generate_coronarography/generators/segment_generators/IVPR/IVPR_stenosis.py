from typing import List

from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.IVPR.IVPR_dissection_parser import (
    IVPR_dissection_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.IVPR.IVPR_segments import (
    IVPR_lesions_parser,
    IVPR_segments_parser,
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


def IVPR_lesion_description(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):
    [
        IVPR_ostium,
        IVPR_proximal,
        IVPR_distal,
    ] = IVPR_segments_parser(state)

    target = segments[0]

    if len(segments) == 3:
        if (
            not IVPR_ostium.stenosis == "0"
            and not IVPR_proximal.stenosis == "0"
            and not IVPR_distal.stenosis == "0"
        ):
            return f"Sténose longue de {target.stenosis}% au niveau de l'interventriculaire postérieure droite dès son ostium{stent_parser(segments)}{lesion_description(target)} "

    if len(segments) == 2:
        if not IVPR_ostium.stenosis == "0" and not IVPR_proximal.stenosis == "0":
            return f"Sténose de {target.stenosis}% au niveau de l'interventriculaire postérieure droite ostio-marginale{stent_parser(segments)}{lesion_description(target)} "
        if not IVPR_proximal.stenosis == "0" and not IVPR_distal.stenosis == "0":
            return f"Sténose de {target.stenosis}% au niveau de l'interventriculaire postérieure droite{stent_parser(segments)}{lesion_description(target)} "

    if len(segments) == 1:
        return f"Sténose de {target.stenosis}% au niveau de {segments_mapping(target.segment_name)}{stent_parser(segments)}{lesion_description(target)} "

    return f"Sténose de {target.stenosis}% allant de {segments_mapping(segments[0].segment_name)} à {segments_mapping(segments[-1].segment_name)} {stent_parser(segments)}{lesion_description(target)} "


def IVPR_stenosis_parser(state: CoronarySegmentation):

    lesions = IVPR_lesions_parser(state)
    report = (
        f"presence de {len(lesions)} lesions au niveau de l'interventriculaire postérieure droite. "
        if len(lesions) > 1
        else ""
    )

    for lesion in lesions:
        report += IVPR_lesion_description(state, lesion)

    return report


def IVPR_stenosis_generator(state: CoronarySegmentation, IVPR_report: str):

    IVPR_report = ""
    IVPR_report += IVPR_stenosis_parser(state)
    IVPR_report += IVPR_dissection_generator(state)

    occluded_segments = [
        sgt for sgt in IVPR_segments_parser(state=state) if sgt.stenosis == "100"
    ]
    IVPR_report += total_occlusion_parser(occluded_segments)

    IVPR_report += rantrop_parser(state, occluded_segments)

    return IVPR_report
