from src.lib.generate_coronarography.generators.segment_generators.Marg.Marg_Calcification_No_stenosis import (
    Marg_calcification_No_stenosis_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.Marg.Marg_Stent_No_lesion import (
    Marg_stent_No_lesion_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.Marg.Marg_Thrombus_No_stenosis import (
    Marg_Thrombus_No_stenosis_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.Marg.Marg_segments import (
    Marg_segments_parser,
)
from src.lib.generate_coronarography.utils.anomalies_calculator import (
    hole_segment_anomalie_calculator,
    stenotic_with_occlusion_anomalies_calculator,
)
from src.lib.generate_coronarography.utils.coronarography_classes import (
    CoronarySegmentation,
)
from src.lib.generate_coronarography.generators.segment_generators.Marg.Marg_stenosis import (
    Marg_stenosis_generator,
)
from src.lib.generate_coronarography.utils.segment_description import get_remarks


def Marg_generator(state: CoronarySegmentation) -> str:
    Marg_report = ""

    segments = Marg_segments_parser(state)
    all_anomalies = hole_segment_anomalie_calculator(segments)
    lesion_number = stenotic_with_occlusion_anomalies_calculator(segments)

    if lesion_number == 0 and all_anomalies == 0:
        return "Absence de lésions angiographiques au niveau des marginales."
    Marg_report = Marg_stenosis_generator(state, Marg_report)
    Marg_report += Marg_Thrombus_No_stenosis_generator(state)
    Marg_report += Marg_calcification_No_stenosis_generator(state)
    Marg_report += Marg_stent_No_lesion_generator(state)
    remarks = get_remarks(segments)
    Marg_report += f"""({remarks}) """ if len(remarks) > 0 else ""

    return Marg_report
