from src.lib.generate_coronarography.generators.segment_generators.LAD.LAD_Calcification_No_stenosis import (
    LAD_calcification_No_stenosis_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.LAD.LAD_Stent_No_lesion import (
    LAD_stent_No_lesion_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.LAD.LAD_Thrombus_No_stenosis import (
    LAD_Thrombus_No_stenosis_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.LAD.LAD_segments import (
    LAD_segments_parser,
)
from src.lib.generate_coronarography.utils.anomalies_calculator import (
    hole_segment_anomalie_calculator,
    stenotic_with_occlusion_anomalies_calculator,
)
from src.lib.generate_coronarography.utils.coronarography_classes import (
    CoronarySegmentation,
)
from src.lib.generate_coronarography.generators.segment_generators.LAD.LAD_stenosis import (
    LAD_stenosis_generator,
)
from src.lib.generate_coronarography.utils.segment_description import get_remarks


def LAD_generator(state: CoronarySegmentation) -> str:
    LAD_report = ""

    segments = LAD_segments_parser(state)
    all_anomalies = hole_segment_anomalie_calculator(segments)
    lesion_number = stenotic_with_occlusion_anomalies_calculator(segments)

    if lesion_number == 0 and all_anomalies == 0:
        return "Absence de lésions angiographiques au niveau de l'interventriculaire antérieure."
    LAD_report = LAD_stenosis_generator(state, LAD_report)
    LAD_report += LAD_Thrombus_No_stenosis_generator(state)
    LAD_report += LAD_calcification_No_stenosis_generator(state)
    LAD_report += LAD_stent_No_lesion_generator(state)
    remarks = get_remarks(segments)
    LAD_report += f"""({remarks}) """ if len(remarks) > 0 else ""

    return LAD_report
