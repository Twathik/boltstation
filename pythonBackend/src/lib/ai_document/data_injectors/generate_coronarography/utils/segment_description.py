from typing import Callable, List

from src.lib.ai_document.utils.ai_document_classes import CoronarySegmentDescription


def segment_description(segment: CoronarySegmentDescription):

    f"sténose de {segment.stenosis} % {"tortueuse" if segment.tortuosity == True else ''}{"d'une longeur estimée à " + segment.length if not segment.length == None else ''}{", siège d'une thrombose" if segment.thrombosis == True else ''}{", calcifiée" if segment.calcification== True else ''}{", au niveau du siege d'implantation d'un stent" if segment.stent == True else ''}{", flux " + segment.TIMI_Flow  if not segment.TIMI_Flow == None else ''}{", nous notons la présence d'une reprise " + segment.Rantrop_collaterality  if not segment.Rantrop_collaterality == None else ''}{"Rantrop : " + segment.Rantrop  if not segment.Rantrop == None else ''}"


def lesion_description(segment: CoronarySegmentDescription):
    return f"{" la sténose est tortueuse" if segment.tortuosity == True else ''}{" d'une longeure estimée à " + segment.length if not segment.length == None else ''}{", cette sténose est calcifiée" if segment.calcification== True else ''}{", siège d'une thrombose" if segment.thrombosis == True else ''}{",siege d'un flux " + segment.TIMI_Flow  if not segment.TIMI_Flow == None else ''}"


def inject_dissectionType(segment: CoronarySegmentDescription):
    return (
        f" de type {segment.type_dissection}"
        if not segment.type_dissection == None
        else ""
    )


def generic_condition_parser(
    segments: List[CoronarySegmentDescription],
    condition: Callable[[CoronarySegmentDescription], bool],
):

    sequence: List[List[CoronarySegmentDescription]] = []
    index = -1
    current_state: bool = False

    for sgt in segments:
        if condition(sgt):
            if not condition(sgt) == current_state:
                index += 1
                current_state = condition(sgt)
                sequence.append([])
            sequence[index].append(sgt)
        else:
            if len(sequence) > 0:
                index += 1
                current_state = False
                sequence.append([])

    return [arr for arr in sequence if arr]


def get_remarks(segments: List[CoronarySegmentDescription]) -> str:
    return """, """.join([sgt.remark for sgt in segments if not sgt.remark == None])
