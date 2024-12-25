import json
import tempfile
from fastapi import APIRouter, BackgroundTasks, HTTPException, Request
from fastapi.responses import FileResponse
from pathlib import Path
import requests
from src.lib.pdf.get_file_data import get_file_data
from src.lib.pdf.get_file_settings import get_file_settings
from src.lib.pdf.slate_parser.slates_classes import QueryParams
from ..lib.pdf.generate_pdf_util import generate_pdf
from pprintpp import pprint
import os
import shutil
from contextlib import asynccontextmanager


pdf_file_path = Path("test.pdf")


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


@router.get("/{pdf_id}")
async def pdf(
    background_tasks: BackgroundTasks,
    pdf_id: str,
    request: Request,
    page_size: str = "A4",
):
    cookies = request.cookies
    cwd = os.getcwd()

    auth_url = "http://api.bolt.local/auth/user"

    response = requests.get(auth_url, cookies=cookies)
    if not response.status_code == 200:
        raise HTTPException(
            status_code=403,
            detail="You do not have permission to access this resource.",
        )
    user = response.json()
    # pprint(user, indent=5)

    cwd = os.getcwd()
    custom_dir = os.path.join(cwd, "generated")
    # Ensure the custom directory exists
    os.makedirs(custom_dir, exist_ok=True)
    query_params = QueryParams(page_size=page_size)

    async with temporary_directory(custom_dir=custom_dir) as temp_dir:
        settings = await get_file_settings(user_id=user["userId"], temp_dir=temp_dir)
        data = await get_file_data(pdf_id=pdf_id)
        pdf = generate_pdf(
            tmpdirname=temp_dir,
            data=data,
            settings=settings,
            query_params=query_params,
        )
        background_tasks.add_task(lambda: shutil.rmtree(temp_dir))
        return FileResponse(pdf, media_type="application/pdf")
