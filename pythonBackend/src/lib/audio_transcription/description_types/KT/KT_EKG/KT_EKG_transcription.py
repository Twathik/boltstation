from fastapi import Request


from src.lib.audio_transcription.description_types.KT.KT_EKG.KT_EKG_prompt import (
    KT_EKG_system_prompt,
)
from src.lib.audio_transcription.generic_ollama_request import (
    generic_ollama_report_formater,
)


def KT_EKG_transcription(request: Request, audio_transcription: str):
    print(audio_transcription)
    return generic_ollama_report_formater(
        request,
        system_prompt=KT_EKG_system_prompt,
        raw_report=audio_transcription,
    )
