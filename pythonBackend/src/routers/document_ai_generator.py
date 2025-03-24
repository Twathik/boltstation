import asyncio
import json
import shutil
import tempfile
import time
from typing import Any, List, Optional
from fastapi import (
    APIRouter,
    BackgroundTasks,
    File,
    Form,
    HTTPException,
    Request,
    UploadFile,
)
from fastapi.concurrency import asynccontextmanager
from langchain_ollama import OllamaLLM
from pydantic import BaseModel
import requests
import os

from src.lib.ai_document.extract_numerical_values import extract_numerical_values
from src.lib.ai_document.inject_data import inject_data
from src.lib.ai_document.utils.check_if_contains_number_input import (
    check_if_contains_number_input,
)
from src.lib.ai_document.generate_ai_content import generate_ai
from src.lib.websocketTypes.general_classes import OperationEnum, SexeEnum
from src.lib.websocketTypes.publish_temporary_chanel_message import publish_message
from src.lib.websocketTypes.temporary_chanel_message_class import (
    TemporaryMessageType,
)
from src.lib.ai_document.Audio_file_transcription import audio_file_transcription
from dotenv import load_dotenv

load_dotenv()

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


class Document(BaseModel):
    clinicalEventId: str
    content: str
    temporaryChanelId: str
    economizerFormattedTemplate: List[Any]
    sex: SexeEnum


@router.post("/")
async def document_ai_generator(
    background_tasks: BackgroundTasks,
    request: Request,
    clinicalEventId: str = Form(...),
    content: str = Form(...),
    temporaryChanelId: str = Form(...),
    economizerFormattedTemplate: str = Form(...),  # JSON string
    sex: SexeEnum = Form(...),
    audio: Optional[UploadFile] = File(None),
):
    cookies = request.cookies
    document_data = Document(
        clinicalEventId=clinicalEventId,
        content=content,
        temporaryChanelId=temporaryChanelId,
        economizerFormattedTemplate=json.loads(economizerFormattedTemplate),
        sex=sex,
    )
    cwd = os.getcwd()
    custom_dir = os.path.join(cwd, "generated")
    # Ensure the custom directory exists
    os.makedirs(custom_dir, exist_ok=True)
    audio_transcription = ""
    async with temporary_directory(custom_dir=custom_dir) as temp_dir:
        if audio:
            audio_filename = os.path.join(temp_dir, f"uploaded_{audio.filename}.webm")
            with open(audio_filename, "wb") as audio_file:
                audio_file.write(await audio.read())
                audio_transcription = audio_file_transcription(audio_filename)
        background_tasks.add_task(lambda: shutil.rmtree(temp_dir))
    document_data.content = f"""{document_data.content}
    {audio_transcription}
    """
    auth_url = "http://api.bolt.local/auth/user"

    response = requests.get(auth_url, cookies=cookies)
    if not response.status_code == 200:
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to access this resource.",
        )
    user = response.json()

    start_time = time.time()
    list_of_descriptions = []

    try:
        llm = OllamaLLM(
            # model=os.getenv("AI_model"),
            model="gemma2:27b",
            # model="phi4:latest",
            temperature=0.2,
            # other params...
        )

        extracted_data: List[str] = []
        extracted_descriptions = []
        extracted_values = []
        document: List[Any] = []
        extracted_json: dict = {}

        for ck in document_data.economizerFormattedTemplate:
            await inject_data(
                document=document,
                chunk=ck,
                clinicalEventId=clinicalEventId,
                extracted_data=extracted_data,
            )

        # Simulate long processing
        for i in range(len(document)):
            chunk = document[i]

            # Check if the client has disconnected
            if await request.is_disconnected():
                print("Client disconnected!")
                return {"message": "Request aborted by client"}

            # Simulate work (e.g., database call, heavy computation)
            publish_message(
                temporaryChanelId=document_data.temporaryChanelId,
                operation=OperationEnum.publish,
                content=chunk.get("widgetName", ""),
                type=TemporaryMessageType.milestone,
            )
            number_input = check_if_contains_number_input(chunk)

            # pprint(chunk, depth=5, width=80)
            if chunk.get("AIgenerated", False) == True:
                pass
            if chunk.get("AiTarget", False) == True:
                await asyncio.sleep(0.1)
                publish_message(
                    temporaryChanelId=document_data.temporaryChanelId,
                    operation=OperationEnum.publish,
                    content=chunk,
                    type=TemporaryMessageType.payload,
                )

                generate = await generate_ai(
                    chunk=chunk,
                    temporaryChanelId=document_data.temporaryChanelId,
                    llm=llm,
                    request=request,
                    final_remarks=False,
                    extracted_data=extracted_data,
                    content=document_data.content,
                    sex=document_data.sex,
                )
                if not generate == None:
                    return generate

            else:

                if number_input.check == True:
                    publish_message(
                        temporaryChanelId=document_data.temporaryChanelId,
                        operation=OperationEnum.publish,
                        content=chunk,
                        type=TemporaryMessageType.payload,
                    )
                    extract_numerical_values(
                        content=document_data.content,
                        extracted_data=extracted_data,
                        llm=llm,
                        number_inputs=number_input.number_inputs,
                        temporaryChanelId=document_data.temporaryChanelId,
                        extracted_values=extracted_values,
                    )
                    for input in number_input.number_inputs:
                        extracted_descriptions.append(
                            {
                                "name": input.input_name,
                                "description": input.input_description,
                            }
                        )
                        pass
                    pass
                else:
                    await asyncio.sleep(0.1)
                    publish_message(
                        temporaryChanelId=document_data.temporaryChanelId,
                        operation=OperationEnum.publish,
                        content=chunk,
                        type=TemporaryMessageType.payload,
                    )
                    pass

            print(i)
        # Write dictionary to a JSON file
        with open("extracted_descriptions.json", "w", encoding="utf-8") as file:
            json.dump(extracted_descriptions, file, indent=4, ensure_ascii=False)

        with open("extracted_values.json", "w", encoding="utf-8") as file:
            json.dump(extracted_values, file, indent=4, ensure_ascii=False)

        await generate_ai(
            chunk=None,
            temporaryChanelId=document_data.temporaryChanelId,
            llm=llm,
            request=request,
            final_remarks=True,
            extracted_data=extracted_data,
            content=document_data.content,
            sex=document_data.sex,
        )
        end_time = time.time()
        exec_time = end_time - start_time
        print("execussion time", exec_time)
        return {"message": "Request completed", "data": document_data}

    except Exception as e:
        print(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
