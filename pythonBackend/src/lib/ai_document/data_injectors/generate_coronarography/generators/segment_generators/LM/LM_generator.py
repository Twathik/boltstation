from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.LM.LM_Calcification_No_stenosis import (
    LM_calcification_No_stenosis_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.LM.LM_Stent_No_lesion import (
    LM_stent_No_lesion_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.LM.LM_Thrombus_No_stenosis import (
    LM_Thrombus_No_stenosis_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.utils.anomalies_calculator import (
    hole_segment_anomalie_calculator,
    stenotic_anomalies_calculator,
    stenotic_with_occlusion_anomalies_calculator,
)

from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.LM.LM_segments import (
    LM_segments_parser,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.LM.LM_stenosis import (
    LM_stenosis_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.utils.segment_description import (
    get_remarks,
)
from src.lib.ai_document.utils.ai_document_classes import CoronarySegmentation


def LM_generator(state: CoronarySegmentation) -> str:
    LM_report = ""
    segments = LM_segments_parser(state=state)
    all_anomalies = hole_segment_anomalie_calculator(segments)

    lesion_number = stenotic_with_occlusion_anomalies_calculator(segments=segments)

    if lesion_number == 0 and all_anomalies == 0:
        return "Absence de lésions angiographiques."
    LM_report = LM_stenosis_generator(state=state, LM_report=LM_report)
    LM_report += LM_Thrombus_No_stenosis_generator(state)
    LM_report += LM_calcification_No_stenosis_generator(state)
    LM_report += LM_stent_No_lesion_generator(state)
    remarks = get_remarks(segments)
    LM_report += f"""({remarks}) """ if len(remarks) > 0 else ""

    return LM_report
