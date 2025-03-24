from typing import List
from src.lib.generate_coronarography.generators.segment_generators.Marg.Marg_segments import (
    Marg_segments_parser,
)
from src.lib.generate_coronarography.utils.coronarography_classes import (
    CoronarySegmentDescription,
    CoronarySegmentation,
)
from src.lib.generate_coronarography.utils.segment_description import (
    generic_condition_parser,
)
from src.lib.generate_coronarography.utils.segments_mapping import segments_mapping


def Marg_thrombus_description(
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
        if (
            Marg1_ostium.thrombosis
            and Marg1_proximal.thrombosis
            and Marg1_distal.thrombosis
        ):

            return f"Presence d'un thrombus extensif au niveau de la première marginale"
        if (
            Marg2_ostium.thrombosis
            and Marg2_proximal.thrombosis
            and Marg2_distal.thrombosis
        ):

            return f"Presence d'un thrombus extensif au niveau de la deuxième marginale"

    if len(segments) == 2:
        if Marg1_proximal.thrombosis and Marg1_ostium.thrombosis:
            return f"Presence d'un thrombus au niveau de la première marginale ostio-proximale"
        if Marg1_proximal.thrombosis and Marg1_distal.thrombosis:
            return f"Presence d'un thrombus au niveau de la première marginale"

        if Marg2_proximal.thrombosis and Marg2_ostium.thrombosis:
            return f"Presence d'un thrombus au niveau de la deuxième marginale ostio-proximale"
        if Marg2_proximal.thrombosis and Marg2_distal.thrombosis:
            return f"Presence d'un thrombus au niveau de la deuxième marginale"

    if len(segments) == 1:

        return f"Presence d'un thrombus au niveau de {segments_mapping(target.segment_name)}"

    return f"Presence d'un thrombus allant de {segments_mapping(segments[0].segment_name)} à {segments_mapping(segments[-1].segment_name)}"


def Marg_Thrombus_No_stenosis_generator(state: CoronarySegmentation):
    segments = Marg_segments_parser(state)
    lesions = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.stenosis == "0" and x.thrombosis == True,
    )
    print(lesions)
    report = (
        f"presence de {len(lesions)} thrombus au niveau des marginales. "
        if len(lesions) > 1
        else ""
    )

    for lesion in lesions:
        report += Marg_thrombus_description(state, lesion)

        stent = [sgt for sgt in lesion if sgt.stent == True]
        if len(stent) > 0:
            report += " au niveau du site d'implantation d'un stent"
        report += " sans lesion angiographiquement significative sous-jacente"

    return report
