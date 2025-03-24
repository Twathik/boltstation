from src.lib.generate_coronarography.generators.segment_generators.Bisec.Bisec_generator import (
    Bisec_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.CD.CD_generator import (
    CD_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.CX.Cx_generator import (
    Cx_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.Diag.Diag_generator import (
    Diag_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.IVPL.IVPL_generator import (
    IVPL_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.IVPR.IVPR_generator import (
    IVPR_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.LAD.LAD_generator import (
    LAD_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.Marg.Marg_generator import (
    Marg_generator,
)

from src.lib.generate_coronarography.generators.segment_generators.LM.LM_generator import (
    LM_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.RVG.RVG_generator import (
    RVG_generator,
)
from src.lib.generate_coronarography.generators.segment_generators.Sept.Sept_generator import (
    Sept_generator,
)
from src.lib.generate_coronarography.utils.coronarography_classes import (
    CoronarySegmentation,
)


def report_generator(state: CoronarySegmentation) -> str:
    return f"""
    ## **Reseau coronaire gauche:**
    - **Tronc Commun gauche: **{LM_generator(state)}
    - **Interventriculaire anterieure: **{LAD_generator(state)}. {Diag_generator(state)}. {Sept_generator(state)}
    - **Artère circonflex: **{Cx_generator(state)}. {Marg_generator(state)}. {IVPL_generator(state)}.
    - **Artère bisectrice: **:{Bisec_generator(state)}
    
    ## **Reseau coronaire droit:**
    - **Coronaire droite: **{CD_generator(state)}
    - **Interventriculaire posterieur (IVP): **{IVPR_generator(state)}
    - **Rétroventriculaire gauche (RVG): **{RVG_generator(state)}
    """
