from typing import Any, Mapping, Sequence

from fastapi import Request
from fastapi.responses import StreamingResponse
from ollama import Message, chat


def generic_ollama_report_formater(
    request: Request, system_prompt: str, raw_report: str
):
    messages: Sequence[Mapping[str, Any] | Message] | None = [
        {
            "role": "system",
            "content": system_prompt,
        },
        {"role": "user", "content": raw_report},
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
