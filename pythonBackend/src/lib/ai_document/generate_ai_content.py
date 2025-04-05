import asyncio
from typing import Any, List, Optional
from fastapi import Request
from langchain_ollama import OllamaLLM
from langchain.schema import HumanMessage, SystemMessage
from pprintpp import pprint
from ulid import ULID

from src.lib.ai_document.inject_data import WIDGET_PROMPTS
from src.lib.ai_document.system_prompts.french.widgets_prompts.widget_prompts_root import (
    widget_prompts,
)
from src.lib.ai_document.system_prompts.french.get_delta_content_system_message_fr import (
    get_delta_content_system_message_fr,
)
from src.lib.websocketTypes.general_classes import OperationEnum, SexeEnum
from src.lib.websocketTypes.publish_temporary_chanel_message import publish_message
from src.lib.websocketTypes.temporary_chanel_message_class import TemporaryMessageType


async def fallback_publish(chunk: dict, temporaryChanelId: str):
    await asyncio.sleep(0.1)

    publish_message(
        temporaryChanelId=temporaryChanelId,
        operation=OperationEnum.publish,
        content=chunk,
        type=TemporaryMessageType.payload,
        debug="fallback publish in generate ai content",
    )


def build_human_message(
    content: str, sex: SexeEnum, extracted_data: Optional[List[str]] = None
) -> str:
    sex_str = "female" if sex == SexeEnum.F else "male"
    extracted = (
        f"<ExtractedData>{' '.join(extracted_data)}</ExtractedData>"
        if extracted_data
        else ""
    )
    return f"<MedicalObservation>{content}</MedicalObservation><Sex>{sex_str}</Sex>{extracted}"


def build_children(
    chunk: Optional[dict], chunk_agg: str, final_remarks: bool
) -> List[dict]:
    children = (
        [child for child in chunk.get("children", []) if not child.get("refactor")]
        if chunk
        else []
    )

    children.append(
        {
            "id": str(ULID()),
            "text": f"Remarques: {chunk_agg}" if final_remarks else chunk_agg,
            "refactored": True,
        }
    )

    return children


def build_message_content(
    chunk: Optional[dict], children: List[dict], message_id: str, final_remarks: bool
) -> dict:
    if chunk and chunk.get("injected"):
        content = {
            **chunk,
            "children": children,
            "AIgenerated": True,
            "AiTarget": False,
            "id": message_id,
        }

        return content

    return {
        "AiTarget": False,
        "AIgenerated": True,
        "children": children,
        "id": message_id,
        "type": "p",
        "widgetId": chunk.get("widgetId", "") if chunk and not final_remarks else "",
        "widgetName": (
            chunk.get("widgetName", "") if chunk and not final_remarks else ""
        ),
    }


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
    message: List[Any]

    if final_remarks:
        message = [
            SystemMessage(content=get_delta_content_system_message_fr),
            HumanMessage(content=build_human_message(content, sex, extracted_data)),
        ]
    elif chunk:
        widget_id = chunk.get("widgetId", "")
        if widget_id in widget_prompts:
            message = [
                SystemMessage(content=widget_prompts[widget_id]),
                HumanMessage(content=build_human_message(content, sex)),
            ]
        elif chunk.get("injected"):
            message = [
                SystemMessage(content=WIDGET_PROMPTS.get(widget_id, "")),
                HumanMessage(content=content),
            ]
        else:
            await fallback_publish(chunk, temporaryChanelId)
            return
    else:
        await fallback_publish(chunk, temporaryChanelId)
        return

    chunk_agg = ""
    chunk_count = 0
    message_id = str(ULID())

    for c in llm.stream(message):
        if await request.is_disconnected():
            print("Client disconnected!")
            return {"message": "Request aborted by client"}

        chunk_agg += c
        chunk_count += 1

        if chunk_count >= 20:
            children = build_children(chunk, chunk_agg, final_remarks)
            content_to_publish = build_message_content(
                chunk, children, message_id, final_remarks
            )

            # print("chunk to publish", content_to_publish)

            publish_message(
                temporaryChanelId=temporaryChanelId,
                operation=OperationEnum.publish,
                content=content_to_publish,
                type=TemporaryMessageType.chunk,
                debug="chunk publish ai generated",
            )
            chunk_count = 0

    # Final message
    children = build_children(chunk, chunk_agg, final_remarks)
    content_to_publish = build_message_content(
        chunk, children, message_id, final_remarks
    )

    # print("message to publish", content_to_publish)

    publish_message(
        temporaryChanelId=temporaryChanelId,
        operation=OperationEnum.publish,
        content=content_to_publish,
        type=TemporaryMessageType.chunk,
        debug="final publish ai generated",
    )

    if not final_remarks:
        extracted_data.append(f"\n{chunk_agg}")

    return None
