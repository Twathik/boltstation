import json
import shutil
import tempfile
from fastapi import (
    APIRouter,
    BackgroundTasks,
    HTTPException,
    Request,
)
from fastapi.concurrency import asynccontextmanager
from fastapi.responses import FileResponse
from pprintpp import pprint
from pydantic import BaseModel
import requests
import os
import requests
from dotenv import load_dotenv
from src.lib.dicom.copy_to_folder import copy_folder_contents
from src.lib.dicom.create_iso_file import (
    create_iso_with_original_names,
)
from src.lib.extract_kt_product_infos.extract_product_info import extract_product_info
from src.lib.format_string import format_string
from src.lib.typesense.typesense_client import typesense_client
from src.lib.prismaClient import prisma_client
import zipfile
import pycdlib

load_dotenv()
STORAGE_HOST = os.getenv("STORAGE_HOST")
ORTHANC_USER = os.getenv("ORTHANC_USER")
ORTHANC_PSW = os.getenv("ORTHANC_PSW")
orthanc_base_url = "http://pacs.bolt.local"

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
    workingListId: str


@router.get("/{workingListId}")
async def export_dicom(
    background_tasks: BackgroundTasks, request: Request, workingListId: str
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

    try:

        workingList = await prisma_client.workinglist.find_first_or_raise(
            where={"id": workingListId}
        )

        patient = await prisma_client.patient.find_first_or_raise(
            where={"id": workingList.patientId}
        )
        file_name = f"{format_string(patient.lastName)}-{format_string(patient.firstName)}_{workingList.createdAt.strftime("%d-%m-%Y")}.zip"

        async with temporary_directory(custom_dir=custom_dir) as temp_dir:

            params = {
                "Level": "Study",
                "Query": {"AccessionNumber": workingList.id},
                "Expand": True,
            }
            response = requests.post(
                f"{orthanc_base_url}/tools/find",
                auth=(ORTHANC_USER, ORTHANC_PSW),
                json=params,
            )

            if response.status_code == 200:

                study_id = response.json()[0]["ID"]
                url = f"{orthanc_base_url}/studies/{study_id}/media"
                response = requests.get(
                    url, auth=(ORTHANC_USER, ORTHANC_PSW), stream=True
                )
                document_filename = os.path.join(temp_dir, file_name)
                if response.status_code == 200:

                    with open(document_filename, "wb") as f:
                        for chunk in response.iter_content(chunk_size=1024):
                            if chunk:
                                f.write(chunk)

                    with zipfile.ZipFile(document_filename, "r") as zip_ref:
                        # Extract all contents to the specified directory
                        zip_ref.extractall(document_filename.replace(".zip", ""))
                        print(
                            f"Files extracted to {document_filename.replace('.zip','')}"
                        )
                    copy_folder_contents(
                        os.path.join(cwd, "src/lib/dicom/viewer"),
                        document_filename.replace(".zip", ""),
                    )
                    create_iso_with_original_names(
                        document_filename.replace(".zip", ".iso"),
                        document_filename.replace(".zip", ""),
                    )
                    print(f"Study {workingList.linkId} downloaded successfully.")
                    return FileResponse(
                        document_filename.replace(".zip", ".iso"),
                        media_type="application/x-iso9660-image",
                        filename=file_name.replace(".zip", ".iso"),
                    )
                else:
                    print(
                        f"Error: Unable to download study {workingList.linkId}. Status code: {response.status_code}"
                    )
                    raise HTTPException(status_code=500, detail="Internal Server Error")

            else:
                print(
                    f"Error: Unable to search for study. Status code: {response.status_code}"
                )
                raise HTTPException(status_code=500, detail="Internal Server Error")

            # background_tasks.add_task(lambda: shutil.rmtree(temp_dir))
            pass

        return {
            "message": "Request completed",
            "data": "",
        }

    except Exception as e:
        print(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    finally:
        background_tasks.add_task(lambda: shutil.rmtree(temp_dir))
