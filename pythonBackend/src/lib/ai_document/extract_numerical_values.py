from langchain.schema import SystemMessage, HumanMessage
from typing import Any, List, Optional
from fastapi import Request
from langchain_ollama import OllamaLLM
from pprintpp import pprint
from pydantic import BaseModel, Field
from src.lib.ai_document.utils.check_if_contains_number_input import (
    NumberInputDescription,
)
from src.lib.ai_document.utils.populate_found_data import (
    ExtractedData,
    FilteredData,
    populate_found_data,
)
from src.lib.websocketTypes.general_classes import OperationEnum
from src.lib.websocketTypes.publish_temporary_chanel_message import publish_message
from src.lib.websocketTypes.temporary_chanel_message_class import TemporaryMessageType
from src.lib.ai_document.system_prompts.extract_numerical_data_system_prompt import (
    extract_numerical_data_system_prompt,
)
from langchain_core.output_parsers import PydanticOutputParser


parser = PydanticOutputParser(pydantic_object=FilteredData)


def extract_numerical_values(
    temporaryChanelId: str,
    llm: OllamaLLM,
    request: Request,
    extracted_data: List[str],
    content: str,
    chunk: Any,
    number_inputs: List[NumberInputDescription],
):
    data: List[ExtractedData] = []
    for target_input in number_inputs:
        # print(target_input)

        message = [
            SystemMessage(content=extract_numerical_data_system_prompt),
            HumanMessage(
                content=f"""
                    <MedicalObservation>{content}</MedicalObservation>
                    <Description>{target_input.input_description}</Description>
                    {parser.get_format_instructions()}"""
            ),
        ]

        results = llm.invoke(message, format="json")
        results_values: FilteredData | None = None

        if results:
            results_values = parser.parse(results)  # type: ignore
            data.append(
                ExtractedData(data=results_values, input_name=target_input.input_name)
            )
    populate_found_data(chunk=chunk, data=data)

    for d in data:
        extracted_data.append(d.data.sentence)

    publish_message(
        temporaryChanelId=temporaryChanelId,
        operation=OperationEnum.publish,
        content=chunk,
        type=TemporaryMessageType.payload,
    )

    pass
