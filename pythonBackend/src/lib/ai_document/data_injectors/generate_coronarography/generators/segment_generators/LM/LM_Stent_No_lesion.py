from typing import List

from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.LM.LM_segments import (
    LM_segments_parser,
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


def LM_stent_description(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):
    [
        LM_proximal,
        LM_medium,
        LM_distal,
    ] = LM_segments_parser(state)

    target = segments[0]

    if len(segments) == 3:
        if LM_proximal.stent and LM_medium.stent and LM_distal.stent:
            return f"Presence d'un stent long au niveau du tronc commun gauche"

    if len(segments) == 2:
        if LM_medium.stent and LM_proximal.stent:
            return (
                f"Presence d'un stent au niveau du tronc commun gauche ostio-proximale"
            )
        if LM_medium.stent and LM_distal.stent:
            return f"Presence d'un stent au niveau du tronc commun gauche"

    if len(segments) == 1:

        return (
            f"Presence d'un stent au niveau de {segments_mapping(target.segment_name)}"
        )

    return f"Presence d'un stent allant de {segments_mapping(segments[0].segment_name)} à {segments_mapping(segments[-1].segment_name)}"


def LM_stent_No_lesion_generator(state: CoronarySegmentation):
    segments = LM_segments_parser(state)
    stents = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.stenosis == "0"
        and x.stent == True
        and x.thrombosis == False
        and x.calcification == False,
    )

    report = (
        f"presence de {len(stents)} stents au niveau du tronc commun gauche. "
        if len(stents) > 1
        else ""
    )

    for stent in stents:
        report += LM_stent_description(state, stent)
        report += " sans lesion angiographiquement significative sous-jacente"

    return report
