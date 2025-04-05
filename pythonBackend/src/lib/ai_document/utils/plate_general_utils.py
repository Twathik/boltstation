import json
from typing import Any, List, Literal, Optional

from ulid import ULID

from src.lib.ai_document.data_injectors.generate_coronarography.utils.coronary_tree import (
    coronary_tree,
)
from src.lib.ai_document.utils.ai_document_classes import (
    MAIN_ARTERIES,
    MAIN_SEGMENTS,
    CoronarySegmentation,
    FFRSegmentModel,
    IVUSSegmentModel,
    OCTSegmentModel,
)
from src.lib.ai_document.data_injectors.generate_coronarography.utils.coronary_tree import (
    CoronaryTree,
)


def replace_none(string: str) -> str:
    return string if not str(string) == "None" else ""


def generate_simple_list_element(
    text: List[Any], chunk: Any, indent: Optional[int] = None
) -> Any:
    return {
        "AiTarget": chunk["AiTarget"],
        "children": text,
        "type": "p",
        "id": str(ULID()),
        "indent": indent,
        "listStyleType": "disc",
        "widgetId": chunk["widgetId"],
        "widgetName": chunk["widgetName"],
        "injected": True,
    }


def append_generated_text(
    document: List[Any],
    chunk: Any,
    extracted_data: List[str],
    text: List[any],
    indent: Optional[int] = 1,
):
    document.append(generate_simple_list_element(chunk=chunk, text=text, indent=indent))
    extracted_data.append(extract_text_from_children(text))


def extract_text_from_children(children: Any) -> str:
    text = ""
    for child in children:
        if "text" in child:
            text += child["text"]

    return text


def append_title(
    document: List[Any],
    chunk: Any,
    extracted_data: List[str],
    type: Literal["h1", "h2", "h3"],
    text: List[any],
):
    document.append(
        {
            "AiTarget": chunk["AiTarget"],
            "type": type,
            "children": text,
            "id": str(ULID()),
            "widgetId": chunk["widgetId"],
            "widgetName": chunk["widgetName"],
            "injected": True,
        }
    )
    extracted_data.append("###" + extract_text_from_children(text))


def has_ivus(segmentation: CoronarySegmentation) -> bool:
    return any(
        getattr(segmentation, field).IVUS is not None
        for field in segmentation.model_fields
    )


def has_oct(segmentation: CoronarySegmentation) -> bool:
    return any(
        getattr(segmentation, field).OCT is not None
        for field in segmentation.model_fields
    )


def has_ffr(segmentation: CoronarySegmentation) -> bool:
    return any(
        getattr(segmentation, field).FFR is not None
        for field in segmentation.model_fields
    )


def extract_ivus_segments(
    coronary_segmentation: CoronarySegmentation,
) -> List[IVUSSegmentModel]:

    return [
        IVUSSegmentModel(segment_name=name, description=segment.IVUS)
        for name, segment in coronary_segmentation.__dict__.items()
        if segment.IVUS is not None
    ]


def extract_OCT_segments(
    coronary_segmentation: CoronarySegmentation,
) -> List[OCTSegmentModel]:

    return [
        OCTSegmentModel(segment_name=name, description=segment.OCT)
        for name, segment in coronary_segmentation.__dict__.items()
        if segment.OCT is not None
    ]


def extract_FFR_segments(
    coronary_segmentation: CoronarySegmentation,
) -> List[FFRSegmentModel]:

    return [
        FFRSegmentModel(segment_name=name, description=segment.FFR)
        for name, segment in coronary_segmentation.__dict__.items()
        if segment.FFR is not None
    ]


def get_PCI_material_name(material: Any) -> str:

    description = (
        json.loads(getattr(material, "productDetails", ""))
        if not getattr(material, "productDetails", "") == None
        else None
    )
    description_report = ""
    if not description == None:
        description_report = f"{f"{description.get('Description', '') if not description.get('Description', '') == None else ""} {f"diamètre {description.get('Diametre', '')} mm" if not description.get('Diametre', '') == None and len(description.get('Diametre', '')) > 0  else ""} {f"longueur {description.get('Longueur', '')} mm" if not description.get('Longueur', '') == None and len(description.get('Longueur', '')) >0  else ""}" if not description == None else ""}"
    report = (
        f"{getattr(material, 'productName', '')} "
        f"{description_report}"
        f"{f'longueur {getattr(material, "Longueur", "")} mm' if getattr(material, 'Longueur', None) is not None else ''} "
        f"{f'diamètre {getattr(material, "Diametre", "")} mm' if getattr(material, 'Diametre', None) is not None else ''}"
    )

    return report


def get_PCI_step_main_segment(segment: MAIN_SEGMENTS) -> str:
    match segment:
        case "Cx":
            return "artère circonflexe"
        case "Diag1":
            return "première diagonale"
        case "Diag2":
            return "deuxième diagonale"
        case "IVPL":
            return "interventriculaire postérieure gauche"
        case "IVPR":
            return "interventriculaire postérieure droite"
        case "LAD":
            return "interventriculaire antérieure"
        case "Marg1":
            return "première marginale"
        case "Marg2":
            return "deuxième marginale"
        case "RVG":
            return "retro ventriculaire postérieure"
        case _:
            return ""


