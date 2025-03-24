from pydantic import BaseModel
from typing import List, Literal, Optional

# List of property names from CoronarySegmentation
PropertyNames = Literal[
    "LM_proximal",
    "LM_medium",
    "LM_distal",
    "LAD1_ostium",
    "LAD1_proximal",
    "LAD1_distal",
    "LAD2_proximal",
    "LAD2_distal",
    "LAD3_proximal",
    "LAD3_distal",
    "Diag1_ostium",
    "Diag1",
    "Diag2_ostium",
    "Diag2",
    "Sept1",
    "Sept2",
    "Bisec_ostium",
    "Bisec_proximal",
    "Bisec_distal",
    "CX1_ostium",
    "CX1_proximal",
    "CX1_distal",
    "CX2_proximal",
    "CX2_distal",
    "CX3_proximal",
    "CX3_distal",
    "IVPL_ostium",
    "IVPL_proximal",
    "IVPL_distal",
    "Marg1_ostium",
    "Marg1_proximal",
    "Marg1_distal",
    "Marg2_ostium",
    "Marg2_proximal",
    "Marg2_distal",
    "CD1_ostium",
    "CD1_proximal",
    "CD1_distal",
    "CD2_proximal",
    "CD2_distal",
    "IVPR_ostium",
    "IVPR_proximal",
    "IVPR_distal",
    "RVG_ostium",
    "RVG_proximal",
    "RVG_distal",
    "MargR1",
    "MargR2",
]


class CoronarySegmentLesionDescription(BaseModel):
    stenosis: Literal["0", "<30", "30-50", "50", "50-70", "70-90", "90-99", "100"]
    parentOcclusion: bool
    thrombosis: bool
    calcification: bool
    stent: bool
    dissection: bool
    type_dissection: Optional[Literal["1", "2A", "2B", "3", "4"]] = None
    remark: Optional[str] = None
    TIMI_Flow: Optional[str] = None
    length: Optional[str] = None
    tortuosity: Optional[bool] = None
    Rantrop: Optional[str] = None
    Rantrop_collaterality: Optional[str] = None
    associated_segments: List[PropertyNames]  # Corrected to List[str]
    segment_name: Optional[PropertyNames] = None
    acute_occlusion: bool


class CoronarySegmentDescription(BaseModel):
    lesion: CoronarySegmentLesionDescription


class CoronarySegmentation(BaseModel):
    LM_proximal: CoronarySegmentDescription
    LM_medium: CoronarySegmentDescription
    LM_distal: CoronarySegmentDescription
    LAD1_ostium: CoronarySegmentDescription
    LAD1_proximal: CoronarySegmentDescription
    LAD1_distal: CoronarySegmentDescription
    LAD2_proximal: CoronarySegmentDescription
    LAD2_distal: CoronarySegmentDescription
    LAD3_proximal: CoronarySegmentDescription
    LAD3_distal: CoronarySegmentDescription
    Diag1_ostium: CoronarySegmentDescription
    Diag1: CoronarySegmentDescription
    Diag2_ostium: CoronarySegmentDescription
    Diag2: CoronarySegmentDescription
    Sept1: CoronarySegmentDescription
    Sept2: CoronarySegmentDescription
    Bisec_ostium: CoronarySegmentDescription
    Bisec_proximal: CoronarySegmentDescription
    Bisec_distal: CoronarySegmentDescription
    CX1_ostium: CoronarySegmentDescription
    CX1_proximal: CoronarySegmentDescription
    CX1_distal: CoronarySegmentDescription
    CX2_proximal: CoronarySegmentDescription
    CX2_distal: CoronarySegmentDescription
    CX3_proximal: CoronarySegmentDescription
    CX3_distal: CoronarySegmentDescription
    IVPL_ostium: CoronarySegmentDescription
    IVPL_proximal: CoronarySegmentDescription
    IVPL_distal: CoronarySegmentDescription
    Marg1_ostium: CoronarySegmentDescription
    Marg1_proximal: CoronarySegmentDescription
    Marg1_distal: CoronarySegmentDescription
    Marg2_ostium: CoronarySegmentDescription
    Marg2_proximal: CoronarySegmentDescription
    Marg2_distal: CoronarySegmentDescription
    CD1_ostium: CoronarySegmentDescription
    CD1_proximal: CoronarySegmentDescription
    CD1_distal: CoronarySegmentDescription
    CD2_proximal: CoronarySegmentDescription
    CD2_distal: CoronarySegmentDescription
    IVPR_ostium: CoronarySegmentDescription
    IVPR_proximal: CoronarySegmentDescription
    IVPR_distal: CoronarySegmentDescription
    RVG_ostium: CoronarySegmentDescription
    RVG_proximal: CoronarySegmentDescription
    RVG_distal: CoronarySegmentDescription
    MargR1: CoronarySegmentDescription
    MargR2: CoronarySegmentDescription


# The list of property names is now properly defined above as 'property_names'
# It's not needed within the class anymore, as it is a simple list of strings.


class AiChatMessage(BaseModel):
    type: Literal["user", "AI"]
    message: str
    id: str
    done: bool
    selected: bool


class ChatHistory(BaseModel):
    history: Optional[List[AiChatMessage]] = None
