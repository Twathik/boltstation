from src.lib.prismaClient import prisma_client


async def get_document_title(pdf_id: str) -> str:
    if pdf_id == "lorem_ipsum":
        return "Document de demonstration"
    else:
        clinical_event_id = pdf_id.split("-")[1]
        clinical_event = await prisma_client.clinicalevent.find_first_or_raise(
            where={"id": clinical_event_id}
        )
        if not clinical_event.userTitle == None:
            return clinical_event.userTitle
        else:
            match clinical_event.eventType:
                case "DIAGNOSTIC":
                    return "Diagnostic"

                case "CLINICALEXAM":
                    return "Examen clinique"

                case "ECG":
                    return "ECG"

                case "BIOLOGY":
                    return "Bilan biologique"

                case "SONOGRAPHY":
                    return "Echocardiographie"

                case "PRESCRIPTION":
                    return "Ordonance"

                case "MEDICAL_REPORT":
                    return "Rapport médical"

                case "CERTIFICAT":
                    return "Certificat médical"

                case "HOSPITALIZATION":
                    return "Hospitalisation"
                case _:
                    return "unknown"
