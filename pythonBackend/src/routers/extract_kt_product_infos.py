import shutil
import tempfile
from fastapi import (
    APIRouter,
    BackgroundTasks,
    HTTPException,
    Request,
)
from fastapi.concurrency import asynccontextmanager
from pprintpp import pprint
from pydantic import BaseModel
import requests
import os

from dotenv import load_dotenv

from src.lib.extract_kt_product_infos.extract_product_info import extract_product_info
from src.lib.typesense.typesense_client import typesense_client

load_dotenv()
STORAGE_HOST = os.getenv("STORAGE_HOST")

router = APIRouter()


@asynccontextmanager
async def temporary_directory(custom_dir: str):
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp(dir=custom_dir)
    try:
        # Yield the directory path for use in the response
        yield temp_dir
    finally:
        pass


class Document(BaseModel):
    documentUrl: str


@router.post("/")
async def extractKtProductInfos(
    background_tasks: BackgroundTasks, request: Request, document: Document
):
    cookies = request.cookies

    auth_url = "http://api.bolt.local/auth/user"

    response = requests.get(auth_url, cookies=cookies)
    if not response.status_code == 200:
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to access this resource.",
        )
    user = response.json()

    cwd = os.getcwd()
    custom_dir = os.path.join(cwd, "generated")
    # Ensure the custom directory exists
    os.makedirs(custom_dir, exist_ok=True)
    file_name = document.documentUrl.split("/")[-1]

    try:
        image_url = f"http://{STORAGE_HOST}:9000/uploads/{document.documentUrl}"
        response = requests.get(image_url)
        response.raise_for_status()

        async with temporary_directory(custom_dir=custom_dir) as temp_dir:
            document_filename = os.path.join(temp_dir, file_name)
            with open(document_filename, "wb") as scan:
                scan.write(response.content)
                pass
            product = extract_product_info(document_filename)

            background_tasks.add_task(lambda: shutil.rmtree(temp_dir))
            pass

        if not product == None:
            search = typesense_client.collections[
                "inHospitalSpecificMaterials"
            ].documents.search(
                {
                    "q": "",
                    "query_by": "name",
                    "filter_by": f"ref:={product.ref}",
                    "limit_hits": 1,
                    "page": 1,
                    "per_page": 1,
                }
            )
            # print(product)
            if not len(search["hits"]) == 0:
                row_product = search["hits"][0]["document"]

                if not product.GTIN == None:
                    row_product["GTIN"].append(product.GTIN)
                    print(row_product["GTIN"])
                    row_product["GTIN"] = list(set(row_product["GTIN"]))

                row_product["GTIN"] = "-".join(row_product["GTIN"])

                return {
                    "message": "Request completed",
                    "data": row_product,
                }

        return {
            "message": "Request completed",
            "data": product,
        }

    except Exception as e:
        print(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
