import time
from lib.prismaClient import prisma_client
from dotenv import load_dotenv
from utils import (
    get_som_labeled_img,
    check_ocr_box,
    get_caption_model_processor,
    get_yolo_model,
)
import torch
import os
import tempfile
import gc
import json
from llm_queue_utils.general_utils.merge_images import merge_images

device = "cuda"

load_dotenv()
STORAGE_HOST = f'{os.getenv("HOST", "host.docker.internal")}:9000'
cwd = os.getcwd()


async def parse(patientIdentityScanId: str) -> str:
    await prisma_client.connect()
    try:

        som_model = get_yolo_model(model_path=f"{cwd}/weights/icon_detect/best.pt")
        som_model.to(device)
        # caption_model_processor = get_caption_model_processor(model_name="blip2", model_name_or_path="weights/icon_caption_blip2", device=device)
        caption_model_processor = get_caption_model_processor(
            model_name="florence2",
            model_name_or_path=f"{cwd}/weights/icon_caption_florence",
            device=device,
        )

        identity_documents = (
            await prisma_client.patientidentitydocuments.find_first_or_raise(
                where={"id": patientIdentityScanId}
            )
        )

        # Open the image from the response content
        image = merge_images(
            image_urls=list(
                map(
                    lambda x: x.replace("storage.bolt.local", STORAGE_HOST),
                    identity_documents.identityDocumentUrls,
                )
            ),
            direction="vertical",
        )

        temp_image_path = ""
        # Save the image to a temporary file
        with tempfile.TemporaryDirectory() as tmpdirname:
            temp_image_path = f"{tmpdirname}/image.jpeg"

            image.save(temp_image_path)

            BOX_TRESHOLD = 0.03
            box_overlay_ratio = image.size[0] / 3200
            draw_bbox_config = {
                "text_scale": 0.8 * box_overlay_ratio,
                "text_thickness": max(int(2 * box_overlay_ratio), 1),
                "text_padding": max(int(3 * box_overlay_ratio), 1),
                "thickness": max(int(3 * box_overlay_ratio), 1),
            }

            ocr_bbox_rslt, is_goal_filtered = check_ocr_box(
                temp_image_path,
                display_img=False,
                output_bb_format="xyxy",
                goal_filtering=None,
                easyocr_args={"paragraph": False, "text_threshold": 0.9},
                use_paddleocr=True,
            )
            text, ocr_bbox = ocr_bbox_rslt

            dino_labled_img, label_coordinates, parsed_content_list = (
                get_som_labeled_img(
                    temp_image_path,
                    som_model,
                    BOX_TRESHOLD=BOX_TRESHOLD,
                    output_coord_in_ratio=False,
                    ocr_bbox=ocr_bbox,
                    draw_bbox_config=draw_bbox_config,
                    caption_model_processor=caption_model_processor,
                    ocr_text=text,
                    use_local_semantics=True,
                    iou_threshold=0.1,
                    imgsz=640,
                )
            )

            result = parsed_content_list
            # print(json.dumps(result))

            await prisma_client.patientidentitydocuments.update(
                where={"id": patientIdentityScanId},
                data={"extractedData": json.dumps(result)},
            )
            del som_model, caption_model_processor
            torch.cuda.empty_cache()
            gc.collect()
            await prisma_client.disconnect()

            return "200"

        pass
    except Exception as e:
        await prisma_client.disconnect()
        print(e)
        return "500"
