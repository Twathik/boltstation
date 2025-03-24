from typing import List

from src.lib.generate_coronarography.generators.segment_generators.IVPL.IVPL_segments import (
    IVPL_segments_parser,
)
from src.lib.generate_coronarography.utils.coronarography_classes import (
    CoronarySegmentDescription,
    CoronarySegmentation,
)
from src.lib.generate_coronarography.utils.segment_description import (
    generic_condition_parser,
)
from src.lib.generate_coronarography.utils.segments_mapping import segments_mapping


def IVPL_calcification_description(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):
    [
        IVPL_ostium,
        IVPL_proximal,
        IVPL_distal,
    ] = IVPL_segments_parser(state)

    target = segments[0]

    if len(segments) == 3:
        if (
            IVPL_ostium.calcification
            and IVPL_proximal.calcification
            and IVPL_distal.calcification
        ):

            return f"Presence d'une calcification diffuses au niveau de l'interventriculaire postérieure gauche dès son ostium"

    if len(segments) == 2:
        if IVPL_proximal.calcification and IVPL_ostium.calcification:
            return f"Presence d'une calcification ostio-proximale au niveau de l'interventriculaire postérieure gauche"
        if IVPL_proximal.calcification and IVPL_distal.calcification:
            return f"Presence d'une calcification au niveau de l'interventriculaire postérieure gauche"

    if len(segments) == 1:

        return f"Presence d'une calcification au niveau de {segments_mapping(target.segment_name)}"

    return f"Presence d'une calcification allant de {segments_mapping(segments[0].segment_name)} à {segments_mapping(segments[-1].segment_name)}"


def IVPL_calcification_No_stenosis_generator(state: CoronarySegmentation):
    segments = IVPL_segments_parser(state)
    lesions = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.stenosis == "0" and x.calcification == True,
    )
    print(lesions)
    report = (
        f"presence de {len(lesions)} calcification au niveau de l'interventriculaire postérieure gauche. "
        if len(lesions) > 1
        else ""
    )

    for lesion in lesions:
        report += IVPL_calcification_description(state, lesion)
        stent = [sgt for sgt in lesion if sgt.stent == True]
        if len(stent) > 0:
            report += " au niveau du site d'implantation d'un stent"
        report += " sans lesion angiographiquement significative sous-jacente"

    return report
