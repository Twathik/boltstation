from typing import List
from src.lib.generate_coronarography.utils.coronarography_classes import (
    CoronarySegmentDescription,
    CoronarySegmentLesionDescription,
)


def anomalies_calculator(segment: CoronarySegmentLesionDescription):

    return (
        (not segment.stenosis == "0")
        + (not segment.TIMI_Flow == None)
        + (segment.thrombosis)
        + (segment.tortuosity)
        + (segment.stent)
        + (segment.calcification)
        + (segment.dissection)
    )


def hole_segment_anomalie_calculator(segments: List[CoronarySegmentDescription]):

    return sum(anomalies_calculator(segt) for segt in segments)


def stenotic_anomalies_calculator(segments: List[CoronarySegmentDescription]):
    return sum(
        not segt.stenosis == "0" and not segt.stenosis == "100" for segt in segments
    )


def stenotic_with_occlusion_anomalies_calculator(
    segments: List[CoronarySegmentDescription],
):
    return sum(not segt.stenosis == "0" for segt in segments)


def total_occlusion_calculator(segments: List[CoronarySegmentDescription]):
    return sum(
        segt.stenosis == "100" and segt.parentOcclusion == False for segt in segments
    )
