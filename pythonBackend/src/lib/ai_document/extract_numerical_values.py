from langchain.schema import SystemMessage, HumanMessage
from typing import Any, List
from langchain_ollama import OllamaLLM
from src.lib.ai_document.utils.ai_document_classes import ExtractedData, FilteredData
from src.lib.ai_document.utils.check_if_contains_number_input import (
    NumberInputDescription,
)

from src.lib.websocketTypes.general_classes import OperationEnum
from src.lib.websocketTypes.publish_temporary_chanel_message import publish_message
from src.lib.websocketTypes.temporary_chanel_message_class import TemporaryMessageType

from langchain_core.output_parsers import PydanticOutputParser
from src.lib.ai_document.system_prompts.french.extract_numerical_data_system_prompt_fr import (
    extract_numerical_data_system_prompt_fr,
)


parser = PydanticOutputParser(pydantic_object=FilteredData)


def extract_numerical_values(
    temporaryChanelId: str,
    llm: OllamaLLM,
    extracted_data: List[str],
    content: str,
    number_inputs: List[NumberInputDescription],
    extracted_values: List[Any],
):
    data: List[ExtractedData] = []
    for target_input in number_inputs:
        # print(target_input)

        message = [
            SystemMessage(content=extract_numerical_data_system_prompt_fr),
            HumanMessage(
                content=f"""
                    <MedicalObservation>{content}</MedicalObservation>
                    <Description>{target_input.input_description}</Description>
                    {parser.get_format_instructions()}"""
            ),
        ]
        # print(target_input.input_description)

        results = llm.invoke(message, format="json")
        results_values: FilteredData | None = None

        if results:
            results_values = parser.parse(results)  # type: ignore

            extracted_value = {
                "inputName": target_input.input_name,
                "value": results_values.value,
            }

            publish_message(
                temporaryChanelId=temporaryChanelId,
                operation=OperationEnum.publish,
                content=extracted_value,
                type=TemporaryMessageType.value,
                debug="extract numerical values",
            )
            extracted_data.append(results_values.sentence)
            extracted_values.append(extracted_value)

    pass
