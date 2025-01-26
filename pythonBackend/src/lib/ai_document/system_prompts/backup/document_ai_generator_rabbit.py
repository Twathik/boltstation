import asyncio
import json
import queue
import time
from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, Request
from langchain_ollama import OllamaLLM
from pydantic import BaseModel
import requests
import os

from ulid import ULID

from src.lib.ai_document.extract_numerical_values import extract_numerical_values
from src.lib.ai_document.utils.check_if_contains_number_input import (
    check_if_contains_number_input,
)
from src.lib.ai_document.generate_ai_content import generate_ai
from src.lib.ai_document.utils.queue_names import publish_chunk, PUBLISH_CHUNK_EXCHANGE
from src.lib.rabbitMq.connection import RabbitMQManager
from src.lib.websocketTypes.general_classes import OperationEnum, SexeEnum
from src.lib.websocketTypes.publish_temporary_chanel_message import publish_message
from src.lib.websocketTypes.temporary_chanel_message_class import (
    TemporaryMessageType,
)
from pprintpp import pprint
from dotenv import load_dotenv

load_dotenv()


router = APIRouter()
sleep_time = 0.02


class Document(BaseModel):
    clinicalEventId: str
    content: str
    temporaryChanelId: str
    economizerFormattedTemplate: List[Any]
    sex: SexeEnum


@router.post("/")
async def document_ai_generator(
    request: Request, Document: Document, rabbitmq: RabbitMQManager = Depends()
):

    cookies = request.cookies
    cwd = os.getcwd()

    auth_url = "http://api.bolt.local/auth/user"

    response = requests.get(auth_url, cookies=cookies)
    if not response.status_code == 200:
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to access this resource.",
        )
    user = response.json()
    start_time = time.time()
    try:
        llm = OllamaLLM(
            model=os.getenv("AI_model"),
            # model="phi4:latest",
            temperature=0.2,
            # other params...
        )

        extracted_data: List[str] = []
        ai_document_List: List[dict] = []
        numerical_values_list: List[dict] = []

        # Simulate long processing
        for i in range(len(Document.economizerFormattedTemplate)):
            chunk = Document.economizerFormattedTemplate[i]
            # Check if the client has disconnected
            if await request.is_disconnected():
                print("Client disconnected!")
                return {"message": "Request aborted by client"}

            publish_message(
                temporaryChanelId=Document.temporaryChanelId,
                operation=OperationEnum.publish,
                content=chunk.get("widgetName", ""),
                type=TemporaryMessageType.milestone,
            )
            number_input = check_if_contains_number_input(chunk)

            # pprint(chunk, depth=5, width=80)
            if chunk.get("AIgenerated", False) == True:
                pass
            if chunk.get("AiTarget", False) == True:

                await asyncio.sleep(sleep_time)
                publish_message(
                    temporaryChanelId=Document.temporaryChanelId,
                    operation=OperationEnum.publish,
                    content=chunk,
                    type=TemporaryMessageType.payload,
                )

                await asyncio.sleep(sleep_time)
                message_id = str(ULID())
                print("this is the message id", message_id)
                publish_message(
                    temporaryChanelId=Document.temporaryChanelId,
                    operation=OperationEnum.publish,
                    content={
                        "AiTarget": False,
                        "AIgenerated": True,
                        "children": [
                            {"id": str(ULID()), "text": "En cours de géneration ..."},
                        ],
                        "id": message_id,
                        "type": "p",
                        "widgetId": chunk["widgetId"],
                        "widgetName": chunk["widgetName"],
                    },
                    type=TemporaryMessageType.chunk,
                )
                ai_document_List.append(
                    {"chunk": chunk, "target_message_Id": message_id}
                )
                pass
            else:
                if number_input.check == True:

                    await asyncio.sleep(sleep_time)
                    publish_message(
                        temporaryChanelId=Document.temporaryChanelId,
                        operation=OperationEnum.publish,
                        content=chunk,
                        type=TemporaryMessageType.payload,
                    )
                    numerical_values_list.append(chunk)
                    pass
                else:
                    await asyncio.sleep(sleep_time)
                    publish_message(
                        temporaryChanelId=Document.temporaryChanelId,
                        operation=OperationEnum.publish,
                        content=chunk,
                        type=TemporaryMessageType.payload,
                    )
                    pass

        for ai_chunk in ai_document_List:
            body = {
                **ai_chunk,
                "temporaryChanelId": Document.temporaryChanelId,
                "content": Document.content,
                "sex": Document.sex,
            }

            rabbitmq.publish_message(
                exchange=PUBLISH_CHUNK_EXCHANGE,
                routing_key="chunk",
                body=json.dumps(body),
                queue=publish_chunk,
            )
            pass

        """ await generate_ai(
            chunk=None,
            temporaryChanelId=Document.temporaryChanelId,
            llm=llm,
            request=request,
            final_remarks=True,
            extracted_data=extracted_data,
            content=Document.content,
            sex=Document.sex,
        ) """
        end_time = time.time()
        exec_time = end_time - start_time
        print("execussion time", exec_time)
        return {"message": "Request completed", "data": Document}

    except Exception as e:
        print(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
