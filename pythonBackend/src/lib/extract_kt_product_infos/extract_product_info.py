from typing import Optional
from pydantic import BaseModel, ValidationError

from ollama import chat
from langchain_core.output_parsers import PydanticOutputParser
import cv2
from pyzbar import pyzbar
from biip.gs1 import GS1Message
from src.lib.barcode_parser.GS1_barcode_parser import GS1_bar_code_parser


class KTProductInfo(BaseModel):
    ref: str
    name: Optional[str]
    manufacturer: Optional[str]
    GTIN: Optional[str]


def extract_product_info(document_filename: str) -> Optional[KTProductInfo]:
    parser = PydanticOutputParser(pydantic_object=KTProductInfo)
    try:
        # Load the image
        image = cv2.imread(document_filename)

        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Use pyzbar to decode barcodes
        barcodes = pyzbar.decode(gray)
        GTIN: Optional[str] = None
        try:
            for barcode in barcodes:
                # Extract the barcode data and type
                barcode_data = barcode.data.decode("utf-8")
                # print(f"Barcode Data: {barcode_data}")
                # print(f"Barcode Type: {barcode_type}")

                parsed = GS1Message.parse(barcode_data)
                if "GTIN" in parsed:
                    GTIN = parsed["GTIN"]

                # Print the barcode data and type

                # pprint(parsed, depth=4, width=80)
            pass
        except Exception as e:
            print("corrupted barcode", e)

        # Get the LLM response
        response = chat(
            model="llama3.2-vision:latest",
            messages=[
                {
                    "role": "user",
                    "content": f"""Analyse this image and extract the following information:
                    - the product ref
                    - the product name (if the information is not found return None)
                    - the product manufacturer (if the information is not found return None)
                    - the GTIN of the product witch is the (01) Application Identifier according to code128 norm, it is a string of 14 characters (if the information is not found return None) 
                    
                    Avoid returning any schema or structure, only return actual product data in the format provided. 
                    Example response:
                    {{'ref': 'drug-123', 'name': 'Painkiller', 'manufacturer': 'XYZ Corp', 'GTIN': '08717648205613'}}
                    """,
                    "images": [document_filename],
                }
            ],
            format="json",
            options={
                "temperature": 0,
            },
        )

        # Ensure response is not empty
        if response is None or not response.get("message"):
            print("No response from LLM.")
            return None

        # Extract the content from the LLM response
        content = response["message"].get("content", "")
        # print("Raw content:", content)

        # If the content is still a schema, inform the user
        if isinstance(content, str) and "properties" in content:
            print(
                "Received schema instead of data. Please check the model prompt or modify instructions."
            )
            return None

        # If the response contains data, validate it
        try:
            product = parser.parse(content)
            if not GTIN == None:
                product.GTIN = GTIN
            if not len(product.GTIN) == 14:
                product.GTIN = None

            return product
        except ValidationError as e:
            print(f"Validation failed: {e}")
            return None

    except Exception as e:
        print(f"Error during processing: {e}")
        return None
