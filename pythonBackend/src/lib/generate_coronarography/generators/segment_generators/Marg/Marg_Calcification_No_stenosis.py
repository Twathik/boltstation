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


def Marg_calcification_description(
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
            Marg1_ostium.calcification
            and Marg1_proximal.calcification
            and Marg1_distal.calcification
        ):

            return f"Presence d'une calcification diffuses au niveau de la première marginale dès son ostium"

        if (
            Marg2_ostium.calcification
            and Marg2_proximal.calcification
            and Marg2_distal.calcification
        ):

            return f"Presence d'une calcification diffuses au niveau de la deuxième marginale dès son ostium"

    if len(segments) == 2:
        if Marg1_proximal.calcification and Marg1_ostium.calcification:
            return f"Presence d'une calcification ostio-proximale au niveau de la première marginale"
        if Marg1_proximal.calcification and Marg1_distal.calcification:
            return f"Presence d'une calcification au niveau de la première marginale"

        if Marg2_proximal.calcification and Marg2_ostium.calcification:
            return f"Presence d'une calcification ostio-proximale au niveau de la deuxième marginale"
        if Marg2_proximal.calcification and Marg2_distal.calcification:
            return f"Presence d'une calcification au niveau de la deuxième marginale"

    if len(segments) == 1:

        return f"Presence d'une calcification au niveau de {segments_mapping(target.segment_name)}"

    return f"Presence d'une calcification allant de {segments_mapping(segments[0].segment_name)} à {segments_mapping(segments[-1].segment_name)}"


def Marg_calcification_No_stenosis_generator(state: CoronarySegmentation):
    segments = Marg_segments_parser(state)
    lesions = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.stenosis == "0" and x.calcification == True,
    )
    print(lesions)
    report = (
        f"presence de {len(lesions)} calcification au niveau des artères marginales "
        if len(lesions) > 1
        else ""
    )

    for lesion in lesions:
        report += Marg_calcification_description(state, lesion)
        stent = [sgt for sgt in lesion if sgt.stent == True]
        if len(stent) > 0:
            report += " au niveau du site d'implantation d'un stent"
        report += " sans lesion angiographiquement significative sous-jacente"

    return report
