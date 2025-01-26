from typing import List
from llm_queue_utils.publish_chunck_utils.widgets_prompts.examen_clinique.signes_generaux import (
    signes_generaux_widget,
)
from llm_queue_utils.publish_chunck_utils.widgets_prompts.examen_clinique.signes_fonctionnels_cardiovasculaires import (
    signes_fonctionnels_cardiovasculaires_widget,
)

from llm_queue_utils.publish_chunck_utils.widgets_prompts.examen_clinique.signes_fonctionnels_autre import (
    autre_symptomes_widget,
)
from llm_queue_utils.publish_chunck_utils.widgets_prompts.examen_clinique.Examen_vasculaire_perepherique import (
    Examen_vasculaire_perepherique_widget,
)
from llm_queue_utils.publish_chunck_utils.widgets_prompts.examen_clinique.examen_respiratoire import (
    examen_respiratoire_widget,
)
from llm_queue_utils.publish_chunck_utils.widgets_prompts.examen_clinique.auscultation import (
    auscultation_widget,
)

from llm_queue_utils.publish_chunck_utils.widgets_prompts.examen_clinique.antecedents import (
    antecedents_widget,
)
from llm_queue_utils.publish_chunck_utils.widgets_prompts.ECG.analyse_rythme import (
    ECG_analyse_rythme_widget,
)
from llm_queue_utils.publish_chunck_utils.widgets_prompts.ECG.auriculogramme import (
    ECG_auriculogramme_widget,
)
from llm_queue_utils.publish_chunck_utils.widgets_prompts.ECG.ventriculogramme import (
    ECG_ventriculogramme_widget,
)
from llm_queue_utils.publish_chunck_utils.widgets_prompts.ECG.espace_PR import (
    ECG_espace_PR_widget,
)
from llm_queue_utils.publish_chunck_utils.widgets_prompts.ECG.segment_ST import (
    ECG_segment_ST_widget,
)
from llm_queue_utils.publish_chunck_utils.widgets_prompts.ECG.segment_QT import (
    ECG_segment_QT_widget,
)
from llm_queue_utils.publish_chunck_utils.widgets_prompts.examen_clinique.donnee_ecg import (
    donnee_ecg_widget,
)
from llm_queue_utils.publish_chunck_utils.widgets_prompts.ETT.oreillettes import (
    ETT_Oreillettes_widget,
)
from llm_queue_utils.publish_chunck_utils.widgets_prompts.ETT.Aorte import (
    ETT_Aorte_widget,
)
from llm_queue_utils.publish_chunck_utils.widgets_prompts.ETT.CIA import (
    ETT_CIA_widget,
)
from llm_queue_utils.publish_chunck_utils.widgets_prompts.ETT.CIV import (
    ETT_CIV_widget,
)
from llm_queue_utils.publish_chunck_utils.widgets_prompts.ETT.fonction_VD import (
    ETT_fonction_VD_widget,
)
from llm_queue_utils.publish_chunck_utils.widgets_prompts.ETT.fonction_VG import (
    ETT_fonction_VG_widget,
)
from llm_queue_utils.publish_chunck_utils.widgets_prompts.ETT.HTP import (
    ETT_HTP_widget,
)
from llm_queue_utils.publish_chunck_utils.widgets_prompts.ETT.IAO import (
    ETT_IAO_widget,
)
from llm_queue_utils.publish_chunck_utils.widgets_prompts.ETT.IM import (
    ETT_IM_widget,
)
from llm_queue_utils.publish_chunck_utils.widgets_prompts.ETT.IP import (
    ETT_IP_widget,
)
from llm_queue_utils.publish_chunck_utils.widgets_prompts.ETT.IT import (
    ETT_IT_widget,
)
from llm_queue_utils.publish_chunck_utils.widgets_prompts.ETT.prothese_aortique import (
    ETT_prothese_aortique_widget,
)
from llm_queue_utils.publish_chunck_utils.widgets_prompts.ETT.prothese_mitrale import (
    ETT_prothese_mitrale_widget,
)
from llm_queue_utils.publish_chunck_utils.widgets_prompts.ETT.RAO import (
    ETT_RAO_widget,
)
from llm_queue_utils.publish_chunck_utils.widgets_prompts.ETT.RM import (
    ETT_RM_widget,
)
from llm_queue_utils.publish_chunck_utils.widgets_prompts.ETT.RP import (
    ETT_RP_widget,
)
from llm_queue_utils.publish_chunck_utils.widgets_prompts.ETT.RT import (
    ETT_RT_widget,
)
from llm_queue_utils.publish_chunck_utils.widgets_prompts.ETT.Shunts import (
    ETT_Shunts_widget,
)
from llm_queue_utils.publish_chunck_utils.widgets_prompts.ETT.VCI import (
    ETT_VCI_widget,
)

