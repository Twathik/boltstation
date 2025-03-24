import tempfile
from typing import Literal, Optional
from fastapi import (
    APIRouter,
    BackgroundTasks,
    File,
    Form,
    HTTPException,
    Request,
    UploadFile,
)

import requests

from src.lib.ai_document.Audio_file_transcription import audio_file_transcription
import os
import shutil
from contextlib import asynccontextmanager

from src.lib.audio_transcription.audio_types import audio_types
from src.lib.audio_transcription.generate_audio_transcription import (
    generate_transcription,
)

cwd = os.getcwd

router = APIRouter()


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
async def audio_transcription(
    background_tasks: BackgroundTasks,
    request: Request,
    audio_type: audio_types = Form(...),
    audio: Optional[UploadFile] = File(...),
):
    cookies = request.cookies

    auth_url = "http://api.bolt.local/auth/user"

    response = requests.get(auth_url, cookies=cookies)
    if not response.status_code == 200:
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to access this resource.",
        )
    user = response.json()
    # pprint(user, indent=5)
    cwd = os.getcwd()
    custom_dir = os.path.join(cwd, "generated")
    # Ensure the custom directory exists
    os.makedirs(custom_dir, exist_ok=True)

    audio_transcription = ""
    try:
        async with temporary_directory(custom_dir=custom_dir) as temp_dir:
            if audio:
                audio_filename = os.path.join(
                    temp_dir, f"uploaded_{audio.filename}.webm"
                )
                with open(audio_filename, "wb") as audio_file:
                    audio_file.write(await audio.read())
                    audio_transcription = audio_file_transcription(audio_filename)
            background_tasks.add_task(lambda: shutil.rmtree(temp_dir))

            print(type)

        return generate_transcription(request, audio_transcription, type=audio_type)

    except Exception as e:
        print(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
