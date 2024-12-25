from langchain.schema import HumanMessage, AIMessage
from typing import Any, List, Optional
from fastapi import Request
from langchain_ollama import OllamaLLM
from ulid import ULID
from src.lib.websocketTypes.general_classes import OperationEnum, SexeEnum
from src.lib.websocketTypes.publish_temporary_chanel_message import publish_message
from src.lib.websocketTypes.temporary_chanel_message_class import TemporaryMessageType

from pprintpp import pprint
from src.lib.typesense.typesense_client import typesense_client
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from src.lib.ai_document.system_prompts.generate_ai_document_system_message import (
    generate_ai_document_system_message,
)
from src.lib.ai_document.system_prompts.get_delta_content_system_message import (
    get_delta_content_system_message,
)


async def generate_ai(
    temporaryChanelId: str,
    llm: OllamaLLM,
    request: Request,
    final_remarks: bool,
    extracted_data: List[str],
    content: str,
    sex: SexeEnum,
    chunk: Optional[Any] = None,
):
    if final_remarks == True:

        message = [
            SystemMessage(content=get_delta_content_system_message),
            HumanMessage(
                content=f"""<MedicalObservation>{content}</MedicalObservation><Sex>{'female' if sex == SexeEnum.F else 'male'}</Sex><ExtractedData>{' '.join(extracted_data)}</ExtractedData>"""
            ),
        ]
    else:

        widget = (
            typesense_client.collections["patient-widget-data"]
            .documents[chunk["widgetId"]]
            .retrieve()
        )
        message = [
            SystemMessage(content=generate_ai_document_system_message),
            HumanMessage(
                content=f"""<MedicalObservation>{content}</MedicalObservation><Sex>{'female' if sex == SexeEnum.F else 'male'}</Sex><Description>{widget["description"]}</Description>
            """
            ),
        ]

    stream = llm.stream(message)
    chunk_count = 0
    chunk_agg = ""
    message_id = str(ULID())
    for c in stream:
        if await request.is_disconnected():
            print("Client disconnected!")
            return {"message": "Request aborted by client"}

        chunk_agg += c
        if chunk_count == 20:
            publish_message(
                temporaryChanelId=temporaryChanelId,
                operation=OperationEnum.publish,
                content={
                    "AiTarget": False,
                    "AIgenerated": True,
                    "children": [
                        {
                            "id": str(ULID()),
                            "text": (
                                f"remarques: {chunk_agg}"
                                if final_remarks
                                else chunk_agg
                            ),
                        },
                    ],
                    "id": message_id,
                    "type": "p",
                    "widgetId": (chunk["widgetId"] if final_remarks == False else ""),
                    "widgetName": (
                        chunk["widgetName"] if final_remarks == False else ""
                    ),
                },
                type=TemporaryMessageType.chunk,
            )
            chunk_count = 0
        else:
            chunk_count += 1

    publish_message(
        temporaryChanelId=temporaryChanelId,
        operation=OperationEnum.publish,
        content={
            "AiTarget": False,
            "AIgenerated": True,
            "children": [
                {
                    "id": str(ULID()),
                    "text": (
                        f"""Remarques: 
{chunk_agg}"""
                        if final_remarks
                        else chunk_agg
                    ),
                },
            ],
            "id": message_id,
            "type": "p",
            "widgetId": (chunk["widgetId"] if final_remarks == False else ""),
            "widgetName": (chunk["widgetName"] if final_remarks == False else ""),
        },
        type=TemporaryMessageType.chunk,
    )
    if final_remarks == False:
        extracted_data.append(
            f"""
        {chunk_agg}"""
        )
    return None
