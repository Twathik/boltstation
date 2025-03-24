from typing import List
from src.lib.generate_coronarography.generators.segment_generators.LAD.LAD_segments import (
    LAD_segments_parser,
)
from src.lib.generate_coronarography.utils.coronarography_classes import (
    CoronarySegmentDescription,
    CoronarySegmentation,
)
from src.lib.generate_coronarography.utils.segment_description import (
    generic_condition_parser,
)
from src.lib.generate_coronarography.utils.segments_mapping import segments_mapping


def LAD_stent_description(
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
        if LAD1_ostium.stent and LAD1_proximal.stent and LAD1_distal.stent:

            return f"Presence d'un stent au niveau de l'interventriculaire antérieure ostio-proximale"

    if len(segments) == 2:
        if LAD1_proximal.stent and LAD1_ostium.stent:
            return f"Presence d'un stent au niveau de l'interventriculaire antérieure ostio-proximale"
        if LAD1_proximal.stent and LAD1_distal.stent:
            return f"Presence d'un stent au niveau de l'interventriculaire antérieure proximale"
        if LAD2_proximal.stent and LAD2_distal.stent:
            return f"Presence d'un stent au niveau de l'interventriculaire antérieure moyenne"
        if LAD3_proximal.stent and LAD3_distal.stent:
            return f"Presence d'un stent au niveau de l'interventriculaire antérieure distale"
    if len(segments) == 1:

        return (
            f"Presence d'un stent au niveau de {segments_mapping(target.segment_name)}"
        )

    return f"Presence d'un stent allant de {segments_mapping(segments[0].segment_name)} à {segments_mapping(segments[-1].segment_name)}"


def LAD_stent_No_lesion_generator(state: CoronarySegmentation):
    segments = LAD_segments_parser(state)
    stents = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.stenosis == "0"
        and x.stent == True
        and x.thrombosis == False
        and x.calcification == False,
    )

    report = (
        f"presence de {len(stents)} stents au niveau de l'interventriculaire anterieure. "
        if len(stents) > 1
        else ""
    )

    for stent in stents:
        report += LAD_stent_description(state, stent)
        report += " sans lesion angiographiquement significative sous-jacente"

    return report
