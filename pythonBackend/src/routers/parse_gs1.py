from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)
from pydantic import BaseModel
from biip.gs1 import GS1Message
from src.lib.get_auth_token import get_auth_token
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

cwd = os.getcwd

router = APIRouter()

JWT_Secret = os.getenv("JWT_SECRET")

router = APIRouter()


class Document(BaseModel):
    barcode: str


@router.post("/")
async def parse_gs1(document: Document, token: str = Depends(get_auth_token)):

    try:
        jwt.decode(token, JWT_Secret, algorithms=["HS256"])
        pass
    except Exception as e:
        print(f"Error processing request: {e}")
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to access this resource.",
        )

    try:
        print(document.barcode)
        msg = GS1Message.parse(document.barcode)
        Ai = {
            "GTIN": msg.get(ai="01").value,
            "LOT": msg.get(ai="10").value,
            "expiry": msg.get(ai="17").value,
        }

        return {
            "message": "Request completed",
            "data": Ai,
        }

    except Exception as e:
        print(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
