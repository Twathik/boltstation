from typing import List

from src.lib.generate_coronarography.generators.segment_generators.Diag.Diag_segments import (
    Diag_segments_parser,
)
from src.lib.generate_coronarography.utils.coronarography_classes import (
    CoronarySegmentDescription,
    CoronarySegmentation,
)
from src.lib.generate_coronarography.utils.segment_description import (
    generic_condition_parser,
)
from src.lib.generate_coronarography.utils.segments_mapping import segments_mapping


def Diag_thrombus_description(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):
    [
        Diag1_ostium,
        Diag1,
        Diag2_ostium,
        Diag2,
    ] = Diag_segments_parser(state)

    target = segments[0]

    if len(segments) == 2:
        if Diag1_ostium.thrombosis and Diag1.thrombosis:
            return f"Presence d'un thrombus au niveau de la première diagonale à partir de son ostium"
        if Diag2_ostium.thrombosis and Diag2.thrombosis:
            return f"Presence d'un thrombus au niveau de la première diagonale à partir de son ostium"

    if len(segments) == 1:

        return f"Presence d'un thrombus au niveau de {segments_mapping(target.segment_name)}"

    return f"Presence d'un thrombus au niveau de {",".join([segments_mapping(sgt.segment_name) for sgt in segments if sgt.thrombosis == True])}"


def Diag_Thrombus_No_stenosis_generator(state: CoronarySegmentation):
    segments = Diag_segments_parser(state)
    lesions = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.stenosis == "0" and x.thrombosis == True,
    )
    if len(lesions) == 0:
        return ""

    for lesion in lesions:
        report += Diag_thrombus_description(state, lesion)

        stent = [sgt for sgt in lesion if sgt.stent == True]
        if len(stent) > 0:
            report += " au niveau du site d'implantation d'un stent"
        report += " sans lesion angiographiquement significative sous-jacente"

    return report
