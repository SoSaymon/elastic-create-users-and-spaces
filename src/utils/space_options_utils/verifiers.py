import re
from typing import List, Optional

SPACE_ID = str
SPACE_NAME = str
DESCRIPTION = Optional[str]
INITIALS = Optional[str]
COLOR = Optional[str]
DISABLED_FEATURES = Optional[List[str]]
IMAGE_URL = Optional[str]


def verify(value: Optional[str]) -> bool:
    """
    Verify the value
    :param value:  String value
    :return:  Boolean True if valid, False if invalid
    """
    if value:
        return True
    return False


def verify_space_id(space_id: SPACE_ID) -> bool:
    """
    Verify the space ID
    :param space_id:  String space ID
    :return:  Boolean True if valid, False if invalid
    """
    if space_id:
        pattern = r'^[a-z0-9_-]+$'
        if re.match(pattern, space_id):
            return True
    return False


def verify_initials_len(initials: INITIALS) -> bool:
    """
    Verify if the initials are between 1 and 2 characters
    :param initials:  String initials
    :return:  Boolean True if valid, False if invalid
    """
    if initials:
        if 1 <= len(initials) <= 2:
            return True
    return False


def verify_if_color_starts_with_hash(color: COLOR) -> bool:
    """
    Verify if the color starts with a hash
    :param color:  String color
    :return:  Boolean True if valid, False if invalid
    """
    if color.startswith('#'):
        return True
    return False


def verify_if_color_has_seven_characters(color: COLOR) -> bool:
    """
    Verify if the color has seven characters
    :param color:  String color
    :return:  Boolean True if valid, False if invalid
    """
    if len(color) == 7:
        return True
    return False


def verify_color_regex_pattern(color: COLOR) -> bool:
    """
    Verify the color regex pattern
    :param color:  String color
    :return:  Boolean True if valid, False if invalid
    """
    pattern = r'^#([A-Fa-f0-9]{6})$'
    if re.match(pattern, color):
        return True
    return False


def verify_if_space_exists_near_comma(value: str) -> bool:
    """
    Verify if the space exists after a comma in disabled features

    :param value:  String value
    :return:  Boolean True if valid, False if invalid
    """
    if re.search(r',\s', value) or re.search(r'\s,', value):
        return True
    return False


def verify_if_string_starts_with_comma(value: str) -> bool:
    """
    Verify if the string starts with a comma

    :param value:  String value
    :return:  Boolean True if valid, False if invalid
    """
    if value.startswith(','):
        return True
    return False


def verify_if_string_ends_with_comma(value: str) -> bool:
    """
    Verify if the string ends with a comma

    :param value:  String value
    :return:  Boolean True if valid, False if invalid
    """
    if value.endswith(','):
        return True
    return False


def verify_disabled_features_regex_pattern(disabled_features: str) -> bool:
    """
    Verify the disabled features regex pattern

    :param disabled_features:  String disabled features
    :return:  Boolean True if valid, False if invalid
    """
    pattern = r'^[a-zA-Z0-9_-]+(,[a-zA-Z0-9_-]+)*$'
    if re.match(pattern, disabled_features):
        return True
    return False


def verify_if_image_url_starts_with_data_image(image_url: IMAGE_URL) -> bool:
    """
    Verify if the image URL starts with data:image

    :param image_url:  String image URL
    :return:  Boolean True if valid, False if invalid
    """
    if image_url.startswith('data:image'):
        return True
    return False


def verify_if_image_url_has_image_type(image_url: IMAGE_URL) -> bool:
    """
    Verify if the image URL has an image type

    :param image_url:  String image URL
    :return:  Boolean True if valid, False if invalid
    """
    image_type_match = re.match(r"data:image/(\w+);", image_url)
    if image_type_match:
        return True
    return False


def verify_if_image_url_is_base64_encoded(image_url: IMAGE_URL) -> bool:
    """
    Verify if the image URL is base64 encoded

    :param image_url:  String image URL
    :return:  Boolean True if valid, False if invalid
    """
    if re.search(r"base64,", image_url):
        return True
    return False
