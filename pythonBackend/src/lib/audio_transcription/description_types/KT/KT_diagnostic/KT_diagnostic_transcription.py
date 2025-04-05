from fastapi import Request


from src.lib.audio_transcription.description_types.KT.KT_diagnostic.KT_diagnostic_prompt import (
    KT_diagnostic_system_prompt,
)
from src.lib.audio_transcription.generic_ollama_request import (
    generic_ollama_report_formater,
)


def KT_diagnostic_transcription(request: Request, audio_transcription: str):

    return generic_ollama_report_formater(
        request,
        system_prompt=KT_diagnostic_system_prompt,
        raw_report=audio_transcription,
    )
