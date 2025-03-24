from typing import List

from src.lib.generate_coronarography.generators.segment_generators.CD.CD_segments import (
    CD_segments_parser,
)
from src.lib.generate_coronarography.utils.coronarography_classes import (
    CoronarySegmentDescription,
    CoronarySegmentation,
)
from src.lib.generate_coronarography.utils.segment_description import (
    generic_condition_parser,
)
from src.lib.generate_coronarography.utils.segments_mapping import segments_mapping


def CD_stent_description(
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
        if CD1_ostium.stent and CD1_proximal.stent and CD1_distal.stent:

            return (
                f"Presence d'un stent au niveau de la coronaire droite ostio-proximale"
            )

    if len(segments) == 2:
        if CD1_proximal.stent and CD1_ostium.stent:
            return (
                f"Presence d'un stent au niveau de la coronaire droite ostio-proximale"
            )
        if CD1_proximal.stent and CD1_distal.stent:
            return f"Presence d'un stent au niveau de la coronaire droite proximale"
        if CD2_proximal.stent and CD2_distal.stent:
            return f"Presence d'un stent au niveau de la coronaire droite moyenne"

    if len(segments) == 1:

        return (
            f"Presence d'un stent au niveau de {segments_mapping(target.segment_name)}"
        )

    return f"Presence d'un stent allant de {segments_mapping(segments[0].segment_name)} à {segments_mapping(segments[-1].segment_name)}"


def CD_stent_No_lesion_generator(state: CoronarySegmentation):
    segments = CD_segments_parser(state)
    stents = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.stenosis == "0"
        and x.stent == True
        and x.thrombosis == False
        and x.calcification == False,
    )

    report = (
        f"presence de {len(stents)} stents au niveau de la coronaire droite. "
        if len(stents) > 1
        else ""
    )

    for stent in stents:
        report += CD_stent_description(state, stent)
        report += " sans lesion angiographiquement significative sous-jacente"

    return report
