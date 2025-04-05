from typing import List
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.Marg.Marg_dissection_parser import (
    Marg_dissection_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.Marg.Marg_segments import (
    Marg_lesions_parser,
    Marg_segments_parser,
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


def Marg_lesion_description(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):
    [
        Marg1_ostium,
        Marg1_proximal,
        Marg1_distal,
        Marg2_proximal,
        Marg2_distal,
        Marg2_ostium,
    ] = Marg_segments_parser(state)

    target = segments[0]

    if len(segments) == 3:
        if (
            not Marg1_ostium.stenosis == "0"
            and not Marg1_proximal.stenosis == "0"
            and not Marg1_distal.stenosis == "0"
        ):
            return f"Sténose longue de {target.stenosis}% au niveau de la première marginale dès son ostium{stent_parser(segments)}{lesion_description(target)} "
        if (
            not Marg2_ostium.stenosis == "0"
            and not Marg2_proximal.stenosis == "0"
            and not Marg2_distal.stenosis == "0"
        ):
            return f"Sténose longue de {target.stenosis}% au niveau de la deuxième marginale dès son ostium{stent_parser(segments)}{lesion_description(target)} "

    if len(segments) == 2:
        if not Marg1_ostium.stenosis == "0" and not Marg1_proximal.stenosis == "0":
            return f"Sténose de {target.stenosis}% au niveau de la première marginale ostio-marginale{stent_parser(segments)}{lesion_description(target)} "
        if not Marg1_proximal.stenosis == "0" and not Marg1_distal.stenosis == "0":
            return f"Sténose de {target.stenosis}% au niveau de la première marginale{stent_parser(segments)}{lesion_description(target)} "

        if not Marg2_ostium.stenosis == "0" and not Marg2_proximal.stenosis == "0":
            return f"Sténose de {target.stenosis}% au niveau de la première deuxième ostio-marginale{stent_parser(segments)}{lesion_description(target)} "
        if not Marg2_proximal.stenosis == "0" and not Marg2_distal.stenosis == "0":
            return f"Sténose de {target.stenosis}% au niveau de la première deuxième{stent_parser(segments)}{lesion_description(target)} "

    if len(segments) == 1:
        return f"Sténose de {target.stenosis}% au niveau de {segments_mapping(target.segment_name)}{stent_parser(segments)}{lesion_description(target)} "

    return f"Sténose de {target.stenosis}% allant de {segments_mapping(segments[0].segment_name)} à {segments_mapping(segments[-1].segment_name)} {stent_parser(segments)}{lesion_description(target)} "


def Marg_stenosis_parser(state: CoronarySegmentation):

    lesions = Marg_lesions_parser(state)
    report = (
        f"presence de {len(lesions)} lesions au niveau des marginales. "
        if len(lesions) > 1
        else ""
    )

    for lesion in lesions:
        report += Marg_lesion_description(state, lesion)

    return report


def Marg_stenosis_generator(state: CoronarySegmentation, Marg_report: str):

    Marg_report = ""
    Marg_report += Marg_stenosis_parser(state)
    Marg_report += Marg_dissection_generator(state)

    occluded_segments = [
        sgt for sgt in Marg_segments_parser(state=state) if sgt.stenosis == "100"
    ]
    Marg_report += total_occlusion_parser(occluded_segments)

    Marg_report += rantrop_parser(state, occluded_segments)

    return Marg_report
