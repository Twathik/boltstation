from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.Sept.Sept_Calcification_No_stenosis import (
    Sept_calcification_No_stenosis_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.Sept.Sept_Stent_No_lesion import (
    Sept_stent_No_lesion_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.Sept.Sept_Thrombus_No_stenosis import (
    Sept_Thrombus_No_stenosis_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.Sept.Sept_segments import (
    Sept_segments_parser,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.Sept.Sept_stenosis import (
    Sept_stenosis_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.utils.anomalies_calculator import (
    hole_segment_anomalie_calculator,
    stenotic_with_occlusion_anomalies_calculator,
)

from src.lib.ai_document.data_injectors.generate_coronarography.utils.segment_description import (
    get_remarks,
)
from src.lib.ai_document.utils.ai_document_classes import CoronarySegmentation


def Sept_generator(state: CoronarySegmentation) -> str:
    Sept_report = ""

    segments = Sept_segments_parser(state)
    all_anomalies = hole_segment_anomalie_calculator(segments)
    lesion_number = stenotic_with_occlusion_anomalies_calculator(segments)

    if lesion_number == 0 and all_anomalies == 0:
        return "Absence de lésions angiographiques au niveau des septales."
    Sept_report = Sept_stenosis_generator(state, Sept_report)
    Sept_report += Sept_Thrombus_No_stenosis_generator(state)
    Sept_report += Sept_calcification_No_stenosis_generator(state)
    Sept_report += Sept_stent_No_lesion_generator(state)
    remarks = get_remarks(segments)
    Sept_report += f"""({remarks}) """ if len(remarks) > 0 else ""

    return Sept_report
