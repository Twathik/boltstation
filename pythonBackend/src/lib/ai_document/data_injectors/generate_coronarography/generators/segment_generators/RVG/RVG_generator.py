from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.RVG.RVG_Calcification_No_stenosis import (
    RVG_calcification_No_stenosis_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.RVG.RVG_Stent_No_lesion import (
    RVG_stent_No_lesion_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.RVG.RVG_Thrombus_No_stenosis import (
    RVG_Thrombus_No_stenosis_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.RVG.RVG_segments import (
    RVG_segments_parser,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.RVG.RVG_stenosis import (
    RVG_stenosis_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.utils.anomalies_calculator import (
    hole_segment_anomalie_calculator,
    stenotic_with_occlusion_anomalies_calculator,
)

from src.lib.ai_document.data_injectors.generate_coronarography.utils.segment_description import (
    get_remarks,
)
from src.lib.ai_document.utils.ai_document_classes import CoronarySegmentation


def RVG_generator(state: CoronarySegmentation) -> str:
    RVG_report = ""

    segments = RVG_segments_parser(state)
    all_anomalies = hole_segment_anomalie_calculator(segments)
    lesion_number = stenotic_with_occlusion_anomalies_calculator(segments)

    if lesion_number == 0 and all_anomalies == 0:
        return "Absence de lésions angiographiques au niveau de la rétro ventriculaire gauche."
    RVG_report = RVG_stenosis_generator(state, RVG_report)
    RVG_report += RVG_Thrombus_No_stenosis_generator(state)
    RVG_report += RVG_calcification_No_stenosis_generator(state)
    RVG_report += RVG_stent_No_lesion_generator(state)
    remarks = get_remarks(segments)
    RVG_report += f"""({remarks}) """ if len(remarks) > 0 else ""

    return RVG_report
