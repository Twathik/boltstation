from typing import Any, List, Optional

from pprintpp import pprint
from pydantic import BaseModel

from src.lib.typesense.typesense_client import typesense_client

# fmt: off
class FilteredData(BaseModel):
    value: Optional[float] = None
    sentence: Optional[str] = ""
# fmt: on


class ExtractedData(BaseModel):
    input_name: str
    data: FilteredData


def checker_function(child: Any, data: List[ExtractedData]):
    if "children" in child:
        for c in child["children"]:
            checker_function(child=c, data=data)

    if "type" in child:
        if child["type"] == "data-input":
            for d in data:
                if d.input_name == child["inputName"]:
                    child["value"] = 0 if d.data.value == None else d.data.value

    pass


def populate_found_data(chunk: Any, data: List[ExtractedData]) -> Any:
    # print(chunk)
    checker_function(child=chunk, data=data)
