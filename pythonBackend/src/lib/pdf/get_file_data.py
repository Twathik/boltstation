import json
from typing import List

from pprintpp import pprint
from src.lib.prismaClient import prisma_client
from .lorem_ipsum import LoremIpsumData


async def get_file_data(pdf_id: str) -> List[dict]:

    if pdf_id == "lorem_ipsum":
        data = LoremIpsumData
        return data
    else:
        document_store = await prisma_client.documentstore.find_first_or_raise(
            where={"documentName": pdf_id},
        )
        data = json.loads(document_store.textContent)
        return data["children"]
