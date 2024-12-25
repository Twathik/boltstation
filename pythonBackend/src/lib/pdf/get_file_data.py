from typing import List
from .lorem_ipsum import LoremIpsumData


async def get_file_data(pdf_id: str) -> List[dict]:
    data = []
    if pdf_id == "lorem_ipsum":
        data = LoremIpsumData

    return data
