from src.lib.ai_document.utils.ai_document_classes import CoronarySegmentation


def LM_segments_parser(state: CoronarySegmentation):

    LM_proximal = state.LM_proximal.lesion
    LM_medium = state.LM_medium.lesion
    LM_distal = state.LM_distal.lesion

    return [
        LM_proximal,
        LM_medium,
        LM_distal,
    ]


def LM_segments_children_parser(state: CoronarySegmentation):

    LAD1_ostium = state.LAD1_ostium.lesion
    Bisec_ostium = state.Bisec_ostium.lesion
    CX1_ostium = state.CX1_ostium.lesion

    return [
        LAD1_ostium,
        Bisec_ostium,
        CX1_ostium,
    ]
