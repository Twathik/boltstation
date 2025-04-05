from typing import Any, List

from pprintpp import pprint
from sqlalchemy import True_
from ulid import ULID


from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.Bisec.Bisec_generator import (
    Bisec_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.CD.CD_generator import (
    CD_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.CX.Cx_generator import (
    Cx_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.Diag.Diag_generator import (
    Diag_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.IVPL.IVPL_generator import (
    IVPL_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.IVPR.IVPR_generator import (
    IVPR_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.LAD.LAD_generator import (
    LAD_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.LM.LM_generator import (
    LM_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.Marg.Marg_generator import (
    Marg_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.RVG.RVG_generator import (
    RVG_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.Sept.Sept_generator import (
    Sept_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.utils.segments_mapping import (
    segments_mapping,
)
from src.lib.ai_document.utils.ai_document_classes import (
    CoronarySegmentation,
    GeneralAnatomySchema,
)


from src.lib.ai_document.utils.plate_general_utils import (
    append_generated_text,
    append_generated_text,
    extract_FFR_segments,
    extract_OCT_segments,
    extract_ivus_segments,
    has_ffr,
    has_ivus,
    has_oct,
)
from src.lib.prismaClient import prisma_client


async def coro_lesion_description(
    document: List[Any], chunk: Any, clinicalEventId: str, extracted_data: List[str]
) -> Any:

    clinical_event = await prisma_client.clinicalevent.find_first_or_raise(
        where={"id": clinicalEventId},
    )

    state = CoronarySegmentation.model_validate(clinical_event.jsonData["state"])
    generalAnatomy = GeneralAnatomySchema.model_validate(
        clinical_event.jsonData["generalAnatomy"]
    )

    append_generated_text(
        document,
        chunk,
        extracted_data,
        text=[
            {
                "text": "Réseau coronaire gauche:",
                "bold": True,
            }
        ],
    )
    if not generalAnatomy.SizeLM == "cannon de fusile":
        append_generated_text(
            document,
            chunk,
            extracted_data,
            text=[
                {
                    "text": f"**Tronc commun gauche:** {LM_generator(state)}",
                    "refactor": True,
                },
            ],
            indent=2,
        )

    append_generated_text(
        document,
        chunk,
        extracted_data,
        text=[
            {
                "text": f"**Interventriculaire antérieure: **{LAD_generator(state)}. {Diag_generator(state)}. {Sept_generator(state)}",
                "refactor": True,
            },
        ],
        indent=2,
    )
    append_generated_text(
        document,
        chunk,
        extracted_data,
        text=[
            {
                "text": f"**Artère circonflexe: **{Cx_generator(state)}. {Marg_generator(state)}. {IVPL_generator(state)}",
                "refactor": True,
            },
        ],
        indent=2,
    )

    if generalAnatomy.presentBissec:
        append_generated_text(
            document,
            chunk,
            extracted_data,
            text=[
                {
                    "text": f"**Artère bissectrice: **{Bisec_generator(state)}",
                    "refactor": True,
                },
            ],
            indent=2,
        )

    document.append({"text": "\n"})

    append_generated_text(
        document,
        chunk,
        extracted_data,
        text=[
            {
                "text": "Réseau coronaire droit: ",
                "bold": True,
            },
        ],
    )
    append_generated_text(
        document,
        chunk,
        extracted_data,
        text=[
            {"text": f"**Coronaire droite: **{CD_generator(state)}", "refactor": True},
        ],
        indent=2,
    )

    append_generated_text(
        document,
        chunk,
        extracted_data,
        text=[
            {
                "text": f"**Interventriculaire postérieur (IVP): **{IVPR_generator(state)}",
                "refactor": True,
            },
        ],
        indent=2,
    )
    append_generated_text(
        document,
        chunk,
        extracted_data,
        text=[
            {
                "text": f"**Rétroventriculaire gauche (RVG): **{RVG_generator(state)}",
                "refactor": True,
            },
        ],
        indent=2,
    )

    if has_ivus(state):
        IVUS = extract_ivus_segments(state)

        document.append({"text": "\n"})

        append_generated_text(
            document,
            chunk,
            extracted_data,
            text=[
                {
                    "text": "Procédure d'IVUS: ",
                    "bold": True,
                }
            ],
        )
        for sgt in IVUS:
            anomalies_count = (
                sgt.description.calcification
                + sgt.description.fibrotic_lesion
                + sgt.description.thrombotic_lesion
                + sgt.description.wall_hematoma
                + sgt.description.stent_under_expansion
                + sgt.description.intra_stent_restenosis
                + sgt.description.coronary_dissection
            )

            append_generated_text(
                document,
                chunk,
                extracted_data,
                text=[
                    {
                        "text": f"**{segments_mapping(sgt.segment_name)}**: {'absence de plaque au niveau de ce segment' if sgt.description.percent_stenosis == 0 else 'présence dune occlusion complète' if sgt.description.percent_stenosis == 100 else f"presence d'une sténose serrée évaluée à {int(sgt.description.percent_stenosis)}% à ce niveau" if sgt.description.percent_stenosis> 50 else f"presence d'une plaque évaluée à {int(sgt.description.percent_stenosis)}% à ce niveau"}{'.' if anomalies_count == 0 else f", nous notons par ailleurs la présence {"de fibrose importante, " if sgt.description.fibrotic_lesion else ''}{"d'un thrombus, " if sgt.description.thrombotic_lesion else ''}{"d'un hématome de paroi," if sgt.description.wall_hematoma else ''}{"d'une sous expansion de stent, " if sgt.description.stent_under_expansion else ''}{"d'une resténose intra stent, " if sgt.description.intra_stent_restenosis else ''}{"d'une dissection coronaire, " if sgt.description.coronary_dissection else ''} à ce niveau."}",
                        "refactor": True,
                    },
                ],
                indent=2,
            )
        document.append(
            {
                "children": [
                    {
                        "children": [
                            {
                                "children": [
                                    {
                                        "children": [{"text": "segment", "bold": True}],
                                        "type": "p",
                                        "id": str(ULID()),
                                    }
                                ],
                                "type": "td",
                                "id": str(ULID()),
                            },
                            {
                                "children": [
                                    {
                                        "children": [{"text": "MLA/MLD", "bold": True}],
                                        "type": "p",
                                        "id": str(ULID()),
                                    }
                                ],
                                "type": "td",
                                "colSpan": 1,
                                "rowSpan": 1,
                                "id": str(ULID()),
                            },
                            {
                                "children": [
                                    {
                                        "children": [{"text": "ref mm", "bold": True}],
                                        "type": "p",
                                        "id": str(ULID()),
                                    }
                                ],
                                "type": "td",
                                "colSpan": 1,
                                "rowSpan": 1,
                                "id": str(ULID()),
                            },
                            {
                                "children": [
                                    {
                                        "children": [{"text": "long mm", "bold": True}],
                                        "type": "p",
                                        "id": str(ULID()),
                                    }
                                ],
                                "type": "td",
                                "id": str(ULID()),
                            },
                            {
                                "children": [
                                    {
                                        "children": [{"text": "Vol mm3", "bold": True}],
                                        "type": "p",
                                        "id": str(ULID()),
                                    }
                                ],
                                "type": "td",
                                "colSpan": 1,
                                "rowSpan": 1,
                                "id": str(ULID()),
                            },
                        ],
                        "type": "tr",
                        "id": str(ULID()),
                    },
                ]
                + [
                    {
                        "children": [
                            {
                                "children": [
                                    {
                                        "children": [
                                            {
                                                "text": segments_mapping(
                                                    sgt.segment_name
                                                ),
                                                "bold": True,
                                            }
                                        ],
                                        "type": "p",
                                        "id": str(ULID()),
                                    }
                                ],
                                "type": "td",
                                "id": str(ULID()),
                            },
                            {
                                "children": [
                                    {
                                        "children": [
                                            {
                                                "text": f"{int(sgt.description.minimum_lumen_area)}/{int(sgt.description.minimum_lumen_diameter)}"
                                            }
                                        ],
                                        "type": "p",
                                        "id": str(ULID()),
                                    }
                                ],
                                "type": "td",
                                "colSpan": 1,
                                "rowSpan": 1,
                                "id": str(ULID()),
                            },
                            {
                                "children": [
                                    {
                                        "children": [
                                            {
                                                "text": f"{int(sgt.description.reference_vessel_diameter)}"
                                            }
                                        ],
                                        "type": "p",
                                        "id": str(ULID()),
                                    }
                                ],
                                "type": "td",
                                "colSpan": 1,
                                "rowSpan": 1,
                                "id": str(ULID()),
                            },
                            {
                                "children": [
                                    {
                                        "children": [
                                            {
                                                "text": f"{int(sgt.description.length_stenosis)}"
                                            }
                                        ],
                                        "type": "p",
                                        "id": str(ULID()),
                                    }
                                ],
                                "type": "td",
                                "id": str(ULID()),
                            },
                            {
                                "children": [
                                    {
                                        "children": [
                                            {
                                                "text": f"{int(sgt.description.plaque_burden)}"
                                            }
                                        ],
                                        "type": "p",
                                        "id": str(ULID()),
                                    }
                                ],
                                "type": "td",
                                "colSpan": 1,
                                "rowSpan": 1,
                                "id": str(ULID()),
                            },
                        ],
                        "type": "tr",
                        "id": str(ULID()),
                    }
                    for sgt in IVUS
                ],
                "type": "table",
                "id": str(ULID()),
                "colSizes": [225, 121, 110, 111, 99],
                "AiTarget": chunk["AiTarget"],
                "widgetId": chunk["widgetId"],
                "widgetName": chunk["widgetName"],
                "injected": True,
            }
        )
    if has_oct(state):
        OCT = extract_OCT_segments(state)

        document.append({"text": "\n"})
        append_generated_text(
            document,
            chunk,
            extracted_data,
            text=[
                {
                    "text": "Procédure d'OCT: ",
                    "bold": True,
                }
            ],
        )

        for sgt in OCT:
            anomalies_count = (
                sgt.description.calcification
                + sgt.description.fibrotic_lesion  #
                + sgt.description.lipidique_lesion  #
                + sgt.description.vulnerable_lesion  #
                + sgt.description.thrombotic_lesion  #
                + sgt.description.wall_hematoma  #
                + sgt.description.inflamatory_intimal_reaction  #
                + sgt.description.ulceration_lesion  #
                + sgt.description.stent_under_expansion  #
                + sgt.description.stent_over_expansion  #
                + sgt.description.coronary_dissection  #
                + sgt.description.intra_stent_restenosis  #
            )

            append_generated_text(
                document,
                chunk,
                extracted_data,
                text=[
                    {
                        "text": f"**{segments_mapping(sgt.segment_name)}**: {'absence de plaque au niveau de ce segment' if sgt.description.percent_stenosis == 0 else 'présence dune occlusion complète' if sgt.description.percent_stenosis == 100 else f"presence d'une sténose serrée évaluée à {int(sgt.description.percent_stenosis)}% à ce niveau" if sgt.description.percent_stenosis> 50 else f"presence d'une plaque évaluée à {int(sgt.description.percent_stenosis)}% à ce niveau"}{'.' if anomalies_count == 0 else f", nous notons par ailleurs la présence {"d'une ulcération de plaque, " if sgt.description.ulceration_lesion else ''}{"de fibrose importante, " if sgt.description.fibrotic_lesion else ''}{"d'un noyau lipidique important, " if sgt.description.lipidique_lesion else ''}{"d'une plaque vulnérable, " if sgt.description.vulnerable_lesion else ''}{"d'une réaction inflammatoire importante, " if sgt.description.inflamatory_intimal_reaction else ''}{"d'un thrombus, " if sgt.description.thrombotic_lesion else ''}{"d'un hématome de paroi," if sgt.description.wall_hematoma else ''}{"d'une sous expansion de stent, " if sgt.description.stent_under_expansion else ''}{"d'une sur expansion de stent, " if sgt.description.stent_over_expansion else ''}{"d'une resténose intra stent, " if sgt.description.intra_stent_restenosis else ''}{"d'une dissection coronaire, " if sgt.description.coronary_dissection else ''} à ce niveau."}",
                        "refactor": True,
                    },
                ],
                indent=2,
            )

        document.append(
            {
                "children": [
                    {
                        "children": [
                            {
                                "children": [
                                    {
                                        "children": [{"text": "segment", "bold": True}],
                                        "type": "p",
                                        "id": str(ULID()),
                                    }
                                ],
                                "type": "td",
                                "id": str(ULID()),
                            },
                            {
                                "children": [
                                    {
                                        "children": [{"text": "MLA/MLD", "bold": True}],
                                        "type": "p",
                                        "id": str(ULID()),
                                    }
                                ],
                                "type": "td",
                                "colSpan": 1,
                                "rowSpan": 1,
                                "id": str(ULID()),
                            },
                            {
                                "children": [
                                    {
                                        "children": [{"text": "ref mm", "bold": True}],
                                        "type": "p",
                                        "id": str(ULID()),
                                    }
                                ],
                                "type": "td",
                                "colSpan": 1,
                                "rowSpan": 1,
                                "id": str(ULID()),
                            },
                            {
                                "children": [
                                    {
                                        "children": [{"text": "long mm", "bold": True}],
                                        "type": "p",
                                        "id": str(ULID()),
                                    }
                                ],
                                "type": "td",
                                "id": str(ULID()),
                            },
                            {
                                "children": [
                                    {
                                        "children": [{"text": "Vol mm3", "bold": True}],
                                        "type": "p",
                                        "id": str(ULID()),
                                    }
                                ],
                                "type": "td",
                                "colSpan": 1,
                                "rowSpan": 1,
                                "id": str(ULID()),
                            },
                        ],
                        "type": "tr",
                        "id": str(ULID()),
                    },
                ]
                + [
                    {
                        "children": [
                            {
                                "children": [
                                    {
                                        "children": [
                                            {
                                                "text": segments_mapping(
                                                    sgt.segment_name
                                                ),
                                                "bold": True,
                                            }
                                        ],
                                        "type": "p",
                                        "id": str(ULID()),
                                    }
                                ],
                                "type": "td",
                                "id": str(ULID()),
                            },
                            {
                                "children": [
                                    {
                                        "children": [
                                            {
                                                "text": f"{int(sgt.description.minimum_lumen_area)}/{int(sgt.description.minimum_lumen_diameter)}"
                                            }
                                        ],
                                        "type": "p",
                                        "id": str(ULID()),
                                    }
                                ],
                                "type": "td",
                                "colSpan": 1,
                                "rowSpan": 1,
                                "id": str(ULID()),
                            },
                            {
                                "children": [
                                    {
                                        "children": [
                                            {
                                                "text": f"{int(sgt.description.reference_vessel_diameter)}"
                                            }
                                        ],
                                        "type": "p",
                                        "id": str(ULID()),
                                    }
                                ],
                                "type": "td",
                                "colSpan": 1,
                                "rowSpan": 1,
                                "id": str(ULID()),
                            },
                            {
                                "children": [
                                    {
                                        "children": [
                                            {
                                                "text": f"{int(sgt.description.length_stenosis)}"
                                            }
                                        ],
                                        "type": "p",
                                        "id": str(ULID()),
                                    }
                                ],
                                "type": "td",
                                "id": str(ULID()),
                            },
                            {
                                "children": [
                                    {
                                        "children": [
                                            {
                                                "text": f"{int(sgt.description.plaque_burden)}"
                                            }
                                        ],
                                        "type": "p",
                                        "id": str(ULID()),
                                    }
                                ],
                                "type": "td",
                                "colSpan": 1,
                                "rowSpan": 1,
                                "id": str(ULID()),
                            },
                        ],
                        "type": "tr",
                        "id": str(ULID()),
                    }
                    for sgt in OCT
                ],
                "type": "table",
                "id": str(ULID()),
                "colSizes": [225, 121, 110, 111, 99],
                "widgetId": chunk["widgetId"],
                "widgetName": chunk["widgetName"],
                "injected": True,
            }
        )
        table_anomalie_count = sum(
            1
            for sgt in OCT
            if sgt.description.intima_stent_distance is not None
            or sgt.description.intima_media_thickness is not None
        )
        if table_anomalie_count > 0:
            document.append({"text": "\n"})
            document.append(
                {
                    "children": [
                        {
                            "type": "tr",
                            "children": [
                                {
                                    "type": "td",
                                    "children": [
                                        {
                                            "type": "p",
                                            "children": [
                                                {"bold": True, "text": "segment"}
                                            ],
                                            "id": str(ULID()),
                                        }
                                    ],
                                    "id": str(ULID()),
                                },
                                {
                                    "children": [
                                        {
                                            "children": [
                                                {
                                                    "text": "Épaisseur intima media (mm)",
                                                    "bold": True,
                                                }
                                            ],
                                            "type": "p",
                                            "id": str(ULID()),
                                        }
                                    ],
                                    "type": "td",
                                    "colSpan": 1,
                                    "rowSpan": 1,
                                    "id": str(ULID()),
                                },
                                {
                                    "type": "td",
                                    "children": [
                                        {
                                            "type": "p",
                                            "children": [
                                                {
                                                    "text": "Distance stent intima (micromètre)",
                                                    "bold": True,
                                                }
                                            ],
                                            "id": str(ULID()),
                                        }
                                    ],
                                    "id": str(ULID()),
                                },
                            ],
                            "id": str(ULID()),
                        },
                    ]
                    + [
                        {
                            "type": "tr",
                            "children": [
                                {
                                    "type": "td",
                                    "children": [
                                        {
                                            "type": "p",
                                            "children": [
                                                {
                                                    "text": segments_mapping(
                                                        sgt.segment_name
                                                    ),
                                                    "bold": True,
                                                }
                                            ],
                                            "id": str(ULID()),
                                        }
                                    ],
                                    "id": str(ULID()),
                                },
                                {
                                    "children": [
                                        {
                                            "children": [
                                                {
                                                    "text": f"{int(sgt.description.intima_media_thickness)}"
                                                }
                                            ],
                                            "type": "p",
                                            "id": str(ULID()),
                                        }
                                    ],
                                    "type": "td",
                                    "colSpan": 1,
                                    "rowSpan": 1,
                                    "id": str(ULID()),
                                },
                                {
                                    "type": "td",
                                    "children": [
                                        {
                                            "type": "p",
                                            "children": [
                                                {
                                                    "text": f"{int(sgt.description.intima_stent_distance)}"
                                                }
                                            ],
                                            "id": str(ULID()),
                                        }
                                    ],
                                    "id": str(ULID()),
                                },
                            ],
                            "id": str(ULID()),
                        }
                        for sgt in OCT
                    ],
                    "type": "table",
                    "id": str(ULID()),
                    "widgetId": chunk["widgetId"],
                    "widgetName": chunk["widgetName"],
                    "injected": True,
                }
            )
    if has_ffr(state):
        FFR = extract_FFR_segments(state)
        document.append({"text": "\n"})
        append_generated_text(
            document,
            chunk,
            extracted_data,
            text=[
                {
                    "text": "FFR: ",
                    "bold": True,
                }
            ],
        )

        document.append(
            {
                "children": [
                    {
                        "type": "tr",
                        "children": [
                            {
                                "type": "td",
                                "children": [
                                    {
                                        "type": "p",
                                        "children": [
                                            {
                                                "bold": True,
                                                "text": "segment (basale/Hyperhémie)",
                                            }
                                        ],
                                        "id": str(ULID()),
                                    }
                                ],
                                "id": str(ULID()),
                            },
                            {
                                "type": "td",
                                "colSpan": 1,
                                "rowSpan": 1,
                                "children": [
                                    {
                                        "type": "p",
                                        "children": [{"bold": True, "text": "FFR"}],
                                        "id": str(ULID()),
                                    }
                                ],
                                "id": str(ULID()),
                            },
                            {
                                "type": "td",
                                "colSpan": 1,
                                "rowSpan": 1,
                                "children": [
                                    {
                                        "type": "p",
                                        "children": [{"bold": True, "text": "IFR"}],
                                        "id": str(ULID()),
                                    }
                                ],
                                "id": str(ULID()),
                            },
                            {
                                "type": "td",
                                "colSpan": 1,
                                "rowSpan": 1,
                                "children": [
                                    {
                                        "type": "p",
                                        "children": [{"bold": True, "text": "CMR"}],
                                        "id": str(ULID()),
                                    }
                                ],
                                "id": str(ULID()),
                            },
                            {
                                "type": "td",
                                "children": [
                                    {
                                        "type": "p",
                                        "children": [{"bold": True, "text": "IMR"}],
                                        "id": str(ULID()),
                                    }
                                ],
                                "id": str(ULID()),
                            },
                        ],
                        "id": str(ULID()),
                    },
                ]
                + [
                    {
                        "type": "tr",
                        "children": [
                            {
                                "type": "td",
                                "children": [
                                    {
                                        "type": "p",
                                        "children": [
                                            {
                                                "text": segments_mapping(
                                                    sgt.segment_name
                                                ),
                                                "bold": True,
                                            }
                                        ],
                                        "id": str(ULID()),
                                    }
                                ],
                                "id": str(ULID()),
                            },
                            {
                                "type": "td",
                                "colSpan": 1,
                                "rowSpan": 1,
                                "children": [
                                    {
                                        "type": "p",
                                        "children": [
                                            {
                                                "text": f"{int(sgt.description.FFR_basal)}/{int(sgt.description.FFR_hyperemia)}"
                                            }
                                        ],
                                        "id": str(ULID()),
                                    }
                                ],
                                "id": str(ULID()),
                            },
                            {
                                "type": "td",
                                "colSpan": 1,
                                "rowSpan": 1,
                                "children": [
                                    {
                                        "type": "p",
                                        "children": [
                                            {
                                                "text": f"{int(sgt.description.IFR_basal)}/{int(sgt.description.IFR_hyperemia)}"
                                            }
                                        ],
                                        "id": str(ULID()),
                                    }
                                ],
                                "id": str(ULID()),
                            },
                            {
                                "type": "td",
                                "colSpan": 1,
                                "rowSpan": 1,
                                "children": [
                                    {
                                        "type": "p",
                                        "children": [
                                            {
                                                "text": f"{int(sgt.description.CFR_hyperemia)}/{int(sgt.description.CFR_basal)}"
                                            }
                                        ],
                                        "id": str(ULID()),
                                    }
                                ],
                                "id": str(ULID()),
                            },
                            {
                                "type": "td",
                                "children": [
                                    {
                                        "type": "p",
                                        "children": [
                                            {
                                                "text": f"{int(sgt.description.IMR_basal)}/{int(sgt.description.IMR_hyperemia)}"
                                            }
                                        ],
                                        "id": str(ULID()),
                                    }
                                ],
                                "id": str(ULID()),
                            },
                        ],
                        "id": str(ULID()),
                    }
                    for sgt in FFR
                ],
                "type": "table",
                "colSizes": [203, 0, 0, 0, 0],
                "id": str(ULID()),
                "AiTarget": chunk["AiTarget"],
                "widgetId": chunk["widgetId"],
                "widgetName": chunk["widgetName"],
                "injected": True,
            }
        )
