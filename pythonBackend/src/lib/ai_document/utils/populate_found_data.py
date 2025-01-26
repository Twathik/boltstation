from typing import Any, List, Optional

from pprintpp import pprint
from pydantic import BaseModel

from src.lib.typesense.typesense_client import typesense_client
from src.lib.websocketTypes.general_classes import OperationEnum
from src.lib.websocketTypes.publish_temporary_chanel_message import publish_message
from src.lib.websocketTypes.temporary_chanel_message_class import TemporaryMessageType

# fmt: off
class FilteredData(BaseModel):
    value: Optional[float] = None
    sentence: Optional[str] = ""
# fmt: on


class ExtractedData(BaseModel):
    input_name: str
    data: FilteredData


def checker_function(child: Any, data: List[ExtractedData], temporaryChanelId: str):
    if "children" in child:
        for c in child["children"]:
            checker_function(child=c, data=data, temporaryChanelId=temporaryChanelId)

    if "type" in child:
        if child["type"] == "data-input":
            for d in data:
                if d.input_name == child["inputName"]:
                    publish_message(
                        temporaryChanelId=temporaryChanelId,
                        operation=OperationEnum.publish,
                        content={"inputName": d.input_name, "value": d.data.value},
                        type=TemporaryMessageType.value,
                    )

    pass


def populate_found_data(
    chunk: Any, data: List[ExtractedData], temporaryChanelId: str
) -> Any:
    # print(chunk)
    checker_function(child=chunk, data=data, temporaryChanelId=temporaryChanelId)
