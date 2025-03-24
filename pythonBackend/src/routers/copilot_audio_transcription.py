import tempfile
from typing import Optional
from fastapi import (
    APIRouter,
    BackgroundTasks,
    Depends,
    File,
    HTTPException,
    UploadFile,
)

from src.lib.ai_document.Audio_file_transcription import audio_file_transcription
import os
import shutil
from contextlib import asynccontextmanager
from src.lib.get_auth_token import get_auth_token
import jwt
import ffmpeg
from dotenv import load_dotenv

load_dotenv()

cwd = os.getcwd

router = APIRouter()

JWT_Secret = os.getenv("JWT_SECRET")


@asynccontextmanager
async def temporary_directory(custom_dir: str):
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp(dir=custom_dir)
    try:
        # Yield the directory path for use in the response
        yield temp_dir
    finally:
        pass


@router.post("/")
async def copilot_audio_transcription(
    background_tasks: BackgroundTasks,
    audio: Optional[UploadFile] = File(...),  # Receive as file
    token: str = Depends(get_auth_token),
):

    if not audio:
        raise HTTPException(status_code=422, detail="Unsuported request")
    personalChanelId = None
    try:
        decoded_data = jwt.decode(token, JWT_Secret, algorithms=["HS256"])
        personalChanelId = decoded_data["personalChanelId"]

        pass
    except Exception as e:
        print(f"Error processing request: {e}")
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to access this resource.",
        )

    cwd = os.getcwd()
    custom_dir = os.path.join(cwd, "generated")
    # Ensure the custom directory exists
    os.makedirs(custom_dir, exist_ok=True)

    audio_transcription = ""
    try:
        async with temporary_directory(custom_dir=custom_dir) as temp_dir:
            if audio:
                audio_filename = os.path.join(temp_dir, f"uploaded_{audio.filename}")
                with open(audio_filename, "wb") as audio_file:
                    audio_file.write(await audio.read())
                    try:
                        (
                            ffmpeg.input(audio_filename)
                            .output(
                                audio_filename.replace(".m4a", ".mp3"),
                                format="mp3",
                                ar="44100",
                                ac="2",
                                audio_bitrate="192k",
                            )
                            .global_args(
                                "-loglevel", "error"
                            )  # ✅ Suppresses debug logs
                            .run(overwrite_output=True)
                        )

                    except ffmpeg.Error as e:
                        print("FFmpeg Error:", e.stderr.decode())

                audio_transcription = audio_file_transcription(
                    audio_filename.replace(".m4a", ".mp3")
                )
            background_tasks.add_task(lambda: shutil.rmtree(temp_dir))

        return {"message": "Request completed", "transcription": audio_transcription}

    except Exception as e:
        print(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
