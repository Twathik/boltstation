from typing import Any, List, Optional

from pprintpp import pprint
from pydantic import BaseModel
from src.lib.ai_document.system_prompts.french.widgets_prompts.variables_numeriques.numerical_variables_descriptions import (
    numerical_variables_descriptions,
)


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
            pprint(child, depth=4)

            check = next(
                (
                    item
                    for item in numerical_variables_descriptions
                    if item.get("name") == child["inputName"]
                ),
                None,
            )

            if not check == None:
                number_inputs.append(
                    NumberInputDescription(
                        input_name=child["inputName"],
                        input_description=check["description"],
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
