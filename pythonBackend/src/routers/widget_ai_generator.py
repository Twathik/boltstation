import os
from fastapi import APIRouter, HTTPException, Request
from langchain.schema import SystemMessage, HumanMessage
from langchain_ollama import OllamaLLM
from pydantic import BaseModel
import requests
from src.lib.ai_document.system_prompts.french.widgets_prompts.widget_prompts_root import (
    widget_prompts,
)
from src.lib.websocketTypes.general_classes import SexeEnum
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()


class Document(BaseModel):
    temporaryChanelId: str
    widgetId: str
    content: str


@router.post("/")
async def widget_generator(request: Request, document: Document):
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
    print(document)
    try:
        if document.widgetId in widget_prompts:
            llm = OllamaLLM(
                # model=os.getenv("AI_model"),
                model="gemma2:27b",
                # model="phi4:latest",
                temperature=0.2,
                # other params...
            )
            system_prompt = widget_prompts.get(document.widgetId)

            message = [
                SystemMessage(content=system_prompt),
                HumanMessage(
                    content=f"""
                    <MedicalObservation>
                    {document.content}
                    </MedicalObservation>
                    <Sex></Sex>
                """
                ),
            ]
            result = llm.invoke(message)

            return {"message": "Request completed", "status": 1, "data": result}

        else:
            return {"message": "Request completed", "status": 0, "data": ""}

    except Exception as e:
        print(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
