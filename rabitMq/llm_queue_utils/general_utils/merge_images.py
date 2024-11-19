from PIL import Image
from typing import List, Literal
import requests
from io import BytesIO


def merge_images(
    image_urls: List[str],
    direction: Literal["horizontal", "vertical"] = "horizontal",
) -> Image.Image:
    """
    Merges images fetched from URLs either horizontally or vertically, saves the result,
    and returns the merged image.

    Args:
        image_urls (List[str]): A list of URLs pointing to the images to merge.
        direction (Literal["horizontal", "vertical"]): The direction to merge the images.

    Returns:
        Image.Image: The merged PIL image.
    """
    # Download images from URLs
    images = []
    for url in image_urls:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP issues
        images.append(Image.open(BytesIO(response.content)))

    # Merge the images
    if direction == "horizontal":
        total_width = sum(img.width for img in images)
        max_height = max(img.height for img in images)
        merged_image = Image.new("RGB", (total_width, max_height))

        x_offset = 0
        for img in images:
            merged_image.paste(img, (x_offset, 0))
            x_offset += img.width
    elif direction == "vertical":
        total_height = sum(img.height for img in images)
        max_width = max(img.width for img in images)
        merged_image = Image.new("RGB", (max_width, total_height))

        y_offset = 0
        for img in images:
            merged_image.paste(img, (0, y_offset))
            y_offset += img.height

    # Return the merged image
    return merged_image
