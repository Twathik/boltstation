from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.LM.LM_segments import (
    LM_segments_children_parser,
    LM_segments_parser,
)
from src.lib.ai_document.utils.ai_document_classes import (
    CoronarySegmentDescription,
    CoronarySegmentation,
)


def inject_dissectionType(segment: CoronarySegmentDescription):
    return (
        f" de type {segment.type_dissection}"
        if not segment.type_dissection == None
        else ""
    )


def LM_dissection_main_parser(state: CoronarySegmentation) -> str:

    segments = LM_segments_parser(state=state)

    count = sum(sgt.dissection for sgt in segments)

    LM_proximal, LM_median, LM_distal = segments

    if count > 0:
        if count == 3:
            if (
                LM_proximal.type_dissection == None
                and LM_median.type_dissection == None
                and LM_distal.type_dissection == None
            ):
                return " Il exist une dissection prenant l'ensemble du tronc commun gauche."

            if (
                LM_proximal.type_dissection == LM_median.type_dissection
                and LM_proximal.type_dissection == LM_distal.type_dissection
            ):
                return f" Il existe une dissection{inject_dissectionType(LM_proximal)} prenant l'ensemble du tronc commun gauche."
            if LM_proximal.type_dissection == LM_median.type_dissection:
                return f" Il existe une dissection{inject_dissectionType(LM_proximal)} au niveau tu tronc commun gauche ostio-proximo-median, et {inject_dissectionType(LM_distal)} dans son segment distal."
            if LM_median.type_dissection == LM_distal.type_dissection:
                return f" Il existe une dissection {inject_dissectionType(LM_proximal)} au niveau tu tronc commun gauche ostio-proximal, et{inject_dissectionType(LM_distal)} dans son segment medio-distal."
            return f" Il existe une dissection{inject_dissectionType(LM_proximal)} au niveau tu tronc commun gauche ostio-proximal, {inject_dissectionType(LM_median)} dans son segment median et{inject_dissectionType(LM_distal)} dans son segment distal."

        if count == 2:
            if LM_proximal.dissection and LM_median.type_dissection:
                if LM_proximal.type_dissection == LM_median.type_dissection:
                    return f" Il existe une dissection{inject_dissectionType(LM_proximal)} au niveau tu tronc commun gauche ostio-proximo-median."
                return f" Il existe une dissection{inject_dissectionType(LM_proximal)} au niveau tu tronc commun gauche ostio-proximal, et{inject_dissectionType(LM_median)} au niveau median."
            if LM_median.dissection and LM_distal.dissection:
                if LM_median.type_dissection == LM_distal.type_dissection:
                    return f" Il existe une dissection{inject_dissectionType(LM_median)} au niveau tu tronc commun gauche medio-distal."
                return f" Il existe une dissection{inject_dissectionType(LM_median)} au niveau tu tronc commun gauche median et{inject_dissectionType(LM_distal)} au niveau distal."
            return f" Il existe une dissection{inject_dissectionType(LM_proximal)} au niveau tu tronc commun gauche ostio-proximal et{inject_dissectionType(LM_distal)} dans son segment distal."
        if count == 1:
            if LM_proximal.dissection == True:
                return f" Il existe une dissection{inject_dissectionType(LM_proximal)} au niveau tu tronc commun gauche ostio-proximal."
            if LM_median.dissection == True:
                return f" Il existe une dissection{inject_dissectionType(LM_median)} au niveau tu tronc commun gauche median."
            if LM_distal.dissection == True:
                return f" Il existe une dissection{inject_dissectionType(LM_proximal)} au niveau tu tronc commun gauche distal. "

        return ""
    return ""


def LM_dissection_children_parser(state: CoronarySegmentation) -> str:

    segments = LM_segments_children_parser(state=state)
    LAD, Bisec, Cx = segments
    LM_distal = state.LM_distal.lesion

    count = sum(sgt.dissection for sgt in segments)
    dissections = []
    if LAD.dissection:
        dissections.append("l'interventriculaire anterieur proximale")
    if Bisec.dissection:
        dissections.append("la bisectrice")
    if Cx.dissection:
        dissections.append(
            f"{"ainsi que celui de" if count > 1 else ''}l'artère circonflexe"
        )
    if count > 0 and LM_distal.dissection:
        if count == 3:
            return "Cette dissection s’étend vers les ostiums de l'interventriculaire antérieur proximale, la bissectrice ainsi que l'artère circonflexe."
        if count == 2:
            return (
                f"Cette dissection s’étend vers les ostiums de {','.join(dissections)}."
            )
        if count == 1:
            return f"Cette dissection s’étend vers les ostium de {dissections[0]}."
        pass
    return ""


def LM_dissection_generator(state: CoronarySegmentation) -> str:
    return f"{LM_dissection_main_parser(state)}.{LM_dissection_children_parser(state)}"
