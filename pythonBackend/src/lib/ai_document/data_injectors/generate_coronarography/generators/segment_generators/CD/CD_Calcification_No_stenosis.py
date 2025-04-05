from typing import List

from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.CD.CD_segments import (
    CD_segments_parser,
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


def CD_calcification_description(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):
    [
        CD1_ostium,
        CD1_proximal,
        CD1_distal,
        CD2_proximal,
        CD2_distal,
    ] = CD_segments_parser(state)

    target = segments[0]

    if len(segments) == 3:
        if (
            CD1_ostium.calcification
            and CD1_proximal.calcification
            and CD1_distal.calcification
        ):

            return f"Presence d'une calcification diffuses au niveau de la coronaire droite proximale"

    if len(segments) == 2:
        if CD1_proximal.calcification and CD1_ostium.calcification:
            return f"Presence d'une calcification au niveau de la coronaire droite ostio-proximale"
        if CD1_proximal.calcification and CD1_distal.calcification:
            return f"Presence d'une calcification au niveau de la coronaire droite proximale"
        if CD2_proximal.calcification and CD2_distal.calcification:
            return (
                f"Presence d'une calcification au niveau de la coronaire droite moyenne"
            )

    if len(segments) == 1:

        return f"Presence d'une calcification au niveau de {segments_mapping(target.segment_name)}"

    return f"Presence d'une calcification allant de {segments_mapping(segments[0].segment_name)} à {segments_mapping(segments[-1].segment_name)}"


def CD_calcification_children_parser(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):

    bifurcations: List[str] = []

    for sgt in segments:
        if (
            sgt.segment_name == "CD1_proximal"
            and not state.MargR1.lesion.calcification == "0"
        ):
            bifurcations.append(segments_mapping("MargR1"))
        if (
            sgt.segment_name == "CD1_distal"
            and not state.MargR2.lesion.calcification == "0"
        ):
            bifurcations.append(segments_mapping("MargR2"))
        if (
            sgt.segment_name == "CD2_distal"
            and not state.IVPR_ostium.lesion.calcification == "0"
        ):
            bifurcations.append(segments_mapping("IVPR_ostium"))
        if (
            sgt.segment_name == "CD2_distal"
            and not state.RVG_ostium.lesion.calcification == "0"
        ):
            bifurcations.append(segments_mapping("RVG_ostium"))

    if len(bifurcations) == 0:
        return ""
    if len(bifurcations) == 1:
        return f", prenant l{bifurcations[0]}"
    else:
        return f", prenant {', '.join(bifurcations)}"


def CD_calcification_No_stenosis_generator(state: CoronarySegmentation):
    segments = CD_segments_parser(state)
    lesions = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.stenosis == "0" and x.calcification == True,
    )

    report = (
        f"presence de {len(lesions)} calcification au niveau de la coronaire droite. "
        if len(lesions) > 1
        else ""
    )

    for lesion in lesions:
        report += CD_calcification_description(state, lesion)
        report += CD_calcification_children_parser(state, lesion)
        stent = [sgt for sgt in lesion if sgt.stent == True]
        if len(stent) > 0:
            report += " au niveau du site d'implantation d'un stent"
        report += " sans lesion angiographiquement significative sous-jacente"

    return report
