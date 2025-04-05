from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.Diag.Diag_Calcification_No_stenosis import (
    Diag_calcification_No_stenosis_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.Diag.Diag_Stent_No_lesion import (
    Diag_stent_No_lesion_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.Diag.Diag_Thrombus_No_stenosis import (
    Diag_Thrombus_No_stenosis_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.Diag.Diag_segments import (
    Diag_segments_parser,
)
from src.lib.ai_document.data_injectors.generate_coronarography.generators.segment_generators.Diag.Diag_stenosis import (
    Diag_stenosis_generator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.utils.anomalies_calculator import (
    hole_segment_anomalie_calculator,
    stenotic_with_occlusion_anomalies_calculator,
)
from src.lib.ai_document.data_injectors.generate_coronarography.utils.segment_description import (
    get_remarks,
)
from src.lib.ai_document.utils.ai_document_classes import CoronarySegmentation


def Diag_generator(state: CoronarySegmentation) -> str:
    Diag_report = ""

    segments = Diag_segments_parser(state)
    all_anomalies = hole_segment_anomalie_calculator(segments)
    lesion_number = stenotic_with_occlusion_anomalies_calculator(segments)

    if lesion_number == 0 and all_anomalies == 0:
        return "Absence de lésions angiographiques au niveau des diagonales."
    Diag_report = Diag_stenosis_generator(state, Diag_report)
    Diag_report += Diag_Thrombus_No_stenosis_generator(state)
    Diag_report += Diag_calcification_No_stenosis_generator(state)
    Diag_report += Diag_stent_No_lesion_generator(state)
    remarks = get_remarks(segments)
    Diag_report += f"""({remarks}) """ if len(remarks) > 0 else ""

    return Diag_report
