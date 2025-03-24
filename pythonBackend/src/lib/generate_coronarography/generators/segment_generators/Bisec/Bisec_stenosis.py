from typing import List

from src.lib.generate_coronarography.generators.segment_generators.Bisec.Bisec_dissection_parser import (
    Bisec_dissection_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.Bisec.Bisec_segments import (
    Bisec_lesions_parser,
    Bisec_segments_parser,
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


def Bisec_lesion_description(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):
    [
        Bisec_ostium,
        Bisec_proximal,
        Bisec_distal,
    ] = Bisec_segments_parser(state)

    target = segments[0]
    if len(segments) == 3:
        return "Sténose de {target.stenosis}% au niveau de la bissectrice à partir de son ostium"

    if len(segments) == 2:
        if not Bisec_ostium.stenosis == "0" and not Bisec_proximal.stenosis == "0":
            return f"Sténose de {Bisec_proximal.stenosis}% au niveau de la bissectrice à partir de son ostium{stent_parser(segments)}{lesion_description(Bisec_proximal)} "
        if not Bisec_proximal.stenosis == "0" and not Bisec_distal.stenosis == "0":
            return f"Sténose de {Bisec_proximal.stenosis}% au niveau de la bissectrice{stent_parser(segments)}{lesion_description(Bisec_proximal)} "

        f""
    if len(segments) == 1:

        return f"Sténose de {target.stenosis}% au niveau de {segments_mapping(target.segment_name)}{stent_parser(segments)}{lesion_description(target)} "

    return f"Sténose de {target.stenosis}% au niveau de {",".join([segments_mapping(sgt.segment_name) + stent_parser(segments)+lesion_description(target) for sgt in segments if not sgt.stenosis == '0'])}"


def Bisec_stenosis_parser(state: CoronarySegmentation):

    lesions = Bisec_lesions_parser(state)
    report = (
        f"presence de {len(lesions)} lesions au niveau des diagonales. "
        if len(lesions) > 1
        else ""
    )

    for lesion in lesions:
        report += Bisec_lesion_description(state, lesion)

    return report


def Bisec_stenosis_generator(state: CoronarySegmentation, Bisec_report: str):

    Bisec_report = ""
    Bisec_report += Bisec_stenosis_parser(state)
    Bisec_report += Bisec_dissection_generator(state)

    occluded_segments = [
        sgt for sgt in Bisec_segments_parser(state=state) if sgt.stenosis == "100"
    ]
    Bisec_report += total_occlusion_parser(occluded_segments)

    Bisec_report += rantrop_parser(state, occluded_segments)

    return Bisec_report
