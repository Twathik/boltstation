from src.lib.generate_coronarography.generators.segment_generators.IVPR.IVPR_Calcification_No_stenosis import (
    IVPR_calcification_No_stenosis_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.IVPR.IVPR_Stent_No_lesion import (
    IVPR_stent_No_lesion_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.IVPR.IVPR_Thrombus_No_stenosis import (
    IVPR_Thrombus_No_stenosis_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.IVPR.IVPR_segments import (
    IVPR_segments_parser,
)
from src.lib.generate_coronarography.generators.segment_generators.IVPR.IVPR_stenosis import (
    IVPR_stenosis_generator,
)
from src.lib.generate_coronarography.utils.anomalies_calculator import (
    hole_segment_anomalie_calculator,
    stenotic_with_occlusion_anomalies_calculator,
)
from src.lib.generate_coronarography.utils.coronarography_classes import (
    CoronarySegmentation,
)
from src.lib.generate_coronarography.utils.segment_description import get_remarks


def IVPR_generator(state: CoronarySegmentation) -> str:
    IVPR_report = ""

    segments = IVPR_segments_parser(state)
    all_anomalies = hole_segment_anomalie_calculator(segments)
    lesion_number = stenotic_with_occlusion_anomalies_calculator(segments)

    if lesion_number == 0 and all_anomalies == 0:
        return "Absence de lésions angiographiques au niveau de l'artère interventriculaire postérieure droite."
    IVPR_report = IVPR_stenosis_generator(state, IVPR_report)
    IVPR_report += IVPR_Thrombus_No_stenosis_generator(state)
    IVPR_report += IVPR_calcification_No_stenosis_generator(state)
    IVPR_report += IVPR_stent_No_lesion_generator(state)
    remarks = get_remarks(segments)
    IVPR_report += f"""({remarks}) """ if len(remarks) > 0 else ""

    return IVPR_report
