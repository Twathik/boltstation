from src.lib.generate_coronarography.generators.segment_generators.IVPL.IVPL_Calcification_No_stenosis import (
    IVPL_calcification_No_stenosis_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.IVPL.IVPL_Stent_No_lesion import (
    IVPL_stent_No_lesion_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.IVPL.IVPL_Thrombus_No_stenosis import (
    IVPL_Thrombus_No_stenosis_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.IVPL.IVPL_segments import (
    IVPL_segments_parser,
)
from src.lib.generate_coronarography.generators.segment_generators.IVPL.IVPL_stenosis import (
    IVPL_stenosis_generator,
)
from src.lib.generate_coronarography.utils.anomalies_calculator import (
    hole_segment_anomalie_calculator,
    stenotic_with_occlusion_anomalies_calculator,
)
from src.lib.generate_coronarography.utils.coronarography_classes import (
    CoronarySegmentation,
)
from src.lib.generate_coronarography.utils.segment_description import get_remarks


def IVPL_generator(state: CoronarySegmentation) -> str:
    IVPL_report = ""

    segments = IVPL_segments_parser(state)
    all_anomalies = hole_segment_anomalie_calculator(segments)
    lesion_number = stenotic_with_occlusion_anomalies_calculator(segments)

    if lesion_number == 0 and all_anomalies == 0:
        return "Absence de lésions angiographiques au niveau de l'artère interventriculaire postérieure gauche."
    IVPL_report = IVPL_stenosis_generator(state, IVPL_report)
    IVPL_report += IVPL_Thrombus_No_stenosis_generator(state)
    IVPL_report += IVPL_calcification_No_stenosis_generator(state)
    IVPL_report += IVPL_stent_No_lesion_generator(state)
    remarks = get_remarks(segments)
    IVPL_report += f"""({remarks}) """ if len(remarks) > 0 else ""

    return IVPL_report