def get_PCI_step_main_artery(segment: MAIN_ARTERIES) -> str:
    match segment:
        case "CD":
            return "coronaire droite"
        case "Cx":
            return "artère circonflexe"
        case "LAD":
            return "interventriculaire antérieure"
        case "LM":
            return "tronc commun gauche"
        case _:
            return ""


# Function to check for a segment in the tree
def check_for_segment(
    tree: CoronaryTree, sgt_to_find: List[str]
) -> Optional[CoronaryTree]:
    if tree.main in sgt_to_find:
        return tree
    for leaf in tree.children:
        check = check_for_segment(leaf, sgt_to_find)
        if check is not None:
            return check
    return None


# Function to group segments
def group_segments(
    end_of_lesion: List[str], tree: CoronaryTree, segments: List[str], index: int = 0
) -> None:
    if tree.main in segments:

        while len(end_of_lesion) <= index:
            end_of_lesion.append("")

        end_of_lesion[index] = tree.main

    for leaf_index, leaf in enumerate(tree.children):
        if leaf.main in segments:
            if leaf.tree_type == "main":
                group_segments(end_of_lesion, leaf, segments, index)
            else:
                group_segments(end_of_lesion, leaf, segments, len(end_of_lesion))


def get_segment_title(segment: str) -> str:
    titles = {
        "Bisec_distal": "Bisectrice distale",
        "Bisec_ostium": "Ostium de la bisectrice",
        "Bisec_proximal": "Bisectrice proximale",
        "CD1_distal": "CD1 distale",
        "CD1_ostium": "Ostium de la CD1",
        "CD1_proximal": "CD1 proximale",
        "CD2_distal": "CD2 distale",
        "CD2_proximal": "CD2 proximale",
        "CX1_distal": "CX1 distale",
        "CX1_ostium": "Ostium de la CX1",
        "CX1_proximal": "CX1 proximale",
        "CX2_distal": "CX2 distale",
        "CX2_proximal": "CX2 proximale",
        "CX3_distal": "CX3 distale",
        "CX3_proximal": "CX3 proximale",
        "Diag1": "1er diagonale",
        "Diag1_ostium": "Ostium de la 1er diagonale",
        "Diag2": "2em diagonale",
        "Diag2_ostium": "Ostium de la 2em diagonale",
        "IVPL_distal": "IVP gauche distale",
        "IVPL_ostium": "Ostium de l'IVP gauche",
        "IVPL_proximal": "IVP gauche proximale",
        "IVPR_distal": "IVP droite distale",
        "IVPR_ostium": "Ostium de l'IVP droite",
        "IVPR_proximal": "IVP droite proximale",
        "LAD1_distal": "IVA1 distale",
        "LAD1_ostium": "Ostium de l'IVA1",
        "LAD1_proximal": "IVA1 proximale",
        "LAD2_distal": "IVA2 distale",
        "LAD2_proximal": "IVA2 proximale",
        "LAD3_distal": "IVA3 distale",
        "LAD3_proximal": "IVA3 proximale",
        "LM_distal": "TCG distal",
        "LM_medium": "TCG moyen",
        "LM_proximal": "TCG proximal",
        "Marg1_distal": "1er marginale distale",
        "Marg1_ostium": "Ostium de la 1er marginale",
        "Marg1_proximal": "1er marginale proximale",
        "Marg2_distal": "2em marginale distale",
        "Marg2_ostium": "Ostium de la 2em marginale",
        "Marg2_proximal": "2em marginale proximale",
        "MargR1": "1er marginale du bord droit",
        "MargR2": "2em marginale du bord droit",
        "RVG_distal": "RVG distale",
        "RVG_ostium": "Ostium de la RVG",
        "RVG_proximal": "RVG proximale",
        "Sept1": "1er septale",
        "Sept2": "2em septale",
    }
    return titles.get(segment, "")


# Function to get lesion localization
def get_lesion_localisation(segments: List[str]) -> str:
    if not segments:
        return ""

    first_segment_tree: Optional[CoronaryTree] = None

    # Find the first matching segment in the tree
    for tree in coronary_tree:
        check = check_for_segment(tree, segments)
        if check:
            first_segment_tree = check
            break

    end_of_lesion: List[str] = [""]
    if first_segment_tree:
        group_segments(end_of_lesion, first_segment_tree, segments)
        end_of_lesion = [e for e in end_of_lesion if e != first_segment_tree.main]

        if len(end_of_lesion) == 0:
            return get_segment_title(first_segment_tree.main)
        elif len(end_of_lesion) == 1:
            return f"{get_segment_title(first_segment_tree.main)} -> {get_segment_title(end_of_lesion[0])}"
        else:

            return f"{get_segment_title(first_segment_tree.main)} -> {' - '.join(get_segment_title(e) for e in end_of_lesion)}"
    else:
        raise ValueError("unknown segment")
