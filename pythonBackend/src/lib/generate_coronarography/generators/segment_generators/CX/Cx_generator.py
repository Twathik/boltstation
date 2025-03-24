from src.lib.generate_coronarography.generators.segment_generators.CX.Cx_Calcification_No_stenosis import (
    Cx_calcification_No_stenosis_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.CX.Cx_Stent_No_lesion import (
    Cx_stent_No_lesion_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.CX.Cx_Thrombus_No_stenosis import (
    Cx_Thrombus_No_stenosis_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.CX.Cx_segments import (
    Cx_segments_parser,
)
from src.lib.generate_coronarography.generators.segment_generators.CX.Cx_stenosis import (
    Cx_stenosis_generator,
)
from src.lib.generate_coronarography.utils.anomalies_calculator import (
    hole_segment_anomalie_calculator,
    stenotic_with_occlusion_anomalies_calculator,
)
from src.lib.generate_coronarography.utils.coronarography_classes import (
    CoronarySegmentation,
)

from src.lib.generate_coronarography.utils.segment_description import get_remarks


def Cx_generator(state: CoronarySegmentation) -> str:
    Cx_report = ""

    segments = Cx_segments_parser(state)
    all_anomalies = hole_segment_anomalie_calculator(segments)
    lesion_number = stenotic_with_occlusion_anomalies_calculator(segments)

    if lesion_number == 0 and all_anomalies == 0:
        return "Absence de lésions angiographiques au niveau de l'interventriculaire antérieure."
    Cx_report = Cx_stenosis_generator(state, Cx_report)
    Cx_report += Cx_Thrombus_No_stenosis_generator(state)
    Cx_report += Cx_calcification_No_stenosis_generator(state)
    Cx_report += Cx_stent_No_lesion_generator(state)
    remarks = get_remarks(segments)
    Cx_report += f"""({remarks}) """ if len(remarks) > 0 else ""

    return Cx_report
