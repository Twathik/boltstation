from typing import Optional

from src.lib.prismaClient import prisma_client
from src.lib.pdf.slate_parser.slates_classes import Patient
from datetime import datetime


async def get_patient_data(pdf_id: str) -> Optional[Patient]:

    if not pdf_id == "lorem_ipsum":
        patient_id = pdf_id.split("-")[0]
        patient = await prisma_client.patient.find_first_or_raise(
            where={"id": patient_id}
        )

        return Patient(
            first_name=patient.firstName,
            last_name=patient.lastName,
            dob=patient.ddn.strftime("%d-%m-%Y"),
        )
    else:
        return None
