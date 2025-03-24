from typing import List

from src.lib.generate_coronarography.generators.segment_generators.LM.LM_segments import (
    LM_segments_parser,
)
from src.lib.generate_coronarography.utils.coronarography_classes import (
    CoronarySegmentDescription,
    CoronarySegmentation,
)
from src.lib.generate_coronarography.utils.segment_description import (
    generic_condition_parser,
)
from src.lib.generate_coronarography.utils.segments_mapping import segments_mapping


def LM_calcification_description(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):
    [
        LM_proximal,
        LM_medium,
        LM_distal,
    ] = LM_segments_parser(state)

    target = segments[0]

    if len(segments) == 3:
        if (
            LM_proximal.calcification
            and LM_medium.calcification
            and LM_distal.calcification
        ):

            return f"Presence d'une calcification diffuses au niveau du tronc commun gauche dès son ostium"

    if len(segments) == 2:
        if LM_medium.calcification and LM_proximal.calcification:
            return f"Presence d'une calcification ostio-proximale au niveau du tronc commun gauche"
        if LM_medium.calcification and LM_distal.calcification:
            return f"Presence d'une calcification au niveau du tronc commun gauche"

    if len(segments) == 1:

        return f"Presence d'une calcification au niveau de {segments_mapping(target.segment_name)}"

    return f"Presence d'une calcification allant de {segments_mapping(segments[0].segment_name)} à {segments_mapping(segments[-1].segment_name)}"


def LM_calcification_No_stenosis_generator(state: CoronarySegmentation):
    segments = LM_segments_parser(state)
    lesions = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.stenosis == "0" and x.calcification == True,
    )
    print(lesions)
    report = (
        f"presence de {len(lesions)} calcification au niveau du tronc commun gauche. "
        if len(lesions) > 1
        else ""
    )

    for lesion in lesions:
        report += LM_calcification_description(state, lesion)
        stent = [sgt for sgt in lesion if sgt.stent == True]
        if len(stent) > 0:
            report += " au niveau du site d'implantation d'un stent"
        report += " sans lesion angiographiquement significative sous-jacente"

    return report
