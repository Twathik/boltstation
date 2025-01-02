import os
from pprintpp import pprint
import requests
from src.lib.pdf.slate_parser.slates_classes import PDF_Urls, PDF_paddings, PDF_settings
from src.lib.prismaClient import prisma_client

cwd = os.getcwd()
host = os.getenv("HOST", "localhost")


async def get_file_settings(user_id: str, temp_dir: str) -> PDF_settings:

    settings = await prisma_client.user.find_unique_or_raise(
        where={"userId": user_id},
    )

    if not settings.documentSettings == None and not settings.documentSettings == "":
        settings = PDF_settings.model_validate_json(settings.documentSettings)

        if "storage.bolt.local" in settings.urls.evenUrl:
            # Send a GET request to the image URL
            response = requests.get(
                settings.urls.evenUrl.replace("storage.bolt.local", f"{host}:9000"),
                stream=True,
            )
            response.raise_for_status()
            even_file_name = (
                os.path.basename(settings.urls.evenUrl.split("/")[-1]) + ".png"
            )
            even_temp_file_path = os.path.join(temp_dir, even_file_name)
            with open(even_temp_file_path, "wb") as tmp_file:
                tmp_file.write(response.content)
                settings.urls.evenUrl = even_temp_file_path
        else:

            settings.urls.evenUrl = os.path.join(cwd, settings.urls.evenUrl)

        if "storage.bolt.local" in settings.urls.oddUrl:
            # Send a GET request to the image URL
            response = requests.get(
                settings.urls.oddUrl.replace("storage.bolt.local", f"{host}:9000"),
                stream=True,
            )
            response.raise_for_status()
            odd_file_name = (
                os.path.basename(settings.urls.oddUrl.split("/")[-1]) + ".png"
            )
            odd_temp_file_path = os.path.join(temp_dir, odd_file_name)
            with open(odd_temp_file_path, "wb") as tmp_file:
                tmp_file.write(response.content)
                settings.urls.oddUrl = odd_temp_file_path
        else:

            settings.urls.oddUrl = os.path.join(cwd, settings.urls.oddUrl)

    else:
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
                evenUrl=os.path.join(cwd, f"Templates/1withHeader.jpg"),
                oddUrl=os.path.join(cwd, f"Templates/1noHeader.jpg"),
            ),
        )
    return settings
