from typing import Annotated, List, Literal, Optional, Union

from pydantic import BaseModel, Field, RootModel, StringConstraints, constr


class NumberInputDescription(BaseModel):
    input_name: str
    input_description: str
    input_value: Optional[float] = None


class NumberInputsCheckerResponse(BaseModel):
    check: bool
    number_inputs: List[NumberInputDescription]


class FilteredData(BaseModel):
    value: Optional[float] = None
    sentence: Optional[str] = ""


class ExtractedData(BaseModel):
    input_name: str
    data: FilteredData


TimeStr = Annotated[
    str, StringConstraints(pattern=r"^([01][0-9]|2[0-3]):([0-5][0-9])$")
]


class ProcedureDetails(BaseModel):
    startTime: TimeStr
    endTime: Optional[TimeStr] = None
    anesthesia: Optional[Literal["None", "générale", "locale"]] = None
    rayDuration: Optional[float] = None
    graphyDuration: Optional[float] = None
    procedureDuration: Optional[float] = None
    rayDose: Optional[float] = None
    contrastDose: Optional[float] = None
    clairance: Optional[float] = None

    primaryShift: Optional[
        Literal[
            "fémorale droite",
            "radiale droite",
            "fémorale gauche",
            "radiale gauche",
            "humérale",
            "cubitale",
        ]
    ] = None
    primaryShiftSize: Optional[Literal["None", "5F", "6F", "7F", "8F", "other"]] = None
    primaryFailure: Optional[bool] = None
    primaryClosureFailure: Optional[bool] = None

    secondaryShift: Optional[
        Literal[
            "None",
            "fémorale droite",
            "radiale droite",
            "fémorale gauche",
            "radiale gauche",
            "humérale",
            "cubitale",
        ]
    ] = None
    secondaryShiftSize: Optional[Literal["None", "5F", "6F", "7F", "8F", "other"]] = (
        None
    )
    secondaryFailure: Optional[bool] = None
    secondaryClosureFailure: Optional[bool] = None

    tertiaryShift: Optional[
        Literal[
            "None",
            "fémorale droite",
            "radiale droite",
            "fémorale gauche",
            "radiale gauche",
            "humérale",
            "cubitale",
        ]
    ] = None
    tertiaryShiftSize: Optional[Literal["None", "5F", "6F", "7F", "8F", "other"]] = None
    tertiaryFailure: Optional[bool] = None
    tertiaryClosureFailure: Optional[bool] = None

    venousPrimaryShift: Optional[
        Literal[
            "None",
            "fémorale droite",
            "fémorale gauche",
            "sous clavière droite",
            "axillaire droite",
            "axillaire gauche",
        ]
    ] = None
    venousPrimaryShiftSize: Optional[
        Literal["None", "5F", "6F", "7F", "8F", "other"]
    ] = None
    venousPrimaryFailure: Optional[bool] = None
    venousPrimaryClosureFailure: Optional[bool] = None

    venousSecondaryShift: Optional[
        Literal[
            "None",
            "fémorale droite",
            "fémorale gauche",
            "sous clavière droite",
            "axillaire droite",
            "axillaire gauche",
        ]
    ] = None
    venousSecondaryShiftSize: Optional[
        Literal["None", "5F", "6F", "7F", "8F", "other"]
    ] = None
    venousSecondaryFailure: Optional[bool] = None
    venousSecondaryClosureFailure: Optional[bool] = None

    venousTertiaryShift: Optional[
        Literal[
            "None",
            "fémorale droite",
            "fémorale gauche",
            "sous clavière droite",
            "axillaire droite",
            "axillaire gauche",
        ]
    ] = None
    venousTertiaryShiftSize: Optional[
        Literal["None", "5F", "6F", "7F", "8F", "other"]
    ] = None
    venousTertiaryFailure: Optional[bool] = None
    venousTertiaryClosureFailure: Optional[bool] = None

    circulatorySupport: Optional[
        Literal[
            "None",
            "IABP",
            "LVAD",
            "RVDA",
            "BiVAD",
            "VA ECMO",
            "VV ECMO",
            "Impella",
        ]
    ] = None


class CoronarographyClinicalContext(BaseModel):
    weight: Optional[int] = None
    length: Optional[int] = None
    BMI: Optional[int] = None
    history: str
    clinical_exam: str
    diagnostic: str
    electric: str
    ischemicTest: str


