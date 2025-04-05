from typing import Optional

from fastapi import Request
from src.lib.audio_transcription.audio_types import audio_types

from src.lib.audio_transcription.description_types.KT.KT_EKG.KT_EKG_transcription import (
    KT_EKG_transcription,
)
from src.lib.audio_transcription.description_types.KT.KT_bypass.KT_bypass_transcription import (
    KT_bypass_transcription,
)
from src.lib.audio_transcription.description_types.KT.KT_clinical_exam.KT_clinical_exam_transcription import (
    KT_clinical_exam_transcription,
)
from src.lib.audio_transcription.description_types.KT.KT_diagnostic.KT_diagnostic_transcription import (
    KT_diagnostic_transcription,
)
from src.lib.audio_transcription.description_types.KT.KT_history.KT_history_transcription import (
    KT_history_transcription,
)
from src.lib.audio_transcription.description_types.KT.KT_ischemic_tests.KT_isxchemic_tests_transcription import (
    KT_ischemic_tests_transcription,
)
from src.lib.audio_transcription.description_types.KT.KT_procedure_prescription.KT_procedure_prescription_transcription import (
    KT_procedure_prescription_transcription,
)
from src.lib.audio_transcription.description_types.generic_description import (
    generic_description,
)


def generate_transcription(
    request: Request, audio_transcription: str, type: Optional[audio_types] = None
):

    match type:
        case "KT_clinical_exam":
            return KT_clinical_exam_transcription(request, audio_transcription)
        case "KT_diagnostic":
            return KT_diagnostic_transcription(request, audio_transcription)
        case "KT_history":
            return KT_history_transcription(request, audio_transcription)

        case "KT_ECG":
            return KT_EKG_transcription(request, audio_transcription)

        case "KT_ischemic_test":
            return KT_ischemic_tests_transcription(request, audio_transcription)
        case "KT_bypass":
            return KT_bypass_transcription(request, audio_transcription)
        case "KT_procedure_prescription":
            return KT_procedure_prescription_transcription(request, audio_transcription)

        case "generic":
            return generic_description(audio_transcription)

        case _:
            return generic_description(audio_transcription)

    pass
