from typing import List

from src.lib.generate_coronarography.generators.segment_generators.Bisec.Bisec_segments import (
    Bisec_segments_parser,
)
from src.lib.generate_coronarography.utils.coronarography_classes import (
    CoronarySegmentDescription,
    CoronarySegmentation,
)
from src.lib.generate_coronarography.utils.segment_description import (
    generic_condition_parser,
)
from src.lib.generate_coronarography.utils.segments_mapping import segments_mapping


def Bisec_stent_description(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):
    [
        Bisec_ostium,
        Bisec_proximal,
        Bisec_distal,
    ] = Bisec_segments_parser(state)

    target = segments[0]

    if len(segments) == 3:
        return "Presence d'un stent au niveau de la bissectrice à partir de son ostium"

    if len(segments) == 2:
        if Bisec_ostium.stent and Bisec_proximal.stent:
            return f"Presence d'un stent au niveau de la bissectrice à partir de son ostium"
        if Bisec_proximal.stent and Bisec_distal.stent:
            return f"Presence d'un stent au niveau de la bissectrice"

    if len(segments) == 1:

        return (
            f"Presence d'un stent au niveau de {segments_mapping(target.segment_name)}"
        )

    return f"Presence d'un stent au niveau de {",".join([segments_mapping(sgt.segment_name) for sgt in segments if sgt.stent == True])}"


def Bisec_stent_No_lesion_generator(state: CoronarySegmentation):
    segments = Bisec_segments_parser(state)
    stents = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.stenosis == "0"
        and x.stent == True
        and x.thrombosis == False
        and x.calcification == False,
    )

    if len(stents) == 0:
        return ""

    for stent in stents:
        report += Bisec_stent_description(state, stent)
        report += " sans lesion angiographiquement significative sous-jacente"

    return report
