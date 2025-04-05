from typing import List

import pydash

from src.lib.ai_document.data_injectors.generate_coronarography.utils import (
    coronary_tree,
)
from src.lib.ai_document.data_injectors.generate_coronarography.utils.coronary_tree import (
    CoronaryTree,
)
from src.lib.ai_document.data_injectors.generate_coronarography.utils.segments_mapping import (
    segments_mapping,
)
from src.lib.ai_document.utils.ai_document_classes import (
    SEGMENT_NAMES,
    CoronarySegmentDescription,
    CoronarySegmentation,
)


def total_occlusion_parser(occluded_segments: list[CoronarySegmentDescription]):

    if len(occluded_segments) == 0:
        return ""

    return f" Présence d'une occlusion totale au niveau {','.join([segments_mapping(sgt.segment_name) + f"{" (aiguë)" if sgt.acute_occlusion else ""}" for sgt in occluded_segments])}"


def find_rantrop_location_in_tree(
    state: CoronarySegmentation,
    tree: CoronaryTree,
    collaterality: List[CoronarySegmentDescription],
):

    for child in tree.children:
        segment = getattr(state, child.main)
        if segment.lesion.stenosis != "100" and segment.lesion.parentOcclusion == False:
            collaterality.append(segment)
        else:
            # Recursively check all children
            find_rantrop_location_in_tree(state, child, collaterality)


def find_rantrop_location(
    state: CoronarySegmentation,
    property_name: SEGMENT_NAMES,
    coronary_tree: List[CoronaryTree],
    collaterality: List[CoronarySegmentDescription],
):

    # First, check if the current tree node matches the given property name and conditions
    for tree in coronary_tree:
        if tree.main == property_name:
            # Traverse the children
            find_rantrop_location_in_tree(state, tree, collaterality)
        else:

            find_rantrop_location(state, property_name, tree.children, collaterality)


def rantrop_parser(
    state: CoronarySegmentation, occluded_segments: list[CoronarySegmentDescription]
) -> str:

    if len(occluded_segments) == 0:
        return ""

    collaterality: List[CoronarySegmentDescription] = []
    for occluded in occluded_segments:
        find_rantrop_location(
            state, occluded.segment_name, coronary_tree, collaterality
        )

    collaterality = pydash.uniq_by(collaterality, "segment_name")

    grouped = pydash.group_by(
        collaterality, lambda item: (item.Rantrop, item.Rantrop_collaterality)
    )

    report = ""
    for group_key, group_items in grouped.items():

        report += f' Il existe une reprise {f"{group_key[1]}e" if not group_key[1] == None else ""}{f" de type Rantrop {group_key[0]}" if not group_key[0] == None else ""} au niveau {','.join([segments_mapping(sgt.segment_name) for sgt in group_items])}.'

    return report
