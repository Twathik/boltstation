from typing import List

from src.lib.generate_coronarography.generators.segment_generators.CX.Cx_dissection_parser import (
    Cx_dissection_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.CX.Cx_segments import (
    Cx_children_parser,
    Cx_lesions_parser,
    Cx_segments_parser,
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


def Cx_lesion_description(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):
    [
        Cx1_ostium,
        Cx1_proximal,
        Cx1_distal,
        Cx2_proximal,
        Cx2_distal,
        Cx3_proximal,
        Cx3_distal,
    ] = Cx_segments_parser(state)

    target = segments[0]

    if len(segments) == 3:
        if (
            not Cx1_ostium.stenosis == "0"
            and not Cx1_proximal.stenosis == "0"
            and not Cx1_distal.stenosis == "0"
        ):
            return f"Stenose de {target.stenosis}% au niveau de l'artère circonflexe ostio-proximale{stent_parser(segments)}{lesion_description(target)} "

    if len(segments) == 2:
        if not Cx1_ostium.stenosis == "0" and not Cx1_proximal.stenosis == "0":
            return f"Sténose de {target.stenosis}% au niveau de l'artère circonflexe ostio-proximale{stent_parser(segments)}{lesion_description(target)} "
        if not Cx1_proximal.stenosis == "0" and not Cx1_distal.stenosis == "0":
            return f"Sténose de {target.stenosis}% au niveau de l'artère circonflexe proximale{stent_parser(segments)}{lesion_description(target)} "
        if not Cx2_proximal.stenosis == "0" and not Cx2_distal.stenosis == "0":
            return f"Sténose de {target.stenosis}% au niveau de l'artère circonflexe moyenne{stent_parser(segments)}{lesion_description(target)} "
        if not Cx3_proximal.stenosis == "0" and not Cx3_distal.stenosis == "0":
            return f"Sténose de {target.stenosis}% au niveau de l'artère circonflexe distale{stent_parser(segments)}{lesion_description(target)} "
    if len(segments) == 1:

        return f"Sténose de {target.stenosis}% au niveau de {segments_mapping(target.segment_name)}{stent_parser(segments)}{lesion_description(target)} "

    return f"Sténose de {target.stenosis}% allant de {segments_mapping(segments[0].segment_name)} à {segments_mapping(segments[-1].segment_name)} {stent_parser(segments)}{lesion_description(target)} "


def Cx_stenosis_parser(state: CoronarySegmentation):

    lesions = Cx_lesions_parser(state)
    report = (
        f"presence de {len(lesions)} lesions au niveau de l'artère circonflexe. "
        if len(lesions) > 1
        else ""
    )

    for lesion in lesions:
        report += Cx_lesion_description(state, lesion)
        report += Cx_children_parser(state, lesion)

    return report


def Cx_stenosis_generator(state: CoronarySegmentation, Cx_report: str):

    Cx_report = ""
    Cx_report += Cx_stenosis_parser(state)
    Cx_report += Cx_dissection_generator(state)

    occluded_segments = [
        sgt for sgt in Cx_segments_parser(state=state) if sgt.stenosis == "100"
    ]
    Cx_report += total_occlusion_parser(occluded_segments)

    Cx_report += rantrop_parser(state, occluded_segments)

    return Cx_report
