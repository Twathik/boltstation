import re
from typing import Dict, Any

from src.lib.barcode_parser.GS1_mapping import Gs1Mapping

# Assuming Gs1Mapping and ParsedBarCodeModel are imported from other modules


def get_decimal(barcode: str) -> str:
    first_part = barcode[4 : 4 + int(barcode[4], 10)]
    second_part = barcode[4 + int(barcode[4], 10) : 10]
    return f"{first_part},{second_part}"


def check_ai_identifiers(barcode: str) -> Dict[str, Any]:
    if barcode[0] == "0":
        if barcode.startswith("00"):
            return {
                "parsedElements": {"SSCC": barcode[2:18]},
                "remainingBarcode": barcode[18:],
            }
        if barcode.startswith("01"):
            return {
                "parsedElements": {"GTIN": barcode[2:16]},
                "remainingBarcode": barcode[16:],
            }
        if barcode.startswith("02"):
            return {
                "parsedElements": {"GTIN_CONTENT": barcode[2:16]},
                "remainingBarcode": barcode[16:],
            }

    if barcode[0] == "1":
        if barcode.startswith("10"):
            return {
                "parsedElements": {"LOT": barcode[2:22]},
                "remainingBarcode": barcode[22:],
            }
        if barcode.startswith("11"):
            return {
                "parsedElements": {"PROD_DATE": barcode[2:8]},
                "remainingBarcode": barcode[8:],
            }
        if barcode.startswith("12"):
            return {
                "parsedElements": {"DUE_DATE": barcode[2:8]},
                "remainingBarcode": barcode[8:],
            }
        if barcode.startswith("13"):
            return {
                "parsedElements": {"PACK_DATE": barcode[2:8]},
                "remainingBarcode": barcode[8:],
            }
        if barcode.startswith("15"):
            return {
                "parsedElements": {"BEST_BEFORE": barcode[2:8]},
                "remainingBarcode": barcode[8:],
            }
        if barcode.startswith("17"):
            return {
                "parsedElements": {"USE_BY_oder_EXPIRY": barcode[2:8]},
                "remainingBarcode": barcode[8:],
            }

    if barcode[0] == "2":
        if barcode.startswith("20"):
            return {
                "parsedElements": {"VARIANT": barcode[2:4]},
                "remainingBarcode": barcode[4:],
            }
        if barcode.startswith("21"):
            return {
                "parsedElements": {"SERIAL": barcode[2:22]},
                "remainingBarcode": barcode[22:],
            }
        if barcode.startswith("240"):
            return {
                "parsedElements": {"ADDITIONAL_ID": barcode[3:33]},
                "remainingBarcode": barcode[33:],
            }
        if barcode.startswith("241"):
            return {
                "parsedElements": {"CUST_PART_NO": barcode[3:33]},
                "remainingBarcode": barcode[33:],
            }
        if barcode.startswith("250"):
            return {
                "parsedElements": {"SECONDARY_SERIAL": barcode[3:33]},
                "remainingBarcode": barcode[33:],
            }
        if barcode.startswith("251"):
            return {
                "parsedElements": {"REF_TO_SOURCE": barcode[3:33]},
                "remainingBarcode": barcode[33:],
            }
        if barcode.startswith("253"):
            return {
                "parsedElements": {"GDTI": f"{barcode[3:16]}_{barcode[16:33]}"},
                "remainingBarcode": barcode[33:],
            }

    if barcode[0] == "3":
        if barcode.startswith("30"):
            return {
                "parsedElements": {"VAR_COUNT": barcode[2:10]},
                "remainingBarcode": barcode[10:],
            }
        if barcode.startswith("31"):
            if barcode.startswith("310"):
                return {
                    "parsedElements": {"POIDS_NET_kg": get_decimal(barcode)},
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("311"):
                return {
                    "parsedElements": {"LONGUEUR_m": get_decimal(barcode)},
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("312"):
                return {
                    "parsedElements": {"LARGEUR_m": get_decimal(barcode)},
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("313"):
                return {
                    "parsedElements": {"HAUTEUR_m": get_decimal(barcode)},
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("314"):
                return {
                    "parsedElements": {"SURFACE_m2": get_decimal(barcode)},
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("315"):
                return {
                    "parsedElements": {"VOLUME_NET_l": get_decimal(barcode)},
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("316"):
                return {
                    "parsedElements": {"VOLUME_NET_m3": get_decimal(barcode)},
                    "remainingBarcode": barcode[10:],
                }

        if barcode.startswith("32"):
            if barcode.startswith("320"):
                return {
                    "parsedElements": {"POIDS_NET_lb": get_decimal(barcode)},
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("321"):
                return {
                    "parsedElements": {"LONGUEUR_i": get_decimal(barcode)},
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("322"):
                return {
                    "parsedElements": {"LONGUEUR_f": get_decimal(barcode)},
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("323"):
                return {
                    "parsedElements": {"LONGUEUR_y": get_decimal(barcode)},
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("324"):
                return {
                    "parsedElements": {"LARGEUR_i": get_decimal(barcode)},
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("325"):
                return {
                    "parsedElements": {"LARGEUR_f": get_decimal(barcode)},
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("326"):
                return {
                    "parsedElements": {"LARGEUR_y": get_decimal(barcode)},
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("327"):
                return {
                    "parsedElements": {"HAUTEUR_i": get_decimal(barcode)},
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("328"):
                return {
                    "parsedElements": {"HAUTEUR_f": get_decimal(barcode)},
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("329"):
                return {
                    "parsedElements": {"HAUTEUR_y": get_decimal(barcode)},
                    "remainingBarcode": barcode[10:],
                }

        if barcode.startswith("35"):
            if barcode.startswith("350"):
                return {
                    "parsedElements": {
                        "SURFACE_i2": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("351"):
                return {
                    "parsedElements": {
                        "SURFACE_f2": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("352"):
                return {
                    "parsedElements": {
                        "SURFACE_y2": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("356"):
                return {
                    "parsedElements": {
                        "POIDS_NET_t": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("357"):
                return {
                    "parsedElements": {
                        "VOLUME_NET_oz": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
        if barcode.startswith("36"):
            if barcode.startswith("360"):
                return {
                    "parsedElements": {
                        "VOLUME_NET_lb": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("361"):
                return {
                    "parsedElements": {
                        "VOLUME_NET_g": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("364"):
                return {
                    "parsedElements": {
                        "VOLUME_NET_i3": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("365"):
                return {
                    "parsedElements": {
                        "VOLUME_NET_f3": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("366"):
                return {
                    "parsedElements": {
                        "VOLUME_NET_y3": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }

        if barcode.startswith("37"):
            return {
                "parsedElements": {
                    "COUNT": barcode[2:10],
                },
                "remainingBarcode": barcode[10:],
            }
        if barcode.startswith("33"):
            if barcode.startswith("330"):
                return {
                    "parsedElements": {
                        "POIDS_BRUT_kg": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("331"):
                return {
                    "parsedElements": {
                        "LONGUEUR_m_log": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("332"):
                return {
                    "parsedElements": {
                        "LARGEUR_m_log": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("333"):
                return {
                    "parsedElements": {
                        "HAUTEUR_m_log": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("334"):
                return {
                    "parsedElements": {
                        "SURFACE_m2_log": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("335"):
                return {
                    "parsedElements": {
                        "VOLUME_l_log": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("336"):
                return {
                    "parsedElements": {
                        "VOLUME_m3_log": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("337"):
                return {
                    "parsedElements": {
                        "KG_PER_m2": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }

        if barcode.startswith("34"):
            if barcode.startswith("340"):
                return {
                    "parsedElements": {
                        "POIDS_BRUT_lb": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("341"):
                return {
                    "parsedElements": {
                        "LONGUEUR_i_log": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("342"):
                return {
                    "parsedElements": {
                        "LONGUEUR_f_log": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("343"):
                return {
                    "parsedElements": {
                        "LONGUEUR_y_log": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("344"):
                return {
                    "parsedElements": {
                        "LARGEUR_i_log": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("345"):
                return {
                    "parsedElements": {
                        "LARGEUR_f_log": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("346"):
                return {
                    "parsedElements": {
                        "LARGEUR_y_log": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("347"):
                return {
                    "parsedElements": {
                        "HAUTEUR_i_log": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("348"):
                return {
                    "parsedElements": {
                        "HAUTEUR_f_log": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("349"):
                return {
                    "parsedElements": {
                        "HAUTEUR_y_log": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }

        if barcode.startswith("35"):
            if barcode.startswith("353"):
                return {
                    "parsedElements": {
                        "SURFACE_i2_log": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("354"):
                return {
                    "parsedElements": {
                        "SURFACE_f2_log": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("355"):
                return {
                    "parsedElements": {
                        "SURFACE_y2_log": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }

        if barcode.startswith("36"):
            if barcode.startswith("362"):
                return {
                    "parsedElements": {
                        "VOLUME_q_log": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("363"):
                return {
                    "parsedElements": {
                        "VOLUME_g_log": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("367"):
                return {
                    "parsedElements": {
                        "VOLUME_i3_log": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("368"):
                return {
                    "parsedElements": {
                        "VOLUME_f3_log": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("369"):
                return {
                    "parsedElements": {
                        "VOLUME_y3_log": get_decimal(barcode),
                    },
                    "remainingBarcode": barcode[10:],
                }
        if barcode.startswith("39"):
            if barcode.startswith("390"):
                return {
                    "parsedElements": {
                        "AMOUNT_local_Curr": f"{barcode[4:4 + int(barcode[4], 10)]},{barcode[4 + int(barcode[4], 10):19]}",
                    },
                    "remainingBarcode": barcode[19:],
                }
            if barcode.startswith("391"):
                return {
                    "parsedElements": {
                        "AMOUNT_curr_code": f"{barcode[4:7]}-{barcode[7:7 + int(barcode[4], 10)]},{barcode[7 + int(barcode[4], 10):22]}",
                    },
                    "remainingBarcode": barcode[22:],
                }
            if barcode.startswith("392"):
                return {
                    "parsedElements": {
                        "AMOUNT_local_curr_variable_WeightCONTENT": f"{barcode[4:4 + int(barcode[4], 10)]},{barcode[4 + int(barcode[4], 10):19]}",
                    },
                    "remainingBarcode": barcode[19:],
                }
            if barcode.startswith("393"):
                return {
                    "parsedElements": {
                        "AMOUNT_curr_code_variable_Weight": f"{barcode[4:7]}-{barcode[7:7 + int(barcode[4], 10)]},{barcode[7 + int(barcode[4], 10):22]}",
                    },
                    "remainingBarcode": barcode[22:],
                }
    if barcode[0] == "4":
        if barcode.startswith("40"):
            if barcode.startswith("400"):
                return {
                    "parsedElements": {
                        "ORDER_NUMBER": barcode[3:33],
                    },
                    "remainingBarcode": barcode[33:],
                }

            if barcode.startswith("401"):
                return {
                    "parsedElements": {
                        "CONSIGNMENT": barcode[3:33],
                    },
                    "remainingBarcode": barcode[33:],
                }

            if barcode.startswith("402"):
                return {
                    "parsedElements": {
                        "SHIPMENT_NO": barcode[3:20],
                    },
                    "remainingBarcode": barcode[20:],
                }

            if barcode.startswith("403"):
                return {
                    "parsedElements": {
                        "ROUTE": barcode[3:33],
                    },
                    "remainingBarcode": barcode[33:],
                }

        if barcode.startswith("41"):
            if barcode.startswith("410"):
                return {
                    "parsedElements": {
                        "SHIP_TO_LOC": barcode[3:16],
                    },
                    "remainingBarcode": barcode[16:],
                }
            if barcode.startswith("411"):
                return {
                    "parsedElements": {
                        "BILL_TO": barcode[3:16],
                    },
                    "remainingBarcode": barcode[16:],
                }
            if barcode.startswith("412"):
                return {
                    "parsedElements": {
                        "PURCHASE_FROM": barcode[3:16],
                    },
                    "remainingBarcode": barcode[16:],
                }
            if barcode.startswith("413"):
                return {
                    "parsedElements": {
                        "SHIP_FOR_LOC": barcode[3:16],
                    },
                    "remainingBarcode": barcode[16:],
                }
            if barcode.startswith("414"):
                return {
                    "parsedElements": {
                        "LOC_NO": barcode[3:16],
                    },
                    "remainingBarcode": barcode[16:],
                }
            if barcode.startswith("415"):
                return {
                    "parsedElements": {
                        "PAY_TO": barcode[3:16],
                    },
                    "remainingBarcode": barcode[16:],
                }

        if barcode.startswith("42"):
            if barcode.startswith("420"):
                return {
                    "parsedElements": {
                        "SHIP_TO_POST": barcode[3:23],
                    },
                    "remainingBarcode": barcode[23:],
                }
            if barcode.startswith("421"):
                return {
                    "parsedElements": {
                        "SHIP_TO_POST_With_Code": f"{barcode[3:6]}-{barcode[6:15]}",
                    },
                    "remainingBarcode": barcode[15:],
                }
            if barcode.startswith("422"):
                return {
                    "parsedElements": {
                        "ORIGIN": barcode[3:6],
                    },
                    "remainingBarcode": barcode[6:],
                }
    if barcode[0] == "8":
        if barcode.startswith("80"):
            if barcode.startswith("8001"):
                return {
                    "parsedElements": {
                        "DIMENSIONS": barcode[4:18],
                    },
                    "remainingBarcode": barcode[18:],
                }
            if barcode.startswith("8002"):
                return {
                    "parsedElements": {
                        "CMT_NO": barcode[4:24],
                    },
                    "remainingBarcode": barcode[24:],
                }
            if barcode.startswith("8003"):
                return {
                    "parsedElements": {
                        "GRAI": f"{barcode[4:18]}-{barcode[18:34]}",
                    },
                    "remainingBarcode": barcode[34:],
                }
            if barcode.startswith("8004"):
                return {
                    "parsedElements": {
                        "GIAI": barcode[4:34],
                    },
                    "remainingBarcode": barcode[34:],
                }
            if barcode.startswith("8005"):
                return {
                    "parsedElements": {
                        "PRICE_PER_UNIT": barcode[4:10],
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("8006"):
                return {
                    "parsedElements": {
                        "GCTIN": f"{barcode[4:18]}-{barcode[18:20]}-{barcode[20:22]}",
                    },
                    "remainingBarcode": barcode[22:],
                }
            if barcode.startswith("8007"):
                return {
                    "parsedElements": {
                        "IBAN": barcode[4:34],
                    },
                    "remainingBarcode": barcode[34:],
                }
            if barcode.startswith("8018"):
                return {
                    "parsedElements": {
                        "GSRN": barcode[4:22],
                    },
                    "remainingBarcode": barcode[22:],
                }
            if barcode.startswith("8020"):
                return {
                    "parsedElements": {
                        "REF_NO": barcode[4:29],
                    },
                    "remainingBarcode": barcode[29:],
                }

        if barcode.startswith("81"):
            if barcode.startswith("8100"):
                return {
                    "parsedElements": {
                        "Coopon_Code_GS1_1": f"{barcode[4:5]}-{barcode[5:10]}",
                    },
                    "remainingBarcode": barcode[10:],
                }
            if barcode.startswith("8101"):
                return {
                    "parsedElements": {
                        "Coopon_Code_GS1_2": f"{barcode[4:5]}-{barcode[5:10]}-{barcode[10:14]}",
                    },
                    "remainingBarcode": barcode[14:],
                }
            if barcode.startswith("8102"):
                return {
                    "parsedElements": {
                        "Coopon_Code_GS1_3": f"{barcode[4:5]}-{barcode[5:6]}",
                    },
                    "remainingBarcode": barcode[6:],
                }

    if barcode.startswith("90"):
        return {
            "parsedElements": {
                "INTERNAL": barcode[2:32],
            },
            "remainingBarcode": barcode[32:],
        }

    for index in range(91, 100):
        if barcode.startswith(str(index)):
            return {
                "parsedElements": {
                    "INTERNAL_Id": barcode[2:32],
                },
                "remainingBarcode": barcode[32:],
            }

    # Continuing similarly for other fields...

    raise ValueError("Unrecognized AI code")


def GS1_bar_code_parser(barcode: str) -> Dict[str, Any]:
    remaining_barcode = barcode
    parsed_elements = {}
    i = 110
    while len(remaining_barcode) > 0 and i > 0:
        check_identifiers = check_ai_identifiers(remaining_barcode)
        remaining_barcode = check_identifiers["remainingBarcode"]
        parsed_element_key = list(check_identifiers["parsedElements"].keys())[0]
        if parsed_element_key:
            regexp = Gs1Mapping[parsed_element_key]["regEx"]
            if not regexp.match(
                check_identifiers["parsedElements"][parsed_element_key].replace(",", "")
            ):
                raise ValueError(
                    f"Barcode corruption detected: Key => {parsed_element_key}, value => {check_identifiers['parsedElements'][parsed_element_key]}"
                )
        parsed_elements.update(check_identifiers["parsedElements"])
        i -= 1

    return parsed_elements
