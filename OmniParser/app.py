from fastapi import Body, FastAPI
from pydantic import BaseModel
from lib.prismaClient import prisma
import requests
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv
from utils import get_som_labeled_img, check_ocr_box, get_caption_model_processor, get_yolo_model
import torch
from ultralytics import YOLO
from PIL import Image
import os
import tempfile
import gc
import json

device = 'cuda'

load_dotenv()
STORAGE_HOST = f'{os.getenv("HOST", "host.docker.internal")}:9000'

async def lifespan(app: FastAPI):
    # Setup: Code to run at startup
    
    try:
        print("Starting up...")
        await prisma.connect()
       
    except Exception as e:
        print(f"Error connecting to Redis: {e}")
        raise e

    yield  # This yields control back to FastAPI, allowing it to run the app
    # Teardown: Code to run at shutdown
    await prisma.disconnect()
    print("Shutting down...")


# Create the FastAPI app
app = FastAPI(lifespan=lifespan)  # type: ignore

# Define a Pydantic model for complex request body data
class Item(BaseModel):
    scannedDocumentId: str


@app.get("/")
async def index():
    
    return {"message": "Welcome to reloaded"}

@app.post("/extract")
async def create_item(
    item: Item = Body(...),
):
    try:
        som_model = get_yolo_model(model_path='weights/icon_detect/best.pt')
        som_model.to(device)
        #caption_model_processor = get_caption_model_processor(model_name="blip2", model_name_or_path="weights/icon_caption_blip2", device=device)
        caption_model_processor = get_caption_model_processor(model_name="florence2", model_name_or_path="weights/icon_caption_florence", device=device,)
        
        scannedDocument = await prisma.patientscanneddocument.find_first_or_raise(where={"id":item.scannedDocumentId})
            
        cnt = 0
        image_url = scannedDocument.documentCollectionUrls[0].replace("storage.mobile.bolt3.local",STORAGE_HOST)
        response = requests.get(image_url)
        if response.status_code == 200:
            # Open the image from the response content
            image = Image.open(BytesIO(response.content))
            temp_image_path= ''
            # Save the image to a temporary file
            with tempfile.TemporaryDirectory() as tmpdirname:
                temp_image_path = f"{tmpdirname}/image.jpeg"
                print(temp_image_path)
                image.save(temp_image_path)
                # Now the image is saved in a temporary directory
                print(f"Image saved at {temp_image_path}")

                # You can perform additional operations on the image here if needed
                # image_path = 'imgs/windows_home.png'
                #image_path = 'imgs/windows_multitab.png'

                BOX_TRESHOLD = 0.03               
                box_overlay_ratio = image.size[0] / 3200
                draw_bbox_config = {
                    'text_scale': 0.8 * box_overlay_ratio,
                    'text_thickness': max(int(2 * box_overlay_ratio), 1),
                    'text_padding': max(int(3 * box_overlay_ratio), 1),
                    'thickness': max(int(3 * box_overlay_ratio), 1),
                }

                ocr_bbox_rslt, is_goal_filtered = check_ocr_box(temp_image_path, display_img = False, output_bb_format='xyxy', goal_filtering=None, easyocr_args={'paragraph': False, 'text_threshold':0.9}, use_paddleocr=True)
                text, ocr_bbox = ocr_bbox_rslt


                dino_labled_img, label_coordinates, parsed_content_list = get_som_labeled_img(temp_image_path, som_model, BOX_TRESHOLD = BOX_TRESHOLD, output_coord_in_ratio=False, ocr_bbox=ocr_bbox,draw_bbox_config=draw_bbox_config, caption_model_processor=caption_model_processor, ocr_text=text,use_local_semantics=True, iou_threshold=0.1, imgsz=640)


                property_value_array = list(map(lambda x: [x[0], x[1]], label_coordinates.items()))

                parsed : list[str, list[int]] = []
                for coordinate in property_value_array:
                    index, coord = coordinate

                    parsed.append([parsed_content_list[int(index)], coord.tolist()])
                    pass
                
                result = {
                    'image_size' : image.size,
                    'coordinates': parsed,
                    'text': parsed_content_list
                }
                await prisma.patientscanneddocument.update(where={'id':item.scannedDocumentId}, data={'extractedData': json.dumps(result)})

                torch.cuda.empty_cache()
                del som_model
                del caption_model_processor
                gc.collect()

                return {'message': 'OK'}
    
            
        else:
            print("Failed to download the image.")
            return {'message': 'NONE'}
        
        pass
    except Exception as e:
        print(e)
        return {'message': 'NONE'}
    




