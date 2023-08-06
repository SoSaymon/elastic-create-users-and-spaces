import re
from typing import Optional

IMAGE_URL = Optional[str]


def get_image_url_image_type(image_url: IMAGE_URL) -> Optional[str]:
    """
    Get the image URL image type

    :param image_url:  String image URL
    :return:  String image type
    """
    image_type_match = re.match(r"data:image/(\w+);", image_url)
    if image_type_match:
        return image_type_match.group(1)
    return None


def get_input(prompt: str) -> str:
    """
    Get user input.

    :param prompt:  String prompt
    :return:  String user input
    """
    return input(prompt)
