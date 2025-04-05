from typing import List
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.Marg.Marg_segments import (
    Marg_segments_parser,
)

from src.lib.ai_document.data_injectors.generate_coronarography.utils.segment_description import (
    generic_condition_parser,
)
from src.lib.ai_document.data_injectors.generate_coronarography.utils.segments_mapping import (
    segments_mapping,
)
from src.lib.ai_document.utils.ai_document_classes import (
    CoronarySegmentDescription,
    CoronarySegmentation,
)


def Marg_stent_description(
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
        if Marg1_ostium.stent and Marg1_proximal.stent and Marg1_distal.stent:
            return f"Presence d'un stent long au niveau de la première marginale"
        if Marg2_ostium.stent and Marg2_proximal.stent and Marg2_distal.stent:
            return f"Presence d'un stent long au niveau de la deuxième marginale"

    if len(segments) == 2:
        if Marg1_proximal.stent and Marg1_ostium.stent:
            return f"Presence d'un stent au niveau de la première marginale ostio-proximale"
        if Marg1_proximal.stent and Marg1_distal.stent:
            return f"Presence d'un stent au niveau de la première marginale"
        if Marg2_proximal.stent and Marg2_ostium.stent:
            return f"Presence d'un stent au niveau de la deuxième marginale ostio-proximale"
        if Marg2_proximal.stent and Marg2_distal.stent:
            return f"Presence d'un stent au niveau de la deuxième marginale"
    if len(segments) == 1:

        return (
            f"Presence d'un stent au niveau de {segments_mapping(target.segment_name)}"
        )

    return f"Presence d'un stent allant de {segments_mapping(segments[0].segment_name)} à {segments_mapping(segments[-1].segment_name)}"


def Marg_stent_No_lesion_generator(state: CoronarySegmentation):
    segments = Marg_segments_parser(state)
    stents = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.stenosis == "0"
        and x.stent == True
        and x.thrombosis == False
        and x.calcification == False,
    )

    report = (
        f"presence de {len(stents)} stents au niveau des marginales. "
        if len(stents) > 1
        else ""
    )

    for stent in stents:
        report += Marg_stent_description(state, stent)
        report += " sans lesion angiographiquement significative sous-jacente"

    return report
