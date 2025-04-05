from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.CD.CD_Calcification_No_stenosis import (
    CD_calcification_No_stenosis_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.CD.CD_Stent_No_lesion import (
    CD_stent_No_lesion_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.CD.CD_Thrombus_No_stenosis import (
    CD_Thrombus_No_stenosis_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.CD.CD_segments import (
    CD_segments_parser,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.CD.CD_stenosis import (
    CD_stenosis_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.utils.anomalies_calculator import (
    hole_segment_anomalie_calculator,
    stenotic_with_occlusion_anomalies_calculator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.utils.segment_description import (
    get_remarks,
)
from src.lib.ai_document.utils.ai_document_classes import CoronarySegmentation


def CD_generator(state: CoronarySegmentation) -> str:
    CD_report = ""

    segments = CD_segments_parser(state)
    all_anomalies = hole_segment_anomalie_calculator(segments)
    lesion_number = stenotic_with_occlusion_anomalies_calculator(segments)

    if lesion_number == 0 and all_anomalies == 0:
        return "Absence de lésions angiographiques au niveau de la coronaire droite."
    CD_report = CD_stenosis_generator(state, CD_report)
    CD_report += CD_Thrombus_No_stenosis_generator(state)
    CD_report += CD_calcification_No_stenosis_generator(state)
    CD_report += CD_stent_No_lesion_generator(state)
    remarks = get_remarks(segments)
    CD_report += f"""({remarks}) """ if len(remarks) > 0 else ""

    return CD_report
