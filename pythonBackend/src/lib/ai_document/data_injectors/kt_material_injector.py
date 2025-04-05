import json
from typing import Any, List
from ulid import ULID


from src.lib.prismaClient import prisma_client


async def material_injector(
    document: List[Any], chunk: Any, clinicalEventId: str, extracted_data: List[str]
) -> Any:
    materials = await prisma_client.usedspecificmaterial.find_many(
        where={"clinicalEventId": clinicalEventId, "deleted": False}
    )

    for material in materials:
        product = json.loads(material.productDetails)
        description = f"{"Type: " + product['type'] + '. ' if not product['type'] == '-' else ''}{product['name']} {product['Description']}. { "Fabriquant: " + product['Fabriquant'] + '. ' if not product['Fabriquant'] == None else ''}{"Diametre: " + product['Diametre'] + 'mm. ' if 'Diametre' in product and not product['Diametre'] == None else ''}{"Longueur: " + product['Longueur'] + 'mm. ' if 'Longueur' in product and not product['Longueur'] == None else ''}LOT: {material.LOT}"

        document.append(
            {
                "AiTarget": False,
                "type": "p",
                "children": [
                    {
                        "text": description,
                    },
                ],
                "id": str(ULID()),
                "optionalWidget": False,
                "indent": 1,
                "listStyleType": "disc",
                "widgetId": chunk["widgetId"],
                "widgetName": chunk["widgetName"],
                "injected": True,
            }
        )
        extracted_data.append(description)

    pass
