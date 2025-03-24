from typing import List

from src.lib.generate_coronarography.generators.segment_generators.IVPR.IVPR_segments import (
    IVPR_segments_parser,
)
from src.lib.generate_coronarography.utils.coronarography_classes import (
    CoronarySegmentDescription,
    CoronarySegmentation,
)
from src.lib.generate_coronarography.utils.segment_description import (
    generic_condition_parser,
)
from src.lib.generate_coronarography.utils.segments_mapping import segments_mapping


def IVPR_stent_description(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):
    [
        IVPR_ostium,
        IVPR_proximal,
        IVPR_distal,
    ] = IVPR_segments_parser(state)

    target = segments[0]

    if len(segments) == 3:
        if IVPR_ostium.stent and IVPR_proximal.stent and IVPR_distal.stent:
            return f"Presence d'un stent long au niveau de l'interventriculaire postérieure droite"

    if len(segments) == 2:
        if IVPR_proximal.stent and IVPR_ostium.stent:
            return f"Presence d'un stent au niveau de l'interventriculaire postérieure droite ostio-proximale"
        if IVPR_proximal.stent and IVPR_distal.stent:
            return f"Presence d'un stent au niveau de l'interventriculaire postérieure droite"

    if len(segments) == 1:

        return (
            f"Presence d'un stent au niveau de {segments_mapping(target.segment_name)}"
        )

    return f"Presence d'un stent allant de {segments_mapping(segments[0].segment_name)} à {segments_mapping(segments[-1].segment_name)}"


def IVPR_stent_No_lesion_generator(state: CoronarySegmentation):
    segments = IVPR_segments_parser(state)
    stents = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.stenosis == "0"
        and x.stent == True
        and x.thrombosis == False
        and x.calcification == False,
    )

    report = (
        f"presence de {len(stents)} stents au niveau de l'interventriculaire postérieure droite. "
        if len(stents) > 1
        else ""
    )

    for stent in stents:
        report += IVPR_stent_description(state, stent)
        report += " sans lesion angiographiquement significative sous-jacente"

    return report