class GeneralAnatomySchema(BaseModel):
    dominance: Literal["codominance", "gauche", "droite"]
    presentBissec: bool
    SizeLM: Literal["normal", "cannon de fusile", "court", "long"]
    OrigineLM: Optional[Literal["None", "sinus Valsalva droit", "CD", "autre"]] = None

    rudimentaryRCD: bool
    OrigineRCD: Optional[
        Literal[
            "None",
            "sinus Valsalva gauche",
            "Tronc commun gauche",
            "autre",
        ]
    ] = None
    fistuleRCD: bool

    OrigineLAD: Optional[
        Literal["None", "sinus Valsalva droit", "sinus Valsalva gauche", "CD", "autre"]
    ] = None
    fistuleLAD: bool
    intraMyocardiqueTrajectoryLAD: bool

    OrigineCx: Optional[
        Literal["None", "sinus Valsalva droit", "sinus Valsalva gauche", "CD", "autre"]
    ] = None
    fistuleCx: bool


SEGMENT_NAMES = Literal[
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


class CoronaryLesionDescription(BaseModel):
    stenosis: Literal["0", "<30", "30-50", "50", "50-70", "70-90", "90-99", "100"]
    remark: Optional[str] = None
    TIMI_Flow: Optional[Literal["None", "TIMI 0", "TIMI 1", "TIMI 2", "TIMI 3"]] = None
    length: Optional[Literal["None", "< 10 mm", "10 - 20 mm", "> 20 mm"]] = None
    tortuosity: bool
    Rantrop: Optional[Literal["None", "I", "II", "III"]] = None
    Rantrop_collaterality: Optional[
        Literal["None", "homolateral", "controlateral", "bilateral"]
    ] = None
    dissection: bool
    type_dissection: Optional[Literal["None", "1", "2A", "2B", "3", "4"]] = None
    parentOcclusion: bool
    acute_occlusion: bool
    thrombosis: bool
    stent: bool
    calcification: bool
    bifurcation: Optional[Literal["None", "bifurcation", "trifurcation"]] = None
    bifurcationMedina: Optional[str] = None
    bifurcationAngulation: Optional[float] = None
    segment_name: SEGMENT_NAMES


class CoronaryIVUSDescription(BaseModel):
    minimum_lumen_area: Optional[float] = None
    minimum_lumen_diameter: Optional[float] = None
    percent_stenosis: Optional[float] = Field(default=None, ge=0, le=100)
    length_stenosis: Optional[float] = None
    plaque_burden: Optional[float] = None
    reference_vessel_diameter: Optional[float] = None
    calcification: Optional[bool] = None
    fibrotic_lesion: Optional[bool] = None
    thrombotic_lesion: Optional[bool] = None
    wall_hematoma: Optional[bool] = None
    stent_under_expansion: Optional[bool] = None
    intra_stent_restenosis: Optional[bool] = None
    coronary_dissection: Optional[bool] = None


class CoronaryOCTDescription(BaseModel):
    minimum_lumen_area: Optional[float] = None
    minimum_lumen_diameter: Optional[float] = None
    percent_stenosis: Optional[float] = None
    length_stenosis: Optional[float] = None
    plaque_burden: Optional[float] = None
    reference_vessel_diameter: Optional[float] = None
    calcification: Optional[bool] = None
    fibrotic_lesion: Optional[bool] = None
    lipidique_lesion: Optional[bool] = None
    vulnerable_lesion: Optional[bool] = None
    thrombotic_lesion: Optional[bool] = None
    wall_hematoma: Optional[bool] = None
    intima_media_thickness: Optional[float] = None
    inflamatory_intimal_reaction: Optional[bool] = None
    ulceration_lesion: Optional[bool] = None
    stent_under_expansion: Optional[bool] = None
    stent_over_expansion: Optional[bool] = None
    intima_stent_distance: Optional[float] = None
    coronary_dissection: Optional[bool] = None
    intra_stent_restenosis: Optional[bool] = None


class CoronaryFFRDescription(BaseModel):
    FFR_hyperemia: Optional[float] = None
    FFR_basal: Optional[float] = None
    IFR_hyperemia: Optional[float] = None
    IFR_basal: Optional[float] = None
    CFR_hyperemia: Optional[float] = None
    CFR_basal: Optional[float] = None
    IMR_hyperemia: Optional[float] = None
    IMR_basal: Optional[float] = None


class CoronarySegmentDescription(BaseModel):
    lesion: CoronaryLesionDescription
    IVUS: Optional[CoronaryIVUSDescription] = None
    OCT: Optional[CoronaryOCTDescription] = None
    FFR: Optional[CoronaryFFRDescription] = None


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


MAIN_SEGMENTS = Literal[
    "LAD", "Diag1", "Diag2", "Cx", "Marg1", "Marg2", "IVPL", "IVPR", "RVG"
]
MAIN_ARTERIES = Literal["LM", "LAD", "Cx", "CD"]


class IVUSSegmentModel(BaseModel):
    segment_name: SEGMENT_NAMES
    description: CoronaryIVUSDescription


class OCTSegmentModel(BaseModel):
    segment_name: SEGMENT_NAMES
    description: CoronaryOCTDescription


class FFRSegmentModel(BaseModel):
    segment_name: SEGMENT_NAMES
    description: CoronaryFFRDescription


class ATLCatheter(BaseModel):
    segment: MAIN_ARTERIES
    difficultPassthrough: bool
    success: bool
    complication: Optional[str] = None
    remark: Optional[str] = None
    usedSpecificMaterialId: List[str]


class ATLGuideWire(BaseModel):
    segment: MAIN_SEGMENTS
    guideWireExchange: bool
    difficultPassthrough: bool
    success: bool
    complication: Optional[str] = None
    remark: Optional[str] = None
    usedSpecificMaterialId: List[str]


class ATLBalloon(BaseModel):
    inflationType: Literal[
        "pre-dilatation", "optimisation", "perforation", "Kissing-balloon"
    ]
    difficultPassthrough: bool
    success: bool
    inflation_pressure: Optional[int] = Field(default=None, ge=0, le=40)
    complication: Optional[str] = None
    remark: Optional[str] = None
    usedSpecificMaterialId: List[str]


class ATLStent(BaseModel):
    difficultPassthrough: bool
    success: bool
    inflation_pressure: Optional[int] = Field(default=None, ge=0, le=40)
    complication: Optional[str] = None
    remark: Optional[str] = None
    usedSpecificMaterialId: Optional[str] = None
    specificTechnic: List[
        Literal["parallel-wiring", "anchoring-balloon", "extension-Kt", "other"]
    ]


class ATLRotationalAtherectomy(BaseModel):
    difficultPassthrough: bool
    success: bool
    complication: Optional[str] = None
    remark: Optional[str] = None
    usedSpecificMaterialId: List[str]


class ATLMicroCatheter(BaseModel):
    segment: MAIN_SEGMENTS
    difficultPassthrough: bool
    success: bool
    complication: Optional[str] = None
    remark: Optional[str] = None
    usedSpecificMaterialId: Optional[str] = None


class ATLDEB(BaseModel):
    difficultPassthrough: bool
    success: bool
    inflation_pressure: Optional[int] = Field(default=None, ge=0, le=40)
    complication: Optional[str] = None
    remark: Optional[str] = None
    usedSpecificMaterialId: List[str]


class ATLResult(BaseModel):
    result: Literal["success", "intermediary", "failure"]
    residualStenosis: Literal[
        "0", "<30", "30-50", "50", "50-70", "70-90", "90-99", "100"
    ]
    TIMI_Flow: Optional[Literal["None", "TIMI 0", "TIMI 1", "TIMI 2", "TIMI 3"]] = None
    difficultPassthrough: bool
    failureOrigin: Optional[str] = None
    complication: Optional[str] = None
    remark: Optional[str] = None
    usedSpecificMaterialId: Optional[str] = None


class ATLGeneric(BaseModel):
    success: bool
    description: str
    complication: Optional[str] = None
    remark: Optional[str] = None
    usedSpecificMaterialId: Optional[str] = None


class GeneralProcedureStep(BaseModel):
    id: str


class AngioplastyKT(ATLCatheter, GeneralProcedureStep):
    type: Literal["KT"]


class AngioplastyGuideWire(ATLGuideWire, GeneralProcedureStep):
    type: Literal["guide-wire"]


class AngioplastyBalloon(ATLBalloon, GeneralProcedureStep):
    type: Literal["balloon"]
    segments: List[
        SEGMENT_NAMES
    ]  # Will be checked against actual CoronarySegmentation keys


class AngioplastyStent(ATLStent, GeneralProcedureStep):
    type: Literal["stent"]
    segments: List[SEGMENT_NAMES]


class AngioplastyRotationalAtherectomy(ATLRotationalAtherectomy, GeneralProcedureStep):
    type: Literal["rotational-atherectomy"]
    segments: List[SEGMENT_NAMES]


class AngioplastyMicroKT(ATLMicroCatheter, GeneralProcedureStep):
    type: Literal["micro-KT"]


class AngioplastyDEB(ATLDEB, GeneralProcedureStep):
    type: Literal["DEB"]
    segments: List[SEGMENT_NAMES]


class AngioplastyResult(ATLResult, GeneralProcedureStep):
    type: Literal["result"]
    segments: List[SEGMENT_NAMES]


class AngioplastyGeneric(ATLGeneric, GeneralProcedureStep):
    type: Literal["generic"]
    segments: List[SEGMENT_NAMES]


class AngioplastyProcedureStep(
    RootModel[
        Union[
            AngioplastyKT,
            AngioplastyGuideWire,
            AngioplastyBalloon,
            AngioplastyStent,
            AngioplastyRotationalAtherectomy,
            AngioplastyMicroKT,
            AngioplastyDEB,
            AngioplastyResult,
            AngioplastyGeneric,
        ]
    ]
):
    pass
