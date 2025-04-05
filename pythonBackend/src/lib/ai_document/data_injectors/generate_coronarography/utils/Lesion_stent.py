from typing import List

from src.lib.ai_document.utils.ai_document_classes import CoronarySegmentDescription


def stent_parser(segments: List[CoronarySegmentDescription]):

    count = sum(sgt.stent for sgt in segments)

    if count > 0:
        return " au niveau du site d'implantation d'un stent "
    return ""
