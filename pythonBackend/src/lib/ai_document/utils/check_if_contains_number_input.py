from typing import Any, List, Optional

from pprintpp import pprint
from pydantic import BaseModel
from src.lib.typesense.typesense_client import typesense_client


class NumberInputDescription(BaseModel):
    input_name: str
    input_description: str
    input_value: Optional[float] = None


class NumberInputsCheckerResponse(BaseModel):
    check: bool
    number_inputs: List[NumberInputDescription]


def checker_function(child: Any, number_inputs: List[NumberInputDescription]):
    if "children" in child:
        for c in child["children"]:
            checker_function(child=c, number_inputs=number_inputs)

    if "type" in child:
        if child["type"] == "data-input":
            # pprint(child, depth=4)
            input_data = typesense_client.collections[
                "patient-input-data"
            ].documents.search(
                {
                    "q": child["inputName"],
                    "query_by": "inputName",
                    "filter_by": f"inputName:{child['inputName']} && deleted:false",
                }
            )
            # pprint(input_data, depth=4)
            if input_data["found"] >= 1:
                found = input_data["hits"][0]["document"]
                number_inputs.append(
                    NumberInputDescription(
                        input_name=child["inputName"],
                        input_description=found["description"],
                        input_value=None,
                    )
                )
                # pprint(found, depth=4)
    pass


def check_if_contains_number_input(chunk: Any) -> NumberInputsCheckerResponse:
    # print(chunk)
    number_inputs: List[NumberInputDescription] = []
    checker_function(child=chunk, number_inputs=number_inputs)
    result = NumberInputsCheckerResponse(
        check=len(number_inputs) > 0, number_inputs=number_inputs
    )

    return result
