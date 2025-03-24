import traceback
from fastapi import APIRouter, HTTPException, Request
from pprintpp import pprint
from pydantic import BaseModel
import httpx  # Async HTTP requests
from dotenv import load_dotenv

from src.lib.generate_coronarography.generators.generate_coronarography_initial_report import (
    generate_initial_coronarography_report,
)
from src.lib.generate_coronarography.utils.coronarography_classes import (
    AiChatMessage,
    ChatHistory,
    CoronarySegmentation,
)
from src.lib.prismaClient import prisma_client

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI router
router = APIRouter()


class Document(BaseModel):
    clinicalEventId: str
    userMessage: str


@router.post("/")
async def generate_coronarography(request: Request, document: Document):
    cookies = request.cookies

    auth_url = "http://api.bolt.local/auth/user"

    # Use httpx for async HTTP requests
    async with httpx.AsyncClient() as client:
        response = await client.get(auth_url, cookies=cookies)

    if response.status_code != 200:
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to access this resource.",
        )

    user = response.json()

    try:
        clinical_event = await prisma_client.clinicalevent.find_first_or_raise(
            where={"id": document.clinicalEventId}
        )
        message_history = ChatHistory(
            history=[
                AiChatMessage(**msg) for msg in clinical_event.jsonData["chatMessages"]
            ]
        )

        state = CoronarySegmentation.model_validate(clinical_event.jsonData["state"])

        bypass_state = clinical_event.jsonData["bypassDescription"]

        return generate_initial_coronarography_report(
            state=state,
            bypass_state=bypass_state,
            message_history=message_history,
            request=request,
        )

    except Exception as e:
        pprint(e, depth=4, width=80)
        tb = traceback.format_exc()  # Get the traceback as a string
        print("Traceback information:")
        print(tb)
        raise HTTPException(status_code=500, detail="Internal Server Error")
