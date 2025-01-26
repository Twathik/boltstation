from datetime import datetime, timezone
import time
from lib.redisClient import notification_chanel, redis_client
from lib.prismaClient import prisma_client
from dotenv import load_dotenv
import os
import json
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain_ollama.chat_models import ChatOllama
from langchain_core.messages import SystemMessage
from langchain_core.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate

from websocketTypes.general_classes import MessageDestination, OperationEnum
from websocketTypes.patient_identity_document_add_message_class import (
    AddPatientIdentityDocumentMessage,
    PatientIdentityDocument,
    Payload,
    ProcessedData,
)
from ulid import ULID

load_dotenv()
cwd = os.getcwd()


parser = PydanticOutputParser(pydantic_object=ProcessedData)


async def generate_user_info_model(scannedDocumentId: str) -> str:

    try:
        await prisma_client.connect()
        model = ChatOllama(
            model="gemma2:latest",
            keep_alive="10m",
            temperature=0.2,
        )
        system_prompt = """
        you are a helpful agent specialized in analyzing the content of scanned identity documents. the user will give you an array of strings from an OCR of an identity document written in French. analyze this array to extract information related to this document.
        """
        user_prompt = HumanMessagePromptTemplate.from_template(
            "{request}\n{format_instructions}"
        )
        chat_prompt = ChatPromptTemplate.from_messages(
            [
                SystemMessage(content=system_prompt),
                user_prompt,
            ]
        )

        try:
            identity = await prisma_client.patientidentitydocuments.find_first_or_raise(
                where={"id": scannedDocumentId}
            )
            parsed_document = json.loads(identity.extractedData)

            request = chat_prompt.format_prompt(
                request=str(parsed_document),
                format_instructions=parser.get_format_instructions(),
            ).to_messages()

            results = model.invoke(request, temperature=0, format="json")

            results_values: ProcessedData | None = None
            if results:
                results_values = parser.parse(results.content)
            print(results_values)

            elapsedTime = (
                datetime.now(timezone.utc) - identity.startProceeding
            ).total_seconds()
            print(elapsedTime)
            doc = await prisma_client.patientidentitydocuments.update(
                where={"id": scannedDocumentId},
                data={
                    "processedData": results_values.model_dump_json(),
                    "proceeded": True,
                    "elapsedTime": elapsedTime,
                },
            )

            message = AddPatientIdentityDocumentMessage(
                bashPayload=None,
                destination=[MessageDestination.Patient_identity_document],
                globalMessage=True,
                id=ULID(),
                payload=Payload(
                    operation=OperationEnum.add,
                    PatientIdentityDocument=PatientIdentityDocument(
                        elapsedTime=doc.elapsedTime,
                        id=doc.id,
                        identityDocumentUrls=doc.identityDocumentUrls,
                        processedData=results_values,
                        sexe=doc.sexe,
                    ),
                ),
                type=MessageDestination.Patient_identity_document,
                subscriptionIds=[],
            )

            redis_client.publish(notification_chanel, message.model_dump_json())
            await prisma_client.disconnect()
            print("operation finished with success")
            pass
        except Exception as e:
            await prisma_client.disconnect()
            raise e
        pass
    except Exception as e:
        raise e


async def generate_user_info_error(scannedDocumentId: str):
    await prisma_client.connect()
    try:
        doc = await prisma_client.patientidentitydocuments.update(
            where={"id": scannedDocumentId},
            data={"extractedData": None},
        )
        message = AddPatientIdentityDocumentMessage(
            bashPayload=None,
            destination=[MessageDestination.Patient_identity_document],
            globalMessage=True,
            id=ULID(),
            payload=PatientIdentityDocument(
                id=scannedDocumentId,
                elapsedTime=0,
                identityDocumentUrls=doc.identityDocumentUrls,
                processedData=None,
                sexe=doc.sexe,
            ),
            type=MessageDestination.Patient_identity_document,
            subscriptionIds=[],
        )
        await redis_client.publish(notification_chanel, message)
        await prisma_client.disconnect()
        pass
    except Exception as e:
        await prisma_client.disconnect()
        raise e
