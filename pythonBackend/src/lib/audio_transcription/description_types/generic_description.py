from fastapi.responses import StreamingResponse


def generic_description(audio_transcription: str):
    return StreamingResponse(audio_transcription, media_type="text/plain")
