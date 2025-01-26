import asyncio
from langchain.schema import HumanMessage, AIMessage
from typing import Any, Optional

from langchain_ollama import OllamaLLM
from ulid import ULID
from llm_queue_utils.publish_chunck_utils.widgets_prompts.widget_prompts_root import (
    widget_prompts,
)
from websocketTypes.general_classes import OperationEnum, SexeEnum
from langchain.schema import HumanMessage, SystemMessage
from websocketTypes.publish_temporary_chanel_message import publish_message
from websocketTypes.temporary_chanel_message_class import TemporaryMessageType


async def generate_ai(
    temporaryChanelId: str,
    llm: OllamaLLM,
    content: str,
    sex: SexeEnum,
    target_message_Id: str,
    chunk: Optional[Any] = None,
):

    if chunk["widgetId"] in widget_prompts:
        system_prompt = widget_prompts.get(chunk["widgetId"])

        message = [
            SystemMessage(content=system_prompt),
            HumanMessage(
                content=f"""
                <MedicalObservation>
                {content}
                </MedicalObservation>
                <Sex>{'female' if sex == SexeEnum.F else 'male'}</Sex>
            """
            ),
        ]

    else:
        await asyncio.sleep(0.1)
        publish_message(
            temporaryChanelId=temporaryChanelId,
            operation=OperationEnum.publish,
            content=chunk,
            type=TemporaryMessageType.payload,
        )
        return None

    stream = llm.stream(message)
    chunk_count = 0
    chunk_agg = ""

    for c in stream:
        if False:
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
                        {"id": str(ULID()), "text": chunk_agg},
                    ],
                    "id": target_message_Id,
                    "type": "p",
                    "widgetId": chunk["widgetId"],
                    "widgetName": chunk["widgetName"],
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
                {"id": str(ULID()), "text": chunk_agg},
            ],
            "id": target_message_Id,
            "type": "p",
            "widgetId": chunk["widgetId"],
            "widgetName": chunk["widgetName"],
        },
        type=TemporaryMessageType.chunk,
    )

    return None
