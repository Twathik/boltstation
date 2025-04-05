from pydantic import BaseModel
from typing import List, Literal, Optional


class AiChatMessage(BaseModel):
    type: Literal["user", "AI"]
    message: str
    id: str
    done: bool
    selected: bool


class ChatHistory(BaseModel):
    history: Optional[List[AiChatMessage]] = None
