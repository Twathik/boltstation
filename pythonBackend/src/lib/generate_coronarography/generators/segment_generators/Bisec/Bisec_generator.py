from src.lib.generate_coronarography.generators.segment_generators.Bisec.Bisec_Calcification_No_stenosis import (
    Bisec_calcification_No_stenosis_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.Bisec.Bisec_Stent_No_lesion import (
    Bisec_stent_No_lesion_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.Bisec.Bisec_Thrombus_No_stenosis import (
    Bisec_Thrombus_No_stenosis_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.Bisec.Bisec_segments import (
    Bisec_segments_parser,
)
from src.lib.generate_coronarography.generators.segment_generators.Bisec.Bisec_stenosis import (
    Bisec_stenosis_generator,
)
from src.lib.generate_coronarography.utils.anomalies_calculator import (
    hole_segment_anomalie_calculator,
    stenotic_with_occlusion_anomalies_calculator,
)
from src.lib.generate_coronarography.utils.coronarography_classes import (
    CoronarySegmentation,
)

from src.lib.generate_coronarography.utils.segment_description import get_remarks


def Bisec_generator(state: CoronarySegmentation) -> str:
    Bisec_report = ""

    segments = Bisec_segments_parser(state)
    all_anomalies = hole_segment_anomalie_calculator(segments)
    lesion_number = stenotic_with_occlusion_anomalies_calculator(segments)

    if lesion_number == 0 and all_anomalies == 0:
        return "Absence de lésions angiographiques au niveau des diagonales."
    Bisec_report = Bisec_stenosis_generator(state, Bisec_report)
    Bisec_report += Bisec_Thrombus_No_stenosis_generator(state)
    Bisec_report += Bisec_calcification_No_stenosis_generator(state)
    Bisec_report += Bisec_stent_No_lesion_generator(state)
    remarks = get_remarks(segments)
    Bisec_report += f"""({remarks}) """ if len(remarks) > 0 else ""

    return Bisec_report
