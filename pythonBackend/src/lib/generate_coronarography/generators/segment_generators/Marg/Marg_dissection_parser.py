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
    inject_dissectionType,
)
from src.lib.generate_coronarography.utils.segments_mapping import segments_mapping


def Marg_dissection_description(
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
            Marg1_ostium.dissection
            and Marg1_proximal.dissection
            and Marg1_distal.dissection
        ):

            return f"Dissection diffuse {inject_dissectionType(target)} au niveau de la première marginale"
        if (
            Marg2_ostium.dissection
            and Marg2_proximal.dissection
            and Marg2_distal.dissection
        ):

            return f"Dissection diffuse {inject_dissectionType(target)} au niveau de la deuxième marginale"

    if len(segments) == 2:
        if Marg1_proximal.dissection and Marg1_ostium.dissection:
            return f"Dissection{inject_dissectionType(target)} au niveau de la première marginale ostio-proximale"
        if Marg1_proximal.dissection and Marg1_distal.dissection:
            return f"Dissection{inject_dissectionType(target)} au niveau de la première marginale"
        if Marg2_proximal.dissection and Marg2_ostium.dissection:
            return f"Dissection{inject_dissectionType(target)} au niveau de la deuxième marginale ostio-proximale"
        if Marg2_proximal.dissection and Marg2_distal.dissection:
            return f"Dissection{inject_dissectionType(target)} au niveau de la deuxième marginale"

    if len(segments) == 1:

        return f"Dissection{inject_dissectionType(target)} au niveau de {segments_mapping(target.segment_name)}"

    return f"Dissection{inject_dissectionType(target)} allant de {segments_mapping(segments[0].segment_name)} à {segments_mapping(segments[-1].segment_name)}"


def Marg_dissection_generator(state: CoronarySegmentation):
    segments = Marg_segments_parser(state)

    dissections = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.dissection == True,
    )

    report = (
        f"presence de {len(dissections)} dissections au niveau des marginales. "
        if len(dissections) > 1
        else ""
    )

    for dissection in dissections:
        report += Marg_dissection_description(state, dissection)

    return report
