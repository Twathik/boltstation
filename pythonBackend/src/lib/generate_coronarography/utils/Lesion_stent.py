from typing import List
from src.lib.generate_coronarography.generators.segment_generators.LM.LM_segments import (
    LM_segments_parser,
)
from src.lib.generate_coronarography.utils.coronarography_classes import (
    CoronarySegmentDescription,
)


def stent_parser(segments: List[CoronarySegmentDescription]):

    count = sum(sgt.stent for sgt in segments)

    if count > 0:
        return " au niveau du site d'implantation d'un stent "
    return ""
