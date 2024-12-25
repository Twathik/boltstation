import json
import tempfile
from fastapi import APIRouter, BackgroundTasks, HTTPException, Request
from fastapi.responses import FileResponse
from pathlib import Path

import requests

from src.lib.pdf.slate_parser.slates_classes import (
    PDF_Urls,
    PDF_paddings,
    PDF_settings,
    PageSizeEnum,
    QueryParams,
)
from ..lib.pdf.lorem_ipsum import LoremIpsumData
from ..lib.pdf.generate_pdf_util import generate_pdf
from ..lib.pdf.lorem_ipsum import LoremIpsumData
from pprintpp import pprint
import os
import shutil
from contextlib import asynccontextmanager


pdf_file_path = Path("test.pdf")

cwd = os.getcwd

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


@router.get("/{demo_id}")
async def pdf_demo(background_tasks: BackgroundTasks, demo_id: str, request: Request):
    cookies = request.cookies

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

    data = [
        {"text": "1"},
        {"type": "page-break", "children": [{"text": ""}]},
        {"text": "2"},
    ]
    # data = LoremIpsumData
    settings = PDF_settings(
        paddings=PDF_paddings(
            A4paddingBottom=10,
            A4paddingLeft=10,
            A4paddingRight=10,
            A4paddingTop=10,
            A5paddingBottom=10,
            A5paddingLeft=10,
            A5paddingRight=10,
            A5paddingTop=10,
        ),
        urls=PDF_Urls(
            evenUrl=os.path.join(cwd, f"Templates/{demo_id}withHeader.jpg"),
            oddUrl=os.path.join(cwd, f"Templates/{demo_id}noHeader.jpg"),
        ),
    )

    async with temporary_directory(custom_dir=custom_dir) as temp_dir:

        pdf = generate_pdf(
            tmpdirname=temp_dir,
            data=data,
            settings=settings,
            query_params=QueryParams(page_size=PageSizeEnum.A4),
        )

        background_tasks.add_task(lambda: shutil.rmtree(temp_dir))
        return FileResponse(pdf, media_type="application/pdf")
