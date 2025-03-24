from typing import List

from src.lib.generate_coronarography.generators.segment_generators.CX.Cx_segments import (
    Cx_segments_parser,
)
from src.lib.generate_coronarography.utils.coronarography_classes import (
    CoronarySegmentDescription,
    CoronarySegmentation,
)
from src.lib.generate_coronarography.utils.segment_description import (
    generic_condition_parser,
)
from src.lib.generate_coronarography.utils.segments_mapping import segments_mapping


def Cx_stent_description(
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
        if Cx1_ostium.stent and Cx1_proximal.stent and Cx1_distal.stent:

            return (
                f"Presence d'un stent au niveau de l'artère circonflexe ostio-proximale"
            )

    if len(segments) == 2:
        if Cx1_proximal.stent and Cx1_ostium.stent:
            return (
                f"Presence d'un stent au niveau de l'artère circonflexe ostio-proximale"
            )
        if Cx1_proximal.stent and Cx1_distal.stent:
            return f"Presence d'un stent au niveau de l'artère circonflexe proximale"
        if Cx2_proximal.stent and Cx2_distal.stent:
            return f"Presence d'un stent au niveau de l'artère circonflexe moyenne"
        if Cx3_proximal.stent and Cx3_distal.stent:
            return f"Presence d'un stent au niveau de l'artère circonflexe distale"
    if len(segments) == 1:

        return (
            f"Presence d'un stent au niveau de {segments_mapping(target.segment_name)}"
        )

    return f"Presence d'un stent allant de {segments_mapping(segments[0].segment_name)} à {segments_mapping(segments[-1].segment_name)}"


def Cx_stent_No_lesion_generator(state: CoronarySegmentation):
    segments = Cx_segments_parser(state)
    stents = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.stenosis == "0"
        and x.stent == True
        and x.thrombosis == False
        and x.calcification == False,
    )

    report = (
        f"presence de {len(stents)} stents au niveau de l'artère circonflexe. "
        if len(stents) > 1
        else ""
    )

    for stent in stents:
        report += Cx_stent_description(state, stent)
        report += " sans lesion angiographiquement significative sous-jacente"

    return report
