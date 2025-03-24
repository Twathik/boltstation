import re
from typing import Dict

# Mapping definition using Python
Gs1Mapping: Dict[str, Dict[str, object]] = {
    "SSCC": {
        "code": "00",
        "decimal": False,
        "regEx": re.compile(r"^(\d{18})$"),
    },
    "GTIN": {
        "code": "01",
        "decimal": False,
        "regEx": re.compile(r"^(\d{14})$"),
    },
    "GTIN_CONTENT": {
        "code": "02",
        "decimal": False,
        "regEx": re.compile(r"^(\d{14})$"),
    },
    "PROD_DATE": {
        "code": "11",
        "decimal": False,
        "regEx": re.compile(r"^(\d{2}(?:0\d|1[0-2])(?:[0-2]\d|3[01]))$"),
    },
    "DUE_DATE": {
        "code": "12",
        "decimal": False,
        "regEx": re.compile(r"^(\d{2}(?:0\d|1[0-2])(?:[0-2]\d|3[01]))$"),
    },
    "PACK_DATE": {
        "code": "12",
        "decimal": False,
        "regEx": re.compile(r"^(\d{2}(?:0\d|1[0-2])(?:[0-2]\d|3[01]))$"),
    },
    "BEST_BEFORE": {
        "code": "15",
        "decimal": False,
        "regEx": re.compile(r"^(\d{2}(?:0\d|1[0-2])(?:[0-2]\d|3[01]))$"),
    },
    "USE_BY_oder_EXPIRY": {
        "code": "17",
        "decimal": False,
        "regEx": re.compile(r"^(\d{2}(?:0\d|1[0-2])(?:[0-2]\d|3[01]))$"),
    },
    "VARIANT": {
        "code": "20",
        "decimal": False,
        "regEx": re.compile(r"^(\d{2})$"),
    },
    "SERIAL": {
        "code": "21",
        "decimal": False,
        "regEx": re.compile(r"^([!%-?A-Z_a-z\x22]{1,20})$"),
    },
    "CPV": {
        "code": "22",
        "decimal": False,
        "regEx": re.compile(r"^([!%-?A-Z_a-z\x22]{1,20})$"),
    },
    "ADDITIONAL_ID": {
        "code": "240",
        "decimal": False,
        "regEx": re.compile(r"^([!%-?A-Z_a-z\x22]{1,30})$"),
    },
    "CUST_PART_NO": {
        "code": "241",
        "decimal": False,
        "regEx": re.compile(r"^([!%-?A-Z_a-z\x22]{1,30})$"),
    },
    "SECONDARY_SERIAL": {
        "code": "250",
        "decimal": False,
        "regEx": re.compile(r"^([!%-?A-Z_a-z\x22]{1,30})$"),
    },
    "REF_TO_SOURCE": {
        "code": "251",
        "decimal": False,
        "regEx": re.compile(r"^([!%-?A-Z_a-z\x22]{1,30})$"),
    },
    "GDTI": {
        "code": "253",
        "decimal": False,
        "regEx": re.compile(r"^(\d{13})([!%-?A-Z_a-z\x22]{0,17})$"),
    },
    "VAR_COUNT": {
        "code": "30",
        "decimal": False,
        "regEx": re.compile(r"^(\d{0,8})$"),
    },
    "POIDS_NET_kg": {
        "code": "310",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "LONGUEUR_m": {
        "code": "311",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "LARGEUR_m": {
        "code": "312",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "HAUTEUR_m": {
        "code": "313",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "SURFACE_m2": {
        "code": "314",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "VOLUME_NET_l": {
        "code": "315",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "VOLUME_NET_m3": {
        "code": "316",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "POIDS_NET_lb": {
        "code": "320",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "LONGUEUR_i": {
        "code": "321",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "LONGUEUR_f": {
        "code": "322",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "LONGUEUR_y": {
        "code": "323",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "LARGEUR_i": {
        "code": "324",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "LARGEUR_f": {
        "code": "325",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "LARGEUR_y": {
        "code": "326",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "HAUTEUR_i": {
        "code": "327",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "HAUTEUR_f": {
        "code": "328",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "HAUTEUR_y": {
        "code": "329",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "SURFACE_i2": {
        "code": "350",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "SURFACE_f2": {
        "code": "351",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "SURFACE_y2": {
        "code": "352",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "POIDS_NET_t": {
        "code": "356",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "VOLUME_NET_oz": {
        "code": "357",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "VOLUME_NET_lb": {
        "code": "360",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "VOLUME_NET_g": {
        "code": "361",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "VOLUME_NET_i3": {
        "code": "364",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "VOLUME_NET_f3": {
        "code": "365",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "VOLUME_NET_y3": {
        "code": "366",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "POIDS_BRUT_kg": {
        "code": "330",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "LONGUEUR_m_log": {
        "code": "331",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "LARGEUR_m_log": {
        "code": "332",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "HAUTEUR_m_log": {
        "code": "333",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "SURFACE_m2_log": {
        "code": "334",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "VOLUME_l_log": {
        "code": "335",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "VOLUME_m3_log": {
        "code": "336",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "POIDS_BRUT_lb": {
        "code": "340",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "LONGUEUR_i_log": {
        "code": "341",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "LONGUEUR_f_log": {
        "code": "342",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "LONGUEUR_y_log": {
        "code": "343",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "LARGEUR_i_log": {
        "code": "344",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "LARGEUR_f_log": {
        "code": "345",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "LARGEUR_y_log": {
        "code": "346",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "HAUTEUR_i_log": {
        "code": "347",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "HAUTEUR_f_log": {
        "code": "348",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "HAUTEUR_y_log": {
        "code": "349",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "SURFACE_i2_log": {
        "code": "353",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "SURFACE_f2_log": {
        "code": "354",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "SURFACE_y2_log": {
        "code": "355",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "VOLUME_q_log": {
        "code": "362",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "VOLUME_g_log": {
        "code": "363",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "VOLUME_i3_log": {
        "code": "367",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "VOLUME_f3_log": {
        "code": "368",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "VOLUME_y3_log": {
        "code": "369",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "ORDER_NUMBER": {
        "code": "400",
        "decimal": False,
        "regEx": re.compile(r"^([!%-?A-Z_a-z\x22]{1,30})$"),
    },
    "CONSIGNMENT": {
        "code": "401",
        "decimal": False,
        "regEx": re.compile(r"^([!%-?A-Z_a-z\x22]{1,30})$"),
    },
    "SHIPMENT_NO": {
        "code": "402",
        "decimal": False,
        "regEx": re.compile(r"^(\d{17})$"),
    },
    "ROUTE": {
        "code": "400",
        "decimal": False,
        "regEx": re.compile(r"^([!%-?A-Z_a-z\x22]{1,30})$"),
    },
    "SHIP_TO_LOC": {
        "code": "410",
        "decimal": False,
        "regEx": re.compile(r"^(\d{13})$"),
    },
    "BILL_TO": {
        "code": "411",
        "decimal": False,
        "regEx": re.compile(r"^(\d{13})$"),
    },
    "PURCHASE_FROM": {
        "code": "412",
        "decimal": False,
        "regEx": re.compile(r"^(\d{13})$"),
    },
    "SHIP_FOR_LOC": {
        "code": "413",
        "decimal": False,
        "regEx": re.compile(r"^(\d{13})$"),
    },
    "LOC_NO": {
        "code": "414",
        "decimal": False,
        "regEx": re.compile(r"^(\d{13})$"),
    },
    "PAY_TO": {
        "code": "415",
        "decimal": False,
        "regEx": re.compile(r"^(\d{13})$"),
    },
    "SHIP_TO_POST": {
        "code": "420",
        "decimal": False,
        "regEx": re.compile(r"^([!%-?A-Z_a-z\x22]{1,20})$"),
    },
    "SHIP_TO_POST_With_Code": {
        "code": "421",
        "decimal": False,
        "regEx": re.compile(r"^(\d{3})([!%-?A-Z_a-z\x22]{1,9})$"),
    },
    "ORIGIN": {
        "code": "422",
        "decimal": False,
        "regEx": re.compile(r"^(\d{3})$"),
    },
    "DIMENSIONS": {
        "code": "8001",
        "decimal": False,
        "regEx": re.compile(r"^(\d{4})(\d{5})(\d{3})(\d{1})(\d{1})$"),
    },
    "CMT_NO": {
        "code": "8002",
        "decimal": False,
        "regEx": re.compile(r"^([!%-?A-Z_a-z\x22]{1,20})$"),
    },
    "GRAI": {
        "code": "8003",
        "decimal": False,
        "regEx": re.compile(r"^(0)(\d{13})([!%-?A-Z_a-z\x22]{0,16})$"),
    },
    "GIAI": {
        "code": "8004",
        "decimal": False,
        "regEx": re.compile(r"^([!%-?A-Z_a-z\x22]{1,30})$"),
    },
    "PRICE_PER_UNIT": {
        "code": "8005",
        "decimal": False,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "GCTIN": {
        "code": "8006",
        "decimal": False,
        "regEx": re.compile(r"^(\d{14})(\d{4})$"),
    },
    "IBAN": {
        "code": "8007",
        "decimal": False,
        "regEx": re.compile(r"^([!%-?A-Z_a-z\x22]{1,34})$"),
    },
    "GSRN": {
        "code": "8018",
        "decimal": False,
        "regEx": re.compile(r"^(\d{18})$"),
    },
    "REF_NO": {
        "code": "8020",
        "decimal": False,
        "regEx": re.compile(r"^([!%-?A-Z_a-z\x22]{1,25})$"),
    },
    "Coopon_Code_GS1_1": {
        "code": "8100",
        "decimal": False,
        "regEx": re.compile(r"^([!%-?A-Z_a-z\x22]{1,70})$"),
    },
    "Coopon_Code_GS1_2": {
        "code": "8101",
        "decimal": False,
        "regEx": re.compile(r"^([!%-?A-Z_a-z\x22]{1,70})$"),
    },
    "Coopon_Code_GS1_3": {
        "code": "8102",
        "decimal": False,
        "regEx": re.compile(r"^([!%-?A-Z_a-z\x22]{1,70})$"),
    },
    "INTERNAL": {
        "code": "90",
        "decimal": False,
        "regEx": re.compile(r"^([!%-?A-Z_a-z\x22]{1,30})$"),
    },
    "AMOUNT_local_Curr": {
        "code": "390",
        "decimal": True,
        "regEx": re.compile(r"^(\d{1,15})$"),
    },
    "AMOUNT_curr_code": {
        "code": "391",
        "decimal": True,
        "regEx": re.compile(r"^(\d{3})(\d{1,15})$"),
    },
    "AMOUNT_local_curr_variable_WeightCONTENT": {
        "code": "392",
        "decimal": True,
        "regEx": re.compile(r"^(\d{1,15})$"),
    },
    "AMOUNT_curr_code_variable_Weight": {
        "code": "393",
        "decimal": True,
        "regEx": re.compile(r"^(\d{3})(\d{1,15})$"),
    },
    "COUNT": {
        "code": "37",
        "decimal": False,
        "regEx": re.compile(r"\d{1,8}"),
    },
    "KG_PER_m2": {
        "code": "337",
        "decimal": True,
        "regEx": re.compile(r"^(\d{6})$"),
    },
    "LOT": {
        "code": "10",
        "decimal": False,
        "regEx": re.compile(r"^([!%-?A-Z_a-z\x22]{1,20})$"),
    },
    "INTERNAL_Id": {
        "code": "91",
        "decimal": False,
        "regEx": re.compile(r"^([!%-?A-Z_a-z\x22]{1,90})$"),
    },
}
