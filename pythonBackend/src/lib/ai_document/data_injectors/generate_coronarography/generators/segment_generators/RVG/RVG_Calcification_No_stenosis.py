from typing import List

from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.RVG.RVG_segments import (
    RVG_segments_parser,
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


def RVG_calcification_description(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):
    [
        RVG_ostium,
        RVG_proximal,
        RVG_distal,
    ] = RVG_segments_parser(state)

    target = segments[0]

    if len(segments) == 3:
        if (
            RVG_ostium.calcification
            and RVG_proximal.calcification
            and RVG_distal.calcification
        ):

            return f"Presence d'une calcification diffuses au niveau de la rétro ventriculaire gauche dès son ostium"

    if len(segments) == 2:
        if RVG_proximal.calcification and RVG_ostium.calcification:
            return f"Presence d'une calcification ostio-proximale au niveau de la rétro ventriculaire gauche"
        if RVG_proximal.calcification and RVG_distal.calcification:
            return f"Presence d'une calcification au niveau de la rétro ventriculaire gauche"

    if len(segments) == 1:

        return f"Presence d'une calcification au niveau de {segments_mapping(target.segment_name)}"

    return f"Presence d'une calcification allant de {segments_mapping(segments[0].segment_name)} à {segments_mapping(segments[-1].segment_name)}"


def RVG_calcification_No_stenosis_generator(state: CoronarySegmentation):
    segments = RVG_segments_parser(state)
    lesions = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.stenosis == "0" and x.calcification == True,
    )

    report = (
        f"presence de {len(lesions)} calcification au niveau de la rétro ventriculaire gauche. "
        if len(lesions) > 1
        else ""
    )

    for lesion in lesions:
        report += RVG_calcification_description(state, lesion)
        stent = [sgt for sgt in lesion if sgt.stent == True]
        if len(stent) > 0:
            report += " au niveau du site d'implantation d'un stent"
        report += " sans lesion angiographiquement significative sous-jacente"

    return report