widget_prompts: dict = {
    "01JH5W1TD1C2KR64MREYY1EQRD": signes_generaux_widget,  #
    "01JH5W1W46ZS5FC4TFXMAPN6N1": signes_fonctionnels_cardiovasculaires_widget,
    "01JH5YJQ7ZCM5ZMX83MGKTSMH6": autre_symptomes_widget,
    "01JH5W2BJMG7JVG739P67SV94Q": Examen_vasculaire_perepherique_widget,
    "01JH5W2DZ0FSACWWADN1N0KRGM": examen_respiratoire_widget,
    "01JH5YJTPF57W0DN953XBHGNA0": auscultation_widget,
    "01JH5YJY7E0KNYSC9G5CZNM5HK": antecedents_widget,
    "01JH5YK0B99KVE8BPK9FPVEEYV": ECG_analyse_rythme_widget,
    "01JH5YJWERKQ56NMPAEM4CE30F": ECG_auriculogramme_widget,
    "01JH5W0DAC3WCF9J7ZV4622XRP": ECG_ventriculogramme_widget,  #
    "01JH5YJFS6FQ63ZBNPSDTE2557": ECG_espace_PR_widget,
    "01JH5W20XSATVKHQS7YE1SYTP2": ECG_segment_ST_widget,
    "01JH5W1YENRZX8DTGVM24Z4Q5Y": ECG_segment_QT_widget,
    "01JH5YJHG6KNM6D5VH295YQY0F": donnee_ecg_widget,
    "01JH5YJBPSSP8MH2RDXPP7MQ06": ETT_Oreillettes_widget,
    "01JH5YJ9Z1RRYD671FYMTC1976": ETT_Aorte_widget,
    "01JH5YJ0N8VSN5NFJM6XJBYGQQ": ETT_CIA_widget,
    "01JH5YHYBRQC2V6P1SVWNGQ6C9": ETT_CIV_widget,
    "01JH5YJ7RQBASA1E0H2MYDWDFW": ETT_fonction_VD_widget,
    "01JH5W29SYRK8DJ3E4JZWX0C34": ETT_fonction_VG_widget,
    "01JH5YJ5WZMC6W5CQPRA61NHMH": ETT_HTP_widget,
    "01JH5YHRKFYVC5NFRC7XNZNPFB": ETT_IAO_widget,
    "01JH5YHPVQFCD3337DD50HP86H": ETT_IM_widget,
    "01JH5YHMVNTP0QW0RZQRXG5QJ7": ETT_IP_widget,
    "01JH60Z2WADN98FZ2P72YEQ9C9": ETT_IT_widget,
    "01JH611BZV0AKY74F8MG6FP2A6": ETT_prothese_aortique_widget,
    "01JH612TTVFGV1BK6JGBTY054K": ETT_prothese_mitrale_widget,
    "01JH614EGEGH1DPTBHZ62E1ZY7": ETT_RAO_widget,
    "01JH617K1AA6V67RMC71HA0PWC": ETT_RM_widget,
    "1JH6199TCA0Q8T2X312AKH7Q9": ETT_RP_widget,
    "01JH61AT2NPSFGHA1J7SN3CH62": ETT_RT_widget,
    "01JH61D6HJG8W5232BKEV7AS0M": ETT_Shunts_widget,
    "01JH61F6P7SBB8XKCYGXP0XZ1Y": ETT_VCI_widget,
}
