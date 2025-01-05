from typing import List
from src.lib.ai_document.system_prompts.french.widgets_prompts.examen_clinique.signes_generaux import (
    signes_generaux_widget,
)
from src.lib.ai_document.system_prompts.french.widgets_prompts.examen_clinique.signes_fonctionnels_cardiovasculaires import (
    signes_fonctionnels_cardiovasculaires_widget,
)

from src.lib.ai_document.system_prompts.french.widgets_prompts.examen_clinique.signes_fonctionnels_autre import (
    autre_symptomes_widget,
)
from src.lib.ai_document.system_prompts.french.widgets_prompts.examen_clinique.Examen_vasculaire_perepherique import (
    Examen_vasculaire_perepherique_widget,
)
from src.lib.ai_document.system_prompts.french.widgets_prompts.examen_clinique.examen_respiratoire import (
    examen_respiratoire_widget,
)
from src.lib.ai_document.system_prompts.french.widgets_prompts.examen_clinique.auscultation import (
    auscultation_widget,
)

from src.lib.ai_document.system_prompts.french.widgets_prompts.examen_clinique.antecedents import (
    antecedents_widget,
)
from src.lib.ai_document.system_prompts.french.widgets_prompts.ECG.analyse_rythme import (
    ECG_analyse_rythme_widget,
)
from src.lib.ai_document.system_prompts.french.widgets_prompts.ECG.auriculogramme import (
    ECG_auriculogramme_widget,
)
from src.lib.ai_document.system_prompts.french.widgets_prompts.ECG.ventriculogramme import (
    ECG_ventriculogramme_widget,
)
from src.lib.ai_document.system_prompts.french.widgets_prompts.ECG.espace_PR import (
    ECG_espace_PR_widget,
)
from src.lib.ai_document.system_prompts.french.widgets_prompts.ECG.segment_ST import (
    ECG_segment_ST_widget,
)
from src.lib.ai_document.system_prompts.french.widgets_prompts.ECG.segment_QT import (
    ECG_segment_QT_widget,
)

widget_prompts: dict = {
    "01JF871FEKE6DAFX1TDYX20DJ9": signes_generaux_widget,
    "01JFMF1QBKA5J2ZG27QCJW40ES": signes_fonctionnels_cardiovasculaires_widget,
    "01JGKNA9XB1SAYTC73NYKEM9G4": autre_symptomes_widget,
    "01JF8ATGYHDZ4R0GR4AMAQPE4B": Examen_vasculaire_perepherique_widget,
    "01JF8AB732DHCX69CFAHHP37TK": examen_respiratoire_widget,
    "01JF8A6H3H79DHW294BF32GQQS": auscultation_widget,
    "01JF3BDJJDQ0AA9WNM203A3P88": antecedents_widget,
    "01JGTX65TYNS43FD3NH9ETD5AW": ECG_analyse_rythme_widget,
    "01JGV0994FBRBRA9CPCPP1S7CQ": ECG_auriculogramme_widget,
    "01JGV5GGSN9AN6V7GS8ZS9RBN4": ECG_ventriculogramme_widget,
    "01JGVP9DE5YAJX7T1JMBZYC9RQ": ECG_espace_PR_widget,
    "01JGVR7YYBMM44H64SY07RP058": ECG_segment_ST_widget,
    "01JGVS3WGCGYVZA4SGYMD8MQTR": ECG_segment_QT_widget,
}
