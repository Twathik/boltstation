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


def IVPL_thrombus_description(
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
            IVPL_ostium.thrombosis
            and IVPL_proximal.thrombosis
            and IVPL_distal.thrombosis
        ):

            return f"Presence d'un thrombus extensif au niveau de l'interventriculaire postérieure gauche"

    if len(segments) == 2:
        if IVPL_proximal.thrombosis and IVPL_ostium.thrombosis:
            return f"Presence d'un thrombus au niveau de l'interventriculaire postérieure gauche ostio-proximale"
        if IVPL_proximal.thrombosis and IVPL_distal.thrombosis:
            return f"Presence d'un thrombus au niveau de l'interventriculaire postérieure gauche"

    if len(segments) == 1:

        return f"Presence d'un thrombus au niveau de {segments_mapping(target.segment_name)}"

    return f"Presence d'un thrombus allant de {segments_mapping(segments[0].segment_name)} à {segments_mapping(segments[-1].segment_name)}"


def IVPL_Thrombus_No_stenosis_generator(state: CoronarySegmentation):
    segments = IVPL_segments_parser(state)
    lesions = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.stenosis == "0" and x.thrombosis == True,
    )
    print(lesions)
    report = (
        f"presence de {len(lesions)} thrombus au niveau de l'interventriculaire postérieure gauche. "
        if len(lesions) > 1
        else ""
    )

    for lesion in lesions:
        report += IVPL_thrombus_description(state, lesion)

        stent = [sgt for sgt in lesion if sgt.stent == True]
        if len(stent) > 0:
            report += " au niveau du site d'implantation d'un stent"
        report += " sans lesion angiographiquement significative sous-jacente"

    return report
