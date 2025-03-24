from fastapi import Request


from src.lib.audio_transcription.description_types.KT.KT_history.KT_history_prompt import (
    KT_history_system_prompt,
)
from src.lib.audio_transcription.generic_ollama_request import (
    generic_ollama_report_formater,
)


def KT_history_transcription(request: Request, audio_transcription: str):
    print(audio_transcription)
    return generic_ollama_report_formater(
        request,
        system_prompt=KT_history_system_prompt,
        raw_report=audio_transcription,
    )
