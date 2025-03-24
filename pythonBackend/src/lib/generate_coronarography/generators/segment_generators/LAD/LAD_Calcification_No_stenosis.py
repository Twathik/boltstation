from typing import List
from src.lib.generate_coronarography.generators.segment_generators.LAD.LAD_segments import (
    LAD_segments_parser,
)
from src.lib.generate_coronarography.utils.coronarography_classes import (
    CoronarySegmentDescription,
    CoronarySegmentation,
)
from src.lib.generate_coronarography.utils.segment_description import (
    generic_condition_parser,
)
from src.lib.generate_coronarography.utils.segments_mapping import segments_mapping


def LAD_calcification_description(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):
    [
        LAD1_ostium,
        LAD1_proximal,
        LAD1_distal,
        LAD2_proximal,
        LAD2_distal,
        LAD3_proximal,
        LAD3_distal,
    ] = LAD_segments_parser(state)

    target = segments[0]

    if len(segments) == 3:
        if (
            LAD1_ostium.calcification
            and LAD1_proximal.calcification
            and LAD1_distal.calcification
        ):

            return f"Presence d'une calcification diffuses au niveau de l'interventriculaire antérieure ostio-proximale"

    if len(segments) == 2:
        if LAD1_proximal.calcification and LAD1_ostium.calcification:
            return f"Presence d'une calcification au niveau de l'interventriculaire antérieure ostio-proximale"
        if LAD1_proximal.calcification and LAD1_distal.calcification:
            return f"Presence d'une calcification au niveau de l'interventriculaire antérieure proximale"
        if LAD2_proximal.calcification and LAD2_distal.calcification:
            return f"Presence d'une calcification au niveau de l'interventriculaire antérieure moyenne"
        if LAD3_proximal.calcification and LAD3_distal.calcification:
            return f"Presence d'une calcification au niveau de l'interventriculaire antérieure distale"
    if len(segments) == 1:

        return f"Presence d'une calcification au niveau de {segments_mapping(target.segment_name)}"

    return f"Presence d'une calcification allant de {segments_mapping(segments[0].segment_name)} à {segments_mapping(segments[-1].segment_name)}"


def LAD_calcification_children_parser(
    state: CoronarySegmentation, segments: List[CoronarySegmentDescription]
):

    bifurcations: List[str] = []

    for sgt in segments:
        if sgt.segment_name == "LAD1_distal" and state.Sept1.lesion.calcification:
            bifurcations.append(segments_mapping("Sept1"))
        if (
            sgt.segment_name == "LAD2_proximal"
            and state.Diag1_ostium.lesion.calcification
        ):
            bifurcations.append(segments_mapping("Diag1_ostium"))
        if (
            sgt.segment_name == "LAD2_distal"
            and state.Diag2_ostium.lesion.calcification
        ):
            bifurcations.append(segments_mapping("Diag2_ostium"))
        if sgt.segment_name == "LAD2_distal" and state.Sept2.lesion.calcification:
            bifurcations.append(segments_mapping("Sept2"))
    if len(bifurcations) == 0:
        return ""
    if len(bifurcations) == 1:
        return f", prenant l{bifurcations[0]}"
    else:
        return f", prenant {', '.join(bifurcations)}"


def LAD_calcification_No_stenosis_generator(state: CoronarySegmentation):
    segments = LAD_segments_parser(state)
    lesions = generic_condition_parser(
        segments=segments,
        condition=lambda x: x.stenosis == "0" and x.calcification == True,
    )
    print(lesions)
    report = (
        f"presence de {len(lesions)} calcification au niveau de l'interventriculaire anterieure. "
        if len(lesions) > 1
        else ""
    )

    for lesion in lesions:
        report += LAD_calcification_description(state, lesion)
        report += LAD_calcification_children_parser(state, lesion)
        stent = [sgt for sgt in lesion if sgt.stent == True]
        if len(stent) > 0:
            report += " au niveau du site d'implantation d'un stent"
        report += " sans lesion angiographiquement significative sous-jacente"

    return report
