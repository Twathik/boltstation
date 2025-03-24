from typing import Any, List, Mapping, Sequence
from fastapi import Request
from fastapi.responses import StreamingResponse
from ollama import Message, chat
from pprintpp import pprint

from src.lib.generate_coronarography.generators.report_generator import report_generator
from src.lib.generate_coronarography.prompts.initial_coronarography_report import (
    initial_coronarography_report,
)
from src.lib.generate_coronarography.utils.coronarography_classes import (
    ChatHistory,
    CoronarySegmentation,
)


""" if not message_history.history == None:
for msg in message_history.history:

    messages.append(
        {
            "role": "user" if msg.type == "user" else "assistant",
            "content": msg.message,
        }
    ) """


def generate_initial_coronarography_report(
    state: CoronarySegmentation,
    bypass_state: str,
    message_history: ChatHistory,
    request: Request,
):

    generated_report = report_generator(state=state)
    print(generated_report)

    messages: Sequence[Mapping[str, Any] | Message] | None = [
        {
            "role": "system",
            "content": initial_coronarography_report,
        },
        {"role": "user", "content": generated_report},
    ]

    async def stream():
        stream = chat(
            # model="llama3.3:latest",
            # model="phi4:latest",
            model="gemma3:27b",
            messages=messages,
            stream=True,
            options={"temperature": 0},
        )
        # Use asyncio.to_thread to run the synchronous generator in a background thread
        for chunk in stream:
            if await request.is_disconnected():
                break
            # Run the generator in a thread
            yield chunk.message.content  # Convert to string if it's not

    return StreamingResponse(stream(), media_type="text/plain")
